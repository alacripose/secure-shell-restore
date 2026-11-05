# CUA axis driver training: the Debian store, end to end (2026-11-05)

Command (inside the Debian host, sealed credential decrypted for the run only):

```
systemd-creds decrypt --name=mongo-uri /etc/secure-shell/mongo-uri.cred /run/drill-mongo.uri
cd /mnt/c/Users/ala/Documents/secure_shell_v2
/opt/drill-venv/bin/python tools/cua_training.py --uri-file /run/drill-mongo.uri --documents --depth 2 --budget 90
```

Exit status read from the process: `TRAIN_OK`. Transcript `blake3:18c6607b9dd1e67ca102e746df7e46e5bf81a6096f28b6b6b44d9aaf1607980b`, 3 390 events, re-adopted by the shipped `Receiver` (`adoptions: 1`, state `held`, exit 0). The same run is corroborated in `reports/cua-training/2026-11-05-training-uncapped.md`; the numbers below are read from `reports/cua-training/train-docs.ndjson` and `reports/cua-training/exclusions.json`, not restated from a summary.

## The corpus as it stands

| Item | Count |
|---|---|
| Documents admitted | 3 264 |
| Project bundles (one per audit row) | 55 |
| Learning-apply tickets | 3 321 |
| Matching receipts | 3 321 |
| of which document and bundle tickets | 3 319 (3 264 + 55) |
| of which witness and kernel tickets | 2 |
| Duplicate admissions | 0 |
| Excluded documents | 3 (named below) |
| Projects discovered / contributing documents | 67 / 62 |

Selection rules, as they now stand: root `.md` and `.txt`, `docs/**`, `tickets/**`, `patches/**`, and `.agents/skills/**/SKILL.md`. Vendored trees — `references/`, `node_modules/`, `target/`, `build/`, `generated/`, `.cache/`, `.git/` — are skipped by rule (64 directories across the corpus) because they hold copies of other projects, not this project's expectations. There is no per-project cap and no bundle ceiling: the largest corpora are admitted whole, `shploingus` 1 154 documents, `planet-shploingus` 710, `shploingus-clean` 601, `testport1` 128.

Revisions are deduplicated deliberately, by relative path and content digest, so two copies of one file are two documents and a changed document is a new identity beside the old one; hence zero duplicate admissions while the CGA contract appears under two paths.

## Every exclusion, named

Three documents are not admitted, for one deterministic reason: the axis accepts a request body of at most 1 000 000 bytes (`server/axis-server.mjs`), and these encoded bundles exceed it.

| Project | Document | Encoded bundle bytes |
|---|---|---|
| `shploingus` | `docs/design_reference/GOD_AGENTS.md` | 2 815 216 |
| `shploingus` | `docs/original_reference/GOD_AGENTS.md` | 2 826 918 |
| `shploingus-clean` | `docs/LEDGER.md` | 1 048 524 |

A limit is not a cap: the bound is the axis's own body maximum, each skipped document is named with its size, and learning them needs the axis to accept a multi-part bundle — a contract change with its own ticket.

## Projects that carry no expectation documents

Five discovered projects contributed no document at all: `DenseOres`, `Ecologics`, `MineFactoryReloaded`, `SeedDelight`, `optical`. Each is a Minecraft mod source clone with no `AGENTS.md`, no `docs/` and no tickets, so there is nothing in it to learn from beyond its audit row.

## The expectation contract

The CGA civilian acceptance contract is in the learned set, twice, because `testport1` carries it at two paths, and each copy was applied under its own ticket:

- `secure-shell.training.docs/testport1-docs-cellular-generativity-axis--37a681f1b0@a0b10dc468719c38`
- `secure-shell.training.docs/testport1-docs-cellular-generativity-axis--877a73489e@a61b512143291176`

## Checks

