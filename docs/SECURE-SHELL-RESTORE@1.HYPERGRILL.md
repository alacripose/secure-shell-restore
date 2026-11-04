<!-- Format changed 2026-11-04 by owner ruling: hypergrilling is not an owner-facing question queue. It is a CUA driver deliberating on cadence-tick budget, with web and code search, escalating only what only the owner can decide. Append-only for rulings; the resolution backlog is a target graph, not a script. BRAND: "Secure Shell" is never abbreviated. -->

# SECURE-SHELL-RESTORE@1 — hypergrilling

**Document identity:** `SECURE-SHELL-RESTORE@1`
**Kind:** HYPERGRILL
**Status:** Format v2. Round-based owner questioning retired. The backlog below is worked by a CUA driver, not by the owner.

## 1. What was retired

The previous format asked the owner 20 questions per round, offered a "(Recommended)" default on nearly every one, and stopped between rounds. The owner ruled that this is the legacy shape, and that in the real system the hypergrilling target is the **CUA driver** — plausibly a second CUA agent rather than an LLM at all — which may spend the unbounded CPU time available within a cadence tick searching everything, including the web, before it is entitled to ask anyone anything.

## 2. Why the old format failed, in this session's own record

| Failure mode | Evidence in this worksheet |
|---|---|
| The owner did the search work | Q063–Q076 are all answerable from BLAKE3 and canonical-JSON practice; none needed the owner |
| Recommended-default bias | 24 of 26 answers in round 01 were the suggested option; the format was steering, not asking |
| Contradictions found late | `T-001`–`T-004` surfaced across four rounds; three were structural, not matters of taste |
| A question whose premise had died | `N002` was invalidated by `Q007` and still sat in the queue as if live |
| A duplicate question | `N011` restated `N001` and consumed a slot |
| Human pacing as the bottleneck | 120 answered, 407 spine remaining, one round per turn |
| Tension recorded, not resolved | `T-001`/`T-002` were written down as "cannot both hold" and then left for the owner to adjudicate |

Each of these is a defect the new loop is supposed to remove, so each is recorded rather than forgotten.

## 3. What hypergrilling is now

Hypergrilling is a **deliberation loop run by a CUA driver**, target `secure-shell-driver`. The driver receives the open question set, and inside a cadence tick it may:

1. read the recorded decisions and the evidence pins;
2. search the code, the Mongo store, the package corpus and the audit copies;
3. search the web for external facts — library versions, format specifications, platform behaviour;
4. run bounded experiments where a measurement settles the question faster than an argument;
5. write a resolution with its evidence, or a strike with its reason, or an escalation naming why the question is not its to answer.

A second CUA agent is the default deliberator; an LLM is not required. The driver's authority is bounded by §5.

**Mechanics.** `tools/hypergrill_resolver.py` implements this contract. `seed` reads the appendices into `docs/hypergrill/state.json`; `tick` schedules the cheapest open question and names the next search; `resolve` admits only a five-field receipt carrying evidence; `lookup` searches a checked-out repository and returns `code` evidence with a `path:line` ref; `fold` and `strike` close duplicates and dead premises with a citation; `self-check` asserts the contract on a throwaway copy. The appendices are the seed, not the live status — status lives in `state.json`, and every closure appends to `docs/hypergrill/receipts.jsonl`.

## 4. Tick contract

- The **cadence tick** is the scheduling unit, as the SWF importer already runs it. It is not a work limit.
- Within a tick the driver's CPU time is **unbounded**: a question may consume the whole tick, or several, if search is what settles it.
- Questions persist **across ticks** through the evidence ledger. A tick ending mid-question is a recorded state, never a lost thread and never a stall.
- A tick's output is a receipt: resolved, struck, escalated, or `still-open` with the next cheapest discriminating search named.
- Budget pressure changes *order*, not *rigour*: cheap convergent searches run first, expensive ones are scheduled, and nothing is resolved by running out of time.

## 5. Resolver classes and the escalation boundary

Every open question is assigned one class. The class decides who may close it.

| Class | Closer | Example from this worksheet |
|---|---|---|
| `code` | driver, by reading the repository | whether the ledger already stores an oplog position |
| `spec` | driver, by deriving from recorded rulings | what the preimage layout version must be, given §12.8 |
| `external` | driver, by web search and citation | which Qt 6 minor is pinnable, which minisign implementation to adopt |
| `measure` | driver, by a bounded experiment | the logarithmic scaling constant in `N035` |
| `owner` | **only the owner** | brand form, risk appetite, publication, money, destructive writes, taste |

