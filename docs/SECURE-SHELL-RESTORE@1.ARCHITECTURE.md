<!-- Continuation of the SECURE-SHELL-V2 planning set. Written after the 20 owner decisions and the four follow-up rulings recorded in docs/answers.txt. No repository was modified; no implementation or client witness is claimed. -->

# SECURE-SHELL-RESTORE@1 — architecture

**Document identity:** `SECURE-SHELL-RESTORE@1`
**Canonical form (release time):** `SECURE-SHELL-RESTORE@1+blake3:<content-hash>`
**Status:** Accepted direction. Supersedes `SECURE-SHELL-V2-ARCHITECTURE.md` as the working architecture; the V2 files stay in `docs/` as the pre-decision record.
**Release name:** **Restore**. The first version is not a renderer upgrade. It rebuilds the Debian store and streams the first desktop from it.

A document cannot carry its own BLAKE3 hash in its filename: the hash would have to be computed over a name that contains it. Release identity is therefore assigned by CI at packaging time and recorded in the release manifest. `:` is also illegal in Windows paths, so document filenames stop at `@<revision>` while the canonical `+blake3:` form lives in the manifest and in every ledger row that cites the document.

## 1. What the owner rulings changed

| # | V2 proposal | Restore position (settled) |
|---|---|---|
| 1 | Identity and naming open | `secure-shell` keeps its identity; every artifact pins its version and hash in its name |
| 2 | Coordinated vs independent versions open | Independent revision per component; the name also pins what it compiled against |
| 3 | MongoDB authority open | MongoDB is **mandatory** outside CUA-provided scratch workspaces |
| 4 | Topology open | Debian provides everything; first release is **Restore** — rebuild the database on Debian and stream the basic TUI desktop first |
| 5 | Security conditions open | Encrypted storage, authenticated service identities, append-only event permissions, verified backups: **all mandatory** |
| 6 | Integrity algorithm open | Fast, stateful, network-streamable, small-device-capable, massively scalable, operable by trained CUA: **BLAKE3** identity |
| 7 | Signing authority open | **The Debian server** |
| 8 | Stream vs `surface.mount/2` open | The stream **carries mount receipts** as an independently versioned subordinate contract |
| 9 | OpenLock generation open | **Yes** — the programmatic shell from OpenLock begins the Debian store regeneration |
| 10 | Qt meaning open | **Qt 6**, exact version pinned per release through GitHub CI; must carry motion and bitmaps |
| 11 | Display ownership open | Server sends declarations and content only; the local desktop owns rendering, focus, input, CUA observation |
| 12 | SWF boundary open | SWF importer is **examples**, isolated behind the streamer API |
| 13 | Planet removal open | `planet-*` **quarantined** as a legacy decoder during migration |
| 14 | Legacy policy open | Legacy packages become an explicit compatibility representation, then are rewritten into the new format |
| 15 | Split families open | Read from the committed audit: pre-split and post-split families are named with distinct identifiers, refused by name, never auto-detected |
| 16 | Normalization open | **Yes** — UTF-8, declared newline policy, canonical serialization; conversion only through recorded migrations |
| 17 | CUA responsibilities open | **Yes**, and wider: boot, recovery, health, format identification, mount, migration verification, then system-level streaming coverage |
| 18 | Agent API open | **Yes** — generated template plus capability-scoped manifest streamed from the internal store, without mounting the desktop |
| 19 | Civilian verification open | Civilians are the model for CUA agents; `cellular_generativity_axis_civilian_expectations_prototype_rechecked` is the current representation |
| 20 | Daily acceptance open | **24-hour continuous simulation** |

Four follow-up rulings are equally binding:

- **R-A · Identity grammar.** `package-name@<monotonic-integer-revision>+blake3:<content-hash>`.
- **R-B · Revision.** Monotonic integers only. Semantic versions never appear in package identity; API and compatibility versions are tracked separately.
- **R-C · BLAKE3 coverage.** The digest covers the complete canonical package content — manifest, declared dependencies, schemas, payload bytes after deterministic serialization — and **not** transport framing, encryption, or the Debian signature envelope.
- **R-D · Health gate is not the work.** A slow gate that drifted into scratch Python scripts and repeated improvised tree scans is the failure being corrected. Verification tools are versioned capabilities of the driver, and checks are **incremental** (changed components plus dependency closure) with full-tree audits only at release gates and the scheduled 24-hour run.

