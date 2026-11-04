import json
import pathlib
import re
import subprocess
import sys
import tempfile

failures = []


def check(name, ok, detail=""):
    print(f"{'PASS' if ok else 'FAIL'}  {name}{'' if ok else '  <- ' + detail}")
    if not ok:
        failures.append(name)


receipt = {
    "question": "N052",
    "class": "owner",
    "evidence": [
        {
            "kind": "owner",
            "ref": "docs/SECURE-SHELL-RESTORE@1.HYPERGRILL.md#8.2",
            "note": "verbatim: \"One successful mount plus a render witness\"",
        }
    ],
    "resolution": (
        "A successful mount that renders and produces a client witness is enough to record the mount "
        "as healthy. The scheduled 24-hour run is not a precondition, and the grade is not withheld "
        "pending it."
    ),
    "effect": (
        "The drive loop may raise a degraded observation to healthy on one rendering mount, and must "
        "cite that mount's witness as the evidence in the ledger row."
    ),
}

with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False, encoding="utf-8") as fh:
    json.dump(receipt, fh)
    tmp = fh.name
proc = subprocess.run([sys.executable, "tools/hypergrill_resolver.py", "resolve", tmp],
                      capture_output=True, text=True)
text = (proc.stdout or proc.stderr).strip()
print("N052 exit=%d %s" % (proc.returncode, text[:200]))
check("the owner answer was accepted as owner evidence", proc.returncode == 0, text[:200])

state = json.loads(pathlib.Path("docs/hypergrill/state.json").read_text(encoding="utf-8"))
questions = state.get("questions", state)
entries = questions.values() if isinstance(questions, dict) else questions
counts = {"resolved": 0, "open": 0, "folded": 0}
for entry in entries:
    status = entry.get("status") if isinstance(entry, dict) else None
    if status in counts:
        counts[status] += 1
print("state counts:", counts)
check("nothing is open", counts["open"] == 0, f"open={counts['open']}")
check("nothing new was folded", counts["folded"] == 1, f"folded={counts['folded']}")
check("the resolved count includes the owner answer", counts["resolved"] == 138, f"{counts['resolved']}")

worksheet = pathlib.Path("docs/SECURE-SHELL-RESTORE@1.HYPERGRILL.md").read_text(encoding="utf-8")
check("the round is recorded verbatim",
      "One successful mount plus a render witness" in worksheet)
check("the round states zero remaining", "**0 remaining.**" in worksheet)

receipts = pathlib.Path("docs/hypergrill/receipts.jsonl").read_text(encoding="utf-8").strip().splitlines()
print("receipts:", len(receipts))
check("every closed ticket in this tick left a receipt", len(receipts) >= 20, f"{len(receipts)}")

agents = pathlib.Path("AGENTS.md")
raw = agents.read_bytes()
text_agents = raw.decode("utf-8")
check("AGENTS.md unchanged in shape", len(re.findall(r"^## ", text_agents, re.M)) == 15)
check("AGENTS.md has no CR", b"\r" not in raw)
check("DECISIONS.md still absent", not pathlib.Path("docs/DECISIONS.md").exists())

print(f"\nRESULT: {'PASS' if not failures else 'FAIL ' + str(failures)}")
sys.exit(0 if not failures else 1)
