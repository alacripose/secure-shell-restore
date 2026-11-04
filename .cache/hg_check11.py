"""Check the forked drive scan: shape, truncation honesty, digests, and the twelve corrections."""

from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]
PARENT = ROOT.parent
DOC = ROOT / "docs" / "secure-shell-audit" / "cua_driver_reaudit_synthesis.md"
AUDIT = ROOT / "docs" / "hypergrill" / "audit@2026-11-04.json"
STATE = ROOT / "docs" / "hypergrill" / "scan_state@2026-11-04.json"
OLD = [ROOT / "docs" / "hypergrill" / "TASK@2026-11-04-cua-driver.md",
       ROOT / "docs" / "hypergrill" / "REFERENCES@2026-11-04.md"]

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
    if not DOC.is_file() or not STATE.is_file():
        print("refused: the scan output or its state is missing")
        return 2
    body = DOC.read_bytes()
    doc = body.decode("utf-8")
    state = json.loads(STATE.read_text(encoding="utf-8"))

    check("the inventory is LF-only", b"\r" not in body and body.endswith(b"\n"))
    check("it keeps the forked scanner's title",
          doc.startswith("# secure shell v2 — CUA driver re-audit inventory"))
    check("it states its budgets and the streaming rule",
          "Started " in doc and "truncated: yes` is a refusal, not a pass" in doc)
    for heading in ("## Totals", "## Refusals this scan itself demonstrates",
                    "## Classification of reference hits", "## The one task"):
        check("it has %s" % heading, heading in doc)
    sections = re.findall(r"^## `(.+)`$", doc, re.M)
    check("one section per root", len(sections) >= 15, str(len(sections)))
    check("every section reports truncation", doc.count("**truncated: ") >= len(sections),
          "%d vs %d" % (doc.count("**truncated: "), len(sections)))
    check("drives are walked, not just Documents", any(s.endswith(":\\") or s.endswith(":/") for s in sections),
          str(sections[-3:]))
    check("the refusals block names its own gaps",
          all(code in doc for code in ("audit-stream-truncated", "audit-gap-silent",
                                       "audit-unprovenanced", "audit-unstreamed",
                                       "reference-capped", "digest-documents-only",
                                       "scan-pruned")))

    rows = re.findall(r"^\| (D\d+) \|", doc, re.M)
    check("the one task carries twelve corrections", rows == ["D%d" % n for n in range(1, 13)], str(rows))
    check("every correction has a reference and an exit test",
          all(line.count("|") >= 5 for line in doc.split("\n") if re.match(r"^\| D\d+ \|", line)))
    check("the task names the witness rule",
          "with every action is" not in doc and "every action is" in doc)

    refs = re.findall(r"^\| `(R\d+)` \| `([^`]+)` \| (\d+) \| `([0-9a-f]{64}|not computed)` \|", doc, re.M)
    check("references are listed with sizes", len(refs) >= 500, str(len(refs)))
    check("the state agrees with the table", state["refs"] == len(refs),
          "%s vs %s" % (state.get("refs"), len(refs)))
    digested = [r for r in refs if r[3] != "not computed"]
    check("most project references carry a digest", len(digested) >= 50, str(len(digested)))
    bad = []
    for _, path, size, digest in digested:
        p = Path(path)
        if not p.is_file() or p.stat().st_size != int(size):
            bad.append(path)
            continue
        if hashlib.sha256(p.read_bytes()).hexdigest() != digest:
            bad.append(path)
    check("every digest verifies", not bad, str(bad[:5]))

    audit = json.loads(AUDIT.read_text(encoding="utf-8"))
    check("the audit still reports zero contradictions", audit["counts"]["contradicted"] == 0)
    unresolved = [ref for finding in audit["findings"] for ref in finding["refs"]
                  if not any((base / ref.rsplit(":", 1)[0]).is_file() for base in (PARENT, ROOT))]
    check("every audit citation resolves on disk", not unresolved, str(unresolved[:5]))
    check("the old two-writer artifacts are gone", not any(path.exists() for path in OLD))

    print("\n%d checks, %d failed" % (checks, len(failures)))
    if failures:
        print("failed: " + ", ".join(failures))
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
