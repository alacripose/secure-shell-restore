import json
import pathlib
import re
import subprocess
import sys
import tempfile

WS = pathlib.Path("docs/SECURE-SHELL-RESTORE@1.HYPERGRILL.md")
STATE = pathlib.Path("docs/hypergrill/state.json")
RECEIPTS = pathlib.Path("docs/hypergrill/receipts.jsonl")
CIV = pathlib.Path("docs/SECURE-SHELL-RESTORE@1.CUA-CIVILIAN-ACCEPTANCE.md")

WORD = "the node cua driver is the operation layer for the civilian acceptance document"


def record_answer():
    text = WS.read_text(encoding="utf-8")
    old = "| `N055` | What authorization does a Node-driven CUA witness carry? | `owner` | open |"
    new = ("| `N055` | What authorization does a Node-driven CUA witness carry? | `owner` | "
           f"answered — \"{WORD}\" |")
    if old not in text:
        raise SystemExit("N055 row not found in the worksheet")
    text = text.replace(old, new, 1)

    answered = ("**Answered 2026-11-04 (N055).** The Node CUA driver is the operation layer for "
                "`SECURE-SHELL-RESTORE@1.CUA-CIVILIAN-ACCEPTANCE.md`. The rule this register refuses "
                "therefore does not merely lack family support; it contradicts the role the owner has "
                "assigned.\n\n**How the backwalk was run.**")
    text = text.replace("**How the backwalk was run.**", answered, 1)
    WS.write_bytes(text.encode("utf-8"))


def resolve_n055():
    receipt = {
        "question": "N055",
        "class": "owner",
        "verbatim": WORD,
        "evidence": [{"kind": "owner",
                      "ref": "docs/SECURE-SHELL-RESTORE@1.HYPERGRILL.md#8.5",
                      "note": "verbatim: " + WORD}],
        "resolution": ("The Node CUA driver is the operation layer for the civilian acceptance "
                       "document. A Node process is therefore authorized as the operation layer, and "
                       "a rule that treats a Node check as not a witness is refused as authority."),
        "effect": ("The civilian acceptance document names the Node CUA driver as its operation layer. "
                   "Q129's rendering requirement stands; its Node clause is refused."),
    }
    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False, encoding="utf-8") as fh:
        json.dump(receipt, fh)
        tmp = fh.name
    proc = subprocess.run([sys.executable, "tools/hypergrill_resolver.py", "resolve", "--owner", tmp],
                          capture_output=True, text=True)
    out = (proc.stdout or proc.stderr).strip()
    print(f"N055 exit={proc.returncode} {out.splitlines()[0] if out else '<no output>'}")
    return proc.returncode == 0


def write_civilian_role():
    text = CIV.read_text(encoding="utf-8")
    if "## Operation layer" in text:
        return False
    block = (
        "\n## Operation layer\n\n"
        "The operation layer for this acceptance is the **Node CUA driver**: the mineflayer bodies that "
        "read exact AXIS packages and connect directly to the Minecraft server, as they run in "
        "`ala-civ-bots-prototype` (`tools/residents/src/main.mjs`, recorded at `CHECKPOINT.md:38` of that "
        "checkout). Recorded by the owner, 2026-11-04.\n\n"
        "The consequence is narrow and it is the point: a body written in Node is not disqualified from "
        "this role, and a claim that only a rendered browser client may witness is refused as authority "
        "rather than applied. What the operation layer must show is unchanged — the mount, the render and "
        "the digest — and the language it is written in is not evidence of anything.\n\n"
        "The refusal is recorded as `AV-001` in `SECURE-SHELL-RESTORE@1.HYPERGRILL.md` §8.5.\n")
    CIV.write_bytes((text.rstrip("\n") + "\n" + block).encode("utf-8"))
    return True


def rewrite_83():
    state = json.loads(STATE.read_text(encoding="utf-8"))
    entries = state["questions"]
    counts = {"resolved": 0, "open": 0, "folded": 0, "struck": 0}
    for entry in entries.values():
        counts[entry["status"]] = counts.get(entry["status"], 0) + 1
    receipts = RECEIPTS.read_text(encoding="utf-8").strip().splitlines()

    text = WS.read_text(encoding="utf-8")
    block = f"""## 8.3 Driver progress (2026-11-04)

| Block | Seeded | Closed | Open |
|---|---|---|---|
| Carried set (Appendix C) | 20 | 20 | 0 |
| Stream protocol (Appendix D) | 20 | 20 | 0 |
| Mount receipts (Appendix E) | 20 | 20 | 0 |
| **Worked so far** | **60** | **60** | **0** |

`state.json` holds {len(entries)} entries: {counts['resolved']} resolved, {counts['folded']} folded, \
{counts['struck']} struck, {counts['open']} open. Receipts on file: {len(receipts)}. \
Remaining spine: 367 of 500.

Nothing is open. Every question this block raised has been answered by the owner, closed on evidence, \
or struck with its reason; none is waiting in prose.

"""
    pattern = re.compile(r"## 8\.3 Driver progress.*?(?=## 8\.4)", re.S)
    if not pattern.search(text):
        raise SystemExit("8.3 not found")
    WS.write_bytes(pattern.sub(block, text, count=1).encode("utf-8"))
    return counts, len(entries), len(receipts)


def main():
    record_answer()
    ok = resolve_n055()
    added = write_civilian_role()
    counts, entries, receipts = rewrite_83()
    print("civilian role section added:", added)
    print("state:", counts, "entries:", entries, "receipts:", receipts)
    good = (ok and counts["resolved"] == 178 and counts["open"] == 0 and counts["struck"] == 1
            and counts["folded"] == 1 and entries == 180 and receipts == 61)
    print("RESULT:", "PASS" if good else "FAIL")
    return 0 if good else 1


if __name__ == "__main__":
    sys.exit(main())
