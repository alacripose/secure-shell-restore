<!-- Continuation of the SECURE-SHELL-V2 planning set. The 20 decisions and the four follow-up rulings in docs/answers.txt are recorded here as settled. No repository was modified. -->

# SECURE-SHELL-RESTORE@1 — implementation plan and decision register

**Document identity:** `SECURE-SHELL-RESTORE@1`
**Status:** Accepted sequence. Replaces `SECURE-SHELL-V2-IMPLEMENTATION-PLAN.md`, whose decision gate is now closed.
**Release:** Restore. OpenLock generation → Debian store rebuild → streamed TUI taskbar and console → Qt client.

## 1. The eleven rules that govern this plan

1. Every contract, defect, and unit gets a ticket.
2. One ticket → one branch → small coherent commits → PR.
3. Every commit cites its ticket and the ledger row it produces. No row, no commit.
4. Every command that can refuse prints a machine-readable result and exits non-zero. A silent failure is a tool defect.
5. A unit changes a named artifact and has an executable exit test. `git status`, `git diff`, or a screenshot alone is not a unit.
6. Health runs every test turn and only tightens: a check once held may not fail again.
7. A proposal is not a rule. It becomes one through ticket, owner decision, implementation, acceptance.
8. Artifacts stay under the checkout; prompts, keys, and secrets stay outside git.
9. Commit budget: at most 40 files or 4,000 insertions.
10. A CUA or bot report is not a client witness.
11. **A health gate is not the work.** It measures work that a trained driver performed. When a gate starts absorbing the project's effort into scratch scripts, the gate is the defect.

## 2. Decision register — closed

Answers are the owner's. Nothing here is re-litigated by implementers; a change requires a new recorded ruling.

| # | Question | Ruling |
|---|---|---|
| 1 | Identity and naming | `secure-shell` keeps its identity, and pins version and hash by name |
| 2 | Version scheme | Version is independent and bumps per revision, while still pinning what it compiled against in the name |
| 3 | MongoDB authority | Mandatory, except inside CUA-provided scratch workspaces |
| 4 | MongoDB topology | Debian provides everything; first version is **Restore** — rebuild the DB on Debian, stream the basic TUI desktop first, CUA shows spinning loaders for work in progress, the taskbar's default window is the actual Debian console, other Debian features stream securely through the format; CUA must be performant at thousands of workers, which `ala_civ_bots_prototype` tested |
| 5 | Persistence and security | Yes: encrypted storage, authenticated service identities, append-only event permissions, verified backups |
| 6 | Package integrity | Whatever is fast, stateful, network-streamable, runs on small things but scales hugely, and can be operated by trained CUA drivers → **BLAKE3** content identity |
| 7 | Signing authority | The Debian server |
| 8 | Stream contract | Carry mount receipts as an independently versioned subordinate contract |
| 9 | OpenLock generation | Yes — the programmatic shell begins the Debian store regeneration, providing the streamed TUI taskbar, the console window, and the client's QTXML reader |
| 10 | Display format | Qt 6, latest pinned per release via GitHub CI; must support motion and bitmaps as the SWF importer attempted |
| 11 | Display ownership | Server sends declarations and content; the client owns rendering, focus, input, and CUA observation |
| 12 | SWF boundary | The SWF importer is examples; isolated behind the streamer API |
| 13 | Planet migration | `planet-*` retained as a quarantined legacy decoder during migration |
| 14 | Legacy handling | Legacy packages imported into an explicit compatibility representation, then rewritten into the new format |
| 15 | Split formats | Determined by reading the committed audit: distinct identifiers per family, refused by name, never auto-detected |
| 16 | Text normalization | Yes: UTF-8, declared newline policy, canonical serialization, conversion only through recorded migrations |
| 17 | CUA responsibilities | Yes, and wider: boot, recovery, health, format identification, mount, migration verification; the ratchet measures streamed vs legacy coverage; the driver works through the system over time, down to kernel-level operations on an air-gapped host controlled over the network, as a security-enhanced authorization system driven by a System-1 model |
| 18 | Agent API | Yes: a small generated API template plus capability-scoped manifest, streamed from the internal store, without mounting every shell component |
| 19 | Civilian verification | Yes; civilians are the model for CUA agents, represented by `cellular_generativity_axis_civilian_expectations_prototype_rechecked` |
| 20 | Daily acceptance | 24-hour continuous simulation |

