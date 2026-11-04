"""Exit tests for the declared package object: schema ids, manifest vocabulary, chunk domains.

Run: python tests/packages/run_cases_canonical.py

The R-C properties are asserted here rather than assumed: re-signing and re-chunking must not
move identity, a changed content byte must, and a chunked digest must equal the unchunked one.
"""

from __future__ import annotations

import json
import subprocess
import sys
import traceback
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from impl.packages import canonical as cn  # noqa: E402
from impl.packages import identity as idn  # noqa: E402

HASH_A = "a" * 64
HASH_B = "b" * 64

CASES: list = []


def case(function):
    CASES.append(function)
    return function


def refused(refusal: str, call, *arguments, **keywords) -> None:
    try:
        call(*arguments, **keywords)
    except idn.Refused as error:
        assert error.refusal == refusal, f"refused {error.refusal}, expected {refusal}"
        assert error.subject, "a refusal must carry a subject"
        assert error.reason, "a refusal must carry a reason"
        return
    raise AssertionError(f"expected refusal {refusal}, got a value")


def manifest(**overrides):
    base = {
        "name": "secure-shell-store",
        "revision": 1,
        "schemas": ["secure-shell.package/1", "secure-shell.stream/1"],
        "dependencies": [f"secure-shell-openlock-shell@3+blake3:{HASH_A}"],
        "entry_points": ["bin/store", "lib/store.mjs"],
        "lengths": {"manifest": 128, "payload": 4096},
    }
    base.update(overrides)
    return base


@case
def schema_id_parses_family_and_version():
    parsed = cn.parse_schema_id("secure-shell.stream/1")
    assert parsed["family"] == "secure-shell.stream" and parsed["version"] == 1
    assert cn.parse_schema_id("surface.mount/2")["version"] == 2


@case
def schema_id_rejects_version_zero():
    refused("schema-id-invalid", cn.parse_schema_id, "secure-shell.stream/0")


@case
def schema_id_rejects_leading_zero_version():
    refused("schema-id-invalid", cn.parse_schema_id, "secure-shell.stream/01")


@case
def schema_id_rejects_uppercase_family():
    refused("schema-id-invalid", cn.parse_schema_id, "Secure-Shell.stream/1")


@case
def schema_id_rejects_missing_version():
    refused("schema-id-invalid", cn.parse_schema_id, "secure-shell.stream")


@case
def schema_id_rejects_empty_family():
    refused("schema-id-invalid", cn.parse_schema_id, "/1")


@case
def schema_set_must_be_ordered():
    refused("schema-unordered", cn.schema_ids, ["secure-shell.stream/1", "secure-shell.package/1"])


@case
def schema_set_refuses_duplicates():
    refused(
        "schema-duplicate",
        cn.schema_ids,
        ["secure-shell.package/1", "secure-shell.package/1"],
    )


@case
def manifest_requires_every_declared_field():
    incomplete = manifest()
    del incomplete["schemas"]
    refused("manifest-field-missing", cn.validate_manifest, incomplete)


@case
def manifest_refuses_a_key_outside_the_vocabulary():
    refused("manifest-key-unknown", cn.validate_manifest, manifest(extra="surprise"))


@case
def manifest_refuses_unordered_dependencies():
    refused(
        "dependency-unordered",
        cn.validate_manifest,
        manifest(
            dependencies=[
                f"z-dep@1+blake3:{HASH_A}",
                f"a-dep@1+blake3:{HASH_B}",
            ]
        ),
    )


@case
def manifest_refuses_a_negative_length():
    refused("length-invalid", cn.validate_manifest, manifest(lengths={"payload": -1}))


@case
def manifest_refuses_an_unordered_entry_point_set():
    refused("entry-point-invalid", cn.validate_manifest, manifest(entry_points=["b", "a"]))


@case
def manifest_refuses_a_bad_entry_point_name():
    refused("entry-point-invalid", cn.validate_manifest, manifest(entry_points=["bad entry"]))


@case
def declared_manifest_digest_matches_identity_digest():
    """Wired, not parallel: the declared shape must hash to the identity module's digest."""
    value = manifest()
    assert cn.package_digest(value, b"payload") == idn.package_digest(value, b"payload")


