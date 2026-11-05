# TICKET-0013 — the four substrates, and the client window the absence claim outlived

Status: done (2026-11-05). Two repositories: `secure-shell` (the build) and this one (the record).

## Why this is a ticket and not a drive-by

AGENTS §6: a contract change needs a ticket first. This changes two contracts:

1. `reports/cua-training/2026-11-05-driven-training.md` carried four `NOT-ENFORCED` rows. They are
   lowered to `HELD` (three) and `PARTIAL` (one), which changes the report's verdict, not its wording.
2. `.cache/hg_check7.py` asserted "the client/ directory is still empty (absence is real)". That
   assertion was true on 2026-11-04 and is false now, because the client window was built. A check
   that encodes a stale absence fails for the right reason, so the check is corrected beside a dated
   supersession in the architecture document rather than deleted or weakened.

## What was built (`secure-shell` @ `94b14b1`)

| Row | Module | What it refuses |
|---|---|---|
| CGA-38, CGA-45 | `server/cellframe.mjs` | `cellframe-owner` (one civilian ticking another's cells), `cellframe-schedule`, `cellframe-budget`, `cellframe-rule`, `cellframe-inputs`, `cellframe-digest`; `civilian.cellframe/1` is separate from `civilian.axis-cells/1` |
| CGA-44 | `server/stars.mjs` | `star-bare-token`, `star-ladder-mismatch`, `star-token-unknown`, `star-ladder-collapsed`, `star-axis-count-rewritten`, `star-reduced-to-score` |
| CGA-14, CGA-28 | `server/world.mjs` | `world-evidence-absent`, `world-not-verified`, `world-stale`, `world-adapter-unknown`, `world-version`, `world-result`, `world-frame-capability` |
| client window, taskbar, delegation chat | `client/index.html` | a delegation that cannot open a ticket shows the refusal code, never a success line |

The axis edge gained the routes these need (`server/axis-server.mjs`), and an act may cite a
cellframe reading, which the axis checks before recording the act.

## Evidence, commands and exit statuses

```
node --test server/test/*.test.mjs          -> 78 tests, 78 pass, 0 fail
node tools/axis-scale.mjs --drivers 1000    -> exit 0
```

`tools/axis-scale.mjs` on 2026-11-05: 1 000 drivers, 1 000 cellframes, 1 000 ticks, the reading
choosing 960 witness and 40 world acts, 1 000 receipts, tickets 1 001 (the extra one is the
deliberately stale citation, refused `cellframe-digest`, which correctly leaves no receipt), and four
refusals firing: `cellframe-owner`, `world-not-verified`, `world-adapter-unknown`, `cellframe-digest`.

Client surface, checked in the browser panel rather than read from the file: taskbar `3 drivers`,
`1 ticket`, `3 cellframes`; typing `aria-node witness` produced `aria-node:ticket:1 · witness` in the
chat, `ticket aria-node:ticket:1 for witness` in the console, and `POST /api/axis/tickets → 200`.

## Superseded in part, the same day

The `PARTIAL` verdict in this ticket's table was true when it was written and is not true now:
`TICKET-0014` built `tools/game-adapter` against the game's own `shploingus-voxel-world` crate and
the row is now `HELD`. This paragraph stays readable rather than being edited away.

## What this ticket does not claim

Physical outcome verification stays `PARTIAL`. The frame protocol is enforced and `loopback-world` is
a genuine observing adapter, but no game server has registered as an adapter, so no physical body was
acted on and no physical outcome was verified against a world this build did not write. The report
keeps that half absent rather than folding it into the row's PASS.
