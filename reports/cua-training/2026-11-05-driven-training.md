# CUA axis driver training: the Debian store, end to end (2026-11-05)

Command (inside the Debian host, sealed credential decrypted for the run only):

```
systemd-creds decrypt --name=mongo-uri /etc/secure-shell/mongo-uri.cred /run/drill-mongo.uri
cd /mnt/c/Users/ala/Documents/secure_shell_v2
/opt/drill-venv/bin/python tools/cua_training.py --uri-file /run/drill-mongo.uri --documents
```

Exit status read from the process: `TRAIN_OK`, stderr
`{"documents": 221, "receipts": 335, "trained": 55,
"transcript": "blake3:4a98333480aae708d9748b96cb1093e7e7c6738e24a83755d6acf937fa308e32",
"truncated_roots": 0}`.

| Check | Evidence | State |
|---|---|---|
| Driver registers and attests | `/api/axis/state` names `project-corpus-driver`, `trusted: true`, capabilities `witness, learning-apply, kernel` | PASS |
| Corpus is the folder audit | `docs/secure-shell-audit/resynth_audit@2026-11-04.json`, 55 rows, written by `tools/resynth_agents.py --report` | PASS |
| Project bundles reach the Mongo authority | one document per project, digest computed by `impl.packages.mongo_store.admit` | PASS |
| Project documents are learned from | 221 documents from 24 projects (`AGENTS.md`, `VOWS.md`, `CHECKPOINT.md`, `CONTEXT.md`, `docs/**`, `tickets/**`), each applied under its own ticket | PASS |
| The expectation contract is in the corpus | - the CGA expectation contract was not present in any project's documents | NOT-ENFORCED |
| Corpus witnessed | `witness` receipt over `sha256` of the audit file | PASS |
| Kernel scope is declared, not assumed | `kernel` act accepted with `scope: kernel` under a driver that declares `kernel` | PASS |
| The transcript adopts | `python -m impl.packages.toolstream verify`: 280 events, 108679 bytes, state `held`, exit 0 | PASS |
| Cellular substrate (CGA-38, CGA-45) | no cellframe/CA runtime exists in this workspace; the axis records decisions, not cellular state | NOT-ENFORCED |
| Six-star aggregation (CGA-44) | `secure-shell.axis/1` exposes drivers, tickets, receipts; it does not name six stars | NOT-ENFORCED |
| Client window, taskbar, delegation chat | no client surface built yet | NOT-ENFORCED |
| Physical outcome verification (CGA-14, CGA-28) | nothing here acts on a body; the game server remains the authority | NOT-ENFORCED |

A `NOT-ENFORCED` row is `absent`, never a pass. This report proves that a CUA driver learned
from every project and its own expectation documents on this machine, through the Debian
store, under axis tickets; it does not prove a civilian lived, a cellframe evolved, or a
window rendered.
