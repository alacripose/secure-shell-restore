<!-- Continuation of the SECURE-SHELL-V2 planning set. Decision 15 was answered by reading the committed audit; this document records what that reading found. No repository was modified. -->

# SECURE-SHELL-RESTORE@1 — format and import audit

**Document identity:** `SECURE-SHELL-RESTORE@1`
**Status:** Audit continuation. Supersedes `SECURE-SHELL-V2-FORMAT-IMPORT-AUDIT.md` where that file says the split-family question is open — decision 15 was answered by reading the committed audit, and the findings are below.

## 1. Where the audit actually lives

The Secure Shell audit exists in two places, and they are not the same artifact:

| Location | Artifact | Pin |
|---|---|---|
| `secure-shell/docs/FORMAT-SOURCES-AUDIT.md` | The original ~1,180-line multi-project census | blob `61cd33413e8510e95f1e4bc4e3251c8c258926dc`, 85,859 B |
| `swf-cell-runtime/docs/secure-shell-audit/` | The committed copy plus the ruling records and machine census | tree `45bbcbc0885239f35a64f3a8a61a4e12a0edfa0d` |

Contents of the committed copy, as read on 2026-11-04:

| File | Size | What it settles |
|---|---|---|
| `cell-schema-ruling.md` | 8,260 B | Cells, ceilings, streamed vocabulary, and the MongoDB/store ruling |
| `secure_shell_synthesis.md` | 58,334 B | The identifier and magic census across four roots, plus store and evidence sites |
| `testport1_plan_resynthesis.md` | 23,044 B | Plan resynthesis after the split |
| `cellular_generativity_axis_civilian_expectations.md` | 65,183 B | Civilian expectations, earlier revision |
| `cellular_generativity_axis_civilian_expectations_prototype_rechecked.md` | 144,027 B | The current civilian/CUA representation cited by decision 19 |
| `scan_stream.jsonl` | 42,292 B | Machine-readable scan stream |
| `scan_state.json` | 3,912 B | Scan state |
| `scan_drives.py` | 10,297 B | The scanner itself |

The scanner is part of the record. A census whose tool is not committed cannot be reproduced, and an unreproducible census is `absent`.

## 2. Confirmed facts that change the plan

1. **The store question is already ruled.** `cell-schema-ruling.md` records: MongoDB, systemd-managed on the Debian host, credentials from `systemd-creds`; the `No MongoDB ... derail` line in `secure-shell/docs/ARCHITECTURE.md` is a branch position, not a v2 requirement. Decision 3 and decision 5 of `answers.txt` are consistent with this, not in tension with it.
2. **Key topology is per-package, not per-master.** The ruling changed to one key per package with no master, superseding the earlier three-derived-domain-keys line. The open consequence — ledger and store rows spanning packages — is `OPEN-KEY-2`.
3. **Ceilings are recorded but not defaulted.** 1 GiB working size, 4 GiB hard ceiling per package, 64-bit offsets, refused by name. The 512 KiB / 16 384 pair is overruled. The default value a new package gets is still `OPEN-FMT-1`.
4. **Vocabulary is streamed and per-package.** A labelled section at the top of the declaration, read before any cell that uses it. A name used but not declared is `shaper-undeclared`; a declared name whose body hash does not match is `shaper-hash-mismatch`. Open across packages, closed within each one.
5. **Cells are seven kinds, not four.** `row`, `bands`, `materials`, `shell`, plus cell, binding, and placement. Bindings name a declared identifier and nothing else — no paths, no expressions, no arithmetic.
6. **The first mounted surface uses cells.** The taskbar and dashboard XML lowers into declared cells rather than travelling as a payload. This is the bridge between the OpenLock generation step and the QTXML reader: XML is authored, cells are the package's declared form.

## 3. The legacy lock

The importer is compiled against the old package family. Confirmed dependency edge:

```toml
# swf-cell-runtime/crates/planet-package/Cargo.toml  (blob 43628df92f937db3dec2436246a7ead72525f39c)
[dependencies]
planet-shell-ledger = { path = "../planet-shell-ledger" }

[dev-dependencies]
planet-shell-ledger = { path = "../planet-shell-ledger" }
```

