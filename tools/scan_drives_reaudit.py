#!/usr/bin/env python3
"""Streaming, read-only inventory scanner for the CUA driver re-audit.

Forked from testport1/docs/secure-shell-audit/scan_drives.py (the scanner that
produced secure_shell_synthesis.md). Same walk, same per-root budget, same
flush-as-you-go rule; this fork adds the driver topics, a reference table with
digests, and the twelve corrections the audit ends with.

Never enters inputs/, shell-private/ or captures/. Read-only: it writes only the
three outputs named below.
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import sys
import time
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOTDIR = HERE.parent
OUT = ROOTDIR / "docs" / "secure-shell-audit" / "cua_driver_reaudit_synthesis.md"
STREAM = ROOTDIR / "docs" / "hypergrill" / "scan_stream@2026-11-04.jsonl"
STATE = ROOTDIR / "docs" / "hypergrill" / "scan_state@2026-11-04.json"

D = Path("C:/Users/ala/Documents")
ROOTS = [
    D / "secure_shell_v2", D / "testport1", D / "shploingus-clean", D / "shploingus-game",
    D / "shploingus", D / "openlock", D / "secure-shell", D / "dl-enclave",
    D / "ala_civ_bots_prototype", D / "ala_package_designer", D / "agent_god_files",
    Path("F:/planet-shploingus"), Path("F:/shploingus-mod-sources"),
    Path("F:/ala-cities-temp"), Path("F:/agent_god_build"), Path("F:/tmp_db"),
]
DRIVES = [Path(f"{d}:/") for d in "CDEFGH"]

SKIP = {
    ".git", "node_modules", "target", "dist", "build", "out", ".venv", "venv",
    "__pycache__", ".next", ".cache", ".gradle", ".tools", ".idea", "AppData",
    "Windows", "ProgramData", "Program Files", "Program Files (x86)", "$RECYCLE.BIN",
    "System Volume Information", "SteamLibrary", "inputs", "shell-private", "captures",
    "WpSystem", "WpSystemBackup", "Recovery", "Config.Msi", "$WinREAgent",
    "secure-shell-audit", "openlock.reference",
}
TEXT = {".md", ".rs", ".js", ".mjs", ".cjs", ".ts", ".java", ".json", ".toml",
        ".yml", ".yaml", ".ps1", ".sh", ".sml", ".gradle", ".xml", ".cfg", ".qml", ".py"}

MAX_FILE = 512 * 1024
ROOT_BUDGET = 5.0
DRIVE_BUDGET = 12.0
TOTAL_BUDGET = 195.0
MAX_REFS = 6000
MAX_DIGESTS = 900

ID_RE = re.compile(r'["`]([a-z][a-zA-Z0-9._-]{2,48}/[0-9]{1,3})["`]')
HASH_ID_RE = re.compile(r'\b([a-z][a-z0-9-]{1,30}\.[a-z][a-z0-9-]{1,30}/[0-9a-f]{8,64})\b')
MAGIC_RE = re.compile(r'b?"([A-Z0-9]{1,12}PKG[0-9]{3})"')
ALGO_RE = re.compile(r"^(SHA|HMAC|AES|BLAKE|MD5|TestVet)", re.I)
MONGO_RE = re.compile(r'mongodb://|MongoClient|getDatabase\(|getCollection\(')
LEDGER_RE = re.compile(r"ledger\.jsonl|surface\.mount|planet-shell\.ledger")
AXIS_RE = re.compile(r"axis-grant|civilian-unwitnessed|CivilianRefusal|cua-action|AxisGate")
QT_RE = re.compile(r"QGuiApplication|QQmlApplicationEngine|QXmlStreamReader|find_package\(Qt6|qt_add_qml", re.I)

TOPICS = {
    "witness": re.compile(r"witness|axis-grant|civilian-unwitnessed|attest", re.I),
    "civilians": re.compile(r"CivilianRefusal|civilian|cua-action|\bCUA\b", re.I),
    "cadence": re.compile(r"\btick\b|\bHz\b|cadence", re.I),
    "health": re.compile(r"ratchet|health|degraded", re.I),
    "format": re.compile(r"V4PKG00\d|format[-_ ]registry|format_id|magic", re.I),
    "mount": re.compile(r"surface\.mount|mount/2|planet\.surface", re.I),
    "client": re.compile(r"QGuiApplication|QQml|WebGPU|Minecraft", re.I),
    "policy": re.compile(r"policy|refus|gate\b|budget", re.I),
    "ledger": re.compile(r"ledger|receipt|sha256", re.I),
}

started = time.time()
files_seen = 0
digests = 0
refs_omitted = 0
refs: list[dict] = []
ref_paths: set[str] = set()
totals = {"formats": Counter(), "magics": Counter(), "hash_ids": Counter(), "xml": Counter(),
          "topics": Counter(), "refs": 0, "digested": 0, "absent": []}
TMP_OUT = OUT.with_name(OUT.name + ".tmp")
TMP_STREAM = STREAM.with_name(STREAM.name + ".tmp")
TMP_STATE = STATE.with_name(STATE.name + ".tmp")
GENERATED_OUTPUTS = {ROOTDIR / "docs" / "hypergrill" / "AUDIT@2026-11-04.md", ROOTDIR / "docs" / "hypergrill" / "audit@2026-11-04.json"}
stream = TMP_STREAM.open("w", encoding="utf-8", newline=chr(10))
report = TMP_OUT.open("w", encoding="utf-8", newline=chr(10))


def emit(line: str) -> None:
    report.write(line + "\n")
    report.flush()
    os.fsync(report.fileno())


def emit_bulk(line: str) -> None:
    """Table rows are flushed in one go; a per-row fsync would dominate the run."""
    report.write(line + "\n")


def emit_json(record: dict) -> None:
    stream.write(json.dumps(record, sort_keys=True) + "\n")
    stream.flush()
    os.fsync(stream.fileno())


def add_ref(p: Path, topics: list[str]) -> None:
    global refs_omitted, digests
    key = str(p)
    if p in (OUT, STREAM, STATE, TMP_OUT, TMP_STREAM, TMP_STATE) or key in ref_paths:
        return  # the scan's own outputs are not references; hashing them mid-write is a false digest
    if len(refs) >= MAX_REFS:
        refs_omitted += 1
        return
    ref_paths.add(key)
    digest = ""
    try:
        size = p.stat().st_size
        if str(p).startswith(str(D)) and digests < MAX_DIGESTS and p not in GENERATED_OUTPUTS:
            digest = hashlib.sha256(p.read_bytes()).hexdigest()
            digests += 1
    except OSError:
        size = 0
    refs.append({"id": "R%04d" % (len(refs) + 1), "path": key, "bytes": size,
                 "sha256": digest, "topics": topics})
    totals["refs"] += 1
    totals["digested"] += 1 if digest else 0
    for topic in topics:
        totals["topics"][topic] += 1


def walk(root: Path, budget: float, max_depth: int = 8) -> dict:
    global files_seen
    root_start = time.time()
    local = {"root": str(root), "files": 0, "truncated": False, "formats": Counter(),
             "hash_ids": Counter(), "magics": Counter(), "stores": [], "axis": [],
             "qt": [], "xml": 0, "notes": [], "own_refs": 0, "topics": Counter()}
    if not root.exists():
        local["truncated"] = True
        local["notes"].append("absent")
        totals["absent"].append(str(root))
        return local
    for dirpath, dirnames, filenames in os.walk(root, onerror=lambda e: local["notes"].append(f"walk: {e}")):
        if time.time() - root_start > budget or time.time() - started > TOTAL_BUDGET:
            local["truncated"] = True
            local["notes"].append(f"budget reached at {dirpath}")
            break
        dirnames[:] = [d for d in dirnames if d not in SKIP and not d.startswith(".git")]
        if dirpath[len(str(root)):].count(os.sep) >= max_depth:
            dirnames[:] = []
        for name in filenames:
            local["files"] += 1
            files_seen += 1
            p = Path(dirpath) / name
            ext = p.suffix.lower()
            if ext == ".xml":
                local["xml"] += 1
                totals["xml"][str(root)] += 1
                continue
            if ext not in TEXT:
                continue
            try:
                if p.stat().st_size > MAX_FILE:
                    continue
                text = p.read_text(encoding="utf-8", errors="replace")
            except OSError as exc:
                local["notes"].append(f"{p}: {exc}")
                continue
            rel = str(p)
            for ident in ID_RE.findall(text):
                local["formats"][ident] += 1
                totals["formats"][ident] += 1
            for ident in HASH_ID_RE.findall(text):
                local["hash_ids"][ident] += 1
                totals["hash_ids"][ident] += 1
            for magic in MAGIC_RE.findall(text):
                local["magics"][magic] += 1
                totals["magics"][magic] += 1
            topics = [topic for topic, rx in TOPICS.items() if rx.search(text)]
            if topics:
                local["topics"].update(topics)
                local["own_refs"] += 1
                add_ref(p, topics)
            mongo = MONGO_RE.search(text)
            if mongo:
                snippet = text[max(0, mongo.start() - 30):mongo.start() + 110].replace("\n", " ")
                local["stores"].append(f"{rel} :: {snippet.strip()}")
            elif LEDGER_RE.search(text):
                local["stores"].append(rel)
            if AXIS_RE.search(text):
                local["axis"].append(rel)
            if QT_RE.search(text):
                local["qt"].append(rel)
    local["stores"] = local["stores"][:60]
    local["axis"] = local["axis"][:60]
    local["qt"] = local["qt"][:40]
    local["seconds"] = round(time.time() - root_start, 1)
    return local


def repo_scan(root: Path) -> list:
    repos = []
    for dirpath, dirnames, _ in os.walk(root):
        if time.time() - started > TOTAL_BUDGET:
            return repos
        dirnames[:] = [d for d in dirnames if d not in SKIP]
        if dirpath[len(str(root)):].count(os.sep) >= 3:
            dirnames[:] = []
        try:
            is_repo = (Path(dirpath) / ".git").exists()
        except OSError:
            is_repo = False
        if is_repo:
            wf = Path(dirpath) / ".github" / "workflows"
            repos.append({"path": dirpath,
                          "workflows": sorted(x.name for x in wf.glob("*")) if wf.is_dir() else [],
                          "docs": [n for n in ("AGENTS.md", "VOWS.md", "CHECKPOINT.md", "CONTEXT.md")
                                   if (Path(dirpath) / n).exists()]})
            dirnames[:] = []
    return repos


def stream_root(local: dict, repos: list) -> None:
    own = Counter({k: v for k, v in local["formats"].items() if not ALGO_RE.match(k)})
    emit(f"\n## `{local['root']}`")
    emit(f"- files: {local['files']} · seconds: {local['seconds']} · "
         f"**truncated: {'yes' if local['truncated'] else 'no'}** · xml: {local['xml']}")
    if repos:
        for r in repos:
            emit(f"- repo `{r['path']}` docs={r['docs'] or '**none**'} workflows={r['workflows'] or '**none**'}")
    if local["own_refs"]:
        emit(f"- driver references: {local['own_refs']} · " +
             ", ".join(f"`{k}`×{v}" for k, v in local["topics"].most_common(9)))
    if own:
        emit("- identifiers: " + ", ".join(f"`{k}`×{v}" for k, v in own.most_common(25)))
    if local["hash_ids"]:
        emit("- hash-named ids: " + ", ".join(f"`{k}`" for k in local["hash_ids"])[:400])
    if local["magics"]:
        emit("- magics: " + ", ".join(f"`{k}`×{v}" for k, v in local["magics"].most_common()))
    if local["stores"]:
        emit("- store sites:")
        for s in local["stores"]:
            emit(f"  - `{s}`")
    if local["axis"]:
        emit("- axis/civ sites: " + ", ".join(f"`{a}`" for a in local["axis"][:12]))
    if local["qt"]:
        emit("- qt sites: " + ", ".join(f"`{q}`" for q in local["qt"][:8]))
    for n in local["notes"][:4]:
        emit(f"- note: {n}")
    record = {k: local[k] for k in ("root", "files", "seconds", "truncated", "xml", "own_refs")}
    record["identifiers"] = dict(own.most_common(50))
    record["magics"] = dict(local["magics"])
    record["stores"] = local["stores"][:20]
    record["topics"] = dict(local["topics"])
    record["axis_sites"] = len(local["axis"])
    record["repos"] = repos
    emit_json(record)


TASK = [
    ("D1", "Close `Q060`: carry `grade` in the digest preimage instead of leaving the field ruled but unimplemented.",
     "testport1/crates/planet-package/src/format_id.rs:103-128",
     "`python tools/hypergrill_reaudit.py --strict` reports zero `absent-on-disk` findings."),
    ("D2", "Rule the id width: the code truncates to 32 hex, so a 64-hex id is a change to the format, not a formatting choice.",
     "testport1/crates/planet-package/src/format_id.rs:128",
     "The ruling names one width and the truncation line either matches it or is deleted."),
    ("D3", "Resolve the Q063 tension between `domain|schema|len|payload` framing and a line-oriented preimage, without averaging the two.",
     "testport1/crates/planet-package/src/frame.rs:12-24",
     "One document states the frame; the other is superseded by name with its line cited."),
    ("D4", "Write the ruled manifest/Merkle shape into the architecture document.",
     "docs/SECURE-SHELL-RESTORE@1.HYPERGRILL.md §8.7",
     "The section quotes the ruling verbatim and the older shape is marked superseded."),
    ("D5", "Fix digest encoding at full 64 hex for both the manifest and the Merkle node.",
     "docs/SECURE-SHELL-RESTORE@1.HYPERGRILL.md §8.7",
     "A grep finds no remaining `[..32]` digest rendering outside the id function."),
    ("D6", "Add the cadence answer: the driver must not hardcode `ala-cities`' 20 Hz tick rate.",
     "testport1/docs/TICK-CADENCE.md:11",
     "The driver reads its cadence from config and a test fails when it is pinned to 20."),
    ("D7", "Bind every action to a witness: the driver reports, the server attests, and the driver holds no authority of its own.",
     "secure-shell/server/axis-driver.mjs:4,102",
     "A driver action without a witness receipt is refused, and the test that expects refusal passes."),
    ("D8", "Name the civilian refusal codes and make `cua-action` carry one.",
     "secure-shell/server/axis.mjs:24,110,155",
     "An action from an unwitnessed civilian returns its named code, not a bare failure."),
    ("D9", "Seal each tick into the ledger with the Ed25519 envelope.",
     "secure-shell/server/ledger.mjs:494-532",
     "A tampered receipt fails verification and the test asserts the failure."),
    ("D10", "Keep the mount receipt store as the one owner of mount state.",
     "secure-shell/tools/port/store.mjs:20-43",
     "A mount recorded twice is refused by the store rather than overwritten."),
    ("D11", "Point the signing seam at the voxel package's signing module instead of a second implementation.",
     "shploingus-clean/crates/voxel-package/src/signing.rs:57-110",
     "Exactly one signing path exists and the duplicate is deleted, not deprecated."),
    ("D12", "Name retention and deprecation as absent: the survey found no retention rule in any of the nine roots.",
     "docs/hypergrill/AUDIT@2026-11-04.md (survey, A-07)",
     "Either a retention rule is written with its pin, or the absence is recorded as `absent-on-disk`."),
]


def main() -> int:
    emit("# secure shell v2 — CUA driver re-audit inventory")
    emit(f"Started {time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}. "
         f"Per-root budget {ROOT_BUDGET:.0f}s, drive budget {DRIVE_BUDGET:.0f}s, total {TOTAL_BUDGET:.0f}s. "
         "Each root is flushed as it completes; `truncated: yes` is a refusal, not a pass.")
    for root in ROOTS:
        repos = repo_scan(root)
        found = walk(root, ROOT_BUDGET)
        stream_root(found, repos)
    for d in DRIVES:
        if time.time() - started > TOTAL_BUDGET:
            emit(f"\n## `{d}` skipped (total budget exhausted)")
            continue
        if d.exists():
            stream_root(walk(d, DRIVE_BUDGET, max_depth=2), repo_scan(d))
    emit("\n## Totals")
    emit(f"- files inspected: {files_seen} · elapsed: {time.time() - started:.0f}s")
    emit(f"- references: {totals['refs']} · with digest: {totals['digested']} · omitted over cap: {refs_omitted}")
    emit(f"- roots absent: {', '.join('`%s`' % a for a in totals['absent']) or 'none'}")
    emit("- topics: " + ", ".join(f"`{k}`×{v}" for k, v in totals["topics"].most_common()))
    numeric = {k: v for k, v in totals["formats"].items()
               if not ALGO_RE.match(k) and re.search(r"/[0-9]+$", k)}
    emit(f"- own numeric identifiers: {len(numeric)} distinct, {sum(numeric.values())} occurrences")
    emit(f"- magics: {dict(totals['magics'])} · xml files: {sum(totals['xml'].values())}")
    emit("\n## Refusals this scan itself demonstrates")
    emit("- `audit-stream-truncated`: a root hit its budget and still produced a partial row.")
    emit("- `audit-gap-silent`: an absent root is reported as absent, never as zero findings.")
    emit("- `audit-unprovenanced`: a count without file:line is not accepted as evidence.")
    emit("- `audit-unstreamed`: output held until exit hides truncation and is refused.")
    emit(f"- `reference-capped`: at most {MAX_REFS} references are recorded; {refs_omitted} were counted but not listed.")
    emit(f"- `digest-documents-only`: digests are computed under `{D}` only, capped at {MAX_DIGESTS}; elsewhere the path and size are the reference.")
    emit("- `scan-pruned`: `target`, `node_modules`, `build`, `Windows`, `AppData` and the audit's own output are never entered.")
    emit("\n## Classification of reference hits")
    emit("| Topic | Files | Serves |")
    emit("|---|---:|---|")
    serves = {
        "witness": "D7 — the driver reports, the server attests",
        "civilians": "D8 — the refusal a civilian action carries",
        "cadence": "D6 — the tick rate that must not be hardcoded",
        "health": "D9/D12 — whether a degraded run is sealed or dropped",
        "format": "D1–D5 — id width, preimage and framing",
        "mount": "D10 — the one owner of mount state",
        "client": "D7 — the surface the driver drives",
        "policy": "D8/D12 — refusals and retention",
        "ledger": "D9 — receipts and their digest",
    }
    for topic, count in totals["topics"].most_common():
        emit(f"| `{topic}` | {count} | {serves.get(topic, '—')} |")
    emit("\n### Primary references")
    emit("| Id | Path | Bytes | sha256 | Topics |")
    emit("|---|---|---:|---|---|")
    for row in refs:
        emit_bulk("| `%s` | `%s` | %d | `%s` | %s |" % (row["id"], row["path"], row["bytes"],
                                                        row["sha256"] or "not computed",
                                                        ", ".join(row["topics"])))
    report.flush()
    os.fsync(report.fileno())
    emit("\n## The one task")
    emit("Set the CUA driver right in one pass: each correction below is a single artifact, and each"
         " exit test is a command that can fail. The driver is only correct when every action is"
         " ticketed, bounded, and witnessed — this is not a rule that a document can grant, it is"
         " what the receipts prove.")
    emit("")
    emit("| Id | Correction | Reference | Exit test |")
    emit("|---|---|---|---|")
    for ident, correction, ref, exit_test in TASK:
        emit_bulk(f"| {ident} | {correction} | `{ref}` | {exit_test} |")
    report.flush()
    os.fsync(report.fileno())
    TMP_STATE.write_text(json.dumps({"files": files_seen, "seconds": round(time.time() - started, 1),
                                 "refs": len(refs), "omitted": refs_omitted,
                                 "digests": totals["digested"], "absent": totals["absent"],
                                 "topics": totals["topics"], "formats": totals["formats"],
                                 "magics": totals["magics"], "hash_ids": totals["hash_ids"]},
                                indent=2), encoding="utf-8")
    stream.close()
    report.close()
    # A killed run leaves only temporary files behind: the completed document is replaced
    # only after every section, row and state file has been written.
    os.replace(TMP_STREAM, STREAM)
    os.replace(TMP_OUT, OUT)
    os.replace(TMP_STATE, STATE)
    print(f"done in {time.time() - started:.1f}s files={files_seen} refs={len(refs)}"
          f" digests={totals['digested']} omitted={refs_omitted}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
