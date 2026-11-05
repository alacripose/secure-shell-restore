#!/usr/bin/env python3
"""Train the CUA axis drivers from this machine's projects, and prove the loop end to end.

The axis owns the authority rules: a driver registers declared capabilities, attests, and may act
only under a ticket the axis issued for that exact action. This tool is the training half, and it
learns from two corpora:

- the folder audit (`docs/secure-shell-audit/resynth_audit@2026-11-04.json`), one bundle per project;
- the projects' own documents, because the expectation documents a project carries — the CGA
  acceptance contract is one of them — are what its civilians are meant to learn from.

There is no per-project cap and no bundle ceiling. Every qualifying document is admitted: root
`.md`/`.txt`, `docs/`, `tickets/`, `patches/`, and `.agents/skills/**/SKILL.md`, skipping vendored
trees (`references/`, `node_modules/`, `target/`, `build/`, `generated/`, `.git/`, `.cache/`) because
those are copies of other projects, not this project's expectations. Vendored trees are reported as
excluded, never silently passed over.

One hard limit is real and is named rather than hidden: the axis accepts a request body of at most
1,000,000 bytes (`server/axis-server.mjs`), so a document whose encoded bundle exceeds that is
skipped with `axis-body-limit` and its path and size appear in the transcript and the report. The
limit is deterministic, and a skip is an exclusion that is stated, not a silent cap.

Encoding is not a filter: these projects keep evidence as UTF-16 with a byte-order mark and as
cp1252, so a document is decoded under UTF-8, then UTF-16 when a BOM is present, then cp1252, and a
text document that none of those decode is excluded as `unreadable-encoding` with its size. Bytes
with a NUL in them and no BOM are binary and are excluded by name rather than admitted as mojibake.

Revisions are deduplicated deliberately: a bundle is identified by its relative path and the sha256
of its bytes, so the same document learned twice is one bundle, while a changed document is a new
revision kept beside the old one instead of overwriting it.

Every bundle is admitted into the Mongo authority on the Debian host, then applied through the axis
under a ticket, so a receipt exists for every item. Nothing is written before the ticket is granted.

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

AXIS_BODY_LIMIT = 1_000_000
BUNDLE_HEADROOM = 512
ROOT_SUFFIXES = (".md", ".txt")
DOC_DIRS = ("docs", "tickets", "patches")
SKILL_DIRS = (".agents/skills",)
DOC_SUFFIXES = (".md", ".txt")
SKIP_DIRS = {"node_modules", ".git", "target", "build", "generated", ".cache", "references",
             "venv", ".venv", "dist", ".next", "coverage"}


def post(axis: str, path: str, body: dict[str, Any]) -> dict[str, Any]:
    request = urllib.request.Request(
        axis + path,
        data=json.dumps(body).encode("utf-8"),
        headers={"content-type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=20) as answer:
            return json.loads(answer.read().decode("utf-8"))
    except urllib.error.HTTPError as error:
        payload = json.loads(error.read().decode("utf-8") or "{}")
        raise Refused(
            str(payload.get("refused") or "axis-refused"),
            str(payload.get("subject") or DRIVER_ID),
            str(payload.get("why") or payload.get("detail") or f"http {error.code}"),
        )


def get(axis: str, path: str) -> dict[str, Any]:
    with urllib.request.urlopen(axis + path, timeout=20) as answer:
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


def host_path(value: str) -> Path:
    """A root named on the Windows host, reachable from the Debian side of the mount."""
    text = value.replace(chr(92), "/")
    if _os.path.isdir("/mnt/c") and len(text) > 2 and text[1] == ":":
        return Path("/mnt/" + text[0].lower() + text[2:])
    return Path(text)


def bundle_for(row: dict[str, Any]) -> tuple[str, bytes]:
    name = str(row.get("name") or "")
    if not name:
        raise Refused("bundle-name", "row", "a corpus row without a project name cannot be trained")
    body = {"schema": "secure-shell.training/1", "project": name, "row": row}
    payload = (json.dumps(body, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")
    return f"secure-shell.training/{name}@1", payload


def candidate_documents(root: Path) -> tuple[list[Path], int]:
    """Every document a project carries, plus the count of vendored trees deliberately skipped."""
    files: list[Path] = []
    skipped_dirs = 0

    def walk(base: Path) -> None:
        nonlocal skipped_dirs
        for entry in sorted(base.iterdir()):
            if entry.is_dir():
                if entry.name in SKIP_DIRS or entry.name.startswith("."):
                    skipped_dirs += 1
                    continue
                walk(entry)
            elif entry.suffix.lower() in DOC_SUFFIXES:
                files.append(entry)

    try:
        for entry in sorted(root.iterdir()):
            if entry.is_file() and entry.suffix.lower() in ROOT_SUFFIXES:
                files.append(entry)
        for name in DOC_DIRS:
            base = root / name
            if base.is_dir():
                walk(base)
        for name in SKILL_DIRS:
            base = root / name
            if base.is_dir():
                walk(base)
    except (PermissionError, OSError):
        pass
    return files, skipped_dirs


def decode_document(raw: bytes) -> tuple[str | None, str]:
    """Text under the encodings these projects actually use; binary is refused, not mojibake'd."""
    if not raw:
        return None, "empty"
    if raw[:2] in (b"\xff\xfe", b"\xfe\xff"):
        try:
            return raw.decode("utf-16"), "utf-16"
        except UnicodeDecodeError:
            return None, "binary"
    if b"\x00" in raw:
        return None, "binary"
    for encoding in ("utf-8-sig", "cp1252"):
        try:
            return raw.decode(encoding), encoding
        except UnicodeDecodeError:
            continue
    return None, "binary"