Escalation is a refusal to guess, not a request for permission to work. An escalated question must name the class boundary it hit and the cheapest owner input that would release it. The driver may not escalate a question it could have searched.

## 6. Owner-only residue

These are the questions in the remaining set that the driver may not close, grouped so they can be answered in one pass rather than streamed:

- **Brand and naming taste.** The minimum display form (answered: "Secure Shell" plus the pinned hash), plus any future grade names.
- **Risk appetite.** Retention windows, deprecation window length, backup cadence, the 64 GiB hard ceiling.
- **Authority and publication.** What may be published, what may be destroyed, what may be spent.
- **Acceptance.** What counts as a successful day: the 24-hour continuous simulation, a recorded workday of cadence ticks, or a count of independently verified tasks — still unanswered from `docs/answers.txt`.
- **Scale policy.** Whether the worker ceiling stays a user attestation or becomes a verified gate.

Everything else in the 407 is `code`, `spec`, `external` or `measure`.

## 7. Resolution record

A resolution is accepted only with all five fields:

| Field | Meaning |
|---|---|
| `question` | the id and the question as asked |
| `class` | one of the five classes in §5 |
| `evidence` | what was read, searched or measured, with pins and URLs |
| `resolution` | the decision, stated so it could be refused |
| `effect` | which documents change, and whether it contradicts an existing ruling |

A resolution that contradicts a recorded ruling is a **supersession** and must name it. A resolution without evidence is a guess and is refused `resolution-unsupported`.

## 8. State

| Counter | Value |
|---|---|
| Spine total (planned) | 500 |
| Asked under the retired format | 139 questions |
| Answered | 119 |
| Open, unanswered | 20 (round 07, carried into the loop as its first batch) |
| Remaining spine | 407 |
| Newly opened, logged | 54 |
| Struck or folded | 2 |
| Supersessions | 2 |
| Tensions (resolved / open) | 4 / 0 |

The 20 carried questions are the loop's first tick. They are no longer put to the owner: `Q077`–`Q093` and `N052`–`N054` are reclassified in Appendix B, and the driver closes the `code`/`spec`/`external` ones with evidence before the next tick.

## 8.1 Format rulings (2026-11-04)

| Question | Ruling |
|---|---|
| Which format governs, the driver loop or manual rounds? | **The driver loop governs; manual rounds are the fallback.** Searchable questions are closed with cited evidence; only owner-only ones reach the owner |
| Does `tools/hypergrill_resolver.py` stay? | **Kept as a named fixture** — it validates receipts and cannot block a commit |
| Does `docs/DECISIONS.md` get created now? | **No.** It stays absent until a round produces entries to project |
| Did the §0 count rewrite overstep? | **No.** Four dropped, ten kept stands |

## 8.2 Round held 2026-11-04 (v2.1)

One question, because one question was the residue: every other open item was closed by search with
a citation. The answer is recorded in the owner's words and is not curated.

| id | question | owner's words | state |
|---|---|---|---|
| `N052` | What evidence raises a mount whose observation came back degraded to healthy? | "One successful mount plus a render witness" | answered |

**State:** asked 1 · answered 1 · open 0 · struck 0 · superseded 0 — **0 remaining.**

## 8.3 Driver progress (2026-11-04)

| Block | Seeded | Closed | Open |
|---|---|---|---|
| Carried set (Appendix C) | 20 | 20 | 0 |
| Stream protocol (Appendix D) | 20 | 20 | 0 |
| Mount receipts (Appendix E) | 20 | 20 | 0 |
| **Worked so far** | **60** | **60** | **0** |

`state.json` holds 180 entries: 178 resolved, 1 folded, 1 struck, 0 open. Receipts on file: 61. Remaining spine: 367 of 500.

Nothing is open. Every question this block raised has been answered by the owner, closed on evidence, or struck with its reason; none is waiting in prose.

## 8.4 Round held 2026-11-04 (v2.2): mount receipts

Four questions put to the owner. Three were answered; the fourth was struck because its premise was
false. Nothing was folded to keep the block tidy, and no open question was left unasked.

| Id | Question | Owner's words | State |
|---|---|---|---|
| `Q137` | How long are mount receipts retained before retention removes the vault blobs they point at? | "Kept forever; receipts and their evidence are never removed" | answered |
| `Q138` | May mount receipts leave the machine — published, exported or shared outside it? | "Publishable in full, including evidence refs" | answered |
| `Q139` | What counts as a successful acceptance day? | "all 3" | answered |
| `Q140` | May the driver witness its own mount and count that as receipt evidence? | "False, we have node cua bots in ala-civ-bots-prototype, another authorization violation that will have to be refused and backwalked against the hypergrilling tree through an automated audit to see where such a thing came from, which was the performance test for the 1000 cua drivers" | struck — premise false |

