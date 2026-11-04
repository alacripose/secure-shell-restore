"""Exit tests for the package stream: ordering, truncation, corruption and atomic adoption.

Run: python tests/packages/run_cases_stream.py

The atomicity cases are the point: for every fault, the receiver's prior state must be byte
for byte what it was before the attempt.
"""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import traceback
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from impl.packages import canonical as cn  # noqa: E402
from impl.packages import identity as idn  # noqa: E402
from impl.packages import stream as st  # noqa: E402

HASH_A = "a" * 64
PAYLOAD = bytes(range(256)) * 20  # spans several 1 KiB chunks

CASES: list = []


def case(function):
    CASES.append(function)
    return function


def refused(refusal: str, call, *arguments, **keywords) -> None:
    try:
        call(*arguments, **keywords)
    except idn.Refused as error:
        assert error.refusal == refusal, f"refused {error.refusal}, expected {refusal}"
        assert error.subject and error.reason, "a refusal carries a subject and a reason"
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


def built(chunk_size: int = 1024):
    return st.frame_content(manifest(), PAYLOAD, chunk_size)


def fault_drop(wire):
    return wire[:-1]


def fault_swap(wire):
    wire = list(wire)
    wire[0], wire[1] = wire[1], wire[0]
    return wire


def fault_duplicate(wire):
    return list(wire) + [wire[0]]


def fault_torn(wire):
    return [{**wire[0], "data": wire[0]["data"][:-1]}] + list(wire[1:])


def fault_corrupt(wire):
    return [{**wire[0], "data": bytes([wire[0]["data"][0] ^ 0xFF]) + wire[0]["data"][1:]}] + list(wire[1:])


def fault_offset(wire):
    return [{**wire[0], "offset": wire[0]["offset"] + 1}] + list(wire[1:])


def fault_oversized(wire):
    first = wire[0]
    data = first["data"] + b"x" * (first["length"] + 1)
    return [{**first, "length": len(data), "data": data}] + list(wire[1:])


def fault_zero_length(wire):
    return [{**wire[0], "length": 0, "data": b""}] + list(wire[1:])


@case
def chunks_are_contiguous_and_bounded():
    header, wire = built(1024)
    assert header["chunk_count"] == len(wire) > 1
    offset = 0
    for position, chunk in enumerate(header["chunks"]):
        assert chunk["index"] == position and chunk["offset"] == offset
        assert 0 < chunk["length"] <= 1024
        offset += chunk["length"]
    assert offset == header["total_length"] == len(cn.content_bytes(manifest(), PAYLOAD))


@case
def chunks_reuse_the_shipped_payload_domain():
    header, wire = built(1024)
    assert header["chunks"][0]["domain"] == cn.chunk_domain("payload")
    assert header["chunks"][0]["digest"] == cn.chunk_digest("payload", 0, wire[0]["data"])


@case
def stream_digest_equals_the_canonical_digest():
    header, _wire = built(1024)
    assert header["digest"] == cn.package_digest(manifest(), PAYLOAD)
    assert header["digest"] == cn.chunked_package_digest(manifest(), PAYLOAD, 1024)


@case
def stream_digest_is_independent_of_chunk_size():
    digests = {st.package_stream(manifest(), PAYLOAD, size)["digest"] for size in (1, 7, 1024, 65536)}
    assert len(digests) == 1 and digests.pop() == cn.package_digest(manifest(), PAYLOAD)


@case
def a_complete_stream_is_adopted():
    header, wire = built(1024)
    receiver = st.Receiver(prior=b"previous-revision", prior_digest="blake3:old")
    result = receiver.adopt(header, wire)
    assert result["state"] == "held"
    assert receiver.state == cn.content_bytes(manifest(), PAYLOAD)
    assert receiver.digest == cn.package_digest(manifest(), PAYLOAD)
    assert receiver.adoptions == 1


@case
def a_package_with_an_empty_payload_still_streams():
    """The manifest is content: an empty payload does not make an empty stream."""
    empty = manifest(lengths={"manifest": 0, "payload": 0}, dependencies=[])
    header, wire = st.frame_content(empty, b"", 1024)
    assert header["segments"][1]["length"] == 0
    assert header["chunk_count"] == len(wire) >= 1
    receiver = st.Receiver(prior=None)
    result = receiver.adopt(header, wire)
    assert result["state"] == "held"
    assert receiver.state == cn.content_bytes(empty, b"")
    assert result["digest"] == cn.package_digest(empty, b"")


@case
def adopting_the_same_stream_twice_is_idempotent():
    header, wire = built(1024)
    receiver = st.Receiver(prior=b"old")
    first = receiver.adopt(header, wire)
    second = receiver.adopt(header, list(wire))
    assert first["digest"] == second["digest"] and receiver.adoptions == 2


@case
def out_of_order_chunks_are_refused():
    header, wire = built(1024)
    refused("chunk-out-of-order", st.Receiver().adopt, header, fault_swap(wire))


@case
def duplicate_chunks_are_refused():
    header, wire = built(1024)
    refused("chunk-duplicate", st.Receiver().adopt, header, fault_duplicate(wire))


@case
def a_displaced_chunk_is_refused():
    header, wire = built(1024)
    refused("chunk-out-of-range", st.Receiver().adopt, header, fault_offset(wire))


@case
def an_oversized_chunk_is_refused():
    header, wire = built(1024)
    refused("chunk-oversized", st.Receiver().adopt, header, fault_oversized(wire))


