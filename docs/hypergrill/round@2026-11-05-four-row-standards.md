# Round: what the four rows must observe, 2026-11-05 (second round)

One theme: the four `NOT-ENFORCED` rows are built, and the first round of this date held three of them
short of `HELD`. This round fixes the *standard* each one must meet — not whether the code exists, but
what an observation has to show before the row may be called met. Four questions, asked once, answered
once. No round-end options were offered.

Source class of every answer below: `user`. The questions and the pre-search are `planner`.

## What the search settled before the questions

The first round (`round@2026-11-05-four-rows.md`, R1–R6) answered whether the rows are built and which
report is the record. None of those six is asked again. The residue this round is the *shape of the
proof*, and each question below survived a search that could have closed it:

| Finding | Evidence |
|---|---|
| The frame keeps a bounded lineage and the axis refuses a stale citation | `secure-shell/server/cellframe.mjs:153`, `:187` push `stateDigest` on open and tick; `:235` refuses `cellframe-digest` with both digests named; `axis-server.mjs:131` verifies a cited frame before the act |
| The reading an agent may cite is its own state at its own generation | `cellframe.mjs:192` `feel()` returns `civilian.cellframe-reading/1` with `driver`, `generation`, `digest`, `density`, `budgetLeft` |
| The scale run reads once, then acts on that same reading | `secure-shell/tools/axis-scale.mjs`, `one()`: `tickAndRead()` then `actLocally()`/`actThroughGame()` — no tick between them, so no lineage step exists yet |
| Two digests, two authors, already kept apart | `server/world.mjs:95` the axis's `stateDigest` over `{adapter, version, action, state}`; `:113` `source: adapter` when the adapter declares its own; `:177` the record carries `digest` and `stateDigest` side by side |
| The two aggregates are separate documents | `civilian.axis-cells/1` (`server/axispackage.mjs`) and `civilian.cellframe-reading/1` (`cellframe.mjs:192`); the acceptance text at `cellular_…_rechecked.md:1405` forbids presenting the first as CA state |
| Scope is a wall today, not a gate | `server/learn.mjs:89-91` `setScope()` throws `learn-scope-fixed` unconditionally; `tools/axis-learn.mjs` plants it (`learn-scope-fixed: refusedAs(() => plant.setScope({scope: "kernel"}))`) and the report cites it at `:203` and `:233` as proof the gate holds |
| The physical run is recorded, and its body is named | `tickets/TICKET-0015-…md:19,24`: flat world in `run/live-mc`, port 25566, body `AxisBody` at server entity id 1; digests `fc7cfa24…` → `0ee6c3f5…` → `f49ceb59…` |
| The requirement texts | `cellular_…_rechecked.md:1253` (`CGA-38`), `:1405` (`CGA-45`), `:1040` (`CGA-28`), `:708` (`CGA-14`) |

## Questions and answers

### S1 — what makes a fresh run fresh

**Asked.** R5 asked for "a fresh run — new world, new body, no reuse of the old digests" but did not say
what makes a run fresh. `TICKET-0015` ran a flat 1.20.1 world in `run/live-mc` on port 25566 with a
mineflayer body `AxisBody` at entity id 1. Five conditions were offered — a differing level/seed declared
in the record; a body identity that is not `AxisBody` entity id 1; an assertion that no digest equals the
three recorded ones; a fresh axis process at zero; the server's own log line captured — and the owner was
asked to choose every one that is required.

**Answered (verbatim).** "A body identity that is not `AxisBody` entity id 1 — new name and new UUID, so
the entity id cannot be inherited"

One condition was ticked of five. The other four are recorded as offered and not required; they are not
silently treated as met.

### S2 — what proves the frame moved and the act differed because it moved

**Asked.** `cellframe.mjs` keeps a bounded lineage and the axis refuses an act citing a frame that moved
(`cellframe-digest`); `axis-scale.mjs` currently reads once, then acts on that same reading. Four
standards were offered: paired arms from one frame; lineage proof; denial proof through the stale
citation; world-outcome proof.