## 2. Naming and identity

### 2.1 Canonical package name

```
name@<rev>+blake3:<64 lowercase hex>
```

- `name` — lowercase, hyphen-separated, no version inside it. A name is a lineage, not a release.
- `rev` — monotonically increasing integer, starting at 1, never reused, never renumbered. Any change to a byte inside the hashed preimage increments it. A rebuild that produces identical bytes does not.
- `blake3:<hash>` — the content identity from R-C.

Examples of the shape only (no hash here is a real package):

```
secure-shell-store@1+blake3:<hash>
secure-shell-openlock-shell@3+blake3:<hash>
secure-shell-qt-client@2+blake3:<hash>
secure-shell-axis-cua@1+blake3:<hash>
```

### 2.2 The pin-complete name

Decision 2 requires the name to pin what the artifact compiled against. The canonical name is the short form; builds, tickets, and ledger rows use the pin-complete form:

```
name@<rev>+blake3:<hash>(dep-a@<rev>+blake3:<hash>, dep-b@<rev>+blake3:<hash>)
```

The parenthesised set is ordered by dependency name, contains no duplicates, and is part of the build record — not part of the content hash. A package built against a different dependency revision is a different build with the same content identity; the ledger must never conflate the two.

### 2.3 Document identity

```
SECURE-SHELL-RESTORE@<rev>.<KIND>.md
```

`KIND` ∈ `ARCHITECTURE`, `IMPLEMENTATION-PLAN`, `FORMAT-IMPORT-AUDIT`, `CUA-CIVILIAN-ACCEPTANCE`, `AGENT-BOOTSTRAP-API`. Documents are planning artifacts, not streamed packages: they carry no payload, so they take `@rev` now and the `+blake3:` pin at release. A document revision bumps when a settled decision changes, not when prose is edited.

### 2.4 What the hash does not do

BLAKE3 proves byte identity. It does not prove authorship, safety, correct rendering, or admission. Those are separate steps, in this order: content identity → Debian signature → admission verdict → stream → client mount → client witness. A hash never substitutes for any later step, and no later step may re-derive the hash with different rules.

## 3. Component map

```
                 ┌────────────────────────── Qt 6 client (sole display) ─────────────────────────┐
                 │ window manager + taskbar + console window · focus · input · CUA observation    │
                 │ witness surface: command · exit status · checks · surface · digest             │
                 └───────────────▲───────────────────────────────────────────▲────────────────────┘
                                 │ signed stream (chunks, receipts)          │ bounded API
                 ┌───────────────┴───────────────┐            ┌──────────────┴───────────────┐
                 │ package streamer              │            │ Axis System-1 CUA driver     │
                 │ BLAKE3 + Debian signature     │            │ tickets, postconditions      │
                 └───────────────▲───────────────┘            └──────────────▲───────────────┘
                                 │                                           │
                 ┌───────────────┴────────────────── Debian host ─────────────┴───────────────┐
                 │ MongoDB (mandatory authority; systemd-managed, systemd-creds)               │
                 │ package objects · revisions · admission · receipts · activity ledger        │
                 │ OpenLock-generated shell declarations → TUI taskbar + debian console        │
                 └─────────────────────────────────────────────────────────────────────────────┘
```

Ownership is unchanged from the family rules: one reader per format, one display implementation, one store, client as the only test surface, verdicts issued by the server and rendered by the client.

## 4. Debian store

### 4.1 Authority

MongoDB is the canonical durable record on the Debian host. The only exempt case is a CUA-provided scratch workspace, and a scratch workspace can never be promoted to authority — its results must be re-admitted through the store.

This supersedes the `No MongoDB ... derail` line in `secure-shell/docs/ARCHITECTURE.md`. That line is a branch position, not a Restore requirement; `docs/secure-shell-audit/cell-schema-ruling.md` already recorded the same resolution and moved credentials to `systemd-creds`.

### 4.2 Restore, the first release

Restore means: rebuild the database on the Debian host from declared inputs, then stream the basic TUI desktop first. Not a migration wizard, not an incremental upgrade — a reproducible reconstruction with a digest of the result. The sequence is the acceptance test:

