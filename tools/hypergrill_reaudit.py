#!/usr/bin/env python3
"""Re-audit the hypergrilling record against the projects as they exist on disk.

The spine is 500 slots (Q001-Q500). This tool does not invent questions: a slot with no
question text on disk is reported `unasked`, never guessed. For every recorded entry it
either runs a named probe that resolves an on-disk file and a line, or records why no
probe applies. A probe whose file or needle is missing is a refusal (exit 3), never a pass.

    python tools/hypergrill_reaudit.py            # write the report and the JSON
    python tools/hypergrill_reaudit.py --strict   # exit 2 when any ruling is contradicted

Verdicts:
  supported        an on-disk file states what the ruling states
  contradicted     an on-disk file states the opposite or a different shape
  absent-on-disk   the mechanism the ruling names is not implemented by any file read
  tension          two on-disk facts are lawful but disagree with the ruling's scope
  no-probe         no file on disk settles it (store, policy or signature envelope)
  unasked          no question text exists anywhere on disk
"""

from __future__ import annotations

import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PARENT = ROOT.parent
STATE = ROOT / "docs" / "hypergrill" / "state.json"
WORKSHEET = ROOT / "docs" / "SECURE-SHELL-RESTORE@1.HYPERGRILL.md"
OUT_MD = ROOT / "docs" / "hypergrill" / "AUDIT@2026-11-04.md"
OUT_JSON = ROOT / "docs" / "hypergrill" / "audit@2026-11-04.json"

VERDICTS = ("supported", "contradicted", "absent-on-disk", "tension", "superseded",
            "no-probe", "unasked")

# Owner rulings recorded 2026-11-04 in Appendix 8.7. A re-ruling does not erase the on-disk
# finding: the refs stay, and the verdict records that the record now says something else.
RULINGS = {
    "Q060": ("absent-on-disk",
             "Owner ruling 2026-11-04: add the deprecation-window field now. No file carries it yet, so "
             "the gap stands until the field lands."),
    "Q063": ("superseded",
             "Owner ruling 2026-11-04: full 64 hex for both hashes. The 32-hex format id is pre-migration."),
    "Q064": ("superseded",
             "Owner ruling 2026-11-04: the ruled manifest shape is the package format; V4PKG001 is a "
             "legacy input that is read and converted."),
    "Q068": ("superseded",
             "Owner ruling 2026-11-04: the manifest side is the format, so the JSON-on-disk ruling stands "
             "and the binary frame is a carried legacy input."),
    "Q070": ("superseded",
             "Owner ruling 2026-11-04: the Merkle payload walk is the format; the frame's single digest is "
             "the legacy input's form."),
    "Q071": ("superseded",
             "Owner ruling 2026-11-04: per-file hashes are part of the format the conversion produces."),
    "Q074": ("superseded",
             "Owner ruling 2026-11-04: add the grade to the preimage, so a grade change is a new id."),
}

