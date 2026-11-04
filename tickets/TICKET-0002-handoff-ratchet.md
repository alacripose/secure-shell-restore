# TICKET-0002 — the handoff ratchet executes

**Status:** `complete`
**Opened:** 2026-11-04
**Branch:** `ticket/TICKET-0002-handoff-ratchet`

## MISSION

Turn the refusal recorded under `A-12` — "`handoff-absent` at unit close" — into a check that
runs, refuses and gates. Quoted from the owner's mission: "true autonomy grade requires a ratcheter
that forces the agent to create the agent to verify handing off to the trained cua axis system."

## SCOPE

| In | Out |
|---|---|
| `tools/handoff_ratchet.py` — `list`, `self-check`, `close` with five enumerated refusals | Any grade token, star rung or ladder entry |
| `tests/handoff/` — three concrete unit-close cases and their receipts | The Debian TUI taskbar, the Mongo stream store, the Qt reader |
| `docs/SECURE-SHELL-HEALTH@1.HANDOFF.md` — the register, in the health format | A sixth `SECURE-SHELL-RESTORE@1` document |
| CI steps that gate a push on the ratchet | A skip flag, an environment bypass, or a "trust me" path |

## CONSTRAINTS

- The author and the verifier are different identities; a self-verified close is a refusal.
- No new refusal name outside `[a-z0-9-]` (Q021); no grade token is invented (N042 is a closed enum).
- `A-11`'s traffic-light naming stays unresolved; nothing is written into `axis.data.json`.
- One artifact per commit, under 40 files and 4,000 insertions.

## RESOURCES

`A-12` in `SECURE-SHELL-RESTORE@1.HYPERGRILL.md` §8.8; the failure ledger's rows `AF-10`–`AF-12`;
`.github/workflows/hypergrill-audit.yml`; `.cache/hg_check7.py`–`hg_check11.py`;
`tools/hypergrill_resolver.py`.

## EVIDENCE

| Check | Command | Must be |
|---|---|---|
| No receipt | `python tools/handoff_ratchet.py close --close tests/handoff/close-no-receipt.json --store tests/handoff/receipts-empty.jsonl` | exit 1, `handoff-absent` |
| Second identity, held | same with `close-with-receipt.json` / `receipts-valid.jsonl` | exit 0, `permitted` |
| Author verifies itself | same with `close-self-verified.json` / `receipts-self.jsonl` | exit 1, `handoff-self-verified` |
| Contract | `python tools/handoff_ratchet.py self-check` | `RESULT: PASS` |
| The three cases | `python tests/handoff/run_cases.py` | `3 cases, 0 failed` |
| Existing checks | `hg_check7`–`hg_check11`, resolver, `hypergrill_reaudit.py --strict` | all exit 0 |

## DELIVERABLE

`main` at `alacripose/secure-shell-restore` carrying the ratchet, its fixtures, the register and the
CI gate, with this unit's own close permitted by a receipt from a second identity.

## STOP

Stop and report, without closing, if: the ratchet permits a close with no receipt; it permits a
self-verified close; a pre-existing check regresses; or the PR cannot be merged.

## Todo

- [x] Write the ratchet and its enumerated refusals
- [x] Write the three cases and their receipts
- [x] Run the cases and record the exit codes
- [x] Obtain a second identity's verification of this unit
- [x] Close this unit through its own ratchet
- [x] Rescan, run every check, commit, push, open and merge the PR

## Receipt

| Field | Value |
|---|---|
| Commits | `82369e0` ratchet and cases, `9ea2bec` no-probe for an absent file, `3f18114` CI contradiction gate, `b3d0dec` local-only checks named, `fc431fc` receipt bound to its author |
| Unit close | `python tools/handoff_ratchet.py close --close tickets/TICKET-0002.close.json` → `permitted`, receipt digest `13d28bb8e4904f87` |
| Refused before the receipt | the same close against the store before the receipt existed → exit 1 |
| Verifier | `researcher-web:verification-1`, a separately spawned agent that read commit `fc431fc` and returned `HELD`, then two documentation defects that were fixed |
| CI | run `41850615681` on `fc431fc`, conclusion `success` |
| Cases | `python tests/handoff/run_cases.py` → `3 cases, 0 failed` |
| Contract | `python tools/handoff_ratchet.py self-check` → `RESULT: PASS (0 failed)` over eight throwaway cases |

Not done in this unit, named rather than implied: the store is unsigned and caller-supplied, identity
is an unchecked string, `evidence` is shape-checked only, and no grade token was added because N042
closes the enum and A-11's traffic-light naming is still unresolved.
