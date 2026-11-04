<!-- Continuation of the SECURE-SHELL-V2 planning set. Decision 17 and 19-20 are recorded as settled, including the ratchet's role and the 24-hour target. No implementation is claimed. -->

# SECURE-SHELL-RESTORE@1 — Axis System-1 CUA and civilian acceptance

**Document identity:** `SECURE-SHELL-RESTORE@1`
**Status:** Accepted acceptance contract. Supersedes `SECURE-SHELL-V2-CUA-CIVILIAN-ACCEPTANCE.md`.

## 1. Three authorities, never merged

| Authority | Owns | May not |
|---|---|---|
| Debian server | store, package admission, signing, stream | render, focus, or witness the client |
| Axis | permission, capability, gate verdict | perform the action it authorizes |
| System-1 CUA driver | observation, diagnosis, bounded operation, verification | widen its catalogue, mint signer authority, erase evidence, certify itself |
| Civilian runtime | identity, mind, memory, work commitments, practice | manufacture institutional outcomes, grant tools, alter shared schemas |

A trained driver is still a driver. Training, confidence, and prior success never grant a capability; only a recorded Axis decision does.

## 2. The control cycle

```
observe → classify → plan → ticket → Axis gate → act → observe postcondition → verify → record → learn within scope
```

Every operation carries: stable actor identity, session identity, operation id, expected sequence/revision, ticket, presenter, action id, bounded arguments, expiry, and a typed acknowledgement.

Named refusals: stale revision, duplicate operation, out-of-scope target, unsupported action, expired ticket, permission denied, cancelled, timed-out, postcondition mismatch. Continuous input has a bounded duration and releases automatically on completion, timeout, or disconnect.

## 3. What the driver owns (decision 17)

Boot, recovery, health inspection, format identification, mounting, and pre/post-migration verification — and then more, over time:

1. **Shell lifecycle.** Start, present, mount, verify, recover, roll back.
2. **Format identification.** Name the family and revision it found. It does not guess upward.
3. **Recovery.** A state machine, not a retry loop: detect → preserve evidence → classify → choose an allowed recovery → execute once with idempotency → verify server and client postconditions → record recovered or refused.
4. **Coverage expansion.** Work through the installed system adding package cells and windows to the stream — the ratchet measures how much is streamed versus legacy, so expansion is a number with evidence.
5. **System-level operations.** Beyond the client, toward kernel-level operations on an air-gapped host managed over the network, as a security-enhanced authorization system driven by a System-1 model.

### 3.1 Staged gates for the system-level ambition

The kernel-level, air-gapped claim is staged. Each gate is a ticket with an exit test; nothing skips ahead.

| Gate | Scope | Exit evidence |
|---|---|---|
| G0 | Read-only inspection of the host | Inventory with digests; no mutation possible |
| G1 | Service lifecycle on the Debian host (restart, health, backup verify) | Postcondition observed after each action |
| G2 | Mount, rollback, restore | Prior revision survives; restore drill artifact |
| G3 | Privileged host operations through a broker | Every operation ticketed, brokered, recorded, reversible or explicitly irreversible |
| G4 | Kernel-adjacent operations on an air-gapped host | Capability catalogue entry, broker path, recovery procedure, refusal tests |
| G5 | Continuous authorization across the installed system | Ratchet shows streamed coverage rising; legacy surface shrinking with a sunset date |

`OPEN-CUA-1` holds the capability catalogue. A capability that is not catalogued cannot be requested, and an agent cannot add one.

## 4. Scale

The requirement is performance at thousands of workers. `ala_civ_bots_prototype` is the scale test that was actually run, and it is cited as evidence of the load class, not as proof that Restore inherits its architecture.

Budgets are open (`OPEN-CUA-2`), but the measurement shape is fixed from R11 onward: worker count, tick latency distribution, action throughput, queue depth, refusal rate under load, and recovery time after a worker loss. A scale claim without those numbers is `absent`.

## 5. The ratchet judges coverage, not effort

The ratchet's job (decision 17) is to judge **how much of the system is streamed versus legacy**, and it only tightens:

- A component that was streamed may not silently revert to a legacy decoder.
- A legacy surface that shrinks cannot grow back without a new ruling.
- A check that was once held may not fail again.
- Progress is reported as coverage plus refusals, not as hours spent.

This is the same discipline the family already applies to health: `held`, `absent`, `refused`. An `absent` reading is a state, never a pass.

## 6. Civilian model

