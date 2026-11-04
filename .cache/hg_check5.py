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
questions = state["questions"]
counts = {}
for entry in questions.values():
    counts[entry["status"]] = counts.get(entry["status"], 0) + 1
print("state:", counts, "entries:", len(questions))

receipts = [json.loads(line) for line in
            pathlib.Path("docs/hypergrill/receipts.jsonl").read_text(encoding="utf-8").strip().splitlines()]
print("receipts:", len(receipts))

block = [f"Q{n}" for n in range(121, 141)]
resolved = [q for q in block if questions[q]["status"] == "resolved"]
open_ = [q for q in block if questions[q]["status"] == "open"]
check("block: nineteen resolved", len(resolved) == 19, str(len(resolved)))
check("block: Q140 struck", questions["Q140"]["status"] == "struck", questions["Q140"]["status"])
check("block: nothing open", not open_, str(open_))

check("N055 exists", "N055" in questions)
check("N055 is owner-class and open",
      questions["N055"]["class"] == "owner" and questions["N055"]["status"] == "open",
      f"{questions['N055']['class']}/{questions['N055']['status']}")
check("N055 carries evidence", bool(questions["N055"].get("evidence")))

open_ids = [q for q, e in questions.items() if e["status"] == "open"]
check("every open question is owner-class",
      all(questions[q]["class"] == "owner" for q in open_ids), str(open_ids))
check("every open question carries evidence",
      all(questions[q].get("evidence") for q in open_ids), str(open_ids))

by_q = {}
for r in receipts:
    by_q.setdefault(r["question"], []).append(r)
check("three owner answers recorded verbatim",
      all(by_q[q][-1].get("class") == "owner" and by_q[q][-1].get("verbatim") for q in ("Q137", "Q138", "Q139")))
check("Q140 closed by strike", by_q["Q140"][-1]["status"] == "struck", by_q["Q140"][-1]["status"])
check("no receipt claims a node witness rule", not any("headless" in (r.get("resolution") or "").lower()
                                                       for r in receipts))

ws = pathlib.Path("docs/SECURE-SHELL-RESTORE@1.HYPERGRILL.md")
raw = ws.read_bytes()
text = raw.decode("utf-8")

m = re.search(r"holds (\d+) entries: (\d+) resolved, (\d+) folded, (\d+) struck, (\d+) open", text)
check("8.3 states all four counters", bool(m), "no match")
if m:
    doc = tuple(int(x) for x in m.groups())
    live = (len(questions), counts.get("resolved", 0), counts.get("folded", 0),
            counts.get("struck", 0), counts.get("open", 0))
    check("8.3 counters match state exactly", doc == live, f"doc {doc} state {live}")

m = re.search(r"Receipts on file: (\d+)", text)
check("8.3 receipt count matches the file", bool(m) and int(m.group(1)) == len(receipts))
check("remaining spine still 367", "Remaining spine: 367 of 500." in text)
check("8.4 records the owner's words", "Kept forever; receipts and their evidence are never removed" in text)
check("8.4 records all three answers", "all 3" in text and "Publishable in full, including evidence refs" in text)
check("8.5 register present", "## 8.5 Authorization violation register" in text)
check("AV-001 recorded", "AV-001" in text)
check("AV-001 cites the sibling checkout", "ala-civ-bots-prototype:CHECKPOINT.md:" in text)
check("AV-001 records the perf test as absent", "**`absent`.**" in text)
check("worksheet has no CR", b"\r" not in raw, str(raw.count(b"\r")))

check("AGENTS.md still 15 sections",
      len(re.findall(rb"^## ", pathlib.Path("AGENTS.md").read_bytes(), re.M)) == 15)
check("DECISIONS.md still absent", not pathlib.Path("docs/DECISIONS.md").exists())

print(f"\nRESULT: {'PASS' if not failures else 'FAIL ' + str(failures)}")
sys.exit(0 if not failures else 1)
