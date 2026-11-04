# TICKET-0001 — record round v2.4, publish the record

**Status:** `review`
**Opened:** 2026-11-04
**Branch:** `main` (first unit; the branch convention starts with TICKET-0002)

## MISSION

Carry the owner's five answers of round v2.4 into the record, start the failure ledger the owner
required, and publish this workspace as its own repository — quoted from `A-14`: "you need to track
your failures as you work in true autonomy mode as a part of health and policy so the cua driver can
get a better understanding of you until it can be trusted to use git itself."

## SCOPE

| In | Out |
|---|---|
| `docs/SECURE-SHELL-RESTORE@1.HYPERGRILL.md` §8.8 — five answers verbatim, state table, what they change, the A-11 residue, message provenance, the publication directive | Any traffic-light token written into `axis.data.json` |
| `docs/SECURE-SHELL-RESTORE@1.FAILURE-LEDGER.md` — nine rows, each with evidence and the correction actually applied | Any claim that a ledger row clears a failure |
| Repository creation, visibility, first push | Any code, any package, any store schema |

## CONSTRAINTS

- Answers are recorded in the owner's words and are not curated.
- `A-11` is not read back into any of the four options offered; what it leaves unstated is named.
- No star token is invented, because N042 closes the grade enum and Q021 restricts names to `[a-z0-9-]`.
- Nothing is published that names a key, a token or a secret.
- One artifact per commit; under 40 files and 4,000 insertions.

## RESOURCES

`PATCH-004-five-star-axis.md` (`star.count: 6`, `star.lens: 5 rungs`), `N037`, `N042`, `A-04`,
`SECURE-SHELL-RESTORE@1.IMPLEMENTATION-PLAN.md` §1 rules 5 and 9, §7; the working tree's checks
`.cache/hg_check7.py`–`.cache/hg_check11.py`, `tools/hypergrill_resolver.py`,
`tools/hypergrill_reaudit.py`.

## EVIDENCE

| Check | Command | Expected |
|---|---|---|
| Re-audit of the 500 | `python tools/hypergrill_reaudit.py --strict` | exit 0 |
| Synthesis shape and digests | `python .cache/hg_check11.py` | every digest verifies against the committed tree |
| Coverage, register, counts | `python .cache/hg_check10.py` · `hg_check9.py` · `hg_check8.py` · `hg_check7.py` | 0 failed each |
| Resolver contract | `python tools/hypergrill_resolver.py self-check` | `RESULT: PASS` |
| Line endings | `python .cache/normalize_lf.py` | no CR remains |
| Publication | `sites`-free: repository visibility read back from the GitHub API | `private: false` |

## DELIVERABLE

A pushed repository at `alacripose/secure-shell-restore` whose `main` carries the round record and the
failure ledger, with each check's exit status written into the completion note rather than asserted.

## STOP

Stop and report, without closing the ticket, if: a digest does not verify after a rescan; the push is
refused for credentials; the visibility change is refused; or a file in the tree names a secret.

## Todo

- [x] Ask the five questions and record the answers verbatim
- [x] Write the failure ledger
- [x] Record the publication directive in the round
- [ ] Rescan so every digest matches the committed files
- [ ] Run the six checks and record their exit statuses
- [ ] Create the repository, make it public, push `main`
- [ ] Close the ticket with the receipt
