"""The Mongo authority: the durable record R3 names, written and read back by digest.

The plan's R3 says MongoDB is the canonical durable record on the Debian host, and that a clean
host reproduces the store digest. This module is the half of that sentence a restore can execute:
a package is admitted as one document keyed by its canonical identity, carrying the payload and
the digest the loader computed, and a restore reads it back and recomputes the digest before it
hands the bytes to anyone.

What it proves and what it does not: a matching BLAKE3 digest proves the bytes are the bytes that
were admitted. It says nothing about who admitted them — there is no signature here, and R5's
signing authority is still `absent`.

A refusal is a code, a subject and a reason, and the subject never carries the connection string:
a credential that reaches a log is a credential that leaked. The URI is read from a file so a
caller can hand it one written by `systemd-creds decrypt`, and it is redacted everywhere else.

Payloads are stored inline in the document, so this refuses a payload at or above BSON's 16 MiB
document limit by name (`mongo-payload-oversized`) rather than letting the driver fail opaquely.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

from blake3 import blake3

from impl.packages.identity import Refused

DB_DEFAULT = "secure_shell"
COLLECTION = "packages"
PAYLOAD_LIMIT = 16 * 1024 * 1024 - 64 * 1024
TIMEOUT_MS = 5000


def redact(uri: str) -> str:
    """A URI safe to name in a refusal: scheme, host and database, never the credentials."""
    if "@" in uri and "://" in uri:
        scheme, rest = uri.split("://", 1)
        return f"{scheme}://{rest.split('@', 1)[1]}"
    return uri


def client(uri: str):
    try:
        from pymongo import MongoClient
        from pymongo.errors import PyMongoError
    except ImportError:
        raise Refused("mongo-driver-absent", "pymongo", "the driver is not installed in this interpreter")
    handle = MongoClient(uri, serverSelectionTimeoutMS=TIMEOUT_MS)
    try:
        handle.admin.command("ping")
    except PyMongoError as error:
        raise Refused("mongo-absent", redact(uri), f"no server answered: {type(error).__name__}")
    return handle


def admit(uri: str, identity: str, manifest: dict[str, Any], payload: bytes, database: str = DB_DEFAULT) -> dict[str, Any]:
    """Admit one package under its canonical identity; a second different payload is refused."""
    if len(payload) >= PAYLOAD_LIMIT:
        raise Refused("mongo-payload-oversized", identity, f"{len(payload)} bytes exceeds the inline limit")
    digest = "blake3:" + blake3(payload).hexdigest()
    handle = client(uri)
    collection = handle[database][COLLECTION]
    existing = collection.find_one({"_id": identity})
    if existing is not None:
        if existing.get("digest") != digest:
            raise Refused("mongo-digest", identity, f"stored {existing.get('digest')}, offered {digest}")
        return {"state": "held", "identity": identity, "digest": digest, "duplicate": True}
    document = {
        "_id": identity,
        "name": manifest["name"],
        "revision": manifest["revision"],
        "length": len(payload),
        "digest": digest,
        "files": manifest.get("lengths", {}).get("files", 0),
        "manifest": json.dumps(manifest, sort_keys=True, separators=(",", ":")),
        "payload": payload,
        "schema": "secure-shell.mongo.package/1",
    }
    collection.insert_one(document)
    stored = collection.find_one({"_id": identity}) or {}
    if stored.get("digest") != digest:
        raise Refused("mongo-digest", identity, "the document read back does not match what was written")
    return {"state": "held", "identity": identity, "digest": digest, "duplicate": False, "database": database}


def restore(uri: str, identity: str, database: str = DB_DEFAULT) -> tuple[bytes, dict[str, Any]]:
    """Read a package back and recompute its digest before returning the bytes."""
    handle = client(uri)
    document = handle[database][COLLECTION].find_one({"_id": identity})
    if document is None:
        raise Refused("mongo-package-absent", identity, f"no document in {database}.{COLLECTION}")
    payload = bytes(document["payload"])
    digest = "blake3:" + blake3(payload).hexdigest()
    if digest != document.get("digest"):
        raise Refused("mongo-digest", identity, f"stored {document.get('digest')}, recomputed {digest}")
    return payload, {
        "state": "held",
        "identity": identity,
        "digest": digest,
        "length": len(payload),
        "database": database,
        "collection": COLLECTION,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="impl.packages.mongo_store")
    parser.add_argument("command", choices=("admit", "restore"))
    parser.add_argument("--uri-file", required=True)
    parser.add_argument("--identity")
    parser.add_argument("--manifest")
    parser.add_argument("--payload")
    parser.add_argument("--out")
    parser.add_argument("--database", default=DB_DEFAULT)
    args = parser.parse_args(argv)
    uri = Path(args.uri_file).read_text(encoding="utf-8").strip()
    try:
        if args.command == "admit":
            if not (args.identity and args.manifest and args.payload):
                raise Refused("mongo-argument-missing", "admit", "identity, manifest and payload are required")
            manifest = json.loads(Path(args.manifest).read_text(encoding="utf-8"))
            payload = Path(args.payload).read_bytes()
            print(json.dumps(admit(uri, args.identity, manifest, payload, args.database), sort_keys=True))
            return 0
        if not args.identity:
            raise Refused("mongo-argument-missing", "restore", "identity is required")
        payload, record = restore(uri, args.identity, args.database)
        if args.out:
            Path(args.out).write_bytes(payload)
        print(json.dumps(record, sort_keys=True))
        return 0
    except Refused as refusal:
        print(json.dumps(refusal.as_dict(), sort_keys=True))
        return 1


if __name__ == "__main__":
    sys.exit(main())
