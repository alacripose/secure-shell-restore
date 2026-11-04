#!/usr/bin/env python3
"""The handoff ratchet's three concrete cases, run from this repository's own tooling.

Case 1: a unit close with no receipt            -> exits non-zero, refuses `handoff-absent`
Case 2: the same close with a second-identity   -> exits zero, permitted
        receipt naming the driver ticket
Case 3: the same close verified by the author   -> exits non-zero, refuses `handoff-self-verified`

A case that does not do what this table says is a failure of the case, not of the ratchet,
and the runner exits 1. Run: python tests/handoff/run_cases.py
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
RATCHET = ROOT / "tools" / "handoff_ratchet.py"

CASES = (
    ("no receipt", "close-no-receipt.json", "receipts-empty.jsonl", 1, "handoff-absent"),
    ("second identity, held", "close-with-receipt.json", "receipts-valid.jsonl", 0, ""),
    ("author verifies itself", "close-self-verified.json", "receipts-self.jsonl", 1, "handoff-self-verified"),
)


def main() -> int:
    failed = 0
    for label, close, store, want_exit, want_refusal in CASES:
        proc = subprocess.run(
            [sys.executable, str(RATCHET), "close", "--close", str(HERE / close),
             "--store", str(HERE / store)],
            capture_output=True, text=True)
        line = (proc.stdout.strip().splitlines() or ["{}"])[-1]
        try:
            payload = json.loads(line)
        except ValueError:
            payload = {}
        refusal = payload.get("refusal", "")
        ok = proc.returncode == want_exit and refusal == want_refusal
        state = payload.get("state", "unreadable")
        print(f"{'ok  ' if ok else 'FAIL'} {label}: exit {proc.returncode}, state {state}"
              f"{', refusal ' + refusal if refusal else ''}")
        if not ok:
            print(f"     expected exit {want_exit}, refusal {want_refusal!r}")
            failed += 1
    print(f"{len(CASES)} cases, {failed} failed")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
