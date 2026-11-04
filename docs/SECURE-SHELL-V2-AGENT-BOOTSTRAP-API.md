<!-- Planning artifact; source snapshot: GitHub main branches inspected 2026-11-04. No repository was modified and no implementation test is claimed. -->

# Secure Shell v2 — agent bootstrap, proposals, API tooling, and internal templates

**Status:** Proposed operating contract for agent-assisted development and runtime operations. It combines the SWF runtime's ticket/branch/ledger/health-ratchet workflow with Secure Shell's prompt-ledger and user-surface requirements. It does not authorize automatic changes to `AGENTS.md` or any trust boundary.

## 1. Project bootstrap sequence

The project setup must establish environment, authority and evidence before an agent implements product code.

### 1.1 Clone and identify

1. Clone `alacripose/secure-shell` into a known project-local directory.
2. Record repository URL, remote, branch, commit SHA, clean/dirty status, submodules and worktrees.
3. Confirm the Debian target, Qt toolchain, Rust/Node/Python versions and dependency-manager versions from manifests/lockfiles. Do not guess or silently upgrade.
4. Read root `AGENTS.md`, then linked authority documents: `docs/DECISIONS.md`, `docs/LEDGER.md`, `docs/ARCHITECTURE.md`, and current machine-readable plan. Record conflicts before editing.
5. Install hooks, formatters, linters and test entry points using repository-owned scripts; do not replace pinned project tools with unpinned global installations.

### 1.2 Open the activity and authority record

- Initialize the owner-only external prompt vault and append-only activity ledger before the first edit, using existing Secure Shell policy until the user explicitly supersedes it.
- Classify every instruction source: user, project file, mission/planner, system/developer, agent, retrieved file or repository content. Only an actual user instruction is user authority.
- Never put full prompts, tokens, signing keys, database passwords or connection strings in git, package metadata, ordinary logs or screenshots.
- Record conflicts between current `AGENTS.md` and new Mongo/format/Qt direction as a proposed superseding decision. Do not reinterpret old rules silently.
- Each implementation unit gets a ticket before editing, an activity row after evidence-producing commands, and a small commit/PR. Ledger unavailable blocks edits/commits according to governing policy.

### 1.3 Project map before code

Generate and version a small navigation map containing:

- product crates/services and their owners;
- package schemas, readers/writers and version IDs;
- Debian endpoints, store interfaces, stream interfaces and event-record owners;
- client UI and actual user-facing test surface;
- CUA action catalogue, Axis policy adapter and session identity;
- OpenLock source inputs and generated outputs;
- SWF importer compatibility boundary;
- civilian-state store vs shell-activity store;
- test commands, health ratchet and unresolved `absent` subjects.

The map is derived navigation, not a new source of authority. The owning schema/code is the source of truth.

## 2. Recommended repository structure

Use the Secure Shell convention of creating directories only when real artifacts land. This is a proposed v2 shape, not an instruction to create empty folders or move current files before a ticket.

```text
secure-shell/
  AGENTS.md
  README.md
  Cargo.toml / Cargo.lock               # if Rust owns package/stream/CUA components
  package.json / lockfile               # only if Node server components remain
  docs/
    ARCHITECTURE.md
    DECISIONS.md
    FORMAT-IMPORT-AUDIT.md
    VERSION-MATRIX.md
    LEDGER.md
    AGENTS-PROPOSALS-YYYY-MM-DD.md
    research/
  server/
    store/
    admission/
    signer-client/
    stream/
    api/
  packages/
    shell-bootstrap/
    axis/
  client/
    qt/
    generated/                           # only if policy permits; provenance required
  crates/
    secure-shell-package/
    secure-shell-stream/
    secure-shell-axis-cua/
    secure-shell-swf-import/
  compat/
    legacy-readers/                      # read-only; no legacy emission
  api/
    schemas/
    templates/
  tests/
    fixtures/
    conformance/
  baselines/
  tickets/
  patches/
  reports/
  artifacts/health/
  tools/
  logs/authority/                        # governed; secrets/redaction policy applies
```

Do not split code across Node/Rust/Qt for aesthetic layering. Keep a single owner per responsibility and move existing code only as part of a migration ticket.

## 3. `AGENTS.md` proposals and automatic convention updates

The SWF runtime provides a useful pattern: `tools/health.py` measures each unit, records a health report, maintains a monotonic ratchet, and writes proposals to `artifacts/health/proposals.jsonl`; the dated human-readable proposal file includes evidence and the ticket required. A proposal is not a rule until a ticket lands it in `AGENTS.md`.

Secure Shell v2 should adopt that governance with an explicit owner-review step.

### 3.1 Proposal record shape

Each JSONL row should contain fields like these; placeholders are illustrative, not actual IDs or hashes:

