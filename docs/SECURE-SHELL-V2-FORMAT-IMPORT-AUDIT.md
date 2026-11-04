<!-- Planning artifact; source snapshot: GitHub main branches inspected 2026-11-04. This is a scoped source audit, not a complete byte-level scan. -->

# Secure Shell v2 — format, importer, and project-wide source audit

**Audit basis:** GitHub integration reads of `alacripose/secure-shell`, `alacripose/dl-openshell`, `alacripose/swf-cell-runtime`, `alacripose/ala_civ_bots_prototype`, and `alacripose/ala-cities`, current through 2026-11-04 where repository commits are available.

**Status:** Planning audit and migration diagnosis, not an exhaustive byte-level census of every source file. A reproducible repo-wide scanner and format-owner review remain M1 deliverables. Findings below distinguish confirmed repository facts from target recommendations.

## 1. Executive findings

1. The requested Secure Shell audit exists: [`docs/FORMAT-SOURCES-AUDIT.md`](https://github.com/alacripose/secure-shell/blob/main/docs/FORMAT-SOURCES-AUDIT.md), approximately 1,180 lines on the inspected `main` branch. It already records the multi-project format census, MongoDB history, OpenLock drift, importer/API gaps, envelope shortcomings, and older `planet-*` package family.
2. Current Secure Shell rules explicitly exclude MongoDB and new package formats. The existing system describes a Debian backend, SHA-256 chained activity ledger, Ed25519 checkpoints, AES-256-GCM prompt vault, `secure-shell.ingest/1`, `surface.mount/2`, and additive `secure-shell.served/1` records. The README says MongoDB is not implemented; `AGENTS.md` forbids adding a second store or signature scheme without a recorded decision.
3. The SWF importer remains directly dependent on `planet-*`. Its `Cargo.toml` imports `planet-aead`, `planet-package`, and `planet-shell-ledger`, with `planet-client` in dev dependencies. `planet-package` owns `V4PKG001`. A computed hashed identifier was added around a family name, but the frame still carries the numeric schema field and old framing contract.
4. Newer SWF decisions say `planet-shploingus` is not authoritative for the shell family. It is evidence about old readers and migration hazards. The importer can teach Secure Shell about declared cells, asset carriage, cadence, truncation, and source-safe measurement without requiring v2 to inherit `planet-*` crates.
5. CRLF/LF is a byte-identity and reproducible-build issue, not a package schema. SWF tickets 0068/0069 show selftest identity changing when checkout line endings change. The inspected `.gitattributes` pins selected paths to LF; a complete project-wide scan is still needed for all tracked text and byte-sensitive files.
6. OpenLock's optional package envelope is not a production signature proof. The audit reports committed envelope rows as unsigned with empty digest/key/signature/work information; the generator reads the envelope, but the client renderer does not verify it. Server-side admission must own verification; UI only presents the result.
7. The audited `planet-mcp` surface has 17 verbs, only one write verb, 10 of 17 tool schemas with empty `properties`, and no tool that accepts/builds a declaration document. V2 agent API needs typed documents and bounded operations, not only paths into a confined package directory.
8. The civilian architecture has a meaningful specification and partial implementation, but it is not yet a completed trained cellular-generative System-1 CUA. The rechecked spec says no NCA/evolutionary-CA substrate was found in the inspected prototype; persistent identity, mind, memory, practice and some CUA/body controls exist, with substantial lived-life and parity proof still open.

## 2. Repository and source status

| Repository | Inspected evidence | Relevance | Important limitation |
|---|---|---|---|
| [`alacripose/secure-shell`](https://github.com/alacripose/secure-shell) | `AGENTS.md`, `README.md`, `docs/ARCHITECTURE.md`, `docs/DECISIONS.md`, `docs/SELECTIONS.md`, `docs/PLAN.md`, `docs/FORMAT-SOURCES-AUDIT.md`, baselines and patch inventory | Debian server, ledger, served package, first shell client | Current no-Mongo/no-new-format rules conflict with requested v2 direction |
| [`alacripose/dl-openshell`](https://github.com/alacripose/dl-openshell) | `AGENTS.md`, README, root tree, manifest and source references from audit | OpenLock window manager, taskbar, delivery, XML, generators and theme | Game/Panorama context and historical format drift; do not copy every runtime/package format |
| [`alacripose/swf-cell-runtime`](https://github.com/alacripose/swf-cell-runtime) | Current AGENTS, docs, tickets, package ownership, format decisions, importer manifests, newline tickets and health workflow | Cellular, importer, package and evidence lessons | Current implementation still uses `planet-*` for actual package ownership |
| [`alacripose/ala_civ_bots_prototype`](https://github.com/alacripose/ala_civ_bots_prototype) | README, `AGENTS_DO_NOT_IGNORE.txt`, `CONTEXT.md`, `CHECKPOINT.md`, recent commits | Persistent identity, System-1, body adapters, work and action control | Does not establish full cellular-generative CUA learning or complete civic institutions |
| [`alacripose/ala-cities`](https://github.com/alacripose/ala-cities) | `AGENTS.md`, design/unified-design docs and institutional design inventory | Institutions, work, courts, learning trees and governance | Design documents alone do not prove implemented behavior |

Inspected main-branch recency: Secure Shell latest visible main commit 2026-10-31; OpenLock 2026-10-30; civilian prototype 2026-11-02; SWF runtime latest visible commits include TICKET-0091 on 2026-11-04. This is a branch snapshot, not proof that no unmerged branches or working-tree changes exist.

## 3. Secure Shell audit — confirmed facts

### 3.1 Existing architecture and formats

- `docs/ARCHITECTURE.md` assigns the Debian backend package stream, server records, ledger/events and security verdict; the client owns the native forked OpenLock display.
- The decision table records `dl-enclave.surface/1` as the window declaration and `surface.mount/2` as the receipt. `secure-shell.served/1` is an additive served representation, not a third window schema.
- `secure-shell.ingest/1` is server accept-only and should not become a client-readable window format.
- `surface.mount/2` describes a mount/push receipt; the planned served record carries window records, content tree and evidence rows.
- Existing package/ledger code and tests are Node ESM. README describes SHA-256 chaining, idempotent operation IDs, stale-sequence refusal, fsync, Ed25519 checkpoint, AES-256-GCM prompt vault, and HTTP/SSE with bearer-token/loopback defaults. README states MongoDB is absent.
- `AGENTS.md` excludes key material and secrets from the repository. The shell may verify integrity, but does not issue signer/trust-root/security verdicts.

### 3.2 OpenLock display selection

Secure Shell conventions select a fork of OpenLock's `openlock_shell.js` and taskbar/display path as the display owner. Relevant source inputs include:

- `clientaddon/panorama/layout/openlock_shell.xml`;
- `clientaddon/panorama/scripts/openlock_shell.js`;
- `clientaddon/panorama/scripts/openlock_delivery.js`;
- OpenLock generation tools and shell declaration files;
- landing-page addon theme assets and `openlock.manifest.json`.

The actual source is expected to be used by a generator with a recorded file selection. A second display implementation, second renderer, or unowned display contract is a known risk. Secure Shell `docs/SELECTIONS.md` leaves the mounted-set-to-window contract open; the Qt client must close it before implementation.

### 3.3 API/MCP deficiency

Audit §3A reports `planet-mcp` with 17 verbs, one write verb (`present_package`), 10 of 17 tools declaring empty `properties`, and no authoring verb accepting a document. Package-build capability exists as a CLI, not a typed MCP authoring surface. V2 should expose structured input/output schemas and bounded operations; it should not solve this by handing agents unrestricted filesystem access.

## 4. MongoDB — what exists and what does not

### 4.1 OpenLock's axis-witness store

The Secure Shell audit describes `openlock_axis` as a local MongoDB comparison store used by `tools/axis_witness.py`. The useful pattern is write → read back → independently re-derive, with a named `mongodb_unavailable` blocked state. The same audit notes serious gaps in that helper: local development ports, unauthenticated store, no encryption at rest, no collection indexes identified in the inspected tools, and no production service/backup policy.

**Reuse:** three-reading verification discipline, named unavailability state, and comparison role.

**Do not reuse:** local development authentication/storage model as the Debian production database.

### 4.2 `dl-enclave` MongoDB plan vs implementation

Audit §3D says `dl-enclave` documented MongoDB as canonical record but did not add MongoDB imports, connection URI, or driver in the inspected implementation. Its visible shell/mount work proceeded without the store. The audit also identifies unresolved licensing/redistribution questions for bundling MongoDB Community in an appliance.

**Conclusion:** MongoDB in a plan is not a running MongoDB service. V2 needs actual schema, writer, service, backup and restore proof before claiming to be Mongo-backed. Packaging/license review is an explicit task.

### 4.3 Secure Shell conflict

Current Secure Shell `docs/ARCHITECTURE.md`, `docs/DECISIONS.md`, `docs/PLAN.md`, and `AGENTS.md` explicitly select Debian plus append-only files and reject MongoDB. This needs an owner-recorded superseding ruling, not a hidden driver addition.

## 5. SWF importer — legacy dependency lock

### 5.1 Current dependency graph

Inspected `crates/swf-import/Cargo.toml`:

```toml
[dependencies]
planet-aead = { path = "../planet-aead" }
planet-package = { path = "../planet-package" }
planet-shell-ledger = { path = "../planet-shell-ledger" }
flate2 = "1"

[dev-dependencies]
planet-client = { path = "../planet-client" }
```

TICKET-0035 documents that the importer emits a `dl-enclave.surface/1` declaration, validates it with `planet_package::Surface::parse`, then frames it as `V4PKG001`. It is directly compiled against the old package family and mount stack; this is not just a crate-name cosmetic problem.

### 5.2 Why the hashed identifier work is not yet migration

TICKET-0066 changes a declaration identifier to `planet.surface/<32 hex>` and makes numeric identifiers legacy/read-only on emission. The ticket itself says the `V4PKG001` header still carries `schema: u16`; replacing that field and digest preimage needs a separate reader/erratum. A hashed family ID does not mean the old package frame has been replaced.

TICKET-0037 registers 129 numeric historical IDs in `config/legacy-formats.json` so code cannot emit unregistered numeric tokens. That registry is classification/provenance bookkeeping; it does not rewrite packages, remove readers, or implement the new Secure Shell package service.

TICKET-0062 adds sealed JSONL importer rows using `planet_aead` and `PLANET_STREAM_KEY`. It flushes rows and refuses truncated streams, but its own text says the tag walk is already materialised and it adds no store writer. This is valuable failure evidence, not the target transport.

### 5.3 Migration rule

Do not merely rename `planet-package` to `secure-shell-package`. Replace the ownership boundary:

1. Specify a new Secure Shell package frame, digest domains, signature, schema IDs and compatibility rules.
2. Implement its canonical reader/writer and conformance fixtures in the Secure Shell family.
3. Keep old planet-format reading in a quarantined, read-only legacy adapter.
4. Convert only through an explicit migration recording source/target format, before/after digests, unknown/lost fields, actor and ticket.
5. Emit new packages only in the new family.
6. Remove `planet-*` runtime dependencies once the new format runs end-to-end and legacy inputs are handled by the isolated adapter.

The `planet-*` projects remain source evidence, not Secure Shell v2 authority. SWF `docs/DECISIONS-PORT.md` explicitly records that `planet-shploingus` is not authoritative for the shell family.

## 6. SWF cellular/importer lessons worth retaining

- **One owner per format.** Importer measures or lowers only according to a declared owner format; it must not invent convenient output grammar.
- **A cell is a declared display unit over data, not a fixed raster grid.** SWF decisions reject importing a particular 8×16 paper/ink raster as the definition of a cell. Preserve typed fields, bindings, shapers, projections, ordering and dependencies.
- **Media is typed.** Bitmap, font and audio need explicit kind/ownership, not raw untyped bytes.
- **Cell programs are bounded.** The SWF decision describes deterministic instruction execution with budgets, cancellation and capabilities, without host/filesystem/network/native-code escape hatches.
- **Streaming is a layer over canonical package bytes.** It must not become a second package family, store or content schema.
- **Truncation is explicit.** Incomplete output is named and refused; completion is not inferred from partial output.
- **Source-safe import.** SWF source stays behind its trust boundary; source names, identifiers, offsets, payload bytes and raw media do not leak into tracked artifacts.
- **Proposals are not rules.** SWF health tooling proposes changes to `AGENTS.md`; a ticket and owner acceptance must land the rule.
- **Health is a ratchet.** Each unit has a health report; checks once held cannot silently regress.

## 7. Line endings, serialization, and byte identity

### 7.1 What the SWF records establish

TICKET-0068 records a selftest identity computed over LF-written files, followed by checkout materialization as CRLF due to `core.autocrlf`, changing exact bytes. Regenerating the test record after checkout fixed the immediate state, not portability. TICKET-0069 disables `core.autocrlf` locally and identifies a portable `.gitattributes` rule as the durable next step. The inspected `.gitattributes` pins selected paths (`AGENTS.md`, `.gitignore`, `.github`, `config`, `docs`, `ledger`, `patches`, `tickets`, `tools`) to LF.

This establishes a reproducibility hazard; it does not establish that LF or CRLF is a package format version. A newline policy is a text-file checkout property. A package schema is a byte grammar and semantic contract.

### 7.2 Proposed v2 byte policy

- **Text source/docs:** UTF-8, one declared repository newline policy, no mixed endings; `.gitattributes` must make checkouts reproducible.
- **Structured records:** deterministic field ordering, number/string encoding, and explicit serializer version; newline framing is specified separately.
- **Binary package objects:** preserve exact bytes; never run text newline conversion; hash after canonical serialization and before transport.
- **Signed manifest:** canonical encoding and domain-separated signature input; verifier must not parse and reserialize with different rules.
- **Generated artifacts:** generator/version/input identity recorded; identity report written after checkout/materialization if checkout can mutate bytes.
- **Migration:** newline normalization is a repository/text migration; schema migration is a separate operation with source/target versions, separate tests and ledger entry.

The repo-wide scan must classify every tracked file as text, binary, generated, source-derived/private, or deterministic structured data. Detect BOM, invalid UTF-8, CRLF/LF/mixed endings, missing final newline where relevant, git filters, `core.autocrlf`, generator identity and all hash/signature preimages. Do not globally rewrite bytes without a baseline/review; that changes digests and signatures.

## 8. OpenLock envelope observations

Secure Shell audit §3I says OpenLock's optional envelope declares digest, authority, work, nonce, algorithm, key and signature. It reports four committed envelope records as unsigned, with zero work and empty digest/key/authority/signature values. The generator reads the envelope before use and can name refusals, but the client shell/C# plugin do not verify it. The existing mechanism uses HMAC-SHA256 and a leading-zero nonce proof, not the requested BLAKE3 content digest plus a separate portable public-key signature.

**Keep:** fail-closed named refusals, owner-held keys outside checkout, signature verification before presenting untrusted data, and visible wishes/refusal state.

**Replace:** optional unsigned acceptance as production default, renderer-owned trust, nonce work as package identity, and any in-band trust claim treated as a verdict.

## 9. Qt XML fact boundary

SWF ticket 0041 implements a small XML window reader in `planet-client`, with allowlisted `window` declarations and named refusals. Its own documentation distinguishes it from the Qt reader, which belongs to Secure Shell v2 and is not implemented in SWF. Do not cite that test XML parser as a completed Qt client.

The civilian expectations require XML to remain declarative: it can describe UI and issue typed authorized requests, but cannot call a motor, alter cognition, add verbs, grant capabilities, execute arbitrary scripts or certify itself. Enforce parser budgets at the real package reader.

## 10. Civilian model reality check

The current prototype/rechecked expectations establish stable identity and one mind decision owner; journal/snapshot recovery and practice history; needs, beliefs, intentions, reflexes, ticketed skill routines and body adapters; a System-1 sense/select/gate/act/verify progression; and some ordinary-life work/rest/social-transfer/reconnect cases.

They do **not** establish a completed trained cellular-generative CUA policy. The rechecked document explicitly says no NCA/evolutionary-CA substrate was found in the inspected prototype; its local Axis authority gateway was provisional; complete post-test autonomous life and broad relationship/commitment continuity remained open; and full native client parity was not proved. Treat the cellular/System-1 integration as new implementation work, not an already solved feature.

## 11. Project-wide audit procedure still required

M1 should add a repeatable tool/report that inventories:

1. Repository commit and branch identity.
2. Format tokens, version suffixes, headers/magic, digest domains, serializers and signatures.
3. Reader/writer/declaration owner for each family; duplicate readers and shadow stores.
4. Dependency graph: importer → package → store → stream → client.
5. Legacy registry and emit/refuse gate.
6. Pre/post-split schema crosswalk and migration coverage.
7. Line endings and canonical-byte report for every tracked file category.
8. Generated file provenance and clean regeneration proof.
9. MCP/API tool inventory, JSON Schema completeness, permissions and document authoring support.
10. CUA action catalogue, ticket/authority binding and postcondition evidence.
11. Civilian identity/continuity/cellular learning/workday coverage and explicit absent entries.
12. Threat review: package traversal, signature/key handling, stale/replay packages, BSON injection, decompression bombs, parser/resource limits, bearer/session leakage, server restore and client trust boundary.

The audit output is source-derived report plus machine-readable inventory, not an agent-generated declaration of what the repository must mean.

## 12. Key references

- Secure Shell audit: https://github.com/alacripose/secure-shell/blob/main/docs/FORMAT-SOURCES-AUDIT.md
- Secure Shell decisions: https://github.com/alacripose/secure-shell/blob/main/docs/DECISIONS.md
- Secure Shell architecture: https://github.com/alacripose/secure-shell/blob/main/docs/ARCHITECTURE.md
- SWF importer manifest: https://github.com/alacripose/swf-cell-runtime/blob/main/crates/swf-import/Cargo.toml
- SWF legacy-format ticket: https://github.com/alacripose/swf-cell-runtime/blob/main/tickets/TICKET-0037-legacy-formats.md
- SWF importer streaming ticket: https://github.com/alacripose/swf-cell-runtime/blob/main/tickets/TICKET-0062-importer-stream.md
- SWF format-family ticket: https://github.com/alacripose/swf-cell-runtime/blob/main/tickets/TICKET-0066-format-family.md
- SWF line-ending tickets: https://github.com/alacripose/swf-cell-runtime/blob/main/tickets/TICKET-0068-record-line-endings.md and https://github.com/alacripose/swf-cell-runtime/blob/main/tickets/TICKET-0069-lf-working-tree.md
- SWF package ownership: https://github.com/alacripose/swf-cell-runtime/blob/main/docs/PACKAGE-OWNERSHIP.md
- SWF port decisions: https://github.com/alacripose/swf-cell-runtime/blob/main/docs/DECISIONS-PORT.md
- Civilian expectations: https://github.com/alacripose/swf-cell-runtime/blob/main/docs/cellular_generativity_axis_civilian_expectations_prototype_rechecked.md
- OpenLock: https://github.com/alacripose/dl-openshell
- Civilians: https://github.com/alacripose/ala_civ_bots_prototype
- Cities: https://github.com/alacripose/ala-cities
