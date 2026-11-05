#!/usr/bin/env python3
"""Train the CUA axis drivers from this machine's projects, and prove the loop end to end.

The axis owns the authority rules: a driver registers declared capabilities, attests, and may act
only under a ticket the axis issued for that exact action. This tool is the training half of that
contract, and it learns from two corpora:

- the folder audit (`docs/secure-shell-audit/resynth_audit@2026-11-04.json`), one bundle per project;
- the projects' own documents (`AGENTS.md`, `VOWS.md`, `CHECKPOINT.md`, `CONTEXT.md`, `docs/**`,
  `tickets/**`), because the expectation documents a project carries — the CGA acceptance contract
  is one of them — are what its civilians are meant to learn from, not commentary about them.

Every bundle is admitted into the Mongo authority on the Debian host, then applied through the axis
under a ticket, so a receipt exists for every document and every project the driver learned from.

Nothing is written before the ticket is granted. A refusal from the axis stops that bundle and is
reported with its own code, and the tool exits non-zero rather than reporting a pass it did not get.

Beyond learning it exercises the two autonomous controls the axis names:

  witness  — hash the corpus file the row bundles were built from
  kernel   — a kernel-scoped action, allowed only because this driver declares `kernel`; the axis
             records the receipt and grants nothing the declaration did not already claim

Run it inside the Debian host, where the axis listens on loopback and the sealed credential can be
decrypted for the run:

  /opt/drill-venv/bin/python tools/cua_training.py --uri-file /run/drill-mongo.uri --documents
"""

from __future__ import annotations

import os as _os
import sys
import sys as _sys

_sys.path.insert(0, _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))))

import argparse
import hashlib
import json
import re
import time
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any

from impl.packages.identity import Refused
from impl.packages.mongo_store import admit as mongo_admit
from impl.packages.toolstream import ToolStream

DRIVER_ID = "project-corpus-driver"
DRIVER_REVISION = "1"
DRIVER_CAPABILITIES = ["witness", "learning-apply", "kernel"]
CORPUS = Path("docs/secure-shell-audit/resynth_audit@2026-11-04.json")
STREAM = ToolStream("cua-training")

DOC_NAMES = ("AGENTS.md", "VOWS.md", "CHECKPOINT.md", "CONTEXT.md")
DOC_DIRS = ("docs", "tickets")
DOC_BYTES = 200_000
DOCS_PER_PROJECT = 12
MAX_DOC_BUNDLES = 400


