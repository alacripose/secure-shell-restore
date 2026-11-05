#!/usr/bin/env python3
"""Train the CUA axis drivers from this machine's projects, and prove the loop end to end.

The axis already owns the authority rules: a driver registers declared capabilities, attests, and may
only act under a ticket the axis issued for that exact action. This tool is the training half of that
contract. It reads the folder audit (`docs/secure-shell-audit/resynth_audit@2026-11-04.json`, written
by `tools/resynth_agents.py --report`) as the corpus, turns each project into a learning bundle,
admits that bundle into the Mongo authority on the Debian host, and then applies it through the axis
under a ticket, so a receipt exists for every project the driver learned from.

Nothing is written before the ticket is granted. A refusal from the axis stops that project and is
reported with its own code, and the tool exits non-zero rather than reporting a pass it did not get.

Two acts beyond learning are exercised because they are the autonomous controls the axis names:

  witness  — hash the corpus file the bundles were built from
  kernel   — a kernel-scoped action, allowed only because this driver declares `kernel`; the axis
             records the receipt and grants nothing the declaration did not already claim

Run it inside the Debian host, where the axis listens on loopback and the sealed Mongo credential
can be decrypted for the run:

  /opt/drill-venv/bin/python tools/cua_training.py --uri-file /run/drill-mongo.uri
"""

from __future__ import annotations

import os as _os
import sys
import sys as _sys

_sys.path.insert(0, _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))))

import argparse
import hashlib
import json
import time
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any

from blake3 import blake3

from impl.packages.identity import Refused
from impl.packages.mongo_store import admit as mongo_admit
from impl.packages.toolstream import ToolStream

DRIVER_ID = "project-corpus-driver"
DRIVER_REVISION = "1"
DRIVER_CAPABILITIES = ["witness", "learning-apply", "kernel"]
CORPUS = Path("docs/secure-shell-audit/resynth_audit@2026-11-04.json")
STREAM = ToolStream("cua-training")


def post(axis: str, path: str, body: dict[str, Any]) -> dict[str, Any]:
    request = urllib.request.Request(
        axis + path,
        data=json.dumps(body).encode("utf-8"),
        headers={"content-type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=10) as answer:
            return json.loads(answer.read().decode("utf-8"))
    except urllib.error.HTTPError as error:
        payload = json.loads(error.read().decode("utf-8") or "{}")
        raise Refused(
            str(payload.get("refused") or "axis-refused"),
            str(payload.get("subject") or DRIVER_ID),
            str(payload.get("why") or payload.get("detail") or f"http {error.code}"),
        )


def get(axis: str, path: str) -> dict[str, Any]:
    with urllib.request.urlopen(axis + path, timeout=10) as answer:
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


def bundle_for(row: dict[str, Any]) -> tuple[str, bytes]:
    name = str(row.get("name") or "")
    if not name:
        raise Refused("bundle-name", "row", "a corpus row without a project name cannot be trained")
    body = {"schema": "secure-shell.training/1", "project": name, "row": row}
    payload = (json.dumps(body, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")
    return f"secure-shell.training/{name}@1", payload


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="cua_training")
    parser.add_argument("--axis", default=_os.environ.get("AXIS_URL", "http://127.0.0.1:8787"))
    parser.add_argument("--corpus", default=str(CORPUS))
    parser.add_argument("--uri-file", default="/run/drill-mongo.uri")
    parser.add_argument("--database", default="secure_shell")
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--ticks", type=int, default=1)
    args = parser.parse_args(argv)

    corpus = Path(args.corpus)
    if not corpus.is_file():
        raise Refused("corpus-absent", str(corpus), "run tools/resynth_agents.py --report first")
    rows = json.loads(corpus.read_text(encoding="utf-8"))["rows"]
    if args.limit:
        rows = rows[: args.limit]

    uri = Path(args.uri_file).read_text(encoding="utf-8").strip()
    trained = 0
    for tick in range(max(1, args.ticks)):
        until = int(time.time() * 1000) + 86_400_000
        register(args.axis, until)
        lapsed = get(args.axis, "/api/axis/review").get("review", [])
        STREAM.emit({"event": "tick", "tick": tick, "lapsed": len(lapsed), "projects": len(rows)})
        for row in rows:
            identity, payload = bundle_for(row)
            digest = "sha256:" + hashlib.sha256(payload).hexdigest()
            admitted = mongo_admit(uri, identity, {
                "name": identity.split("/", 1)[-1].split("@", 1)[0],
                "revision": 1,
                "schemas": ["secure-shell.training/1"],
                "dependencies": [],
                "entry_points": ["bundle.json"],
                "lengths": {"files": 1, "payload": len(payload)},
            }, payload, args.database)
            receipt = ticketed(args.axis, "learning-apply", {
                "bundle": {"bytes": payload.decode("utf-8"), "digest": digest},
            })
            if receipt.get("applied") is not True:
                raise Refused("training-not-applied", identity, "the axis recorded no applied receipt")
            trained += 1
            STREAM.emit({
                "event": "trained", "project": str(row.get("name")), "identity": identity,
                "store": admitted.get("digest"), "receipt": receipt.get("digest"),
                "duplicate": admitted.get("duplicate", False),
            })
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
        "tickets": state.get("tickets"), "receipts": state.get("receipts"), "trained": trained,
    })
    header = STREAM.close(state="held")
    print(json.dumps({"trained": trained, "receipts": state.get("receipts"),
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
