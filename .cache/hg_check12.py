"""Check the handoff gate: the enumerated entry a unit cannot close past.

`A-12` requires a unit close to carry a verification receipt from an identity that is not the author,
naming the driver ticket the unit handed off to. `tools/handoff_ratchet.py` decides that; this file is
the enumerated check that runs the decision, so the decision cannot be stepped around by not invoking
it.

Every case below is a real subprocess call, and the expected statuses are the register's, not this
file's opinion:

| case | inputs | expected |
|---|---|---|
| no receipt | a zero-byte store | exit 1, `handoff-absent` |
| second identity, held | one receipt naming `TICKET-0100` | exit 0, permitted |
| author verifies itself | the same receipt with `verifier` = `author` | exit 1, `handoff-self-verified` |
| no store | a path that does not exist | exit 1, `handoff-receipt-unreadable` |
| committed closes | every `tickets/*.close.json` against the committed store | exit 0 each |

The last row is the gate. A close file committed without a receipt in
`docs/hypergrill/handoff@2026-11-04.jsonl` fails here, before it can merge.

This check enforces label difference between two identities, not minted identity. It does not sign
the store and does not open the `evidence` a receipt cites. Those limits are named in the register
and are not softened to make this pass.
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RATCHET = ROOT / "tools" / "handoff_ratchet.py"
REGISTER = ROOT / "docs" / "SECURE-SHELL-HEALTH@1.HANDOFF.md"
WORKFLOW = ROOT / ".github" / "workflows" / "hypergrill-audit.yml"
STORE = ROOT / "docs" / "hypergrill" / "handoff@2026-11-04.jsonl"
DRIVER = "TICKET-0100"

failures: list[str] = []
checks = 0


def check(name: str, ok: bool, detail: str = "") -> None:
    global checks
    checks += 1
    if ok:
        print("ok   %s" % name)
    else:
        print("FAIL %s%s" % (name, (": " + detail) if detail else ""))
        failures.append(name)


def run(close: Path, store: Path) -> tuple[int, dict]:
    proc = subprocess.run(
        [sys.executable, str(RATCHET), "close", "--close", str(close), "--store", str(store)],
        capture_output=True, text=True)
    line = (proc.stdout.strip().splitlines() or ["{}"])[-1]
    try:
        payload = json.loads(line)
    except ValueError:
        payload = {}
    return proc.returncode, payload


def enumerated() -> dict:
    proc = subprocess.run([sys.executable, str(RATCHET), "list"],
                          capture_output=True, text=True)
    if proc.returncode != 0:
        return {}
    try:
        return json.loads(proc.stdout)
    except ValueError:
        return {}


def main() -> int:
    if not RATCHET.is_file() or not REGISTER.is_file():
        print("refused: the ratchet or its register is missing")
        return 2

    listing = enumerated()
    codes = sorted(listing.get("refusals", {}))
    check("the ratchet enumerates its refusals", len(codes) == 6, str(codes))
    check("it names the driver-ticket refusal by name", "handoff-driver-unnamed" in codes)
    check("it names the self-verification refusal by name", "handoff-self-verified" in codes)
    check("no refusal name breaks the family schema",
          all(name.replace("-", "").isalnum() and name.islower() for name in codes), str(codes))

    register = REGISTER.read_text(encoding="utf-8")
    documented = sorted(set(
        line.split("`")[1] for line in register.splitlines()
        if line.startswith("| `handoff-") and line.count("`") >= 2))
    check("the register documents exactly the enumerated refusals", documented == codes,
          "%s vs %s" % (documented, codes))
    check("the register names this enumerated entry", "hg_check12" in register)

    runs = [line.strip() for line in WORKFLOW.read_text(encoding="utf-8").splitlines()
            if line.strip().startswith("run:") and "hg_check12.py" in line]
    check("CI executes this entry as a step", len(runs) == 1, str(runs))

    import tempfile
    with tempfile.TemporaryDirectory() as tmp:
        base = Path(tmp)
        close = {"schema": "secure-shell.handoff/1", "unit": "TICKET-9001",
                 "author": "agent:author", "driver_ticket": DRIVER,
                 "at": "2026-11-04T00:00:00Z"}
        close_path = base / "close.json"
        close_path.write_text(json.dumps(close), encoding="utf-8")

        def receipt(**over: object) -> dict:
            row = {"schema": "secure-shell.handoff/1", "unit": "TICKET-9001",
                   "author": "agent:author", "verifier": "agent:verifier",
                   "driver_ticket": DRIVER, "result": "held",
                   "evidence": "tests/handoff/receipts-valid.jsonl:1",
                   "at": "2026-11-04T00:00:00Z"}
            row.update(over)
            return row

        empty = base / "empty.jsonl"
        empty.write_text("", encoding="utf-8")
        code, payload = run(close_path, empty)
        check("a close with no receipt is refused handoff-absent",
              code == 1 and payload.get("refusal") == "handoff-absent",
              "exit %d, refusal %r" % (code, payload.get("refusal", "")))

        held = base / "held.jsonl"
        held.write_text(json.dumps(receipt()) + "\n", encoding="utf-8")
        code, payload = run(close_path, held)
        check("a second identity naming %s permits the close" % DRIVER,
              code == 0 and payload.get("state") == "permitted"
              and payload.get("driver_ticket") == DRIVER,
              "exit %d, state %r" % (code, payload.get("state", "")))

        selfy = base / "self.jsonl"
        selfy.write_text(json.dumps(receipt(verifier="agent:author")) + "\n", encoding="utf-8")
        code, payload = run(close_path, selfy)
        check("a self-verified close is refused, not permitted",
              code == 1 and payload.get("refusal") == "handoff-self-verified",
              "exit %d, refusal %r" % (code, payload.get("refusal", "")))

        absent = base / "nothing-here.jsonl"
        code, payload = run(close_path, absent)
        check("a missing store is refused, never a pass",
              code == 1 and payload.get("refusal") == "handoff-receipt-unreadable"
              and absent.name in str(payload.get("subject", "")),
              "exit %d, refusal %r, subject %r"
              % (code, payload.get("refusal", ""), payload.get("subject", "")))

    closes = sorted((ROOT / "tickets").glob("*.close.json"))
    check("the repository has a committed close to gate", bool(closes), str(closes))
    for path in closes:
        code, payload = run(path, STORE)
        check("the committed close %s is permitted" % path.name,
              code == 0 and payload.get("state") == "permitted",
              "exit %d, refusal %r" % (code, payload.get("refusal", "")))
        check("%s hands off to %s" % (path.name, DRIVER),
              payload.get("driver_ticket", json.loads(path.read_text(encoding="utf-8"))
                          .get("driver_ticket")) == DRIVER,
              str(payload.get("driver_ticket", "")))

    print("\n%d checks, %d failed" % (checks, len(failures)))
    if failures:
        print("failed: " + ", ".join(failures))
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
