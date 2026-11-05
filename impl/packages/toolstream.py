"""The streamed tool report: a tool's output is a package stream, not prose.

This project already owns a stream format (`secure-shell.stream/1`): a header that declares its
segments and chunk digests, frames that carry the bytes, and a receiver that adopts the whole thing
or leaves prior state untouched. Tools that print "ok / FAIL" lines are outside that contract, so a
consumer — the client, the drill, the CUA driver — cannot adopt their output or verify it without
re-parsing prose. This module closes that gap.

A tool using this writes one JSON event per line to stdout as it runs, then a terminal line that is a
`secure-shell.stream/1` header describing the transcript. The header carries the manifest beside the
shipped fields, because the stream's `total_length` and chunk offsets count the canonical manifest
bytes and then the payload: without the manifest a reader cannot place a single chunk. The transcript
payload is the event lines, each terminated by one newline.

Two rules come with it, both from the family:

- **Refuse by name.** A tool that fails emits `state: refused` with `code`, `subject` and `why`, and
  exits non-zero. It does not exit 0 with a failure buried in a detail.
- **Nothing oversized silently.** An event longer than the maximum chunk size is refused
  `tool-event-oversized` rather than split, because splitting would make "one line, one chunk"
  false and the transcript would stop being what it says it is.

`python -m impl.packages.toolstream verify <transcript>` reads such a transcript and adopts it with
the shipped `Receiver`, printing the digest it recomputed. That is how a tool's own output is
checked: a transcript that does not verify is not a report.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

from impl.packages import canonical as cn
from impl.packages.identity import Refused
from impl.packages.stream import STREAM_SCHEMA, Receiver, package_stream

TRANSCRIPT_SCHEMA = "secure-shell.toolstream/1"
TRANSCRIPT_FILE = "tool-report.ndjson"


def _encode(event: dict[str, Any]) -> bytes:
    return json.dumps(event, sort_keys=True, separators=(",", ":")).encode("utf-8")


class ToolStream:
    """Emit events as they happen; close with a header that makes them adoptable."""

    def __init__(self, name: str, chunk_size: int = cn.CHUNK_DEFAULT, out: Any = None) -> None:
        self.name = name
        self.chunk_size = chunk_size
        self.out = out if out is not None else sys.stdout
        self.chunks: list[bytes] = []
        self.closed = False
        self.state = "held"

    def emit(self, event: dict[str, Any]) -> None:
        if self.closed:
            raise Refused("tool-stream-closed", self.name, "an event arrived after the header")
        line = _encode(event)
        if len(line) > self.chunk_size:
            raise Refused("tool-event-oversized", self.name, f"{len(line)} bytes exceeds chunk size {self.chunk_size}")
        self.chunks.append(line)
        if event.get("state") == "refused":
            self.state = "refused"
        self.out.write(line.decode("utf-8") + "\n")
        self.out.flush()

    def close(self, state: str | None = None) -> dict[str, Any]:
        if self.closed:
            return {}
        payload = b"".join(line + b"\n" for line in self.chunks)
        manifest = {
            "name": self.name,
            "revision": 1,
            "schemas": sorted([STREAM_SCHEMA, TRANSCRIPT_SCHEMA]),
            "dependencies": [],
            "entry_points": [TRANSCRIPT_FILE],
            "lengths": {"files": len(self.chunks), "payload": len(payload)},
        }
        header = package_stream(manifest, payload, self.chunk_size)
        header["state"] = state or self.state
        header["events"] = len(self.chunks)
        header["manifest"] = manifest
        self.closed = True
        self.out.write(json.dumps(header, sort_keys=True, separators=(",", ":")) + "\n")
        self.out.flush()
        return header


def verify(transcript: str) -> dict[str, Any]:
    """Adopt a transcript with the shipped receiver: the tool's own words, checked."""
    lines = [line for line in transcript.splitlines() if line.strip()]
    if len(lines) < 2:
        raise Refused("tool-transcript-invalid", "transcript", "a transcript is events plus a terminal header")
    header = json.loads(lines[-1])
    if header.get("schema") != STREAM_SCHEMA:
        raise Refused("tool-transcript-invalid", str(header.get("schema")), f"terminal line must be {STREAM_SCHEMA}")

    manifest = header.get("manifest")
    if not isinstance(manifest, dict):
        raise Refused("tool-transcript-invalid", "header", "header carries no manifest to anchor the chunks")

    body = lines[:-1]
    payload = b"".join(line.encode("utf-8") + bytes([10]) for line in body)
    kept = {key: value for key, value in manifest.items() if key not in cn.EXCLUDED}
    content = cn.canonical_bytes(kept) + payload
    if header.get("total_length") != len(content):
        raise Refused(
            "tool-transcript-invalid",
            str(header.get("total_length")),
            f"header declares {header.get('total_length')} bytes, transcript carries {len(content)}",
        )

    frames = []
    for chunk in header["chunks"]:
        offset, length = chunk["offset"], chunk["length"]
        frames.append({**chunk, "data": content[offset : offset + length]})

    adopted = {key: value for key, value in header.items() if key != "manifest"}
    result = Receiver().adopt(adopted, frames)
    return {**result, "events": len(body), "state": header.get("state", "held")}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="secure-shell toolstream")
    parser.add_argument("command", choices=("verify",))
    parser.add_argument("path")
    args = parser.parse_args(argv)
    try:
        text = Path(args.path).read_text(encoding="utf-8")
        print(json.dumps(verify(text), sort_keys=True))
        return 0
    except Refused as refusal:
        print(json.dumps(refusal.as_dict(), sort_keys=True))
        return 1


if __name__ == "__main__":
    sys.exit(main())
