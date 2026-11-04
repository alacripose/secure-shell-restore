"""Secure Shell Restore — canonical package identity (R4).

The contract is `docs/SECURE-SHELL-RESTORE@1.ARCHITECTURE.md` §2 and §5:

    name@<rev>+blake3:<64 lowercase hex>
    name@<rev>+blake3:<hex>(dep-a@<rev>+blake3:<hex>, dep-b@<rev>+blake3:<hex>)

Every refusal is named and exits non-zero. Nothing falls back to a plausible value: an
identity that does not parse is refused with the subject and the reason, never repaired.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any, Iterable

from blake3 import blake3

SCHEMA = "secure-shell.package/1"
DOMAIN = b"secure-shell.package/1"

# Q021's family schema: lowercase, hyphen-separated. A name is a lineage, not a release.
NAME = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
# R-B: monotonic integers only, starting at 1, never renumbered, never zero-padded.
REVISION = re.compile(r"^[1-9][0-9]*$")
HASH = re.compile(r"^[0-9a-f]{64}$")

# R-C: the digest covers canonical content only. These fields are transport, envelope or
# timestamp material and are excluded so identity survives re-encryption and re-signing.
EXCLUDED = frozenset(
    {
        "signature",
        "signature_algorithm",
        "received_at",
        "admitted_at",
        "hash",
        "digest",
        "nonce",
        "chunk_frame",
    }
)

REFUSALS = (
    "algorithm-unsupported",
    "dependency-duplicate",
    "dependency-malformed",
    "dependency-unordered",
    "hash-invalid",
    "identity-malformed",
    "manifest-malformed",
    "name-invalid",
    "revision-invalid",
)


class Refused(Exception):
    """A named refusal, carrying the subject and the reason."""

    def __init__(self, refusal: str, subject: str, reason: str) -> None:
        # The family schema, not this module's enum: sibling modules declare their own
        # vocabularies and each of them asserts membership where it refuses.
        assert isinstance(refusal, str) and NAME.match(refusal), refusal
        super().__init__(reason)
        self.refusal = refusal
        self.subject = subject
        self.reason = reason

    def as_dict(self) -> dict[str, Any]:
        return {
            "schema": SCHEMA,
            "state": "refused",
            "refusal": self.refusal,
            "subject": self.subject,
            "reason": self.reason,
        }


def _refuse(refusal: str, subject: str, reason: str) -> None:
    raise Refused(refusal, subject, reason)


def _subject(value: Any, limit: int = 96) -> str:
    text = value if isinstance(value, str) else repr(value)
    return text if len(text) <= limit else text[:limit] + "…"


def _check_name(name: Any) -> str:
    if not isinstance(name, str) or not NAME.match(name):
        _refuse("name-invalid", _subject(name), "name must be lowercase hyphen-separated [a-z0-9-]")
    return name


def _check_revision(revision: Any) -> str:
    if isinstance(revision, int) and not isinstance(revision, bool):
        revision = str(revision)
    if not isinstance(revision, str) or not REVISION.match(revision):
        _refuse(
            "revision-invalid",
            _subject(revision),
            "revision must be a monotonic integer starting at 1, with no leading zero",
        )
    return revision


def _check_hash(value: Any) -> str:
    text = value
    if isinstance(text, str) and text.startswith("blake3:"):
        text = text[len("blake3:"):]
    if not isinstance(text, str) or not HASH.match(text):
        _refuse("hash-invalid", _subject(value), "hash must be 64 lowercase hex digits")
    return text


def _split_dependencies(text: str) -> tuple[str, tuple[str, ...]]:
    """Split the trailing `(...)` set from an identity, refusing a malformed one."""
    if not text.endswith(")"):
        if "(" in text:
            _refuse("identity-malformed", _subject(text), "unclosed dependency set")
        return text, ()
    opened = text.rfind("(")
    if opened < 0:
        _refuse("identity-malformed", _subject(text), "closing parenthesis without opening parenthesis")
    inner = text[opened + 1 : -1]
    if not inner.strip():
        _refuse("dependency-malformed", _subject(text), "empty dependency set")
    entries = tuple(entry.strip() for entry in inner.split(","))
    if any(not entry for entry in entries):
        _refuse("dependency-malformed", _subject(text), "empty dependency entry")
    body = text[:opened]
    if "(" in body:
        _refuse("dependency-malformed", _subject(text), "dependency sets do not nest")
    return body, entries


def parse_identity(text: Any) -> dict[str, Any]:
    """Parse a canonical or pin-complete identity into its parts, or refuse by name."""
    if not isinstance(text, str) or not text:
        _refuse("identity-malformed", _subject(text), "identity must be a non-empty string")
    if text != text.strip():
        _refuse("identity-malformed", _subject(text), "identity must not be padded with whitespace")

    body, dependency_texts = _split_dependencies(text)

    if "@" not in body:
        _refuse("name-invalid", _subject(text), "no name@revision part")
    name, _, rest = body.partition("@")
    _check_name(name)

    if "+" not in rest:
        _refuse("revision-invalid", _subject(text), "no revision+algorithm:hash part")
    revision, _, tail = rest.partition("+")
    _check_revision(revision)

    algorithm, colon, hash_text = tail.partition(":")
    if not colon:
        _refuse("algorithm-unsupported", _subject(text), "no algorithm:hash part")
    if algorithm != "blake3":
        _refuse("algorithm-unsupported", _subject(algorithm), "only blake3 identity is admitted in this release")
    digest = _check_hash(hash_text)

    dependencies = [parse_identity(entry) for entry in dependency_texts]
    for dependency in dependencies:
        if dependency["dependencies"]:
            _refuse("dependency-malformed", _subject(dependency["identity"]), "dependency sets do not nest")

    names = [dependency["name"] for dependency in dependencies]
    if len(names) != len(set(names)):
        duplicate = next(name for name in names if names.count(name) > 1)
        _refuse("dependency-duplicate", _subject(duplicate), f"dependency {duplicate} appears more than once")
    if names != sorted(names):
        _refuse("dependency-unordered", _subject(text), "dependencies must be ordered by name")

    return {
        "schema": SCHEMA,
        "state": "held",
        "identity": text,
        "name": name,
        "revision": int(revision),
        "algorithm": "blake3",
        "hash": digest,
        "dependencies": dependencies,
        "pin_complete": bool(dependencies),
    }


def format_identity(
    name: Any,
    revision: Any,
    digest: Any,
    dependencies: Iterable[str] = (),
) -> str:
    """Build the canonical name; dependencies are ordered by name and never duplicated."""
    _check_name(name)
    revision = _check_revision(revision)
    digest = _check_hash(digest)

    parsed = [parse_identity(entry) for entry in dependencies]
    for dependency in parsed:
        if dependency["dependencies"]:
            _refuse("dependency-malformed", _subject(dependency["identity"]), "dependency sets do not nest")
    names = [dependency["name"] for dependency in parsed]
    if len(names) != len(set(names)):
        duplicate = next(entry for entry in names if names.count(entry) > 1)
        _refuse("dependency-duplicate", _subject(duplicate), f"dependency {duplicate} appears more than once")

    ordered = sorted(parsed, key=lambda dependency: dependency["name"])
    canonical = f"{name}@{revision}+blake3:{digest}"
    if ordered:
        canonical += "(" + ",".join(dependency["identity"] for dependency in ordered) + ")"
    return canonical


def next_revision(existing: Iterable[Any]) -> int:
    """R-B: the next revision is one past the highest, or 1. Revisions are never reused."""
    revisions = [int(_check_revision(value)) for value in existing]
    return max(revisions) + 1 if revisions else 1


def canonical_bytes(value: Any) -> bytes:
    """Deterministic serialization: sorted keys, no incidental whitespace, UTF-8."""
    try:
        return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    except (TypeError, ValueError) as error:
        _refuse("manifest-malformed", _subject(value), f"value is not canonically serializable: {error}")


def package_digest(manifest: dict[str, Any], payload: bytes = b"") -> str:
    """R-C: BLAKE3 over the canonical content, with each field length-prefixed.

    Excluded material never reaches the hash, so the same content re-signed, re-encrypted or
    re-chunked keeps its identity; a change to any admitted byte changes it.
    """
    if not isinstance(manifest, dict):
        _refuse("manifest-malformed", _subject(manifest), "manifest must be an object")
    if not isinstance(payload, (bytes, bytearray)):
        _refuse("manifest-malformed", _subject(type(payload)), "payload must be bytes")

    kept = {key: value for key, value in manifest.items() if key not in EXCLUDED}
    hasher = blake3()
    hasher.update(DOMAIN)
    for field in (canonical_bytes(kept), bytes(payload)):
        hasher.update(len(field).to_bytes(8, "big"))
        hasher.update(field)
    return "blake3:" + hasher.hexdigest()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="secure-shell identity", description=__doc__.splitlines()[0])
    commands = parser.add_subparsers(dest="command", required=True)

    parse_command = commands.add_parser("parse", help="parse a canonical or pin-complete identity")
    parse_command.add_argument("identity")

    format_command = commands.add_parser("format", help="build a canonical identity")
    format_command.add_argument("--name", required=True)
    format_command.add_argument("--revision", required=True)
    format_command.add_argument("--hash", required=True)
    format_command.add_argument("--dependency", action="append", default=[])

    digest_command = commands.add_parser("digest", help="content identity of a file")
    digest_command.add_argument("path")
    digest_command.add_argument("--manifest", help="manifest JSON; the file is then the payload")

    commands.add_parser("refusals", help="the enumerated refusal names")

    arguments = parser.parse_args(argv)
    try:
        if arguments.command == "parse":
            result: dict[str, Any] = parse_identity(arguments.identity)
        elif arguments.command == "format":
            result = {
                "schema": SCHEMA,
                "state": "held",
                "identity": format_identity(
                    arguments.name,
                    arguments.revision,
                    arguments.hash,
                    arguments.dependency,
                ),
            }
        elif arguments.command == "digest":
            payload = Path(arguments.path).read_bytes()
            if arguments.manifest:
                manifest = json.loads(Path(arguments.manifest).read_text(encoding="utf-8"))
                result = {"schema": SCHEMA, "state": "held", "digest": package_digest(manifest, payload)}
            else:
                result = {"schema": SCHEMA, "state": "held", "digest": "blake3:" + blake3(payload).hexdigest()}
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
                    "refusal": "identity-unreadable",
                    "subject": getattr(error, "filename", None) or arguments.path,
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
