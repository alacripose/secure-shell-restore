"""Append the ingested-sources register to the CUA acceptance document, once.

Append-only on purpose: §10 Pins keeps its number, so no existing cross-reference moves. Writes bytes,
never text mode, because a text write on Windows emits CRLF.
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs" / "SECURE-SHELL-RESTORE@1.CUA-CIVILIAN-ACCEPTANCE.md"
MARK = "## 11. Sources ingested"

BLOCK = """## 11. Sources ingested

Two owner-supplied transcripts are ingested for this document. A transcript is a source, not an
instruction: it may support a premise, and it may not write a rule. Each entry separates what the source
says from what the driver takes, and names what the source refuses to support. Quotes are verbatim; the
pin for each is the document's own name, byte count and date.

### 11.1 World-model transcript (2026-11-04, 14,287 bytes)

Premise only: a body needs an understanding of the world before it can be granted control of one. It is
recorded in full in the architecture document's §8.1 and is not restated here beyond its share of this
register: the civilian acceptance document and that premise are read together.

### 11.2 Dory, NVIDIA's looped transformer (2026-11-04, 15,061 bytes)

**What it says.**

- A 3.97B model whose middle block loops: an input block of 16 layers runs once, a recurrent block of 40
  layers repeats, an output block of 16 runs once. The input block's output is re-added each lap, "like
  the ResNet models".
- The loop count is set at inference — Nvidia calls it "elastic inference compute" — because the output
  block "is trained to read the state after any of the loops. So, one loop, two loops, four loops are all
  valid models".
- Compute per token rises with laps while "the weights in memory don't change at all": 72 effective
  layers at one loop, 112 at two, 192 at four.
- More laps is not reliably better: "it's not a hard and fast rule that one of them will have more output
  tokens", and quality changes "depending on the actual problem". Against Gemma 4 26B the model wins 1 of
  10 benchmarks at one loop, 4 at two, 5 at four — and loses the knowledge benchmarks outright, which the
  source attributes to having fewer weights in which to store knowledge.
- The cost is memory, not weights: a per-loop KV cache is about 2 GB per sequence at 32k context and two
  loops against 1.32 GB in last-loop mode, where Nvidia says accuracy and length stay close.
- Deployment advice: two loops by default, four for harder agentic work, and a router in front to pick
  between them.

**What the driver takes from it — proposed, each needing its own ticket before it changes code.**
A transcript may support a rule; it may not write one, so these are proposals with an exit test each.

| Rule | The proposal | Where it binds | Exit test |
|---|---|---|---|
| E1 | An attempt records the effort it spent, per attempt, not per deployment | the act receipt | a receipt with no effort field is refused by name |
| E2 | Verification must not depend on effort: the postcondition is observed after the act, so a result verified cheaply is verified the same expensively | §2 control cycle | the same act passes the same postcondition at two effort levels |
| E3 | Effort is a declared scope on the ticket, never a knob the driver turns itself | §1, architecture §11 | a driver raising its own effort scope is refused `ticket-scope` |
| E4 | Knowledge claims are refused; the driver observes instead | §5 | an answer asserted from memory is refused as evidence |

**What it refuses to support.** It does not say the driver is, or should be, a looped transformer: it
describes an LLM and never a CUA agent. It does not say more effort improves control — the source says
quality moves "depending on the actual problem" and that it is "not something that I would just sort of
say it's the same as sort of turning up reasoning". It contains no shell operation, no benchmark of one,
and no number that may become a target here: no lap count, latency or token budget in this document is
derived from it.

### 11.3 Named absent

These are the documents that would improve this driver and are not in either tree. Naming them is the
point: each is a place where the driver has one writer and no independent reader.

| Document | What it would supply | Referenced from | State |
|---|---|---|---|
| `ala-civ-bots-prototype/CHECKPOINT.md` | the only running Node CUA driver, and its body-to-action contract (`CHECKPOINT.md:38` is pinned in this record) | `secure-shell/docs/DECISIONS.md` | absent from both trees |
| `income-engine/cua_worker.py` | how a real worker gates an action before performing it | `secure-shell/docs/DECISIONS.md` | absent |
| `AXIS-MODULE.md` §2 | the refusal of mining and the hash lottery | `patches/PATCH-004-five-star-axis.md` | absent |
| `voxel-model/src/proof.rs`, `voxel-package/src/civilians.rs` | the ticking proof, and observe-versus-rule for civilians | `docs/PROOF-OF-WORK.md` | absent |
| `dl-enclave/docs/DRIFT.md` D-3, `CLIENT-UI.md` §8 | a refused mechanism, and the client UI boundary | `patches/PATCH-004-five-star-axis.md`, `docs/DECISIONS.md` | absent |
| a driver action catalogue | the capabilities `server/axis-driver.mjs` declares, as a document a second reader can check | nothing: it does not exist | absent — `secure-shell/packages/` holds `axis/` and `toast/` only |
| a driver receipt schema | `RECEIPT_SCHEMA` in `server/axis.mjs`, which has no second reader | `server/axis.mjs` | absent |

The last two are this driver's own gaps rather than another project's: its capability set and its receipt
shape each have exactly one writer, which is the condition this family refuses.
"""


def main() -> int:
    raw = DOC.read_bytes().decode("utf-8")
    if MARK in raw:
        print("present: the sources register is already appended; nothing written")
        return 0
    if not raw.endswith("\n"):
        print("refused: document does not end with a newline")
        return 2
    merged = raw + "\n" + BLOCK
    DOC.write_bytes(merged.encode("utf-8"))
    print("appended: '## 11. Sources ingested' (%d chars)" % len(BLOCK))
    print("cr present: %s" % ("\r" in merged))
    print("ends with newline: %s" % merged.endswith("\n"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
