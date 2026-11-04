"""Check the axis shell against the document that describes it, and the record it must not disturb.

Every check is a command with an exit status. A check that cannot run prints `absent: <tool>` and is
recorded as absent, never as a pass.
"""

from pathlib import Path
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parent / "secure-shell"
DOC = ROOT / "docs" / "SECURE-SHELL-RESTORE@1.ARCHITECTURE.md"
AXIS = REPO / "server" / "axis.mjs"
SERVER = REPO / "server" / "axis-server.mjs"
DRIVER = REPO / "server" / "axis-driver.mjs"
TESTS = [
    REPO / "server" / "test" / "axis.test.mjs",
    REPO / "server" / "test" / "axis-server.test.mjs",
    REPO / "server" / "test" / "axis-driver.test.mjs",
]
UNIT = REPO / "deploy" / "secure-shell-axis.service"
INSTALLER = REPO / "deploy" / "install-debian.sh"

failures = []
checks = 0


def check(name, ok, detail=""):
    global checks
    checks += 1
    if ok:
        print("ok   %s" % name)
    else:
        print("FAIL %s%s" % (name, (": " + detail) if detail else ""))
        failures.append(name)


def text(path):
    return path.read_bytes().decode("utf-8")


def flat(value):
    """Collapse prose whitespace so a wrapped title is still the title."""
    return " ".join(value.split())


def section_81(doc):
    start = doc.find("### 8.1 The Debian axis shell")
    if start < 0:
        return ""
    end = doc.find("\n## 9.", start)
    return doc[start:] if end < 0 else doc[start:end]


def entries_of(state):
    if isinstance(state, list):
        return state
    if isinstance(state, dict):
        if isinstance(state.get("questions"), dict):
            return [dict(entry, id=key) for key, entry in state["questions"].items()]
        if isinstance(state.get("entries"), list):
            return state["entries"]
        return [dict(entry, id=key) for key, entry in state.items() if isinstance(entry, dict)]
    return []


