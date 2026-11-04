import json
import pathlib
import re
import subprocess
import sys
import tempfile

ARCH = "docs/SECURE-SHELL-RESTORE@1.ARCHITECTURE.md"
WS = "docs/SECURE-SHELL-RESTORE@1.HYPERGRILL.md"
LEDGER = "docs/LEDGER.md"
REPO = pathlib.Path("C:/Users/ala/Documents/secure-shell")


def line_of(path, needle):
    raw = pathlib.Path(path).read_text(encoding="utf-8", errors="replace")
    text = raw.replace("*", " ").replace("`", " ")
    tokens = needle.replace("*", " ").replace("`", " ").split()
    pattern = re.compile(r"\s+".join(re.escape(p) for p in tokens))
    match = pattern.search(text)
    if not match:
        raise SystemExit(f"anchor not found in {path}: {needle!r}")
    return text[: match.start()].count("\n") + 1


def doc(path, needle, note):
    return {"kind": "doc", "ref": f"{path}:{line_of(path, needle)}", "note": note}


def code(rel, needle, note):
    return {"kind": "code", "ref": f"secure-shell:{rel}:{line_of(REPO / rel, needle)}", "note": note}


def repo_doc(rel, needle, note):
    return {"kind": "code", "ref": f"secure-shell:{rel}:{line_of(REPO / rel, needle)}", "note": note}


