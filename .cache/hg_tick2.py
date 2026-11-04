import json
import pathlib
import re
import subprocess
import sys
import tempfile


def line_of(path, needle):
    text = pathlib.Path(path).read_text(encoding="utf-8", errors="replace")
    pattern = re.compile(r"\s+".join(re.escape(part) for part in needle.split()))
    match = pattern.search(text)
    if not match:
        raise SystemExit(f"anchor not found in {path}: {needle!r}")
    return text[: match.start()].count("\n") + 1


def ev(path, needle, note):
    return {"kind": "doc", "ref": f"{path}:{line_of(path, needle)}", "note": note}


ARCH = "docs/SECURE-SHELL-RESTORE@1.ARCHITECTURE.md"

receipt = {
    "question": "Q091",
    "class": "spec",
    "evidence": [
        ev(ARCH, "part of the BLAKE3 preimage", "the revision is outside identity"),
        ev(ARCH, "The hash covers the package alone", "content identity is the package bytes"),
    ],
    "resolution": (
        "No new revision. The revision is not part of the BLAKE3 preimage and the hash covers the "
        "package alone, so adding a signature changes neither identity nor content; the event is "
        "recorded in the ledger and the store's envelope set, not in the revision number."
    ),
    "effect": (
        "A signature may be added to a published package in place. The revision does not move, and "
        "the ledger records a signature event against the same hash."
    ),
}

with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False, encoding="utf-8") as fh:
    json.dump(receipt, fh)
    tmp = fh.name
proc = subprocess.run([sys.executable, "tools/hypergrill_resolver.py", "resolve", tmp],
                      capture_output=True, text=True)
print("Q091 exit=%d %s" % (proc.returncode, (proc.stdout or proc.stderr).strip()[:160]))

failures = []


def check(name, ok, detail=""):
    print(f"{'PASS' if ok else 'FAIL'}  {name}{'' if ok else '  <- ' + detail}")
    if not ok:
        failures.append(name)


raw = pathlib.Path("AGENTS.md").read_bytes()
text = raw.decode("utf-8")
check("AGENTS.md decodes as UTF-8", True)
check("AGENTS.md has no CR", b"\r" not in raw, f"{raw.count(chr(13).encode())} CR bytes")
check("AGENTS.md has no BOM", not raw.startswith(b"\xef\xbb\xbf"))
heads = re.findall(r"^## (.+)$", text, re.M)
check("AGENTS.md keeps 15 sections (-1, 0-13)", len(heads) == 15, f"{len(heads)}: {heads}")
check("AGENTS.md keeps the -1 section", heads[0].startswith("-1. Build the maximal system now"), heads[0])
check("AGENTS.md records the driver-loop ruling",
      "The driver loop governs; manual rounds are the fallback" in text)
check("AGENTS.md still forbids a script marking an answer",
      "may not mark one answered" in text)
check("AGENTS.md keeps the three-source provenance refusals",
      "attribution-laundered" in text and "attribution-missing" in text)

worksheet = pathlib.Path("docs/SECURE-SHELL-RESTORE@1.HYPERGRILL.md").read_text(encoding="utf-8")
check("worksheet records the 2026-11-04 format rulings", "8.1 Format rulings (2026-11-04)" in worksheet)
check("worksheet keeps DECISIONS.md absent by ruling", "stays absent until a round produces entries" in worksheet)

state = json.loads(pathlib.Path("docs/hypergrill/state.json").read_text(encoding="utf-8"))
questions = state.get("questions", state)
entries = questions.values() if isinstance(questions, dict) else questions
counts = {"resolved": 0, "open": 0, "folded": 0}
for entry in entries:
    status = entry.get("status") if isinstance(entry, dict) else None
    if status in counts:
        counts[status] += 1
print("state counts:", counts)
check("exactly one question is still open", counts["open"] == 1, f"open={counts['open']}")
check("nothing new was folded", counts["folded"] == 1, f"folded={counts['folded']}")

receipts = pathlib.Path("docs/hypergrill/receipts.jsonl").read_text(encoding="utf-8").strip().splitlines()
check("receipts grew by the tickets closed this tick", len(receipts) >= 19, f"receipts={len(receipts)}")
check("DECISIONS.md still absent", not pathlib.Path("docs/DECISIONS.md").exists())

print(f"\nRESULT: {'PASS' if not failures else 'FAIL ' + str(failures)}")
sys.exit(0 if not failures else 1)
