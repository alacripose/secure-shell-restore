<!-- Planning artifact; source snapshot: GitHub main branches inspected 2026-11-04. No repository was modified and no implementation test is claimed. -->

# Secure Shell v2 — implementation plan and owner decisions

**Status:** Proposed, evidence-based sequence. This document is intended to become the successor to the current `docs/PLAN.md` only after its step grammar, version tokens, and exit-test reader are agreed. It does not silently supersede the current plan.

**Goal:** Generate the initial shell from OpenLock, place its first usable window in the Debian-backed store, serve it through a versioned BLAKE3-addressed and public-key-signed package stream, and operate/verify it with an Axis-governed System-1 CUA driver. Then migrate the SWF importer away from the legacy `planet-*` dependency family while retaining the cellular and evidence workflow. Finally, exercise a full workday through persistent civilians and a real Qt client.

## 1. Execution discipline

Current Secure Shell conventions are project rules: external owner-only prompt/activity ledger, no commit without ledger entry, recorded user decisions, one display implementation, one window at a time, and a client-visible witness. The proposed v2 direction conflicts with current no-MongoDB/no-new-format rules; it must be entered as a superseding owner decision before implementation starts.

Adopt the SWF project's stronger workflow as a v2 proposal:

1. Every contract, defect and implementation unit receives a ticket.
2. One ticket → one branch → small coherent commits → PR; no giant untracked session or squash erasing evidence.
3. Every commit names its ticket and activity-ledger event.
4. Each command that can refuse prints a machine-readable result and exits non-zero. A silent failure is a tool defect.
5. Each unit changes a named artifact and has an executable exit test. “Analysis complete”, `git status`, `git diff`, or a screenshot alone is not a completed unit.
6. Run the health ratchet each test turn. A previously held check may not regress; a new failure becomes owned evidence debt, not a pass.
7. Automatically generated proposals do not become rules automatically. A proposal becomes an `AGENTS.md` rule only after ticket, owner decision, implementation, and acceptance test.
8. Project artifacts stay under the checkout. Secrets and user prompts stay outside git in owner-controlled storage.
9. Enforce the current family commit budget of at most 40 files or 4,000 insertions per commit unless the user revises it.
10. A bot/CUA report is not a client witness. Actual Qt client rendering and operation must be witnessed on the user-facing shell.

## 2. Proposed milestone sequence

The order is deliberate: generate the shell from OpenLock before improvising a new renderer; define the package/store owner before building the stream; make CUA operate the first window before asking it to perform migrations/recovery; migrate SWF only after the new package and stream owners exist.