`planet-package` owns the `V4PKG001` frame. The family tree also contains `planet-aead`, `planet-client`, and `planet-save`. A hashed family identifier was added around the old frame, but the frame still carries its numeric schema field and its original digest preimage — the identifier work is classification, not migration.

`config/format-allowlist.json` (blob `5b9129f558c893374b8a07d76bbc10bf02b84f1c`) permits exactly one magic, `V4PKG001`, and forbids the identifiers `shpkg` and `openlock.addons` as content formats. The census below shows the tree carrying more than that allowlist admits. That gap is the finding, not a scanning error: the gate reads code, the census reads everything.

## 4. Pre-split and post-split families (decision 15)

Read from `secure_shell_synthesis.md`'s census. File counts and presence markers are as recorded there.

| Root | Files | Repo markers | XML | Magics seen | Character |
|---|---|---|---|---|---|
| `shploingus-game` | 27,925 | no `AGENTS.md`, no workflows | 1,452 | none recorded in the census lines read | **Pre-split** — the large historical tree |
| `shploingus` | 8,318 | no `AGENTS.md`, no workflows | 726 | none recorded | **Pre-split** — intermediate |
| `shploingus-clean` | 4,214 | `VOWS.md`, no workflows | 0 | `SHPKG002`, `SHPKG003` | **Post-split** — cleaned tree, conventions without CI |
| `testport1` | 108 | `AGENTS.md` + `port-gate.yml` | 0 | `V4PKG001`, `SHPKG002`, `SHPKG003`, `V4PKG002` | **Post-split** — the tree with a gate |

Four magics are observed across these roots: `V4PKG001`, `V4PKG002`, `SHPKG002`, `SHPKG003`. Only `V4PKG001` is allowlisted.

Identifier density differs by family and is the signature of the split:

| Identifier | Where it dominates | Reading |
|---|---|---|
| `shploingus.cellframe/1` | `testport1` (×30), `shploingus-clean` (×13) | Post-split cell surface |
| `shploingus.cells/1` | `testport1` (×26), `shploingus-clean` (×4) | Post-split cell set |
| `surface.mount/2` | `testport1` (×16) | The mount receipt Restore must carry as a subordinate contract |
| `dl-enclave.surface/1` | `testport1` (×6) | The window declaration selected by Secure Shell |
| `shploingus.recipe/3` | `shploingus-clean` (×29) | Post-split recipe schema |
| `openlock.addons/2` | `testport1` (×3) | Display contract, not a package format |
| `planet-shell.ledger/1` | `testport1` (×2) | Legacy ledger identifier |
| `shploingus.layer/1`, `compendium/1`, `receipt/2`, `save/1`, `mesh/2` | `shploingus-clean` | Post-split families with no Restore counterpart yet |
| `shploingus.receipt/0`, `/1`, `/2` | `shploingus-clean` | Three receipt revisions coexisting — a migration hazard |

### 4.1 The rule this produces

- Each family gets its own schema identifier and its own reader. No automatic detection by sniffing magic, length, or filename.
- A frame from a family the build does not read is refused by name with `found` and `supported`.
- `SHPKG002`, `SHPKG003`, and `V4PKG002` are **legacy decoder** inputs, never emit targets.
- `shploingus.receipt/0` and `/1` are read only through the compatibility representation; `receipt/2` is the migration source for the Restore receipt contract.
- The pre-split trees are evidence about old readers. They are not format authority, and Restore does not inherit their grammars.

## 5. Migration route (decisions 13, 14)

```
legacy package ──▶ quarantined read-only decoder ──▶ compatibility representation
                                                              │
                                                              ▼
                                                    explicit rewrite record
                                          (source id, target id, before/after digest,
                                           unknown/lost fields, actor, ticket)
                                                              │
                                                              ▼
                                              new package in the Restore family
```

Rules:

- The legacy decoder is read-only, quarantined behind the streamer boundary, and carries a sunset policy.
- The compatibility representation is explicit: it has a schema, not "whatever the old reader returned".
- A rewrite never happens in place. The source package keeps its identity and its bytes.
- A field the target cannot carry is recorded as lost, by name, in the rewrite record. Silent dropping is `legacy-field-lost-unrecorded`.
- New emissions are Restore-family only. `planet-*` disappears from the canonical path at R10, not at R0.