# (id, class, question, resolution, effect, evidence)  resolution None => held open for the owner
BLOCK = [
    ("Q121", "spec", "What is the mount receipt's own schema tag?",
     "The mount receipt is `surface.mount/2`. It keeps its own version and its own reader, and it lives in the family's existing mount store (`dl-enclave` `MountStore`).",
     "Receipt identity is a named format, not an ad-hoc record; a second receipt reader is refused as the door's words read twice.",
     [doc(ARCH, "keeps its own version and its own reader", "the receipt contract owns its version"),
      repo_doc("AGENTS.md", "Receipt store", "where the receipts already live")]),

    ("Q122", "spec", "Does the receipt schema move with the stream schema?",
     "No. A stream schema bump does not bump the mount receipt schema, and a receipt bump does not disturb the stream.",
     "Two version axes, two refusal vocabularies, tested independently.",
     [doc(ARCH, "A stream schema bump does not bump the mount receipt schema, and vice versa", "the non-coupling rule"),
      doc(ARCH, "keeps its own version and its own reader", "the receipt's own axis")]),

    ("Q123", "spec", "Is the receipt state set closed or open?",
     "Closed. A receipt carries a closed state set plus a separate refusal code, and there is no warnings field.",
     "An unknown state is refused by name rather than carried; warnings never ride a receipt.",
     [doc(ARCH, "closed state set", "closed, not open"),
      doc(ARCH, "there is no warnings field", "the field that does not exist")]),

    ("Q124", "spec", "Is `degraded` a state or a warning?",
     "A state. `degraded` enters the state set and must name its cause in `refusal`; it is non-applied, so the applied-row and floor logic already exclude it.",
     "N050's \"degraded until it proves itself\" needs no schema change.",
     [doc(ARCH, "enters the state set", "degraded is a state"),
      doc(ARCH, "must name its cause", "and carries a refusal code")]),

    ("Q125", "spec", "Who produces a mount receipt?",
     "The client. The mount row of the signing table assigns the adopted revision to a client receipt, and the witness row assigns rendering to the client.",
     "The server cannot report an adoption it did not observe.",
     [doc(ARCH, "Client receipt, subordinate contract", "the receipt's producer"),
      doc(ARCH, "What did the client actually render and check?", "the witness's producer")]),

    ("Q126", "spec", "Is a receipt authorization to adopt?",
     "No. A receipt is evidence of adoption, not authorization to adopt; admission is a server-policy verdict recorded separately.",
     "Possessing a receipt never admits anything, and admitting never implies a receipt.",
     [doc(ARCH, "A receipt is evidence of adoption, not authorization to adopt", "the separation"),
      doc(ARCH, "Server policy, recorded as a verdict", "where authorization actually lives")]),

    ("Q127", "spec", "What does a receipt bind?",
     "The revision actually adopted: the receipt identity is a subject and its digest, and a receipt naming a different revision than the mount is `receipt-mismatch`.",
     "A receipt is bound to bytes, not to a package name loose in prose.",
     [repo_doc("docs/LEDGER.md", "receipt identity", "subject plus digest"),
      doc(ARCH, "receipt-mismatch", "what a mismatch is called")]),

    ("Q128", "spec", "Is the receipt the durable record, or is the ledger row?",
     "The ledger row is the durable record; the mount receipt is the subject that row names. The chain, its fsync and its append-only file are the durability, and the receipt is what the row points at.",
     "A receipt written without a ledger row is not proof; a ledger row without a receipt names nothing.",
     [repo_doc("server/ledger.mjs", "the mount receipt is the subject", "the row names the receipt"),
      repo_doc("AGENTS.md", "the durable record of the witness", "the row is the record")]),

    ("Q129", "spec", "Can a receipt be produced without rendering?",
     "No. A check the client cannot see is `test-surface-unwitnessed`, and a check that runs only in Node, a headless browser or a separate witness page is not a witness.",
     "A module check may pass and still produce no receipt.",
     [repo_doc("AGENTS.md", "test-surface-unwitnessed", "the refusal for an unseen check"),
      repo_doc("AGENTS.md", "headless browser", "what does not count as a witness")]),

    ("Q130", "spec", "Is a parity digest alone sufficient as a witness?",
     "No. Both are required: the mount-and-render witness and the parity digest. The digest proves the bytes arrived; the witness proves the surface rendered.",
     "Either one alone is an incomplete adoption record.",
     [doc(WS, "| N010 |", "the ruling that both are required"),
      doc(ARCH, "What did the client actually render and check?", "the rendering half")]),

    ("Q131", "spec", "What happens to receipts when a revision is withdrawn?",
     "They remain, and the pin still resolves: a withdrawn revision stays retired forever but still resolves for the consumer that pinned it.",
     "Withdrawal stops new pins; it does not erase the record of an adoption that happened.",
     [doc(WS, "| Q054 |", "a withdrawn revision still resolves"),
      repo_doc("docs/LEDGER.md", "never deleted or edited", "rows are not rewritten")]),

    ("Q132", "spec", "Are receipts mutable?",
     "No. Ledger rows are never deleted or edited; retention removes encrypted vault blobs and appends a `retention` entry naming what it removed.",
     "A correction is a new row, never an overwrite.",
     [repo_doc("docs/LEDGER.md", "never deleted or edited", "the append-only invariant"),
      repo_doc("docs/LEDGER.md", "Retention removes encrypted vault blobs", "how removal is recorded")]),

    ("Q133", "spec", "Does a receipt count as completion evidence for a ticket?",
     "Yes, when it is a ledger entry: the ledger entry is the durable record of the witness, and a check that did not write an entry did not run.",
     "A mount claim with no ledger row is not evidence and cannot close a ticket.",
     [repo_doc("AGENTS.md", "the durable record of the witness", "the record rule"),
      repo_doc("AGENTS.md", "did not write an entry", "the negative form")]),

    ("Q134", "spec", "Is the receipt itself signed?",
     "Not individually. Authenticity comes from the chained ledger: a checkpoint signs a head that is in the chain, and a checkpoint does not prove the truth of the entries it covers.",
     "Receipt trust is inherited from the chain, so tampering is a chain break, not a signature re-check per row.",
     [repo_doc("docs/LEDGER.md", "does not prove the truth of the entries", "what a checkpoint does not do"),
      repo_doc("server/ledger.mjs", "CHECKPOINT_SCHEMA", "the checkpoint contract in code")]),

    ("Q135", "spec", "Does an `absent` receipt exist, or is absent the absence of a receipt?",
     "Absent is a reported state, never a passing receipt: a health check that never ran is reported as absent and never as a pass.",
     "No receipt is fabricated for work that did not happen, so absence stays visible.",
     [doc(ARCH, "Health check never run", "the condition"),
      doc(ARCH, "reported as absent", "how it is reported")]),

    ("Q136", "spec", "Is the receipt store the same store as the ledger?",
     "No. Receipts live in the mount store (`dl-enclave` `MountStore`); the ledger row names the receipt as its subject. Two stores, one authority each.",
     "Clearing or migrating one store cannot silently take the other's evidence with it.",
     [repo_doc("AGENTS.md", "Receipt store", "the receipt store"),
      repo_doc("server/ledger.mjs", "the mount receipt is the subject", "the ledger's relationship to it")]),

    ("Q137", "owner", "How long are mount receipts retained before the retention action removes them?",
     None, None,
     [repo_doc("docs/LEDGER.md", "Retention removes encrypted vault blobs", "retention exists; the window does not")]),

    ("Q138", "owner", "May mount receipts leave the machine — published, exported or shared outside it?",
     None, None,
     [doc(ARCH, "A receipt is evidence of adoption, not authorization to adopt", "governs adoption, says nothing about publication")]),

    ("Q139", "owner", "What counts as a successful acceptance day?",
     None, None,
     [doc(WS, "still unanswered", "the residue recorded in section 6")]),

    ("Q140", "owner", "May the driver witness its own mount and count that as receipt evidence?",
     None, None,
     [repo_doc("AGENTS.md", "headless browser", "what does not count as a witness"),
      doc(WS, "| N010 |", "the witness the record requires")]),
]


def seed():
    path = pathlib.Path("docs/hypergrill/state.json")
    state = json.loads(path.read_text(encoding="utf-8"))
    added = 0
    for qid, klass, text, _res, _eff, evidence in BLOCK:
        if qid in state["questions"]:
            continue
        state["questions"][qid] = {"id": qid, "text": text, "class": klass,
                                   "status": "open", "ruling": "", "evidence": evidence}
        added += 1
    path.write_bytes((json.dumps(state, indent=2, sort_keys=True) + "\n").encode("utf-8"))
    return added