| Milestone | Work | Required artifacts | Exit condition |
|---|---|---|---|
| M0 — Authority and version ruling | Resolve conflict with current Secure Shell rules; record Mongo, format, naming, Qt, signature, stream and compatibility decisions | `docs/DECISIONS.md`, version matrix, proposal ticket | No implementation relies on unresolved store/format/identity owner |
| M1 — Project-wide source audit | Re-audit Secure Shell, OpenLock, SWF runtime, civilian prototype, ala-cities, generated files and byte/newline identity | `docs/SECURE-SHELL-V2-FORMAT-IMPORT-AUDIT.md` | Each format has one owner, reader/writer, current version, migration policy and evidence |
| M2 — OpenLock shell generation | Generate initial shell package from selected OpenLock XML/JS/declarations/theme; preserve generator provenance | Generator, source-selection record, generated declaration, baseline | Clean regeneration is reproducible; no hand-edited generated output |
| M3 — First-window baseline | Define one useful bootstrap/operations window, tokens, content, layout, accessibility and refusal states | `baselines/v2-shell-window.*`, one window declaration | Source-generated window renders in actual Qt client and has a witness |
| M4 — Package/naming contract | Name package family, canonical serialization, schema version, package ID, hash preimage, signature envelope and compatibility | Format ADR, schema, conformance fixtures, version map | Independent reader/writer agree; tamper, old/new and ambiguous-version cases refuse by name |
| M5 — Debian MongoDB store | Build Debian service, Mongo authority model, immutable package objects, retention, backups, transactions and activity integration | Store service, schema/index migrations, backup/restore procedure | Restart, duplicate-operation, crash recovery, restore and consistency tests pass |
| M6 — Signed streamer | Implement bounded chunks, resume, BLAKE3, signature verification, ordered completion and atomic adoption | Stream protocol, signer/verifier service, client receiver | Package streams Debian→client; tampered, truncated, stale, replayed and wrong-version fixtures refuse |
| M7 — Qt declarative client | Implement one bounded XML reader and rendering path; map OpenLock-generated shell declarations | Qt client, XML schema, parser conformance suite | First server-stored window appears/behaves in user-facing client; no browser-only pass |
| M8 — Axis System-1 CUA bootstrap | Safe inspection, presentation, health, mount and recovery operations | Axis CUA component, action catalogue, tickets, operation records | Every operation ticketed, bounded, idempotent, acknowledged, postcondition-verified and client-visible |
| M9 — Agent API/templates | Publish scoped API/MCP manifest; generate thin per-task client templates from internal store | API catalogue, JSON schemas, generated TS/Python templates | Agent can inspect/stream one declared surface without mounting every desktop component or seeing secrets |
| M10 — SWF importer migration | Replace `planet-*` frame/store dependencies with new owners; preserve SWF source boundary | `secure-shell-swf-import`, legacy registry, migration tests | Import→canonical package→signed stream→Qt render works without `planet-*` runtime dependency |
| M11 — Civilian cellular System-1 validation | Integrate agent-owned cell state, stable identity, learning, work, social coordination, institutions and courts under Axis | Civilian adapter, cell contract, cadence/workday suite | Same residents complete a declared workday across restart/interruption and resume ordinary life |
| M12 — Cross-host parity/release | Rebuild from clean clone and compare Debian store, Qt client, CUA, API templates and fixtures | Release baseline, compatibility report, rollback package | Second host reproduces package identity, stream result and client witness; rollback restores prior revision |

## 3. Detailed unit order

### M0 — Record owner decisions

- Create a superseding decision identifying the current restrictions being changed: no MongoDB, no new package format, existing `surface.mount/2`, file-backed activity log, and current SHA-256/Ed25519 division.
- Record which rules remain binding: one reader per format, user-owned names, one display, client as witness, external prompt vault, no secrets in git, and refusal-by-name.
- Assign separate owners for package format, store, signing, stream, Qt declaration, CUA action catalogue and civilian state.
- Do not start with a broad rewrite. Create a ticket chain for one window and one end-to-end package.

### M1 — Audit the whole family, not only SWF

Audit these checkouts at pinned commits:

- `alacripose/secure-shell`: `AGENTS.md`, `docs/ARCHITECTURE.md`, `docs/DECISIONS.md`, `docs/SELECTIONS.md`, `docs/PLAN.md`, `docs/FORMAT-SOURCES-AUDIT.md`, `server/`, `packages/`, `shell/`, `tools/`, generated assets.
- `alacripose/dl-openshell`: OpenLock layout, display and delivery scripts, declarations, generator tools, landing theme, manifest, installer/package reader, and dirty/uncommitted state where accessible.
- `alacripose/swf-cell-runtime`: `AGENTS.md`, `docs/PACKAGE-OWNERSHIP.md`, `docs/DECISIONS-PORT.md`, `docs/CELL-SCHEMA.md`, `docs/CELL-TRANSPORT-DECISION.md`, `docs/AGENTS-PROPOSALS-2026-11-04.md`, importer crates, tickets 0035/0037/0062/0066/0068/0069 and latest health reports.
- `alacripose/ala_civ_bots_prototype`: `AGENTS_DO_NOT_IGNORE.txt`, `CONTEXT.md`, architecture, current checkpoint, continuity/work-ledger implementation, runtime/version constraints.
- `alacripose/ala-cities`: `AGENTS.md`, design/unified-design docs, institutional, organization, court, economy, work and learning-tree owners.

