<!-- Skill load record. Hyperskill is non-conclusive: loading it grants no authority and replaces no user decision. -->

# HYPERSKILL@0.1.0 — loaded

**Status:** Loaded and adopted as the working protocol for Restore planning and delegation.
**Loaded:** 2026-11-04, by reading the public artifact, not a local copy.
**Non-conclusive:** this load grants no authority, guarantees no improvement, and does not override `AGENTS.md`, `docs/DECISIONS.md`, or any user decision.

## 1. What was loaded

| Field | Value |
|---|---|
| Repository | `alacripose/hyperskill` (public, MIT, Rust) |
| Branch tree | `0fb648ac2a333b37d68a6b671eadb933356d489e` |
| Skill artifact | `SKILL.md`, blob `dd9e1d34de64a3a1a41454f621d4fe7fb61b3219`, 21,796 B |
| Declared identity | `name: hyperskill`, `version: 0.1.0` |
| Crate | `hyperskill-diffusion` 0.1.0, lib `hyperskill_diffusion`, bin `hyperskill-diffusion` |
| Toolchain | pinned by `rust-toolchain.toml`; SKILL build identity names rust 1.98.1 |
| Publication contract | the public artifact is one standalone `SKILL.md`; internal ledgers are not runtime dependencies |

The skill's own build identity block is preserved there and is not restated here, because restating digests is how digests drift.

## 2. What this changes in practice

These are now binding on how I work in this project, not suggestions:

- **Seven-field contracts.** Every delegated ticket states MISSION, SCOPE, CONSTRAINTS, RESOURCES, EVIDENCE, DELIVERABLE, STOP. A contract may narrow inherited authority, never widen it. A missing field is a refusal or a `needs-context` result, not an improvisation.
- **Declared context budget per lane.** `required_context` = skill slice + source cards + claim-map slice + diagram source + ticket contract + required evidence + output reserve. Dispatch only when the declared load fits the measured window; otherwise narrow or refuse. Never silently truncate.
- **Governed ticket statuses only:** `queued`, `open`, `active`, `blocked`, `review`, `complete`, `rejected`, `handled`, `dropped`. `STATUS.md` is derived and authorizes nothing.
- **Retirement before completion.** No ticket reaches `complete` without a separate retirement record naming terminal state, reason, grounding, impact, verification, evidence, outcome, governance. A status flip is not retirement.
- **Evidence review and self-grill.** Every material claim links to evidence; a fresh reviewer attempts falsification against raw evidence. Prose, a DONE, or a reviewer recommendation is not completion.
- **Honest host-process evidence.** If an independent dispatch or completion trace is unavailable, the claim is `not_evaluable`. A self-authored counter proves nothing about the host.
- **Candidate isolation.** A candidate is a proposal with baseline, variant, hypothesis, acceptance checks, limitations, exact base digest, rollback reference. Review patches apply inside the prototype only.
- **Hypergrilling user control.** Material decisions — scope, authority, evidence, publication, destructive writes, dependencies, unresolved ambiguity — are not asked of the user by default. Hypergrilling is a CUA driver deliberating on cadence-tick budget, with code and web search, and it escalates only the residue that is genuinely owner-only. Children return uncertainty packets; they cannot prompt the user.

## 3. Mapping onto Restore

| Hyperskill requirement | Where it lands in this project |
|---|---|
| Seven-field contract | `SECURE-SHELL-RESTORE@1.IMPLEMENTATION-PLAN.md` §1 and §7 |
| Incremental verification, not gate-as-work | Same document, R-D and §5 |
| Governed statuses | Replaces ad-hoc status language in tickets under `tickets/` |
| Retirement record | Required before any R-milestone closes |
| Rollback with exact base digest | Already required by the package identity rule; now also required per unit |
| Diagram freshness manifest | Applies to the Restore component map if it is ever promoted from ASCII to a rendered diagram |
| Preserved disagreement | See §4 |

## 4. Preserved disagreement (not silently resolved)

Hyperskill states: *"Delegate only through a native local child session. Online agents, hosted services, remote APIs, external CLIs, and web-mediated dispatch are forbidden."*

The project owner has directed the opposite for research: the SWF importer's failure was that the project devolved into scratch scripts *"instead of doing assigned work by a trained cua driver with websearches to find missing gaps."* The GitHub integration was also used, on instruction, to read the audit.

Both cannot be true at once for research lanes. The skill's own rule applies: the disagreement is preserved and adjudicated, not synthesized away. Until the owner rules:

- **Delegation** (work handed to another agent to produce artifacts) stays native-local, per the skill.
- **Research** (reading public sources to find a missing requirement) is recorded as a user-authorized exception, per the owner's direction, with the source and the authorization in the ticket.
- Neither reading is quietened by the other.

## 5. Hypergrilling format — v2 as of 2026-11-04

The owner ruled that round-end options (`continue`, `one more round`, `pause`, `stop`) are the legacy format, and then that owner-facing question rounds are the legacy shape entirely. Both are retired.

Hypergrilling is a **deliberation loop run by a CUA driver**, plausibly a second CUA agent rather than an LLM. Within a cadence tick its CPU time is unbounded; it may search the code, the store and the web before it is entitled to ask anyone anything. Every open question is classified `code`, `spec`, `external`, `measure` or `owner`; only `owner` reaches the user, and only as a named residue rather than a stream of rounds.

**Record:** `SECURE-SHELL-RESTORE@1.HYPERGRILL.md` (format v2, with the resolver classes and the owner-only residue).

## 6. What this load does not do

- It does not make the Restore plan authoritative; only the owner does that.
- It does not promote any candidate patch.
- It does not license editing a generated `SKILL.md`, a live skill, or a public boundary.
- It does not turn a screenshot, a bot report, or a green gate into a client witness.
