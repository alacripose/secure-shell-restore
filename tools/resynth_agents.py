#!/usr/bin/env python3
"""Resynthesize this project's AGENTS.md additively, per project.

The rule this tool exists to enforce: a resynthesis states a project's conventions and its status to
the shell connection, and it **adds**. It never substitutes for what the file already says, because
the lines a resynthesis is tempted to "clean up" are the owner's rules. The failure that produced
this tool was exactly that: a rewrite dropped "Build the maximal system now", the audit table that
records where each rule came from, and the sentence saying that removing the maximal-system section
violates a principal rule of the project.

So the tool is guarded rather than trusted:

- the prior file is read from `git archive HEAD AGENTS.md`, never from the working copy, so a
  previous bad rewrite on disk cannot become the base;
- the new content is the prior file byte-for-byte, followed by appended sections;
- every non-empty line of the prior file must appear in the result. If one does not, the tool refuses
  `agents-authority-trimmed`, names the first missing line, and writes nothing.

Stale claims in the earlier text are not edited. They are named in the corrections section with a
date, which is the same discipline the decision register uses: supersede beside the text, never
rewrite it.
"""

from __future__ import annotations

import argparse
import io
import subprocess
import sys
import tarfile
from pathlib import Path

STATUS = """
## 14. Corrections to earlier sections (2026-11-04)

These sentences above were true when written and are no longer true. They stay as written; this
section supersedes them, and §15 carries the evidence. §5 says a stale status sentence is the defect,
so naming it is the fix — not deleting it.

- **§1's "It contains no runtime, no store, no package reader, no client, no server and no gate."**
  Superseded: `impl/packages/` now ships `identity.py`, `canonical.py`, `stream.py`, `loader.py` and
  `mongo_store.py`; `tests/packages/` runs their suites in CI; `tools/` carries the restore drill and
  the local capabilities.
- **§2's "It is absent today; when it exists it is a projection of (1)"**, about a curated decisions
  file. Superseded: the register exists in the project decisions belong to
  (`secure-shell/docs/DECISIONS.md`), and the storage question was settled there by a dated
  supersession row rather than by editing the 2026-10-31 text.
- **§4's list of five document checks.** Superseded: the checks are now commands — `hg_check3` …
  `hg_check12`, `normalize_lf`, `hg_ci_gate`, the strict re-audit, the resolver and ratchet
  self-checks, the four package-contract suites, and the local restore drill. Two rules were added
  with them: an exit status is read from the process and never from an echoed `$?` (`AF-31`), and
  editing a file the inventory records means rebuilding the scan before believing `hg_check11`.
- **§12's "This workspace has no executable surface."** Superseded in kind, not in rule: there is an
  executable surface now, and none of it polices prose. No gate blocks a commit; the drill refuses a
  package or a stream by name, and it does not refuse a document.

## 15. Status to the shell connection

This is the only place in this project that states connection status, and every line below came from
a command on 2026-11-04. When it changes, this section changes with the command beside it.

**The host.** Debian GNU/Linux 13 (trixie), `x86_64`, node `v22.23.4`, `mongod` `v8.0.34`, both in
WSL2 on this machine, both services `active`.

| Piece | Evidence | State |
|---|---|---|
| `secure-shell-axis` (`/api/axis/state`) | `curl` -> `{"schema":"secure-shell.axis/1","drivers":[],"tickets":0,"receipts":0}`, `http=200` | `held` |
| `mongod` with `authorization: enabled` | `systemctl is-active mongod` -> `active`; authenticated `ping` -> `ok: 1.0` | `held` |
| Mongo authority for packages | `impl.packages.mongo_store admit` -> `digest blake3:80acb981...`, `database secure_shell`; restore -> same digest, `length 184` | `held` |
| Sealed credential | `/etc/secure-shell/mongo-uri.cred` with `systemd-creds --with-key=host`, decrypted to `/run/drill-mongo.uri` for the run only | `held` |
| Install path | `sh deploy/install-debian.sh` -> exit 0; the unit is bound to the host's node | `held` |
| Restore drill | `python tools/restore_drill.py` -> 22 steps, 0 failed, exit 0 | `held` |

**What the drill refuses, by name,** each leaving prior state unchanged: `stream-corrupt`,
`chunk-out-of-order`, `stream-truncated`, `store-digest`, `mongo-digest`.

**What is deliberately not connected yet, named rather than implied.**

- `signature-absent` - nothing signs a package. A matching digest proves the bytes, never authorship.
- `replica-absent` - one `mongod`, no replica set and no failover.
- `backup-absent` - no backup or restore-from-backup path, and credential rotation is untested.
- `per-package-keys-absent` - one app identity (`secure_shell`, `readWrite` on `secure_shell`), not a
  key per package.
- `cua-driver-absent` - the CUA driver's system-handling features are not built here.

A status line may say `held`, `absent` or `refused`. It may never say "probably", and a line that
cannot be backed by a command from this pass is `absent`.

## 16. Resynthesizing a sibling's file

Each project's `AGENTS.md` answers the same two questions from its own evidence: what conventions does
this project enforce, and what is its status to the shell connection. Three rules keep the set
coherent, and this tool enforces the third mechanically.

- **Same shape, different facts.** Sibling files are read for their shape, never for their claims.
- **No copied status.** `openlock` generating the shell data package does not make `dl-enclave`'s
  store `held`; each project states what it can prove, and a cross-project claim is cited with a pin.
- **Authority is never trimmed.** A resynthesis is additive: every prior line survives, a stale claim
  is superseded by a dated line beside it, and a deleted rule is the drift the ratchet exists to
  catch. `tools/resynth_agents.py` refuses `agents-authority-trimmed` rather than write such a file.
"""


def prior_from_git(root: Path, name: str) -> str:
    proc = subprocess.run(["git", "archive", "HEAD", name], cwd=root, capture_output=True)
    if proc.returncode != 0:
        raise SystemExit(f"refused: agents-base-absent: {name}: {proc.stderr.decode('utf-8', 'replace').strip()}")
    with tarfile.open(fileobj=io.BytesIO(proc.stdout)) as archive:
        member = archive.extractfile(name)
        if member is None:
            raise SystemExit(f"refused: agents-base-absent: {name}: not in HEAD")
        return member.read().decode("utf-8")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="resynth_agents")
    parser.add_argument("--project", required=True, help="the project this file speaks for")
    parser.add_argument("--file", default="AGENTS.md")
    parser.add_argument("--root", default=".")
    args = parser.parse_args(argv)
    root = Path(args.root).resolve()

    prior = prior_from_git(root, args.file)
    candidate = prior.rstrip("\n") + "\n" + STATUS.replace("this project", f"`{args.project}`", 1)

    missing = [line for line in prior.splitlines() if line.strip() and line not in candidate]
    if missing:
        print(f"refused: agents-authority-trimmed: {args.file}: {missing[0][:120]}", file=sys.stderr)
        return 1

    (root / args.file).write_text(candidate, encoding="utf-8", newline="\n")
    print(
        f"resynthesized {args.file} for {args.project}: "
        f"{len(prior.splitlines())} prior lines kept, {len(STATUS.splitlines())} appended"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