```json
{
  "proposal_id": "SSV2-PROP-0001",
  "observed_at": "<UTC timestamp>",
  "source_unit": "TICKET-0001",
  "observed_failure": "<named refusal or regression>",
  "evidence": {
    "command": "<exact command>",
    "exit_status": 1,
    "check_count": 12,
    "artifact": "<project-relative path>",
    "digest": "blake3:<hex>"
  },
  "proposed_rule": "<precise, testable AGENTS.md wording>",
  "affected_scope": ["client", "stream"],
  "owner": "<responsible owner role>",
  "required_ticket": "TICKET-0000",
  "status": "proposed"
}
```

### 3.2 Proposal lifecycle

`observed → proposal written → ticket opened → owner review → rule accepted/rejected → AGENTS.md updated only if accepted → enforcement test added → health baseline advanced`.

A rejected proposal remains in append-only history with reason. A duplicate proposal links to an existing ticket. No model, health script, build tool or CUA driver may edit project rules automatically. It may draft a patch/open a ticket; it cannot make itself its own authority.

### 3.3 Conditions that can generate proposals

- commit exceeds configured size budget;
- behavior changes without tests;
- test has no activity/ledger entry;
- a check regresses after it was previously held;
- ambiguous/unregistered format or version token;
- writer emits a legacy schema;
- duplicate package reader or second store writer;
- tool schema has empty/missing properties or undocumented side effects;
- unsigned package is presented as signed;
- line-ending change mutates a byte-sensitive baseline;
- CUA action lacks ticket, presenter, scope, expected revision or postcondition;
- resident identity/continuity is lost or a workday test puppets residents.

The health tool can report proposals and implementation facts. Only the shell's gate assigns `held`, `absent`, or `refused`.

## 4. Agent API design

The API must work for a small agent that needs one function/contract without mounting every shell component. It is a service-level, capability-scoped interface with a discoverable manifest and generated client templates.

### 4.1 API surface rules

- Version every API and every nontrivial schema independently.
- Use JSON Schema or equivalent with required fields, types, enums, bounds, `additionalProperties: false`, auth scope and typed result/error envelopes.
- No empty `properties` objects for tools accepting structured input.
- Avoid arbitrary filesystem paths. Use package IDs, revision IDs, manifest IDs, cursors and bounded documents.
- Every mutation has an idempotency key, expected revision/sequence and auditable operation record.
- Reads are paginated/size-bounded; streams have explicit cursor and resume offsets.
- Return typed refusals with machine-readable code, subject and reason; do not hide refusals in prose or stderr.
- Give each agent only tools/templates its scope allows. Do not mount/download UI, shell runtime or private assets merely to use an API.
- API returns data and action requests; it never returns trust-root secrets or blanket capability grants.

### 4.2 Initial candidate tools

Names, schemas, scopes and version IDs remain proposals.

| Candidate tool | Access | Purpose | Minimum result |
|---|---|---|---|
| `secure_shell.describe_api` | Read | Return API manifest and compatibility versions | Versioned tools, schemas and scopes |
| `secure_shell.read_store_head` | Read | Read canonical server/catalogue head | Revision, sequence, time and digest |
| `secure_shell.list_packages` | Read | Paginated package discovery | Package ID, latest admitted revision, schema and signer status |
| `secure_shell.read_manifest` | Read | Retrieve one canonical manifest | Manifest object, digest, signer/key ID and compatibility |
| `secure_shell.read_schema` | Read | Fetch one schema/version | Schema and declared limits |
| `secure_shell.stream_package` | Read/stream | Fetch one admitted package | Chunk cursor, offset, per-chunk digest and finalization |
| `secure_shell.read_activity` | Read | Read bounded activity/evidence rows | Cursor, event identity, subject digest and proof links |
| `secure_shell.inspect_health` | Read | Read server/client health facts | Metrics and named absent/refused states |
| `secure_shell.fetch_template` | Read | Fetch small API/client template from internal store | Template version, dependencies, digest and generated source |
| `secure_shell.request_operation` | Request | Submit one typed CUA operation for admission | Operation ID, ticket requirement and typed status |
| `secure_shell.read_operation` | Read | Inspect one operation | Acknowledgement, postcondition and evidence/refusal |
| `secure_shell.request_recovery` | Request | Ask for approved bounded recovery | Proposed action and required authority; no silent execution |
| `secure_shell.inspect_legacy` | Read | Identify old format by registered ID/header | Source family/version and owning reader |
| `secure_shell.migrate_record` | Mutate | Execute approved explicit migration | Source/target ID, before/after digest and loss accounting |

### 4.3 Tool response contract

Success carries `api_version`, `operation_id` (for mutations), `status`, `result`, `evidence`, and `revision`. Refusal carries `status: refused`, stable `code`, `subject`, `reason`, supported versions when relevant, and whether a partial write occurred. `absent` is not `pending`; a call that did not execute must say so explicitly.