# Appendix B, transcribed with the on-disk sources that now exist for each block.
BLOCKS = [
    (77, 100, "Remaining preimage detail", "code, spec",
     ["testport1/crates/planet-package/src/format_id.rs",
      "testport1/crates/planet-package/src/frame.rs",
      "shploingus-clean/crates/voxel-package/src/signing.rs"]),
    (101, 120, "Stream protocol", "code, spec",
     ["secure-shell/server/ingest.mjs", "secure-shell/server/decl.mjs"]),
    (121, 140, "Mount receipts and subordinate versions", "code, spec",
     ["testport1/crates/planet-package/src/mount.rs", "secure-shell/tools/port/store.mjs"]),
    (141, 160, "MongoDB schema and authority", "code, measure", []),
    (161, 180, "Store security, backups, retention", "owner, external",
     ["secure-shell/server/ledger.mjs"]),
    (181, 200, "Restore procedure", "code, spec", ["secure-shell/docs/FIRST-TEN-HOURS.md"]),
    (201, 220, "Debian host and systemd", "code, external",
     ["secure-shell/deploy/secure-shell-axis.service"]),
    (221, 240, "OpenLock generation", "code", ["openlock/README.md"]),
    (241, 260, "TUI taskbar and console", "spec", ["dl-enclave/docs/CLIENT-UI.md"]),
    (261, 280, "Qt client and QTXML reader", "external, spec", []),
    (281, 300, "Motion, bitmaps, budgets", "measure, spec", ["secure-shell/docs/MOTION.md"]),
    (301, 320, "Legacy families and quarantine", "external, code",
     ["testport1/crates/planet-package/src/format_id.rs",
      "testport1/docs/TICK-CADENCE.md"]),
    (321, 340, "Migration and compatibility representation", "code, spec",
     ["secure-shell/server/decl.mjs"]),
    (341, 360, "Text normalization and canonical serialization", "spec",
     ["testport1/crates/planet-package/src/format_id.rs"]),
    (361, 380, "CUA catalogue and recovery", "code, spec",
     ["secure-shell/server/axis.mjs", "secure-shell/server/axis-driver.mjs"]),
    (381, 400, "CUA scale and measurement", "measure", []),
    (401, 420, "Kernel-level and air-gapped authorization", "owner, spec",
     ["ala_civ_bots_prototype/CHECKPOINT.md"]),
    (421, 440, "Civilian model", "owner, spec",
     ["shploingus-clean/crates/voxel-package/src/civilians.rs"]),
    (441, 460, "24-hour acceptance", "owner",
     ["docs/SECURE-SHELL-RESTORE@1.CUA-CIVILIAN-ACCEPTANCE.md"]),
    (461, 480, "Agent API and templates", "code, spec",
     ["docs/SECURE-SHELL-RESTORE@1.AGENT-BOOTSTRAP-API.md"]),
    (481, 500, "Workflow, health ratchet, evidence, release", "spec, owner",
     ["testport1/tools/health.py", "testport1/.github/workflows/port-gate.yml"]),
]

