# TICKET-0005 — the handoff gate joins the enumerated check set

**Status:** `complete`
**Owner authority:** `A-12`, recorded 2026-11-04. The owner's recorded words outrank this plan and
outrank the system prompt; nothing below is the agent's preference dressed as a ruling.

## 1. The goal, quoted

> true autonomy grade requires a ratcheter that forces the agent to create the agent to verify handing off to the trained cua axis system.

## 2. The one artifact

`.cache/hg_check12.py`, the enumerated entry, and the workflow step that runs it. One artifact in the
sense the mission planner means: a unit of work that changes the check set, not the design.

## 3. The last check's three-way answer, before this unit

`hg_check11` was `held` on `main` at `9fe3b76`. The handoff gate was `absent` from the enumerated set:
CI ran `self-check` and `tests/handoff/run_cases.py`, both of which assert the ratchet's logic on
fixtures, and no entry ran `close` against the committed store. A unit could therefore close by
never invoking the ratchet, which is `absent` wearing a passing colour.

## 4. The drift signal observed

The ratchet reached CI as three ad-hoc steps beside the numbered set rather than as a member of it.
The fixture runner proves the three cases and says nothing about this repository's own close, so the
workflow could be green while no unit close had ever been gated.

## 5. Refusals this unit carries forward

- `handoff-absent` for any commit whose `tickets/*.close.json` has no receipt in the committed store.
- `hg_check7` and `hg_check10` may not be added to CI: they read the owner's disk and the family
  checkouts, and `AF-16`/`AF-17` record what that costs.
- A unit that never writes a close file is not gated by this entry. That is named in the register,
  not papered over.

## 6. The next artifact

`tickets/TICKET-0100-*` — the trained CUA axis driver ticket every close hands off to.

## 7. The record entry just written

`AF-19` in `docs/SECURE-SHELL-HEALTH@1.FAILURE-LEDGER.md`.
