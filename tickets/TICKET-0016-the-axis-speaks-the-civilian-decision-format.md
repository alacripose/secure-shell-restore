# TICKET-0016 — the 1 000 drivers now emit the civilian decision package

Status: done (2026-11-05).

## Why this is a ticket

Until this change the axis had its own vocabulary — drivers, tickets, receipts, cellframes, stars —
and the civilian project had a different one: `civilian.decision/1`, `civilian.axis-cells/1`,
`civilian.ticket/1`, nine qualified ladders and a framed digest. Both were enforced, neither was
connected, so 1 000 operable drivers produced nothing a learner in `ala_civ_bots_prototype` could
ingest, and the axis's nine ladders and that project's nine ladders were two tables that happened to
agree with no check saying so. This ticket records the format bridge and its refusals.

## What was read, and what it owns

| Wiring | Owner | What it states |
|---|---|---|
| `src/main/java/dev/ensouled/axis/DecisionPackage.java` | civilian project | `civilian.decision/1`: artifact, digest, tick span, world, presenter, ticket, token, witness, target |
| `src/main/java/dev/ensouled/axis/AxisGate.java` | civilian project | `civilian.axis-cells/1`, batch 200 decisions / 1 200 ticks, chained by `prev` |
| `src/main/java/dev/ensouled/axis/AxisProof.java` | civilian project | `planet-artifact-v1 ‖ u16 schema ‖ u64 length ‖ payload` |
| `src/main/java/dev/ensouled/axis/AxisVocabulary.java` | civilian project | the nine ladders and their members |
| `tools/residents/src/axis.mjs` | civilian project | the body-side reader and its refusal codes |
| `server/stars.mjs` | this axis | the same nine ladders, and six stars over them |
| `server/axispackage.mjs` | **this ticket** | the bridge: build and read both packages, with those codes |

## What changed

`server/axispackage.mjs` builds `civilian.decision/1` exactly as `DecisionPackage.of` does (the
artifact is the decision, so re-hashing `artifact_bytes` yields `artifact_digest`), builds and reads
`civilian.axis-cells/1` batch records, and reads `civilian.ticket/1`. It refuses, by name:
`FormatRefused`, `BareTokenRefused`, `AxisInterchangeRefused`, `UncoveredAxis`,
`UncheckedReading`, `DigestMismatch`, `TicketStateRefused`, `CellBudgetRefused`,
`CompletionByDeclaration`, and — on the batch record — `AxisCountRefused`, `CoverageIncomplete`,
`TokenCountRefused`.

`tools/axis-scale.mjs` now takes `--coverage <ledger>` and reads the ladder vocabulary out of the
civilian project's own published package. With no package the run stops `coverage-absent` rather
than falling back to a table this repository would then own twice; with a package it refuses
`coverage-mismatch` unless that table is value-for-value the axis's nine `LADDERS`.

## Evidence

```
node --test server/test/*.test.mjs                    -> 87 tests, 87 pass, 0 fail
node tools/axis-scale.mjs --drivers 1000 --game http://127.0.0.1:8789 \
     --coverage ../ala_civ_bots_prototype/tools/proofs/ingest/ledger.jsonl   -> exit 0
```

The run: 1 000 drivers, 1 000 packages built, **1 000 stood**, 0 refused; five batch packages of 200
decisions, chained (4/4 links), nine ladders each, 1 000 decisions counted, no batch refusals; the
ticket probe (`HELD`, `held 40/40`) reads clean; and the four plants are refused by the codes the
civilian probe plants: `BareTokenRefused`, `AxisInterchangeRefused`, `UncheckedReading`,
`DigestMismatch`. The 1 000 frame receipts, 41 verified world acts and four axis refusals are
unchanged from the previous run.

Artifacts: `var/axis-packages.jsonl` (1 000 decision packages), `var/axis-cell-packages.jsonl`
(5 batch packages), `var/scale-wiring.json` (the summary above).

## Named, not done

- `FileMotor`'s per-frame client evidence (`tools/residents/src/observation.mjs`, render/audio/UI) is
  not yet a driver feed, so the client window still shows axis rows rather than what a body saw.
- `ExternalBrains` (`world/ensouled/external-brains.txt`) is the civilian project's identity rule; the
  axis's `world-driver` refusal is not yet fed from it.
- `TrainingLedger.clientResult` teaches a skill→verb mapping on that side; this axis emits
  `verb`/`verb_basis` but does not yet hold a verb library that a result can revise.
- The batch package's digest is this family's framed digest over its body; the civilian ledger row's
  digest is `StreamLedger`'s over the row. They are different owners and this module does not claim
  to reproduce the second.
