import json
import pathlib
import re
import sys

failures = []


def check(name, ok, detail=""):
    print(f"{'PASS' if ok else 'FAIL'}  {name}{'' if ok else '  <- ' + detail}")
    if not ok:
        failures.append(name)


state = json.loads(pathlib.Path("docs/hypergrill/state.json").read_text(encoding="utf-8"))
questions = state.get("questions", state)
entries = questions.values() if isinstance(questions, dict) else questions
counts = {"resolved": 0, "open": 0, "folded": 0, "struck": 0}
own_answers = []
for entry in entries:
    if not isinstance(entry, dict):
        continue
    status = entry.get("status")
    if status in counts:
        counts[status] += 1
    if entry.get("class") == "owner" and status == "resolved":
        own_answers.append(entry.get("id"))

print("state counts:", counts)
check("nothing is open", counts["open"] == 0, f"open={counts['open']}")
check("nothing new was folded", counts["folded"] == 1, f"folded={counts['folded']}")
check("resolved is 138", counts["resolved"] == 138, f"{counts['resolved']}")
check("N052 is resolved", "N052" in own_answers, str(own_answers))

receipts = [json.loads(line) for line in
            pathlib.Path("docs/hypergrill/receipts.jsonl").read_text(encoding="utf-8").strip().splitlines()]
print("receipts:", len(receipts))
check("20 receipts", len(receipts) == 20, str(len(receipts)))
n052 = [r for r in receipts if r.get("question") == "N052"]
check("the owner receipt quotes the owner",
      bool(n052) and n052[-1].get("verbatim") == "One successful mount plus a render witness",
      str(n052[-1:]))
check("the driver did not sign the owner's answer",
      bool(n052) and n052[-1].get("class") == "owner")

every = [r["question"] for r in receipts if r.get("question")]
check("every receipt names a question", all(q for q in every))
check("no receipt is a duplicate of another question's closure",
      len(set(every)) == len(every), f"{len(set(every))} unique vs {len(every)}")

worksheet = pathlib.Path("docs/SECURE-SHELL-RESTORE@1.HYPERGRILL.md").read_text(encoding="utf-8")
check("the round is recorded verbatim", "One successful mount plus a render witness" in worksheet)
check("the round states zero remaining", "**0 remaining.**" in worksheet)

raw = pathlib.Path("AGENTS.md").read_bytes()
text = raw.decode("utf-8")
check("AGENTS.md keeps 15 sections", len(re.findall(r"^## ", text, re.M)) == 15)
check("AGENTS.md has no CR", b"\r" not in raw)
check("AGENTS.md records the driver-loop ruling",
      "The driver loop governs; manual rounds are the fallback" in text)
check("DECISIONS.md still absent", not pathlib.Path("docs/DECISIONS.md").exists())

print(f"\nRESULT: {'PASS' if not failures else 'FAIL ' + str(failures)}")
sys.exit(0 if not failures else 1)
