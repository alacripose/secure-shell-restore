# CUA axis driver training: the Debian store, end to end (2026-11-05)

Command (inside the Debian host, sealed credential decrypted for the run only):

```
systemd-creds decrypt --name=mongo-uri /etc/secure-shell/mongo-uri.cred /run/drill-mongo.uri
cd /mnt/c/Users/ala/Documents/secure_shell_v2
/opt/drill-venv/bin/python tools/cua_training.py --uri-file /run/drill-mongo.uri --documents --depth 2 --budget 90
```

Exit status read from the process: `TRAIN_OK`; transcript `blake3:18c6607b9dd1e67ca102e746df7e46e5bf81a6096f28b6b6b44d9aaf1607980b`, 3 390 events, 1 545 317 bytes, re-adopted by the shipped `Receiver` (`adoptions: 1`, state `held`, exit 0).

## What was admitted

| Corpus | Items | Evidence |
|---|---|---|
| Project bundles (one per audit row) | 55 | `project-corpus-driver` trained, `state.tickets = 3 321` |
| Project documents | 3 264 | 3 264 `trained-document` events with `store` and `receipt` digests |
| Learning-apply tickets / receipts | 3 319 / 3 319 | 55 + 3 264, one ticket per item, one receipt per ticket |
| Witness and kernel tickets | 2 | `witnessed` and `kernel-scope` events, `receipts = 3 321` |

Projects discovered: 67. Projects that contributed documents: 62. There is **no per-project cap and no bundle ceiling**: the largest corpora were learned whole — `shploingus` 1 154 documents, `planet-shploingus` 710, `shploingus-clean` 601, `testport1` 128, `GregTech-Modern` 117, `ala-system` 80.

Selection rules, widened on purpose and stated here rather than implied: root `.md`/`.txt`, `docs/**`, `tickets/**`, `patches/**` and `.agents/skills/**/SKILL.md`. Vendored trees (`references/`, `node_modules/`, `target/`, `build/`, `generated/`, `.cache/`, `.git/`) are skipped by rule — 64 such directories across the corpus — because they hold copies of other projects, not this project's expectations.

## Every exclusion, named

Three documents were not admitted, for one deterministic reason: the axis accepts a request body of at most 1 000 000 bytes (`server/axis-server.mjs`), and these bundles exceed it.

| Project | Document | Encoded bundle bytes |
|---|---|---|
| `shploingus` | `docs/design_reference/GOD_AGENTS.md` | 2 815 216 |
| `shploingus` | `docs/original_reference/GOD_AGENTS.md` | 2 826 918 |
| `shploingus-clean` | `docs/LEDGER.md` | 1 048 524 |

This is a limit, not a cap: it is computed from the axis's own maximum body, it names each document and its size, and it changes the count in this report only when one of those documents changes. Learning them needs the axis to accept a multi-part bundle, which is a contract change and needs its own ticket.

Encoding is not a filter. These projects keep evidence as UTF-16 with a byte-order mark and as cp1252; 334 documents that the previous run recorded as `unreadable-utf8` are admitted in this run under the decode order UTF-8 → UTF-16 (BOM) → cp1252, with a NUL-and-no-BOM guard so binary is excluded by name instead of admitted as mojibake.

Revisions are deduplicated deliberately, by relative path and content digest: two copies of one file are two documents, and a changed document is a new identity beside the old one. Duplicate admissions in this run: 0.

## The expectation contract

The CGA civilian acceptance contract is in the learned set, twice, because `testport1` carries it at two paths:

- `secure-shell.training.docs/testport1-docs-cellular-generativity-axis--37a681f1b0@a0b10dc468719c38`
- `secure-shell.training.docs/testport1-docs-cellular-generativity-axis--877a73489e@a61b512143291176`

Both were applied under their own `learning-apply` ticket, so a receipt exists for each.

## Checks

