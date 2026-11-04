from pathlib import Path

repo = Path("../secure-shell")
axis = (repo / "server/axis.mjs").read_text(encoding="utf-8").split("\n")
drv = (repo / "server/axis-driver.mjs").read_text(encoding="utf-8").split("\n")
srv = (repo / "server/axis-server.mjs").read_text(encoding="utf-8").split("\n")


def line_of(lines, needle):
    hits = [i + 1 for i, l in enumerate(lines) if needle in l]
    assert hits, "missing: " + needle
    return hits[0]


L = {
    "ATTEST": line_of(axis, "function attest("),
    "CAPCHECK": line_of(axis, "if (!driver.capabilities.includes(action))"),
    "ACT": line_of(axis, "function act("),
    "RECEIPT": line_of(axis, "const receipt = Object.freeze({"),
    "DIGEST": line_of(axis, "digest: text(input.digest)"),
    "LEARN": line_of(axis, 'throw new AxisError("learning-digest"'),
    "TTL": line_of(axis, "ticketTtlMs"),
    "CAPS": line_of(drv, "export const CAPABILITIES"),
    "WITNESS": line_of(drv, "async function witness("),
    "APPLY": line_of(drv, "async function applyLearning("),
    "ACTROUTE": line_of(srv, "/api/axis/act"),
}
print("refs:", L)