| Check | Evidence | State |
|---|---|---|
| Driver registers and attests | `/api/axis/state` names `project-corpus-driver`, `trusted: true`, capabilities `witness, learning-apply, kernel` | PASS |
| Corpus is the folder audit | `docs/secure-shell-audit/resynth_audit@2026-11-04.json`, 55 rows, written by `tools/resynth_agents.py --report` | PASS |
| Project bundles reach the Mongo authority | one bundle per audit row, digest computed by `impl.packages.mongo_store.admit` | PASS |
| Every qualifying document is learned from | 3 264 documents from 62 projects, each applied under its own `learning-apply` ticket | PASS |
| Every item is ticketed before it is applied | tickets = receipts = 3 321; 3 319 item tickets plus the witness and kernel tickets | PASS |
| No silent cap remains | largest corpora admitted whole (1 154 / 710 / 601 documents); every exclusion named above | PASS |
| The expectation contract is in the corpus | both CGA identities above | PASS |
| Corpus witnessed | `witness` receipt over `sha256` of the audit file | PASS |
| Kernel scope is declared, not assumed | `kernel` act accepted with `scope: kernel` under a driver that declares `kernel` | PASS |
| The transcript adopts | `python -m impl.packages.toolstream verify`: `adoptions: 1`, state `held`, exit 0 | PASS |
| Cellular substrate (CGA-38, CGA-45) | `server/cellframe.mjs`: per-driver ownership, declared neighbour radius, schedule, rule revision, lineage, resource budget and state digest; `civilian.cellframe/1` is a separate schema from `civilian.axis-cells/1`. 1 000 frames opened in `tools/axis-scale.mjs`; the reading chose the action (960 sparse frames witnessed, 40 dense frames acted), and a decision citing a moved frame was refused `cellframe-digest` | HELD |
| Six-star aggregation (CGA-44) | `server/stars.mjs` and `server/axis.mjs`: every act receipt names all six stars, each with its owner, its own lens and its own presenter, and a star is held only on a verified record whose `stateDigest` the axis recomputed itself; a star with no presenter, no lens or no such record leaves a `secure-shell.axis-refusal/1` row. Measured by `tools/axis-stars.mjs`: 1 000 drivers, 500 presenting six stars, 500 control, 500/500 held on every star, control held 0 and refused `star-unverified` (`secure-shell` 20b3c31) | HELD |
| Client window, taskbar, delegation chat | `client/index.html` served by the axis at `/`: the taskbar read 3 drivers, 1 ticket, 3 cellframes; the console printed `ticket aria-node:ticket:1 for witness`; the delegation box POSTed `/api/axis/tickets` and showed the ticket the axis issued | HELD |
| Physical outcome verification (CGA-14, CGA-28) | Verified through a **live Minecraft 1.20.1 server** (port 25566): a mineflayer body (`AxisBody`, server entity id 1) acts by ordinary player input, and `minecraft-live` reports a digest of the state the server sent it. A move changed it `sha256:fc7cfa24…` → `sha256:0ee6c3f5…` (1.91 blocks walked), a dig changed it `sha256:0ee6c3f5…` → `sha256:f49ceb59…` (grass at `6,-61,-3` now air per the server's block update); the axis recorded the adapter's digest (`source: adapter`) and `civ-0000:ticket:1` verified against it. Also held against the game's own `shploingus-voxel-world` substrate crate (`sha256:4677a45c…`). A frame with no observation is still refused `world-not-verified`, an unregistered adapter `world-adapter-unknown`, and a client claim has nothing to cite | HELD |

**Superseded 2026-11-05 by the round at `docs/hypergrill/round@2026-11-05-four-rows.md`.** The rows above
stay as written. Beside them: `CGA-38` is under-evidenced — a reading that selects one action is not
influence across generations, so the missing proof is `absent` by name; `CGA-45` gains a requirement — a
receipt carrying the `axis-cells` aggregate and the cellframe reading side by side, also `absent`;
`CGA-14`/`CGA-28` keep the recorded run and lose nothing, but the fresh run the owner asked for has not
happened and is `absent`; `CGA-44` and the client row are unchanged by that round.

**Standards fixed 2026-11-05 by the second round at
`docs/hypergrill/round@2026-11-05-four-row-standards.md`.** The rows above stay as written; this block
says what each one must now observe. `CGA-38`: the act's cited digest must be the immediate successor of
the read digest in the frame's lineage, and the action must differ from what the reading's rule would
have chosen at the earlier generation — `axis-scale.mjs` reads once and acts on that reading, so the
row stays `absent`. `CGA-45`: one receipt document, `cellframe` a nested object carrying its schema,
driver, generation and digest, the `axis-cells` aggregate a row inside it — still `absent`. `CGA-14` /
`CGA-28`: the re-proof needs a body that is not `AxisBody` entity id 1 (new name and new UUID); whether
the level/seed must also differ is a named open tension, not decided. The citation of
`learn-scope-fixed` at `:203` and `:233` stays readable, but the owner has fixed that refusal as
*bounded* — a proposed scope change is refused unless it cites evidence the axis verified — which
`server/learn.mjs:89-91` does not implement yet.


A `NOT-ENFORCED` row is `absent`, never a pass, and `PARTIAL` is not a pass either: it names which half
of the row is held and which half is still absent. This report proves that a CUA driver learned from
every qualifying expectation document every project on this machine carries, through the Debian
store, under axis tickets; that 1 000 drivers each own a cellframe whose reading chose the action
they took; that six stars are computed from nine typed ladders without being reduced to them; and
that a window with a taskbar, a console and a delegation chat served from the axis opened a real
ticket. The physical row now rests on a real server holding the world and a real client acting in it. What
it still does not prove: that the Fabric *mind* ran the body. This is a mineflayer session, not the
headless Fabric client, so the server-side decision layer, the mod's control bridge and
`tools/headlessmc` are not exercised here; the adapter is a motor, and the axis verified its
effects rather than the mind that would author them.

## The wiring that was already in the civilian project

`ala_civ_bots_prototype` had a decision format this axis never spoke, so 1 000 operable drivers
produced nothing that project's learners could ingest. The formats are now emitted, and the
vocabulary is read from that project's own published package rather than copied here.

| Wiring, and where it is owned | What the 1 000 drivers do with it |
|---|---|
| `civilian.decision/1` (`axis/DecisionPackage.java`) — artifact, digest, tick span, world, presenter, ticket, token, witness, target | every driver emits one package per act: `var/axis-packages.jsonl`, 1 000 built, **1 000 stood**, 0 refused |
| `civilian.axis-cells/1` (`axis/AxisGate.java`, batch 200 decisions / 1 200 ticks, chained by `prev`) | 5 batch records, 200 decisions each, 1 000 counted, 4/4 chain links, 9 ladders each |
| framed digest `planet-artifact-v1` (`axis/AxisProof.java`; body-side twin in `tools/residents/src/axis.mjs`) | the artifact is the decision, so re-hashing `artifact_bytes` yields the named digest; tampered bytes are `DigestMismatch` |
| nine qualified ladders (`axis/AxisVocabulary.java`; table at `tools/proofs/ingest/ledger.jsonl`) | read with `--coverage` from that package and compared value-for-value with this axis's own nine `LADDERS`; a missing package is `coverage-absent`, a disagreement `coverage-mismatch`, never a default |
| `civilian.ticket/1`, `CompletionByDeclaration` (`tools/residents/src/axis.mjs`) | a `HELD` ticket must cite an observed count: `held 40/40` reads clean, `done` is refused |
| the four damaged packages (`tools/residents/probe-axis.mjs`) | the same four plants are refused here by the same codes: `BareTokenRefused`, `AxisInterchangeRefused`, `UncheckedReading`, `DigestMismatch` |

The bridge is `server/axispackage.mjs`; the run that carries it is
`node tools/axis-scale.mjs --drivers 1000 --game http://127.0.0.1:8789 --coverage ../ala_civ_bots_prototype/tools/proofs/ingest/ledger.jsonl`,
exit 0, with the ticket's four other rows unchanged.

**Still stray, named rather than implied.** `FileMotor`'s per-frame client evidence
(`tools/residents/src/observation.mjs`: render, audio, UI rows) is not yet a driver feed, so the
client window still shows axis rows rather than what a body saw. `ExternalBrains`
(`world/ensouled/external-brains.txt`) is that project's identity rule and does not yet feed the
axis's `world-driver` refusal. `TrainingLedger.clientResult` revises a skill→verb mapping on that
side; this axis emits `verb` and `verb_basis` but holds no verb library a result could revise. And
the batch digest is this family's framed digest over its body, not `StreamLedger`'s digest of the
ledger row — two owners, not one fact written twice.

## What moved, and the command that moved it (2026-11-05)

The four rows above were `NOT-ENFORCED` earlier the same day. They moved because the substrate was
built, not because the wording was loosened. The evidence is commands, run in `../secure-shell`:

```
node --test server/test/*.test.mjs      -> 78 tests, 78 pass, 0 fail
node tools/axis-scale.mjs --drivers 1000 -> exit 0
```

`tools/axis-scale.mjs` registers 1 000 drivers on a live axis, attests each, opens a 6×6 cellframe
per driver, ticks it, reads it, and then lets the reading decide the action: 960 frames were sparse
and only witnessed their own state, 40 were dense and were ticketed to act on the world through the
`loopback-world` adapter. Tickets 1 001, receipts 1 000 — the extra ticket is the deliberately stale
citation, which is refused `cellframe-digest` and correctly leaves no receipt. The other refusals
that fired: `cellframe-owner` (one driver ticking another's cells), `world-not-verified` (a frame
citing an observation nobody recorded), `world-adapter-unknown`.

The client surface was checked in the browser panel, not inferred from the file: the taskbar read
3 drivers / 1 ticket / 3 cellframes, and typing `aria-node witness` into the delegation box produced
`aria-node:ticket:1 · witness` in the chat, `ticket aria-node:ticket:1 for witness` in the console,
and a `POST /api/axis/tickets → 200` on the wire.

The physical row moved through the game itself, not through another adapter of ours.
`tools/game-adapter` is a small Rust crate that links `shploingus-voxel-world` — the game's own
substrate, at the workspace version — and serves the field the body stands in. Its identity is the
crate's `FieldSampleSet::identity()`, so the evidence digest is computed by game code, recorded by
the axis with `source: adapter`, and cited by the frame; the axis keeps its own hash beside it for
integrity rather than substituting it. In the 1 000-driver run, 40 loopback frames and one game
frame were verified (`verified: 41`), the game frame citing `sha256:4677a45c…` after the body moved
to `(12, 0, 0)`; the digest changed with the position, which is the outcome being observed rather
than an animation being reported.

**Superseded the same day — a live server now runs.** The gap named above was a server, a JVM and a
body; all three were already on this machine in `ala_civ_bots_prototype` (the 1.20.1 server jar
fabric-loom had cached, JDK 21, and `tools/residents`' mineflayer 4.39), so the adapter was built
against them rather than against another model of a world:

- `tools/residents/world-adapter.mjs` logs in as an ordinary player (`AxisBody`) and serves
  `/version`, `/state` and `POST /act`; its digest is a sha256 over the position and the 245 blocks
  the server sent it, so an unloaded cell reads `unloaded` and is never guessed;
- `move` walks through the pathfinder and refuses `world-not-moved` if the body stayed put; `dig`
  re-reads the block and refuses `world-not-dug` unless the server's update made it air;
- `axis-scale.mjs` now acts from the position the world reports (`/state` then a target two blocks
  on) instead of a coordinate the script invented, and refuses a run whose digest did not change.

Measured on the running server, then in the scale run:

## Historical: the capped run of the same day (superseded)

Kept as written, because the cap these numbers record is exactly what the current run removed. The
first run of 2026-11-05 selected documents only from `AGENTS.md`, `VOWS.md`, `CHECKPOINT.md`,
`CONTEXT.md`, `docs/**` and `tickets/**`, with a per-project limit of 24 documents and a corpus
ceiling of 400 bundles.

Command:

```
/opt/drill-venv/bin/python tools/cua_training.py --uri-file /run/drill-mongo.uri --documents
```

Exit status read from the process: `TRAIN_OK`; transcript `blake3:13a422fd2a0c7e391f7225933abd71dd904dca43ecf0ec1e57990ea8df7bb8f0` with 427 events, adopted by the shipped `Receiver` with exit 0.

| Check | Evidence | State |
|---|---|---|
| Project documents are learned from | 368 documents from 24 projects, each applied under its own ticket | PASS |
| The expectation contract is in the corpus | `secure-shell.training.docs/testport1-docs-cellular-generativity-axis-civilian@fd6644ef` | PASS |

Those 368 documents and 425 tickets were true of that run. They are superseded by the 3 264
documents and 3 321 tickets above; see `reports/cua-training/2026-11-05-training-uncapped.md` for the
run that replaced them.

## The driver learns from an outcome it did not author

The four rows above are `HELD` on work a driver performed. What they did not show is the last clause
of the mission: that a driver's *next* choice is decided by what the world said about the last one.

`secure-shell` `43a997b` closes that, in the terms the acceptance document already set. A reward is
only accepted from a verified record carrying both the adapter's digest and the axis's own hash of the
state it read (`E6`, and `E11`'s refusal to collapse "not read" into empty); the act receipt names its
presenter and carries `expected`/`observed` (`E5`, `E7`); a digest mismatch leaves a
`secure-shell.axis-refusal/1` row, not a string in a response body (`E8`); and a learner that tries to
set its own scope is refused `learn-scope-fixed` (`E3`).

Measured, not asserted: `node tools/axis-learn.mjs` → exit 0, **1 000 drivers, 500 rewarded from a
verified observation and 500 control**. Every driver is asked the same probe, whose own reading rule
says `witness`. The rewarded half answers `move` — 500/500 — and the control answers `witness` —
500/500. 500 receipts, 0 refusals, and the three plants refused `learn-no-evidence`,
`learn-unverified-action`, `learn-scope-fixed`. `node --test server/test/*.test.mjs` → 96 tests, 96
pass, 0 fail.

The three files that made this possible were untracked until now: `server/axis.mjs`,
`server/axis-driver.mjs` and their suites were written in earlier passes and never committed, so the
axis runtime a reader needs in order to check any of the four rows above was outside the repository.
They are in `43a997b` with the rest.

## The six stars the axis can defend

CGA-44 asked that six stars be named and that the six stay six. `secure-shell` 20b3c31 makes the axis
answer it on every receipt rather than in a table a reader has to trust.

Each receipt carries `starCount` and all six stars — `presence`, `craft`, `evidence`, `standing`,
`conduct`, `continuity` — each with its owner, its own lens (`civilians.laya`, `material_grade`,
`proof-of-work`, `grade`, `civilians.von`, `evidence_grade`) and its own presenter. A star is `held`
only when it cites a record the axis verified, and only on that record's `stateDigest` — the hash the
axis computed itself, not the adapter's identity of it. A star offered with no presenter, no lens, or
no such record is refused as a `secure-shell.axis-refusal/1` row naming `refusedBy`, the presenter and
one recovery line; a star nobody offered is `absent`, never a quiet `false`.

Measured, not asserted: `node tools/axis-stars.mjs` → exit 0, **1 000 drivers, 500 presenting six
stars and 500 control**. Every starred receipt names six stars (500/500), each star is held exactly
500 times, the control half presents nothing it did not earn (`control_held` 0) and is refused
`star-unverified` 500 times, and the learner's own refusals (`learn-no-evidence`,
`learn-scope-fixed`) still fire — a six-star presentation is not a way to reward an unverified action.
`node --test server/test/*.test.mjs` → 101 tests, 101 pass, 0 fail.

The other five rows cannot leave `NOT-ENFORCED` in this pass, and the reason is not effort:
`client_witness` and `client_run_h9` need a mounted client window and a human report; 
`source_access_isolation` needs filesystem/workspace isolation outside the repository;
`alternate_surface_or_runtime` needs a client crate that does not exist; `branch_and_pr_review` needs a
configured remote and a human review record. `CGA-38` and `CGA-45` **are** built — `secure-shell`
`server/cellframe.mjs` and `server/axis-server.mjs` — and the round of 2026-11-05 holds their evidence
short of `HELD`: `CGA-38` needs the frame to move between the reading and the act, and `CGA-45` needs a
receipt carrying the aggregate and the cellframe reading side by side
(`docs/hypergrill/round@2026-11-05-four-rows.md`). `CGA-14`/`CGA-28` remain `HELD` on a recorded live run,
and the owner has asked for a fresh run whose digests do not reuse the old ones; that run has not
happened, so it is `absent`, not passed.
