# TICKET-0011 — R3: a Debian host built by the install script, and a cold restore drill

**Status:** `complete` for the pass; the milestone's Mongo authority is **not** closed.
**Owner authority:** the owner's turn of 2026-11-04, source `user`: "get the secure shell restore
actually running end to end on a Debian host, not described".

## 1. The goal, quoted

> **R3 — Debian restore** | Rebuild the MongoDB store on Debian from declared inputs; `systemd-creds`
> credentials; per-package keys; backups and a restore drill | A clean host reproduces the store
> digest; restore drill artifact exists

(`docs/SECURE-SHELL-RESTORE@1.IMPLEMENTATION-PLAN.md` §3, R3.)

## 2. The one artifact

`tools/restore_drill.py`: a 14-step run against the WSL `Debian` distro that installs the axis with
`secure-shell/deploy/install-debian.sh`, proves the route serves, generates a fresh OpenLock package,
admits it through `impl/packages/loader.py` and the `dl-enclave` store, restores it into an empty
directory, and refuses three tampered streams and one tampered package by name.

## 3. The last check's three-way answer

The Debian host was `absent` — no host had ever been built by the install script, and the first
attempt failed twice (`AF-27`, `AF-28`). It is now `held`: the drill exits 0 with 14/14 steps on
`Debian GNU/Linux 13 (trixie)`, `x86_64`, `node v22.23.4`, and the Mongo authority R3 names is
still `absent` (`AF-29` records the register repair; no `mongod` runs on this host).

## 4. The drift signal

The first drill run reported 11/12 and the "passing" 12th was an echoed exit status (`AF-31`). A
drill that reports its own echo as evidence is the drift this workspace exists to catch.

## 5. Evidence

Host: `Debian GNU/Linux 13 (trixie)`, kernel from WSL2, run as root, 2026-11-04.

```
ok   host identity                     exit=0  PRETTY_NAME="Debian GNU/Linux 13 (trixie)" node v22.23.4
ok   deploy/install-debian.sh          exit=0  installed: secure-shell-axis.service
ok   axis unit active                  exit=0  active
ok   axis serves /api/axis/state       exit=0  {"schema":"secure-shell.axis/1","drivers":[],"tickets":0,"receipts":0} http=200
ok   generation twice, identical bytes exits=0,0 bytes=482260 sha256=7f5d587a7f32fddb identical=True
ok   loader identity                  exit=0  secure-shell-openlock-shell-data@1+blake3:59ac1e8a…
ok   store install                    exit=0  installed dashboard 1.0.0 client-dashboard
ok   store verify                     exit=0  dashboard 1.0.0 … sha256:8c820617…
ok   cold restore adopts the package  exit=0  {"adoptions":1,"state":"held","digest":"blake3:59ac1e8a…"}
ok   cold digest equals the loader identity
ok   refuses a digest-corrupt stream  exit=1  refusal=stream-corrupt prior_unchanged=True
ok   refuses a reordered stream       exit=1  refusal=chunk-out-of-order prior_unchanged=True
ok   refuses a truncated stream       exit=1  chunks=7 refusal=stream-truncated prior_unchanged=True
ok   store refuses a tampered package exit=1  store-digest … index_unchanged=True
```

Reproduce: `python tools/restore_drill.py` on a machine with the `Debian` WSL distro and the
`openlock`, `secure-shell` and `dl-enclave` checkouts. CI cannot run it; the workflow does not claim to.

## 6. Refusals for the next unit

- `mongo-absent`: no MongoDB reconstruction, `systemd-creds` credential or per-package key exists in
  this pass. The drill restores a package and a stream; it does not rebuild the Mongo authority.
- `signature-absent`: nothing in this pass signs anything. A BLAKE3 digest proves bytes, not authorship.
- `store-not-authority`: the store exercised here is `dl-enclave`'s file-backed addon store, not the
  canonical durable record R3 names.

## 7. The next artifact

A restore that reconstructs the Mongo authority on this host from declared inputs, with
`systemd-creds` credentials, then re-runs this drill against it — and the register row `AF-29`
already names the rule that permits it.
