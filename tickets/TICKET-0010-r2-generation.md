# TICKET-0010 — R2: the OpenLock generator runs, and byte identity is environment-conditional

**Status:** `complete` for the run; the milestone itself is **not** closed.
**Owner authority:** the owner's turn of 2026-11-04, source `user`: "openlock has the template
generator". That sentence is the unit's premise and it is true: `C:\Users\ala\Documents\openlock\
tools\gen_shell_data.py` is the generator, reading `shell/alpha-shell/package.shspec`,
`package.cells` and `frames/*.frame` and writing `clientaddon/panorama/scripts/
openlock_shell_data.js`.

## 1. The goal, quoted

> Select and generate from OpenLock's real sources; record selection and rejection; capture
> generator identity — exit condition: "Clean regeneration reproduces byte identity; no hand-edited
> generated output"

(`docs/SECURE-SHELL-RESTORE@1.IMPLEMENTATION-PLAN.md` §3, R2.)

## 2. The one artifact

No new repository artifact: the unit's evidence is a real run of the existing generator, recorded
here with its digests. Nothing was edited in the OpenLock tree; both outputs went to temp paths.

## 3. The last check's three-way answer

The generator was `absent` from the record — named as a missing prerequisite in `TICKET-0007`,
`TICKET-0008` and `TICKET-0009`. It was present the whole time, which is `AF-23` again, one level
out. It is now `held` in the narrow sense that it runs and reports; the milestone is not `held`.

## 4. The drift signal observed

Generation is a function of the machine as well as of the package. Two runs on this host agree
exactly; the committed asset does not agree with either.

| Run | Result |
|---|---|
| `python tools/gen_shell_data.py shell/alpha-shell /tmp/gen1/openlock_shell_data.js` | exit 0, `349 windows, 9 refusals, 22 wishes` |
| the same command again into `/tmp/gen2` | exit 0, same counts |
| `cmp` between the two runs | identical |
| size and digest of both | `482,260` bytes, `blake3 7831bd21c600545254d119f2ba8f028910e305086883b29dc5815c77e8bb6c82` |
| committed `clientaddon/panorama/scripts/openlock_shell_data.js` | `482,057` bytes, **not** identical |

The diff names the cause rather than a mystery: the committed copy carries `release shape` where a
fresh run carries `dev shape`, and the fresh run additionally discovers
`game:citadel@C:/Users/ala/Downloads/Reduced_CSDK_13`. The generator shapes its output from the
Steam libraries and Deadlock installs it finds on the host. So byte identity holds **per
environment**, not across environments, and a clean host will not reproduce this workstation's
bytes without its discovered installs pinned.

As a package under the shipped contract, both runs agree:
`secure-shell-openlock-shell-data@1+blake3:9a9c74f1b7dccbadc1838efd52b72ebe0e1834e31318f6198f6f8d7295e87097`.

## 5. Refusals this unit carries forward

- R2 is **not** closed: the exit condition says "clean regeneration reproduces byte identity", and
  a clean host has not been tried. What is proven is that this host regenerates identically.
- The generator identity is not yet inside the package. The digest above covers the output, not the
  `gen_shell_data.py` revision that produced it, so the same bytes from a different generator would
  be indistinguishable.
- The committed generated asset is stale relative to a fresh run on this host. That is a delivery
  question for the OpenLock project, not something this repository may silently rewrite.
- R3 is still unrun: the store code exists (`dl-enclave/tools/port/src/addon-store.mjs` with
  `store-digest`, `store-package`, `store-index` refusals; `secure-shell/server/` with
  `ingest.mjs`, `ledger.mjs` and the axis), but no Debian host was built and no restore drill ran.
  `secure-shell/docs/DECISIONS.md` records "no MongoDB dependency" as the owner's 2026-10-31
  instruction, so a `mongod` on this workstation is not the authority the plan describes.

## 6. The next artifact

A pinned-input regeneration record: the package digest, the generator revision digest, and the
discovered-install set, so "regenerates byte-identically" is a claim about named inputs instead of
about one machine's Steam library.

## 7. The record entry just written

`AF-25` in `docs/SECURE-SHELL-HEALTH@1.FAILURE-LEDGER.md`.
