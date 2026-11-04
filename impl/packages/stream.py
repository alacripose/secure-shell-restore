"""Secure Shell Restore — the package stream (`secure-shell.stream/1`).

A package travels as an explicitly ordered sequence of bounded chunks over the domains
`canonical.py` already declares. Nothing here invents a second vocabulary: a chunk digest is
`canonical.chunk_digest("payload", index, data)` and the package digest is
`canonical.package_digest`, so a streamed package and a locally read package are the same
package or a refusal.

Adoption is atomic. `Receiver.adopt` builds the candidate in a private buffer and assigns it
to `state` only after the count, the total length and the whole-content digest all agree. Every
failure leaves the receiver exactly as it was, which is the property the restore depends on: a
torn stream can never leave half a desktop admitted.

What this does not do, stated rather than implied: the digest proves byte identity and ordering
only. There is no signature and no admission verdict here — the Debian signing authority is not
reachable from this machine, so authorship and authenticity remain R5's unsolved problem.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Iterable, Iterator

from blake3 import blake3

from impl.packages import canonical as cn
from impl.packages.identity import HASH, Refused

STREAM_SCHEMA = "secure-shell.stream/1"
DOMAIN = cn.DOMAIN  # one preimage, one domain, one digest

REFUSALS = (
    "chunk-duplicate",
    "chunk-length-invalid",
    "chunk-out-of-order",
    "chunk-out-of-range",
    "chunk-oversized",
    "chunk-size-invalid",
    "fault-target-invalid",
    "stream-chunk-count-invalid",
    "stream-corrupt",
    "stream-digest-mismatch",
    "stream-header-invalid",
    "stream-length-mismatch",
    "stream-segment-invalid",
    "stream-torn",
    "stream-truncated",
)


def _refuse(refusal: str, subject: Any, reason: str) -> None:
    assert refusal in REFUSALS, refusal
    raise Refused(refusal, subject if isinstance(subject, str) else repr(subject), reason)


def _subject(value: Any, limit: int = 96) -> str:
    text = value if isinstance(value, str) else repr(value)
    return text if len(text) <= limit else text[:limit] + "…"


def package_stream(manifest: Any, payload: bytes = b"", chunk_size: int = cn.CHUNK_DEFAULT) -> dict[str, Any]:
    """Frame a package. The header is what a receiver needs; the chunks carry the bytes."""
    cn.validate_manifest(manifest)
    content = cn.content_bytes(manifest, payload)
    chunks = cn.chunk_manifest(content, chunk_size, "payload")
    return {
        "schema": STREAM_SCHEMA,
        "state": "held",
        "digest": cn.package_digest(manifest, payload),
        "total_length": len(content),
        "chunk_size": chunk_size,
        "chunk_count": len(chunks),
        "segments": [
            {"role": "manifest", "length": len(cn.canonical_bytes({k: v for k, v in manifest.items() if k not in cn.EXCLUDED}))},
            {"role": "payload", "length": len(bytes(payload))},
        ],
        "chunks": [{key: entry[key] for key in ("index", "offset", "length", "domain", "digest")} for entry in chunks],
    }


def frames(header: dict[str, Any], content: bytes) -> Iterator[dict[str, Any]]:
    """The wire frames for a built stream: each chunk's declared shape plus its bytes."""
    for chunk in header["chunks"]:
        offset = chunk["offset"]
        yield {**chunk, "data": content[offset : offset + chunk["length"]]}


def frame_content(manifest: Any, payload: bytes = b"", chunk_size: int = cn.CHUNK_DEFAULT) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    header = package_stream(manifest, payload, chunk_size)
    return header, list(frames(header, cn.content_bytes(manifest, payload)))


