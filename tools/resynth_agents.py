#!/usr/bin/env python3
"""Resynthesize AGENTS.md for every project found, additively and per project.

The rule this tool exists to enforce: a resynthesis states a project's conventions and its status to
the shell connection, and it **adds**. It never substitutes for what the file already says, because
the lines a resynthesis is tempted to "clean up" are the owner's rules. The failure that produced
this tool was exactly that: a rewrite dropped "Build the maximal system now", the audit table that
records where each rule came from, and the sentence saying that removing the maximal-system section
violates a principal rule of the project.

So it is guarded rather than trusted:

- the prior file is read from `git archive HEAD AGENTS.md` when the project is a git repository, so a
  previous bad rewrite on disk cannot become the base; a project without git is read as it stands;
- the new content is the prior file byte-for-byte, followed by appended sections;
- every non-empty line of the prior file must appear in the result. If one does not, the tool refuses
  `agents-authority-trimmed`, names the first missing line, and writes nothing.

Scope is every project, not a chosen list. `--report` walks the roots and prints one row per project:
its head, its layers (api/server, skills, scratch, tools, examples, fixtures, schema, packages),
and the format revisions it carries. `--apply` writes the appended sections into each project found.
No project is silently skipped; one that cannot be written is named with the reason.

Formats are read the way the audit tools read them (`tools/scan_drives_reaudit.py`): dotted schema
identifiers such as `secure-shell.stream/1` and package magics such as `SHPKG002`. A family at more
than one revision is reported as upgraded-versus-legacy rather than averaged, because a legacy value
is evidence to be read, never silently converted (`dl-enclave` §1, §3).
"""

from __future__ import annotations

import os as _os
import sys as _sys

_sys.path.insert(0, _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))))


import argparse
import io
import re
import subprocess
import sys
import tarfile
import time
from collections import Counter
from pathlib import Path

from impl.packages.toolstream import ToolStream

STREAM = ToolStream("resynth-agents")

SCHEMA_RE = re.compile(r"\b([a-z][a-z0-9-]*(?:\.[a-z0-9-]+)+/[0-9]{1,2})\b")
MAGIC_RE = re.compile(r'b?"([A-Z0-9]{1,12}PKG[0-9]{3})"')
SKIP = {".git", "node_modules", "dist", "obj", "bin", "__pycache__", "var", ".cache", ".venv", "venv"}
LAYERS = {
    "api": ("api", "server", "mcp", "serverless", "routes"),
    "skills": ("skills", ".skills"),
    "scratch": ("scratch", ".scratch", "experiments"),
    "tools": ("tools", "scripts"),
    "examples": ("examples", "samples", "demos"),
    "fixtures": ("fixtures", "testdata"),
    "schema": ("schema", "schemas", "formats"),
    "packages": ("packages", "clientaddon", "addons"),
    "docs": ("docs",),
}
CONNECTED = {
    "secure_shell_v2": ("held", "`python tools/restore_drill.py` -> 22 steps, 0 failed, exit 0"),
    "secure-shell": ("held", "unit `secure-shell-axis` active; `/api/axis/state` -> http=200"),
    "openlock": ("held", "`tools/gen_shell_data.py` produced the admitted shell-data package"),
    "dl-enclave": ("held", "`tools/port/src/addon-store.mjs` install/verify -> `dashboard`, refuses `store-digest`"),
}


def git(root: Path, *args: str) -> subprocess.CompletedProcess:
    return subprocess.run(["git", "-C", str(root), *args], capture_output=True)


def prior(root: Path) -> tuple[str, str]:
    """The file as HEAD has it, so a bad working copy cannot become the base."""
    name = "AGENTS.md"
    if (root / ".git").exists() or (root / ".git").is_file():
        archive = git(root, "archive", "HEAD", name)
        if archive.returncode == 0:
            with tarfile.open(fileobj=io.BytesIO(archive.stdout)) as tar:
                member = tar.extractfile(name)
                if member is not None:
                    return member.read().decode("utf-8"), "HEAD"
    path = root / name
    if path.is_file():
        return path.read_text(encoding="utf-8"), "worktree"
    return "", "absent"


