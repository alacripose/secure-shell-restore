# Round: the four CGA rows, 2026-11-05

One theme: what each of the four rows — cellular substrate (`CGA-38`, `CGA-45`), six stars (`CGA-44`),
client surface, physical outcome (`CGA-14`, `CGA-28`) — may assert, and which file is allowed to say it.
Six questions, asked once, answered once. No round-end options were offered.

Source class of every answer below: `user`. The questions and the pre-search are `planner`.

## What the search settled before the questions

The questions are the residue. Four things were answered by reading the family, and are not asked:

| Finding | Evidence |
|---|---|
| The cellular substrate is built, not missing | `secure-shell/server/cellframe.mjs`, 245 lines: per-driver frame, `rule-1` as a named revision, declared radius, schedule, lineage, budget, `stateDigest`; refuses `cellframe-owner`, `cellframe-rule`, `cellframe-schedule`, `cellframe-budget`, `cellframe-inputs`, `cellframe-size`, `cellframe-digest`, `cellframe-lineage` |
| The axis enforces it at act time | `secure-shell/server/axis-server.mjs:130-131` verifies a cited `cellframe{driver,digest}` before the act; `:101`, `:140`, `:144`, `:148` serve state, open, tick, feel |
| Coverage exists | `secure-shell/server/test/civilian.test.mjs` (ownership, schedule, budget, rule, digest); `tools/axis-scale.mjs` opens 1 000 frames and refuses a moved citation |
| A client surface exists | `secure-shell/client/index.html`, 136 lines: driver/ticket/receipt/cellframe pills, console, Delegation form POSTing `/api/axis/tickets` |
| The two reports disagree | `reports/cua-training/2026-11-05-driven-training.md:68-71` = `HELD`; `reports/cua-training/2026-11-05-training-uncapped.md:65-68` = `NOT-ENFORCED`; and the driven file's own prose at `:233` still says the substrate "is not built here" |
| The requirement texts | `docs/secure-shell-audit/cellular_generativity_axis_civilian_expectations_prototype_rechecked.md:1253` (`CGA-38`), `:1405` (`CGA-45`), `:1404` (`CGA-44`) |

## Questions and answers

### R1 — which report is the record

**Asked.** Two training reports disagree about the same four rows: `driven` says `HELD` (68–71) while
`uncapped` says `NOT-ENFORCED` (65–68), and the driven file's own closing prose (233) still says the
cellular substrate "is not built here". Which is the record?

**Answered (verbatim).** "The driven report is the record — correct the uncapped rows and the closing
prose to match what was measured"

### R2 — what `CGA-38` influence requires

**Asked.** `CGA-38` requires that "observed CA changes influence the owning agent's actual behavior".
`axis-scale.mjs` shows a reading selecting the action (sparse frame → witness, dense frame → act). Is a
reading that selects the action enough?

**Answered (verbatim).** "No — require the frame to have moved between the reading and the act, so the
influence is across generations and not one snapshot"

### R3 — what `CGA-45` still needs

**Asked.** `CGA-45` says `civilian.axis-cells/1` must stay a decision-evidence aggregate and never be
presented as CA state. Two schemas exist and are separate. What does that row still need?

**Answered (verbatim).** "A receipt that carries both, side by side, with the cellframe reading in its
own field"

### R4 — what autonomy requires

**Asked.** The drivers must be "operable and learn autonomously". Today each run is a fresh 1 000-driver
cohort with a reward gate that only accepts a record carrying both digests. What does autonomy require?

**Answered (verbatim).** "Drivers must set their own scope, not just follow an injected reward"

### R5 — whether to re-prove the physical rows

**Asked.** `CGA-14`/`CGA-28` rest on a recorded live Minecraft run; the server and adapter are stopped
because their stats files were rewritten under the digests. Should this pass re-prove them?

**Answered (verbatim).** "Re-run the live server entirely fresh — new world, new body, no reuse of the
old digests"

### R6 — reading scope

**Asked.** Which paths may be read and pinned from, given the owner's direction to refuse the
folder restriction?

**Answered (verbatim).** "The five siblings plus the two vow-bearing folders plus `AWA3D` and
`ala-system`"

## State table

| # | Question | State |
|---|---|---|
| R1 | which report is the record | answered |
| R2 | what `CGA-38` influence requires | answered |
| R3 | what `CGA-45` still needs | answered |
| R4 | what autonomy requires | answered |
| R5 | whether to re-prove the physical rows | answered |
| R6 | reading scope | answered |

Asked 6, answered 6, open 0, struck 0, superseded 0. Remaining: 0 in this round. The rows the answers
constrain are tracked below, not as open questions.

## What the answers change about rows already marked `HELD`

None of these is a new question; each is the owner applying a standard the row did not meet. The rows
stay readable and the dated line beside them says what changed.

| Row | Was | Now |
|---|---|---|
| `CGA-38` | `HELD` — reading selected the action (`axis-scale.mjs`) | **Under-evidenced by R2.** A reading that selects one action in one snapshot is not influence across generations. `absent`: a run where the frame moves between reading and act and the act differs because it moved |
| `CGA-45` | `HELD` — two separate schemas, documented | **Adds a requirement rather than weakening one.** `absent`: a receipt carrying the `axis-cells` aggregate and the cellframe reading side by side, the reading in its own field |
| `CGA-44` | `HELD` — 1 000 drivers, 500/500 per star, control 0 | **Unchanged by this round.** R4 constrains the learner's autonomy, not the star receipt |
| Client window | `HELD` — `client/index.html` served, taskbar read 3/1/3, ticket printed | **Unchanged by this round.** No answer asked for more |
| `CGA-14`, `CGA-28` | `HELD` — recorded live run, digests `fc7cfa24…` → `0ee6c3f5…` → `f49ceb59…` | **`HELD` on the recorded run, re-proof demanded by R5 and not yet run.** The fresh run is `absent`; the old run is not deleted, and its digests may not be reused |

## The named tension R4 creates

`R4` asks that drivers set their own scope. The learner refuses scope changes by name —
`learn-scope-fixed` in `secure-shell/server/learn.mjs` — and the report cites that refusal as evidence
the gate holds. Both cannot stand as written: a learner that always refuses a scope change cannot be
one whose drivers set scope. The one question that would resolve it is whether `learn-scope-fixed`
becomes a *bounded* refusal (scope may change only with cited evidence, and is refused when it does
not) or disappears in favour of drivers proposing scope. It is not resolved here and the plan does not
assume an answer.

## What this round does not decide

- It does not promote any row to `HELD`; three rows move the other way.
- It does not authorise deleting the old digests, the old rows or the older report; `R1` corrects
  wording, and every superseded claim stays readable.
- It does not make a fresh Minecraft run a pass by being run; the run has to report its own digests.
- It does not settle `learn-scope-fixed`, which is named above as a tension with its question
  unasked.

## Next units, in the order the answers force

1. `CGA-45` side-by-side receipt — smallest, a field and an assertion.
2. `CGA-38` generation-move run — a tool that reads, ticks, then acts, with the act differing because
   the frame moved.
3. `learn-scope-fixed` — the tension above, as its own ticket before any learner change.
4. `CGA-14`/`CGA-28` — fresh world, fresh body, fresh digests; the most expensive and the last.
