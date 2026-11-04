"""Flip one byte of an admitted package's stored payload, for the drill's refusal case.

This is a drill fixture, not shipped code: it exists so `mongo-digest` is proven by a real
corrupted record rather than asserted from a description. It never prints the URI.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from pymongo import MongoClient


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--uri-file", required=True)
    parser.add_argument("--identity", required=True)
    parser.add_argument("--database", default="secure_shell")
    args = parser.parse_args()
    uri = Path(args.uri_file).read_text(encoding="utf-8").strip()
    collection = MongoClient(uri, serverSelectionTimeoutMS=5000)[args.database]["packages"]
    document = collection.find_one({"_id": args.identity})
    if document is None:
        print(f"refused: mongo-package-absent: {args.identity}", file=sys.stderr)
        return 1
    payload = bytearray(document["payload"])
    payload[0] ^= 0xFF
    collection.update_one({"_id": args.identity}, {"$set": {"payload": bytes(payload)}})
    print(f"tampered: {args.identity}: 1 byte flipped, stored digest left as it was")
    return 0


if __name__ == "__main__":
    sys.exit(main())
