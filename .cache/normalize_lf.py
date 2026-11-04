"""Convert every generated text file to UTF-8 with LF line endings.

Windows text-mode writes translate "\\n" to "\\r\\n"; the workspace requires LF.
Binary read/write is used so the translation cannot happen again. `--self-test`
exercises the counter on a throwaway CRLF file, so the per-file number is proven
rather than asserted.
"""
import pathlib
import sys
import tempfile

TARGETS = []
TARGETS += sorted(pathlib.Path("docs").rglob("*.md"))
TARGETS += sorted(pathlib.Path("docs/hypergrill").glob("*.json"))
TARGETS += sorted(pathlib.Path("docs/hypergrill").glob("*.jsonl"))
TARGETS += sorted(pathlib.Path("tools").glob("*.py"))
TARGETS += sorted(pathlib.Path(".cache").glob("*.py"))
TARGETS += [pathlib.Path("AGENTS.md")]


def normalize(path: pathlib.Path) -> tuple[int, int]:
    """Rewrite one file with LF endings. Returns (CR before, CR after)."""
    blob = path.read_bytes()
    before = blob.count(b"\r")
    if before == 0:
        return 0, 0
    cleaned = blob.replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    path.write_bytes(cleaned)
    return before, cleaned.count(b"\r")


def self_test() -> bool:
    with tempfile.TemporaryDirectory() as tmp:
        probe = pathlib.Path(tmp) / "probe.md"
        probe.write_bytes(b"one\r\ntwo\r\nthree\r\n")
        before, after = normalize(probe)
        ok = before == 3 and after == 0 and probe.read_bytes() == b"one\ntwo\nthree\n"
        print(f"{'ok  ' if ok else 'FAIL'} self-test: counter reported {before} CR before, {after} after")
        again_before, again_after = normalize(probe)
        ok = ok and again_before == 0 and again_after == 0
        print(f"{'ok  ' if again_before == 0 else 'FAIL'} self-test: a clean file reports 0")
        return ok


def main() -> int:
    ok = self_test()
    fixed = 0
    for path in TARGETS:
        if not path.is_file():
            continue
        before, after = normalize(path)
        if before == 0:
            continue
        print(f"normalized {path}: {before} CR before, {after} after")
        fixed += 1
        if after != 0:
            ok = False
    print(f"files normalized: {fixed}")

    remaining = [str(p) for p in TARGETS if p.is_file() and b"\r" in p.read_bytes()]
    if remaining:
        print("RESULT: FAIL, CR remains in", remaining)
        return 1
    print("RESULT:", "PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
