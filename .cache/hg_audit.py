import pathlib
import re
import sys

WS = pathlib.Path("docs/SECURE-SHELL-RESTORE@1.HYPERGRILL.md")
SPEC = pathlib.Path("secure-shell/AGENTS.md")
ALA = pathlib.Path("C:/Users/ala/Documents/ala_civ_bots_prototype")
RECEIPTS = pathlib.Path("docs/hypergrill/receipts.jsonl")


def line_of(path, needle):
    raw = pathlib.Path(path).read_text(encoding="utf-8", errors="replace")
    text = raw.replace("*", " ").replace("`", " ")
    tokens = needle.replace("*", " ").replace("`", " ").split()
    pattern = re.compile(r"\s+".join(re.escape(p) for p in tokens))
    match = pattern.search(text)
    if not match:
        raise SystemExit(f"anchor not found in {path}: {needle!r}")
    return text[: match.start()].count("\n") + 1


rule = line_of("C:/Users/ala/Documents/secure-shell/AGENTS.md", "not a witness for")
prop = line_of(RECEIPTS, '"question": "Q129"')
body = line_of(ALA / "CHECKPOINT.md", "the connected body is the Node mineflayer process")
client = line_of(ALA / "build/reports/gameplay-degrees.txt", "it is a client, not a gameplay phase")

BLOCK = f"""## 8.5 Authorization violation register

### AV-001 — a Node check is not a witness (refused)

| Field | Value |
|---|---|
| Owner's words | "False, we have node cua bots in ala-civ-bots-prototype, another authorization violation that will have to be refused and backwalked against the hypergrilling tree through an automated audit to see where such a thing came from, which was the performance test for the 1000 cua drivers" |
| The rule as written | `secure-shell:AGENTS.md:{rule}` — "a check that runs only in Node, a headless browser, or a separate witness page is not a witness" |
| Where it was propagated | `docs/hypergrill/receipts.jsonl:{prop}` — `Q129`, which used it as its second pin |
| What the family actually runs | `ala-civ-bots-prototype:CHECKPOINT.md:{body}` — "the connected body is the Node mineflayer process in `tools/residents/src/main.mjs`, not a Fabric client"; `ala-civ-bots-prototype:build/reports/gameplay-degrees.txt:{client}` — "the mineflayer body reads exact AXIS packages; it is a client" |
| The 1000-driver performance test | **`absent`.** Not located in that checkout by this audit. The missing artifact is a performance-test record naming 1000 drivers. The owner reports it; the file was not found, and it is recorded as owner-reported rather than as a citation |
| Disposition | The rule is **refused as authority**. `Q129`'s conclusion — a receipt requires a rendering, not a check the client cannot see — survives on its other pin (`test-surface-unwitnessed`), so no receipt is retracted. The authorization question beneath it is `N055` |

**How the backwalk was run.** Automated, not by reading around: the claim is grepped across this tree
and the family checkout, every hit is pinned with a path and a line, and the register records what the
search found and what it did not. A missing artifact is written as `absent` with its name, never
inferred from silence.

**What the audit establishes.** The rule is a local convention of `secure-shell`, not a family-wide
invariant: the tree that states it is contradicted by a sibling checkout whose residents are Node
processes. A convention stated in one repository was cited as though it were family law, and that is
the authorization violation — not the existence of Node bodies.

"""


def main():
    text = WS.read_text(encoding="utf-8")
    if "## 8.5 Authorization violation register" in text:
        print("8.5 already present")
        return 0
    anchor = "## Appendix A —"
    if anchor not in text:
        raise SystemExit("appendix A anchor missing")
    text = text.replace(anchor, BLOCK + anchor, 1)
    WS.write_bytes(text.encode("utf-8"))
    print(f"8.5 written; pins: rule={rule} propagated={prop} body={body} client={client}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