Decision 19 makes civilians the model for CUA agents, with `cellular_generativity_axis_civilian_expectations_prototype_rechecked` as the current representation (blob `5af5d32388795767f02b709dbd8479eb110645c3`, 144,027 B).

What the specification establishes: stable identity and one mind decision owner; journal/snapshot recovery; practice history; needs, beliefs, intentions, reflexes; ticketed skill routines and body adapters; a System-1 sense/select/gate/act/verify progression; and some ordinary-life work, rest, social transfer, and reconnect cases.

What it does **not** establish, and Restore must not claim: a completed trained cellular-generative CUA policy. The rechecked document states no NCA/evolutionary-CA substrate was found in the inspected prototype, the local Axis authority gateway was provisional, complete post-test autonomous life and broad relationship continuity remained open, and full native client parity was not proved. This work is new implementation.

## 7. The 24-hour acceptance protocol

Decision 20: a day is 24 continuous hours. Not a compressed cadence, not a task quota.

### 7.1 Before the day

- Freeze the package set; record `name@rev+blake3:` for every surface in play.
- Record the streamed-versus-legacy ratio at start.
- Declare the task queue with inputs, owners, postconditions, windows, and exit tests.
- Declare the injected failures for the day.
- Confirm the prior admitted revision and rollback path.

### 7.2 During the day

- The driver observes and diagnoses before acting; every action is ticketed.
- The client is the witness surface: command, exit status, check count, surface id, digest.
- Work is verified from server and client postconditions, never from the driver's own report.
- Injected events: stream interruption and resume; bad chunk digest; bad signature; unknown or revoked signer; old-schema input; client crash and reconnect; store outage; stale client revision; backup restore; malformed tool arguments; expired ticket; duplicate command; denied permission.
- Civilian residents live through the day: work, rest, help-seeking, learning by observation, practice, mistake, and social transmission.

### 7.3 End of day

- Record the streamed-versus-legacy ratio at end. It must not have fallen.
- Reconcile every task against its exit test.
- Preserve refusals, timeouts, and recoveries as rows.
- Confirm residents returned to ordinary autonomous life and test-owned resources were released.
- Write the witness and the ledger row for the day.

### 7.4 Pass conditions

A day passes only if: one stable identity persisted start to finish; every task has a verified postcondition; no task was skipped, duplicated, widened, or completed without evidence; at least one interruption and one recovery completed without history loss; pre/post-split inputs were read by their exact readers with migration lineage; rollback left the prior revision available; the coverage ratio did not regress; and a real client witness confirmed the windows and at least one meaningful CUA operation.

Anything less is `refused` or `incomplete`, reported as such.

## 8. What civilians may not be used for

- They may not manufacture jobs, institutions, judges, legal findings, or social outcomes on residents' behalf.
- They may not be cited as a client witness.
- They may not certify a package, a signature, or a schema.
- They may not be counted as proof that a shell feature works because a simulation looked plausible. Plausible is the failure mode the realtime-simulation transcript warns about: off-screen fabrication, inconsistent state, jerky timing, and interactions that do not obey intended rules.

## 9. Metrics that must exist before a claim

| Metric | Refusal if missing |
|---|---|
| Streamed vs legacy coverage | `coverage-unmeasured` |
| Worker count and latency distribution | `scale-unmeasured` |
| Client witness count per day | `witness-absent` |
| Refusal counts by code | `refusals-unrecorded` |
| Recovery success and time | `recovery-unmeasured` |
| Restore reproducibility | `restore-unmeasured` |
| Migration coverage (legacy fixtures read) | `migration-unmeasured` |

## 10. Pins

`cellular_generativity_axis_civilian_expectations_prototype_rechecked.md` — blob `5af5d32388795767f02b709dbd8479eb110645c3`, 144,027 B, in `swf-cell-runtime/docs/` (and its committed copy under `docs/secure-shell-audit/`).
`ala_civ_bots_prototype` — inspected as the scale-test reference; its own continuity and action-control work is evidence, not Restore authority.

## Operation layer

The operation layer for this acceptance is the **Node CUA driver**: the mineflayer bodies that read exact AXIS packages and connect directly to the Minecraft server, as they run in `ala-civ-bots-prototype` (`tools/residents/src/main.mjs`, recorded at `CHECKPOINT.md:38` of that checkout). Recorded by the owner, 2026-11-04.

The consequence is narrow and it is the point: a body written in Node is not disqualified from this role, and a claim that only a rendered browser client may witness is refused as authority rather than applied. What the operation layer must show is unchanged — the mount, the render and the digest — and the language it is written in is not evidence of anything.

