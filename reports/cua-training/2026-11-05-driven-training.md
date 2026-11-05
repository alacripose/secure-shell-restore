# CUA axis driver training: the Debian store, end to end (2026-11-05)

> **Superseded 2026-11-05** by `reports/cua-training/2026-11-05-training-uncapped.md`. This run was
> capped at 24 documents per project and 400 bundles, so it learned 368 documents from 24 projects.
> The replacement removes both limits and admits 3 264 documents from 62 projects. The lines below
> stay as written: the counts were true of this run, and the cap is exactly what the newer run
> removed.

Command (inside the Debian host, sealed credential decrypted for the run only):

```
systemd-creds decrypt --name=mongo-uri /etc/secure-shell/mongo-uri.cred /run/drill-mongo.uri
cd /mnt/c/Users/ala/Documents/secure_shell_v2
/opt/drill-venv/bin/python tools/cua_training.py --uri-file /run/drill-mongo.uri --documents
```

Exit status read from the process: `TRAIN_OK`; transcript `blake3:13a422fd2a0c7e391f7225933abd71dd904dca43ecf0ec1e57990ea8df7bb8f0` with 427 events, adopted by the shipped `Receiver` with exit 0.

| Check | Evidence | State |
|---|---|---|
| Driver registers and attests | `/api/axis/state` names `project-corpus-driver`, `trusted: true`, capabilities `witness, learning-apply, kernel` | PASS |
| Corpus is the folder audit | `docs/secure-shell-audit/resynth_audit@2026-11-04.json`, 55 rows, written by `tools/resynth_agents.py --report` | PASS |
| Project bundles reach the Mongo authority | one document per project, digest computed by `impl.packages.mongo_store.admit` | PASS |
| Project documents are learned from | 368 documents from 24 projects (`AGENTS.md`, `VOWS.md`, `CHECKPOINT.md`, `CONTEXT.md`, `docs/**`, `tickets/**`), each applied under its own ticket | PASS |
| The expectation contract is in the corpus | the CGA expectation contract is in the corpus as `secure-shell.training.docs/testport1-docs-cellular-generativity-axis-civilian@fd6644ef` | PASS |
| Corpus witnessed | `witness` receipt over `sha256` of the audit file | PASS |
| Kernel scope is declared, not assumed | `kernel` act accepted with `scope: kernel` under a driver that declares `kernel` | PASS |
| The transcript adopts | `python -m impl.packages.toolstream verify`: state `held`, exit 0 | PASS |
| Cellular substrate (CGA-38, CGA-45) | no cellframe/CA runtime exists in this workspace; the axis records decisions, not cellular state | NOT-ENFORCED |
| Six-star aggregation (CGA-44) | `secure-shell.axis/1` exposes drivers, tickets, receipts; it does not name six stars | NOT-ENFORCED |
| Client window, taskbar, delegation chat | no client surface built yet | NOT-ENFORCED |
| Physical outcome verification (CGA-14, CGA-28) | nothing here acts on a body; the game server remains the authority | NOT-ENFORCED |

A `NOT-ENFORCED` row is `absent`, never a pass. This report proves that a CUA driver learned
from every project and its expectation documents on this machine, through the Debian store,
under axis tickets; it does not prove a civilian lived, a cellframe evolved, or a window
rendered.