**Answered (verbatim).** "Lineage proof: the act's cited digest is the immediate successor of the read
digest in the frame's own lineage, and the action chosen differs from what the reading's rule would have
chosen at the earlier generation"

### S3 — how the two aggregates live in one artefact

**Asked.** R3 asked for "a receipt that carries both, side by side, with the cellframe reading in its own
field". `civilian.axis-cells/1` aggregates decisions; `civilian.cellframe-reading/1` is a separate
document. Three shapes were offered: sibling fields under one digest; two documents cross-citing each
other; a nested `cellframe` object with the aggregate as a row inside it.

**Answered (verbatim).** "One receipt document where `cellframe` is a nested object carrying its schema,
driver, generation and digest, and the aggregate is a row inside it"

### S4 — the scope refusal

**Asked.** R4 requires that drivers set their own scope; `learn.mjs:89-91` always throws
`learn-scope-fixed` ("scope is declared on the ticket, never by the learner"), and `axis-learn.mjs` cites
that throw as proof the gate holds. Two ways to reconcile them were offered, plus reading R4 as autonomy
inside a fixed scope.

**Answered (verbatim).** "`learn-scope-fixed` becomes a bounded refusal: a driver may propose a scope
change, and it is refused unless it cites evidence the axis verified — refusal stays, but as a gate rather
than a wall"

## State table

| # | Question | State |
|---|---|---|
| S1 | what makes a fresh run fresh | answered |
| S2 | what proves the frame moved and the act differed because it moved | answered |
| S3 | how the two aggregates live in one artefact | answered |
| S4 | the scope refusal | answered |

Asked 4, answered 4, open 0, struck 0, superseded 0. Remaining: 0 in this round. Round `R1`–`R6` of the
same date remains answered and is not reopened.

## What the answers change about rows marked `HELD` or `absent`

None of these promotes a row. Each fixes the measurement a later unit must produce.

| Row | Was | Now |
|---|---|---|
| `CGA-38` | `absent` — needs a run where the frame moves between reading and act (`R2`) | **Standard fixed.** The act's cited digest must be the immediate successor of the read digest in the frame's lineage, and the chosen action must differ from what the reading's rule would have chosen at the earlier generation. `axis-scale.mjs` does not produce this today: `tickAndRead()` then `actLocally()` reads once and acts on it. Still `absent` |
| `CGA-45` | `absent` — needs a receipt carrying both, side by side (`R3`) | **Shape fixed.** One receipt document; `cellframe` is a nested object carrying its own schema, driver, generation and digest; the `axis-cells` aggregate is a row inside it. Still `absent` — no such document exists |
| `CGA-14`, `CGA-28` | `HELD` on the recorded run; re-proof `absent` (`R5`) | **Freshness fixed, narrowly.** The body must not be `AxisBody` entity id 1 — new name and new UUID, so the entity id cannot be inherited. The recorded run keeps its `HELD`; the re-proof is still `absent` and its digests may not be reused |
| `CGA-44`, client row | `HELD` | **Unchanged.** No answer in either round asks for more from the star receipt or the client |
| Learner (`learn-scope-fixed`) | A wall, cited as proof the gate holds (report `:203`, `:233`) | **Standard changed.** The refusal stays and becomes bounded: a proposed scope change is refused unless it cites evidence the axis verified. `learn.mjs:89-91` does not implement that yet — today it refuses every proposal — so the code and the standard disagree until the unit lands. Both report sentences stay readable and are superseded beside them |

## The tension S1 leaves open

`R5` says "new world, new body, no reuse of the old digests". `S1` requires the new body identity and was
offered — and did not require — a differing level/seed, an assertion that no digest matches the three
recorded ones, a fresh axis process, and the server's log line in the record. Those are not the same
requirement. The tension is named rather than averaged: **is a new body identity sufficient for
freshness, or must the world's level/seed differ as `R5`'s words say?** It is not resolved here, and the
queued unit must not assume either answer. The one thing both readings forbid is reuse of the three
recorded digests, which `R5` states in terms.

