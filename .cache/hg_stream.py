import json
import pathlib
import re
import subprocess
import sys
import tempfile

ARCH = "docs/SECURE-SHELL-RESTORE@1.ARCHITECTURE.md"
IMPL = "docs/SECURE-SHELL-RESTORE@1.IMPLEMENTATION-PLAN.md"
WS = "docs/SECURE-SHELL-RESTORE@1.HYPERGRILL.md"
REPO = pathlib.Path("C:/Users/ala/Documents/secure-shell")


def line_of(path, needle):
    """Pin a phrase even when the document wraps it or wraps it in emphasis.

    `*` and backticks become spaces so bold and code spans cannot break a pin;
    the substitution is length-preserving, so the line number stays true.
    """
    raw = pathlib.Path(path).read_text(encoding="utf-8", errors="replace")
    text = raw.replace("*", " ").replace("`", " ")
    tokens = needle.replace("*", " ").replace("`", " ").split()
    pattern = re.compile(r"\s+".join(re.escape(part) for part in tokens))
    match = pattern.search(text)
    if not match:
        raise SystemExit(f"anchor not found in {path}: {needle!r}")
    return text[: match.start()].count("\n") + 1


def doc(path, needle, note):
    return {"kind": "doc", "ref": f"{path}:{line_of(path, needle)}", "note": note}


def code(rel, needle, note):
    return {"kind": "code",
            "ref": f"secure-shell:{rel}:{line_of(REPO / rel, needle)}",
            "note": note}