### 2.1 Follow-up rulings

| Id | Ruling |
|---|---|
| R-A | Canonical identity `package-name@<monotonic-integer-revision>+blake3:<content-hash>` |
| R-B | Monotonic integer revisions; API and compatibility versions tracked separately |
| R-C | BLAKE3 covers the complete canonical content after deterministic serialization, and not transport framing, encryption, or the Debian signature envelope |
| R-D | Health is incremental by default (changed components plus dependency closure); full-tree and exhaustive migration audits run at release gates and the scheduled 24-hour run; verification tools are versioned driver capabilities, not scratch scripts |

## 3. Milestones

The order is fixed by the rulings: generate from OpenLock before writing a renderer; establish the store before the stream; stream before the client polish; train the driver on one window before asking it to migrate anything.

| Milestone | Work | Exit condition |
|---|---|---|
| **R0 — Record and supersede** | Land the decision register in `secure-shell/docs/DECISIONS.md`; name the superseded rules (no MongoDB, no new format, file-backed ledger as sole record) and the rules that still bind (one reader, one display, client witness, external vault, refusal by name) | No implementation depends on an unresolved owner; the superseding entry cites this document |
| **R1 — Family audit at pinned commits** | Reproduce the audit procedure over `secure-shell`, `swf-cell-runtime`, OpenLock, `ala_civ_bots_prototype`, `ala-cities` | Every format has one owner, one reader, a version, and a migration policy; unknowns are `absent` with a named lookup |
| **R2 — OpenLock generation** | Select and generate from OpenLock's real sources; record selection and rejection; capture generator identity | Clean regeneration reproduces byte identity; no hand-edited generated output |
| **R3 — Debian restore** | Rebuild the MongoDB store on Debian from declared inputs; `systemd-creds` credentials; per-package keys; backups and a restore drill | A clean host reproduces the store digest; restore drill artifact exists |
| **R4 — Package contract** | Implement `name@rev+blake3:` identity, canonical serialization, schema ids, chunk domains | Independent reader and writer agree; tampered, truncated, ambiguous, and foreign-revision fixtures refuse by name |
| **R5 — Signed stream** | `secure-shell.stream/1` with subordinate `surface.mount/2` receipts; Debian signature; resume; atomic adoption | Tampered, unsigned, stale, replayed, truncated, and wrong-version fixtures refuse; adoption is exactly one revision |
| **R6 — TUI taskbar and console** | Stream the first desktop: taskbar, default Debian console window, CUA loaders for in-progress work | Both surfaces mount from the store and are witnessed; no out-of-band console channel |
| **R7 — Qt client** | One bounded QTXML reader and renderer; motion and bitmap support under budgets; Qt 6 pinned in CI | First stored window renders in the real client; a client-side check produces a witness |
| **R8 — Axis CUA on the first window** | Read-only inspection first, then launch/present/mount/health/recovery verbs, each ticketed | Every action bounded, idempotent, acknowledged, postcondition-verified, client-visible |
| **R9 — Agent API and templates** | Capability-scoped manifest; generated template streamed from the internal store | An agent inspects and streams one declared surface without mounting the desktop and without seeing secrets |
| **R10 — Legacy quarantine** | Compatibility representation; read-only legacy decoder; rewrite path into the new format; sunset policy | Legacy fixtures read through the adapter; new packages only in the new family; no `planet-*` runtime dependency on the canonical path |
| **R11 — Civilian 24-hour simulation** | The lived workday under Axis, with interruption, recovery, and independent verification | A 24-hour run passes the acceptance contract in §6 |
| **R12 — Cross-host parity** | Clean second host, rebuild, re-stream, re-witness, roll back | Package identity, stream result, and client witness reproduce; rollback restores the prior revision |

## 4. What each milestone owes the next

- R0 owes R1 a decision record, not a summary.
- R1 owes R2 a source-selection record with rejected alternatives named.
- R2 owes R3 declarations that are byte-stable on regeneration.
- R3 owes R4 objects whose canonical bytes are already deterministic.
- R4 owes R5 a manifest whose preimage excludes framing — otherwise the stream redefines identity.
- R5 owes R6 receipts that name exactly one revision.
- R6 owes R7 a declaration the client can read without a second grammar.
- R7 owes R8 a witness surface the driver can observe honestly.
- R8 owes R9 an action catalogue narrow enough to publish as a tool manifest.
- R9 owes R10 typed document authoring, so migration is a recorded operation rather than a script.
- R10 owes R11 a system whose streamed-versus-legacy ratio is measurable.
- R11 owes R12 a run that can be repeated.

