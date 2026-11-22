"""Write the contour record the secure shell restore carries, from the files that own it.

The pinned contour is not authored here and is not re-measured here. It is owned by
`deadlock-model-forge/pins/contour-pin.json` (the accepted numbers and the two captured images) and
implemented twice: `openlock/clientaddon/panorama/scripts/openlock_contour.js` for the shell inside
the game, and `popit-shell/ui/contour.js` for the reference page. This tool reads all three, refuses
when one is absent, and writes the record the axis reads:

    packages/contour/contour.json      the numbers, the two implementations and their digests
    packages/contour/contour.meta.json the package manifest (name@revision, schema, lengths)

A file that changed without the record being rewritten is `contour-record-stale`; a missing owner
file is `contour-owner-absent`. Neither falls back to a remembered number.

    python tools/contour_record.py            # read the owners, write the record
    python tools/contour_record.py --check    # exit 1 when the record is not these files
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RECORD = ROOT / "packages" / "contour" / "contour.json"
MANIFEST = ROOT / "packages" / "contour" / "contour.meta.json"

FAMILY = Path("<home>/Documents/deadlock-model-forge")
OWNERS = {
    "pin": FAMILY / "pins" / "contour-pin.json",
    "openlock": Path("<home>/Documents/openlock/clientaddon/panorama/scripts/openlock_contour.js"),
    "popit": Path("F:/Documents/popit-shell/ui/contour.js"),
}

SCHEMA = "secure-shell.contour/1"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes().replace(b"\r\n", b"\n")).hexdigest()


def build() -> str:
    missing = [name for name, path in OWNERS.items() if not path.exists()]
    if missing:
        print(json.dumps({"schema": SCHEMA, "state": "absent", "refusal": "contour-owner-absent",
                          "subject": ", ".join(sorted(missing)), "reason": "the owner file is not on disk"},
                         sort_keys=True))
        raise SystemExit(1)
    pin = json.loads(OWNERS["pin"].read_text(encoding="utf-8"))
    surfaces = pin["surfaces"]
    record = {
        "schema": SCHEMA,
        "name": "contour-pin",
        "revision": 1,
        "owners": {
            "pin": str(OWNERS["pin"]).replace("\\", "/"),
            "pin_sha256": sha256(OWNERS["pin"]),
        },
        "surfaces": {
            "plate": surfaces["plate"],
            "card": surfaces["card"],
            "application": surfaces["application"],
        },
        "corner_px": pin.get("corner_px", {"width": 7.67, "height": 11.0}),
        "implementations": {
            "openlock": {
                "path": "openlock/clientaddon/panorama/scripts/openlock_contour.js",
                "sha256": sha256(OWNERS["openlock"]),
                "draws": ["surface silhouette through --clip", "frame stroke on the host edge", "overhang"],
            },
            "popit": {
                "path": "popit-shell/ui/contour.js",
                "sha256": sha256(OWNERS["popit"]),
                "draws": ["surface silhouette through --clip", "frame stroke inside the clip", "corner of the chip"],
            },
        },
        "images": pin.get("images", {}),
        "note": "Both implementations are read from their own files; this record names them and their digests, it does not restate their code.",
    }
    manifest = {
        "name": "contour-pin",
        "revision": 1,
        "schemas": [SCHEMA],
        "dependencies": [],
        "entry_points": ["packages/contour/contour.json"],
        "lengths": {"payload": 0},
    }
    text = json.dumps(record, indent=2, sort_keys=True) + "\n"
    manifest["lengths"]["payload"] = len(text.encode("utf-8"))
    return json.dumps({"record": text, "manifest": json.dumps(manifest, indent=2) + "\n"}, sort_keys=True)


def write() -> int:
    built = json.loads(build())
    RECORD.parent.mkdir(parents=True, exist_ok=True)
    RECORD.write_text(built["record"], encoding="utf-8")
    MANIFEST.write_text(built["manifest"], encoding="utf-8")
    print(f"wrote {RECORD.relative_to(ROOT)} and {MANIFEST.relative_to(ROOT)}")
    return 0


def check() -> int:
    if not RECORD.exists() or not MANIFEST.exists():
        print("[FAIL] contour-record-missing: run python tools/contour_record.py")
        return 1
    built = json.loads(build())
    if RECORD.read_text(encoding="utf-8") != built["record"]:
        print("[FAIL] contour-record-stale: the owners changed, run python tools/contour_record.py")
        return 1
    if MANIFEST.read_text(encoding="utf-8") != built["manifest"]:
        print("[FAIL] contour-record-stale: the manifest does not match the record")
        return 1
    record = json.loads(RECORD.read_text(encoding="utf-8"))
    print(f"contour record is the owners: pin {record['owners']['pin_sha256'][:12]}, "
          f"openlock {record['implementations']['openlock']['sha256'][:12]}, "
          f"popit {record['implementations']['popit']['sha256'][:12]}")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="secure-shell contour", description=__doc__.splitlines()[0])
    parser.add_argument("--check", action="store_true", help="exit 1 when the record is not these files")
    arguments = parser.parse_args(argv)
    return check() if arguments.check else write()


if __name__ == "__main__":
    sys.exit(main())