def formats(root: Path, budget_files: int = 2500) -> tuple[Counter, Counter]:
    identifiers: Counter = Counter()
    magics: Counter = Counter()
    seen = 0
    for path in root.rglob("*"):
        if seen >= budget_files:
            break
        if not path.is_file() or path.suffix.lower() not in {".md", ".py", ".mjs", ".js", ".rs", ".json", ".xml", ".shspec", ".surface", ".ts", ".toml", ".yaml", ".yml"}:
            continue
        if any(part in SKIP for part in path.relative_to(root).parts):
            continue
        seen += 1
        try:
            text = path.read_text(encoding="utf-8", errors="replace")[:200_000]
        except OSError:
            continue
        for value in SCHEMA_RE.findall(text):
            identifiers[value] += 1
        for value in MAGIC_RE.findall(text):
            magics[value] += 1
    return identifiers, magics


def revisions(values: Counter) -> tuple[dict[str, int], dict[str, list[str]]]:
    newest: dict[str, int] = {}
    grouped: dict[str, list[str]] = {}
    for value in values:
        head, _, number = value.rpartition("/")
        if not head:
            continue
        grouped.setdefault(head, []).append(value)
        newest[head] = max(newest.get(head, 0), int(number))
    legacy = {head: sorted(v for v in values if v.rpartition("/")[0] == head and int(v.rpartition("/")[2]) < newest[head]) for head in grouped}
    return newest, legacy


def layers(root: Path) -> dict[str, list[str]]:
    found: dict[str, list[str]] = {}
    present = {entry.name for entry in root.iterdir() if entry.is_dir()}
    for layer, names in LAYERS.items():
        hit = sorted(present & set(names))
        if hit:
            found[layer] = hit
    return found


def section(*, name: str, root: Path, head: str, layers_found: dict[str, list[str]], ids: Counter, magics: Counter, start: int) -> str:
    newest, legacy = revisions(ids)
    state, evidence = CONNECTED.get(name, ("absent", "no admitted package, running unit or drill step names this project"))
    layer_text = ", ".join(f"`{v[0]}`" for v in layers_found.values()) or "none at the top level"
    id_text = ", ".join(f"`{k}`x{v}" for k, v in ids.most_common(12)) or "none read"
    magic_text = ", ".join(f"`{k}`x{v}" for k, v in magics.most_common(8)) or "none read"
    legacy_lines = []
    for family, values in sorted(legacy.items()):
        if values:
            legacy_lines.append(f"  - `{family}`: newest `{family}/{newest[family]}`, older {', '.join('`' + v + '`' for v in values)}")
    legacy_block = "\n".join(legacy_lines) if legacy_lines else "  - no family was read at more than one revision"
    return f"""
## {start}. Formats: upgraded and legacy

This project carries formats at their own revisions, and the audit tools inventory them rather than
trusting a summary: `scan_drives_reaudit.py` in `secure_shell_v2` reads dotted schema identifiers and
package magics across every project, and its register is checked rather than described.

Read here on {time.strftime("%Y-%m-%d")} under `{root}` (head `{head}`):

- identifiers: {id_text}
- magics: {magic_text}

Upgraded versus legacy, by family:

{legacy_block}

A legacy value is evidence to read, never a value to convert silently: an older frame is refused by
name, and `dl-enclave` §1 and §3 own that rule for this family.

## {start + 1}. Status to the shell connection

This project's connection state, from commands on 2026-11-04, not from its own README:

| Question | Answer |
|---|---|
| Does a running unit, admitted package or drill step name this project? | `{state}` |
| Evidence | {evidence} |
| Layers this project keeps | {layer_text} |

`held` here means the named command produced the named result. `absent` means nothing proved it yet;
it is not a judgement about the project's quality, and it changes only when a command changes it.

## {start + 2}. Resynthesizing this file

This section was appended by `secure_shell_v2/tools/resynth_agents.py`, which refuses
`agents-authority-trimmed` rather than write a file that lost a prior line. A resynthesis of this
project adds: its formats at their revisions, its connection state, and its conventions as the file
already states them. It does not delete, re-word or "tidy" an existing rule; a stale claim is
superseded by a dated line beside it.
"""