Record exact branch, commit SHA, file, format token, version, owner, writer, reader, serializer, newline handling, hash domain, compatibility and evidence. Unknowns remain `absent` with a named lookup; they are not silently counted complete.

### M2–M3 — Generate and witness first OpenLock-derived shell

1. Identify the actual OpenLock shell implementation and package/data generators. Do not start from a screenshot or manually coded Qt mock.
2. Write a source-selection record: exact files/symbols, selected and rejected content, known defects, rejected alternatives and parity evidence.
3. Run the existing generator path first; capture source revision, generator revision, tool versions and output digest.
4. Add only the minimal Qt lowering required for the first window. Keep OpenLock-specific parsing at the migration boundary; the canonical Qt renderer consumes the new package contract, not a second OpenLock store.
5. Store that single package revision on Debian. The Qt client fetches it and presents it in a real shell window.
6. Capture declaration, 1440×900 and 1024×768 frames, resolved token set, package digest, client version and actual interaction results.
7. Do not begin a second window until the first passes the client witness and ledger check.

The first operations surface should show store/stream health and explicit refusal states. Exact window name/content is user-owned. Axis is a content lane, not a floating frame.

### M4–M6 — Replace legacy package foundation

Write the new package spec before code. Separate schema identity from package content identity. BLAKE3 is the proposed content digest, with a domain-separated preimage over exact canonical bytes and framing metadata. A public-key algorithm signs the canonical manifest; it is a separate choice. Key management, rotation and revocation must be specified before production signature claims.

The stream moves canonical package bytes and signed manifest records; it does not define a second window format. Specify:

- ordering, chunk size and maximum package length;
- duplicate/replay handling and idempotency;
- resume-token scope and expiry;
- manifest and chunk digest domains;
- finalization and partial/truncated refusal;
- schema/version refusal rather than automatic conversion;
- mount/adoption receipt proving exactly one revision was applied;
- old-revision retention and rollback.

Implement MongoDB as a single-writer canonical service initially unless replica/failover is selected. Provide authentication, encryption at rest/volume, least privilege, backups and restore drills, schema migration, transaction boundaries, unique operation IDs and failure injection. Package objects and metadata must have one authoritative write path; a second sidecar database is refused.

### M7–M9 — CUA client and small agent APIs

Start with read-only inspection, not arbitrary shell control. The first CUA slice observes the real window and server revision, retrieves the manifest, verifies the package and reports exact state. Then add bounded launch/present/mount/health/recovery verbs by ticket.

Every API method has a complete JSON Schema: required fields, `additionalProperties: false`, bounds, semantic validation, authentication scope, version negotiation, typed refusals, idempotency, pagination/streaming and output limits. No `properties: {}` placeholder. A tool does not accept an arbitrary filesystem path where a package document or typed record is required. Generate a small internal-store template with only the schemas/examples/client calls required for a task. Agents do not need to mount the entire desktop to call a service API.

### M10 — Free the importer from `planet-*`

The inspected `crates/swf-import/Cargo.toml` imports `planet-aead`, `planet-package`, `planet-shell-ledger`; tests also import `planet-client`. Its writer uses the `V4PKG001` package family through `planet-package`. That is the dependency to remove, not merely a crate prefix to rename.

Before removing it:

- preserve measured behavior and named refusals as conformance fixtures;
- map every legacy family/id to its source, old reader, migration reader and target schema;
- quarantine legacy readers as read-only compatibility adapters with a sunset policy;
- emit new packages only in the new Secure Shell family;
- record each legacy conversion with source/target format, before/after digest, unknown/lost fields, actor and ticket;
- never rewrite an old package in place or silently assign it new meaning;
- remove `planet-*` runtime dependencies only after legacy fixtures are readable through the adapter and new packages pass the canonical client path.

