"""Check the hypergrill re-audit: 500 slots covered, findings cited, re-rulings applied, record unmoved."""

from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs" / "hypergrill" / "AUDIT@2026-11-04.md"
JSON = ROOT / "docs" / "hypergrill" / "audit@2026-11-04.json"
WS = ROOT / "docs" / "SECURE-SHELL-RESTORE@1.HYPERGRILL.md"
STATE = ROOT / "docs" / "hypergrill" / "state.json"
RECEIPTS = ROOT / "docs" / "hypergrill" / "receipts.jsonl"

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


def main():
    if not DOC.is_file() or not JSON.is_file():
        print("refused: the audit report or its JSON is missing")
        return 2
    body = DOC.read_bytes()
    doc = body.decode("utf-8")
    audit = json.loads(JSON.read_text(encoding="utf-8"))
    ws = WS.read_text(encoding="utf-8")

    check("the audit report is LF-only", b"\r" not in body and body.endswith(b"\n"))
    check("all 500 spine slots are present", sorted(audit["slots"]) == ["Q%03d" % n for n in range(1, 501)])
    check("every slot has a known verdict",
          all(row["verdict"] in {"supported", "contradicted", "absent-on-disk", "tension",
                                 "superseded", "no-probe", "unasked"}
              for row in audit["slots"].values()))
    check("the unasked spine is 367", audit["unasked_spine"] == 367, str(audit["unasked_spine"]))
    check("the recorded spine is 133", audit["recorded_spine"] == 133, str(audit["recorded_spine"]))

    recorded = json.loads(STATE.read_text(encoding="utf-8"))["questions"]
    check("the record still holds 180 entries", len(recorded) == 180, str(len(recorded)))
    receipts = [line for line in RECEIPTS.read_text(encoding="utf-8").split("\n") if line.strip()]
    check("the record still holds 61 receipts", len(receipts) == 61, str(len(receipts)))

    check("no probe refused",
          all(row["verdict"] != "refused" for row in audit["slots"].values()))
    check("no ruling is contradicted after the round",
          audit["counts"]["contradicted"] == 0, str(audit["counts"]["contradicted"]))
    check("the format re-rulings are superseded",
          {q for q, row in audit["slots"].items() if row["verdict"] == "superseded"}
          >= {"Q063", "Q064", "Q068", "Q070", "Q071", "Q074"},
          str(sorted(q for q, row in audit["slots"].items() if row["verdict"] == "superseded")))
    check("the deprecation window stays a named gap",
          audit["slots"]["Q060"]["verdict"] == "absent-on-disk")

    findings = audit["findings"]
    check("findings are recorded", len(findings) >= 6, str(len(findings)))
    for row in findings:
        check("%s cites at least two refs" % row["id"], len(row["refs"]) >= 2, str(row["refs"]))
        for ref in row["refs"]:
            path, _, line = ref.rpartition(":")
            ok = path and line.isdigit()
            target = ROOT / path if path else None
            if target is not None and not target.is_file():
                target = ROOT.parent / path
            check("  %s ref %s resolves" % (row["id"], ref),
                  bool(ok) and target is not None and target.is_file())

    check("the report names the unasked 367", "367" in doc and "unasked" in doc)
    check("the report names the cadence gap", "TICK-CADENCE.md" in doc and "20 Hz" in doc)
    check("the report records the round", "2026-11-04" in doc and "superseded" in doc)
    check("the worksheet points at the audit", "## 8.6" in ws and "AUDIT@2026-11-04.md" in ws)
    check("the worksheet records the round", "## 8.7 Round held 2026-11-04 (v2.3)" in ws)
    check("the round quotes the owner", '"Full 64 hex for both"' in ws
          and '"The ruled manifest/Merkle shape"' in ws)
    check("the worksheet still carries 8.3", "state.json` holds 180 entries" in ws)

    print("\n%d checks, %d failed" % (checks, len(failures)))
    if failures:
        print("failed: " + ", ".join(failures))
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
