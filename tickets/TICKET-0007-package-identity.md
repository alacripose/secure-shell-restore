# TICKET-0007 — the restore begins: canonical package identity

**Status:** `complete`
**Owner authority:** the owner's turn of 2026-11-04, source `user`: "get the secure shell restore
going". The plan's R4 is the first milestone that can be executed on a workstation without the
OpenLock checkout or a Debian host. Placing the runtime in `impl/` is the agent's choice and is
labelled as one; it is not an owner decision.

## 1. The goal, quoted

> Implement `name@rev+blake3:` identity, canonical serialization, schema ids, chunk domains — exit
> condition: "Independent reader and writer agree; tampered, truncated, ambiguous, and
> foreign-revision fixtures refuse by name"

(`docs/SECURE-SHELL-RESTORE@1.IMPLEMENTATION-PLAN.md` §3, R4.)

## 2. The one artifact

`impl/packages/identity.py` and its exit tests in `tests/packages/run_cases.py`. The repository now
contains a runtime, which every prior document said it did not; the plan's rule 5 requires an
executable exit test, and no document can satisfy that.

## 3. The last check's three-way answer

`hg_check12` (`held`) on `fa4a0bf`, 14 checks, 0 failed. The R4 contract before this unit was
`absent` in the strict sense the family uses: the grammar existed only as prose in
`SECURE-SHELL-RESTORE@1.ARCHITECTURE.md` §2.1, and no command in this repository could produce or
refuse a canonical name.

## 4. The drift signal observed

Four milestones of a plan about a running system had produced zero runnable bytes, while the
project's effort continued to go into checks that read documents. That is exactly the failure
`rule 11` names: a health gate is not the work. The first contract that does not need a server is
package identity, so the runtime starts there rather than with another audit.

## 5. Refusals this unit carries forward

- R2 has not run **in this unit**: the OpenLock checkout is on this machine, but no generator was
  executed here, so generator identity and byte-stable regeneration remain unproven.
- R3 has not run: `mongod` 8.3.11 is installed on this workstation, but no Debian-hosted store, store
  digest or restore drill exists, and a local `mongod` is not the Debian authority.
- **Corrected 2026-11-04** (`AF-23`): this section first said there was no OpenLock checkout and no
  `mongod`. Both were on disk; the claim was made without checking, and `TICKET-0009` records the
  paths.
- Chunk domains and schema ids from R4 remain unimplemented; the entry covers the canonical name,
  the pin-complete set, and the R-C digest preimage only, and this ticket says so rather than
  letting the milestone look finished.
- Signature, admission and stream layers (R5) are untouched. A BLAKE3 name still proves only byte
  identity, never authorship.

## 6. The next artifact

`impl/packages/canonical.py` — chunk domains and schema ids, so the package object the digest covers
has a declared shape rather than an ad-hoc manifest.

## 7. The record entry just written

`AF-21` in `docs/SECURE-SHELL-HEALTH@1.FAILURE-LEDGER.md`.
