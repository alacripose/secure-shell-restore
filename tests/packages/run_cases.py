"""Exit tests for the canonical package identity contract (R4).

Run: python tests/packages/run_cases.py — prints one line per case and a final count,
exit 1 if any case fails. These are the fixtures the plan's R4 exit condition names:
independent reader and writer agree, and tampered, truncated, ambiguous and
foreign-revision inputs refuse by name.
"""

from __future__ import annotations

import json
import subprocess
import sys
import traceback
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from impl.packages import identity as idn  # noqa: E402

HASH = "a" * 64
HASH_B = "b" * 64

CASES: list = []


def case(function):
    CASES.append(function)
    return function


def refused(refusal: str, call, *arguments) -> None:
    try:
        call(*arguments)
    except idn.Refused as error:
        assert error.refusal == refusal, f"refused {error.refusal}, expected {refusal}"
        assert error.subject, "a refusal must carry a subject"
        assert error.reason, "a refusal must carry a reason"
        return
    raise AssertionError(f"expected refusal {refusal}, got a value")


@case
def canonical_name_parses():
    parsed = idn.parse_identity(f"secure-shell-store@1+blake3:{HASH}")
    assert parsed["state"] == "held"
    assert (parsed["name"], parsed["revision"], parsed["hash"]) == ("secure-shell-store", 1, HASH)
    assert parsed["dependencies"] == [] and parsed["pin_complete"] is False


@case
def pin_complete_name_parses_in_order():
    text = f"secure-shell-store@1+blake3:{HASH}(secure-shell-openlock-shell@3+blake3:{HASH_B})"
    parsed = idn.parse_identity(text)
    assert parsed["pin_complete"] is True
    assert [dependency["name"] for dependency in parsed["dependencies"]] == ["secure-shell-openlock-shell"]


@case
def uppercase_name_is_refused():
    refused("name-invalid", idn.parse_identity, f"Secure-Shell@1+blake3:{HASH}")


@case
def underscore_name_is_refused():
    refused("name-invalid", idn.parse_identity, f"secure_shell@1+blake3:{HASH}")


@case
def revision_zero_is_refused():
    refused("revision-invalid", idn.parse_identity, f"secure-shell@0+blake3:{HASH}")


@case
def revision_with_leading_zero_is_refused():
    refused("revision-invalid", idn.parse_identity, f"secure-shell@01+blake3:{HASH}")


@case
def revision_that_is_not_an_integer_is_refused():
    refused("revision-invalid", idn.parse_identity, f"secure-shell@1.2.3+blake3:{HASH}")


@case
def uppercase_hash_is_refused():
    refused("hash-invalid", idn.parse_identity, "secure-shell@1+blake3:" + "A" * 64)


@case
def truncated_hash_is_refused():
    refused("hash-invalid", idn.parse_identity, f"secure-shell@1+blake3:{HASH[:63]}")


@case
def foreign_algorithm_is_refused():
    refused("algorithm-unsupported", idn.parse_identity, f"secure-shell@1+sha256:{HASH}")


@case
def padded_identity_is_refused():
    refused("identity-malformed", idn.parse_identity, f" secure-shell@1+blake3:{HASH}")


@case
def duplicate_dependencies_are_refused():
    dependency = f"dep@1+blake3:{HASH}"
    refused(
        "dependency-duplicate",
        idn.parse_identity,
        f"secure-shell@1+blake3:{HASH}({dependency},{dependency})",
    )


@case
def unordered_dependencies_are_refused():
    refused(
        "dependency-unordered",
        idn.parse_identity,
        f"secure-shell@1+blake3:{HASH}(z-dep@1+blake3:{HASH},a-dep@1+blake3:{HASH_B})",
    )


@case
def nested_dependency_sets_are_refused():
    inner = f"inner@1+blake3:{HASH_B}"
    refused(
        "dependency-malformed",
        idn.parse_identity,
        f"secure-shell@1+blake3:{HASH}(outer@1+blake3:{HASH}({inner}))",
    )


@case
def empty_dependency_set_is_refused():
    refused("dependency-malformed", idn.parse_identity, f"secure-shell@1+blake3:{HASH}()")