SEC = """### 11.4 `ala_civ_bots_prototype/CHECKPOINT.md` (2026-11-02, 54,028 bytes)

**Provenance.** `C:/Users/ala/Documents/ala_civ_bots_prototype/CHECKPOINT.md`, 54,028 bytes, last
written 2026-11-02. It is that project's execution log for a Minecraft/Fabric mod and the Node
mineflayer body — not a Secure Shell specification. It is read because §10 pins that project's body as
this acceptance's operation layer.

**What it specifies.**

- "Axis is not a Node-side decision layer." The Node process "only executes motor frames and connects
  directly to the Minecraft server."
- Evidence is per body: `observation.mjs` "records logical render snapshots (position, yaw/pitch, held
  item, nearby blocks/entities, screen) on each frame", and it is "deliberately `mode=logical-headless`:
  no GPU frame or audio device is claimed."
- A count is not a decision: "`civilian.axis-cells/1` rows are 200-decision count batches, not a
  decision tree".
- One gate: "`WorldState.accept` is the only gate, and its answer
  (`APPLIED`/`REPLAYED`/`STALE`/`WRONG_WORLD`) is what a caller must handle."

**Delta against the driver.**

- *Agrees.* The driver "holds no authority of its own" (`server/axis-driver.mjs:4`) and
  `server/axis.mjs:__ACT__` is the single act gate. The document's division is the code's division.
- *Lacks.* The receipt has no body, no observation and no count: `server/axis.mjs:__RECEIPT__` records
  `{schema, at, ticket, driver, action, scope, digest}`. The per-body render snapshot has no
  counterpart — `witness()` reads bytes and hashes them (`server/axis-driver.mjs:__WITNESS__`) and
  never observes a scene.
- *Not encoded.* Nothing in the receipt can say whether a number is a decision or a summary batch.

E5 covers the observation field and E7 the body identity; the batch distinction is named and carries no
proposal, because nothing in this driver records decisions yet.

### 11.5 `AXIS-MODULE.md` (2026-10-06, 24,913 bytes)

**Provenance.** `C:/Users/ala/Documents/agent_god_files/reference/AXIS-MODULE.md`, 24,913 bytes, signed
2026-10-05 and last written 2026-10-06. It is the approved module note for the planet-god-files axis
gate; the repo already cites its §2 refusal. It is not a Secure Shell specification.

**What it specifies.**

- "no mining, no hash lottery, no incentives, no consensus set."
- "Every proof is **anchored**: `{ artifact, claim, origin, evidence, tick_span, world_digest }`."
- "A proof is **current** only within a declared tick window." "**Stale is refused; nothing is
  grandfathered; nothing enters mid-tick.**"
- "a missing instrument is a refusal; silence is not permission; **a refusal nobody can read did not
  happen.**"

**Delta against the driver.**

- *Lacks a window.* The ticket has a lifetime (`server/axis.mjs:__TTL__`), but the receipt carries no
  `tick_span`, no `world_digest` and no evidence window: `server/axis.mjs:__RECEIPT__`. Nothing in a
  receipt can go stale, so "nothing is grandfathered" has no mechanism to enforce.
- *Refusals are said, not recorded.* A refusal is thrown (`AxisError` at `server/axis.mjs:29`) and
  returned as an HTTP error (`server/axis-server.mjs:__ACTROUTE__`), and `act()` appends only successful
  receipts (`server/axis.mjs:__RECEIPT__`). The sentence "a refusal nobody can read did not happen" is
  not met.
- E8 below is the rule this grounds.

### 11.6 `dl-enclave/docs/DRIFT.md` (2026-10-30, 25,560 bytes)

**Provenance.** `C:/Users/ala/Documents/dl-enclave/docs/DRIFT.md`, 25,560 bytes, last written
2026-10-30. A drift census of thirteen project folders, gathered for dl-enclave; not a Secure Shell
specification.

**What it specifies.**

- "declarations generate the artifacts, one reader owns each format, and a witness is a record, not a
  glance."
- "**HMAC is symmetric**, so every verifier is also a forger."
- A road is not a permission; it is an `allowed: Vec<Capability>` that "may only ever narrow its
  source's capabilities". The finding is that "the gate and the grant never meet."

**Delta against the driver.**

- *Lacks narrowing.* A driver's capabilities are the driver's own declaration
  (`server/axis-driver.mjs:__CAPS__`), and the axis checks only that the requested action is among them
  (`server/axis.mjs:__CAPCHECK__`). Nothing compares the declared set with what the attestation grants,
  so a driver can widen itself by editing its own list.
- *Weaker than the document's concern.* `attest()` takes a `verifier` string and an expiry
  (`server/axis.mjs:__ATTEST__`) — no key and no signature at all, so the document's symmetric-HMAC
  problem is replaced by an unauthenticated name.
- E9 below is the rule this grounds.

### 11.7 `dl-enclave/docs/CLIENT-UI.md` (2026-10-30, 45,827 bytes)

**Provenance.** `C:/Users/ala/Documents/dl-enclave/docs/CLIENT-UI.md`, 45,827 bytes, last written
2026-10-30. The enclave's visual and interaction specification; its own subject is the enclave's client
and TUI, not this shell.

**What it specifies.**

- "The client is never an authority. It renders verdicts the enclave already made, and every refusal it
  shows carries the enclave's code verbatim."
- A refusal shows "the code in mono (`not-attenuated`), the sentence *what* was refused, **who** refused
  it (the enclave, never the client), and one recovery line."
- "No retry button exists unless the enclave returned a retryable code".

**Delta against the driver.**

- *Agrees.* The driver renders nothing and decides nothing (`server/axis-driver.mjs:4`); authority sits
  at `server/axis.mjs:__ACT__`.
- *Lacks two fields.* The axis error carries code, subject and why only (`server/axis.mjs:29`), so a
  refusal cannot say **who** refused it or offer a recovery line, and there is no retryability flag. The
  shell has no client surface at all — `server/axis-server.mjs:__ACTROUTE__` returns JSON.
- E8 is extended with `refusedBy` and one recovery line rather than duplicated.

### 11.8 `income-engine/cua_worker.py` (2026-09-18, 28,161 bytes)

**Provenance.**
`C:/Users/ala/Documents/shploingus-game/references/Docs-A/tiket-ledger-reference/income-engine/cua_worker.py`,
28,161 bytes, last written 2026-09-18. A reference copy of the income-engine's coordinator between a
money engine and the cua SDK; not a Secure Shell specification.

**What it specifies.**

- "No channel policy — not even `agent_ok` — permits an agent to create an account, enter credentials,
  move money, accept terms, or sign anything. Those are `HARD_DENY`."
- "the planner does not emit the task; it raises a **gate** instead"
- "The deny-by-default chokepoint. Unknown action => refused."
- It "never closes a task without an artifact on disk".

**Delta against the driver.**

- *Lacks a ceiling.* The axis refuses only an action the driver does not declare
  (`server/axis.mjs:__CAPCHECK__`); a driver that declares `move-money` is ticketed for it. The
  document's hard-deny set is above the axis's only check.
- *Closes without an artifact.* `act()` records the digest it was handed (`server/axis.mjs:__DIGEST__`);
  only `learning-apply` recomputes one (`server/axis.mjs:__LEARN__`). E6 already covers the
  recomputation; E10 below carries the ceiling.

### 11.9 `voxel-model/src/proof.rs` and `voxel-package/src/civilians.rs` (2026-10-14 / 2026-10-25, 4,681 + 33,514 bytes)

**Provenance.** `C:/Users/ala/Documents/shploingus-clean/crates/voxel-model/src/proof.rs` (4,681 bytes,
2026-10-14) and `.../crates/voxel-package/src/civilians.rs` (33,514 bytes, 2026-10-25). Two crates of the
older shploingus tree, read as mechanism references — the family's rule is that its old trees are
reasons, never requirements.

**What they specify.**

- "A proof is current only inside its declared window; stale is refused, nothing is grandfathered, and
  the bytes must hash to what the proof names."
- A proof is "refused rather than shown against bytes it was not made from"; "no presenter names who is
  acting; a presentation with no accountable actor is refused"; "the origin is the proof's to carry, not
  the claimant's to declare."
- "One reading per ladder, never one reading summarised onto seven." "a row that did not parse is a row,
  not an omission." "the record could not be read" and "the record does not carry this" are different
  facts.

**Delta against the driver.**

- *Corroborates E6 with a source.* `verify_bytes` recomputes the artifact digest before admitting;
  `server/axis.mjs:__DIGEST__` records what the caller asserted.
- *Lacks a presenter.* The receipt names `driver` and nothing else (`server/axis.mjs:__RECEIPT__`); the
  document refuses a presentation with no accountable actor. E7 is extended with `presenter`.
- *Collapses three answers into one.* `server/axis.mjs:__DIGEST__` writes `digest: text(input.digest) ||
  ""`, so "not read" and "absent" are both an empty string — the exact distinction `civilians.rs` keeps
  between `readable` and `present`. E11 below is the rule.

"""

doc = Path("docs/SECURE-SHELL-RESTORE@1.CUA-CIVILIAN-ACCEPTANCE.md")
raw = doc.read_bytes().decode("utf-8")
for k, v in L.items():
    SEC = SEC.replace("__%s__" % k, str(v))

old_head = "### 11.4 Named absent"
assert old_head in raw, "absence heading not found"
assert "### 11.4 `ala_civ_bots_prototype/CHECKPOINT.md`" not in raw, "already ingested"
merged = raw.replace(old_head, SEC + "### 11.10 Named absent", 1)
merged = merged.replace(
    "The table keeps its scoped claim; this line records where the documents actually are.",
    "The table keeps its scoped claim; this line records where the documents actually are. All seven\n"
    "were then read in full; §11.4–§11.9 record what each specifies against the driver, quote by quote.",
    1,
)
doc.write_bytes(merged.encode("utf-8"))
print("written | bytes:", len(merged.encode("utf-8")), "| CR:", "\r" in merged,
      "| newline:", merged.endswith("\n"))
print("headings:", [l for l in merged.split("\n") if l.startswith("### 11.")])