## 5. Small API-template import workflow

A template is not a shell-component mount. It is a small source package containing only the types/client code needed for the requested task.

1. Agent calls `describe_api` and identifies required API version and scope.
2. Agent requests a template by task (e.g. `read-manifest`, `stream-one-package`, `inspect-health`, `verify-recovery`), language (e.g. TypeScript or Python), and target API version.
3. Server resolves template from internal store and returns its manifest, content digest, generator provenance, dependency lock and license/source references.
4. Agent verifies template digest and schema version. Importing source does not grant a new server scope.
5. Agent compiles/runs thin client against a mock conformance fixture, then invokes bounded API with existing credentials.
6. Writes still require ticket, presenter, current scope and Axis admission. Template installation does not authorize an operation.

The template generator must be deterministic and tested against valid, invalid, near-miss and over-limit inputs. Generated outputs carry generator provenance and are never hand-edited.

## 6. MCP/API lessons from the existing audit

The existing audit found the package/MCP deficiency: `planet-mcp` exposed 17 tools, but only one write verb; 10 schemas had empty `properties`; package builder remained CLI-only; no declared input shape carried a document an agent could author. The solution is not unrestricted file access. It is a typed document/API shape with a shared validator used by builder and acceptor, plus a compact set of bounded operations.

Every tool needs tests for:

- complete valid invocation;
- missing required property;
- unknown property;
- wrong type / out-of-range value;
- duplicate or stale operation ID;
- unauthorized scope;
- oversized document/page;
- malformed package ID/path traversal;
- refused old/new schema;
- partial failure with no accidental commit;
- read-back and independent re-derivation of a resulting record.

## 7. Project conventions and naming

- Documentation uses uppercase descriptive names and v2 prefix, e.g. `SECURE-SHELL-V2-...md`, consistent with `FORMAT-SOURCES-AUDIT.md`, `FIRST-TEN-HOURS.md`, and `TICKET-####-...` patterns.
- Tickets use `TICKET-NNNN-<slug>.md`; patches use `PATCH-NNN-<slug>.md` only for an actual patch artifact, not a general plan.
- New Cargo crates use `secure-shell-*`; no `planet-*` crate is a new runtime dependency. Old crates may remain in a read-only compatibility adapter until migration criteria pass.
- Format IDs, package IDs, API IDs and Cargo crate names are different namespaces; do not infer one from another.
- Generated files carry generator/source digests. Do not maintain duplicate handwritten/generated representations of an authoritative fact.
- GitHub issues/PRs track implementation; local planning markdown is not a remote issue or accepted decision.

## 8. First implementation ticket breakdown

Create after M0 decision capture; IDs below are placeholders to be allocated by the repository's actual ticket sequence.

| Candidate ticket | Outcome | Exit gate |
|---|---|---|
| Audit OpenLock generation boundary | Reproducible source→generated shell path | Source digest + clean regeneration |
| Record v2 naming/version matrix | Owner-selected component and format IDs | No unregistered/ambiguous identifier |
| Specify package/signature contract | BLAKE3 content identity + separate signature | Golden vectors and tamper refusals |
| Implement Debian MongoDB store | Canonical record and immutable object references | Restart/restore/duplicate/crash tests |
| Implement signed stream receiver | Ordered/resumable chunks and atomic adoption | Truncation/replay/stale-schema refusal |
| Generate Qt first-window package | One OpenLock-derived useful window | Actual client witness |
| Implement Axis CUA bootstrap | Health/inspect/present/recover operations | Ticket/Axis/postcondition tests |
| Publish agent API tools | Full JSON Schema and generated templates | Tool conformance and scope tests |
| Quarantine planet importer | Read-only legacy adapter and new output | No new legacy emissions |
| Implement civilian workday | Resident-owned lived verification | Same identities and autonomous post-test life |

## 9. Operational limits

This plan grants no permission to deploy, change remote GitHub branches, mutate the user's store, change signer keys, or launch a live CUA operation. Those require explicit action through the project authority model. The present task creates planning artifacts only; it does not create remote commits or claim tests passed.

## 10. Source register

- Secure Shell rules: https://github.com/alacripose/secure-shell/blob/main/AGENTS.md
- SWF rules: https://github.com/alacripose/swf-cell-runtime/blob/main/AGENTS.md
- SWF dated proposals: https://github.com/alacripose/swf-cell-runtime/blob/main/docs/AGENTS-PROPOSALS-2026-11-04.md
- SWF health workflow: https://github.com/alacripose/swf-cell-runtime/blob/main/tools/health.py
- Secure Shell API audit: https://github.com/alacripose/secure-shell/blob/main/docs/FORMAT-SOURCES-AUDIT.md
- OpenLock: https://github.com/alacripose/dl-openshell
- SWF runtime: https://github.com/alacripose/swf-cell-runtime