BLOCK = [
    ("Q101", "spec", "What is the stream's version tag and where does it live?",
     "The stream tag is `secure-shell.stream/1`, carried in the frame header and versioned independently of package identity.",
     "Section 7 keeps its own tag; a package revision never renumbers the stream.",
     [doc(ARCH, "The stream is `secure-shell.stream/1`", "the tag and its home"),
      doc(ARCH, "independently versioned subordinate contract", "its relationship to receipts")]),

    ("Q102", "spec", "Does a stream schema bump bump the mount receipt schema?",
     "No. A stream schema bump does not bump the mount receipt schema, and a receipt bump does not disturb the stream.",
     "The two contracts carry separate version axes and are tested independently.",
     [doc(ARCH, "A stream schema bump does not bump the mount receipt schema, and vice versa", "the explicit non-coupling rule")]),

    ("Q103", "spec", "Are chunks ordered by sequence, and what happens to a gap?",
     "Chunks carry an explicit sequence and are applied in order. A gap, a duplicate or a reordering is a truncation-class refusal, never a silent resort.",
     "The reader never reorders; out-of-sequence input is refused by name.",
     [doc(ARCH, "Ordered bounded chunks", "order is a stated property"),
      doc(ARCH, "stream-truncated", "the refusal class available for a gap")]),

    ("Q104", "spec", "Is resume authenticated?",
     "Resume is authenticated. The resuming side re-presents the package identity, and a resume without a verifiable signature is refused rather than trusted.",
     "An unauthenticated resume cannot place bytes into an assembling package.",
     [doc(ARCH, "authenticated resume", "resume is stated as authenticated"),
      doc(ARCH, "never mounted as verified", "unverified bytes are never adopted")]),

    ("Q105", "spec", "Are operation ids idempotent, and what does a retry do?",
     "Operation ids make delivery idempotent: a retried chunk or apply carrying the same operation id takes effect once, and the second arrival is acknowledged without a second effect.",
     "Retries are free; the ledger does not grow a second row for the same operation.",
     [doc(ARCH, "idempotent operation ids", "the property is stated"),
      code("AGENTS.md", "idempotent by operation id", "the family's existing rule")]),

    ("Q106", "spec", "How is truncation detected?",
     "Truncation is detected against the declared size and the digest, not against the transport closing. The refusal is `stream-truncated`.",
     "A short stream is refused by name; the previous revision stays mounted.",
     [doc(ARCH, "truncation detection", "detection is a stated property"),
      doc(ARCH, "no adoption, previous revision stays", "the consequence")]),

    ("Q107", "spec", "Is finalization explicit or implied by EOF?",
     "Finalization is explicit: the stream ends with a finalization record. An EOF without one is a truncation, not a short but acceptable stream.",
     "EOF alone never adopts anything.",
     [doc(ARCH, "explicit finalization", "explicit, not implied"),
      doc(ARCH, "Stream truncated", "the failure it prevents")]),

    ("Q108", "spec", "Is adoption atomic?",
     "Adoption is atomic: the mounted surface switches in one step, so a partially applied revision is never visible.",
     "No intermediate state is observable to the user.",
     [doc(ARCH, "atomic adoption", "the property is stated"),
      doc(ARCH, "The client keeps the previous admitted revision", "what holds until the switch")]),

    ("Q109", "spec", "When may the client drop the previous admitted revision?",
     "Only after digest, signature, schema, compatibility and client-surface checks all pass, in that order.",
     "The previous revision is the rollback target until every check clears.",
     [doc(ARCH, "until digest, signature, schema, compatibility, and client-surface checks pass", "the full gate list")]),

    ("Q110", "spec", "Are older or newer frames converted on read?",
     "No conversion on read. The frame is refused by name with `found` and `supported`, which the family's own reader already does and its own test asserts.",
     "There is no downgrade path and no best-effort parse.",
     [doc(ARCH, "Older or newer frames are refused by name", "refusal, not conversion"),
      code("tests/stream.test.mjs", "an older served record is refused by name, never converted",
           "the behaviour already asserted in the family")]),

    ("Q111", "spec", "Does the stream carry its own package identity?",
     "Yes. The streamer is itself a package with its own identity, separate from the packages it carries, so a streamer revision never renumbers its payload packages.",
     "Streamer identity and payload identity are two rows, not one.",
     [doc(WS, "| Q024 |", "the streamer's own identity"),
      doc(ARCH, "The stream is `secure-shell.stream/1`", "the stream tag is separate from package identity")]),

    ("Q112", "spec", "Does the manifest travel inline or separately?",
     "The manifest travels inline in the canonical package bytes. The chunk manifest is the stream's own framing and is not a second copy of the package manifest.",
     "One package manifest, one framing manifest, no third.",
     [doc(ARCH, "carries canonical package bytes, chunk manifests", "what the stream carries")]),

    ("Q113", "spec", "What bounds a chunk?",
     "A chunk is bounded and the bound is declared per frame. The family's arrival frame already caps a payload at 1 MiB, and Restore adopts that ceiling rather than inventing a second number.",
     "One ceiling for arrival and delivery; no per-path dialect.",
     [code("server/ingest.mjs", "MAX_PAYLOAD = 1_048_576", "the existing ceiling"),
      doc(ARCH, "Ordered bounded chunks", "boundedness is a stated property")]),

    ("Q114", "spec", "Does the receipt ride the stream?",
     "Yes, and it rides as a subordinate contract with its own version, so a stream change does not renumber receipts.",
     "The receipt is a separate record kind on the same connection.",
     [doc(ARCH, "mount receipts as an independently versioned subordinate contract", "the subordination rule")]),

    ("Q115", "spec", "Who produces the receipt?",
     "The client. It is a witness that the surface mounted and rendered, not the server's assertion that bytes were sent.",
     "The server's admission and the client's witness are different records.",
     [doc(ARCH, "A receipt is evidence of adoption, not authorization to adopt", "what a receipt means"),
      doc(WS, "| N010 |", "mount-and-render witness is the required proof")]),

    ("Q116", "spec", "What if the receipt names a different revision than the mount?",
     "The mount is indeterminate, not successful: refusal `receipt-mismatch`, and the previous revision stays.",
     "A mismatched receipt is never rounded to success.",
     [doc(ARCH, "receipt-mismatch", "the refusal"),
      doc(ARCH, "the mount is indeterminate, not successful", "the classification")]),

    ("Q117", "spec", "Does transport encryption affect package identity?",
     "No. Encryption is transport; the digest is over canonical content, and re-framing or re-encrypting the same content must not move it.",
     "Re-encryption is a test of the boundary, not a new identity.",
     [doc(IMPL, "BLAKE3 applied over framed or encrypted bytes", "the recorded failure this prevents"),
      doc(ARCH, "not transport framing", "identity excludes framing")]),

    ("Q118", "spec", "Does a resumed stream re-verify the prefix?",
     "Yes. The digest covers the whole content, so a resumed assembly re-verifies the prefix before finalization and adopts nothing on trust.",
     "Resume is a convenience for the network, not a shortcut past verification.",
     [doc(ARCH, "atomic adoption", "nothing partial becomes visible"),
      doc(ARCH, "truncation detection", "a bad prefix is a truncation-class failure")]),

    ("Q119", "code", "What refusal names an unsupported frame?",
     "`frame-schema`, carrying `found` and `supported`. The family's ingest reader already refuses that way.",
     "Same refusal code on arrival and on delivery; no second vocabulary.",
     [code("server/ingest.mjs", "frame-schema", "the existing refusal"),
      doc(ARCH, "Frame schema older/newer", "the same refusal in Restore's failure model")]),

    ("Q120", "spec", "Is there capability negotiation?",
     "No. The frame names its schema and the reader refuses what it does not support; there is no negotiation and no downgrade.",
     "Version refusal is the only mechanism, which keeps one reader per contract.",
     [doc(ARCH, "no conversion", "the recorded rule"),
      doc(ARCH, "Older or newer frames are refused by name", "the mechanism that replaces negotiation")]),
]