@case
def format_then_parse_round_trips():
    built = idn.format_identity("secure-shell-store", 2, HASH)
    assert built == f"secure-shell-store@2+blake3:{HASH}"
    assert idn.parse_identity(built)["identity"] == built


@case
def format_orders_dependencies_by_name():
    built = idn.format_identity(
        "secure-shell-store",
        1,
        HASH,
        [f"z-dep@1+blake3:{HASH}", f"a-dep@1+blake3:{HASH_B}"],
    )
    assert built.endswith(f"(a-dep@1+blake3:{HASH_B},z-dep@1+blake3:{HASH})"), built
    assert idn.parse_identity(built)["pin_complete"] is True


@case
def format_refuses_a_duplicate_dependency():
    dependency = f"dep@1+blake3:{HASH}"
    refused("dependency-duplicate", idn.format_identity, "secure-shell-store", 1, HASH, [dependency, dependency])


@case
def serialization_is_deterministic_across_key_order():
    left = idn.canonical_bytes({"b": 1, "a": 2})
    right = idn.canonical_bytes({"a": 2, "b": 1})
    assert left == right == b'{"a":2,"b":1}'


@case
def digest_is_stable_across_key_order():
    first = idn.package_digest({"name": "secure-shell-store", "revision": 1}, b"payload")
    second = idn.package_digest({"revision": 1, "name": "secure-shell-store"}, b"payload")
    assert first == second, (first, second)


@case
def digest_changes_with_payload_and_with_content():
    base = idn.package_digest({"name": "secure-shell-store"}, b"one")
    assert base != idn.package_digest({"name": "secure-shell-store"}, b"two")
    assert base != idn.package_digest({"name": "secure-shell-store", "extra": True}, b"one")


@case
def digest_ignores_signature_and_timestamps():
    """R-C: re-signing or re-encrypting the same content must not move identity."""
    base = idn.package_digest({"name": "secure-shell-store"}, b"content")
    resigned = idn.package_digest(
        {
            "name": "secure-shell-store",
            "signature": "ed25519:deadbeef",
            "signature_algorithm": "ed25519",
            "received_at": "2026-11-04T00:00:00Z",
            "nonce": "0011223344556677",
        },
        b"content",
    )
    assert base == resigned, (base, resigned)


@case
def revision_bumps_are_monotonic():
    assert idn.next_revision([]) == 1
    assert idn.next_revision([1, 3, 2]) == 4
    refused("revision-invalid", idn.next_revision, [0])


@case
def cli_parse_holds_and_refuses_with_exit_status():
    held = subprocess.run(
        [sys.executable, "-m", "impl.packages.identity", "parse", f"secure-shell-store@1+blake3:{HASH}"],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert held.returncode == 0, held.stderr
    assert json.loads(held.stdout)["state"] == "held"

    rejected = subprocess.run(
        [sys.executable, "-m", "impl.packages.identity", "parse", "secure-shell@0+blake3:" + HASH],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert rejected.returncode == 1, rejected.returncode
    body = json.loads(rejected.stdout)
    assert body["state"] == "refused" and body["refusal"] == "revision-invalid", body


@case
def cli_digest_matches_the_module():
    path = ROOT / "tests" / "packages" / "fixture.txt"
    path.write_bytes(b"secure shell restore\n")
    result = subprocess.run(
        [sys.executable, "-m", "impl.packages.identity", "digest", str(path)],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stderr
    from blake3 import blake3

    assert json.loads(result.stdout)["digest"] == "blake3:" + blake3(b"secure shell restore\n").hexdigest()
    path.unlink()


@case
def every_refusal_name_fits_the_family_schema():
    assert len(idn.REFUSALS) == len(set(idn.REFUSALS))
    for name in idn.REFUSALS:
        assert idn.NAME.match(name), name


def main() -> int:
    failures = 0
    for function in CASES:
        try:
            function()
        except Exception:  # noqa: BLE001 - a failing case is reported, never swallowed
            failures += 1
            detail = traceback.format_exc(limit=1).strip().splitlines()[-1]
            print(f"FAIL {function.__name__}: {detail}")
        else:
            print(f"ok   {function.__name__}")
    print(f"\n{len(CASES)} cases, {failures} failed")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
