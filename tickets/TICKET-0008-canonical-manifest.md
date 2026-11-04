# TICKET-0008 — the declared package object: schema ids, manifest vocabulary, chunk domains

**Status:** `complete`
**Owner authority:** the owner's turn of 2026-11-04, source `user`: "get the secure shell restore
going", continued by the mission to take the next executable milestone in dependency order. R4's
second half is a plan requirement, not an agent preference; the vocabulary chosen here is the
agent's and is labelled so.

## 1. The goal, quoted

> Implement `name@rev+blake3:` identity, canonical serialization, schema ids, chunk domains — exit
> condition: "Independent reader and writer agree; tampered, truncated, ambiguous, and
> foreign-revision fixtures refuse by name"

(`docs/SECURE-SHELL-RESTORE@1.IMPLEMENTATION-PLAN.md` §3, R4.)

## 2. The one artifact

`impl/packages/canonical.py` with `tests/packages/run_cases_canonical.py`. Identity was already
decided; this unit declares what the content it hashes may contain.

## 3. The last check's three-way answer

Identity `held` on `24fc04e` (26 cases, 0 failed) and `hg_check12` `held` (14 checks, 0 failed).
The manifest shape was `absent`: `identity.package_digest` hashed whatever dictionary it was
handed, so an undeclared key entered the preimage and a typo could change a package's identity
without any refusal.

## 4. The drift signal observed

The architecture document names the preimage in prose (`canonical_manifest || deps || schemas ||
payload`) but nothing enforced which keys exist, what a schema id looks like, or that a chunk
digest is a different thing from a package digest. A contract that exists only in a document is
the same defect `AF-21` recorded one level up.

## 5. Refusals this unit carries forward

- R2 and R3 remain `absent` with their missing inputs named: no OpenLock checkout for generator
  identity, no `mongod` and no Debian host for the store digest and the restore drill.
- Chunking is fixed-offset, not content-defined. That is deliberate for a first cut and is not the
  same property as resumable content-defined chunking; a resume implementation must not assume it.
- Chunk digests prove bytes arrived under their role domain. They never prove package identity,
  and nothing here should be read as signature or admission (R5).
- The manifest vocabulary is closed by this ticket. Adding a key is a contract change and needs its
  own ticket; `manifest-key-unknown` exists to make that refusal audible.

## 6. The next artifact

`impl/packages/stream.py` — ordered bounded chunks, truncation detection and atomic adoption with
the signature slot explicitly absent, because the Debian signing authority is not reachable here.

## 7. The record entry just written

`AF-22` in `docs/SECURE-SHELL-HEALTH@1.FAILURE-LEDGER.md`.