1. OpenLock generation produces the shell's declarations and generated assets.
2. The Debian store is rebuilt from those declarations plus the declared base set.
3. The TUI taskbar and the default console window (the actual Debian console, streamed securely through the format) are admitted and streamed.
4. The Qt client mounts them and witnesses.

A restore that cannot be repeated on a clean host is refused, not "mostly working".

### 4.3 Conditions of admission

Mandatory, not aspirational (decision 5):

- encrypted storage at rest, with per-package keys per the recorded ruling (one key per package, no master);
- authenticated service identities — no unauthenticated local socket accepted as a production path;
- append-only permissions on event collections; corrections are new rows naming the row they correct;
- verified backups, with a restore drill whose result is a stored artifact, not a claim.

Replica-set support is designed in; the first implementation may be a single Debian instance. The topology decision was answered as "Debian provides everything", so a second host is a later scaling step, and no component may assume a replica set exists.

### 4.4 What the store holds

Catalogue identity, content identity, revisions, signer, admission verdict, receipts, lifecycle, activity rows. Payloads are immutable content-addressed objects; MongoDB holds the records and the transaction boundary. One authoritative write path — a sidecar database is refused by name.

## 5. Package integrity

Per R-C, the digest preimage is the canonical content only:

```
blake3(
  canonical_manifest            # name, rev, dependency identities, schema ids,
                                # declared vocabulary, entry points, lengths
  || canonical_declared_deps
  || canonical_schema_set
  || payload_bytes_after_deterministic_serialization
)
```

Excluded, deliberately: chunk framing, compression, AEAD nonces and tags, the Debian signature envelope, timestamps, and the hash itself. This is the point of the upgrade — identity must survive re-encryption, re-chunking, and re-signing, so a package can be streamed over different transports without becoming a different package.

Chunk digests are a transport concern, computed under their own domain, and never confused with package identity. A chunk that verifies proves bytes arrived; only the package digest proves the package is the one admitted.

## 6. Signing

The Debian server is the signing authority (decision 7). Signing is separate from identity and separate from admission:

| Layer | Question | Owner |
|---|---|---|
| Content identity | Are these the bytes? | BLAKE3 over canonical content |
| Signature | Did the Debian server assert this revision? | Debian signing key, over a domain-separated manifest |
| Admission | Does policy accept it for this receiver? | Server policy, recorded as a verdict |
| Mount | Which revision did the client adopt? | Client receipt, subordinate contract |
| Witness | What did the client actually render and check? | Client |

Key custody and rotation remain open (OPEN-KEY-1). Ed25519 is the working suite because `dl-enclave.sig/1` already uses it for ledger checkpoints; adopting it for packages is a compatibility choice the owner may supersede.

## 7. Stream contract

The stream is `secure-shell.stream/1`. It carries canonical package bytes, chunk manifests, and — per decision 8 — mount receipts as an **independently versioned subordinate contract**. `surface.mount/2` keeps its own version and its own reader.

Consequences that must hold:

- A stream schema bump does not bump the mount receipt schema, and vice versa.
- A receipt is evidence of adoption, not authorization to adopt.
- Ordered bounded chunks, authenticated resume, idempotent operation ids, truncation detection, explicit finalization, atomic adoption.
- The client keeps the previous admitted revision until digest, signature, schema, compatibility, and client-surface checks pass.
- Older or newer frames are refused by name with `found` and `supported`, never converted on read.

## 8. From OpenLock to the first streamed desktop

The first deliverable is generated, not hand-written: the programmatic shell from OpenLock begins the Debian store regeneration. Source selection must name the actual files (`openlock_shell.xml`, `openlock_shell.js`, delivery scripts, generators, manifest, landing theme) in the selection record, with rejected alternatives.

The first surface is the TUI taskbar plus the default console window — the real Debian console, streamed through the format rather than exposed as an out-of-band channel. The taskbar also carries the CUA development state: spinning loaders for components the driver is developing or that the agent has requested for training, so work in progress is visible instead of implied.

Only after that first window is mounted and witnessed does a second window start.

### 8.1 The Debian axis shell and its node drivers

