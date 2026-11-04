<!-- Health-and-policy record. Owner ruling A-12, 2026-11-04: a unit may not close without a verification receipt from a second agent identity naming the trained axis driver ticket it handed off to. Append-only. -->

# SECURE-SHELL-HEALTH@1 — handoff register

**Document identity:** `SECURE-SHELL-HEALTH@1`
**Kind:** HANDOFF
**Status:** Executing. The refusal set below is enumerated, runnable and gating; the CI workflow runs it on every push.

## 1. What this record is

`A-12` ruled that a unit close is refused `handoff-absent` unless a second agent identity has verified
the handoff. That ruling was a sentence with nothing behind it until this register. The mechanism is
`tools/handoff_ratchet.py`, and this document is its human-readable register: what it refuses, what a
receipt carries, and what each case actually did when it ran.

It sits in the health format rather than in the five `SECURE-SHELL-RESTORE@1` plan documents, because
Q019 keeps those five and a sixth document there would be a second writer to an ownership that is
already fixed.

## 2. The refusal set, enumerated

Order matters: the ratchet stops at the first failure, so an unreadable store is refused before it can
be read as an empty one.

| Refusal | When | Subject in the output |
|---|---|---|
| `handoff-receipt-unreadable` | the store, the close or a receipt cannot be read against `secure-shell.handoff/1`, the store is missing, or a receipt's date or evidence is not shaped like one | the path |
| `handoff-driver-unnamed` | the close names no driver ticket, or the receipts name a different one | the unit |
| `handoff-absent` | no receipt in the store names this unit | the unit |
| `handoff-author-mismatch` | every receipt for this unit names another author than the closing one | the unit |
| `handoff-self-verified` | the only verifier for this unit and ticket is the author | the unit |
| `handoff-not-held` | the second-identity receipt reports something other than `held` | the unit |

There is no skip flag, no `--force`, no environment bypass and no wildcard unit. A close that cannot be
verified cannot be made to pass; that is the difference between a ratchet and a suggestion.

## 3. The receipt, and why the identities must differ

A receipt is one JSON object per line in `docs/hypergrill/handoff@2026-11-04.jsonl`, append-only, read
the way `receipts.jsonl` is read:

| Field | Meaning |
|---|---|
| `schema` | `secure-shell.handoff/1`, refused if anything else |
| `unit` | the ticket being closed |
| `author` | the identity that did the work |
| `verifier` | the identity that checked it; equal to `author` is `handoff-self-verified` |
| `driver_ticket` | the trained axis driver ticket the unit hands off to |
| `result` | `held` permits; anything else is `handoff-not-held` |
| `evidence` | a pin the verifier read — a path with a line, or a command and its exit status |
| `at` | when the verification finished |

The rule the ratchet exists for is the `verifier` ≠ `author` comparison. An agent that verifies itself
is the failure mode `AV-001` recorded, and `A-12` closed the question of whether that counts.

## 4. The three cases, as they ran on 2026-11-04

Run from this repository's own command, `python tools/handoff_ratchet.py close`, against the fixtures
in `tests/handoff/`. The outputs below are the tool's own lines, unedited.

| Case | Command inputs | Exit | Output |
|---|---|---|---|
| no receipt | `close-no-receipt.json` · `receipts-empty.jsonl` | **1** | `{"reason": "no receipt for this unit in the store", "refusal": "handoff-absent", "schema": "secure-shell.handoff/1", "state": "refused", "subject": "TICKET-9001"}` |
| second identity, held | `close-with-receipt.json` · `receipts-valid.jsonl` | **0** | `{"author": "agent:author", "driver_ticket": "TICKET-0100", "receipt_digest": "e12be728d4385091", "schema": "secure-shell.handoff/1", "state": "permitted", "unit": "TICKET-9001", "verifier": "agent:verifier"}` |
| author verifies itself | `close-self-verified.json` · `receipts-self.jsonl` | **1** | `{"reason": "the only verifier is the author (agent:author)", "refusal": "handoff-self-verified", "schema": "secure-shell.handoff/1", "state": "refused", "subject": "TICKET-9001"}` |

`python tools/handoff_ratchet.py self-check` — `RESULT: PASS (0 failed)` over eight throwaway cases,
including a missing store and a receipt whose `evidence` is blank.

`python tests/handoff/run_cases.py` — `3 cases, 0 failed`.

## 5. Where it gates

`.github/workflows/hypergrill-audit.yml` runs the contract and the three cases after the existing
checks. A push whose close cannot be verified fails there, before it is merged. Locally the same three
commands are part of the check set that a unit runs before it commits.

## 6. This unit's own handoff

`TICKET-0002` is closed through this ratchet, not around it. Its author is the agent that wrote the
ratchet; its verifier is a separately spawned research agent that read the published commit
`fc431fc` in its own context and returned `HELD` after quoting the lines behind each decision, and
which returned a further two documentation defects that were fixed before the close.

| Field | Value |
|---|---|
| unit | `TICKET-0002` |
| author | `buffy:secure_shell_v2` |
| verifier | `researcher-web:verification-1` |
| driver ticket | `TICKET-0100` (the driver-training ticket this unit hands off to; not yet opened) |
| evidence | the verifier's reading of `tools/handoff_ratchet.py` at `fc431fc`, and CI run `41850615681` |
| result | `held` |

The same close, run against the store before the receipt existed, is refused `handoff-absent`:
that refusal is what this unit's transcript shows, and it is why the receipt is not decoration.

## 7. What this does not do

- It does not grade anything. No token is added to `axis.data.json`, because `N042` closes the grade
  enum and `A-11`'s traffic-light naming is still unresolved.
- It does not prove the work is correct. It proves a second identity saw it and held it, which is a
  weaker and checkable claim.
- It does not cover the Debian TUI taskbar, the Mongo stream store or the Qt reader. Those come after
  the handoff grades, and none of them is started here.
- The store is caller-supplied and unsigned. `--store` exists so the three cases can run against
  fixtures, and a hand-written line in the real store would be read as evidence like any other. Signing
  the store is named here as missing rather than implied to exist.
- Identity is a string, compared case-folded. A receipt is only as good as the identity that wrote it,
  and this repository does not yet mint identities.
- `evidence` is shape-checked only. A receipt must carry something shaped like a path or a
  `path:line`, and nothing opens it, so a verifier's evidence is not yet re-read by the ratchet.
