"""CI gate for the re-audit: assert what the artifact can prove where no family checkout exists.

`hg_check10.py` pins refs into sibling checkouts (`testport1`, `secure-shell`, `shploingus-clean`).
A runner has none of them, so it cannot run there; it stays a local check and says so. What CI can
prove is the owner's rule from A-08: a contradiction fails the run, and a refused probe is not a
pass either.

Exit 0 only when the artifact reports zero contradictions and the full spine is present.
"""

from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
JSON = ROOT / "docs" / "hypergrill" / "audit@2026-11-04.json"


def main() -> int:
    if not JSON.is_file():
        print("refused: the audit artifact is missing at %s" % JSON)
        return 2
    audit = json.loads(JSON.read_text(encoding="utf-8"))
    slots = audit.get("slots", {})
    counts = audit.get("counts", {})
    problems = []
    if sorted(slots) != ["Q%03d" % n for n in range(1, 501)]:
        problems.append("the spine is not 500 slots")
    if counts.get("contradicted", 1) != 0:
        problems.append("contradicted %d" % counts.get("contradicted", -1))
    refused = sorted(q for q, row in slots.items() if row.get("verdict") == "refused")
    if refused:
        problems.append("refused probes: " + ", ".join(refused))
    print("slots %d | contradicted %d | no-probe %d | refused %d"
          % (len(slots), counts.get("contradicted", -1), counts.get("no-probe", -1), len(refused)))
    print("family checkouts: absent here, so ref-pinning checks are local-only")
    for line in problems:
        print("FAIL " + line)
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