def check_header(header: Any) -> dict[str, Any]:
    """Everything a receiver can know before it accepts a single byte."""
    if not isinstance(header, dict):
        _refuse("stream-header-invalid", _subject(header), "stream header must be an object")
    if header.get("schema") != STREAM_SCHEMA:
        _refuse(
            "stream-header-invalid",
            _subject(header.get("schema")),
            f"found {header.get('schema')!r}, supported {STREAM_SCHEMA!r}",
        )

    digest = header.get("digest")
    if not isinstance(digest, str) or not digest.startswith("blake3:") or not HASH.match(digest[len("blake3:"):]):
        _refuse("stream-header-invalid", _subject(digest), "header digest must be blake3:<64 lowercase hex>")

    total = header.get("total_length")
    if isinstance(total, bool) or not isinstance(total, int) or total < 0:
        _refuse("stream-header-invalid", _subject(total), "total_length must be a non-negative integer")

    chunk_size = header.get("chunk_size")
    if isinstance(chunk_size, bool) or not isinstance(chunk_size, int) or chunk_size < 1:
        _refuse("chunk-size-invalid", _subject(chunk_size), "chunk size must be a positive integer")
    if chunk_size > cn.CHUNK_MAX:
        _refuse("chunk-size-invalid", str(chunk_size), f"chunk size must not exceed {cn.CHUNK_MAX} bytes")

    segments = header.get("segments")
    if not isinstance(segments, list) or not segments:
        _refuse("stream-segment-invalid", _subject(segments), "a stream declares its segments")
    declared = 0
    for segment in segments:
        if not isinstance(segment, dict) or segment.get("role") not in ("manifest", "payload"):
            _refuse("stream-segment-invalid", _subject(segment), "segment role must be manifest or payload")
        length = segment.get("length")
        if isinstance(length, bool) or not isinstance(length, int) or length < 0:
            _refuse("stream-segment-invalid", _subject(segment), "segment length must be a non-negative integer")
        declared += length
    if declared != total:
        _refuse("stream-segment-invalid", str(declared), f"segments declare {declared} bytes, header says {total}")

    count = header.get("chunk_count")
    chunks = header.get("chunks")
    if isinstance(count, bool) or not isinstance(count, int) or count < 0 or not isinstance(chunks, list):
        _refuse("stream-chunk-count-invalid", _subject(count), "chunk_count must be a non-negative integer")
    if len(chunks) != count:
        _refuse("stream-chunk-count-invalid", str(len(chunks)), f"header declares {count} chunks, lists {len(chunks)}")

    offset = 0
    for position, chunk in enumerate(chunks):
        if not isinstance(chunk, dict):
            _refuse("stream-header-invalid", _subject(chunk), "chunk declaration must be an object")
        if chunk.get("index") != position:
            _refuse("chunk-out-of-order", _subject(chunk.get("index")), f"chunk declared at position {position} claims index {chunk.get('index')}")
        if chunk.get("offset") != offset:
            _refuse("chunk-out-of-range", _subject(chunk.get("offset")), f"chunk {position} starts at {chunk.get('offset')}, expected {offset}")
        length = chunk.get("length")
        if isinstance(length, bool) or not isinstance(length, int) or length <= 0:
            _refuse("chunk-length-invalid", _subject(length), f"chunk {position} length must be a positive integer")
        if length > chunk_size:
            _refuse("chunk-oversized", _subject(length), f"chunk {position} is larger than the declared chunk size {chunk_size}")
        if chunk.get("domain") != cn.chunk_domain("payload"):
            _refuse("stream-header-invalid", _subject(chunk.get("domain")), "chunk domain must be the shipped payload domain")
        offset += length
    if offset != total:
        _refuse("stream-length-mismatch", str(offset), f"chunks cover {offset} bytes, header says {total}")
    return header