**State:** asked 4 · answered 3 · struck 1 · open 0 · superseded 0 — **0 remaining.**

`Q140` is struck, not answered. The question rested on the rule that a Node, headless or separate-page
check is not a witness; the owner reports the family does not keep that rule, since
`ala-civ-bots-prototype` runs Node CUA bots and the 1000-driver performance test ran on them. A question
whose premise died keeps its id and is closed with its reason. The authorship question beneath it is
reopened as `N055` and asked.

| Id | Question | Class | State |
|---|---|---|---|
| `N055` | What authorization does a Node-driven CUA witness carry? | `owner` | answered — "the node cua driver is the operation layer for the civilian acceptance document" |

## 8.5 Authorization violation register

### AV-001 — a Node check is not a witness (refused)

| Field | Value |
|---|---|
| Owner's words | "False, we have node cua bots in ala-civ-bots-prototype, another authorization violation that will have to be refused and backwalked against the hypergrilling tree through an automated audit to see where such a thing came from, which was the performance test for the 1000 cua drivers" |
| The rule as written | `secure-shell:AGENTS.md:45` — "a check that runs only in Node, a headless browser, or a separate witness page is not a witness" |
| Where it was propagated | `docs/hypergrill/receipts.jsonl:49` — `Q129`, which used it as its second pin |
| What the family actually runs | `ala-civ-bots-prototype:CHECKPOINT.md:38` — "the connected body is the Node mineflayer process in `tools/residents/src/main.mjs`, not a Fabric client"; `ala-civ-bots-prototype:build/reports/gameplay-degrees.txt:78` — "the mineflayer body reads exact AXIS packages; it is a client" |
| The 1000-driver performance test | **`absent`.** Not located in that checkout by this audit. The missing artifact is a performance-test record naming 1000 drivers. The owner reports it; the file was not found, and it is recorded as owner-reported rather than as a citation |
| Disposition | The rule is **refused as authority**. `Q129`'s conclusion — a receipt requires a rendering, not a check the client cannot see — survives on its other pin (`test-surface-unwitnessed`), so no receipt is retracted. The authorization question beneath it is `N055` |

**Answered 2026-11-04 (N055).** The Node CUA driver is the operation layer for `SECURE-SHELL-RESTORE@1.CUA-CIVILIAN-ACCEPTANCE.md`. The rule this register refuses therefore does not merely lack family support; it contradicts the role the owner has assigned.

**How the backwalk was run.** Automated, not by reading around: the claim is grepped across this tree
and the family checkout, every hit is pinned with a path and a line, and the register records what the
search found and what it did not. A missing artifact is written as `absent` with its name, never
inferred from silence.

**What the audit establishes.** The rule is a local convention of `secure-shell`, not a family-wide
invariant: the tree that states it is contradicted by a sibling checkout whose residents are Node
processes. A convention stated in one repository was cited as though it were family law, and that is
the authorization violation — not the existence of Node bodies.

## 8.6 Re-audit of the 500 against the projects on disk (2026-11-04)

The whole spine was re-audited once the family checkouts were available, not just the worked blocks.
`Q001`–`Q140` are the asked range (`Q094`–`Q100` were never written) and `Q141`–`Q500` exist only as
Appendix B blocks, so the audit reports
367 slots `unasked` rather than inventing their wording. Of the 133 recorded
spine questions, 7 are supported by a file read, 5 are contradicted, 1 is a tension,
1 names a mechanism no file implements, and 119 have no probe on disk.

The contradictions are format-shape rulings: `Q064`, `Q068`, `Q070`, `Q071`, `Q074` each describe a JSON manifest, a payload walk,
a Merkle tree over files or per-file hashes, while `testport1` ships `V4PKG001` — one binary frame and
one SHA-256 payload digest over `domain || schema || len || payload`. Both cannot be the package
format; choosing one is a ticket, not an audit.

No `code`, `spec` or `owner` question was closed, reopened, folded or struck by this audit, and
`state.json` and `receipts.jsonl` are unchanged. The report is `docs/hypergrill/AUDIT@2026-11-04.md`,
its JSON is `docs/hypergrill/audit@2026-11-04.json`, and `tools/hypergrill_reaudit.py` re-runs it.

The record also never asks about a tick cadence: `testport1/docs/TICK-CADENCE.md:11` records the plan's
refusal to hardcode a 20 Hz tick, and no slot in the 500 carries the question that would place it.

