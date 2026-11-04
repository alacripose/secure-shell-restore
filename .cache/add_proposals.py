from pathlib import Path

doc = Path("docs/SECURE-SHELL-RESTORE@1.CUA-CIVILIAN-ACCEPTANCE.md")
raw = doc.read_bytes().decode("utf-8")

# E8 and E7 are defined once, in the new proposals subsection; drop "extended" wording that pointed forward.
raw = raw.replace(
    "- E8 is extended with `refusedBy` and one recovery line rather than duplicated.",
    "- E8 carries `refusedBy` and one recovery line rather than a second rule.",
    1,
)
raw = raw.replace(
    "  document refuses a presentation with no accountable actor. E7 is extended with `presenter`.",
    "  document refuses a presentation with no accountable actor. E7 gains a `presenter` field.",
    1,
)

assert "### 11.10 Named absent" in raw
assert "### 11.10 Proposals" not in raw

PROP = """### 11.10 Proposals the located documents ground

Four documents state a rule this driver does not have, and one states a field an existing rule lacks.
Each row is a proposal, not a change: no driver behaviour moves until the row has a ticket.

| Rule | The proposal | Where it binds | Exit test |
|---|---|---|---|
| E7 (extension) | The receipt names a **presenter** — the accountable actor — beside the driver id | `act()` receipt, `server/axis.mjs` | a witness presented with no presenter is refused by name |
| E8 | A refusal is recorded, not only thrown: code, subject, why, `refusedBy`, and one recovery line | `act()` and the axis refusal path, `server/axis.mjs` | a refused act leaves a readable record naming `refusedBy`, and a client renders code, who and recovery without inventing any of them |
| E9 | A driver's declared capabilities are a subset of what its attestation grants; the axis refuses the difference | `attest()` and registration, `server/axis.mjs` | a driver declaring a capability its grant does not carry is refused `capability-not-granted` |
| E10 | A hard-deny set stands above capabilities: some actions have no ticket whatever a driver declares | `requestTicket`, `server/axis.mjs` | a driver declaring `move-money` is refused `hard-deny` before a ticket exists |
| E11 | A receipt answers read, absent and refused separately, and never defaults an unread digest to empty | the `act` receipt | an act with no digest is refused by name rather than recorded `digest: ""` |

E5 and E6 are not restated: E5 already covers expected-versus-observed and E6 already covers digest
recomputation, and both are corroborated rather than extended by the documents above.

"""

raw = raw.replace("### 11.10 Named absent", PROP + "### 11.11 Named absent", 1)
doc.write_bytes(raw.encode("utf-8"))
print("bytes:", len(raw.encode("utf-8")), "| CR:", "\r" in raw, "| newline:", raw.endswith("\n"))
print("headings:", [l for l in raw.split("\n") if l.startswith("### 11.")])

check = Path(".cache/hg_check9.py")
craw = check.read_bytes().decode("utf-8")
craw = craw.replace('"### 11.10 Named absent" in doc', '"### 11.11 Named absent" in doc')
craw = craw.replace(
    'check("the absence section follows the located documents", "### 11.11 Named absent" in doc)',
    'check("the absence section follows the located documents", "### 11.11 Named absent" in doc)\n'
    '    check("the proposals subsection exists", "### 11.10 Proposals" in doc)',
    1,
)
check.write_bytes(craw.encode("utf-8"))
print("check9 anchors:", craw.count("11.11"), "| proposals:", craw.count("11.10"))