Retain SWF cellular, importer, asset-carry, cadence, truncation and health lessons. Do not inherit the old format just because the current importer uses it. Preserve SWF source-access authorization and no-source-identifier/byte leakage rules.

### M11 — Civilian workday and shell-recovery training

The civilian model is not a task scheduler that puppets residents. Each resident owns stable identity, mind, memory, intentions, work commitments, cellular-generative state, practice history and relationships. It may adapt its own local cell state within a bounded learning envelope. It cannot self-grant tools, install a model, alter shared action schemas, sign packages or overrule Axis.

The six-star Axis scale includes a lived-civilian verification star. It exercises authoritative cadence and resident-controlled adaptation. It must not manufacture jobs, institutions, judges, legal findings or social outcomes on residents' behalf. `ala-cities` provides institutional vocabulary/architecture to audit, but each feature claim must be checked against implementing code.

The shell training campaign must cover:

- clean boot from Debian store;
- interrupted package download and resume;
- bad chunk digest, bad signature, unknown signer, expired/revoked key;
- old/new schema refusal, explicit migration and rollback;
- pre-split/post-split records and corrupt/partial records;
- Qt client crash/reconnect with same shell/session identity;
- store/stream outage, stale client revision and backup restore;
- API rate/permission boundaries and malformed tool arguments;
- CUA timeout, duplicate command, expired ticket, denied permission and incorrect postcondition;
- realistic day-long work queue of independent tasks;
- civilian rest, help-seeking, learning, coordination, post-test ordinary life and restart continuity.

### M12 — Cross-host parity and release

Use a clean second Debian/client host. Rebuild from pinned source, retrieve the same package, verify manifest/content digests, signer key/policy, client surface checks and witness replay. Test rollback to last known-good revision. A green local build alone is not release parity.

## 4. Proposed daily acceptance contract

The exact meaning of “a day's worth” is owner question 20. Until answered, use a **logical workday** composed of a declared cadence schedule rather than assuming a 24-hour wall-clock run. It must include ordinary work, breaks/rest, interruption, restart/recovery and more than one task class.

A workday passes only if:

- the same agent identity is active from start through finalization;
- every task has declared input, owner, expected state, time window and exit test;
- CUA observes/diagnoses before acting and executes only admitted operations;
- completions are verified from authoritative server/client postconditions, not model self-report;
- no task is silently skipped, duplicated, widened in scope or completed without evidence;
- incomplete, refused, timed-out and recovered work remains visible;
- streams, tool calls, mounts and client actions have sequence/operation identity and durable records;
- at least one injected interruption and recovery occurs without history loss;
- pre/post split data use exact readers, with explicit migration lineage;
- restore/rollback leaves prior revision available;
- test completion releases only test-owned resources and returns residents to ordinary autonomous life;
- a real client witness confirms first shell window and a meaningful CUA operation.

Only the shell gate assigns `held`, `absent`, or `refused`. Agents may report implementation facts such as present, not implemented or blocked. A CUA report does not assign the gate state.

## 5. Versioning/naming deliverable

Before M4, publish one version matrix:

| Component | Independent version? | Compatibility rule | Upgrade owner |
|---|---|---|---|
| Shell product release | Yes | Coordinates pinned component set | Release owner |
| Package schema | Yes | Exact reader; old/new refuse or explicit migration | Format owner |
| Stream protocol | Yes | Resume/apply semantics negotiated | Stream owner |
| Qt surface schema | Yes | Strict declaration reader | Client/format owner |
| CUA action catalogue | Yes | Closed verbs, explicit adapter compatibility | CUA owner |
| Axis policy/rule set | Yes | Policy revision cited per action | Axis owner |
| Agent API/MCP tools | Yes | JSON schema and tool version negotiation | API owner |
| SWF importer | Yes | Adapter version maps source to target package | Import owner |
| Civilian cellular model | Yes | Migration preserves AgentId and personal state | Civilian owner |