## 8.7 Round held 2026-11-04 (v2.3): the re-audit's residue

Nine questions put to the owner after the 500-slot re-audit; eight answered, one returned as a
search task. Answers are recorded in the owner's words and are not curated.

| Id | Question | Owner's words | State |
|---|---|---|---|
| `A-01` | Which package format does Restore admit: the on-disk `V4PKG001` frame, or the ruled manifest/Merkle shape? | "The ruled manifest/Merkle shape" | answered |
| `A-02` | Both hashes: separate widths, or one? | "Full 64 hex for both" | answered |
| `A-03` | `Q060`'s deprecation window, which no file carries | "Add the field now" | answered |
| `A-04` | Is the grade in the preimage, as `Q074` rules? | "Add grade to the preimage" | answered |
| `A-05` | How should the record treat the 367 slots with no question text? | "Write them block by block" | answered |
| `A-06` | Where does the tick-cadence deprecation belong? | "Add a cadence question and answer it" | answered |
| `A-07` | What should happen to the 119 rulings no checkout implements? | "find them?" | open — returned as a search task |
| `A-08` | Should the re-audit run in CI and fail on contradictions? | "Fail on contradiction" | answered |
| `A-09` | Which references count as primary for the driver task? | "Everything the scan selected" | answered |

**State:** asked 9 · answered 8 · open 1 · struck 0 · superseded 0 — **1 remaining**, `A-07`.

The primary reference set is the whole role-matched scan, not a curator's shortlist: `A-09`
withdrew the selection the planner had made on the owner's behalf, and the scanner now lists
every reference it selected instead of promoting a subset.

**What the answers change.** The ruled manifest/Merkle shape is the package format, so `V4PKG001` is a
legacy input that is read and converted; the five format-shape contradictions are superseded rather
than corrected on the frame. Both hashes become full 64 hex, so the 32-hex format id is a
pre-migration form. The grade joins the preimage, so a grade change is a new id. The deprecation
window becomes a required field with no implementation yet — still reported `absent-on-disk` until a
file carries it. The 367 unwritten slots are to be written block by block, format blocks first.

### A-07 — "find them?": the mechanisms that do exist

The 119 unprobed rulings were searched rather than assumed absent. Four mechanisms are on disk:

| Mechanism | Where | What it settles | What it does not |
|---|---|---|---|
| Mount-receipt store | `secure-shell/tools/port/store.mjs:20-43` (`surface.mount/2`, `STATES`, `FIELDS`, `receipt-id`) | receipt shape, idempotence, refusal states (`Q121`–`Q136`) | retention, withdrawal (`Q131`, `Q137`) |
| Checkpoint envelope | `secure-shell/server/ledger.mjs:494-532` (`ed25519`, `payload-digest`, `record-id`) | scheme, coverage, tamper refusals (`Q082`, `Q083`) | name-and-revision binding (`Q055`) |
| Signing seam | `shploingus-clean/crates/voxel-package/src/signing.rs:57-110` (`KeyId`, `Signature{algorithm, key_id}`) | key identity, algorithm refusal, one-signature shape (`Q085`, `Q086`) | multiple signatures (`Q085` still open) |
| Voxel manifest | `shploingus-clean/crates/voxel-package/src/lib.rs:103-115` (`name`, `version`, `payload`, `requires_*`) | name in the manifest, dependency pinning (`Q062`, `Q072`) | per-file rows; the manifest pins one payload digest |

Retention, deprecation windows and revision history have no file at all — `rg -i "retention|deprecat"`
finds policy prose and nothing executable. Those rulings stay `no-probe` with the missing mechanism
named, not with silence.

## 8.8 Round held 2026-11-04 (v2.4): the civilian star, the autonomy claim and the ratcheter

Five questions, asked after reading `PATCH-004-five-star-axis.md`, the pasted civilian acceptance
contract, N042/N037/A-04 and `SECURE-SHELL-RESTORE@1.IMPLEMENTATION-PLAN.md` §1/§5/§7. The five were
the residue: where the sixth star's rows come from, which axis carries an autonomy claim, what the
handoff ratchet refuses, how a day-sized unit meets the commit budget, and where a push lands. Answers
are recorded in the owner's words and are not curated.