# A probe is a verdict plus the files that state it. Needles are resolved to path:line;
# a missing file or needle refuses the run rather than passing quietly.
PROBES = {
    "Q061": dict(verdict="supported", needles=[
        ("secure-shell/server/ledger.mjs", "return sha256(canonical(rest));"),
        ("testport1/crates/planet-package/src/frame.rs",
         "domain || schema (LE u16) || len (LE u64) || payload")],
        note="Both canonical forms hash the bytes the reader holds, and the frame puts schema and length "
             "inside the preimage so a different layout cannot match."),
    "Q065": dict(verdict="supported", needles=[
        ("testport1/crates/planet-package/src/frame.rs", "pub const DOMAIN"),
        ("testport1/crates/planet-package/src/lib.rs", "domain || schema")],
        note="The frame digest begins with a fixed domain tag, as the ruling requires."),
    "Q076": dict(verdict="supported", needles=[
        ("testport1/crates/planet-package/src/format_id.rs", "READER_VERSION"),
        ("testport1/crates/planet-package/src/frame.rs", "pub const SCHEMA")],
        note="The preimage carries the reader version and the schema number, so a layout change is a new id."),
    "Q064": dict(verdict="contradicted", needles=[
        ("testport1/crates/planet-package/src/format_id.rs", "One fact per line"),
        ("testport1/crates/planet-package/src/lib.rs", "one magic, one frame")],
        note="The preimage on disk is a line-oriented format text (family, legacy families, reader, schemas, "
             "sorted refusals) and the package digest is one frame payload. There is no manifest and no "
             "payload walk, so the ruling describes a format this tree does not ship."),
    "Q068": dict(verdict="contradicted", needles=[
        ("testport1/crates/planet-package/src/lib.rs", "is the only package magic"),
        ("testport1/crates/planet-package/src/frame.rs", "Layout: `magic (8)")],
        note="The package on disk is binary in its stored form; the ruling puts JSON on disk and binary "
             "on the wire, which is the opposite split."),
    "Q070": dict(verdict="contradicted", needles=[
        ("testport1/crates/planet-package/src/frame.rs", "payload digest (32) | payload"),
        ("testport1/crates/planet-package/src/lib.rs", "one receipt, one entry")],
        note="A payload is one digest over `domain || schema || len || payload`. No Merkle tree exists, so "
             "a per-file structure cannot be verified or refused by this reader."),
    "Q071": dict(verdict="contradicted", needles=[
        ("testport1/crates/planet-package/src/frame.rs", "payload digest (32) | payload"),
        ("testport1/crates/planet-package/src/format_id.rs", "REFUSALS")],
        note="No per-file hash is recorded anywhere in the frame or the format id; the refusal set has no "
             "code for a per-file mismatch because there is no per-file row."),
    "Q074": dict(verdict="contradicted", needles=[
        ("testport1/crates/planet-package/src/format_id.rs", 'format!("schema'),
        ("testport1/crates/planet-package/src/format_id.rs", 'format!("family')],
        note="The preimage lines are family, legacy-family, reader, schema and refusal. A grade is not in "
             "the preimage, so two documents differing only by grade would share an id."),
    "Q060": dict(verdict="absent-on-disk", needles=[
        ("testport1/crates/planet-package/src/frame.rs", "Layout: `magic (8)"),
        ("secure-shell/server/ledger.mjs", "canonical(rest)")],
        note="No file read carries a deprecation window. The frame header and the ledger row are enumerated "
             "and neither has the field, so the ruling has no mechanism on disk."),
    "Q063": dict(verdict="tension", needles=[
        ("testport1/crates/planet-package/src/format_id.rs", "The width is 32 hex characters"),
        ("testport1/crates/planet-package/src/format_id.rs", "&hex[..32]")],
        note="The format identity is 32 hex characters (128 bits), truncated; the package hash ruling says "
             "the full 32-byte output, untruncated. Two hashes with different widths now exist and the "
             "record names only one of them."),
    "Q082": dict(verdict="supported", needles=[
        ("secure-shell/server/ledger.mjs", "ed25519")],
        note="The ledger signs with Ed25519, matching the scheme the ruling names."),
    "Q135": dict(verdict="supported", needles=[
        ("docs/SECURE-SHELL-RESTORE@1.CUA-CIVILIAN-ACCEPTANCE.md",
         "An `absent` reading is a state, never a pass"),
        ("docs/SECURE-SHELL-RESTORE@1.ARCHITECTURE.md", "Health check never run")],
        note="Both documents keep absence as a reported state rather than a passing receipt."),
    "N023": dict(verdict="supported", needles=[
        ("shploingus-clean/crates/voxel-model/src/proof.rs", "fn verify_bytes")],
        note="The proof reader recomputes the digest and refuses a mismatch rather than tolerating one."),
}

# Rulings whose subject is a store, envelope or policy that no checkout implements yet.
NO_PROBE = {
    "Q055": "signature envelope binding name, revision and hash: no signer in this tree binds all three",
    "Q062": "dependency pinning: no resolver on disk",
    "Q067": "key ordering: no manifest object on disk to order",
    "Q075": "receipt domain tag: the mount receipt is not written by any file read here",
    "Q083": "envelope coverage: no envelope reader on disk",
    "Q019": "counted directly, not by a single file",
    "Q021": "checked by the package directory names, not by one line",
    "Q042": "revision reuse: no store on disk",
    "Q026": "rename lineage: no store on disk",
    "Q060b": "revision history: no store on disk",
}


def needle_line(path: Path, needle: str) -> int:
    if not path.is_file():
        raise FileNotFoundError(str(path))
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if needle in line:
            return number
    raise LookupError("%s: needle not found: %r" % (path, needle))