The refusal is recorded as `AV-001` in `SECURE-SHELL-RESTORE@1.HYPERGRILL.md` §8.5.

## 11. Sources ingested

Three sources are ingested for this document: two transcripts supplied by the owner, and one build
session located by the 2026-11-04 reachability enumeration. A transcript is a source, not an
instruction: it may support a premise, and it may not write a rule. Each entry separates what the source
says from what the driver takes, and names what the source refuses to support. Quotes are verbatim; the
pin for each is the document's own name, byte count and date.

### 11.1 World-model transcript (2026-11-04, 14,287 bytes)

Premise only: a body needs an understanding of the world before it can be granted control of one. It is
recorded in full in the architecture document's §8.1 and is not restated here beyond its share of this
register: the civilian acceptance document and that premise are read together.

### 11.2 Dory, NVIDIA's looped transformer (2026-11-04, 15,061 bytes)

**What it says.**

- A 3.97B model whose middle block loops: an input block of 16 layers runs once, a recurrent block of 40
  layers repeats, an output block of 16 runs once. The input block's output is re-added each lap, "like
  the ResNet models".
- The loop count is set at inference — Nvidia calls it "elastic inference compute" — because the output
  block "is trained to read the state after any of the loops. So, one loop, two loops, four loops are all
  valid models".
- Compute per token rises with laps while "the weights in memory don't change at all": 72 effective
  layers at one loop, 112 at two, 192 at four.
- More laps is not reliably better: "it's not a hard and fast rule that one of them will have more output
  tokens", and quality changes "depending on the actual problem". Against Gemma 4 26B the model wins 1 of
  10 benchmarks at one loop, 4 at two, 5 at four — and loses the knowledge benchmarks outright, which the
  source attributes to having fewer weights in which to store knowledge.
- The cost is memory, not weights: a per-loop KV cache is about 2 GB per sequence at 32k context and two
  loops against 1.32 GB in last-loop mode, where Nvidia says accuracy and length stay close.
- Deployment advice: two loops by default, four for harder agentic work, and a router in front to pick
  between them.

**What the driver takes from it — proposed, each needing its own ticket before it changes code.**
A transcript may support a rule; it may not write one, so these are proposals with an exit test each.

| Rule | The proposal | Where it binds | Exit test |
|---|---|---|---|
| E1 | An attempt records the effort it spent, per attempt, not per deployment | the act receipt | a receipt with no effort field is refused by name |
| E2 | Verification must not depend on effort: the postcondition is observed after the act, so a result verified cheaply is verified the same expensively | §2 control cycle | the same act passes the same postcondition at two effort levels |
| E3 | Effort is a declared scope on the ticket, never a knob the driver turns itself | §1, architecture §11 | a driver raising its own effort scope is refused `ticket-scope` |
| E4 | Knowledge claims are refused; the driver observes instead | §5 | an answer asserted from memory is refused as evidence |

**What it refuses to support.** It does not say the driver is, or should be, a looped transformer: it
describes an LLM and never a CUA agent. It does not say more effort improves control — the source says
quality moves "depending on the actual problem" and that it is "not something that I would just sort of
say it's the same as sort of turning up reasoning". It contains no shell operation, no benchmark of one,
and no number that may become a target here: no lap count, latency or token budget in this document is
derived from it.

### 11.3 Imported build session, `ala_civ_bots_prototype` (2026-11-01, 12,245,017 bytes)

**Provenance.** `ala_civ_bots_prototype/.cloud-attachments/imported-conversation-3cec07c402bccd33b63571cc89f60ce5c652f8ddfb482c52f5c3e792cc131197.json`,
12,245,017 bytes, last written 2026-11-01 16:05. A JSON array of 296 turns — 147 user, 149 assistant —
whose assistant turns carry embedded tool records of the form
`{"kind":"tool","toolName":...,"input":...,"output":...,"status":"success"}`. It is a session record,
not a document describing one: the act and its observation sit in the same record. It was found by
enumeration, outside both trees, and it is the build session of the Fabric mod and the Node body that §10
already pins as this acceptance's operation layer.

**What it says.**

- The interaction contract is a tuple: "perceived object identity, reachability, available capabilities,
  permission, requested operation, server-side result, observed postcondition, canonical event + evidence."
- Verification is comparative and external: "verification compares expected vs observed; the routine does
  the comparison using WorldView (world authority)."