The restore grade's first deliverable is the axis: the Debian-side authority every CUA node driver must
pass through. It is code in the `secure-shell` checkout, not a claim this document makes on its behalf.

| Piece | Path | What it is |
|---|---|---|
| Axis core | `server/axis.mjs` | driver registry, attestation, ticket gate, receipts |
| HTTP edge | `server/axis-server.mjs` | loopback-by-default endpoints for drivers on the host |
| Core checks | `server/test/axis.test.mjs` | the gate, the lapses, the learning digest |
| Edge checks | `server/test/axis-server.test.mjs` | the same refusals over a real socket |
| Driver | `server/axis-driver.mjs` | the node driver: ticket first, then the act |
| Driver checks | `server/test/axis-driver.test.mjs` | ordering, lapses, and a refused bundle |
| Unit | `deploy/secure-shell-axis.service` | systemd, no capabilities, read-only home |
| Installer | `deploy/install-debian.sh` | refuses to run without root; installs and enables |

**The gate.** A driver that presents no ticket is refused `cua-unticketed` before anything runs; the
wording of that refusal belongs to the failure model in §11, and this section only says which code
implements it. A ticket names one driver, one action and one scope, is issued only for a capability the
driver declared, expires, and cannot carry a different action. An attestation that lapses between ticket
and act refuses the act instead of letting it finish on a stale grant. The module's complete refusal set
is its exported `CODES`; it is the single enumeration, and it is not copied here.

**The driver, and what it refuses to claim.** The node driver declares `witness` and `learning-apply`,
and deliberately does not declare `kernel`. It hashes a path on the device and applies a learned bundle
under its own state root, and it does neither until the axis has issued a ticket for that exact action
and the act has been reported: authorization first, device second, so a refusal leaves the device
untouched rather than half-touched. A bundle that is not UTF-8 text is refused by name instead of being
mangled, because the act carries text today and a driver that silently transcoded a lesson would be
replicating something the axis never authorized. A witness receipt carries the digest it witnessed, so
the record says what was seen rather than only that something happened.

**Securing itself over time.** Attestation carries an expiry. When it lapses the driver is untrusted,
new tickets are refused, and `review()` names every driver awaiting re-attestation; re-attestation
restores trust without re-registering the driver. That is the internal driver model securing the shell
over time rather than once at install: grants are short-lived and renewal is an explicit act.

**Learning replicated under the same gate.** `learning-apply` is a ticketed act like any other, and it
applies only when the bundle's bytes hash to the digest the axis was given. A device cannot be taught by
a bundle that was never authorized, and bytes that changed in flight are refused by name rather than
applied.

**Scope, stated honestly.** `kernel` is a declared scope and a refusal boundary, not a privilege the
axis exercises. Nothing in this code performs a kernel write, and nothing here claims to. What it
guarantees is narrower and checkable: a kernel-scoped action cannot be requested by a driver that did
not declare `kernel`, and cannot run unticketed. The unit file grants the service no capabilities at
all for the same reason.

**Audit source.** The restore grade's premise was audited against the transcript *The Rapid Progress of
Realtime Simulations* (owner-supplied, 2026-11-04, 14,287 bytes). It supports exactly one premise:
that a body needs an understanding of the world before it can be granted control of one — "when we
finally give AI bodies that it can control, it will understand how it can interact with the world for
itself". It is a commentary on world-model progress, not a design document, and no requirement here is
attributed to it beyond that premise.

**Absent, and recorded as absent.** `systemd-analyze` is not installed on this Windows host
(`command -v systemd-analyze` exits non-zero), so the unit file has not been validated by systemd here
and is not reported as valid. The module checks are module checks: by AV-001 they are not a client
witness and may not be cited as one.

## 9. Qt client

Qt 6, exact version pinned per release through GitHub CI. The release ticket re-verifies the current LTS at pin time; this document does not float a version. The client must carry motion and bitmaps — the capability the SWF importer was reaching for — under declared budgets, not as an escape hatch.

QTXML meaning: the dialect — Qt Widgets with XML-defined UI, Qt Quick/QML, or a hybrid — stays open (OPEN-QT-1). What is already settled is that one reader and one renderer own it, XML is declarative and bounded, no embedded script, no plugin loading, no direct motor calls, and unknown or duplicate fields refuse by name.