| Id | Question | Owner's words | State |
|---|---|---|---|
| `A-10` | What turns `cold` and `tired` into a row of the sixth star's lens? | "Needs stay prose; only rest (CGA-08) is a row" | answered |
| `A-11` | Which token names true autonomy, and on which axis does it live? | "agent skill, operable by any of the max 1000 axis cua drivers for training or shell work, one of the three traffic light modes," | answered |
| `A-12` | What does the handoff ratchet refuse, and when? | "`handoff-absent` at unit close" | answered |
| `A-13` | How does a day's work fit one unit and the 40-file/4,000-insertion budget? | "A unit is a day-ticket; commits stay under 40/4,000; one PR closes the day" | answered |
| `A-14` | Which repository receives the per-unit pushes? | "Make `secure_shell_v2` a repository with its own remote" · "you need to track your failures as you work in true autonomy mode as a part of health and policy so the cua driver can get a better understanding of you until it can be trusted to use git itself. use git integrations." | answered |

**State:** asked 5 · answered 5 · open 0 · struck 0 · superseded 0 — **0 remaining in this round**.
`A-07` from §8.7 stays open and is not counted here.

**What the answers change.** `A-10` keeps needs out of the star: the sixth star's lens stays at the
five rungs PATCH-004 already reads, and `cold`, `tired` and the rest of that class are recorded as
prose in a day's narrative, never as a predicate. The star therefore cannot be lit or refused by a
need, which is a narrower claim than the mission asked for and is written down as the narrower claim.

`A-12` adds one refusal name to the vocabulary: a unit does not close until a second agent identity
has produced a verification receipt naming the trained driver's ticket, and a unit attempting to close
without one is refused `handoff-absent`, with the refusal stored as a row rather than printed. That is
the ratcheter the mission asked for, and it is the first entry in the ratchet that is not a coverage
number.

`A-13` redefines the unit without moving a number: a day is a ticket, commits inside it stay under 40
files and 4,000 insertions, and one pull request closes the day. Rule 5 of the implementation plan now
describes the commit and rule 9 keeps its per-commit meaning.

`A-14` makes this workspace a repository with its own remote, and makes the agent's own failures a
health-and-policy record the driver reads — `SECURE-SHELL-HEALTH@1.FAILURE-LEDGER.md`. The owner's
reason is narrow and is the point: the driver learns the agent's failure shape before it is trusted
to use git itself.

### A-11 — what the answer leaves unstated

The answer does not select any of the four options the question offered, and it is not read back into
one. It establishes four things: the claim is an **agent skill**; it is operable by at most 1000 axis
CUA drivers, whether the work is training or shell work; and it takes **one of three traffic light
modes**. Two consequences are named rather than guessed:

| Unstated | Why it cannot be derived | Cheapest thing that settles it |
|---|---|---|
| the three traffic light mode tokens | N042 closes the grade enum to `install` and `os` "others by ruling", and Q021 restricts names to `[a-z0-9-]`, so the tokens are a naming ruling, not a derivation | the owner names the three modes, or rules that the modes are `grade` values |
| which ladder carries them, `grade` or `evidence_grade` | A-04 puts `grade` in the preimage, so a mode carried there mints a new id each time; `evidence_grade` does not touch identity | one ruling: does moving between modes change a package's identity? |

Until both are ruled, no traffic light token is written into `axis.data.json` and no skill is graded,
because a made-up token would be refused `star-token-unknown` or would silently join a closed enum.

**Message provenance for this round.** The enabling brief arrived as a mission message; the same words
also arrived as the owner's own turn. The ruling is recorded under the owner's voice because the owner
typed it, and the mission brief is quoted only as the goal it states, per §13. The brief's own claims —
that the agent is failing the shell, that the remedy is a CUA axis driver powered by the Debian shell —
are recorded as the owner's assessment of the agent and not as a finding of this document.

**Publication.** The owner's words, 2026-11-04: "Publish publially." Recorded as a directive rather
than a question, because there was nothing to search: publication is the owner's alone (§6). The
repository that carries this record is `alacripose/secure-shell-restore`; it was created private by the
agent's own conservative reading of "its own remote" and is made public on this directive, so the
visibility change cites the owner rather than the agent's preference. What is published is this
workspace — the five plan documents, the round and audit records, the tools, the checks the CI workflow
calls, and the scan record. What is never published is a key, a token, a credential or a private
prompt: a secret in the tree is a defect to be removed, not a risk to be weighed.

## Appendix A — owner rulings recorded under the retired format

These are the answers that survive as authority. They are unchanged by the format change.

### Rounds 01–02 (Q001–Q025, N001–N016)