def main():
    required = [AXIS, SERVER, DRIVER, UNIT, INSTALLER] + TESTS
    for path in required:
        check("exists %s" % path.relative_to(REPO), path.is_file())

    if not all(path.is_file() for path in required):
        print("\nrefused: a required file is missing; the remaining checks are absent")
        return 2

    doc = text(DOC)
    axis = text(AXIS)
    server = text(SERVER)
    unit = text(UNIT)
    installer = text(INSTALLER)
    s81 = section_81(doc)
    s81_flat = flat(s81)

    check("architecture has 8.1", s81 != "")
    check("8.1 cites the failure model it implements", "\u00a711" in s81)
    check("8.1 names cua-unticketed", "`cua-unticketed`" in s81)
    check("8.1 records systemd-analyze absent", "systemd-analyze" in s81_flat and "Absent" in s81)
    check("8.1 names the audited transcript",
          "The Rapid Progress of Realtime Simulations" in s81_flat)
    check("8.1 records the audit premise", "understanding of the world" in s81_flat)
    check("8.1 does not restate the refusal set",
          "ticket-scope" not in s81 and "driver-duplicate" not in s81,
          "a second writer of the code set appeared in 8.1")

    # The failure model owns the wording; the module must implement it.
    model = doc[doc.find("## 11. Failure model"):]
    cut = model.find("\n## 12.")
    if cut >= 0:
        model = model[:cut]
    check("failure model names cua-unticketed", "cua-unticketed" in model)

    codes_match = re.search(r"export const CODES = Object\.freeze\(\[(.*?)\]\)", axis, re.S)
    check("axis exports a closed CODES array", codes_match is not None)
    codes = re.findall(r'"([a-z][a-z-]*)"', codes_match.group(1)) if codes_match else []
    check("CODES is non-empty and unique", len(codes) > 0 and len(set(codes)) == len(codes))
    check("CODES implements the failure model refusal", "cua-unticketed" in codes)

    raised = set(re.findall(r'new AxisError\(\s*"([a-z][a-z-]*)"', axis))
    unknown = sorted(raised - set(codes))
    check("every literal refusal raised is in CODES", unknown == [], "unknown: %s" % unknown)

    check("edge refuses unknown routes by name", '"route-unknown"' in server)
    check("edge binds loopback unless told otherwise", '"127.0.0.1"' in server)
    check("edge bounds its body", "MAX_BODY = 1_000_000" in server)

    exec_line = next((line for line in unit.split("\n") if line.startswith("ExecStart=")), "")
    check("unit starts the axis edge", exec_line.endswith("server/axis-server.mjs"), exec_line)
    check("unit grants no capabilities", "\nCapabilityBoundingSet=\n" in unit)
    check("unit does not run as root", "User=root" not in unit)
    check("unit hardens the filesystem",
          "ProtectSystem=strict" in unit and "ProtectHome=read-only" in unit)

    check("installer refuses without root", "id -u" in installer and "exit 3" in installer)
    check("installer requires node", "command -v node" in installer)

    # A driver that acts below the application layer must be the one to say so, not this document.
    driver_text = text(DRIVER)
    declared = re.search(r"export const CAPABILITIES = Object\.freeze\(\[(.*?)\]\)", driver_text, re.S)
    says = re.findall(r'"([a-z][a-z-]*)"', declared.group(1)) if declared else []
    check("driver declares capabilities", len(says) > 0)
    check("driver claims no kernel capability", "kernel" not in says, str(says))
    check("8.1 says the driver claims no kernel", "does not declare `kernel`" in s81_flat)
    check("driver authorizes before it writes",
          driver_text.find("/api/axis/tickets") < driver_text.find("writeFileSync("))
    check("8.1 names the driver", "server/axis-driver.mjs" in s81)

    # The section and the emitter that writes it must be the same text, or one is a second writer.
    emitter = text(ROOT / ".cache" / "emit_axis_doc.py")
    opened = emitter.find('BLOCK = """')
    closed = emitter.find('"""', opened + 11) if opened >= 0 else -1
    block = emitter[opened + 11:closed] if opened >= 0 and closed > 0 else ""
    check("emitter carries the section it would write", flat(block) == s81_flat,
          "emitter BLOCK and 8.1 differ")

    if sys.platform == "win32":
        print("absent: executable-bit check (win32 reports no POSIX mode; run on Debian to check)")
    else:
        check("installer is executable", bool(INSTALLER.stat().st_mode & 0o111))

    for path in required:
        body = path.read_bytes()
        check("LF only %s" % path.relative_to(REPO), b"\r" not in body and body.endswith(b"\n"))

    # The parked record must not move because a deliverable landed.
    state = json.loads((ROOT / "docs" / "hypergrill" / "state.json").read_text(encoding="utf-8"))
    entries = entries_of(state)
    check("hypergrill record is readable", len(entries) > 0)
    check("hypergrill entry ids are unique", len({entry["id"] for entry in entries}) == len(entries))

    statuses = {}
    for entry in entries:
        key = entry.get("status", "")
        statuses[key] = statuses.get(key, 0) + 1
    check("every entry has a known status",
          set(statuses) <= {"resolved", "open", "struck", "folded", "superseded"},
          str(sorted(statuses)))
    check("status counts sum to the table", sum(statuses.values()) == len(entries),
          "%d vs %d" % (sum(statuses.values()), len(entries)))

    receipts = [line for line in (ROOT / "docs" / "hypergrill" / "receipts.jsonl")
                .read_text(encoding="utf-8").split("\n") if line.strip()]
    parsed = 0
    for line in receipts:
        try:
            json.loads(line)
            parsed += 1
        except json.JSONDecodeError:
            pass
    check("every receipt parses", parsed == len(receipts), "%d of %d" % (parsed, len(receipts)))
    print("note: %d entries %s, %d receipts" %
          (len(entries), dict(sorted(statuses.items())), len(receipts)))

    print("\n%d checks, %d failed" % (checks, len(failures)))
    if failures:
        print("failed: " + ", ".join(failures))
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
