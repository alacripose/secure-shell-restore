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
check("158 resolved", counts.get("resolved") == 158, str(counts.get("resolved")))
check("0 open", counts.get("open", 0) == 0, str(counts.get("open")))
check("1 folded", counts.get("folded") == 1, str(counts.get("folded")))
check("159 entries", len(questions) == 159, str(len(questions)))

stream_ids = [f"Q{n}" for n in range(101, 121)]
check("all twenty stream questions are in state", all(q in questions for q in stream_ids))
check("all twenty are resolved",
      all(questions[q]["status"] == "resolved" for q in stream_ids))
check("each has evidence",
      all(questions[q].get("evidence") for q in stream_ids))

receipts = pathlib.Path("docs/hypergrill/receipts.jsonl").read_text(encoding="utf-8").strip().splitlines()
print("receipts:", len(receipts))
check("40 receipts", len(receipts) == 40, str(len(receipts)))
stream_receipts = [json.loads(r) for r in receipts if json.loads(r).get("question") in stream_ids]
check("every stream question left a receipt", len(stream_receipts) == 20, str(len(stream_receipts)))
check("no stream receipt is owner-class",
      all(r.get("class") != "owner" for r in stream_receipts))
for receipt in stream_receipts:
    for item in receipt["evidence"]:
        check(f"pin has a line number: {receipt['question']} {item['ref'][-24:]}",
              bool(re.search(r":\d+$", item["ref"])), item["ref"])

ws_path = pathlib.Path("docs/SECURE-SHELL-RESTORE@1.HYPERGRILL.md")
raw = ws_path.read_bytes()
text = raw.decode("utf-8")
check("worksheet has no CR", b"\r" not in raw, str(raw.count(b"\r")))
check("worksheet has Appendix D", "## Appendix D" in text)
check("worksheet has 8.3", "## 8.3 Driver progress (2026-11-04)" in text)
check("8.3 states the remaining spine", "Remaining spine: 387 of 500." in text)
rows = re.findall(r"^\| (Q1[0-2][0-9]) \|", text, re.M)
check("Appendix D has 20 rows", len(rows) == 20, str(len(rows)))
check("Appendix D ids are unique", len(set(rows)) == len(rows))

agents = pathlib.Path("AGENTS.md").read_bytes()
check("AGENTS.md still 15 sections",
      len(re.findall(rb"^## ", agents, re.M)) == 15)
check("DECISIONS.md still absent", not pathlib.Path("docs/DECISIONS.md").exists())

print(f"\nRESULT: {'PASS' if not failures else 'FAIL ' + str(failures)}")
sys.exit(0 if not failures else 1)
