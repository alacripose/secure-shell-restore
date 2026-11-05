# TICKET-0017 — the driver learns from an outcome the axis verified

**Status:** `review` (implementation landed; acceptance is the run recorded here)
**Branch:** `main` in `secure-shell` (the change is nine files, under the 40-file unit rule)
**Commit:** `secure-shell` `43a997b`
**Approved by:** the owner, 2026-11-05, on the written build plan required by `VOWS.md` v6–v7

## Contract (seven fields)

| Field | Value |
|---|---|
| MISSION | A driver's next choice is decided by a world observation the axis verified itself, rather than by the harness script or the driver's own report. |
| SCOPE | `server/axis.mjs` receipt and refusal rows; `server/world.mjs` verified record; `server/learn.mjs`; `tools/axis-learn.mjs`; three test files. No other project's authority is touched. |
| CONSTRAINTS | Acceptance E5, E6, E7, E11 (`SECURE-SHELL-RESTORE@1.CUA-CIVILIAN-ACCEPTANCE.md` §11.10): expected/observed from the world, digest recomputed by the axis, presenter named, read/absent/refused never collapsed. E3: scope is declared on the ticket, never by the learner. Plan §7: one unit, ≤40 files, refusals as rows. |
| RESOURCES | One process, no network, no external service, no model call. |
| EVIDENCE | `node --test server/test/*.test.mjs` → 96 tests, 96 pass, 0 fail, exit 0. `node tools/axis-learn.mjs` → exit 0, 1 000 drivers, 500 rewarded, 500 control, `followed_own_reward` 500, `control_kept_reading` 500, 500 receipts, 0 refusals, and the three plant refusals `learn-no-evidence`, `learn-unverified-action`, `learn-scope-fixed` all firing. |
| DELIVERABLE | The commit above, this ticket, and `var/axis-learn.json`. |
| STOP | Stop at any refusal the learner cannot honestly satisfy. No reward from one digest, no self-granted scope, no claim that the control proves more than that it did not move. |

## What changed

- **`server/axis.mjs`.** The act receipt answers `digestState` as `read` (the axis recomputed the
  digest from bytes it was handed), `absent` (a digest nobody handed bytes for), or a `digest-mismatch`
  refusal that leaves a `secure-shell.axis-refusal/1` row naming `refusedBy`, the action, the presenter
  and one recovery line. The receipt carries `presenter`, `expected`, `observed` and `recomputed`.
- **`server/world.mjs`.** A verified record now carries the axis's own `stateDigest` beside the
  adapter's `digest`, and the `expected` the frame declared.
- **`server/learn.mjs`.** `createLearner` ranks the actions its ticket allows; `reward()` requires a
  verified record with **both** digests, matching the action; `setScope()` always refuses
  `learn-scope-fixed`.
- **`tools/axis-learn.mjs`.** 1 000 drivers: the even half acts in the world and is rewarded from the
  record, the odd half is the control. Every driver is then asked the same probe, whose own reading
  rule says `witness`; the rewarded half answers `move`, the control answers `witness`.

## What this does not claim

- Not that a driver has a mind: the weights are three numbers over two actions, and the autonomy claim
  is that a recorded outcome, not the script, decides the next choice.
- Not that a client witnessed anything: `client_witness` and `client_run_h9` remain `NOT-ENFORCED`
  with their owners (`shell/test harness`, `user`).
- `digestState` is `absent` on acts that cite an observation digest without handing bytes over — which
  is what a `world-act` does by construction. That is the honest answer, not a missing feature.

## Note on the ledger id

Plan §7 asks the commit subject to begin with a ticket id and a ledger entry id. The subject carries
`TICKET-0017`; the ledger id is **not invented** here, and this row is the record the commit points
at. Inventing a number to satisfy the shape would be the failure that rule exists to prevent.
