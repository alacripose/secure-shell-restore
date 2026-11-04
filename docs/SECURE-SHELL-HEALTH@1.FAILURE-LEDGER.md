<!-- Health-and-policy record. Owner ruling A-14, 2026-11-04: failures are tracked while working in true-autonomy mode so the trained CUA axis driver can understand the agent's failure shape before it is trusted with git. Append-only. A row is added, never rewritten. -->

# SECURE-SHELL-HEALTH@1 — agent failure ledger

**Document identity:** `SECURE-SHELL-HEALTH@1`
**Kind:** FAILURE-LEDGER
**Status:** Open record. Append-only. One row per observed failure, with its evidence and the correction that was actually applied.

## 1. What this record is

The owner ruled (`A-14`, 2026-11-04) that an agent working in true-autonomy mode must track its own
failures as part of health and policy, so that the trained CUA axis driver can learn the agent's
failure shape before the agent is trusted to use git itself.

It is a record, not a confession and not a score. It does not clear a refusal, does not restore a
check that failed, and does not promote the agent. Each row states what happened, the evidence that
it happened, what it cost, and what changed so that it cannot happen the same way twice. A repeat of a
row already in this table is a ratchet regression, and the ratchet only tightens.

## 2. Rows

| Id | Failure | Evidence | What it cost | Correction applied |
|---|---|---|---|---|
| `AF-01` | Hand-rolled a second reference scanner (`tools/collect_references.py`) instead of forking the family's `scan_drives.py` | owner: "so what the fuck are you doing if you're not just going to fork the already existing project scanner" | a second, weaker walker with its own conventions, and a document citing it | forked to `tools/scan_drives_reaudit.py`; the hand-rolled tool and its JSON were deleted |
| `AF-02` | Presented a nine-folder, depth-limited pass as the reference inventory | the first synthesis listed 3,377 files from `Documents` only, with no drive section | a coverage claim the scan could not support, delivered as if it were complete | re-ran across 16 project roots plus `C:`, `D:`, `E:`, `F:`, `H:` — 68,629 files, 21 root sections, each carrying `truncated:` |
| `AF-03` | Left `G:` unopened and called the run complete | `scan_state@2026-11-04.json` names the budget stop; no `G:` section exists | one drive unread while the totals read as whole | recorded as `audit-unstreamed`, not as coverage; the bound is stated in the document |
| `AF-04` | Two `SyntaxError: unterminated string literal` failures from escaping backslashes through heredocs and patches | the tracebacks, twice, in this workspace | two wasted units and a half-written file | path separators are built with `chr(92)`, output handles use `newline=chr(10)` |
| `AF-05` | Wrote the synthesis in text mode, producing CRLF on Windows | `hg_check11.py` line-ending assertion | an LF check that failed on files the agent had just written | `newline=''` on write, then `.cache/normalize_lf.py` as a check rather than as a fix |
| `AF-06` | Carried a digest for `SECURE-SHELL-HEALTH@1.HYPERGRILL.md` computed before that file was next edited | `hg_check11.py`: `every digest verifies: [...HYPERGRILL.md]` | a document asserting a hash the file no longer had | edit before scan, rescan after every edit; the check now fails rather than warning |
| `AF-07` | Kept a superseded second writer (`docs/hypergrill/references@2026-11-04.json`) alive after the document replaced it | two artifacts claiming the same reference set | one fact with two owners | deleted; the scan stream is the only machine-readable copy |
| `AF-08` | Interrupted mid-cleanup and left a known-bad tree with no written state | the restart turn had to re-derive state by reading files | the work stopped being resumable from its own record | this ledger, plus the round record in `HYPERGRILL.md` §8.8, so state is read rather than rediscovered |
| `AF-09` | Asked the owner a question the record already answered, in the first version of the v2.4 round | the pre-ask draft asked whether the sixth star exists; `PATCH-004-five-star-axis.md` records `star.count: 6` | one question of a five-question budget | the round premise is read from the pinned file before the question is written |

| `AF-10` | A cancelled tool call killed the scanner mid-walk, and the document it had already truncated stayed truncated | the `Totals` line reads "files inspected: 28118 · elapsed: 290s" over an inventory that had held 68,629 files and 6,000 references; the same commit carries the 356 KB partial | the record asserted a partial inventory as the whole, and commit `3c3540a` captured it | the scanner now writes to a temporary path and renames only after the run completes, so a killed run cannot replace a complete document; a partial `Totals` block is refused as evidence |
| `AF-11` | Committed 29 `.cache` entries into a public tree, including one-off emitters and a nested `secure-shell` checkout | `git ls-tree -r HEAD` counts 29 paths under `.cache/`, among them `append_86.py` and `emit_v2_client.py` | scratch scripts published as if they were the project, plus a nested checkout that is not a package of this repository | `.gitignore` tracks only `.cache/hg_check*.py` and `.cache/normalize_lf.py`; the rest is ignored and removed from the index |
| `AF-12` | Ran one five-minute command that scanned, checked, committed and pushed, so the cancellation landed mid-sequence with no written state | the partial-run error, then `git ls-remote origin` returning no refs while the local commit claimed the unit was recorded | the push never happened and the commit could not be trusted as the state of the unit | long runs are backgrounded with a log and an exit status; the unit is committed only after its checks pass, and the push is its own step |

Nothing in this table was closed by the agent's own report. Each correction names the file, the check
or the owner's words that carry it.

## 3. What the driver should take from it

| Pattern | What it predicts | Where it will show first |
|---|---|---|
| Coverage inflation | the agent describes the part it scanned as the whole | any audit, any scan, any "all references" claim |
| Second writer | the agent builds a parallel artifact rather than forking the family's | any new tool that duplicates an existing one |
| Unverified assertion | the agent states a hash, a count or a mount it did not recompute | package identity, receipts, `held`/`absent` claims |
| Silent resumption | the agent restarts work without reading its own record | across a disconnect, a restart or a new session |

The detector for all four is the same and it is not prose: a check that recomputes, a refusal that is
stored, and a record that is read before the work is resumed.

## 4. What this record does not do

- It does not make the agent trustworthy; only the driver's verification and the owner's ruling do.
- It does not substitute for `handoff-absent` (`A-12`): the unit still closes only with a second
  agent's verification receipt.
- It does not record an owner failure, a family repository's defect, or a vendor's bug. Those get their
  own records.
