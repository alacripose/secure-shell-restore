# TICKET-0018 — six stars on every receipt, from a state the axis recomputed

**Status:** `review` — implementation and measurement landed; acceptance is the run below.
**Commit:** `secure-shell` `20b3c31` (four files, well under the 40-file unit budget)
**Record:** `docs/hypergrill/handoff@2026-11-04.jsonl`, `unit: TICKET-0018` (appended by this unit)

## Contract (seven fields)

| Field | Value |
|---|---|
| MISSION | CGA-44 stops being `NOT-ENFORCED`: `secure-shell.axis/1` names all six stars on every act receipt, each defended by a presenter, its own lens, and a state digest the axis computed itself. |
| SCOPE | `server/stars.mjs`, `server/axis.mjs`, `server/test/star-receipt.test.mjs`, `tools/axis-stars.mjs`. No client surface, no taskbar, no delegation chat, no physical row work. |
| CONSTRAINTS | `DECISIONS.md`'s six-star rule, each star carrying a lens and a proof with a presenter, never a nonce; acceptance E5–E11 (presenter named, expected/observed from the world, digest recomputed, read/absent/refused never collapsed, refusals recorded as rows); the existing `learn.mjs` refusals must keep firing. |
| RESOURCES | One Node process, no network, no model call, no external service. |
| EVIDENCE | `node --test server/test/*.test.mjs` → 101 tests, 101 pass, 0 fail, exit 0. `node tools/axis-stars.mjs` → exit 0: 1 000 drivers, 500 presenting six stars, 500 control, `named_six` 500, every star held 500 times, `control_held` 0, 500 `star-unverified` refusal rows, learner plants still refusing. |
| DELIVERABLE | The commit above, this ticket, the report section, and `secure-shell/var/axis-stars.json`. |
| STOP | Stop at any star that cannot be defended. No star from an adapter digest alone, no quiet `false`, no reward through a star. |

## The plan, as written before the first edit

1. Read `server/stars.mjs`, `server/axis.mjs` and the receipt it already emits; extend, do not parallel.
2. Give each of the six stars a lens drawn from the family's own list in `DECISIONS.md` (laya/von, the
   material ladder, the ticking proof, `grade`, `evidence_grade`), so six stars carry six lenses.
3. Wire the axis to the world's verified register (`createAxis({ world })`), so `starRows` can require
   `record.observed.stateDigest` — the hash the axis computed — and never the adapter's `digest`.
4. Refuse `star-unknown`, `star-no-presenter`, `star-no-lens`, `star-unverified` as
   `secure-shell.axis-refusal/1` rows with `refusedBy`, presenter and a recovery line.
5. Measure it with a 1 000-driver tool shaped like `axis-learn.mjs`: rewarded half presents six stars,
   control presents one it did not earn; print per-star counts and refusal counts; exit non-zero on any
   unearned presentation.
6. Record here, update the acceptance row, run the workspace gates, commit, push, read CI from the run.

## Why the other rows stay where they are

`client_witness`, `client_run_h9` (a human at a mounted window), `source_access_isolation` (filesystem
isolation outside this repository), `alternate_surface_or_runtime` (no client crate), and
`branch_and_pr_review` (a configured remote plus a human review record) are not decidable from this
tree. `CGA-38`/`CGA-45` would need a cellular substrate that is not built here, and holding them on the
cellframe runtime would be a different row's evidence. `CGA-14`/`CGA-28` were held on the live-server
run recorded in this report; this pass re-proves nothing about them and does not claim to.

## Ledger note

This workspace has no `LEDGER-####` ledger of its own: the only such ids on disk belong to
`testport1`'s ledger, quoted inside `docs/secure-shell-audit/testport1_plan_resynthesis.md`. Copying one
of those here would attribute this unit to another project's record, so the unit record is the handoff
row appended above, and no ledger id is invented.