Display ownership (decision 11): the server transmits declarations and content. It never owns focus, input, layout, or observation.

### 9.1 A question is not open until it is asked

The client owns rounds, not a question queue. A question only the owner can answer is recorded as open
**and** presented as a round through the client's own surface. An open question that exists only in a
document is a client defect, not a pending item: it looks like work in progress while being invisible
to the person who has to answer it.

**The gate is code.** `shell/openlock/panorama/scripts/secure_shell_rounds.js` reads a round and refuses
it by name before the client may draw it or report it finished. `tests/rounds.test.mjs` runs it. The
refusal set is closed and is the same set the module exports as `CODES`:

| Code | Refused when |
|---|---|
| `round-format` | the record is not a `secure-shell.round/1` record, or a question has no id, or an id repeats |
| `round-state` | a question carries a state outside `open`, `answered`, `struck`, `folded` |
| `round-question-unasked` | an open question has no recorded ask call; the round cannot be reported complete |
| `round-no-effect` | a question does not say what the answer changes |
| `round-closure-unsubstantiated` | an `answered`, `struck` or `folded` question carries no recorded basis |
| `round-words-invented` | an answer quotes words the owner is not recorded saying |
| `round-question-dropped` | a question disappears between two revisions of a round without a closure |

`assertComplete` is the ask-before-complete gate: a round may complete while questions are still open,
because an open question is waiting rather than finished, but it may not complete while an open question
was never asked. `renderRound` returns only validated rows, so a question cannot be drawn as answered
without words that survive the check, and `reconcile` refuses a question removed without a closure.

**Absent, and recorded rather than inferred.** There is no `client/` source tree in the `secure-shell`
checkout: `ls -la client` reports an empty directory (only `.` and `..`) and there is no `package.json`
at the repository root. The gate therefore lives beside the executable client reader under
`shell/openlock/panorama/scripts/`. A future `client/` must require this module, not restate the rule;
a second implementation of the same check would be the second reader this family refuses everywhere
else.

**What the gate does not do.** It does not deliver a round to the owner, does not draw one, and does not
know whether an ask call reached anyone. Those are the client's job. The gate makes the bad state
unrepresentable: a round that was never asked cannot be read, drawn or completed.

## 10. Axis CUA as a system, not a screenshot tool

The driver owns boot, recovery, health, format identification, mounting, and pre/post-migration verification, with every action ticketed, bounded, and witnessed. The ratchet measures how much of the system is **streamed versus legacy**, so the driver's progress is a number with evidence rather than a narrative.

Scope extends past the client: the same driver works through the installed system over time, adding package cells and windows to the stream, down to kernel-level operations on an air-gapped host managed over the network — a real security-enhanced authorization system driven by a System-1 model. That ambition is staged, not assumed; the staged gates are in `SECURE-SHELL-RESTORE@1.CUA-CIVILIAN-ACCEPTANCE.md`.

Performance and scale are requirements, not hopes: thousands of workers, with `ala_civ_bots_prototype` as the scale test that was actually run.

## 11. Failure model

| Condition | Result |
|---|---|
| Content changed under the same revision | `package-content-mismatch`; refused; new revision required |
| Signature absent or unverifiable | `package-unsigned` / `package-signature-invalid`; never mounted as verified |
| Digest valid, policy denies | `package-not-admitted`; identity is not authorization |
| Frame schema older/newer | `frame-schema` with `found` and `supported`; no conversion |
| Stream truncated | `stream-truncated`; no adoption, previous revision stays |
| Receipt names a different revision than the mount | `receipt-mismatch`; the mount is indeterminate, not successful |
| Store unavailable | `store-unavailable`; no silent fallback to a file store |
| Restore not reproducible | `restore-not-reproducible`; release refused |
| CUA action without ticket | `cua-unticketed`; action refused before execution |
| Health check never run | `absent`, reported as absent — never as a pass |

## 12. Decisions resolved by hypergrilling

Round 01 (Q001–Q020) closed most of the open list. Resolved items keep their id so citations do not break.

