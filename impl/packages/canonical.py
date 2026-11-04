"""Secure Shell Restore — the declared package object (R4: schema ids, chunk domains).

`identity.py` decides what a package is called and hashes whatever canonical content it is
handed. This module declares what that content may contain: a fixed manifest vocabulary, a
schema-id grammar, and chunk domains that never contaminate package identity.

The digest here is *the same* digest `identity.package_digest` produces for the same manifest
and payload — this module adds validation, not a second hash. Chunking is a transport concern:
a package streamed in one chunk or in a thousand reassembles to the same content and therefore
to the same identity (R-C).
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any, Iterable, Iterator

from blake3 import blake3

from impl.packages.identity import (
    EXCLUDED,
    NAME,
    REVISION,
    SCHEMA,
    Refused,
    canonical_bytes,
    parse_identity,
)

# One preimage, one domain, one digest. If this ever diverges from identity.DOMAIN the
# same package would have two identities, which R-C forbids.
DOMAIN = b"secure-shell.package/1"

CHUNK_ROOT = "secure-shell.chunk/1"
CHUNK_DEFAULT = 1 << 20
CHUNK_MAX = 8 << 20
CHUNK_ROLES = ("dependency", "manifest", "payload", "schema")

# `secure-shell.stream/1`, `surface.mount/2`, `secure-shell.package/1`: a family path and a
# monotonic integer. Subordinate contracts keep their own family, so a stream bump cannot
# silently bump a mount receipt (decision 8).
SCHEMA_ID = r"^[a-z][a-z0-9-]*(?:\.[a-z][a-z0-9-]*)*/(?P<version>[1-9][0-9]*)$"
# An entry point is a relative path (bin/store, lib/store.mjs): segments, no leading slash,
# no parent traversal, no backslash. Windows separators are refused rather than translated.
ENTRY_POINT = r"^[A-Za-z0-9][A-Za-z0-9._-]*(?:/[A-Za-z0-9][A-Za-z0-9._-]*)*$"

REQUIRED_FIELDS = ("name", "revision", "schemas", "dependencies", "entry_points", "lengths")

REFUSALS = (
    "chunk-domain-invalid",
    "chunk-sequence-invalid",
    "chunk-size-invalid",
    "dependency-duplicate",
    "dependency-malformed",
    "dependency-unordered",
    "entry-point-invalid",
    "length-invalid",
    "manifest-field-missing",
    "manifest-key-unknown",
    "manifest-malformed",
    "name-invalid",
    "revision-invalid",
    "schema-duplicate",
    "schema-id-invalid",
    "schema-unordered",
)


def _refuse(refusal: str, subject: Any, reason: str) -> None:
    assert refusal in REFUSALS, refusal
    raise Refused(refusal, subject if isinstance(subject, str) else repr(subject), reason)


def _subject(value: Any, limit: int = 96) -> str:
    text = value if isinstance(value, str) else repr(value)
    return text if len(text) <= limit else text[:limit] + "…"


def parse_schema_id(text: Any) -> dict[str, Any]:
    """Parse `family.path/<version>` or refuse it by name. No auto-detection, no repair."""
    if not isinstance(text, str) or not text:
        _refuse("schema-id-invalid", _subject(text), "schema id must be a non-empty string")
    match = re.match(SCHEMA_ID, text)
    if not match:
        _refuse(
            "schema-id-invalid",
            _subject(text),
            "schema id must be lowercase family.path/<monotonic integer>, e.g. secure-shell.stream/1",
        )
    version = int(match.group("version"))
    return {"schema": SCHEMA, "state": "held", "id": text, "family": text.rsplit("/", 1)[0], "version": version}


def schema_ids(values: Iterable[Any]) -> list[str]:
    """A schema set is ordered by id and duplicate-free; an unordered set is refused, not sorted."""
    if isinstance(values, (str, bytes)) or not isinstance(values, Iterable):
        _refuse("manifest-malformed", _subject(values), "schemas must be a list of schema ids")
    parsed = [parse_schema_id(value) for value in values]
    ids = [entry["id"] for entry in parsed]
    if len(ids) != len(set(ids)):
        duplicate = next(entry for entry in ids if ids.count(entry) > 1)
        _refuse("schema-duplicate", duplicate, f"schema {duplicate} is declared more than once")
    if ids != sorted(ids):
        _refuse("schema-unordered", _subject(values), "schemas must be ordered by id")
    return ids


def chunk_domain(role: Any) -> str:
    """Chunk digests live under their own domain, so they can never be mistaken for identity."""
    if role not in CHUNK_ROLES:
        _refuse(
            "chunk-domain-invalid",
            _subject(role),
            f"chunk role must be one of {', '.join(CHUNK_ROLES)}",
        )
    return f"{CHUNK_ROOT}/{role}"


def _check_chunk_size(chunk_size: Any) -> int:
    if isinstance(chunk_size, bool) or not isinstance(chunk_size, int):
        _refuse("chunk-size-invalid", _subject(chunk_size), "chunk size must be an integer")
    if chunk_size < 1:
        _refuse("chunk-size-invalid", str(chunk_size), "chunk size must be at least 1 byte")
    if chunk_size > CHUNK_MAX:
        _refuse("chunk-size-invalid", str(chunk_size), f"chunk size must not exceed {CHUNK_MAX} bytes")
    return chunk_size


def validate_manifest(manifest: Any) -> dict[str, Any]:
    """Check the declared vocabulary and return the kept content. Nothing is silently dropped."""
    if not isinstance(manifest, dict):
        _refuse("manifest-malformed", _subject(manifest), "manifest must be an object")

    missing = [field for field in REQUIRED_FIELDS if field not in manifest]
    if missing:
        _refuse("manifest-field-missing", _subject(manifest.get("name", manifest)), f"missing {', '.join(missing)}")

    unknown = sorted(key for key in manifest if key not in REQUIRED_FIELDS and key not in EXCLUDED)
    if unknown:
        _refuse(
            "manifest-key-unknown",
            ", ".join(unknown),
            "manifest declares a key outside the vocabulary; add it by ticket, not by accident",
        )

    name = manifest["name"]
    if not isinstance(name, str) or not NAME.match(name):
        _refuse("name-invalid", _subject(name), "name must be lowercase hyphen-separated [a-z0-9-]")

    revision = manifest["revision"]
    revision_text = str(revision) if isinstance(revision, int) and not isinstance(revision, bool) else revision
    if not isinstance(revision_text, str) or not REVISION.match(revision_text):
        _refuse("revision-invalid", _subject(revision), "revision must be a monotonic integer starting at 1")

    schemas = schema_ids(manifest["schemas"])

    dependencies = manifest["dependencies"]
    if isinstance(dependencies, (str, bytes)) or not isinstance(dependencies, Iterable):
        _refuse("manifest-malformed", _subject(dependencies), "dependencies must be a list of identities")
    parsed_dependencies = [parse_identity(entry) for entry in dependencies]
    dependency_names = [entry["name"] for entry in parsed_dependencies]
    if len(dependency_names) != len(set(dependency_names)):
        duplicate = next(entry for entry in dependency_names if dependency_names.count(entry) > 1)
        _refuse("dependency-duplicate", duplicate, f"dependency {duplicate} appears more than once")
    if dependency_names != sorted(dependency_names):
        _refuse("dependency-unordered", _subject(dependencies), "dependencies must be ordered by name")

    entry_points = manifest["entry_points"]
    if isinstance(entry_points, (str, bytes)) or not isinstance(entry_points, Iterable):
        _refuse("manifest-malformed", _subject(entry_points), "entry_points must be a list of names")
    for entry_point in entry_points:
        if not isinstance(entry_point, str) or not re.match(ENTRY_POINT, entry_point):
            _refuse("entry-point-invalid", _subject(entry_point), "entry point must match [A-Za-z0-9][A-Za-z0-9._-]*")
    if list(entry_points) != sorted(set(entry_points)):
        _refuse("entry-point-invalid", _subject(entry_points), "entry points must be ordered and unique")

    lengths = manifest["lengths"]
    if not isinstance(lengths, dict):
        _refuse("manifest-malformed", _subject(lengths), "lengths must be an object of non-negative integers")
    for key, value in lengths.items():
        if not isinstance(key, str) or not key:
            _refuse("length-invalid", _subject(key), "length keys must be non-empty strings")
        if isinstance(value, bool) or not isinstance(value, int) or value < 0:
            _refuse("length-invalid", _subject(key), "lengths must be non-negative integers")

    return {
        "schema": SCHEMA,
        "state": "held",
        "name": name,
        "revision": int(revision_text),
        "schemas": schemas,
        "dependencies": [entry["identity"] for entry in parsed_dependencies],
        "entry_points": list(entry_points),
        "lengths": lengths,
    }


def content_segments(manifest: dict[str, Any], payload: bytes = b"") -> Iterator[bytes]:
    """The exact preimage identity.package_digest hashes: kept manifest, then payload."""
    if not isinstance(payload, (bytes, bytearray)):
        _refuse("manifest-malformed", _subject(type(payload)), "payload must be bytes")
    kept = {key: value for key, value in manifest.items() if key not in EXCLUDED}
    yield canonical_bytes(kept)
    yield bytes(payload)


def content_bytes(manifest: dict[str, Any], payload: bytes = b"") -> bytes:
    return b"".join(content_segments(manifest, payload))


def package_digest(manifest: Any, payload: bytes = b"") -> str:
    """Validate the declared shape, then compute the one BLAKE3 identity for it."""
    validate_manifest(manifest)
    hasher = blake3()
    hasher.update(DOMAIN)
    for segment in content_segments(manifest, payload):
        hasher.update(len(segment).to_bytes(8, "big"))
        hasher.update(segment)
    return "blake3:" + hasher.hexdigest()


def chunked_package_digest(manifest: Any, payload: bytes = b"", chunk_size: int = CHUNK_DEFAULT) -> str:
    """The same identity, reached by streaming the preimage in bounded chunks.

    The chunk size changes how the bytes travel, never what they hash to: this is the R-C
    property that a package re-chunked in transit is still the same admitted package.
    """
    validate_manifest(manifest)
    chunk_size = _check_chunk_size(chunk_size)
    hasher = blake3()
    hasher.update(DOMAIN)
    for segment in content_segments(manifest, payload):
        hasher.update(len(segment).to_bytes(8, "big"))
        for offset in range(0, len(segment), chunk_size):
            hasher.update(segment[offset : offset + chunk_size])
    return "blake3:" + hasher.hexdigest()


def chunk_digest(role: str, index: int, data: bytes) -> str:
    """A chunk proves its bytes arrived under its own domain; it never proves package identity."""
    domain = chunk_domain(role)
    if isinstance(index, bool) or not isinstance(index, int) or index < 0:
        _refuse("chunk-sequence-invalid", _subject(index), "chunk index must be a non-negative integer")
    if not isinstance(data, (bytes, bytearray)):
        _refuse("manifest-malformed", _subject(type(data)), "chunk content must be bytes")
    hasher = blake3()
    hasher.update(domain.encode("utf-8"))
    hasher.update(index.to_bytes(8, "big"))
    hasher.update(len(data).to_bytes(8, "big"))
    hasher.update(bytes(data))
    return "blake3:" + hasher.hexdigest()


def chunk_manifest(content: bytes, chunk_size: int = CHUNK_DEFAULT, role: str = "payload") -> list[dict[str, Any]]:
    chunk_size = _check_chunk_size(chunk_size)
    domain = chunk_domain(role)
    chunks = []
    for index, offset in enumerate(range(0, len(content), chunk_size)):
        data = content[offset : offset + chunk_size]
        chunks.append(
            {
                "schema": SCHEMA,
                "state": "held",
                "index": index,
                "offset": offset,
                "length": len(data),
                "domain": domain,
                "digest": chunk_digest(role, index, data),
            }
        )
    return chunks


def reassemble(chunks: Iterable[tuple[int, bytes]]) -> bytes:
    """Ordered, gap-free reassembly; a gap is refused rather than padded over."""
    ordered = sorted(chunks, key=lambda entry: entry[0])
    for expected, (index, _data) in enumerate(ordered):
        if index != expected:
            _refuse(
                "chunk-sequence-invalid",
                f"expected index {expected}, found {index}",
                "chunk sequence has a gap or a duplicate",
            )
    return b"".join(data for _index, data in ordered)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="secure-shell canonical", description=__doc__.splitlines()[0])
    commands = parser.add_subparsers(dest="command", required=True)

    schema_command = commands.add_parser("schema", help="parse a schema id")
    schema_command.add_argument("schema_id")

    manifest_command = commands.add_parser("manifest", help="validate a manifest and digest it")
    manifest_command.add_argument("path")
    manifest_command.add_argument("--payload", help="file used as payload bytes")
    manifest_command.add_argument("--chunk-size", type=int, default=CHUNK_DEFAULT)

    chunk_command = commands.add_parser("chunk", help="chunk a file under a role domain")
    chunk_command.add_argument("path")
    chunk_command.add_argument("--role", default="payload")
    chunk_command.add_argument("--chunk-size", type=int, default=CHUNK_DEFAULT)

    commands.add_parser("refusals", help="the enumerated refusal names")

    arguments = parser.parse_args(argv)
    try:
        if arguments.command == "schema":
            result: dict[str, Any] = parse_schema_id(arguments.schema_id)
        elif arguments.command == "manifest":
            manifest = json.loads(Path(arguments.path).read_text(encoding="utf-8"))
            payload = Path(arguments.payload).read_bytes() if arguments.payload else b""
            result = validate_manifest(manifest)
            result["digest"] = chunked_package_digest(manifest, payload, arguments.chunk_size)
        elif arguments.command == "chunk":
            content = Path(arguments.path).read_bytes()
            chunks = chunk_manifest(content, arguments.chunk_size, arguments.role)
            result = {"schema": SCHEMA, "state": "held", "chunks": len(chunks), "manifest": chunks}
        else:
            result = {"schema": SCHEMA, "state": "held", "refusals": list(REFUSALS)}
    except Refused as refusal:
        print(json.dumps(refusal.as_dict(), sort_keys=True))
        return 1
    except (OSError, json.JSONDecodeError) as error:
        print(
            json.dumps(
                {
                    "schema": SCHEMA,
                    "state": "absent",
                    "refusal": "manifest-unreadable",
                    "subject": getattr(error, "filename", None) or "unknown",
                    "reason": str(error),
                },
                sort_keys=True,
            )
        )
        return 1
    print(json.dumps(result, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