@case
def a_zero_length_chunk_is_refused():
    header, wire = built(1024)
    refused("chunk-length-invalid", st.Receiver().adopt, header, fault_zero_length(wire))


@case
def a_negative_length_chunk_is_refused():
    header, wire = built(1024)
    refused("chunk-length-invalid", st.Receiver().adopt, header, [{**wire[0], "length": -1}] + list(wire[1:]))


@case
def a_missing_chunk_is_truncation():
    header, wire = built(1024)
    refused("stream-truncated", st.Receiver().adopt, header, fault_drop(wire))


@case
def a_short_frame_is_torn():
    header, wire = built(1024)
    refused("stream-torn", st.Receiver().adopt, header, fault_torn(wire))


@case
def a_flipped_byte_is_corruption():
    header, wire = built(1024)
    refused("stream-corrupt", st.Receiver().adopt, header, fault_corrupt(wire))


@case
def a_rewritten_header_digest_is_refused():
    header, wire = built(1024)
    tampered = {**header, "digest": "blake3:" + "0" * 64}
    refused("stream-digest-mismatch", st.Receiver().adopt, tampered, wire)


@case
def a_foreign_stream_schema_is_refused():
    header, wire = built(1024)
    refused("stream-header-invalid", st.Receiver().adopt, {**header, "schema": "secure-shell.served/1"}, wire)


@case
def a_chunk_count_that_disagrees_with_the_list_is_refused():
    header, wire = built(1024)
    refused("stream-chunk-count-invalid", st.Receiver().adopt, {**header, "chunk_count": header["chunk_count"] + 1}, wire)


@case
def a_segment_that_does_not_sum_to_the_total_is_refused():
    header, wire = built(1024)
    segments = [dict(header["segments"][0]), dict(header["segments"][1])]
    segments[1]["length"] += 1
    refused("stream-segment-invalid", st.Receiver().adopt, {**header, "segments": segments}, wire)


@case
def a_bad_chunk_size_is_refused():
    header, wire = built(1024)
    refused("chunk-size-invalid", st.Receiver().adopt, {**header, "chunk_size": 0}, wire)


@case
def every_fault_leaves_the_prior_state_untouched():
    """Atomic adoption: the only observable outcomes are the prior state or the whole package."""
    header, wire = built(1024)
    prior = b"previously admitted desktop"
    faults = {
        "drop": fault_drop,
        "swap": fault_swap,
        "duplicate": fault_duplicate,
        "torn": fault_torn,
        "corrupt": fault_corrupt,
        "offset": fault_offset,
        "oversized": fault_oversized,
        "zero-length": fault_zero_length,
    }
    for name, build in faults.items():
        receiver = st.Receiver(prior=prior, prior_digest="blake3:prior")
        try:
            receiver.adopt(header, build(wire))
        except idn.Refused:
            pass
        else:
            raise AssertionError(f"{name}: a faulty stream was adopted")
        assert receiver.state == prior, f"{name}: prior state changed"
        assert receiver.digest == "blake3:prior", f"{name}: prior digest changed"
        assert receiver.adoptions == 0, f"{name}: adoption was counted"


@case
def cli_refusals_exit_non_zero_with_the_prior_intact():
    workdir = Path(tempfile.mkdtemp(prefix="stream-cli-"))
    manifest_path = workdir / "manifest.json"
    payload_path = workdir / "payload.bin"
    manifest_path.write_text(json.dumps(manifest()), encoding="utf-8")
    payload_path.write_bytes(PAYLOAD)

    def run(*extra):
        return subprocess.run(
            [
                sys.executable,
                "-m",
                "impl.packages.stream",
                "receive",
                "--manifest",
                str(manifest_path),
                "--payload",
                str(payload_path),
                "--chunk-size",
                "1024",
                "--prior",
                "prior-desktop",
                *extra,
            ],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )

    held = run()
    assert held.returncode == 0, held.stdout + held.stderr
    assert json.loads(held.stdout)["state"] == "held"

    for extra, expected in (
        (("--swap", "0", "1"), "chunk-out-of-order"),
        (("--corrupt", "0"), "stream-corrupt"),
        (("--truncate", "1"), "stream-torn"),
    ):
        result = run(*extra)
        assert result.returncode == 1, (extra, result.returncode)
        body = json.loads(result.stdout)
        assert body["refusal"] == expected, (extra, body)
        assert body["prior_unchanged"] is True, (extra, body)

    truncated = run("--drop", str(st.package_stream(manifest(), PAYLOAD, 1024)["chunk_count"] - 1))
    assert truncated.returncode == 1 and json.loads(truncated.stdout)["refusal"] == "stream-truncated"

    # A fault selector naming a chunk that does not exist must refuse, never no-op into a
    # clean adoption: the single-chunk stream is exactly where that bug would hide.
    single = subprocess.run(
        [
            sys.executable,
            "-m",
            "impl.packages.stream",
            "receive",
            "--manifest",
            str(manifest_path),
            "--payload",
            str(payload_path),
            "--chunk-size",
            "1048576",
            "--prior",
            "prior-desktop",
            "--corrupt",
            "1",
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert single.returncode == 1, single.stdout
    body = json.loads(single.stdout)
    assert body["refusal"] == "fault-target-invalid", body
    assert body["prior_unchanged"] is True, body


@case
def every_refusal_name_fits_the_family_schema():
    assert len(st.REFUSALS) == len(set(st.REFUSALS))
    for name in st.REFUSALS:
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