| Id | Status | Ruling |
|---|---|---|
| OPEN-KEY-1 | resolved (Q009, Q010) | Key file under `systemd-creds`, rotated per release |
| OPEN-KEY-2 | resolved (Q011) | Store-level key for rows spanning packages |
| OPEN-STORE-1 | resolved (Q012) | Replication deferred past Restore; designed in |
| OPEN-STORE-2 | resolved (Q013) | Ledger exists as a Mongo collection and as an export; Mongo is authoritative |
| OPEN-QT-1 | resolved (Q014, N001) | All QTXML dialects supported through one reader over a common intermediate; no motion is a refusal; miniaturized targets carry their own declared budget |
| OPEN-QT-2 | resolved (Q015) | Frame-rate floor plus a bitmap memory cap per surface |
| OPEN-FMT-1 | resolved (Q007, N006, N007) | **No default ceiling** — every package declares its size. The declared size streams with the manifest, the server or device reports available space honestly, and a package that overruns its declaration is cut off. Hard ceiling raised to 64 GiB |
| OPEN-CUA-1 | resolved (Q016) | Driver proposes catalogue entries; owner approves |
| OPEN-CUA-2 | resolved (Q017, N015, N016) | Design bound is tens of billions. Default 1,000, settable from 1 upward behind a checkbox and warning window, capped at 1,000 until log incremental runs are verified on that hardware |
| OPEN-API-1 | resolved (Q018) | MCP over stdio |

Still open, but no longer put to the owner as a question queue: the remaining spine is worked by a CUA driver under the tick contract in `SECURE-SHELL-RESTORE@1.HYPERGRILL.md`, which classifies each question by who may close it. Owner-only residue is named there in §6.

### 12.1 Package grade

A package carries a **grade** alongside its name and revision, as an enumerated manifest field. `restore` is both a streamable package and a grade.

**Superseded reading (S-001).** The Q031-era note that Secure Shell adopts OpenLock's `dev`, `player` and `oserver` grades is replaced by the N037 ruling: those grades belong to OpenLock's shell, `observer` among them, and Secure Shell needs its own installation-grade axis. The grade set is open and extended by ruling, so the schema must tolerate additions without a format break.

**Resolved (N042, N044).** The axis is `install` and `os` for now, with further grades added by ruling. An unknown grade is accepted with a warning rather than refused, so a newer artifact still mounts on an older client.

### 12.2 First deployment target

Recorded by ruling (N022, N034): the owner's own machine is x86, so the first Restore runs as a WSL Debian shell there. x86 is therefore not reached through miniaturization; miniaturization stays the path for older formats and devices, which is a separate claim.

### 12.3 Declared size

Recorded by ruling (N006–N020). No default ceiling exists: every package declares its size, the declared size streams with the manifest, the server or device reports available space honestly, options are offered as a chooser, and any overrun above the declaration is a refusal (`declared-size-exceeded`). Space is checked both before the stream opens and during it. The hard ceiling is 64 GiB for every target class.

### 12.4 Family versioning

Recorded by ruling (Q037, Q049, N043): the family is a versioned artifact shipped as the package `secure-shell-family`. A package cites a family revision at or below the current one, never above it.

### 12.5 Recorded tensions

All four recorded tensions are resolved; none is open.

`T-001` (N040): a hotfix adds a name to the same lineage and the counter carries across, so one name still maps to one lineage. `T-002` (N041): a promoted prerelease takes a new stable number and its old number stays spent. `T-003` (N046): Q051 relaxes to "bytes or metadata differ", which makes a duplicate-content revision legal. `T-004` (N047, `S-002`): the revision leaves the BLAKE3 preimage, so renumbering cannot disturb a hash.

### 12.6 Brand constraint

Owner ruling 2026-11-04: Secure Shell is never shortened to an initialism, in code, documents, UI or conversation. The minimum display form carries a pinned hash — `S {PINNED HASH} hell` as dictated — whose exact rendering is question N048. Until that is answered, every document here spells "Secure Shell" in full.

### 12.7 Revision rules

