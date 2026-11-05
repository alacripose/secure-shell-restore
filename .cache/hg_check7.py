import json
import pathlib
import re
import sys

failures = []


def check(name, ok, detail=""):
    print(f"{'PASS' if ok else 'FAIL'}  {name}{'' if ok else '  <- ' + detail}")
    if not ok:
        failures.append(name)


MODULE = pathlib.Path("C:/Users/ala/Documents/secure-shell/shell/openlock/panorama/scripts/secure_shell_rounds.js")
TEST = pathlib.Path("C:/Users/ala/Documents/secure-shell/tests/rounds.test.mjs")
ARCH = pathlib.Path("docs/SECURE-SHELL-RESTORE@1.ARCHITECTURE.md")
CLIENT_DIR = pathlib.Path("C:/Users/ala/Documents/secure-shell/client")

check("the client gate exists", MODULE.is_file(), str(MODULE))
check("its test exists", TEST.is_file(), str(TEST))
# The 2026-11-04 claim was that client/ is empty. It was true then and false from 2026-11-05, when
# the window was built (TICKET-0013). The check now asserts the state that exists, not the absence
# that ended; the document keeps the original sentence and its dated supersession beside it.
CLIENT_WINDOW = CLIENT_DIR / "index.html"
check("the client window exists and is the one TICKET-0013 names",
      CLIENT_WINDOW.is_file() and CLIENT_WINDOW.stat().st_size > 0,
      str(sorted(p.name for p in CLIENT_DIR.iterdir())) if CLIENT_DIR.is_dir() else "missing")

module_text = MODULE.read_text(encoding="utf-8")
codes_in_module = set(re.findall(r'"(round-[a-z-]+)"', module_text))
print("codes in module:", sorted(codes_in_module))

arch = ARCH.read_text(encoding="utf-8")
section = arch.split("### 9.1 A question is not open until it is asked", 1)[1].split("## 10. Axis CUA", 1)[0]
codes_in_doc = set(re.findall(r"`(round-[a-z-]+)`", section))
print("codes in 9.1:", sorted(codes_in_doc))
check("9.1 names every code the module refuses", codes_in_module <= codes_in_doc,
      str(sorted(codes_in_module - codes_in_doc)))
check("9.1 claims no code the module lacks", codes_in_doc <= codes_in_module,
      str(sorted(codes_in_doc - codes_in_module)))
check("9.1 names the module path", "shell/openlock/panorama/scripts/secure_shell_rounds.js" in section)
check("9.1 names the test", "tests/rounds.test.mjs" in section)
check("9.1 records the client/ absence and its dated supersession",
      "`ls -la client`" in section and "empty directory" in section
      and "Superseded 2026-11-05" in section and "index.html" in section)
check("9.1 states what the gate does not do", "does not deliver a round" in section)
check("9.1 no longer claims enforcement it lacks", "A question only the owner can answer is recorded as open" in section)

state = json.loads(pathlib.Path("docs/hypergrill/state.json").read_text(encoding="utf-8"))
counts = {}
for entry in state["questions"].values():
    counts[entry["status"]] = counts.get(entry["status"], 0) + 1
receipts = pathlib.Path("docs/hypergrill/receipts.jsonl").read_text(encoding="utf-8").strip().splitlines()
print("state:", counts, "entries:", len(state["questions"]), "receipts:", len(receipts))
check("state still 180 entries", len(state["questions"]) == 180, str(len(state["questions"])))
check("178 resolved, 1 folded, 1 struck, 0 open",
      (counts.get("resolved"), counts.get("folded"), counts.get("struck"), counts.get("open", 0))
      == (178, 1, 1, 0), str(counts))
check("61 receipts", len(receipts) == 61, str(len(receipts)))

ws = pathlib.Path("docs/SECURE-SHELL-RESTORE@1.HYPERGRILL.md").read_text(encoding="utf-8")
m = re.search(r"holds (\d+) entries: (\d+) resolved, (\d+) folded, (\d+) struck, (\d+) open", ws)
check("8.3 still matches the files", bool(m) and tuple(int(x) for x in m.groups())
      == (len(state["questions"]), counts.get("resolved"), counts.get("folded"),
          counts.get("struck"), counts.get("open", 0)))

check("architecture has no CR", b"\r" not in ARCH.read_bytes())
check("module has no CR", b"\r" not in MODULE.read_bytes())
check("test has no CR", b"\r" not in TEST.read_bytes())

print(f"\nRESULT: {'PASS' if not failures else 'FAIL ' + str(failures)}")
sys.exit(0 if not failures else 1)