class Receiver:
    """A recipient with prior state. `state` changes only when a whole package verifies."""

    def __init__(self, prior: bytes | None = None, prior_digest: str | None = None) -> None:
        self.state = prior
        self.digest = prior_digest
        self.adoptions = 0
        self.attempts = 0

    def adopt(self, header: Any, frames_in: Iterable[dict[str, Any]]) -> dict[str, Any]:
        self.attempts += 1
        check_header(header)

        pending = bytearray()
        seen: set[int] = set()
        expected = 0
        for frame in frames_in:
            index = frame.get("index")
            if isinstance(index, bool) or not isinstance(index, int) or index < 0:
                _refuse("chunk-out-of-range", _subject(index), "chunk index must be a non-negative integer")
            if index in seen:
                _refuse("chunk-duplicate", str(index), f"chunk {index} arrived more than once")
            if index != expected:
                _refuse("chunk-out-of-order", str(index), f"expected chunk {expected}, received {index}")
            if index >= header["chunk_count"]:
                _refuse("chunk-out-of-range", str(index), f"chunk {index} is beyond the declared count {header['chunk_count']}")

            length = frame.get("length")
            if isinstance(length, bool) or not isinstance(length, int) or length <= 0:
                _refuse("chunk-length-invalid", _subject(length), f"chunk {index} length must be a positive integer")
            if length > header["chunk_size"]:
                _refuse("chunk-oversized", _subject(length), f"chunk {index} exceeds the declared chunk size {header['chunk_size']}")

            data = frame.get("data")
            if not isinstance(data, (bytes, bytearray)):
                _refuse("stream-header-invalid", _subject(type(data)), f"chunk {index} carries no bytes")
            if len(data) != length:
                _refuse("stream-torn", str(index), f"chunk {index} declared {length} bytes, carried {len(data)}")

            if frame.get("offset") != len(pending):
                _refuse("chunk-out-of-range", _subject(frame.get("offset")), f"chunk {index} starts at {frame.get('offset')}, expected {len(pending)}")
            if len(pending) + length > header["total_length"]:
                _refuse("chunk-out-of-range", str(len(pending) + length), f"chunk {index} overruns the declared length {header['total_length']}")

            declared_digest = frame.get("digest")
            if cn.chunk_digest("payload", index, bytes(data)) != declared_digest:
                _refuse("stream-corrupt", str(index), f"chunk {index} does not match its declared digest")

            pending.extend(data)
            seen.add(index)
            expected += 1

        if expected != header["chunk_count"]:
            _refuse(
                "stream-truncated",
                str(expected),
                f"received {expected} of {header['chunk_count']} chunks",
            )
        if len(pending) != header["total_length"]:
            _refuse("stream-length-mismatch", str(len(pending)), f"received {len(pending)} bytes, header says {header['total_length']}")

        # Rebuild the exact preimage the canonical path hashes: length-prefixed segments.
        hasher = blake3()
        hasher.update(DOMAIN)
        cursor = 0
        for segment in header["segments"]:
            length = segment["length"]
            hasher.update(length.to_bytes(8, "big"))
            hasher.update(pending[cursor : cursor + length])
            cursor += length
        actual = "blake3:" + hasher.hexdigest()
        if actual != header["digest"]:
            _refuse("stream-digest-mismatch", actual, f"content hashes to {actual}, header claims {header['digest']}")

        self.state = bytes(pending)
        self.digest = actual
        self.adoptions += 1
        return {"schema": STREAM_SCHEMA, "state": "held", "digest": actual, "length": len(self.state), "adoptions": self.adoptions}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="secure-shell stream", description=__doc__.splitlines()[0])
    commands = parser.add_subparsers(dest="command", required=True)

    frame_command = commands.add_parser("frame", help="frame a package and print its stream header")
    frame_command.add_argument("--manifest", required=True)
    frame_command.add_argument("--payload", default=None)
    frame_command.add_argument("--chunk-size", type=int, default=cn.CHUNK_DEFAULT)

    receive_command = commands.add_parser("receive", help="receive a package, with an injectable fault")
    receive_command.add_argument("--manifest", required=True)
    receive_command.add_argument("--payload", default=None)
    receive_command.add_argument("--chunk-size", type=int, default=cn.CHUNK_DEFAULT)
    receive_command.add_argument("--prior", default=None)
    receive_command.add_argument("--drop", type=int, default=None, help="omit this chunk")
    receive_command.add_argument("--swap", nargs=2, type=int, default=None, metavar=("A", "B"))
    receive_command.add_argument("--truncate", type=int, default=None, help="cut this many bytes from chunk 0")
    receive_command.add_argument("--corrupt", type=int, default=None, help="flip one byte in this chunk")

    commands.add_parser("refusals", help="the enumerated refusal names")

    arguments = parser.parse_args(argv)
    try:
        if arguments.command == "frame":
            manifest = json.loads(Path(arguments.manifest).read_text(encoding="utf-8"))
            payload = Path(arguments.payload).read_bytes() if arguments.payload else b""
            print(json.dumps(package_stream(manifest, payload, arguments.chunk_size), sort_keys=True))
            return 0
        if arguments.command == "receive":
            manifest = json.loads(Path(arguments.manifest).read_text(encoding="utf-8"))
            payload = Path(arguments.payload).read_bytes() if arguments.payload else b""
            header, wire = frame_content(manifest, payload, arguments.chunk_size)
            prior = arguments.prior.encode("utf-8") if arguments.prior is not None else None
            receiver = Receiver(prior=prior, prior_digest=None)

            # A fault selector that names no chunk must refuse: silently doing nothing would
            # report a clean adoption for a stream that was never actually damaged.
            # `--truncate` takes a byte count, so the chunk it must find is always chunk 0.
            indices = {frame["index"] for frame in wire}
            requested = [target for target in (arguments.drop, *(arguments.swap or ()), arguments.corrupt) if target is not None]
            try:
                if arguments.truncate is not None:
                    if arguments.truncate < 1:
                        _refuse("fault-target-invalid", str(arguments.truncate), "truncate must remove at least one byte")
                    requested.append(0)
                for target in requested:
                    if target not in indices:
                        _refuse("fault-target-invalid", str(target), f"this stream has no chunk {target}; it carries {len(indices)} chunk(s)")
            except Refused as refusal:
                body = refusal.as_dict()
                body["prior_unchanged"] = receiver.state == prior
                body["adoptions"] = receiver.adoptions
                print(json.dumps(body, sort_keys=True))
                return 1

            if arguments.drop is not None:
                wire = [frame for frame in wire if frame["index"] != arguments.drop]
            if arguments.swap is not None:
                first, second = arguments.swap
                positions = {frame["index"]: position for position, frame in enumerate(wire)}
                if first in positions and second in positions:
                    left, right = positions[first], positions[second]
                    wire[left], wire[right] = wire[right], wire[left]
            if arguments.truncate is not None:
                cut = arguments.truncate
                wire = [{**wire[0], "data": wire[0]["data"][:-cut]}] + wire[1:]
            if arguments.corrupt is not None:
                wire = [
                    ({**frame, "data": bytes([frame["data"][0] ^ 0xFF]) + frame["data"][1:]} if frame["index"] == arguments.corrupt else frame)
                    for frame in wire
                ]
            try:
                result = receiver.adopt(header, wire)
            except Refused as refusal:
                body = refusal.as_dict()
                body["prior_unchanged"] = receiver.state == prior
                body["adoptions"] = receiver.adoptions
                print(json.dumps(body, sort_keys=True))
                return 1
            print(json.dumps(result, sort_keys=True))
            return 0
        print(json.dumps({"schema": STREAM_SCHEMA, "state": "held", "refusals": list(REFUSALS)}, sort_keys=True))
        return 0
    except Refused as refusal:
        print(json.dumps(refusal.as_dict(), sort_keys=True))
        return 1
    except (OSError, json.JSONDecodeError) as error:
        print(
            json.dumps(
                {"schema": STREAM_SCHEMA, "state": "absent", "refusal": "stream-unreadable", "subject": str(error)},
                sort_keys=True,
            )
        )
        return 1


if __name__ == "__main__":
    sys.exit(main())
