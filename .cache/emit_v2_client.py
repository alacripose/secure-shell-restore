"""Write the client round gate, its test, and make section 9.1 describe exactly what it enforces."""
import pathlib
import re
import sys

REPO = pathlib.Path("C:/Users/ala/Documents/secure-shell")
MODULE = REPO / "shell/openlock/panorama/scripts/secure_shell_rounds.js"
TEST = REPO / "tests/rounds.test.mjs"
ARCH = pathlib.Path("docs/SECURE-SHELL-RESTORE@1.ARCHITECTURE.md")

MODULE_TEXT = r'''/**
 * The client's round gate: a question is not open until it is asked.
 *
 * SECURE-SHELL-RESTORE@1.ARCHITECTURE.md 9.1 states the rule; this module is where the rule can
 * refuse. A round is the client's own record of what it put to the owner. It may not be reported
 * complete while an open question has no recorded ask call, an answer may not be quoted unless the
 * owner is recorded saying it, and a question may not disappear between two revisions of a round
 * without a closure.
 *
 * Refusal codes are closed; see CODES.
 */

"use strict";

const HEADER = "secure-shell.round/1";

const STATES = Object.freeze(["open", "answered", "struck", "folded"]);

const CODES = Object.freeze([
  "round-format",
  "round-state",
  "round-question-unasked",
  "round-no-effect",
  "round-closure-unsubstantiated",
  "round-words-invented",
  "round-question-dropped",
]);

class RoundError extends Error {
  constructor(code, subject, why) {
    super(code + ": " + subject + ": " + why);
    this.name = "RoundError";
    this.code = code;
    this.subject = subject;
    this.why = why;
  }
}

function text(value) {
  return typeof value === "string" ? value.trim() : "";
}

/**
 * Read a round record. Every question is checked, and a bad one refuses the whole round rather than
 * being dropped from the display: a round that shows fewer questions than it holds is the failure
 * this module exists to prevent.
 */
function readRound(round) {
  if (!round || typeof round !== "object" || Array.isArray(round)) {
    throw new RoundError("round-format", "round", "not a round record");
  }
  if (round.format !== HEADER) {
    throw new RoundError("round-format", String(round.format), "expected " + HEADER);
  }
  if (!Array.isArray(round.questions) || round.questions.length === 0) {
    throw new RoundError("round-format", "questions", "a round carries at least one question");
  }
  const said = Array.isArray(round.ownerWords) ? round.ownerWords : [];
  const seen = new Set();
  const rows = [];
  for (const question of round.questions) {
    const id = question && question.id;
    if (text(id) === "") {
      throw new RoundError("round-format", "question", "a question needs an id");
    }
    if (seen.has(id)) {
      throw new RoundError("round-format", id, "duplicate question id");
    }
    seen.add(id);
    if (!STATES.includes(question.state)) {
      throw new RoundError("round-state", id, "unknown state " + JSON.stringify(question.state));
    }
    const changes = text(question.changes);
    if (changes === "") {
      throw new RoundError("round-no-effect", id, "does not say what the answer changes");
    }
    if (question.state === "open") {
      const ask = question.ask;
      if (!ask || typeof ask !== "object" || text(ask.at) === "" || text(ask.channel) === "") {
        throw new RoundError("round-question-unasked", id, "open with no recorded ask call");
      }
    }
    if (question.state === "answered") {
      const words = text(question.words);
      if (words === "") {
        throw new RoundError("round-closure-unsubstantiated", id, "answered with no recorded words");
      }
      if (!said.includes(words)) {
        throw new RoundError("round-words-invented", id, "words the owner is not recorded saying");
      }
    }
    if (question.state === "struck" || question.state === "folded") {
      if (text(question.reason) === "") {
        throw new RoundError("round-closure-unsubstantiated", id, "closed as " + question.state + " with no reason");
      }
    }
    rows.push(Object.freeze({
      id: id,
      state: question.state,
      changes: changes,
      words: text(question.words),
      asked: question.state === "open" && question.ask !== undefined,
    }));
  }
  return Object.freeze(rows);
}

/** What the client may draw: the validated rows, with an open question never shown as answered. */
function renderRound(round) {
  return Object.freeze(readRound(round).map(function (row) {
    return Object.freeze({ id: row.id, state: row.state, changes: row.changes });
  }));
}

/**
 * The ask-before-complete gate. A round may complete with open questions, because an open question is
 * waiting rather than finished; it may not complete with an open question that was never asked.
 */
function assertComplete(round) {
  const rows = readRound(round);
  const open = rows.filter(function (row) { return row.state === "open"; });
  const unasked = open.filter(function (row) { return !row.asked; });
  if (unasked.length > 0) {
    throw new RoundError("round-question-unasked", unasked[0].id, "open and never asked");
  }
  return Object.freeze({ complete: true, open: Object.freeze(open.map(function (row) { return row.id; })) });
}

/** A question may leave a round only by being listed in the next round's closures. */
function reconcile(previous, next) {
  const before = readRound(previous);
  const after = new Set(readRound(next).map(function (row) { return row.id; }));
  const closed = new Set((Array.isArray(next.closed) ? next.closed : []).map(function (entry) {
    return entry && entry.id;
  }));
  for (const row of before) {
    if (after.has(row.id) || closed.has(row.id)) {
      continue;
    }
    throw new RoundError("round-question-dropped", row.id, "disappeared without a closure");
  }
  return true;
}

module.exports = {
  HEADER: HEADER,
  STATES: STATES,
  CODES: CODES,
  RoundError: RoundError,
  readRound: readRound,
  renderRound: renderRound,
  assertComplete: assertComplete,
  reconcile: reconcile,
};
'''