- A claim may not exceed its observation: "the quote is the fact and the kind is a reading of it, so a
  being cannot say something its own observation does not contain, and it cannot claim support it did not
  compute."
- Its own architecture separates "10.3 Motor frames and action envelopes" from "10.4 Verify outcomes from
  world facts" — an envelope names the request, the world facts decide the result.

**What the driver takes from it — proposed, each needing its own ticket before it changes code.**

| Rule | The proposal | Where it binds | Exit test |
|---|---|---|---|
| E5 | A receipt records `expected` and `observed`, and `observed` comes from the world surface rather than from the driver's report | the `act` receipt | an act whose observed contradicts expected is recorded `postcondition-mismatch`, never `succeeded` |
| E6 | The axis recomputes the digest of the bytes it was handed instead of recording the digest the driver asserts | `act()` in `server/axis.mjs` | bytes whose hash differs from the presented digest are refused by name |
| E7 | An act carries the body identity and an action envelope — target, requested operation, capability, permission | `server/axis-driver.mjs`, the receipt | an act with no body identity is refused by name |

**What the driver gets wrong today, against that.** `act()` stores `digest: text(input.digest) || ""`, so
the receipt records what the driver *claims*. The `witness` path hashes bytes locally and then asks the
axis to record that hash; the axis never recomputes it. A receipt therefore carries a claim rather than a
computation, which is exactly what the source refuses. The receipt also has no `expected`/`observed` pair
and no body identity, and `witness()` observes nothing after acting: it returns the digest it took before
the ticket was issued.

**What it refuses to support.** It is not a Secure Shell installation record: no axis ticket, no mount, no
surface digest, and it never runs `server/axis.mjs` or `server/axis-driver.mjs`. It cannot support a claim
about the axis shell's runtime. Its tool stream also carries advertising records (`{"kind":"ad",...}`),
so it is raw and unfiltered — a source, not a clean log. It says nothing about the effort rules E1–E4.

### 11.4 `ala_civ_bots_prototype/CHECKPOINT.md` (2026-11-02, 54,028 bytes)

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
  `server/axis.mjs:178` is the single act gate. The document's division is the code's division.
- *Lacks.* The receipt has no body, no observation and no count: `server/axis.mjs:212` records
  `{schema, at, ticket, driver, action, scope, digest}`. The per-body render snapshot has no
  counterpart — `witness()` reads bytes and hashes them (`server/axis-driver.mjs:102`) and
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

- *Lacks a window.* The ticket has a lifetime (`server/axis.mjs:76`), but the receipt carries no
  `tick_span`, no `world_digest` and no evidence window: `server/axis.mjs:212`. Nothing in a
  receipt can go stale, so "nothing is grandfathered" has no mechanism to enforce.
- *Refusals are said, not recorded.* A refusal is thrown (`AxisError` at `server/axis.mjs:29`) and
  returned as an HTTP error (`server/axis-server.mjs:94`), and `act()` appends only successful
  receipts (`server/axis.mjs:212`). The sentence "a refusal nobody can read did not happen" is
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
  (`server/axis-driver.mjs:24`), and the axis checks only that the requested action is among them
  (`server/axis.mjs:155`). Nothing compares the declared set with what the attestation grants,
  so a driver can widen itself by editing its own list.
- *Weaker than the document's concern.* `attest()` takes a `verifier` string and an expiry
  (`server/axis.mjs:110`) — no key and no signature at all, so the document's symmetric-HMAC
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
  at `server/axis.mjs:178`.
- *Lacks two fields.* The axis error carries code, subject and why only (`server/axis.mjs:29`), so a
  refusal cannot say **who** refused it or offer a recovery line, and there is no retryability flag. The
  shell has no client surface at all — `server/axis-server.mjs:94` returns JSON.
- E8 carries `refusedBy` and one recovery line rather than a second rule.

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
  (`server/axis.mjs:155`); a driver that declares `move-money` is ticketed for it. The
  document's hard-deny set is above the axis's only check.
- *Closes without an artifact.* `act()` records the digest it was handed (`server/axis.mjs:215`);
  only `learning-apply` recomputes one (`server/axis.mjs:204`). E6 already covers the
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
  `server/axis.mjs:215` records what the caller asserted.
- *Lacks a presenter.* The receipt names `driver` and nothing else (`server/axis.mjs:212`); the
  document refuses a presentation with no accountable actor. E7 gains a `presenter` field.
