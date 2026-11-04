"""Insert 8.7, the round held after the re-audit, with the owner's words verbatim."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WS = ROOT / "docs" / "SECURE-SHELL-RESTORE@1.HYPERGRILL.md"

raw = WS.read_bytes().decode("utf-8")
if "## 8.7 Round held 2026-11-04 (v2.3)" in raw:
    print("8.7 already present")
    raise SystemExit(0)

SECTION = """## 8.7 Round held 2026-11-04 (v2.3): the re-audit's residue

Eight questions put to the owner after the 500-slot re-audit; seven answered, one returned as a
search task. Answers are recorded in the owner's words and are not curated.

| Id | Question | Owner's words | State |
|---|---|---|---|
| `A-01` | Which package format does Restore admit: the on-disk `V4PKG001` frame, or the ruled manifest/Merkle shape? | "The ruled manifest/Merkle shape" | answered |
| `A-02` | Both hashes: separate widths, or one? | "Full 64 hex for both" | answered |
| `A-03` | `Q060`'s deprecation window, which no file carries | "Add the field now" | answered |
| `A-04` | Is the grade in the preimage, as `Q074` rules? | "Add grade to the preimage" | answered |
| `A-05` | How should the record treat the 367 slots with no question text? | "Write them block by block" | answered |
| `A-06` | Where does the tick-cadence deprecation belong? | "Add a cadence question and answer it" | answered |
| `A-07` | What should happen to the 119 rulings no checkout implements? | "find them?" | open — returned as a search task |
| `A-08` | Should the re-audit run in CI and fail on contradictions? | "Fail on contradiction" | answered |

**State:** asked 8 · answered 7 · open 1 · struck 0 · superseded 0 — **1 remaining**, `A-07`.

**What the answers change.** The ruled manifest/Merkle shape is the package format, so `V4PKG001` is a
legacy input that is read and converted; the five format-shape contradictions are superseded rather
than corrected on the frame. Both hashes become full 64 hex, so the 32-hex format id is a
pre-migration form. The grade joins the preimage, so a grade change is a new id. The deprecation
window becomes a required field with no implementation yet — still reported `absent-on-disk` until a
file carries it. The 367 unwritten slots are to be written block by block, format blocks first.

### A-07 — "find them?": the mechanisms that do exist

The 119 unprobed rulings were searched rather than assumed absent. Four mechanisms are on disk:

| Mechanism | Where | What it settles | What it does not |
|---|---|---|---|
| Mount-receipt store | `secure-shell/tools/port/store.mjs:20-43` (`surface.mount/2`, `STATES`, `FIELDS`, `receipt-id`) | receipt shape, idempotence, refusal states (`Q121`–`Q136`) | retention, withdrawal (`Q131`, `Q137`) |
| Checkpoint envelope | `secure-shell/server/ledger.mjs:494-532` (`ed25519`, `payload-digest`, `record-id`) | scheme, coverage, tamper refusals (`Q082`, `Q083`) | name-and-revision binding (`Q055`) |
| Signing seam | `shploingus-clean/crates/voxel-package/src/signing.rs:57-110` (`KeyId`, `Signature{algorithm, key_id}`) | key identity, algorithm refusal, one-signature shape (`Q085`, `Q086`) | multiple signatures (`Q085` still open) |
| Voxel manifest | `shploingus-clean/crates/voxel-package/src/lib.rs:103-115` (`name`, `version`, `payload`, `requires_*`) | name in the manifest, dependency pinning (`Q062`, `Q072`) | per-file rows; the manifest pins one payload digest |

Retention, deprecation windows and revision history have no file at all — `rg -i "retention|deprecat"`
finds policy prose and nothing executable. Those rulings stay `no-probe` with the missing mechanism
named, not with silence.

"""

anchor = "## Appendix A — owner rulings recorded under the retired format"
assert anchor in raw
raw = raw.replace(anchor, SECTION + anchor, 1)
WS.write_bytes(raw.encode("utf-8"))
print("8.7 inserted | bytes:", len(raw.encode("utf-8")), "| CR:", "\r" in raw)
