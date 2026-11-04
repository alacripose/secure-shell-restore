#!/usr/bin/env python3
"""Hypergrilling resolver (format v2).

The worksheet is a target graph, not a script. This tool gives a CUA driver the
mechanics it needs to close questions with evidence instead of putting them to
the owner:

  seed      parse the worksheet into state
  status    counts by class and status
  tick      the next batch, cheapest first, with the next search named
  resolve   admit a five-field resolution, or refuse it
  lookup    search a checked-out repository and return citable matches
  fold      close a question as a duplicate, citing the question it duplicates
  strike    close a question whose premise is gone, citing the reason
  self-check  assert the contract holds, without touching real state

Refusal codes:
  resolution-unsupported   evidence is missing or empty
  owner-authority          the class is `owner`; only the owner closes it
  supersession-unnamed     it contradicts a recorded ruling and names nothing
  already-closed           the question is no longer open
  unknown-question         the id is not in the worksheet
  bad-receipt              the receipt is missing a required field

Stdlib only. No network: a driver that searches supplies the citations.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WORKSHEET = ROOT / "docs" / "SECURE-SHELL-RESTORE@1.HYPERGRILL.md"
STATE = ROOT / "docs" / "hypergrill" / "state.json"
RECEIPTS = ROOT / "docs" / "hypergrill" / "receipts.jsonl"
ROOTS = ROOT / "docs" / "hypergrill" / "roots.json"

CLASSES = ("code", "spec", "external", "measure", "owner")
# Cheapest first: a repository read beats a derivation, which beats a web fetch,
# which beats a measurement. `owner` is never scheduled by the driver.
COST = {"code": 0, "spec": 1, "external": 2, "measure": 3, "owner": 4}
FIELDS = ("question", "class", "evidence", "resolution", "effect")
EVIDENCE_KINDS = ("code", "doc", "web", "measure", "owner")


def now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def section(text: str, start: str, end: str | None) -> str:
    body = text.split(start, 1)[1]
    return body.split(end, 1)[0] if end else body


def parse_worksheet(path: Path) -> dict:
    """Return {id: {text, class, status, ruling}} from Appendix A and C."""
    text = path.read_text(encoding="utf-8")
    questions: dict[str, dict] = {}

    rulings = section(text, "## Appendix A", "## Appendix B")
    for line in rulings.splitlines():
        m = re.match(r"^\| ((?:Q|N)\d{3}) \| (.+?) \|\s*$", line)
        if m:
            questions[m.group(1)] = {
                "id": m.group(1),
                "text": "",
                "class": "owner",
                "status": "resolved",
                "ruling": m.group(2).strip(),
                "evidence": [{"kind": "owner", "ref": "worksheet Appendix A",
                              "note": "ruling recorded under the retired format"}],
            }

    carried = section(text, "## Appendix C", None)
    for line in carried.splitlines():
        m = re.match(r"^\| ((?:Q|N)\d{3}) \| (.+?) \| (.+?) \|\s*$", line)
        if not m:
            continue
        qid, qtext, cell = m.group(1), m.group(2).strip(), m.group(3)
        # Class cells are written "`spec`", "`code`, `spec`" and "`owner` (acceptance)".
        # The first recognised class wins, which is also the cheapest one to close.
        klass = next((t for t in re.findall(r"`(\w+)`", cell) if t in CLASSES), "spec")
        questions[qid] = {
            "id": qid,
            "text": qtext,
            "class": klass,
            "status": "open",
            "ruling": "",
            "evidence": [],
        }
    return questions


def load_state(worksheet: Path = WORKSHEET, state: Path = STATE) -> dict:
    if not state.exists():
        return {"worksheet": str(worksheet), "seeded_at": None,
                "questions": parse_worksheet(worksheet)}
    return json.loads(state.read_text(encoding="utf-8"))


def save_state(data: dict, state: Path = STATE) -> None:
    state.parent.mkdir(parents=True, exist_ok=True)
    state.write_bytes((json.dumps(data, indent=2, sort_keys=True) + "\n").encode("utf-8"))


def append_receipt(receipt: dict, receipts: Path = RECEIPTS) -> None:
    receipts.parent.mkdir(parents=True, exist_ok=True)
    with receipts.open("a", encoding="utf-8", newline="\n") as fh:
        fh.write(json.dumps(receipt, sort_keys=True) + "\n")


def refuse(code: str, detail: str) -> int:
    """A refusal is a result, not a crash: it says which boundary was hit."""
    print(json.dumps({"refused": code, "detail": detail}))
    return 3


def admit(data: dict, receipt: dict, owner_authorized: bool = False) -> tuple[bool, str]:
    """Validate a five-field resolution against the contract in section 7.

    `owner` is closed only by the owner. A receipt may carry that class only when the
    caller passes `owner_authorized`, and even then the words it quotes must already be
    recorded in the worksheet, so the driver cannot manufacture the answer it cites.
    """
    missing = [f for f in FIELDS if receipt.get(f) in (None, "")]
    if missing:
        return False, f"missing fields: {', '.join(missing)}"
    if receipt["class"] not in CLASSES:
        return False, f"unknown class {receipt['class']!r}"
    if receipt["class"] == "owner" and not owner_authorized:
        return False, "class `owner` is closed only by the owner"
    evidence = receipt["evidence"]
    if not isinstance(evidence, list) or not evidence:
        return False, "no evidence"
    for item in evidence:
        if not isinstance(item, dict) or not item.get("ref"):
            return False, "evidence item without a ref"
        if item.get("kind") not in EVIDENCE_KINDS:
            return False, f"evidence kind {item.get('kind')!r} is not one of {EVIDENCE_KINDS}"

    qid = receipt["question"]
    record = data["questions"].get(qid)
    if record is None:
        return False, f"{qid} is not in the worksheet"
    if record["status"] != "open":
        return False, f"{qid} is already {record['status']}"
    if record["class"] == "owner":
        if not owner_authorized:
            return False, f"{qid} is class `owner` in the worksheet"
        verbatim = (receipt.get("verbatim") or "").strip()
        if not verbatim:
            return False, f"{qid} is an owner question and the receipt quotes nothing"
        if not any(item.get("kind") == "owner" for item in evidence):
            return False, f"{qid} needs an `owner` evidence item"
        recorded = Path(data.get("worksheet", WORKSHEET)).read_text(encoding="utf-8")
        if verbatim not in recorded:
            return False, f"{qid} quotes words the worksheet does not record"
    elif owner_authorized:
        return False, f"{qid} is not an owner question"
    if receipt.get("supersedes"):
        target = data["questions"].get(receipt["supersedes"])
        if target is None:
            return False, f"supersedes {receipt['supersedes']}, which does not exist"
    return True, ""


def cmd_seed(args) -> int:
    data = {"worksheet": str(args.worksheet), "seeded_at": now(),
            "questions": parse_worksheet(args.worksheet)}
    save_state(data, args.state)
    open_count = sum(1 for q in data["questions"].values() if q["status"] == "open")
    print(json.dumps({"seeded": len(data["questions"]), "open": open_count}))
    return 0


def cmd_status(args) -> int:
    data = load_state(args.worksheet, args.state)
    by_status: dict[str, int] = {}
    by_class: dict[str, int] = {}
    for q in data["questions"].values():
        by_status[q["status"]] = by_status.get(q["status"], 0) + 1
        if q["status"] == "open":
            by_class[q["class"]] = by_class.get(q["class"], 0) + 1
    print(json.dumps({"status": by_status, "open_by_class": by_class}, sort_keys=True))
    return 0


def cmd_tick(args) -> int:
    data = load_state(args.worksheet, args.state)
    opened = [q for q in data["questions"].values()
              if q["status"] == "open" and q["class"] != "owner"]
    opened.sort(key=lambda q: (COST.get(q["class"], 9), q["id"]))
    batch = opened[: args.batch]
    print(json.dumps({
        "tick": now(),
        "budget_seconds": args.budget_seconds or "unbounded",
        "open_total": sum(1 for q in data["questions"].values() if q["status"] == "open"),
        "schedulable": len(opened),
        "batch": [{"id": q["id"], "class": q["class"], "text": q["text"]} for q in batch],
        "escalated_to_owner": sorted(q["id"] for q in data["questions"].values()
                                     if q["status"] == "open" and q["class"] == "owner"),
        "next_cheapest_search": batch[0]["text"] if batch else None,
    }, indent=2))
    return 0


SKIP_DIRS = {".git", "node_modules", "target", "dist", "build", ".venv", "__pycache__"}
SKIP_SUFFIX = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".zip", ".gz", ".7z",
               ".bin", ".pak", ".sqlite", ".db", ".pdf", ".ico", ".woff", ".woff2"}


def search_root(root: Path, term: str, limit: int) -> list[dict]:
    """Grep one checkout. Each hit is citable as `root-name:path:line`."""
    hits: list[dict] = []
    for path in root.rglob("*"):
        if len(hits) >= limit:
            break
        if not path.is_file() or path.suffix.lower() in SKIP_SUFFIX:
            continue
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        try:
            if path.stat().st_size > 2_000_000:
                continue
            blob = path.read_bytes()
        except OSError:
            continue
        if b"\x00" in blob[:4096]:
            continue
        try:
            text = blob.decode("utf-8")
        except UnicodeDecodeError:
            continue
        for n, line in enumerate(text.splitlines(), 1):
            if term in line.lower():
                hits.append({"kind": "code",
                             "ref": f"{root.name}:{path.relative_to(root).as_posix()}:{n}",
                             "note": line.strip()[:200]})
                if len(hits) >= limit:
                    break
    return hits


def configured_roots() -> list[Path]:
    if not ROOTS.exists():
        return []
    data = json.loads(ROOTS.read_text(encoding="utf-8"))
    return [Path(r["path"]) for r in data.get("roots", [])]


def cmd_lookup(args) -> int:
    """Grep one checkout, or every family checkout recorded on this machine."""
    if args.all or not args.repo:
        roots = configured_roots()
        if not roots:
            return refuse("no-checkout", "no roots configured; run `roots --discover <dir> --write`")
    else:
        roots = [Path(args.repo)]
    missing = [str(r) for r in roots if not r.is_dir()]
    if missing:
        return refuse("no-checkout", f"not a directory: {missing}")
    term = args.term.lower()
    hits: list[dict] = []
    for root in roots:
        hits.extend(search_root(root, term, args.limit - len(hits)))
        if len(hits) >= args.limit:
            break
    print(json.dumps({"term": args.term, "roots": [str(r) for r in roots],
                      "count": len(hits), "matches": hits}, indent=2))
    return 0 if hits else 4


def cmd_roots(args) -> int:
    """Discover the family checkouts that live on this machine."""
    parent = Path(args.discover) if args.discover else None
    found: list[dict] = []
    if parent and parent.is_dir():
        for entry in sorted(parent.iterdir()):
            if not entry.is_dir() or entry.name.startswith("."):
                continue
            if entry.resolve() == ROOT or not (entry / ".git").exists():
                continue
            markers = [m for m in ("AGENTS.md", "docs/DECISIONS.md", "docs/ARCHITECTURE.md")
                       if (entry / m).exists()]
            found.append({"name": entry.name, "path": entry.as_posix(), "markers": markers})
    data = {"discovered_at": now(),
            "parent": parent.as_posix() if parent else None,
            "roots": found}
    if args.write:
        ROOTS.parent.mkdir(parents=True, exist_ok=True)
        ROOTS.write_bytes((json.dumps(data, indent=2) + "\n").encode("utf-8"))
    print(json.dumps(data, indent=2))
    return 0 if found else 4


def _close(args, status: str, receipt: dict) -> int:
    data = load_state(args.worksheet, args.state)
    record = data["questions"].get(receipt["question"])
    if record is None:
        return refuse("unknown-question", f"{receipt['question']} is not in the worksheet")
    if record["status"] != "open":
        return refuse("already-closed", f"{receipt['question']} is {record['status']}")
    ok, why = True, ""
    if status == "resolved":
        ok, why = admit(data, receipt, owner_authorized=getattr(args, "owner", False))
        if not ok:
            if "owner" in why:
                return refuse("owner-authority", why)
            if "already" in why:
                return refuse("already-closed", why)
            if "supersede" in why:
                return refuse("supersession-unnamed", why)
            if "evidence" in why:
                return refuse("resolution-unsupported", why)
            return refuse("bad-receipt", why)
    record["status"] = status
    record["evidence"] = receipt.get("evidence", [])
    record["resolution"] = receipt.get("resolution") or receipt.get("reason", "")
    record["receipt_at"] = now()
    save_state(data, args.state)
    append_receipt({**receipt, "status": status, "at": now(),
                    "driver": "secure-shell-driver"}, args.receipts)
    print(json.dumps({"closed": receipt["question"], "status": status}))
    return 0


def cmd_resolve(args) -> int:
    receipt = json.loads(args.receipt.read_text(encoding="utf-8"))
    if getattr(args, "owner", False) and receipt.get("class") != "owner":
        return refuse("owner-mismatch", "--owner on a receipt whose class is not `owner`")
    return _close(args, "resolved", receipt)


def cmd_fold(args) -> int:
    return _close(args, "folded", {"question": args.id,
                                   "evidence": [{"kind": "doc", "ref": args.ref,
                                                 "note": args.reason}],
                                   "reason": f"duplicate of {args.ref}"})


def cmd_strike(args) -> int:
    return _close(args, "struck", {"question": args.id,
                                   "evidence": [{"kind": "doc", "ref": args.ref,
                                                 "note": args.reason}],
                                   "reason": args.reason})


def cmd_self_check(args) -> int:
    """Assert the contract on a throwaway copy. Never touches real state."""
    ok = True

    def check(label: str, cond: bool) -> None:
        nonlocal ok
        print(f"{'ok  ' if cond else 'FAIL'} {label}")
        ok = ok and cond

    questions = parse_worksheet(WORKSHEET)
    check("worksheet parses", len(questions) > 100)
    check("119 rulings recorded", sum(1 for q in questions.values() if q["status"] == "resolved") == 119)
    check("60 seeded open (20 carried + 20 stream + 20 receipts)",
          sum(1 for q in questions.values() if q["status"] == "open") == 60)
    check("every open question has a class",
          all(q["class"] in CLASSES for q in questions.values() if q["status"] == "open"))

    with tempfile.TemporaryDirectory() as tmp:
        state = Path(tmp) / "state.json"
        receipts = Path(tmp) / "receipts.jsonl"
        data = {"worksheet": str(WORKSHEET), "seeded_at": now(), "questions": questions}
        save_state(data, state)

        class A:  # tiny argparse stand-in
            pass
        a = A()
        a.state, a.receipts, a.worksheet = state, receipts, WORKSHEET

        good = {"question": "Q077", "class": "spec",
                "evidence": [{"kind": "doc", "ref": "docs/x.md#12.8", "note": "derived"}],
                "resolution": "bytes plus path", "effect": "12.8"}
        okk, why = admit(load_state(WORKSHEET, state), good)
        check("complete receipt admits", okk)

        bad = {**good, "evidence": []}
        okk, why = admit(load_state(WORKSHEET, state), bad)
        check("empty evidence is refused", not okk and "no evidence" in why)

        owner = {**good, "question": "N052", "class": "owner",
                 "evidence": [{"kind": "owner", "ref": "worksheet#8.2", "note": "quoted"}]}
        okk, why = admit(load_state(WORKSHEET, state), owner)
        check("owner class is refused", not okk and "owner" in why)

        okk, why = admit(load_state(WORKSHEET, state), owner, owner_authorized=True)
        check("owner closure without the words is refused",
              not okk and "quotes nothing" in why)

        quoted = {**owner, "verbatim": "One successful mount plus a render witness"}
        okk, why = admit(load_state(WORKSHEET, state), quoted, owner_authorized=True)
        check("owner closure with the recorded words admits", okk)

        invented = {**owner, "verbatim": "words the owner never said"}
        okk, why = admit(load_state(WORKSHEET, state), invented, owner_authorized=True)
        check("owner closure with invented words is refused",
              not okk and "does not record" in why)

        missing = {k: v for k, v in good.items() if k != "effect"}
        okk, why = admit(load_state(WORKSHEET, state), missing)
        check("missing field is refused", not okk and "missing fields" in why)

        closed = {**good, "question": "Q001"}
        okk, why = admit(load_state(WORKSHEET, state), closed)
        check("already-closed is refused", not okk and "already" in why)

    print("RESULT:", "PASS" if ok else "FAIL")
    return 0 if ok else 1


def main(argv: list[str]) -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--worksheet", type=Path, default=WORKSHEET)
    p.add_argument("--state", type=Path, default=STATE)
    p.add_argument("--receipts", type=Path, default=RECEIPTS)
    sub = p.add_subparsers(dest="cmd", required=True)

    sub.add_parser("seed").set_defaults(func=cmd_seed)
    sub.add_parser("status").set_defaults(func=cmd_status)
    sub.add_parser("self-check").set_defaults(func=cmd_self_check)

    t = sub.add_parser("tick")
    t.add_argument("--batch", type=int, default=5)
    t.add_argument("--budget-seconds", type=int, default=0, help="0 means unbounded")
    t.set_defaults(func=cmd_tick)

    r = sub.add_parser("resolve")
    r.add_argument("receipt", type=Path, help="JSON with question, class, evidence, resolution, effect")
    r.add_argument("--owner", action="store_true",
                   help="the receipt carries the owner's recorded words; requires `verbatim`")
    r.set_defaults(func=cmd_resolve)

    lk = sub.add_parser("lookup")
    lk.add_argument("term")
    lk.add_argument("--repo", help="one checkout")
    lk.add_argument("--all", action="store_true", help="every root in docs/hypergrill/roots.json")
    lk.add_argument("--limit", type=int, default=25)
    lk.set_defaults(func=cmd_lookup)

    rt = sub.add_parser("roots")
    rt.add_argument("--discover", help="parent directory holding the family checkouts")
    rt.add_argument("--write", action="store_true", help="save the result as the root list")
    rt.set_defaults(func=cmd_roots)

    f = sub.add_parser("fold")
    f.add_argument("id")
    f.add_argument("--ref", required=True, help="the question or ruling it duplicates")
    f.add_argument("--reason", default="duplicate")
    f.set_defaults(func=cmd_fold)

    s = sub.add_parser("strike")
    s.add_argument("id")
    s.add_argument("--ref", required=True)
    s.add_argument("--reason", required=True)
    s.set_defaults(func=cmd_strike)

    args = p.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