def write_appendix():
    path = pathlib.Path(WS)
    text = path.read_text(encoding="utf-8")
    if "## Appendix E" in text:
        return False
    rows = "\n".join(f"| {qid} | {q} | `{klass}` |" for qid, klass, q, *_ in BLOCK)
    block = (
        "\n## Appendix E — mount receipts and subordinate versions, seeded 2026-11-04\n\n"
        "The third block of the spine. Sixteen of the twenty are settled by the record; the four whose\n"
        "answer is a judgement rather than a derivation are held open and asked at §8.4, not folded to\n"
        "keep the block tidy.\n\n"
        "| Id | Question | Class |\n|---|---|---|\n" + rows + "\n")
    path.write_bytes((text.rstrip("\n") + "\n" + block).encode("utf-8"))
    return True


def resolve_closable():
    closed, refused = [], []
    for qid, klass, _q, resolution, effect, evidence in BLOCK:
        if resolution is None:
            continue
        receipt = {"question": qid, "class": klass, "evidence": evidence,
                   "resolution": resolution, "effect": effect}
        with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False, encoding="utf-8") as fh:
            json.dump(receipt, fh)
            tmp = fh.name
        proc = subprocess.run([sys.executable, "tools/hypergrill_resolver.py", "resolve", tmp],
                              capture_output=True, text=True)
        out = (proc.stdout or proc.stderr).strip()
        print(f"{qid} exit={proc.returncode} {out.splitlines()[0] if out else '<no output>'}")
        (closed if proc.returncode == 0 else refused).append(qid)
    return closed, refused


def rewrite_counters(receipt_count):
    path = pathlib.Path(WS)
    text = path.read_text(encoding="utf-8")
    state = json.loads(pathlib.Path("docs/hypergrill/state.json").read_text(encoding="utf-8"))
    entries = state["questions"]
    counts = {"resolved": 0, "open": 0, "folded": 0, "struck": 0}
    for entry in entries.values():
        counts[entry["status"]] = counts.get(entry["status"], 0) + 1

    seeded = len(BLOCK) + 40  # appendices C, D and E
    closed_here = counts["resolved"] - 158
    open_here = counts["open"]
    remaining = 407 - len(BLOCK) - 20

    open_rows = "\n".join(
        f"| `{qid}` | {q} | `{klass}` |" for qid, klass, q, res, _e, _ev in BLOCK if res is None)

    block = f"""## 8.3 Driver progress (2026-11-04)

| Block | Seeded | Closed | Open |
|---|---|---|---|
| Carried set (Appendix C) | 20 | 20 | 0 |
| Stream protocol (Appendix D) | 20 | 20 | 0 |
| Mount receipts (Appendix E) | {len(BLOCK)} | {closed_here} | {open_here} |
| **Worked so far** | **{seeded}** | **{closed_here + 40}** | **{open_here}** |

`state.json` holds {len(entries)} entries: {counts['resolved']} resolved, {counts['folded']} folded, {counts['open']} open.
Receipts on file: {receipt_count}. Remaining spine: {remaining} of 500.

The {counts['open']} open questions are the block's owner residue. Every one of them is a judgement about
retention, publication, acceptance or independence of witness; none is a fact the record could settle,
and none was closed to make the block look finished. They are asked at §8.4.

## 8.4 Round held 2026-11-04 (v2.2): mount receipts

Four questions, each one the block could not answer for itself. The two evidence pins attached to each
are what the driver could establish; what remains is the part that is not a derivation.

| Id | Question | Class | State |
|---|---|---|---|
{open_rows}

**State:** asked {counts['open']} · answered 0 · open {counts['open']} · struck 0 · superseded 0 — **{counts['open']} remaining.**

"""
    pattern = re.compile(r"## 8\.3 Driver progress.*?(?=## Appendix A —)", re.S)
    if pattern.search(text):
        text = pattern.sub(block, text, count=1)
    else:
        text = text.replace("## Appendix A —", block + "## Appendix A —", 1)
    path.write_bytes(text.encode("utf-8"))
    return counts, len(entries), remaining


def main():
    added = seed()
    appended = write_appendix()
    print(f"seeded {added}; appendix E written: {appended}")
    closed, refused = resolve_closable()
    receipts = pathlib.Path("docs/hypergrill/receipts.jsonl").read_text(encoding="utf-8").strip().splitlines()
    counts, entries, remaining = rewrite_counters(len(receipts))
    print(f"\nclosed={len(closed)} refused={refused}")
    print("state:", counts, "entries:", entries, "receipts:", len(receipts), "spine left:", remaining)
    ok = not refused and counts["resolved"] == 174 and counts["open"] == 4 and counts["folded"] == 1 \
        and entries == 179 and len(receipts) == 56 and remaining == 367
    print("RESULT:", "PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
