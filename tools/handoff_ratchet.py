#!/usr/bin/env python3
"""Handoff ratchet — owner ruling A-12, 2026-11-04.

A unit may not close unless a verification receipt from a second agent identity names the
trained axis driver ticket the unit handed off to. The author and the verifier must be
different identities: the agent must create the agent that verifies, so a self-verified
close is a refusal and not a pass.

Exit 0 only when the close is permitted. Every refusal prints one JSON line naming the
refusal code, the subject and the reason, and exits 1. There is no skip flag and no
environment bypass: an unreadable store is a refusal, never a pass.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STORE = ROOT / "docs" / "hypergrill" / "handoff@2026-11-04.jsonl"
SCHEMA = "secure-shell.handoff/1"

CLOSE_FIELDS = ("schema", "unit", "author", "driver_ticket")
RECEIPT_FIELDS = ("schema", "unit", "author", "verifier", "driver_ticket", "result", "evidence", "at")

REFUSALS = {
    "handoff-absent": "no verification receipt names this unit",
    "handoff-driver-unnamed": "the close names no driver ticket, or the receipts name a different one",
    "handoff-self-verified": "the verifier is the author; an agent may not verify its own handoff",
    "handoff-receipt-unreadable": "the store, the close or a receipt could not be read against the schema",
    "handoff-not-held": "the receipt does not carry result 'held'",
    "handoff-author-mismatch": "every receipt for this unit names a different author than the closing one",
}

CHECKS = (
    "list",
    "self-check",
    "close --close <unit-close.json> --store <receipts.jsonl>",
)


def emit(payload: dict) -> None:
    print(json.dumps(payload, sort_keys=True))


def refuse(code: str, subject: str, reason: str) -> int:
    emit({"schema": SCHEMA, "state": "refused", "refusal": code, "subject": subject, "reason": reason})
    return 1


def read_json(path: Path) -> tuple[dict | None, str]:
    try:
        return json.loads(path.read_text(encoding="utf-8")), ""
    except FileNotFoundError:
        return None, f"{path} does not exist"
    except (OSError, ValueError) as exc:
        return None, f"{path}: {exc}"


def read_receipts(path: Path) -> tuple[list[dict], str]:
    try:
        text = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        return [], f"{path} does not exist"
    except OSError as exc:
        return [], f"{path}: {exc}"
    receipts: list[dict] = []
    for number, line in enumerate(text.splitlines(), start=1):
        line = line.strip()
        if not line:
            continue
        try:
            record = json.loads(line)
        except ValueError as exc:
            return [], f"{path}:{number}: {exc}"
        if not isinstance(record, dict):
            return [], f"{path}:{number}: not an object"
        missing = [field for field in RECEIPT_FIELDS if not str(record.get(field, "")).strip()]
        if missing:
            return [], f"{path}:{number}: missing {', '.join(missing)}"
        if record.get("schema") != SCHEMA:
            return [], f"{path}:{number}: schema is not {SCHEMA}"
        if not re.match(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}", str(record["at"])):
            return [], f"{path}:{number}: at is not an ISO date"
        if ":" not in str(record["evidence"]) and "/" not in str(record["evidence"]):
            return [], f"{path}:{number}: evidence is neither a path nor a path:line"
        receipts.append(record)
    return receipts, ""


def decide(close: dict, receipts: list[dict]) -> tuple[int, dict]:
    """Return (exit code, payload). The order of refusals is the order of the register."""
    unit = str(close["unit"]).strip()
    author = str(close["author"]).strip()
    driver = str(close.get("driver_ticket", "")).strip()
    if not driver:
        return 1, {"refusal": "handoff-driver-unnamed", "subject": unit,
                   "reason": "the close names no driver ticket"}
    for_unit = [r for r in receipts if str(r.get("unit", "")).strip() == unit]
    if not for_unit:
        return 1, {"refusal": "handoff-absent", "subject": unit,
                   "reason": "no receipt for this unit in the store"}
    # A receipt written by somebody else about this unit's id is not evidence about this author's
    # work. Without this, a receipt from any other author would satisfy the second-identity rule.
    same_author = [r for r in for_unit
                   if str(r.get("author", "")).strip().casefold() == author.casefold()]
    if not same_author:
        others = sorted({str(r.get("author", "")).strip() for r in for_unit})
        return 1, {"refusal": "handoff-author-mismatch", "subject": unit,
                   "reason": "receipts name %s, not %s" % (", ".join(others) or "nobody", author)}
    for_driver = [r for r in same_author if str(r.get("driver_ticket", "")).strip() == driver]
    if not for_driver:
        named = sorted({str(r.get("driver_ticket", "")).strip() for r in for_unit})
        return 1, {"refusal": "handoff-driver-unnamed", "subject": unit,
                   "reason": f"receipts name {', '.join(named) or 'nothing'}, not {driver}"}
    second = [r for r in for_driver
              if str(r.get("verifier", "")).strip().casefold() != author.casefold()]
    if not second:
        return 1, {"refusal": "handoff-self-verified", "subject": unit,
                   "reason": f"the only verifier is the author ({author})"}
    held = [r for r in second if str(r.get("result", "")).strip() == "held"]
    if not held:
        states = sorted({str(r.get("result", "")).strip() for r in second})
        return 1, {"refusal": "handoff-not-held", "subject": unit,
                   "reason": f"second-identity receipts report {', '.join(states) or 'no result'}"}
    return 0, {"state": "permitted", "unit": unit, "driver_ticket": driver,
               "author": author, "verifier": str(held[0]["verifier"]).strip(),
               "receipt_digest": hashlib.sha256(
                   json.dumps(held[0], sort_keys=True).encode("utf-8")).hexdigest()[:16]}


def run_close(close_path: Path, store_path: Path) -> int:
    close, why = read_json(close_path)
    if close is None:
        return refuse("handoff-receipt-unreadable", str(close_path), why)
    missing = [field for field in CLOSE_FIELDS if not str(close.get(field, "")).strip()]
    if missing:
        return refuse("handoff-receipt-unreadable", str(close_path), "missing " + ", ".join(missing))
    if close.get("schema") != SCHEMA:
        return refuse("handoff-receipt-unreadable", str(close_path), f"schema is not {SCHEMA}")
    receipts, why = read_receipts(store_path)
    if why:
        return refuse("handoff-receipt-unreadable", str(store_path), why)
    code, payload = decide(close, receipts)
    if code == 0 and payload.get("state") == "permitted":
        digest = payload["receipt_digest"]
        emit({"schema": SCHEMA, "state": "permitted", "unit": payload["unit"],
              "driver_ticket": payload["driver_ticket"], "author": payload["author"],
              "verifier": payload["verifier"], "receipt_digest": digest})
        return 0
    return refuse(payload["refusal"], payload["subject"], payload["reason"])


def self_check() -> int:
    """Assert the contract on a throwaway store. Nothing here touches the real record."""
    failures: list[str] = []
    with tempfile.TemporaryDirectory() as tmp:
        base = Path(tmp)
        close = {"schema": SCHEMA, "unit": "TICKET-9001", "author": "agent:author",
                 "driver_ticket": "TICKET-0100", "at": "2026-11-04T00:00:00Z"}
        close_path = base / "close.json"
        close_path.write_text(json.dumps(close), encoding="utf-8")

        def receipt(**over: object) -> dict:
            row = {"schema": SCHEMA, "unit": "TICKET-9001", "author": "agent:author",
                   "verifier": "agent:verifier", "driver_ticket": "TICKET-0100",
                   "result": "held", "evidence": "self-check:1",
                   "at": "2026-11-04T00:00:00Z"}
            row.update(over)
            return row

        cases = {
            "an absent receipt is refused": ([], 1, "handoff-absent"),
            "a second identity that held is permitted": ([receipt()], 0, ""),
            "the author verifying itself is refused": (
                [receipt(verifier="agent:author")], 1, "handoff-self-verified"),
            "a receipt naming another driver is refused": (
                [receipt(driver_ticket="TICKET-0999")], 1, "handoff-driver-unnamed"),
            "a verifier that did not hold is refused": (
                [receipt(result="refused")], 1, "handoff-not-held"),
            "a receipt from another author is refused": (
                [receipt(author="agent:other")], 1, "handoff-author-mismatch"),
            "a receipt without an ISO date is refused": (
                [receipt(at="later")], 1, "handoff-receipt-unreadable"),
            "an unreadable receipt line is refused": (
                [receipt(evidence="")], 1, "handoff-receipt-unreadable"),
        }
        for label, (rows, want_code, want_refusal) in cases.items():
            store = base / "receipts.jsonl"
            store.write_text("".join(json.dumps(r) + "\n" for r in rows), encoding="utf-8")
            got = run_close_capture(close_path, store)
            ok = got["exit"] == want_code and got.get("refusal", "") == want_refusal
            if not ok:
                failures.append(f"{label}: exit {got['exit']}, refusal {got.get('refusal', '')!r}")
        missing = run_close_capture(base / "close.json", base / "nothing.jsonl")
        if missing["exit"] != 1 or missing.get("refusal") != "handoff-receipt-unreadable":
            failures.append("a missing store is not a pass")
    for line in failures:
        print("FAIL " + line)
    print(f"RESULT: {'PASS' if not failures else 'FAIL'} ({len(failures)} failed)")
    return 0 if not failures else 1


def run_close_capture(close_path: Path, store_path: Path) -> dict:
    import io
    from contextlib import redirect_stdout
    buffer = io.StringIO()
    with redirect_stdout(buffer):
        code = run_close(close_path, store_path)
    payload = json.loads(buffer.getvalue().strip().splitlines()[-1])
    payload["exit"] = code
    return payload


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description="Handoff ratchet (owner ruling A-12)")
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("list", help="enumerate the checks and the refusal set")
    sub.add_parser("self-check", help="assert the contract on a throwaway store")
    close_cmd = sub.add_parser("close", help="decide whether a unit may close")
    close_cmd.add_argument("--close", required=True, type=Path)
    close_cmd.add_argument("--store", type=Path, default=STORE)
    args = parser.parse_args(argv)

    if args.command == "list":
        emit({"schema": SCHEMA, "checks": list(CHECKS), "refusals": REFUSALS,
              "store": str(STORE.relative_to(ROOT))})
        return 0
    if args.command == "self-check":
        return self_check()
    return run_close(args.close.expanduser(), args.store.expanduser())


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