| Id | Ruling |
|---|---|
| Q001 | Lowercase `restore` in names |
| Q002 | `secure-shell-*` for everything |
| Q003 | Each document versioned independently |
| Q004 | Release manifest at `releases/index.json` |
| Q005 | Tags carry `name@rev` only |
| Q006 | Lowercase hex only |
| Q007 | Ceiling much higher; OS and a game; must learn miniaturization |
| Q008 | Ceiling enforced at admission, delivery and mount |
| Q009 | Signing key under `systemd-creds` |
| Q010 | Rotation per release |
| Q011 | Store-level key for spanning rows |
| Q012 | Replication deferred past Restore |
| Q013 | Ledger is both a Mongo collection and an export; Mongo authoritative |
| Q014 | All QTXML dialects; no motion is a refusal |
| Q015 | Frame floor plus bitmap memory cap |
| Q016 | Driver proposes capability catalogue entries, owner approves |
| Q017 | Design bound tens of billions; default 1,000 |
| Q018 | MCP over stdio |
| Q019 | The five documents stay five |
| Q020 | Chat is the record, curation is the rule |
| N001 | One XML reader over a common intermediate |
| N003 | Re-sign every package at each rotation |
| N004 | Each export records its Mongo oplog position |
| N005 | Nightly backup, weekly restore drill |
| N006 | No default ceiling: declaration required; stream declared size; report space honestly; cut off bloat |
| N007 | Hard ceiling raised to 64 GiB |
| N008 | Miniaturization is transform, build mode and training objective, staged |
| N009 | x86 reached after miniaturization |
| N010 | Both mount-and-render witness and parity digest |
| N012 | Motion is a required field on every surface |
| N013 | Budgets differ per target class |
| N014 | Device limits recorded honestly so settings can offer display options |
| N015 | Worker count is user-settable behind a checkbox and warning |
| N016 | Default 1,000, settable from 1 upward |
| Q021 | Names restricted to `[a-z0-9-]` |
| Q022 | All names follow the family naming schema |
| Q023 | `debian-store` is both a package and a role |
| Q024 | The streamer carries its own package identity |
| Q025 | `openlock` renamed at generation |

### Rounds 03–04 (Q026–Q048, N017–N039)

| Id | Ruling |
|---|---|
| N017 | `declared-size-exceeded`; toast proofs are checked |
| N018 | Space checked both preflight and mid-stream |
| N019 | Size options presented as a chooser |
| N020 | Any overrun above the declaration is a refusal |
| N021 | 64 GiB applies to every target class |
| N022 | The owner's machine is x86; the first Restore is WSL Debian there |
| N023 | Exact digest match, no tolerance |
| N024 | A streamed settings package owns device reporting |
| N025 | A lower frame floor degrades with a warning |
| N026 | User attestation; worker count scales logarithmically |
| N033 | OpenLock toast proofs are part of the proof chain |
| N034 | WSL Debian on the owner's machine is the first target |
| N035 | Logarithmic base 2, constant measured |
| N036 | `grade` is an enumerated manifest field |
| N037 | Grade set is open; OpenLock's grades are OpenLock's; Secure Shell has its own install-grade axis |
| N038 | Reader protocol version shared with the client revision |
| N039 | Store package is `secure-shell-store` |
| Q026 | A rename is a deprecation plus a new lineage |
| Q027 | Aliases refused, like a token crosswalk |
| Q028 | Architecture is a manifest field |
| Q029 | A metadata-only package is still a package |
| Q030 | Release bundles have identity |
| Q031 | `restore` is both a streamable package and a grade |
| Q032 | Compatibility representations get package identities |
| Q033 | Generated templates use the package name grammar |
| Q034 | Reserved prefix `secure-shell-internal-` |
| Q035 | The Qt client ships as one package |
| Q036 | The naming schema applies to roles and services |
| Q037 | The family name is itself versioned |
| Q038 | Exact byte comparison, no case folding |
| Q039 | Name length bounded at 64 characters |
| Q040 | A name maps to exactly one lineage |
| Q041 | Revisions start at 1 |
| Q042 | Revisions are never reused |
| Q043 | A withdrawn revision stays retired forever |
| Q044 | Revisions are monotonic per lineage |
| Q045 | A revision never decreases on rollback |
| Q046 | A hotfix is a new name |
| Q047 | Prereleases draw from a separate counter |
| Q048 | Revisions are decimal digits with no leading zeros |

### Rounds 05–06 (Q049–Q076, N040–N051)