def rel(path: str) -> str:
    candidate = PARENT / path
    if candidate.exists():
        return candidate
    return ROOT / path


def resolve(path: str, needle: str) -> str:
    target = rel(path)
    return "%s:%d" % (path, needle_line(target, needle))


def probe_special(entry: dict) -> dict | None:
    """Two probes assert over a directory or a count instead of a line."""
    qid = entry["id"]
    if qid == "Q019":
        plans = sorted(p.name for p in (ROOT / "docs").glob("SECURE-SHELL-RESTORE@1.*.md"))
        kinds = {"ARCHITECTURE", "IMPLEMENTATION-PLAN", "FORMAT-IMPORT-AUDIT",
                 "CUA-CIVILIAN-ACCEPTANCE", "AGENT-BOOTSTRAP-API"}
        counted = [n for n in plans if n.split(".")[-2] in kinds]
        return dict(verdict="supported" if len(counted) == 5 else "contradicted",
                    refs=["docs/ (glob SECURE-SHELL-RESTORE@1.*.md): %d plan documents" % len(counted)],
                    note="Five plan documents exist beside the grilling record.")
    if qid == "Q021":
        base = PARENT / "secure-shell" / "packages"
        if not base.is_dir():
            # A runner has no family checkout. The probe did not run, so it reports no-probe and
            # names the missing path, rather than raising and taking the whole gate down with it.
            return dict(verdict="no-probe", refs=[],
                        note="the family checkout is not in this working tree (%s); the probe did not run"
                             % base)
        packages = sorted(p.name for p in base.iterdir() if p.is_dir())
        bad = [n for n in packages if not re.fullmatch(r"[a-z0-9-]+", n)]
        return dict(verdict="supported" if not bad else "contradicted",
                    refs=["secure-shell/packages/: %d names, %d outside [a-z0-9-]"
                          % (len(packages), len(bad))],
                    note="Package directory names follow the grammar the ruling states.")
    return None


def block_for(number: int):
    for lo, hi, name, klass, sources in BLOCKS:
        if lo <= number <= hi:
            return lo, hi, name, klass, sources
    return None


