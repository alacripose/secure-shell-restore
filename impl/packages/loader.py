"""Load a real source tree into a package under the shipped contract.

This is the bridge between the checkouts on this machine and the package format: it walks a
real directory (the OpenLock shell, for instance), orders the files by relative path, indexes
each one, and produces a manifest plus the payload the canonical and stream units already
understand. Nothing here is a stand-in for the sources — it reads them where they live.

Determinism is the point: the same tree in a different creation order produces the same
identity, so a rebuild can be compared with the admitted revision instead of asserted equal.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Iterable

from blake3 import blake3

from impl.packages import canonical as cn
from impl.packages.identity import Refused, format_identity

INDEX_SCHEMA = "secure-shell.package.files/1"
DEFAULT_EXTENSIONS = (".xml", ".js", ".css", ".json")


def collect(root: Path, extensions: Iterable[str] = DEFAULT_EXTENSIONS) -> list[dict[str, Any]]:
    """Every admitted file, ordered by its relative path. Order is a property of the tree."""
    if not root.is_dir():
        raise Refused("manifest-malformed", str(root), "package root is not a directory")
    wanted = tuple(extension.lower() for extension in extensions)
    files = []
    for path in sorted(root.rglob("*")):
        if not path.is_file() or path.suffix.lower() not in wanted:
            continue
        if any(part in {".git", "node_modules", "dist", "obj", "bin"} for part in path.relative_to(root).parts):
            continue
        data = path.read_bytes()
        files.append(
            {
                "path": path.relative_to(root).as_posix(),
                "length": len(data),
                "digest": "blake3:" + blake3(data).hexdigest(),
            }
        )
    if not files:
        raise Refused("manifest-malformed", str(root), f"no files with {', '.join(wanted)} under the root")
    return files


def build(
    root: Path,
    name: str,
    revision: int = 1,
    extensions: Iterable[str] = DEFAULT_EXTENSIONS,
) -> dict[str, Any]:
    """Build the package record: manifest, payload and the pin-complete identity."""
    files = collect(root, extensions)
    index = {"schema": INDEX_SCHEMA, "files": files}
    payload = cn.canonical_bytes(index)
    manifest = {
        "name": name,
        "revision": revision,
        "schemas": ["secure-shell.package/1", "secure-shell.stream/1"],
        "dependencies": [],
        "entry_points": [entry["path"] for entry in files],
        "lengths": {"files": len(files), "payload": len(payload)},
    }
    digest = cn.package_digest(manifest, payload)
    return {
        "schema": "secure-shell.package/1",
        "state": "held",
        "root": str(root),
        "files": len(files),
        "manifest": manifest,
        "payload": payload,
        "digest": digest,
        "identity": format_identity(name, revision, digest),
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="secure-shell loader", description=__doc__.splitlines()[0])
    parser.add_argument("--root", required=True)
    parser.add_argument("--name", required=True)
    parser.add_argument("--revision", type=int, default=1)
    parser.add_argument("--extensions", default=",".join(DEFAULT_EXTENSIONS))
    parser.add_argument("--write", default=None, help="directory to write manifest.json and payload.bin into")
    arguments = parser.parse_args(argv)
    try:
        record = build(
            Path(arguments.root),
            arguments.name,
            arguments.revision,
            tuple(extension.strip() for extension in arguments.extensions.split(",") if extension.strip()),
        )
    except Refused as refusal:
        print(json.dumps(refusal.as_dict(), sort_keys=True))
        return 1
    payload = record.pop("payload")
    if arguments.write:
        target = Path(arguments.write)
        target.mkdir(parents=True, exist_ok=True)
        (target / "manifest.json").write_text(json.dumps(record["manifest"], sort_keys=True, indent=2), encoding="utf-8")
        (target / "payload.bin").write_bytes(payload)
        record["written"] = str(target)
    print(json.dumps(record, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