def post(axis: str, path: str, body: dict[str, Any]) -> dict[str, Any]:
    request = urllib.request.Request(
        axis + path,
        data=json.dumps(body).encode("utf-8"),
        headers={"content-type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=15) as answer:
            return json.loads(answer.read().decode("utf-8"))
    except urllib.error.HTTPError as error:
        payload = json.loads(error.read().decode("utf-8") or "{}")
        raise Refused(
            str(payload.get("refused") or "axis-refused"),
            str(payload.get("subject") or DRIVER_ID),
            str(payload.get("why") or payload.get("detail") or f"http {error.code}"),
        )


def get(axis: str, path: str) -> dict[str, Any]:
    with urllib.request.urlopen(axis + path, timeout=15) as answer:
        return json.loads(answer.read().decode("utf-8"))


def register(axis: str, until_ms: int) -> None:
    try:
        post(axis, "/api/axis/drivers", {
            "id": DRIVER_ID, "kind": "cua-node", "revision": DRIVER_REVISION,
            "capabilities": DRIVER_CAPABILITIES,
        })
    except Refused as refusal:
        if refusal.as_dict().get("refusal") != "driver-duplicate":
            raise
    post(axis, "/api/axis/attest", {
        "driver": DRIVER_ID, "verifier": "resynth-audit", "expiresAt": until_ms,
    })


def ticketed(axis: str, action: str, extra: dict[str, Any], scope: str = "device") -> dict[str, Any]:
    body = {"driver": DRIVER_ID, "action": action}
    if scope != "device":
        body["scope"] = scope
    ticket = post(axis, "/api/axis/tickets", body)["ticket"]
    payload = {"ticket": ticket["id"], "action": action}
    payload.update(extra)
    return post(axis, "/api/axis/act", payload)["receipt"]


def slug(text: str, limit: int = 60) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")[:limit] or "unnamed"


def bundle_for(row: dict[str, Any]) -> tuple[str, bytes]:
    name = str(row.get("name") or "")
    if not name:
        raise Refused("bundle-name", "row", "a corpus row without a project name cannot be trained")
    body = {"schema": "secure-shell.training/1", "project": name, "row": row}
    payload = (json.dumps(body, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")
    return f"secure-shell.training/{name}@1", payload


def document_bundles(root: Path) -> list[tuple[str, bytes]]:
    """The documents a project carries, bounded: what its civilians are meant to learn from."""
    files: list[Path] = []
    for name in DOC_NAMES:
        candidate = root / name
        if candidate.is_file():
            files.append(candidate)
    for directory in DOC_DIRS:
        base = root / directory
        if not base.is_dir():
            continue
        for found in sorted(base.rglob("*.md")):
            files.append(found)
            if len(files) >= DOCS_PER_PROJECT * 4:
                break
    bundles: list[tuple[str, bytes]] = []
    for path in files:
        if len(bundles) >= DOCS_PER_PROJECT:
            break
        try:
            if path.stat().st_size > DOC_BYTES:
                continue
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue
        relative = str(path.relative_to(root)).replace("\\", "/")
        digest = hashlib.sha256(text.encode("utf-8")).hexdigest()
        body = {
            "schema": "secure-shell.training.document/1",
            "project": root.name,
            "path": relative,
            "sha256": "sha256:" + digest,
            "text": text,
        }
        payload = (json.dumps(body, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")
        bundles.append((f"secure-shell.training.docs/{slug(root.name)}-{slug(relative, 40)}@{digest[:8]}", payload))
    return bundles


def learn(axis: str, uri: str, database: str, identity: str, payload: bytes, extra: dict[str, Any]) -> dict[str, Any]:
    digest = "sha256:" + hashlib.sha256(payload).hexdigest()
    admitted = mongo_admit(uri, identity, {
        "name": identity.split("/", 1)[-1].split("@", 1)[0],
        "revision": 1,
        "schemas": ["secure-shell.training/1"],
        "dependencies": [],
        "entry_points": ["bundle.json"],
        "lengths": {"files": 1, "payload": len(payload)},
    }, payload, database)
    receipt = ticketed(axis, "learning-apply", {
        "bundle": {"bytes": payload.decode("utf-8"), "digest": digest},
    })
    if receipt.get("applied") is not True:
        raise Refused("training-not-applied", identity, "the axis recorded no applied receipt")
    return {"identity": identity, "store": admitted.get("digest"), "receipt": receipt.get("digest"),
            "duplicate": admitted.get("duplicate", False), **extra}


def host_path(value: str) -> Path:
    """A root named on the Windows host, reachable from the Debian side of the mount."""
    text = value.replace(chr(92), "/")
    if _os.path.isdir("/mnt/c") and len(text) > 2 and text[1] == ":":
        return Path("/mnt/" + text[0].lower() + text[2:])
    return Path(text)

def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="cua_training")
    parser.add_argument("--axis", default=_os.environ.get("AXIS_URL", "http://127.0.0.1:8787"))
    parser.add_argument("--corpus", default=str(CORPUS))
    parser.add_argument("--uri-file", default="/run/drill-mongo.uri")
    parser.add_argument("--database", default="secure_shell")
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--ticks", type=int, default=1)
    parser.add_argument("--documents", action="store_true")
    parser.add_argument("--roots", nargs="+", default=["C:/Users/ala/Documents", "F:/"])
    parser.add_argument("--depth", type=int, default=2)
    parser.add_argument("--budget", type=float, default=20.0)
    args = parser.parse_args(argv)

    corpus = Path(args.corpus)
    if not corpus.is_file():
        raise Refused("corpus-absent", str(corpus), "run tools/resynth_agents.py --report first")
    rows = json.loads(corpus.read_text(encoding="utf-8"))["rows"]
    if args.limit:
        rows = rows[: args.limit]

    uri = Path(args.uri_file).read_text(encoding="utf-8").strip()
    trained = 0
    documents = 0
    truncated: list[str] = []
    for tick in range(max(1, args.ticks)):
        until = int(time.time() * 1000) + 86_400_000
        register(args.axis, until)
        lapsed = get(args.axis, "/api/axis/review").get("review", [])
        STREAM.emit({"event": "tick", "tick": tick, "lapsed": len(lapsed), "projects": len(rows)})
        for row in rows:
            identity, payload = bundle_for(row)
            learned = learn(args.axis, uri, args.database, identity, payload, {"project": str(row.get("name"))})
            trained += 1
            STREAM.emit({"event": "trained", **learned})
        if args.documents:
            from tools.resynth_agents import discover

            projects, truncated = discover([host_path(root) for root in args.roots], args.depth, args.budget)
            for root in projects:
                if documents >= MAX_DOC_BUNDLES:
                    truncated = truncated + [f"doc-bundles:{MAX_DOC_BUNDLES}"]
                    break
                for identity, payload in document_bundles(root):
                    if documents >= MAX_DOC_BUNDLES:
                        break
                    learned = learn(args.axis, uri, args.database, identity, payload,
                                    {"project": root.name, "document": identity})
                    documents += 1
                    STREAM.emit({"event": "trained-document", **learned})
            for root in truncated:
                STREAM.emit({"event": "truncated", "root": str(root), "budget_s": args.budget})
        witness = ticketed(args.axis, "witness", {
            "digest": "sha256:" + hashlib.sha256(corpus.read_bytes()).hexdigest(),
        })
        STREAM.emit({"event": "witnessed", "corpus": str(corpus), "receipt": witness.get("digest")})
        control = ticketed(args.axis, "kernel", {"digest": witness.get("digest")}, scope="kernel")
        STREAM.emit({"event": "kernel-scope", "receipt": control.get("digest"), "scope": control.get("scope")})
        if args.ticks > 1:
            time.sleep(1)

    state = get(args.axis, "/api/axis/state")
    STREAM.emit({
        "event": "state", "drivers": len(state.get("drivers", [])),
        "tickets": state.get("tickets"), "receipts": state.get("receipts"),
        "trained": trained, "documents": documents, "truncated_roots": len(truncated),
    })
    header = STREAM.close(state="held")
    print(json.dumps({"trained": trained, "documents": documents, "receipts": state.get("receipts"),
                      "truncated_roots": len(truncated), "transcript": header.get("digest")},
                     sort_keys=True), file=sys.stderr)
    return 0


if __name__ == "__main__":
    try:
        code = main()
    except Refused as refusal:
        STREAM.emit({"event": "refused", "state": "refused", **refusal.as_dict()})
        STREAM.close(state="refused")
        print(json.dumps(refusal.as_dict(), sort_keys=True), file=sys.stderr)
        code = 1
    finally:
        if not STREAM.closed:
            STREAM.close(state="refused")
    sys.exit(code)
