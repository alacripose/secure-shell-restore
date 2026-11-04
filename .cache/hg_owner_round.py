import json
import pathlib
import re
import subprocess
import sys
import tempfile

WS = pathlib.Path("docs/SECURE-SHELL-RESTORE@1.HYPERGRILL.md")
STATE = pathlib.Path("docs/hypergrill/state.json")
RECEIPTS = pathlib.Path("docs/hypergrill/receipts.jsonl")

WORDS = {
    "Q137": "Kept forever; receipts and their evidence are never removed",
    "Q138": "Publishable in full, including evidence refs",
    "Q139": "all 3",
    "Q140": ("False, we have node cua bots in ala-civ-bots-prototype, another authorization violation "
             "that will have to be refused and backwalked against the hypergrilling tree through an "
             "automated audit to see where such a thing came from, which was the performance test for "
             "the 1000 cua drivers"),
}

ROUND = {
    "Q137": "How long are mount receipts retained before retention removes the vault blobs they point at?",
    "Q138": "May mount receipts leave the machine — published, exported or shared outside it?",
    "Q139": "What counts as a successful acceptance day?",
    "Q140": "May the driver witness its own mount and count that as receipt evidence?",
}

N055 = {
    "id": "N055",
    "text": ("Given that `ala-civ-bots-prototype` runs Node CUA bots and the 1000-driver performance test "
             "ran on them, what authorization does a Node-driven CUA witness carry: may such a bot's own "
             "mount observation count as receipt evidence, and what must be refused?"),
    "class": "owner",
    "status": "open",
    "ruling": "",
}


def write_round_block(counts, entries, receipts):
    text = WS.read_text(encoding="utf-8")
    rows = "\n".join(
        f"| `{qid}` | {ROUND[qid]} | \"{WORDS[qid]}\" | {'answered' if qid != 'Q140' else 'struck — premise false'} |"
        for qid in ("Q137", "Q138", "Q139", "Q140"))

    block = f"""## 8.3 Driver progress (2026-11-04)

| Block | Seeded | Closed | Open |
|---|---|---|---|
| Carried set (Appendix C) | 20 | 20 | 0 |
| Stream protocol (Appendix D) | 20 | 20 | 0 |
| Mount receipts (Appendix E) | 20 | 20 | 0 |
| **Worked so far** | **60** | **60** | **0** |

`state.json` holds {entries} entries: {counts.get('resolved', 0)} resolved, {counts.get('folded', 0)} folded, \
{counts.get('struck', 0)} struck, {counts.get('open', 0)} open. Receipts on file: {receipts}. \
Remaining spine: 367 of 500.

## 8.4 Round held 2026-11-04 (v2.2): mount receipts

Four questions put to the owner. Three were answered; the fourth was struck because its premise was
false. Nothing was folded to keep the block tidy, and no open question was left unasked.

| Id | Question | Owner's words | State |
|---|---|---|---|
{rows}

**State:** asked 4 · answered 3 · struck 1 · open 0 · superseded 0 — **0 remaining.**

`Q140` is struck, not answered. The question rested on the rule that a Node, headless or separate-page
check is not a witness; the owner reports the family does not keep that rule, since
`ala-civ-bots-prototype` runs Node CUA bots and the 1000-driver performance test ran on them. A question
whose premise died keeps its id and is closed with its reason. The authorship question beneath it is
reopened as `N055` and asked.

| Id | Question | Class | State |
|---|---|---|---|
| `N055` | What authorization does a Node-driven CUA witness carry? | `owner` | open |
"""

    pattern = re.compile(r"## 8\.3 Driver progress.*?(?=## Appendix A —)", re.S)
    if not pattern.search(text):
        raise SystemExit("section 8.3 not found")
    WS.write_bytes(pattern.sub(block + "\n", text, count=1).encode("utf-8"))


def seed_n055():
    state = json.loads(STATE.read_text(encoding="utf-8"))
    if "N055" not in state["questions"]:
        entry = dict(N055)
        entry["evidence"] = [{
            "kind": "owner",
            "ref": "docs/SECURE-SHELL-RESTORE@1.HYPERGRILL.md#8.4",
            "note": "verbatim: " + json.dumps(WORDS["Q140"])[:160],
        }]
        state["questions"]["N055"] = entry
        STATE.write_bytes((json.dumps(state, indent=2, sort_keys=True) + "\n").encode("utf-8"))