ARTIFACT_PATHS = {
    "inputs": ("inputs",),
    "port-gate": ("tools/port_gate.py", "port_gate.py"),
    "health": ("artifacts/health",),
    "framing": ("impl/packages/canonical.py", "tools/frame.py"),
}


def audit(root: Path) -> dict[str, str]:
    """What the project actually contains, checked on disk rather than assumed from its prose."""
    facts: dict[str, str] = {}
    for name, candidates in ARTIFACT_PATHS.items():
        found = next((root / candidate for candidate in candidates if (root / candidate).exists()), None)
        facts[name] = "present" if found is not None else "absent"
    agents = root / "AGENTS.md"
    claims = agents.read_text(encoding="utf-8", errors="replace") if agents.is_file() else ""
    dropped = re.findall(r"^\| ([^|]+) \| [^|]+ \| \*\*Dropped", claims, re.M)
    facts["dropped-claims"] = str(len(dropped))
    facts["dropped-names"] = ",".join(claim.strip() for claim in dropped) or "-"
    return facts


def discover(roots: list[Path], depth: int = 3, budget: float = 60.0) -> tuple[list[Path], list[str]]:
    """Walk every folder under each root, bounded per root, and name a root that ran out of budget.

    A project is a folder carrying `.git` or `AGENTS.md`; the walk continues past it so a project
    nested inside another is found too. A root that reaches its budget is reported as truncated,
    never as a walk that found nothing.
    """
    found: list[Path] = []
    truncated: list[str] = []
    for root in roots:
        deadline = time.time() + budget
        stack: list[tuple[Path, int]] = [(root, 0)]
        while stack:
            if time.time() > deadline:
                truncated.append(str(root))
                break
            current, level = stack.pop()
            try:
                if (current / ".git").exists() or (current / "AGENTS.md").is_file():
                    found.append(current)
                if level >= depth:
                    continue
                for child in sorted(current.iterdir()):
                    if child.is_dir() and child.name not in SKIP and not child.name.startswith("."):
                        stack.append((child, level + 1))
            except (PermissionError, OSError):
                continue
    return found, truncated

def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="resynth_agents")
    parser.add_argument("--roots", nargs="+", default=["."])
    parser.add_argument("--report", action="store_true")
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--depth", type=int, default=3)
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--budget", type=float, default=60.0)
    args = parser.parse_args(argv)

    projects, truncated = discover([Path(r) for r in args.roots], args.depth, args.budget)
    print(f"projects found: {len(projects)} truncated_roots={len(truncated)}", file=sys.stderr)
    for root in truncated:
        print(f"refused audit-stream-truncated {root}: budget of {args.budget}s reached", file=sys.stderr)

    written = skipped = refused = 0
    for root in projects:
        name = root.name
        base, source = prior(root)
        head = git(root, "rev-parse", "--short", "HEAD").stdout.decode().strip() or "-"
        ids, magics = formats(root)
        next_number = 1 + max([int(m) for m in re.findall(r"^## (\d+)\.", base, re.M)] or [0])
        text = base.rstrip("\n") + "\n" + section(
            name=name, root=root, head=head, layers_found=layers(root), ids=ids, magics=magics, start=next_number
        )
        missing = [line for line in base.splitlines() if line.strip() and line not in text]
        if missing:
            print(f"refused agents-authority-trimmed {name}: {missing[0][:90]}", file=sys.stderr)
            refused += 1
            continue
        if not args.apply:
            state = CONNECTED.get(name, ("absent", ""))[0]
            facts = audit(root)
            STREAM.emit({"event": "project", "name": name, "head": head, "formats": len(ids), "magics": len(magics), "state": state, **facts})
            print(f"{name:28} head={head:9} base={source:9} ids={len(ids):4} magics={len(magics):3} layers={','.join(layers(root)) or '-':45} state={state}", file=sys.stderr)
            continue
        if "Status to the shell connection" in base and not args.force:
            skipped += 1
            continue
        (root / "AGENTS.md").write_text(text, encoding="utf-8", newline="\n")
        written += 1
        print(f"resynthesized {name}: {len(base.splitlines())} prior lines kept, appended from §{next_number}", file=sys.stderr)

    print(f"written={written} skipped={skipped} refused={refused}", file=sys.stderr)
    return 1 if refused else 0


if __name__ == "__main__":
    sys.exit(main())
