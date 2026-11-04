# TICKET-0011 — R3: a Debian host built by the install script, and a cold restore through MongoDB

**Status:** `complete` for the pass. The **Mongo authority is now exercised**; signatures, replica
sets and backups are not.
**Owner authority:** the owner's turns of 2026-11-04, source `user`: "get the secure shell restore
actually running end to end on a Debian host, not described", then "Make the secure shell restore
real against the authority R3 actually names".

## 1. The goal, quoted

> **R3 — Debian restore** | Rebuild the MongoDB store on Debian from declared inputs; `systemd-creds`
> credentials; per-package keys; backups and a restore drill | A clean host reproduces the store
> digest; restore drill artifact exists

(`docs/SECURE-SHELL-RESTORE@1.IMPLEMENTATION-PLAN.md` §3, R3.)

## 2. The one artifact

`tools/restore_drill.py`: a 22-step run against the WSL `Debian` distro. It installs the axis with
`secure-shell/deploy/install-debian.sh`, proves the route serves, regenerates the OpenLock package
twice to byte identity, admits it through `impl/packages/loader.py`, `dl-enclave`'s store and
`impl/packages/mongo_store.py`, restores it cold out of MongoDB, re-derives the loader identity from
the restored bytes, and refuses a tampered Mongo record, a corrupted stream, a reordered stream, a
truncated stream and a tampered package — each by name, each leaving prior state unchanged.

Supporting artifacts: `impl/packages/mongo_store.py` (the authority module), `tools/mongo_setup.py`
(host configuration, users, sealed credential; idempotent), `tools/mongo_tamper.py` (the drill's
refusal fixture).

## 3. The last check's three-way answer

The Debian host and the Mongo authority were both `absent`; they are now `held`. The first attempt
failed twice (`AF-27`, `AF-28`), then the restore turned out to be writing into a file-backed store
rather than the authority R3 names (`AF-32`). Signatures stay `absent`, and `mongo_store` says so in
its own docstring rather than implying authenticity.

## 4. The drift signal

Two of them, both caught by reading exit codes: a drill that read an echoed `$?` through a transport
that blanks it (`AF-31`), and a drill that compared a payload digest with a package identity digest
and reported a correct restore as a failure (`AF-33`).

## 5. Evidence

Host: `Debian GNU/Linux 13 (trixie)`, `x86_64`, `node v22.23.4`, `mongod` `v8.0.34`, `/api/axis/state`
`http=200`.

```
ok   host identity                       exit=0  Debian GNU/Linux 13 (trixie) x86_64 node v22.23.4
ok   deploy/install-debian.sh            exit=0  installed: secure-shell-axis.service
ok   axis unit active                    exit=0  active
ok   axis serves /api/axis/state         exit=0  {"schema":"secure-shell.axis/1",...} http=200
ok   generation twice, identical bytes   exits=0,0 bytes=482260 identical=True
ok   loader identity                     exit=0  secure-shell-openlock-shell-data@1+blake3:ea32a0b5…
ok   store install / store verify        exit=0  dashboard 1.0.0 client-dashboard
ok   cold restore adopts the package     exit=0  {"adoptions":1,"state":"held","digest":"blake3:ea32a0b5…"}
ok   cold digest equals the loader identity
ok   mongod running                      exit=0  active
ok   sealed credential decrypts          exit=0  systemd-creds decrypt /etc/secure-shell/mongo-uri.cred
ok   admit into mongo                    exit=0  digest blake3:80acb981… database secure_shell
ok   cold restore from mongo             exit=0  digest blake3:80acb981… length 184
ok   restored bytes are the admitted bytes          sha256 b2d41e71… on both sides
ok   restored payload re-derives the loader identity ea32a0b5… == ea32a0b5…
ok   tamper the stored record            exit=0  1 byte flipped, stored digest left as it was
ok   mongo refuses a tampered record     exit=1  refusal=mongo-digest prior_unchanged=True
ok   refuses a digest-corrupt stream     exit=1  refusal=stream-corrupt prior_unchanged=True
ok   refuses a reordered stream          exit=1  refusal=chunk-reordered prior_unchanged=True
ok   refuses a truncated stream          exit=1  refusal=stream-truncated prior_unchanged=True
ok   store refuses a tampered package    exit=1  store-digest … index_unchanged=True
```

22 steps, 0 failed. `python tools/restore_drill.py` exits 0. CI cannot run it (it needs a WSL Debian
distro and the family checkouts); the workflow does not claim to.

**Which store the successful restore exercised:** MongoDB. The package document lives in
`secure_shell.packages` on the host's `mongod` (`127.0.0.1:27017`, `authorization: enabled`), keyed
by the canonical identity, carrying the payload and its BLAKE3 digest. The connection string is
sealed at `/etc/secure-shell/mongo-uri.cred` with `systemd-creds --with-key=host` and decrypted to
`/run/drill-mongo.uri` only for the length of a run; the app identity is `secure_shell` with
`readWrite` on `secure_shell` and nothing else. The file-backed `dl-enclave` store and the stream are
still exercised, as separate legs of the same drill.

## 6. Refusals for the next unit

- `signature-absent`: nothing in this pass signs anything. A matching digest proves the bytes are the
  bytes admitted, not who admitted them; R5 remains unbuilt.
- `replica-absent`: a single `mongod`, no replica set and no failover, so the plan's topology
  question is untouched by this pass.
- `backup-absent`: no backup or restore-from-backup path exists, and `systemd-creds` rotation is
  untested.
- `per-package-keys-absent`: R3 names per-package keys; this pass has one app identity, not one key
  per package.

## 7. The next artifact

A signing and verification step over the admitted package digest, so an admission proves authorship
and not only byte identity — and a documented backup/restore of the Mongo database it writes into.