def resolve_owner():
    ok, refused = [], []
    for qid in ("Q137", "Q138", "Q139"):
        receipt = {
            "question": qid,
            "class": "owner",
            "verbatim": WORDS[qid],
            "evidence": [{"kind": "owner",
                          "ref": "docs/SECURE-SHELL-RESTORE@1.HYPERGRILL.md#8.4",
                          "note": "verbatim: " + WORDS[qid]}],
        }
        if qid == "Q137":
            receipt["resolution"] = ("Retention never removes a mount receipt or the evidence it points "
                                     "at. The retention action covers encrypted vault blobs of conversation "
                                     "text only; no receipt is ever named in a retention row.")
            receipt["effect"] = ("The store-security retention policy drops any receipt window. Backups must "
                                 "preserve receipts and their evidence indefinitely.")
        elif qid == "Q138":
            receipt["resolution"] = ("Receipts may leave the machine in full, evidence refs included. There is "
                                     "no redaction projection and no withheld field.")
            receipt["effect"] = ("The receipt format is designed for disclosure; the client gains a full export "
                                 "path and redaction is not a requirement.")
        else:
            receipt["resolution"] = ("All three, in order: a recorded workday of cadence ticks, then the "
                                     "24-hour continuous simulation, then a count of independently verified "
                                     "tasks. A day passes only when all three hold.")
            receipt["effect"] = ("The acceptance gate is threefold and sequential; the section 6 residue closes "
                                 "and the civilian acceptance document adopts the triple.")
        with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False, encoding="utf-8") as fh:
            json.dump(receipt, fh)
            tmp = fh.name
        proc = subprocess.run([sys.executable, "tools/hypergrill_resolver.py", "resolve", "--owner", tmp],
                              capture_output=True, text=True)
        out = (proc.stdout or proc.stderr).strip()
        print(f"{qid} exit={proc.returncode} {out.splitlines()[0] if out else '<no output>'}")
        (ok if proc.returncode == 0 else refused).append(qid)
    return ok, refused


def strike_q140():
    reason = ("premise false: the family does run Node CUA bots (ala-civ-bots-prototype) and the "
              "1000-driver performance test ran on them. Owner: " + WORDS["Q140"])
    proc = subprocess.run([sys.executable, "tools/hypergrill_resolver.py", "strike", "Q140",
                           "--ref", "docs/SECURE-SHELL-RESTORE@1.HYPERGRILL.md#8.4",
                           "--reason", reason], capture_output=True, text=True)
    out = (proc.stdout or proc.stderr).strip()
    print(f"Q140 strike exit={proc.returncode} {out.splitlines()[0] if out else '<no output>'}")
    return proc.returncode == 0


def snapshot():
    state = json.loads(STATE.read_text(encoding="utf-8"))
    entries = state["questions"]
    counts = {"resolved": 0, "open": 0, "folded": 0, "struck": 0}
    for entry in entries.values():
        counts[entry["status"]] = counts.get(entry["status"], 0) + 1
    receipts = RECEIPTS.read_text(encoding="utf-8").strip().splitlines()
    return counts, len(entries), len(receipts)


def main():
    counts, entries, receipts = snapshot()
    # The owner's words must be in the document before the --owner gate reads them.
    write_round_block(counts, entries, receipts)
    ok, refused = resolve_owner()
    struck = strike_q140()
    seed_n055()
    counts, entries, receipts = snapshot()
    write_round_block(counts, entries, receipts)
    print("state:", counts, "entries:", entries, "receipts:", receipts)

    good = (not refused and struck and counts["resolved"] == 177 and counts["struck"] == 1
            and counts["open"] == 1 and counts["folded"] == 1 and entries == 180
            and receipts == 60)
    print("RESULT:", "PASS" if good else "FAIL")
    return 0 if good else 1


if __name__ == "__main__":
    sys.exit(main())
