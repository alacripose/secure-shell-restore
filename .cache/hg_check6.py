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
check("block: nineteen resolved",
      sum(1 for q in block if questions[q]["status"] == "resolved") == 19)
check("block: Q140 struck", questions["Q140"]["status"] == "struck")
check("N055 resolved", questions["N055"]["status"] == "resolved")
check("N055 closed by the owner", questions["N055"]["class"] == "owner")

open_ids = [q for q, e in questions.items() if e["status"] == "open"]
print("open:", open_ids)
check("nothing is open", not open_ids, str(open_ids))

for q, status in (("Q137", "resolved"), ("Q138", "resolved"), ("Q139", "resolved"), ("Q140", "struck"), ("N055", "resolved")):
    rows = [r for r in receipts if r["question"] == q]
    check(f"{q} closed as {status}", bool(rows) and rows[-1]["status"] == status,
          rows[-1]["status"] if rows else "no receipt")

owner_verbatims = {r["question"] for r in receipts if r.get("class") == "owner" and r.get("verbatim")}
expected = {"N052", "Q137", "Q138", "Q139", "N055"}
check("every owner answer is recorded verbatim", owner_verbatims == expected,
      f"got {sorted(owner_verbatims)}")

node_mentions = [r["question"] for r in receipts
                 if "headless" in (r.get("resolution") or "").lower()]
check("only Q129 carries the refused Node clause", node_mentions == ["Q129"], str(node_mentions))

ws = pathlib.Path("docs/SECURE-SHELL-RESTORE@1.HYPERGRILL.md")
raw = ws.read_bytes()
text = raw.decode("utf-8")
m = re.search(r"holds (\d+) entries: (\d+) resolved, (\d+) folded, (\d+) struck, (\d+) open", text)
check("8.3 states all four counters", bool(m))
if m:
    doc = tuple(int(x) for x in m.groups())
    live = (len(questions), counts.get("resolved", 0), counts.get("folded", 0),
            counts.get("struck", 0), counts.get("open", 0))
    check("8.3 counters match state exactly", doc == live, f"doc {doc} state {live}")
m = re.search(r"Receipts on file: (\d+)", text)
check("8.3 receipt count matches the file", bool(m) and int(m.group(1)) == len(receipts))
check("remaining spine still 367", "Remaining spine: 367 of 500." in text)

for words in ("Kept forever; receipts and their evidence are never removed",
              "Publishable in full, including evidence refs", "all 3",
              "the node cua driver is the operation layer"):
    check(f"worksheet records: {words[:38]}", words in text)

check("8.5 register present", "## 8.5 Authorization violation register" in text)
check("AV-001 recorded", "AV-001" in text)
check("AV-001 cites the sibling checkout", "ala-civ-bots-prototype:CHECKPOINT.md:" in text)
check("AV-001 records the perf test as absent", "**`absent`.**" in text)
check("AV-001 records the owner's answer", "**Answered 2026-11-04 (N055).**" in text)

civ = pathlib.Path("docs/SECURE-SHELL-RESTORE@1.CUA-CIVILIAN-ACCEPTANCE.md")
civ_raw = civ.read_bytes()
check("civilian acceptance names its operation layer", b"## Operation layer" in civ_raw)
check("civilian acceptance names the Node CUA driver", b"Node CUA driver" in civ_raw)
check("civilian acceptance has no CR", b"\r" not in civ_raw)
check("worksheet has no CR", b"\r" not in raw, str(raw.count(b"\r")))
check("AGENTS.md still 15 sections",
      len(re.findall(rb"^## ", pathlib.Path("AGENTS.md").read_bytes(), re.M)) == 15)
check("DECISIONS.md still absent", not pathlib.Path("docs/DECISIONS.md").exists())

print(f"\nRESULT: {'PASS' if not failures else 'FAIL ' + str(failures)}")
sys.exit(0 if not failures else 1)
