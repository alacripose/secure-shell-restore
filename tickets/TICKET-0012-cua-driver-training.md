# TICKET-0012 - train the CUA axis driver from every project, through the Debian store

**Problem.** The axis could issue tickets and record receipts, but no driver had ever
learned from this machine's projects, so the training half of the loop was unproven.

**Artifact.** `tools/cua_training.py`, plus the evidence report
`reports/cua-training/2026-11-05-driven-training.md`.

**What it does.** Reads `docs/secure-shell-audit/resynth_audit@2026-11-04.json`, turns each
project row into a `secure-shell.training/1` bundle, admits the bundle into the Mongo
authority on the Debian host, then applies it through the axis under a ticket. It witnesses
the corpus and performs one kernel-scoped act that only a driver declaring `kernel` may hold.

**Evidence.** Run on the Debian host, 2026-11-05: exit `TRAIN_OK`; 55 projects trained;
axis state 1 driver (`trusted: true`), 57 tickets, 57 receipts; transcript
`blake3:14c0d0ef77afbf8fe2bb86e9cff4184b8838437780de2e9e2e2c91879b449d7f` adopted by the
shipped `Receiver` with exit 0.

**Refused.** `driver-duplicate` on re-registration is treated as already enrolled, not as an
error; `corpus-absent` refuses a missing audit; every axis refusal is reported with its code.

**Not claimed.** No cellular substrate, no six-star aggregate, no client window or delegation
chat, no physical body outcome. Those rows are `NOT-ENFORCED` in the report.

**Next artifact.** A client surface that reads the same axis state: taskbar, console, and a
delegation chat that routes through tickets rather than describing them.
