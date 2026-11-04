"""Insert the §8.6 pointer to the re-audit ahead of Appendix A, using the audit's own counts."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WS = ROOT / "docs" / "SECURE-SHELL-RESTORE@1.HYPERGRILL.md"
AUDIT = ROOT / "docs" / "hypergrill" / "audit@2026-11-04.json"

raw = WS.read_bytes().decode("utf-8")
if "## 8.6 Re-audit of the 500" in raw:
    print("8.6 already present")
    raise SystemExit(0)

audit = json.loads(AUDIT.read_text(encoding="utf-8"))
c = audit["counts"]
findings = ", ".join("`%s`" % row["id"] for row in audit["findings"]
                     if row["verdict"] == "contradicted")

SECTION = f"""## 8.6 Re-audit of the 500 against the projects on disk (2026-11-04)

The whole spine was re-audited once the family checkouts were available, not just the worked blocks.
`Q001`–`Q140` are the asked range (`Q094`–`Q100` were never written) and `Q141`–`Q500` exist only as
Appendix B blocks, so the audit reports
{audit["unasked_spine"]} slots `unasked` rather than inventing their wording. Of the {audit["recorded_spine"]} recorded
spine questions, {c["supported"]} are supported by a file read, {c["contradicted"]} are contradicted, {c["tension"]} is a tension,
{c["absent-on-disk"]} name a mechanism no file implements, and {c["no-probe"]} have no probe on disk.

The contradictions are format-shape rulings: {findings} each describe a JSON manifest, a payload walk,
a Merkle tree over files or per-file hashes, while `testport1` ships `V4PKG001` — one binary frame and
one SHA-256 payload digest over `domain || schema || len || payload`. Both cannot be the package
format; choosing one is a ticket, not an audit.

No `code`, `spec` or `owner` question was closed, reopened, folded or struck by this audit, and
`state.json` and `receipts.jsonl` are unchanged. The report is `docs/hypergrill/AUDIT@2026-11-04.md`,
its JSON is `docs/hypergrill/audit@2026-11-04.json`, and `tools/hypergrill_reaudit.py` re-runs it.

The record also never asks about a tick cadence: `testport1/docs/TICK-CADENCE.md:11` records the plan's
refusal to hardcode a 20 Hz tick, and no slot in the 500 carries the question that would place it.

"""

anchor = "## Appendix A — owner rulings recorded under the retired format"
assert anchor in raw
raw = raw.replace(anchor, SECTION + anchor, 1)
WS.write_bytes(raw.encode("utf-8"))
print("8.6 inserted | bytes:", len(raw.encode("utf-8")), "| CR:", "\r" in raw)