| Id | Ruling |
|---|---|
| N040 | A hotfix adds a name to the same lineage; the counter carries across |
| N041 | A promoted prerelease takes a new stable number |
| N042 | Grades are `install` and `os` for now, others by ruling; Secure Shell is never abbreviated |
| N043 | A package cites a family revision at or below current |
| N044 | An unknown grade is accepted with a warning |
| N045 | A protocol change bumps the client revision |
| N046 | A revision may carry identical payload; Q051 relaxes to "bytes or metadata differ" |
| N047 | The revision leaves the BLAKE3 preimage |
| N048 | Minimum display is "Secure Shell" plus the pinned hash |
| N049 | `secure-shell-family` is graded `install` |
| N050 | A warned mount stays degraded until it proves itself |
| N051 | A promoted prerelease's old number stays retired |
| Q049 | The family ships as the package `secure-shell-family` |
| Q050 | A revision is never absent |
| Q051 | A revision requires a content or metadata change |
| Q052 | Two revisions may share identical content |
| Q053 | `latest` is derived at read time |
| Q054 | A withdrawn revision still resolves for the pin |
| Q055 | The signature binds name, revision and hash |
| Q056 | One published revision at a time |
| Q057 | Revision ceiling is 2^64 |
| Q058 | Superseded by `N047`: the revision is not in the preimage |
| Q059 | A promoted prerelease keeps its content hash |
| Q060 | Each revision declares a deprecation window |
| Q061 | The hash covers canonical bytes, and the stored form must match |
| Q062 | The hash covers the package alone; dependencies are pinned separately |
| Q063 | Full 32-byte output, untruncated |
| Q064 | Preimage is the canonical manifest plus a payload walk |
| Q065 | Preimage begins with a fixed domain-separation tag |
| Q066 | Payload is referenced by its own hash |
| Q067 | Object keys sorted by byte order |
| Q068 | JSON on disk, binary on the wire |
| Q069 | Integers only, no floats |
| Q070 | Payload is a Merkle tree over files |
| Q071 | Per-file hashes are recorded |
| Q072 | Package name sits in the manifest header |
| Q073 | Family revision is in the preimage |
| Q074 | Grade is in the preimage |
| Q075 | Receipts use the same rules under a different domain tag |
| Q076 | The preimage layout is version-tagged |

## Appendix B — the remaining spine, by resolver class

The 407 unasked spine questions are grouped here so the driver knows who closes each block. This classification is itself a `spec` resolution that the loop may revise with evidence.

| Range | Block | Class |
|---|---|---|
| Q077–Q080 | Remaining preimage detail (file hash, empty files, walk order, directories) | `code`, `spec` |
| Q081–Q100 | Signature envelope and key handling | `external` (scheme, library), `spec` |
| Q101–Q120 | Stream protocol | `code`, `spec` |
| Q121–Q140 | Mount receipts and subordinate versions | `code`, `spec` |
| Q141–Q160 | MongoDB schema and authority | `code`, `measure` |
| Q161–Q180 | Store security, backups, retention | `owner` for retention and cadence; `external` for practice |
| Q181–Q200 | Restore procedure | `code`, `spec` |
| Q201–Q220 | Debian host and systemd | `code`, `external` |
| Q221–Q240 | OpenLock generation | `code` |
| Q241–Q260 | TUI taskbar and console | `spec` |
| Q261–Q280 | Qt client and QTXML reader | `external` (Qt pinning), `spec` |
| Q281–Q300 | Motion, bitmaps, budgets | `measure`, `spec` |
| Q301–Q320 | Legacy families and quarantine | `external` (format archaeology), `code` |
| Q321–Q340 | Migration and compatibility representation | `code`, `spec` |
| Q341–Q360 | Text normalization and canonical serialization | `spec` |
| Q361–Q380 | CUA catalogue and recovery | `code`, `spec` |
| Q381–Q400 | CUA scale and measurement | `measure` |
| Q401–Q420 | Kernel-level and air-gapped authorization | `owner` for authority; `spec` |
| Q421–Q440 | Civilian model | `owner` for taste; `spec` |
| Q441–Q460 | 24-hour acceptance | `owner` |
| Q461–Q480 | Agent API and templates | `code`, `spec` |
| Q481–Q500 | Workflow, health ratchet, evidence, release | `spec`, `owner` for gates |

## Appendix C — carried open questions, reclassified

The 20 questions asked in round 07 but not yet answered became the loop's first batch, not the owner's next round. Two have since closed on repository evidence — `N053` (degraded is a receipt state; `tools/port/store.mjs:24`) and `Q087` (revocation is not representable; `docs/LEDGER.md:124`) — so this table is the seed and `state.json` is the count.

