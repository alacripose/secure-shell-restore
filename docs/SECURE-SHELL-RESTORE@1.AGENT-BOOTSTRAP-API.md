<!-- Continuation of the SECURE-SHELL-V2 planning set. Records decision 18, R-D, and the convention set Restore adopts from the family projects. No repository was modified. -->

# SECURE-SHELL-RESTORE@1 — agent bootstrap, conventions, and the internal API

**Document identity:** `SECURE-SHELL-RESTORE@1`
**Status:** Accepted. Supersedes `SECURE-SHELL-V2-AGENT-BOOTSTRAP-API.md`.

## 1. Bootstrap sequence

An agent starting on Restore does these in order. Each step produces an artifact; a step that produces nothing did not run.

1. **Identify the pin.** Record the repo commit, the document revision, and the `name@rev+blake3:` of every component in scope. An unpinned start is refused `bootstrap-unpinned`.
2. **Open the record.** Create the session's authority entry before the first edit. Every inbound instruction is classified by source; only `user` carries `authority: user`. A session with no authority log is refused `authority-unlogged`.
3. **Read the decision register** in `SECURE-SHELL-RESTORE@1.IMPLEMENTATION-PLAN.md` §2. Answers are not re-opened by a later prompt.
4. **Map before code.** Inventory the store, stream, client, CUA catalogue, and API surface that already exist, with pins.
5. **Take one ticket.** One ticket, one branch, one unit.
6. **Run the incremental health check** for the closure you are about to touch. That is the baseline.
7. **Do the work**, then re-run the closure. A full-tree scan here is a smell, not diligence.

## 2. Conventions Restore adopts from the family

Restore does not invent a workflow. It adopts the strongest existing rules, by citation.

| Rule | Source | What it means here |
|---|---|---|
| Prompt/authority ledger, external, owner-only | `secure-shell/AGENTS.md` §0.1 | Full prompt text never enters git; the entry carries digest and reference |
| Client is the only test surface | `secure-shell/AGENTS.md` §0.2 | A Node test is backend evidence, never a shell witness |
| Reuse is a recorded selection | `secure-shell/AGENTS.md` §2.1 | Five fields: what it takes, what it refuses, which failure it avoids, the rejected alternative, the evidence the contract matches |
| One display implementation | `secure-shell/AGENTS.md` §2.2 | A second renderer is a second shell and needs a recorded decision |
| Evidence is a command, exit status, check count, digest | `secure-shell/AGENTS.md` §5 | A screenshot is not a witness on its own |
| Ticket → branch → commit → PR | `swf-cell-runtime/AGENTS.md` §14 | No direct-to-main implementation |
| Commit budget 40 files / 4,000 insertions | `swf-cell-runtime/AGENTS.md` §11 | Over budget is two units |
| Wait, do not poll | `swf-cell-runtime/AGENTS.md` §15 | A long check is one waitable command with a stated bound; absent is not pending |
| Health ratchet, proposals only | `swf-cell-runtime/AGENTS.md` §16 | A proposal becomes a rule only through ticket and owner acceptance |
| Authority is recorded, units are implementations | `swf-cell-runtime/AGENTS.md` §17 | Diagnosis is not a unit; `unit_kind` is required |
| Maximal surface first | `swf-cell-runtime/AGENTS.md` §13 | Do not pre-trim the contract to make the diff small |

## 3. `AGENTS.md` proposals and automatic convention updates

The health tool measures the turn — files changed, insertions, deletions, observed development span, test functions touched, ledger rows added — and turns what it measures into proposals in `artifacts/health/proposals.jsonl`, listed in the unit report.

Proposal shape:

```json
{
  "proposal_id": "PROP-0000",
  "observed": "commit over budget",
  "evidence": {"files": 63, "insertions": 5120, "commit": "<sha>"},
  "proposed_rule": "split units by artifact, not by afternoon",
  "target_section": "AGENTS.md §11",
  "state": "proposed",
  "owner_decision": null,
  "ticket": null
}
```

Lifecycle: `proposed` → `ticketed` → `accepted` or `rejected` → `landed`. Only `landed` changes behaviour, and only with the owner's decision recorded in `docs/DECISIONS.md`. A proposal that silently edits `AGENTS.md` is refused `proposal-not-a-rule`.