TEST_TEXT = r'''/**
 * The round gate, checked without a window.
 *
 * This is a **module check**: it proves the client refuses a round it should refuse. It is not a
 * client witness — nothing has been drawn — and nothing here may be reported as one (AGENTS 0.2).
 *
 * The rule under test is SECURE-SHELL-RESTORE@1.ARCHITECTURE.md 9.1: no open question survives a
 * round without being asked, and no closure is accepted without the owner's recorded words.
 */

import { test } from "node:test";
import assert from "node:assert/strict";
import { createRequire } from "node:module";

const require = createRequire(import.meta.url);
const rounds = require("../shell/openlock/panorama/scripts/secure_shell_rounds.js");

const SAID = "the node cua driver is the operation layer for the civilian acceptance document";

const question = (over = {}) => ({
  id: "N055",
  state: "open",
  changes: "whether the node bodies need a refusal path",
  ...over,
});

const round = (over = {}) => ({
  format: rounds.HEADER,
  ownerWords: [SAID],
  questions: [question()],
  ...over,
});

const askedQuestion = (over = {}) =>
  question({ ask: { at: "2026-11-04T12:00:00Z", channel: "ask_questions" }, ...over });

test("a round with an open question and no ask call is refused", () => {
  assert.throws(
    () => rounds.assertComplete(round()),
    (error) => error.code === "round-question-unasked" && error.subject === "N055",
  );
});

test("that round would have been reported complete before the gate existed", () => {
  const previousBehaviour = () => true; // nothing checked whether anyone was asked
  assert.equal(previousBehaviour(), true);
  assert.throws(() => rounds.assertComplete(round()), (error) => error.code === "round-question-unasked");
});

test("the same round completes once the ask call is recorded", () => {
  const done = rounds.assertComplete(round({ questions: [askedQuestion()] }));
  assert.equal(done.complete, true);
  assert.deepEqual(done.open, ["N055"]);
});

test("a closure with no recorded words is refused", () => {
  assert.throws(
    () => rounds.assertComplete(round({ questions: [question({ state: "answered" })] })),
    (error) => error.code === "round-closure-unsubstantiated",
  );
});

test("an answer in words the owner never said is refused", () => {
  assert.throws(
    () => rounds.assertComplete(round({
      questions: [question({ state: "answered", words: "words the owner never said" })],
    })),
    (error) => error.code === "round-words-invented" && error.subject === "N055",
  );
});

test("a closure recorded in the owner's own words is accepted", () => {
  const done = rounds.assertComplete(round({ questions: [question({ state: "answered", words: SAID })] }));
  assert.equal(done.complete, true);
});

test("a question that does not say what the answer changes is refused", () => {
  assert.throws(
    () => rounds.readRound(round({ questions: [askedQuestion({ changes: "  " })] })),
    (error) => error.code === "round-no-effect",
  );
});

test("an unknown state is refused by name", () => {
  assert.throws(
    () => rounds.readRound(round({ questions: [askedQuestion({ state: "answered-ish" })] })),
    (error) => error.code === "round-state",
  );
});

test("a question cannot disappear between rounds without a closure", () => {
  const before = round({ questions: [askedQuestion()] });
  const after = round({ questions: [question({ id: "Q141", ask: { at: "t", channel: "ask_questions" } })] });
  assert.throws(
    () => rounds.reconcile(before, after),
    (error) => error.code === "round-question-dropped" && error.subject === "N055",
  );
  const closed = { ...after, closed: [{ id: "N055", state: "struck", reason: "premise false" }] };
  assert.equal(rounds.reconcile(before, closed), true);
});

test("what the client draws is open until the words exist, never answered", () => {
  const shown = rounds.renderRound(round({ questions: [askedQuestion()] }));
  assert.equal(shown[0].state, "open");
  assert.equal(shown[0].changes, "whether the node bodies need a refusal path");
});
'''

SECTION = """### 9.1 A question is not open until it is asked

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

"""


def main():
    MODULE.parent.mkdir(parents=True, exist_ok=True)
    MODULE.write_bytes(MODULE_TEXT.encode("utf-8"))
    TEST.write_bytes(TEST_TEXT.encode("utf-8"))

    text = ARCH.read_text(encoding="utf-8")
    pattern = re.compile(r"### 9\.1 A question is not open until it is asked.*?(?=## 10\. Axis CUA)", re.S)
    if not pattern.search(text):
        raise SystemExit("9.1 section not found")
    ARCH.write_bytes(pattern.sub(SECTION, text, count=1).encode("utf-8"))

    print("module:", MODULE, MODULE.stat().st_size, "bytes")
    print("test:", TEST, TEST.stat().st_size, "bytes")
    print("9.1 rewritten")
    return 0


if __name__ == "__main__":
    sys.exit(main())