## 5. Health: incremental by default, exhaustive at gates

Per R-D:

| Cadence | Scope | Refusal behavior |
|---|---|---|
| Every test turn | Gate + checks for changed components and their dependency closure | A previously held check that fails is a ratchet regression, exit 2 |
| Every commit | The unit's exit test plus the closure it touches | A unit with no ledger row is refused |
| Release gate | Full-tree audit, exhaustive migration coverage, regeneration proof | Release refused if any check is `refused` |
| Scheduled 24-hour run | Full-tree audit inside the simulation | The run is refused if the audit is `absent` |

What this replaces: the SWF importer's health gate became slow because the project devolved into one-off Python scripts and repeated full-tree scans used as proof of progress. The corrective is not a faster scanner. It is a trained driver that takes an assigned ticket, searches the web for missing requirements, does the work, and runs repository-owned checks whose output is stored — with verification tools versioned as capabilities rather than regenerated each time a check fails.

A full scan is therefore never the routine proof of a small unit. If a unit needs a full scan to look finished, the unit is wrong.

## 6. The 24-hour acceptance contract

A day is 24 continuous hours (decision 20), not a compressed schedule and not a task quota.

A day passes only if all of the following hold:

- one stable agent identity from start to finalization;
- every task has declared input, owner, expected postcondition, window, and exit test;
- CUA observes and diagnoses before acting, and executes only admitted operations;
- completion is verified from server and client postconditions, never from model self-report;
- no task is skipped, duplicated, widened, or completed without evidence;
- refusals, timeouts, and recoveries remain visible in the record;
- at least one injected interruption and one recovery complete without history loss;
- pre/post-split inputs are read by their exact readers, with explicit migration lineage;
- the streamed-versus-legacy ratio is recorded at start and end;
- restore and rollback leave the prior admitted revision available;
- a real client witness confirms the first windows and at least one meaningful CUA operation;
- the day ends with residents returned to ordinary autonomous life, and test-owned resources released.

Only the shell gate assigns `held`, `absent`, or `refused`. The driver reports implementation facts.

## 7. Commit and ticket discipline

- Branch `ticket/TICKET-XXXX-short-name`; commit subject begins with the ticket id and the ledger entry id.
- A commit over 40 files or 4,000 insertions is refused; split the unit.
- A change that removes a named state, store, command, or check to shrink the diff is refused (`surface-trimmed`). Build the maximal surface first; trim later with its own ticket.
- Refusals are recorded rows, not console strings.
- A long check is a waitable command with a stated bound, not a log to watch. A marker that is absent is `absent`, not `pending`.

## 8. Sequence risks

| Risk | Consequence | Mitigation |
|---|---|---|
| OpenLock generation treated as a screenshot port | The shell becomes a mock the store cannot regenerate | R2 requires generator identity and byte-stable regeneration |
| BLAKE3 applied over framed or encrypted bytes | Re-encryption silently changes identity | R-C is a test: re-frame and re-encrypt the same content, digest must not move |
| Stream schema and mount receipt versioned together | A transport change invalidates receipts | Separate version axes, tested independently |
| Health gate absorbing project effort | Slow gate, no work done | R-D; versioned verification tools; full scans only at gates |
| CUA trained on the happy path | Recovery claims without recovery | Injected failure classes in R8 and R11 |
| Legacy adapter becoming the runtime | `planet-*` never leaves | R10 exit requires the canonical path to have no `planet-*` dependency |
| Thousand-worker claim untested | Scale asserted, not measured | R11 records worker counts and latency from the tested prototype |

## 9. Open items carried forward

`OPEN-KEY-1`, `OPEN-KEY-2`, `OPEN-STORE-1`, `OPEN-STORE-2`, `OPEN-QT-1`, `OPEN-QT-2`, `OPEN-FMT-1`, `OPEN-CUA-1`, `OPEN-CUA-2`, `OPEN-API-1` — as defined in `SECURE-SHELL-RESTORE@1.ARCHITECTURE.md` §12. The plan does not silently resolve any of them; each milestone that needs one opens a ticket naming it.
