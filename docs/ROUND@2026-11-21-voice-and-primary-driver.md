# ROUND — the voice of the host, and the primary driver

**Document identity:** `ROUND@2026-11-21-voice-and-primary-driver`
**Status:** answered. The owner's selected words are recorded in `docs/answers.txt` under
`## ROUND 2026-11-21` and are quoted here unchanged.
**Trigger:** the owner refused a transcript where I read the Debian host's probe aloud through the
Windows synthesizer. The refusal is recorded in
`deadlock-model-forge/logs/authority/2026-11-21-speaking-for-the-debian-host.jsonl`.

## 1. What was asked, and what the owner answered

| Id | Question | Answer |
|---|---|---|
| Q-S1 | Which component is the voice of the host? | The host's package carries the line; neither axis nor driver composes it, per `Voice.java`. |
| Q-S2 | What is the primary driver? | The axis itself is the primary driver, and nodes are its hands. |
| Q-S3 | May the primary driver hand work to other drivers? | Yes, but only to drivers that declared the action, and the sub-ticket names its parent. |
| Q-S4 | Must every word come from the host's served data? | Yes, from served fields only, and an unnamed state is refused. Lies are handled too, in the ala-cities original reference; speech is authored only from what the system learns; the prose checkers from the blender addon and Brass Meridian are new and need backporting. |
| Q-S5 | Where does the waveform live? | The host writes a WAV artifact and streams it as a package with a receipt. |
| Q-S6 | Is espeak-ng the accepted engine? | Voice is a separate packaged component with its own revision. |
| Q-S7 | Does every spoken line become a ledger row? | Yes: one row per line, naming the engine, the values read and whether sound was produced. |
| Q-S8 | MongoDB or the speech loop first? | MongoDB restore first, as Restore@1 states. |
| Q-S9 | Are evidence documents in the two-second rule's scope? | Yes, every document, including the evidence records. |
| Q-S10 | Is the civilian prototype the speech reference? | Yes: port the rule of attested words, unsayable refusal and one line per breath. |

## 2. What each answer changes

- **Q-S1 and Q-S10** move the line out of the server and the driver. Speech is a reading of a
  package's own fields, and a state the package cannot name is refused rather than described. This
  is the rule `Voice.java` already states: *unsayable* is a recorded refusal, not prose.
- **Q-S2 and Q-S3** give the axis two new duties: it speaks as the primary driver, and it may open a
  sub-ticket that names its parent. The `cua-unticketed` gate stays; delegation adds lineage.
- **Q-S4** adds two obligations beside the speech rule: lie handling is not to be invented here but
  read from the ala-cities original reference, and two prose checkers exist elsewhere that must be
  backported. That makes the backport an artifact with its own ticket, not a copy step.
- **Q-S5** puts audio on the existing package rules: declared size, BLAKE3 identity, a receipt for
  the adoption. The host's missing playback device stops being a defect and becomes a reason the
  waveform is a package.
- **Q-S6** retires the ad hoc `apt-get install espeak-ng` I ran on the host. The voice is a
  component with its own revision, invoked by pinned name.
- **Q-S7** extends the ledger: a line that could not be spoken is a visible row, the way
  `Voice.say` records `speech_unavailable`.
- **Q-S8** fixes the order. No further driver work until the store is the authoritative record.
- **Q-S9** widens the prose gate to the evidence records, which were 231 sentences over budget when
  measured on the host.

## 3. Consequences recorded, not yet implemented

1. The axis on the host is file-backed and in-memory. Restore@1 makes MongoDB mandatory, so Q-S8
   supersedes the current axis storage for the next unit.
2. The host has espeak-ng 1.52.0 installed from Debian's archive with no pin in a manifest. Under
   Q-S6 that installation is not evidence of a capability.
3. The prose checker on the host runs and exits 1 with 231 issues across 16 documents. Under Q-S9
   those documents are in scope.
4. The lie-handling reference named in Q-S4 is cited in `secure-shell/docs/GRADES.md` as living in
   the ala-cities reference trees. It is not on this machine; the lookup is named in this document
   so the next unit reads it rather than inventing the behaviour.

## 4. Absent, and named as absent

- No MongoDB service on the host; `mongod` is not installed.
- No packaged voice component; the installed synthesizer is unpinned.
- No sub-ticket field in `server/axis.mjs`; delegation lineage does not exist yet.
- The ala-cities lie-handling source has not been read in this round. **The first lookup was wrong
  and its conclusion is withdrawn.** Two repository names were guessed and both answered 404; the
  account listing then showed the reference is `alacripose/ala-cities`, public, Rust, branch `main`,
  tree `72a2f96a`, with `src`, `docs`, `tools`, `saves` and a 2.7 MB `GOD_AGENTS.md` at the root. No
  copy exists under `<home>\Documents` or `F:\Documents`, so it is read through the
  integration. A code search for `deception OR lie OR lying` in that repository returned zero hits,
  so the behaviour is named in its own vocabulary and has not been located yet.
- **The local inventory, measured, after three wrong claims.** `~/ala-cities` holds only `target/`.
  `Documents/ala_cities_v2` holds two design analysis documents and no source. `F:\ala-cities-temp`
  holds four test folders and one kache file. `scan_stream@2026-11-04.jsonl` carries 21 root sections
  and none is an `ala-cities` source. `HYPERGRILLING.md` L-1 item 3 names
  `<home>\AppData\Local\Temp\opencode\ala-cities-design-package` as source-of-record, and
  `LEDGER.md:2939` cites `src/gov/mod.rs` read there at 1,823 lines; that path is absent after the
  2026-11-21 Temp clear. The public repository is the read path. The repeated absence claim is
  recorded as `AF-34` in `SECURE-SHELL-HEALTH@1.FAILURE-LEDGER.md` and in
  `deadlock-model-forge/logs/authority/2026-11-21-absent-declared-without-inventory.jsonl`.

No implementation is claimed by this document.