- *Collapses three answers into one.* `server/axis.mjs:215` writes `digest: text(input.digest) ||
  ""`, so "not read" and "absent" are both an empty string — the exact distinction `civilians.rs` keeps
  between `readable` and `present`. E11 below is the rule.

### 11.10 Proposals the located documents ground

Four documents state a rule this driver does not have, and one states a field an existing rule lacks.
Each row is a proposal, not a change: no driver behaviour moves until the row has a ticket.

| Rule | The proposal | Where it binds | Exit test |
|---|---|---|---|
| E7 (extension) | The receipt names a **presenter** — the accountable actor — beside the driver id | `act()` receipt, `server/axis.mjs` | a witness presented with no presenter is refused by name |
| E8 | A refusal is recorded, not only thrown: code, subject, why, `refusedBy`, and one recovery line | `act()` and the axis refusal path, `server/axis.mjs` | a refused act leaves a readable record naming `refusedBy`, and a client renders code, who and recovery without inventing any of them |
| E9 | A driver's declared capabilities are a subset of what its attestation grants; the axis refuses the difference | `attest()` and registration, `server/axis.mjs` | a driver declaring a capability its grant does not carry is refused `capability-not-granted` |
| E10 | A hard-deny set stands above capabilities: some actions have no ticket whatever a driver declares | `requestTicket`, `server/axis.mjs` | a driver declaring `move-money` is refused `hard-deny` before a ticket exists |
| E11 | A receipt answers read, absent and refused separately, and never defaults an unread digest to empty | the `act` receipt | an act with no digest is refused by name rather than recorded `digest: ""` |

E5 and E6 are not restated: E5 already covers expected-versus-observed and E6 already covers digest
recomputation, and both are corroborated rather than extended by the documents above.

### 11.11 Named absent

These are the documents that would improve this driver and are not in either tree. Naming them is the
point: each is a place where the driver has one writer and no independent reader.

| Document | What it would supply | Referenced from | State |
|---|---|---|---|
| `ala-civ-bots-prototype/CHECKPOINT.md` | the only running Node CUA driver, and its body-to-action contract (`CHECKPOINT.md:38` is pinned in this record) | `secure-shell/docs/DECISIONS.md` | absent from both trees |
| `income-engine/cua_worker.py` | how a real worker gates an action before performing it | `secure-shell/docs/DECISIONS.md` | absent |
| `AXIS-MODULE.md` §2 | the refusal of mining and the hash lottery | `patches/PATCH-004-five-star-axis.md` | absent |
| `voxel-model/src/proof.rs`, `voxel-package/src/civilians.rs` | the ticking proof, and observe-versus-rule for civilians | `docs/PROOF-OF-WORK.md` | absent |
| `dl-enclave/docs/DRIFT.md` D-3, `CLIENT-UI.md` §8 | a refused mechanism, and the client UI boundary | `patches/PATCH-004-five-star-axis.md`, `docs/DECISIONS.md` | absent |
| a driver action catalogue | the capabilities `server/axis-driver.mjs` declares, as a document a second reader can check | nothing: it does not exist | absent — `secure-shell/packages/` holds `axis/` and `toast/` only |
| a driver receipt schema | `RECEIPT_SCHEMA` in `server/axis.mjs`, which has no second reader | `server/axis.mjs` | absent |

The last two are this driver's own gaps rather than another project's: its capability set and its receipt
shape each have exactly one writer, which is the condition this family refuses.

Located since, 2026-11-04. The reachability enumeration found all seven on this machine, outside
both trees, so the absence above is true of the trees and false of the machine:

- `ala_civ_bots_prototype/CHECKPOINT.md` — 54,028 bytes, 2026-11-02
- `agent_god_files/reference/AXIS-MODULE.md` — 24,913 bytes, 2026-10-06
- `dl-enclave/docs/DRIFT.md` — 25,560 bytes, 2026-10-30
- `dl-enclave/docs/CLIENT-UI.md` — 45,827 bytes, 2026-10-30
- `shploingus-game/references/Docs-A/tiket-ledger-reference/income-engine/cua_worker.py` — 28,161 bytes, 2026-09-18
- `shploingus-clean/crates/voxel-model/src/proof.rs` — 4,681 bytes, 2026-10-14
- `shploingus-clean/crates/voxel-package/src/civilians.rs` — 33,514 bytes, 2026-10-25

The table keeps its scoped claim; this line records where the documents actually are. All seven
were then read in full; §11.4–§11.9 record what each specifies against the driver, quote by quote.