No filename, tag, crate, schema ID or package ID is final solely because it appears in this proposal. Owner naming decision remains open.

## 6. Twenty owner questions — midpoint decision gate

The twenty questions were also shown in the conversation in an editable worksheet. Unanswered items remain open; the plan does not infer answers.

1. **Identity/naming:** retain `secure-shell` repository identity while independently versioning shell record, package stream, server API and CUA driver?
2. **Version scheme:** one coordinated release version or independent major versions for interdependent components?
3. **MongoDB authority:** MongoDB canonical for server record and activity ledger, or package/catalogue store with append-only ledger retained as event authority?
4. **MongoDB topology:** single Debian-hosted instance initially, or replica set/failover from first implementation?
5. **Persistence/security:** encrypted storage, authenticated service identities, append-only event permissions and verified backups as mandatory admission conditions?
6. **Package integrity:** BLAKE3 for content identity with separate public-key signature suite; which signature algorithm?
7. **Signing authority:** Debian server, separate signing service, or user-controlled delegated authority?
8. **Stream contract:** replace `surface.mount/2`, or carry a mount receipt as separately versioned subordinate contract?
9. **OpenLock generation:** should first deliverable be agent-generated from OpenLock's actual source, declarations and generators before adding a desktop framework? This plan assumes yes because that is the requested starting point.
10. **Display format:** Qt Widgets with XML-defined UI, Qt Quick/QML, or another Qt XML model?
11. **Display ownership:** Debian transmits declarations/content only; local desktop owns rendering, focus and input?
12. **SWF boundary:** keep SWF as version-isolated import adapter behind new streamer API?
13. **Planet migration:** remove all `planet-*` runtime dependencies, or retain quarantined legacy decoder during transition?
14. **Legacy handling:** migrate old packages to explicit compatibility objects, or keep immutable and stream through version-specific readers?
15. **Split formats:** which exact pre-split/post-split families require separate schema IDs and readers?
16. **Text normalization:** UTF-8 plus declared source newline policy and canonical semantic/binary serialization for signed bytes? “New formats instead of CRLF or LF” needs exact interpretation: line endings are text materialization, not schema versions.
17. **CUA responsibilities:** should Axis CUA own boot, recovery, health, format detection, mount and pre/post-migration verification, with every action ticketed/witnessed?
18. **Agent API:** publish generated small API template and capability-scoped tool manifest from internal store without mounting all shell components?
19. **Civilian verification:** workday should exercise autonomous work, learning trees, courts, organisations, interruption and recovery?
20. **Daily acceptance:** 24-hour continuous simulation, compressed one-day cadence schedule, or a defined verified task quota?

## 7. Source register

- Secure Shell plan: https://github.com/alacripose/secure-shell/blob/main/docs/PLAN.md
- Secure Shell audit: https://github.com/alacripose/secure-shell/blob/main/docs/FORMAT-SOURCES-AUDIT.md
- Secure Shell rules: https://github.com/alacripose/secure-shell/blob/main/AGENTS.md
- SWF rules: https://github.com/alacripose/swf-cell-runtime/blob/main/AGENTS.md
- SWF civilian expectations: https://github.com/alacripose/swf-cell-runtime/blob/main/docs/cellular_generativity_axis_civilian_expectations_prototype_rechecked.md
- SWF decisions: https://github.com/alacripose/swf-cell-runtime/blob/main/docs/DECISIONS-PORT.md
- OpenLock: https://github.com/alacripose/dl-openshell
- Civilian prototype: https://github.com/alacripose/ala_civ_bots_prototype
- City systems: https://github.com/alacripose/ala-cities
- User transcript: `The Rapid Progress of Realtime Simulations_AI(3).txt`.
