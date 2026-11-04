"""Check the ingested-sources register: that it exists, that its quotes stay attributed, and that every
`absent` it claims is still absent on disk.

An absence that quietly becomes a presence is a false claim, so each named document is looked for in the
secure-shell tree. If one appears, this check fails and the register must be updated rather than left
saying a document is missing when it is not.
"""

from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parent / "secure-shell"
DOC = ROOT / "docs" / "SECURE-SHELL-RESTORE@1.CUA-CIVILIAN-ACCEPTANCE.md"
ARCH = ROOT / "docs" / "SECURE-SHELL-RESTORE@1.ARCHITECTURE.md"

ABSENT_BASENAMES = [
    "CHECKPOINT.md",
    "cua_worker.py",
    "AXIS-MODULE.md",
    "proof.rs",
    "civilians.rs",
    "DRIFT.md",
    "CLIENT-UI.md",
]

failures = []
checks = 0


def check(name, ok, detail=""):
    global checks
    checks += 1
    if ok:
        print("ok   %s" % name)
    else:
        print("FAIL %s%s" % (name, (": " + detail) if detail else ""))
        failures.append(name)


def flat(value):
    return " ".join(value.split())


def main():
    if not DOC.is_file():
        print("refused: the CUA acceptance document is missing")
        return 2

    doc = DOC.read_bytes().decode("utf-8")
    arch = ARCH.read_bytes().decode("utf-8")
    text = flat(doc)

    check("the register exists", "## 11. Sources ingested" in doc)
    check("it has all three parts",
          "### 11.1" in doc and "### 11.2" in doc and "### 11.3" in doc)
    check("Pins keeps its number", "## 10. Pins" in doc and "## 11. Pins" not in doc)

    check("the world-model transcript is pinned by size", "14,287 bytes" in text)
    check("the Dory transcript is pinned by size", "15,061 bytes" in text)
    check("the imported session is pinned by size", "12,245,017 bytes" in text)
    check("the imported session is pinned by turn count", "296 turns" in text)
    check("it is named as a session record", "session record" in text)
    check("the receipt defect is named against the code", "text(input.digest)" in doc)
    check("the located documents are not claimed absent on disk", "absent on disk" not in text)
    check("they carry measured sizes", "CHECKPOINT.md` — 54,028 bytes" in text)
    check("the register states that quotes are verbatim", "Quotes are verbatim" in text)
    check("a transcript is a source, not an instruction",
          "A transcript is a source, not an instruction" in text)
    check("the architecture still records its own audit source",
          "The Rapid Progress of Realtime Simulations" in flat(arch))

    for rule in ["E1", "E2", "E3", "E4"]:
        check("%s is proposed with an exit test" % rule,
              "| %s |" % rule in doc and "Exit test" in doc)

    check("the source's own uncertainty is carried", "depending on the actual problem" in text)
    check("the register refuses the reasoning analogy",
          "turning up reasoning" in text)
    check("the register refuses to call the driver a looped transformer",
          "never a CUA agent" in text)
    check("no lap count is adopted as a target", "no lap count" in text)

    # Every absence claimed must still be true, or the claim is false.
    for name in ABSENT_BASENAMES:
        check("the register names %s" % name, name in doc)
        found = [str(path) for path in REPO.rglob(name)] if REPO.is_dir() else []
        check("%s is still absent from the tree" % name, found == [], ", ".join(found[:3]))

    packages = ROOT.parent / "secure-shell" / "packages"
    catalogue = []
    if packages.is_dir():
        catalogue = [p.name for p in packages.iterdir()
                     if p.is_dir() and p.name in {"axis-cua", "cua", "driver", "axis-driver"}]
    check("no action catalogue package exists yet", catalogue == [], str(catalogue))
    check("the register says so", "a driver action catalogue" in text and "holds `axis/` and `toast/`" in text)

    # The family's count rule (Q019): five plan documents, with the grilling record beside them.
    PLAN_KINDS = {"ARCHITECTURE", "IMPLEMENTATION-PLAN", "FORMAT-IMPORT-AUDIT",
                  "CUA-CIVILIAN-ACCEPTANCE", "AGENT-BOOTSTRAP-API"}
    present = sorted(p.name for p in (ROOT / "docs").glob("SECURE-SHELL-RESTORE@1.*.md"))
    plans = [name for name in present if name.split(".")[-2] in PLAN_KINDS]
    check("the five plan documents stay five", len(plans) == 5, str(plans))
    check("the grilling record is the file beside them, not a sixth plan",
          any("HYPERGRILL" in name for name in present) and
          len([n for n in present if n.split(".")[-2] not in PLAN_KINDS]) == 1,
          str(present))

    state = json.loads((ROOT / "docs" / "hypergrill" / "state.json").read_text(encoding="utf-8"))
    questions = state.get("questions", {})
    check("the hypergrill record is untouched by this ingestion", len(questions) == 180,
          "%d entries" % len(questions))
    receipts = [line for line in (ROOT / "docs" / "hypergrill" / "receipts.jsonl")
                .read_text(encoding="utf-8").split("\n") if line.strip()]
    check("its receipts are untouched", len(receipts) == 61, "%d receipts" % len(receipts))

    for path in [DOC, ARCH]:
        body = path.read_bytes()
        check("LF only %s" % path.name, b"\r" not in body and body.endswith(b"\n"))

    print("\n%d checks, %d failed" % (checks, len(failures)))
    if failures:
        print("failed: " + ", ".join(failures))
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
