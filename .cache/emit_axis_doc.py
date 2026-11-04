"""Insert 8.1 (the Debian axis shell) into the architecture document, once.

The section is inserted before the first `## 9.` heading. Re-running is a no-op, so this is safe to
repeat in a batch. Writes bytes, never text mode: a text write on Windows emits CRLF.
"""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs" / "SECURE-SHELL-RESTORE@1.ARCHITECTURE.md"
MARK = "### 8.1 The Debian axis shell and its node drivers"

BLOCK = """### 8.1 The Debian axis shell and its node drivers

The restore grade's first deliverable is the axis: the Debian-side authority every CUA node driver must
pass through. It is code in the `secure-shell` checkout, not a claim this document makes on its behalf.

| Piece | Path | What it is |
|---|---|---|
| Axis core | `server/axis.mjs` | driver registry, attestation, ticket gate, receipts |
| HTTP edge | `server/axis-server.mjs` | loopback-by-default endpoints for drivers on the host |
| Core checks | `server/test/axis.test.mjs` | the gate, the lapses, the learning digest |
| Edge checks | `server/test/axis-server.test.mjs` | the same refusals over a real socket |
| Driver | `server/axis-driver.mjs` | the node driver: ticket first, then the act |
| Driver checks | `server/test/axis-driver.test.mjs` | ordering, lapses, and a refused bundle |
| Unit | `deploy/secure-shell-axis.service` | systemd, no capabilities, read-only home |
| Installer | `deploy/install-debian.sh` | refuses to run without root; installs and enables |

**The gate.** A driver that presents no ticket is refused `cua-unticketed` before anything runs; the
wording of that refusal belongs to the failure model in §11, and this section only says which code
implements it. A ticket names one driver, one action and one scope, is issued only for a capability the
driver declared, expires, and cannot carry a different action. An attestation that lapses between ticket
and act refuses the act instead of letting it finish on a stale grant. The module's complete refusal set
is its exported `CODES`; it is the single enumeration, and it is not copied here.

**The driver, and what it refuses to claim.** The node driver declares `witness` and `learning-apply`,
and deliberately does not declare `kernel`. It hashes a path on the device and applies a learned bundle
under its own state root, and it does neither until the axis has issued a ticket for that exact action
and the act has been reported: authorization first, device second, so a refusal leaves the device
untouched rather than half-touched. A bundle that is not UTF-8 text is refused by name instead of being
mangled, because the act carries text today and a driver that silently transcoded a lesson would be
replicating something the axis never authorized. A witness receipt carries the digest it witnessed, so
the record says what was seen rather than only that something happened.

**Securing itself over time.** Attestation carries an expiry. When it lapses the driver is untrusted,
new tickets are refused, and `review()` names every driver awaiting re-attestation; re-attestation
restores trust without re-registering the driver. That is the internal driver model securing the shell
over time rather than once at install: grants are short-lived and renewal is an explicit act.

**Learning replicated under the same gate.** `learning-apply` is a ticketed act like any other, and it
applies only when the bundle's bytes hash to the digest the axis was given. A device cannot be taught by
a bundle that was never authorized, and bytes that changed in flight are refused by name rather than
applied.

**Scope, stated honestly.** `kernel` is a declared scope and a refusal boundary, not a privilege the
axis exercises. Nothing in this code performs a kernel write, and nothing here claims to. What it
guarantees is narrower and checkable: a kernel-scoped action cannot be requested by a driver that did
not declare `kernel`, and cannot run unticketed. The unit file grants the service no capabilities at
all for the same reason.

**Audit source.** The restore grade's premise was audited against the transcript *The Rapid Progress of
Realtime Simulations* (owner-supplied, 2026-11-04, 14,287 bytes). It supports exactly one premise:
that a body needs an understanding of the world before it can be granted control of one — "when we
finally give AI bodies that it can control, it will understand how it can interact with the world for
itself". It is a commentary on world-model progress, not a design document, and no requirement here is
attributed to it beyond that premise.

**Absent, and recorded as absent.** `systemd-analyze` is not installed on this Windows host
(`command -v systemd-analyze` exits non-zero), so the unit file has not been validated by systemd here
and is not reported as valid. The module checks are module checks: by AV-001 they are not a client
witness and may not be cited as one.
"""


def main() -> int:
    raw = DOC.read_bytes().decode("utf-8")
    if MARK in raw:
        print("present: 8.1 already inserted; nothing written")
        return 0
    lines = raw.split("\n")
    index = next((i for i, line in enumerate(lines) if line.startswith("## 9.")), -1)
    if index < 0:
        print("refused: no '## 9.' heading in the architecture document")
        return 2
    if not raw.endswith("\n"):
        print("refused: document does not end with a newline")
        return 3
    merged = "\n".join(lines[:index]) + "\n" + BLOCK + "\n".join(lines[index:])
    DOC.write_bytes(merged.encode("utf-8"))
    print("inserted: 8.1 before line %d (%s)" % (index + 1, lines[index].strip()))
    print("cr present: %s" % ("\r" in merged))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