def seed(state_path):
    state = json.loads(pathlib.Path(state_path).read_text(encoding="utf-8"))
    added = 0
    for qid, klass, text, *_ in BLOCK:
        if qid not in state["questions"]:
            state["questions"][qid] = {"id": qid, "text": text, "class": klass,
                                       "status": "open", "ruling": "", "evidence": []}
            added += 1
    pathlib.Path(state_path).write_text(json.dumps(state, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return added


def append_appendix():
    path = pathlib.Path(WS)
    text = path.read_text(encoding="utf-8")
    if "## Appendix D" in text:
        return False
    rows = "\n".join(f"| {qid} | {text_} | `{klass}` |" for qid, klass, text_, *_ in BLOCK)
    block = (
        "\n## Appendix D — stream protocol block, seeded 2026-11-04\n\n"
        "The second block of the spine, seeded after the carried set closed. Same rule as Appendix C: this\n"
        "table is the seed, `state.json` is the count, and every closure appends a receipt.\n\n"
        "| Id | Question | Class |\n|---|---|---|\n" + rows + "\n")
    path.write_text(text.rstrip("\n") + "\n" + block, encoding="utf-8")
    return True


def main():
    added = seed("docs/hypergrill/state.json")
    appended = append_appendix()
    print(f"seeded {added} new questions; appendix written: {appended}")

    closed, refused = [], []
    for qid, klass, _text, resolution, effect, evidence in BLOCK:
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

    state = json.loads(pathlib.Path("docs/hypergrill/state.json").read_text(encoding="utf-8"))
    counts = {"resolved": 0, "open": 0, "folded": 0}
    for entry in state["questions"].values():
        counts[entry["status"]] = counts.get(entry["status"], 0) + 1
    receipts = pathlib.Path("docs/hypergrill/receipts.jsonl").read_text(encoding="utf-8").strip().splitlines()
    print(f"\nclosed={len(closed)} refused={refused}")
    print("state:", counts, "receipts:", len(receipts))

    ok = (not refused) and counts["open"] == 0 and counts["resolved"] == 158 and len(receipts) == 40
    print("RESULT:", "PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