**Answered 2026-11-05, in this round.** The question above was put and answered: "A new body identity
is sufficient — a body that is not `AxisBody` entity id 1, with a new name and UUID, makes the run
fresh". The tension is resolved in that direction: `R5`'s "new world" is read as the world the new body
stands in, not as a requirement that the seed differ. The paragraph above stays as written so the
question and its answer can both be read.

## What this round does not decide

- It does not promote any row. All four remain `NOT-ENFORCED` / `HELD (recorded run); re-proof absent`.
- It does not decide the S1 tension above. **Superseded 2026-11-05:** the owner answered it, above —
  a new body identity is sufficient and a differing level/seed is not required.
- It does not authorise deleting the old world, the old body, the old digests or the older report text.
- It does not change `learn.mjs`; the bounded refusal is a standard for a ticket, and the plant that fires
  today fires for a different reason.
- It does not say the world-outcome or denial standards are wrong — only that the lineage standard is the
  one that counts.

## The scan file count, reconciled 2026-11-05

The previous turn recorded two different totals for the same tree and could not explain them: 55 545 files
and 4 943 refs, then 30 466 files and 2 057 refs. The explanation is in the scanner, and it means neither
number is an inventory.

`tools/scan_drives_reaudit.py` walks sixteen roots under `ROOT_BUDGET = 5.0` seconds per root and
`TOTAL_BUDGET = 195.0` seconds overall, and `walk()` breaks out of `os.walk` when either expires, setting
the root's `truncated` flag. The synthesis it writes states the rule in its own header
(`docs/secure-shell-audit/cua_driver_reaudit_synthesis.md:2`): "Per-root budget 5s, drive budget 12s,
total 195s. Each root is flushed as it completes; `truncated: yes` is a refusal, not a pass."

The two passes show the truncation directly, root by root:

| Root | 2026-11-05T00:30Z pass (133.9 s) | 2026-11-05T04:29Z pass (274.9 s) |
|---|---|---|
| `testport1` | 1 294 files, 5.2 s, `truncated: yes` | 538 files, 5.0 s, `truncated: yes` |
| `shploingus-clean` | 746 files, 5.0 s, `truncated: yes` | 420 files, 5.1 s, `truncated: yes` |
| `shploingus-game` | 3 020 files, 5.1 s, `truncated: yes` | 2 763 files, 5.0 s, `truncated: yes` |

Both passes capped digests at `MAX_DIGESTS = 900` and both wrote 900, which is why `hg_check11` (21 checks,
0 failed) accepts either state: it compares the digests that were recorded, not a file total. So `files` in
`scan_state@2026-11-04.json` is a lower bound that moves with how fast the machine walked before each root's
clock ran out — a slower pass is not a smaller family, and a larger number is not a better inventory.

Two further passes in the same turn produced **54 686 files / 4 274 refs / 138.9 s** and **77 971 files /
5 049 refs / 141.1 s**. Four passes, four totals, the same sixteen roots.

What the recorded numbers mean, stated once: all four are budgeted samples of the same roots. The committed
`scan_state@2026-11-04.json` carries whichever total the pass that wrote it happened to reach; that number is
not quoted here as a fact about the family, because the next pass will reach a different one. No row in this
round rests on a file total. Neither is quoted as the size of the family, and no
row in this round rests on a file total.

## Next units, in the order the answers force

1. **`CGA-45` receipt.** Add the nested `cellframe` object to the act receipt and assert the aggregate row
   beside it; one schema, one digest over both. `civilian.cellframe-reading/1` is embedded, not restated.
2. **`CGA-38` lineage run.** A tool that reads at generation `g`, ticks to `g+1`, and acts citing the
   successor digest, with the action compared against the rule's choice at `g`; the run fails if the cited
   digest is not the immediate successor or if the action is unchanged.
3. **`learn-scope-fixed` bounded refusal.** `setScope()` accepts a proposal carrying an axis-verified
   evidence digest, refuses one without it, and the plant is rewritten to prove the refusal fires on the
   unevidenced proposal while the evidenced one is accepted.
4. **`CGA-14`/`CGA-28` fresh run.** New body name and UUID, new world under the tension's resolution, and
   a run that reports its own digests; the old run and its digests stay recorded and unreused.
