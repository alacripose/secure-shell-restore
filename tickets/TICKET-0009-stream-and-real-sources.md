# TICKET-0009 — the stream unit, and the sources that were never absent

**Status:** `complete`
**Owner authority:** the owner's turn of 2026-11-04, source `user`: "the sources with their examples
are on this machine for the love of god". That correction is the unit's starting fact: two tickets
and a plan section had told the owner the work was blocked by inputs that were sitting on disk.

## 1. The goal, quoted

> `secure-shell.stream/1` with subordinate `surface.mount/2` receipts; Debian signature; resume;
> atomic adoption — "Tampered, unsigned, stale, replayed, truncated, and wrong-version fixtures
> refuse; adoption is exactly one revision"

(`docs/SECURE-SHELL-RESTORE@1.IMPLEMENTATION-PLAN.md` §3, R5.) The signature and admission clauses
of that exit condition are **not** met by this unit and are named as absent in §5.

## 2. The one artifact

`impl/packages/stream.py` with `tests/packages/run_cases_stream.py`, plus `impl/packages/loader.py`
and `tests/packages/run_cases_loader.py`, which turn a real source tree on this machine into a
package under the shipped contract.

## 3. The last check's three-way answer

All four suites `held` at `093d436`; the stream unit itself was `absent` — there was no way for a
package to arrive at all, whole or otherwise.

## 4. The drift signal observed

The record asserted two absences without checking the machine: that there was no OpenLock checkout
and no MongoDB. Both were false. `C:\Users\ala\Documents\openlock` carries
`clientaddon/panorama/layout/openlock_shell.xml` and fifteen shell files; `secure-shell` carries
`shell/openlock/panorama/scripts/secure_shell_stream.js`, `secure_shell_rounds.js` and a `server/`
tree; and `/c/Program Files/MongoDB/Server/8.3/bin/mongod.exe` reports `db version v8.3.11`. A claim
about the machine that no command verified is a guess wearing a status, which is exactly what
`AGENTS.md` §8 refuses.

## 5. Refusals this unit carries forward

- **No signature and no admission.** The stream digest proves byte identity and ordering only. It
  says nothing about who produced the package; the Debian signing authority is not reachable here,
  and `signature` is absent from the header rather than faked.
- **R2 has not been run.** The loader gives the OpenLock shell a real identity, but no generator was
  executed, so byte-stable regeneration is still unproven.
- **R3 has not been run.** `mongod` exists on this workstation, but a Debian-hosted store, the
  restore drill and the store digest do not. A local `mongod` is not the Debian authority.
- Chunking is fixed-offset; `--truncate` and resume assume that, and a content-defined chunker
  would need its own ticket.
- The loader admits four extensions and skips `node_modules`, `dist`, `obj` and `bin`. That is a
  selection rule, not a security boundary.

## 6. The next artifact

The R2 selection record: the named OpenLock files, the generator that produces them, and a
regeneration that reproduces the same `secure-shell-openlock-shell` identity byte for byte.

## 7. The record entry just written

`AF-23` and `AF-24` in `docs/SECURE-SHELL-HEALTH@1.FAILURE-LEDGER.md`.