| Id | Question | Class |
|---|---|---|
| N052 | What evidence moves a degraded mount to healthy? | `owner` (acceptance) with `spec` support |
| N053 | Is `degraded` a receipt status or a warning field? | `code`, `spec` |
| N054 | Is the binary wire form canonical or a projection? | `spec` |
| Q077 | Is a per-file hash over bytes or bytes plus path? | `spec` |
| Q078 | Are empty files and empty payloads legal? | `spec` |
| Q079 | Is the walk ordered by path bytes or manifest order? | `spec` |
| Q080 | Does the walk include directory entries? | `spec` |
| Q081 | Detached or embedded signature? | `spec` |
| Q082 | Which signature scheme? | `external` |
| Q083 | Does the envelope cover the manifest only or also the payload root? | `spec` |
| Q084 | Is a timestamp inside the signed bytes? | `spec` |
| Q085 | Are multiple signatures allowed? | `spec` |
| Q086 | Does the envelope carry a key identifier? | `spec` |
| Q087 | Is revocation represented in the store? | `code` |
| Q088 | Does an expired key still verify old signatures? | `spec` |
| Q089 | One key per release or per package? | `owner` (already answered: per release) |
| Q090 | Is the signature stored inside or beside the manifest? | `spec` |
| Q091 | May a signature be added after publish without a revision? | `spec` |
| Q092 | Are signatures versioned independently? | `spec` |
| Q093 | Is a failed signature a refusal or a warning? | `spec` |

## Appendix D — stream protocol block, seeded 2026-11-04

The second block of the spine, seeded after the carried set closed. Same rule as Appendix C: this
table is the seed, `state.json` is the count, and every closure appends a receipt.

| Id | Question | Class |
|---|---|---|
| Q101 | What is the stream's version tag and where does it live? | `spec` |
| Q102 | Does a stream schema bump bump the mount receipt schema? | `spec` |
| Q103 | Are chunks ordered by sequence, and what happens to a gap? | `spec` |
| Q104 | Is resume authenticated? | `spec` |
| Q105 | Are operation ids idempotent, and what does a retry do? | `spec` |
| Q106 | How is truncation detected? | `spec` |
| Q107 | Is finalization explicit or implied by EOF? | `spec` |
| Q108 | Is adoption atomic? | `spec` |
| Q109 | When may the client drop the previous admitted revision? | `spec` |
| Q110 | Are older or newer frames converted on read? | `spec` |
| Q111 | Does the stream carry its own package identity? | `spec` |
| Q112 | Does the manifest travel inline or separately? | `spec` |
| Q113 | What bounds a chunk? | `spec` |
| Q114 | Does the receipt ride the stream? | `spec` |
| Q115 | Who produces the receipt? | `spec` |
| Q116 | What if the receipt names a different revision than the mount? | `spec` |
| Q117 | Does transport encryption affect package identity? | `spec` |
| Q118 | Does a resumed stream re-verify the prefix? | `spec` |
| Q119 | What refusal names an unsupported frame? | `code` |
| Q120 | Is there capability negotiation? | `spec` |

## Appendix E — mount receipts and subordinate versions, seeded 2026-11-04

The third block of the spine. Sixteen of the twenty are settled by the record; the four whose
answer is a judgement rather than a derivation are held open and asked at §8.4, not folded to
keep the block tidy.

| Id | Question | Class |
|---|---|---|
| Q121 | What is the mount receipt's own schema tag? | `spec` |
| Q122 | Does the receipt schema move with the stream schema? | `spec` |
| Q123 | Is the receipt state set closed or open? | `spec` |
| Q124 | Is `degraded` a state or a warning? | `spec` |
| Q125 | Who produces a mount receipt? | `spec` |
| Q126 | Is a receipt authorization to adopt? | `spec` |
| Q127 | What does a receipt bind? | `spec` |
| Q128 | Is the receipt the durable record, or is the ledger row? | `spec` |
| Q129 | Can a receipt be produced without rendering? | `spec` |
| Q130 | Is a parity digest alone sufficient as a witness? | `spec` |
| Q131 | What happens to receipts when a revision is withdrawn? | `spec` |
| Q132 | Are receipts mutable? | `spec` |
| Q133 | Does a receipt count as completion evidence for a ticket? | `spec` |
| Q134 | Is the receipt itself signed? | `spec` |
| Q135 | Does an `absent` receipt exist, or is absent the absence of a receipt? | `spec` |
| Q136 | Is the receipt store the same store as the ledger? | `spec` |
| Q137 | How long are mount receipts retained before the retention action removes them? | `owner` |
| Q138 | May mount receipts leave the machine — published, exported or shared outside it? | `owner` |
| Q139 | What counts as a successful acceptance day? | `owner` |
| Q140 | May the driver witness its own mount and count that as receipt evidence? | `owner` |