Recorded by ruling (Q041–Q062). Revisions start at 1, are decimal digits with no leading zeros, are never reused, stay retired forever once withdrawn, and are monotonic per lineage across renames. A rollback is a new revision rather than a decrease. A revision requires a content change (Q051), though Q052 permits identical content, leaving `T-003` open. Withdrawal stops new pins but a pinned consumer still resolves. `latest` is derived at read time, never stored. The ceiling is 2^64. The revision is **not** part of the BLAKE3 preimage (`S-002`); the signature binds name, revision and hash instead, which is where renumbering is made safe. The hash covers canonical bytes, and the stored form must match the canonical form or the package is refused.

### 12.8 BLAKE3 preimage

Recorded by ruling (Q063–Q076, N047). The output is the full 32 bytes, untruncated. The preimage begins with a fixed domain-separation tag, then a layout version, then the canonical manifest bytes; the payload is referenced by its own hash rather than hashed in line. Canonical serialization sorts object keys by byte order, permits integers only, and is JSON on disk with a binary projection on the wire. The payload is a Merkle tree over files with per-file hashes recorded, so a single file can be verified without rehashing the package. The package name sits in the manifest header; the family revision and the grade are both inside the preimage, so regrading or retargeting an artifact changes its identity. Mount receipts use the same canonical routine under a different domain tag. The hash covers the package alone; dependencies are pinned by their own hashes.

### 12.9 Receipt states

Resolved against the existing store (N053, closed by code evidence). A receipt carries a **closed state set** plus a separate refusal code; there is no warnings field. `degraded` therefore enters the state set rather than being attached as a warning, and it must name its cause in `refusal` — a non-applied state without a refusal code is already refused by the existing row validator. This makes N050's "degraded until it proves itself" expressible with no schema change: degraded is non-applied, so the applied-row and floor logic already exclude it and the refusal query already returns it.

Open finding from the same pass (Q087): revocation is **not** representable today. The ledger holds one generated Ed25519 checkpoint key pair with no history and no expiry, and the signature envelope's `key-id` is never consulted. Restore must add a revocation record and key history; until then, rotation is a file replacement that retires nothing retroactively.

### 12.2 First deployment target

Recorded by ruling (N022): the owner's own machine is x86, so the first Restore runs as a WSL Debian shell there. x86 is therefore not a downstream target reached through miniaturization; miniaturization remains the path for older formats and devices, which is a separate claim.

### 12.3 Declared size

Recorded by ruling (N006–N020). No default ceiling exists: every package declares its size, the declared size streams with the manifest, the server or device reports available space honestly, options are offered as a chooser, and any overrun above the declaration is a refusal (`declared-size-exceeded`). Space is checked both before the stream opens and during it. The hard ceiling is 64 GiB for every target class.

## 13. Evidence pins

Read through the GitHub integration on 2026-11-04. These pin what this document was written against.

| Artifact | Pin |
|---|---|
| `alacripose/secure-shell` main tree | `124b6471891d14038f4402d52598ff1c4357a18a` |
| `secure-shell/docs/FORMAT-SOURCES-AUDIT.md` | blob `61cd33413e8510e95f1e4bc4e3251c8c258926dc`, 85,859 B |
| `secure-shell/docs/ARCHITECTURE.md` | blob `b3d52576b595446dd67d7309a83fedabdeec5965`, 8,517 B |
| `secure-shell/AGENTS.md` | blob `7cfa4e5bfe8f817baa09a687a0b1751b9679487d`, 15,540 B |
| `alacripose/swf-cell-runtime` main tree | `141bb5da43eb4062ba8938c019f2df20de9079d2` |
| `swf-cell-runtime/docs/secure-shell-audit/cell-schema-ruling.md` | blob `526928543625095ef99961eff8e1bda76fe75d1d`, 8,260 B |
| `swf-cell-runtime/docs/secure-shell-audit/secure_shell_synthesis.md` | blob `579afe0ec452d8dee615667e2dd50aeabffd7ff8`, 58,334 B |
| `swf-cell-runtime/docs/cellular_generativity_axis_civilian_expectations_prototype_rechecked.md` | blob `5af5d32388795767f02b709dbd8479eb110645c3`, 144,027 B |
| `swf-cell-runtime/crates/planet-package/Cargo.toml` | blob `43628df92f937db3dec2436246a7ead72525f39c`, 329 B |

The audit committed at `swf-cell-runtime/docs/secure-shell-audit/` is the source of record for the pre-split/post-split question (decision 15); this document cites it rather than restating its census.