@case
def chunked_digest_equals_unchunked_across_sizes():
    value = manifest()
    payload = bytes(range(256)) * 40
    unchunked = cn.package_digest(value, payload)
    for size in (1, 7, 4096, 65536, cn.CHUNK_DEFAULT):
        assert cn.chunked_package_digest(value, payload, size) == unchunked, size
    assert idn.package_digest(value, payload) == unchunked


@case
def changed_content_byte_moves_the_chunked_digest():
    value = manifest()
    left = cn.chunked_package_digest(value, b"content", 16)
    right = cn.chunked_package_digest(value, b"contenT", 16)
    assert left != right


@case
def re_signing_and_timestamps_do_not_move_the_declared_digest():
    base = cn.package_digest(manifest(), b"content")
    resigned = cn.package_digest(
        manifest(
            signature="ed25519:deadbeef",
            signature_algorithm="ed25519",
            received_at="2026-11-04T00:00:00Z",
            nonce="0011223344556677",
        ),
        b"content",
    )
    assert base == resigned, (base, resigned)


@case
def a_manifest_field_change_moves_the_digest():
    base = cn.package_digest(manifest(), b"content")
    assert base != cn.package_digest(manifest(revision=2), b"content")
    assert base != cn.package_digest(manifest(lengths={"payload": 4097}), b"content")


@case
def chunk_digests_are_domain_separated():
    data = b"the same bytes"
    assert cn.chunk_digest("payload", 0, data) != cn.chunk_digest("manifest", 0, data)


@case
def chunk_digests_are_index_separated():
    data = b"the same bytes"
    assert cn.chunk_digest("payload", 0, data) != cn.chunk_digest("payload", 1, data)


@case
def chunk_domain_refuses_an_unknown_role():
    refused("chunk-domain-invalid", cn.chunk_domain, "secrets")
    assert cn.chunk_domain("payload") == "secure-shell.chunk/1/payload"


@case
def chunked_content_reassembles_to_the_preimage():
    value = manifest()
    payload = b"0123456789" * 50
    preimage = cn.content_bytes(value, payload)
    chunks = cn.chunk_manifest(preimage, 37)
    assert len(chunks) > 1
    assert sum(chunk["length"] for chunk in chunks) == len(preimage)
    assert cn.reassemble([(chunk["index"], preimage[chunk["offset"] : chunk["offset"] + chunk["length"]]) for chunk in chunks]) == preimage


@case
def reassembly_refuses_a_gap():
    refused("chunk-sequence-invalid", cn.reassemble, [(0, b"a"), (2, b"c")])


@case
def chunk_size_is_bounded():
    for size in (0, -1, cn.CHUNK_MAX + 1):
        refused("chunk-size-invalid", cn.chunk_manifest, b"x", size)


@case
def cli_manifest_holds_and_refuses_with_exit_status():
    path = ROOT / "tests" / "packages" / "fixture-manifest.json"
    path.write_text(json.dumps(manifest()), encoding="utf-8")
    held = subprocess.run(
        [sys.executable, "-m", "impl.packages.canonical", "manifest", str(path)],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert held.returncode == 0, held.stdout + held.stderr
    body = json.loads(held.stdout)
    assert body["state"] == "held" and body["digest"].startswith("blake3:")
    path.unlink()

    bad = ROOT / "tests" / "packages" / "fixture-bad-schema.json"
    bad.write_text(json.dumps(manifest(schemas=["secure-shell.stream/0"])), encoding="utf-8")
    rejected = subprocess.run(
        [sys.executable, "-m", "impl.packages.canonical", "manifest", str(bad)],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert rejected.returncode == 1, rejected.returncode
    assert json.loads(rejected.stdout)["refusal"] == "schema-id-invalid"
    bad.unlink()


@case
def every_refusal_name_fits_the_family_schema():
    assert len(cn.REFUSALS) == len(set(cn.REFUSALS))
    for name in cn.REFUSALS:
        assert cn.NAME.match(name), name


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