## 6. Text normalization (decision 16)

The SWF tickets established the hazard: a selftest identity computed over LF bytes changed when the checkout materialized CRLF under `core.autocrlf`. Regenerating the record fixed the state, not the portability. `.gitattributes` now pins selected paths to LF (blob `3b37b02dac07d86ebf1350f8624cbf40b52cb2d3`, 571 B).

What Restore adopts:

- **Source and docs:** UTF-8, one declared newline policy, no mixed endings, no BOM. `.gitattributes` makes checkout bytes reproducible.
- **Structured records:** deterministic field order, deterministic number and string encoding, an explicit serializer version.
- **Packages:** exact bytes preserved; no text newline conversion on binary objects; hash computed after canonical serialization and before transport, per R-C.
- **Signed manifests:** canonical encoding, domain-separated input; the verifier must not parse and reserialize under different rules.
- **Generated artifacts:** generator identity, input identity, and a post-materialization identity report, because checkout can mutate bytes.
- **Migrations:** newline normalization is a repository migration; schema migration is a separate operation with its own source/target versions, tests, and ledger row. They are never the same ticket.

The rulings push this further than a newline policy: canonical declaration text is re-encoded on write so spacing cannot move the digest, and the new formats do not depend on CR or LF at all. Newline becomes a checkout property of text, and text becomes a projection of canonical package content — not the package itself.

## 7. OpenLock envelope

The audit records four committed envelope rows as unsigned, with empty digest, key, authority, and signature values and zero work. The generator reads the envelope; the client renderer does not verify it. HMAC-SHA256 plus a leading-zero nonce is the existing mechanism.

Keep: fail-closed named refusals, keys outside the checkout, verification before presenting untrusted data, visible refusal state.
Replace: optional unsigned acceptance as a default, renderer-owned trust, nonce work as identity, any in-band claim treated as a verdict.

## 8. What the first window inherits from this audit

- The window declaration is `dl-enclave.surface/1` content lowered into declared cells — not a new window grammar.
- The mount receipt is `surface.mount/2`, subordinate to the stream and independently versioned.
- The taskbar and console surfaces are package content, streamed; the console is not an out-of-band socket.
- QTXML is the client's reader of the declaration. It is not a package format and does not get a magic.

## 9. Audit procedure still owed (R1)

The committed scanner reports; it does not yet classify. R1 must add a repeatable report covering: commit and branch identity; format token, header, digest domain, serializer, signature; reader/writer/declaration owner per family; the importer→package→store→stream→client graph; the legacy registry and its emit gate; pre/post-split crosswalk coverage; per-file line-ending and canonical-byte classification; generated-file provenance and clean regeneration; API tool schema completeness; CUA action catalogue binding; civilian continuity coverage; and a threat review covering package traversal, key handling, replay, BSON injection, decompression bombs, parser limits, and session leakage.

Output is a source-derived report plus a machine-readable inventory. Not an agent's declaration of what it believes the repository contains.

## 10. Pins

| Artifact | Pin |
|---|---|
| `secure-shell` main tree | `124b6471891d14038f4402d52598ff1c4357a18a` |
| `docs/FORMAT-SOURCES-AUDIT.md` | blob `61cd33413e8510e95f1e4bc4e3251c8c258926dc` |
| `swf-cell-runtime` main tree | `141bb5da43eb4062ba8938c019f2df20de9079d2` |
| `docs/secure-shell-audit/` | tree `45bbcbc0885239f35a64f3a8a61a4e12a0edfa0d` |
| `cell-schema-ruling.md` | blob `526928543625095ef99961eff8e1bda76fe75d1d` |
| `secure_shell_synthesis.md` | blob `579afe0ec452d8dee615667e2dd50aeabffd7ff8` |
| `config/format-allowlist.json` | blob `5b9129f558c893374b8a07d76bbc10bf02b84f1c` |
| `crates/planet-package/Cargo.toml` | blob `43628df92f937db3dec2436246a7ead72525f39c` |
| `.gitattributes` | blob `3b37b02dac07d86ebf1350f8624cbf40b52cb2d3` |