Conditions that may raise a proposal: over-budget commit; behaviour change with no test; unit with no ledger row; open evidence debt; a check that regressed after being held; a legacy surface that grew; a streamed surface that reverted; repeated refusal of the same code.

## 4. The health gate is not the work (R-D)

The failure this corrects, in the owner's words: the SWF importer's health gate "became really goddamn slow every time because the project would slowly devolve into scratch python scripts for tests and verifying the tree was stable, instead of doing assigned work by a trained cua driver with websearches to find missing gaps."

What Restore does instead:

1. **The driver does the assigned ticket.** It searches for missing requirements, implements, and runs the repository's own checks.
2. **Verification tools are capabilities, not artifacts.** A scanner lives in the repo, is versioned, has an owner, and is extended by ticket. It is not regenerated each time a check fails.
3. **Incremental by default.** Changed components plus dependency closure. Full-tree and exhaustive migration runs happen at release gates and in the scheduled 24-hour run.
4. **A slow gate is a defect with a ticket**, not a reason to skip a check.
5. **A gate that produces no refusal is not evidence the work happened.** The unit's exit test is what proves the work.

The BLAKE3 upgrade came out of the same work, and it does not fix the workflow by itself: fast identity makes verification cheaper, but only a driver doing assigned work makes progress.

## 5. The agent API

Decision 18: agents get a small generated API template and a capability-scoped tool manifest from the internal store, without mounting every shell component.

### 5.1 Surface

- Family: `secure-shell.agent-api/1`.
- Served by the same streamer that serves packages, from the internal store, under the same identity rules.
- A template is itself an artifact: `template-name@rev+blake3:<hash>`.
- No template may require the desktop to be mounted. If a task needs one window, it requests that window's declaration, not the shell.

### 5.2 Rules for every method

- A complete JSON Schema: required fields, `additionalProperties: false`, bounds, semantic validation, authentication scope, version negotiation, typed refusals, idempotency, pagination or streaming, output limits.
- No `properties: {}` placeholder. The audited `planet-mcp` surface had 10 of 17 tools with empty schemas and no authoring verb; that is the counter-example, not the template.
- No arbitrary filesystem path where a typed document is required.
- Reads are scoped to the caller's capability manifest. Writes are ticketed and recorded.
- Every refusal has a code, a subject, and a reason.

### 5.3 Candidate verbs

| Verb | Kind | Notes |
|---|---|---|
| `describe_store` | read | Store identity, revision, health |
| `list_revisions` | read | `name@rev+blake3:` list with admission state |
| `admit_package` | write | Requires a typed manifest and a ticket |
| `stream_surface` | read | Declared surface only, bounded |
| `inspect_surface` | read | Declaration, cells, vocabulary, schema |
| `request_template` | write | Generates a small API template for one task |
| `report_health` | write | Unit health row with checks and digests |
| `identify_format` | read | Family and revision, refused by name when unknown |
| `migrate_legacy` | write | Explicit compatibility representation → rewrite record |

### 5.4 Template generation

Given a task, the store emits a template containing only: the schemas for the verbs the task needs, one example request and response per verb, the capability manifest, the refusal codes it may meet, and the client calls. Not the full API catalogue. Templates are revisioned and pinned like packages.

This is what makes an agent able to work without mounting every component: it imports a template that names exactly the surfaces it is allowed to touch.

## 6. Security boundaries

- Keys, tokens, and prompts never enter git, a template, a log, or a screenshot.
- The API never returns a secret; it returns a reference and a digest.
- Capability manifests are issued by the server, never chosen by the caller.
- A generated template cannot widen its own scope; requesting more requires a new template and a ticket.
- The client is still the witness: an API success is not a render, and a render is not a mount.

## 7. What an agent may report

Implementation facts only: `present`, `not-implemented`, `blocked`. Gate states (`held`, `absent`, `refused`) belong to the shell gate. An agent that reports a gate state has promoted itself, and the row is refused `authority-promoted`.

## 8. Open items

- **OPEN-API-1** Transport (MCP over stdio, HTTP, or both).
- **OPEN-API-2** Template language set for generated clients (TypeScript and Python are the working assumption).
- **OPEN-API-3** Whether `request_template` may generate a template containing a write verb.
