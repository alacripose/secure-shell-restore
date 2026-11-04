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

block_ids = [f"Q{n}" for n in range(121, 141)]
check("all twenty receipt questions are seeded", all(q in questions for q in block_ids))
resolved = [q for q in block_ids if questions[q]["status"] == "resolved"]
open_ = [q for q in block_ids if questions[q]["status"] == "open"]
print("resolved:", len(resolved), "open:", len(open_), open_)
check("sixteen resolved", len(resolved) == 16, str(len(resolved)))
check("four held open", len(open_) == 4, str(len(open_)))
check("every held question is owner-class",
      all(questions[q]["class"] == "owner" for q in open_),
      str([questions[q]["class"] for q in open_]))
check("every held question carries its evidence",
      all(questions[q].get("evidence") for q in open_))

closed_receipts = {r["question"]: r for r in receipts if r.get("question") in block_ids}
check("every resolved question has a receipt",
      all(q in closed_receipts for q in resolved),
      str([q for q in resolved if q not in closed_receipts]))
check("no held question has a receipt", all(q not in closed_receipts for q in open_))
bad_pins = [(q, i["ref"]) for q, r in closed_receipts.items() for i in r["evidence"]
            if not re.search(r":\d+$", i["ref"])]
check("every pin ends in a line number", not bad_pins, str(bad_pins))
check("every receipt has two pins", all(len(r["evidence"]) >= 2 for r in closed_receipts.values()))

ws_path = pathlib.Path("docs/SECURE-SHELL-RESTORE@1.HYPERGRILL.md")
raw = ws_path.read_bytes()
text = raw.decode("utf-8")
check("worksheet has Appendix E", "## Appendix E" in text)
check("worksheet has 8.4", "## 8.4 Round held 2026-11-04" in text)
e_section = text.split("## Appendix E", 1)[1] if "## Appendix E" in text else ""
rows = re.findall(r"^\| (Q1[2-4][0-9]) \|", e_section, re.M)
check("Appendix E has 20 rows", len(rows) == 20, str(len(rows)))
check("Appendix E ids are unique", len(set(rows)) == len(rows))
check("Appendix E ids are Q121-Q140", rows == [f"Q{n}" for n in range(121, 141)], str(rows))

m = re.search(r"holds (\d+) entries: (\d+) resolved, (\d+) folded, (\d+) open", text)
check("8.3 states the counters", bool(m), "no match")
if m:
    doc_counts = tuple(int(x) for x in m.groups())
    check("8.3 entries match state", doc_counts[0] == len(questions), f"doc {doc_counts[0]} state {len(questions)}")
    check("8.3 resolved match state", doc_counts[1] == counts.get("resolved"), f"doc {doc_counts[1]} state {counts.get('resolved')}")
    check("8.3 folded match state", doc_counts[2] == counts.get("folded"), f"doc {doc_counts[2]} state {counts.get('folded')}")
    check("8.3 open match state", doc_counts[3] == counts.get("open", 0), f"doc {doc_counts[3]} state {counts.get('open')}")

m = re.search(r"Remaining spine: (\d+) of 500", text)
check("8.3 states the remaining spine", bool(m))
if m:
    check("remaining spine is 367", int(m.group(1)) == 367, m.group(1))

m = re.search(r"Receipts on file: (\d+)", text)
check("8.3 receipt count matches the file", bool(m) and int(m.group(1)) == len(receipts))

check("8.4 states four remaining", "**4 remaining.**" in text)
check("worksheet has no CR", b"\r" not in raw, str(raw.count(b"\r")))
check("AGENTS.md still 15 sections", len(re.findall(rb"^## ", pathlib.Path("AGENTS.md").read_bytes(), re.M)) == 15)
check("DECISIONS.md still absent", not pathlib.Path("docs/DECISIONS.md").exists())

print(f"\nRESULT: {'PASS' if not failures else 'FAIL ' + str(failures)}")
sys.exit(0 if not failures else 1)
