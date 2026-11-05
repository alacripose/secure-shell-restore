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
| Six-star aggregation (CGA-44) | `server/stars.mjs`: six top-level stars, each with an owner and a requirement vector citing the nine typed ladders; `AXIS_COUNT = 9` is guarded (`star-axis-count-rewritten`), and a bare token, a ladder offered as a star verdict, or a request for one score are each refused by name | HELD |
| Client window, taskbar, delegation chat | `client/index.html` served by the axis at `/`: the taskbar read 3 drivers, 1 ticket, 3 cellframes; the console printed `ticket aria-node:ticket:1 for witness`; the delegation box POSTed `/api/axis/tickets` and showed the ticket the axis issued | HELD |
| Physical outcome verification (CGA-14, CGA-28) | Verified through a **live Minecraft 1.20.1 server** (port 25566): a mineflayer body (`AxisBody`, server entity id 1) acts by ordinary player input, and `minecraft-live` reports a digest of the state the server sent it. A move changed it `sha256:fc7cfa24…` → `sha256:0ee6c3f5…` (1.91 blocks walked), a dig changed it `sha256:0ee6c3f5…` → `sha256:f49ceb59…` (grass at `6,-61,-3` now air per the server's block update); the axis recorded the adapter's digest (`source: adapter`) and `civ-0000:ticket:1` verified against it. Also held against the game's own `shploingus-voxel-world` substrate crate (`sha256:4677a45c…`). A frame with no observation is still refused `world-not-verified`, an unregistered adapter `world-adapter-unknown`, and a client claim has nothing to cite | HELD |

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