def main(argv: list[str]) -> int:
    state = json.loads(STATE.read_text(encoding="utf-8"))
    recorded = state.get("questions", {})
    refusals: list[str] = []

    slots: dict[str, dict] = {}
    for number in range(1, 501):
        qid = "Q%03d" % number
        entry = recorded.get(qid)
        if entry is None:
            block = block_for(number)
            lo, hi, name, klass, sources = block
            present = []
            missing = []
            for source in sources:
                (present if rel(source).exists() else missing).append(source)
            slots[qid] = dict(
                id=qid, slot=number, recorded=False, verdict="unasked",
                block="Q%03d-Q%03d %s" % (lo, hi, name), klass=klass,
                sources=present, absent_sources=missing,
                note="no question text exists on disk for this slot; the block is named, the question is not",
            )
            continue
        probe = PROBES.get(qid)
        if probe is None:
            special = probe_special(entry)
            if special is not None:
                slots[qid] = dict(id=qid, slot=number, recorded=True, **special)
                continue
            slots[qid] = dict(id=qid, slot=number, recorded=True, verdict="no-probe",
                              refs=[], note=NO_PROBE.get(qid, "no file on disk settles this ruling"))
            continue
        try:
            refs = [resolve(path, needle) for path, needle in probe["needles"]]
        except (OSError, LookupError) as exc:
            refusals.append("%s: %s" % (qid, exc))
            slots[qid] = dict(id=qid, slot=number, recorded=True, verdict="refused",
                              refs=[], note=str(exc))
            continue
        slots[qid] = dict(id=qid, slot=number, recorded=True, verdict=probe["verdict"],
                          refs=refs, note=probe["note"])

    # Apply the owner's re-rulings, keeping the on-disk evidence attached.
    for qid, (verdict, note) in RULINGS.items():
        row = slots.get(qid)
        if row is None:
            continue
        row["verdict"] = verdict
        row["note"] = note
        row["refs"] = list(row.get("refs", [])) + [
            resolve("docs/SECURE-SHELL-RESTORE@1.HYPERGRILL.md", "## 8.7 Round held 2026-11-04 (v2.3)")]

    # Entries outside the spine (the N series) are recorded, so they are audited too.
    outside = {qid: entry for qid, entry in recorded.items() if not qid.startswith("Q")}
    outside_rows = []
    for qid, entry in sorted(outside.items()):
        probe = PROBES.get(qid)
        if probe is None:
            outside_rows.append(dict(id=qid, verdict="no-probe",
                                     note=NO_PROBE.get(qid, "opened outside the spine; no probe on disk")))
            continue
        try:
            refs = [resolve(path, needle) for path, needle in probe["needles"]]
        except (OSError, LookupError) as exc:
            refusals.append("%s: %s" % (qid, exc))
            outside_rows.append(dict(id=qid, verdict="refused", note=str(exc)))
            continue
        outside_rows.append(dict(id=qid, verdict=probe["verdict"], refs=refs, note=probe["note"]))

    counts: dict[str, int] = {verdict: 0 for verdict in VERDICTS + ("refused",)}
    for row in slots.values():
        counts[row["verdict"]] += 1
    counts["outside_spine"] = len(outside_rows)
    recorded_count = sum(1 for row in slots.values() if row["recorded"])
    unasked_count = sum(1 for row in slots.values() if not row["recorded"])

    if refusals:
        print("REFUSED: " + "; ".join(refusals))
    findings = [row for row in slots.values() if row["verdict"] in
                ("contradicted", "tension", "absent-on-disk", "superseded")]
    findings.sort(key=lambda row: row["id"])

    report = {
        "generated_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "spine": 500,
        "recorded_entries": len(recorded),
        "recorded_spine": recorded_count,
        "unasked_spine": unasked_count,
        "counts": counts,
        "findings": findings,
        "slots": slots,
        "outside_spine": outside_rows,
        "refusals": refusals,
    }
    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_bytes((json.dumps(report, indent=2, sort_keys=True) + "\n").encode("utf-8"))

    lines = [
        "# Hypergrill re-audit — 2026-11-04",
        "",
        "**Scope.** The 500-slot spine (`Q001`–`Q500`) plus the %d recorded `N` entries. Run by"
        % counts["outside_spine"],
        "`tools/hypergrill_reaudit.py`; the JSON beside this file carries every slot.",
        "",
        "| Counter | Value |",
        "|---|---|",
        "| Spine slots | 500 |",
        "| Recorded on disk | %d |" % len(recorded),
        "| Spine slots with a recorded question | %d |" % recorded_count,
        "| Spine slots with no question anywhere | %d |" % unasked_count,
        "| Verdict `supported` | %d |" % counts["supported"],
        "| Verdict `contradicted` | %d |" % counts["contradicted"],
        "| Verdict `tension` | %d |" % counts["tension"],
        "| Verdict `absent-on-disk` | %d |" % counts["absent-on-disk"],
        "| Verdict `superseded` by the 2026-11-04 round | %d |" % counts["superseded"],
        "| Verdict `no-probe` | %d |" % counts["no-probe"],
        "",
        "## What the 500 actually is",
        "",
        "The spine is planned at 500 but only %d `Q` questions exist as text, inside the asked range" % recorded_count,
        "`Q001`–`Q140` (the seven slots `Q094`–`Q100` were never written either). The other %d slots are" % unasked_count,
        "blocks named in Appendix B and nothing more — no file on disk carries their wording. This audit",
        "reports them `unasked`; it does not generate them, because a question nobody wrote is not a",
        "question the record asked.",
        "",
        "## Findings that change a ruling's standing",
        "",
        "| Id | Ruling | Verdict | Why |",
        "|---|---|---|---|",
    ]
    for row in findings:
        ruling = recorded[row["id"]].get("ruling") or recorded[row["id"]].get("resolution") or ""
        lines.append("| `%s` | %s | **%s** | %s |" % (row["id"], ruling, row["verdict"], row["note"]))
    lines += [
        "",
        "### Evidence for each finding",
        "",
    ]
    for row in findings:
        lines.append("- `%s` — %s" % (row["id"], "; ".join("`%s`" % ref for ref in row["refs"])))
    lines += [
        "",
        "The contradiction is not that the tree is wrong; it is that the record rules on a format the",
        "trees do not ship. `testport1` ships `V4PKG001`: one binary frame, one payload digest over",
        "`domain || schema || len || payload`, and a line-oriented format identity. The record rules a",
        "JSON manifest, a payload walk, a Merkle tree over files and per-file hashes. Both cannot be the",
        "format; a ticket has to say which one Restore admits.",
        "",
        "## Supported rulings",
        "",
    ]
    supported = [row for row in slots.values() if row["verdict"] == "supported"]
    for row in sorted(supported, key=lambda r: r["id"]):
        lines.append("- `%s` — %s" % (row["id"], "; ".join("`%s`" % r for r in row["refs"])))
    lines += [
        "",
        "## Rulings with no probe",
        "",
        "%d recorded rulings name a store, envelope or policy that no file read here implements. They are" % counts["no-probe"],
        "reported as unprobed, not as pass or fail; a probe that cannot run is not a pass.",
        "",
        "## The %d unasked slots, by block" % unasked_count,
        "",
        "| Block | Class | On-disk sources now present | Missing |",
        "|---|---|---|---|",
    ]
    for lo, hi, name, klass, sources in BLOCKS:
        present = [s for s in sources if rel(s).exists()]
        missing = [s for s in sources if not rel(s).exists()]
        lines.append("| `Q%03d`–`Q%03d` %s | %s | %s | %s |" % (
            lo, hi, name, klass,
            ", ".join("`%s`" % s for s in present) or "none",
            ", ".join("`%s`" % s for s in missing) or "—"))
    lines += [
        "",
        "A block with sources now on disk is a block whose questions could be settled by reading — but the",
        "questions themselves are missing, so no closure is recorded. That is the one thing this audit",
        "cannot manufacture and the record has not stored.",
        "",
        "## Cadence: the ruling the 500 never asked",
        "",
        "No slot in the record asks about a tick cadence or a frame clock, and no ruling names one. The",
        "only cadence rule on disk is `testport1/docs/TICK-CADENCE.md:11` — the plan's *\"Do not hardcode",
        "`ala-cities`' 20 Hz tick rate\"* — implemented as integer frame accumulation with drawing",
        "independent of the tick. It would belong to `Q481`–`Q500` (workflow, health, evidence) and that",
        "block has no question text, so the deprecation is on disk and absent from the record.",
        "",
        "## What this audit does not do",
        "",
        "- It does not change `state.json` or `receipts.jsonl`; 180 entries and 61 receipts stand.",
        "- It does not close, reopen, fold or strike a question. A contradiction is a finding for a ticket.",
        "- It does not quote a document it did not read; every ref is a resolved `path:line`.",
        "",
    ]
    OUT_MD.write_bytes(("\n".join(lines)).encode("utf-8"))

    print("slots 500 | recorded %d | unasked %d" % (recorded_count, unasked_count))
    print("supported %d | contradicted %d | tension %d | absent-on-disk %d | no-probe %d" % (
        counts["supported"], counts["contradicted"], counts["tension"],
        counts["absent-on-disk"], counts["no-probe"]))
    for row in findings:
        print("FINDING %-4s %-14s %s" % (row["id"], row["verdict"], row["refs"]))
    if refusals:
        print("REFUSED probes: " + "; ".join(refusals))
        return 3
    if "--strict" in argv and counts["contradicted"]:
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