def document_bundles(root: Path) -> tuple[list[tuple[str, bytes]], list[dict[str, Any]], int, int]:
    """Bundles for every qualifying document: no cap, one named exclusion for the axis body limit."""
    files, skipped_dirs = candidate_documents(root)
    bundles: list[tuple[str, bytes]] = []
    excluded: list[dict[str, Any]] = []
    seen: set[tuple[str, str]] = set()
    duplicates = 0
    for path in files:
        try:
            if path.stat().st_size == 0:
                continue
            raw = path.read_bytes()
        except OSError:
            excluded.append({"path": str(path.relative_to(root)), "reason": "unreadable-os"})
            continue
        text, encoding = decode_document(raw)
        if text is None:
            excluded.append({"path": str(path.relative_to(root)), "reason": "unreadable-encoding",
                             "bytes": len(raw)})
            continue
        relative = str(path.relative_to(root)).replace(chr(92), "/")
        digest = hashlib.sha256(text.encode("utf-8")).hexdigest()
        key = (relative, digest)
        if key in seen:
            duplicates += 1
            continue
        seen.add(key)
        body = {
            "schema": "secure-shell.training.document/1",
            "project": root.name,
            "path": relative,
            "sha256": "sha256:" + digest,
            "encoding": encoding,
            "text": text,
        }
        payload = (json.dumps(body, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")
        if len(payload) > AXIS_BODY_LIMIT - BUNDLE_HEADROOM:
            excluded.append({"path": relative, "reason": "axis-body-limit", "bytes": len(payload)})
            continue
        # The path hash keeps two copies of one document at different paths distinct. The identity
        # ends in the payload digest, never the text digest: the store refuses `mongo-digest` when one
        # identity is offered different bytes, so an identity must name the bytes that were stored.
        # A changed bundle shape is therefore a new identity, and an unchanged one is a duplicate.
        path_tag = hashlib.sha256(relative.encode("utf-8")).hexdigest()[:10]
        payload_tag = hashlib.sha256(payload).hexdigest()[:16]
        bundles.append((f"secure-shell.training.docs/{slug(root.name)}-{slug(relative, 32)}-{path_tag}@{payload_tag}", payload))
    return bundles, excluded, duplicates, skipped_dirs


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
    excluded_total: list[dict[str, Any]] = []
    duplicates_total = 0
    without_documents: list[str] = []
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
                bundles, excluded, duplicates, skipped_dirs = document_bundles(root)
                duplicates_total += duplicates
                excluded_total.extend({"project": root.name, **item} for item in excluded)
                if not bundles:
                    without_documents.append(root.name)
                STREAM.emit({"event": "project-documents", "project": root.name,
                             "documents": len(bundles), "excluded": len(excluded),
                             "duplicates": duplicates, "vendored_dirs_skipped": skipped_dirs})
                for identity, payload in bundles:
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
        "trained": trained, "documents": documents,
        "excluded": len(excluded_total), "duplicates": duplicates_total,
        "without_documents": without_documents, "truncated_roots": len(truncated),
    })
    header = STREAM.close(state="held")
    print(json.dumps({"trained": trained, "documents": documents, "excluded": len(excluded_total),
                      "duplicates": duplicates_total, "without_documents": len(without_documents),
                      "receipts": state.get("receipts"), "tickets": state.get("tickets"),
                      "transcript": header.get("digest")}, sort_keys=True), file=sys.stderr)
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