| Check | Evidence | State |
|---|---|---|
| Driver registers and attests | `/api/axis/state` names `project-corpus-driver`, capabilities `witness, learning-apply, kernel` | PASS |
| Corpus is the folder audit | `docs/secure-shell-audit/resynth_audit@2026-11-04.json`, 55 rows | PASS |
| Every bundle reaches the Mongo authority | `impl.packages.mongo_store.admit` digest per item, restore digest matches | PASS |
| Every item is ticketed before it is applied | one `learning-apply` ticket and one applied receipt per item; tickets = receipts = 3 321 | PASS |
| No per-project cap remains | largest corpora admitted whole (1 154 / 710 / 601 documents) | PASS |
| Every exclusion is deterministic and named | the three `axis-body-limit` rows above, with sizes | PASS |
| The expectation contract is in the corpus | both CGA identities above | PASS |
| Corpus witnessed | `witness` receipt over the audit file digest | PASS |
| Kernel scope is declared, not assumed | `kernel` act accepted with `scope: kernel` | PASS |
| The transcript adopts | `python -m impl.packages.toolstream verify`: `adoptions: 1`, state `held`, exit 0 | PASS |
| Cellular substrate (CGA-38, CGA-45) | **Corrected 2026-11-05.** `secure-shell/server/cellframe.mjs` (245 lines) implements `CGA-38`'s contract per driver — ownership, declared radius, schedule, `rule-1`, lineage, budget, `stateDigest` — and `axis-server.mjs` refuses a citation of a frame that moved; `tools/axis-scale.mjs` opened 1 000 frames. `CGA-45` keeps `civilian.axis-cells/1` separate from `civilian.cellframe/1`. The round of 2026-11-05 holds both short of `HELD`: `CGA-38` needs the frame to move between reading and act, `CGA-45` needs a side-by-side receipt. Both are `absent`, not passed | NOT-ENFORCED |
| Six-star aggregation (CGA-44) | **Corrected 2026-11-05.** `secure-shell` 20b3c31: every receipt names six stars, each with its own lens and presenter, held only on a `stateDigest` the axis recomputed; `tools/axis-stars.mjs` → 1 000 drivers, 500/500 held per star, control held 0 | HELD |
| Client window, taskbar, delegation chat | **Corrected 2026-11-05.** `secure-shell/client/index.html` served by the axis: the taskbar read 3 drivers, 1 ticket, 3 cellframes; the delegation box POSTed `/api/axis/tickets` and showed the issued ticket | HELD |
| Physical outcome verification (CGA-14, CGA-28) | **Corrected 2026-11-05.** Held on a recorded live Minecraft 1.20.1 run (digests `fc7cfa24…` → `0ee6c3f5…` → `f49ceb59…`). The owner has since asked for a fresh world, body and digests; that run has not happened, so the re-proof is `absent` and the old digests may not be reused | HELD (recorded run); re-proof `absent` |

**Standards fixed 2026-11-05** by `docs/hypergrill/round@2026-11-05-four-row-standards.md`: the `CGA-45`
receipt is one document with `cellframe` nested and the aggregate a row inside it; the `CGA-38` proof is
lineage — the cited digest is the immediate successor of the read digest and the action differs from the
reading's earlier choice; the fresh physical run needs a body that is neither `AxisBody` nor entity id 1,
with the question of a differing level/seed left open. No row above changes state: all four remain
`NOT-ENFORCED`, and the physical row remains `HELD` only on its recorded run.

**Landed 2026-11-05.** The three standards are implemented and measured, and the two rows that could
move have moved: `CGA-38` is `PARTIAL` (the successor rule is enforced and `cellframe-successor` fires;
`tools/axis-scale.mjs` → 200 drivers, `choice {"differed": 22, "unchanged": 178}`, so a difference is
observed for 22 and the other 178 are recorded as not differing), `CGA-45` is `HELD` (one receipt,
`cellframe` nested with its own schema, driver, generation and digest, the `axis-cells` row inside it,
`server/test/receipt.test.mjs` and `server/test/cellframe-successor.test.mjs` passing in a 106-test
suite), and the learner's scope refusal is bounded — `setScope` accepts a verified record's two digests
and refuses one without, proven by `server/test/learn.test.mjs` and by `tools/axis-learn.mjs` →
`scope_granted_with_evidence` true with the refusal plant still firing. `CGA-14`/`CGA-28` are unmoved:
the owner's answer (a new body identity is sufficient) is recorded, and no fresh run has happened.

## Projects that carry no documents

Five discovered projects contributed no document at all: `DenseOres`, `Ecologics`, `MineFactoryReloaded`, `SeedDelight`, `optical`. Each is a Minecraft mod source clone with no `AGENTS.md`, no `docs/` and no tickets, so there is nothing in them to learn from beyond their audit row. They are named here rather than counted as learned.

A `NOT-ENFORCED` row is `absent`, never a pass. This report proves that a CUA driver learned from every qualifying document every project on this machine carries, through the Debian store, under axis tickets; it does not prove a civilian lived, a cellframe evolved, or a window rendered.
