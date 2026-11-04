"""Exit tests for the loader: a real tree becomes one identity, whatever order it was written in.

Run: python tests/packages/run_cases_loader.py
"""

from __future__ import annotations

import sys
import tempfile
import traceback
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from impl.packages import canonical as cn  # noqa: E402
from impl.packages import identity as idn  # noqa: E402
from impl.packages import loader  # noqa: E402

CASES: list = []


def case(function):
    CASES.append(function)
    return function


def tree(files: dict[str, bytes], order: list[str] | None = None) -> Path:
    root = Path(tempfile.mkdtemp(prefix="loader-"))
    for name in order or list(files):
        path = root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(files[name])
    return root


FILES = {
    "layout/openlock_shell.xml": b"<root><Panel id=\"Taskbar\" /></root>\n",
    "scripts/openlock_shell.js": b"function boot() { return 1; }\n",
    "styles/openlock_shell.css": b".ShellRoot { width: 100%; }\n",
}


@case
def a_tree_becomes_one_identity():
    record = loader.build(tree(FILES), "secure-shell-openlock-shell", 1)
    assert record["state"] == "held"
    assert record["files"] == 3
    assert record["identity"] == f"secure-shell-openlock-shell@1+blake3:{record['digest'][len('blake3:'):]}"
    assert idn.parse_identity(record["identity"])["name"] == "secure-shell-openlock-shell"


@case
def identity_does_not_depend_on_creation_order():
    first = loader.build(tree(FILES), "secure-shell-openlock-shell", 1)
    second = loader.build(tree(FILES, order=list(reversed(list(FILES)))), "secure-shell-openlock-shell", 1)
    assert first["digest"] == second["digest"], (first["digest"], second["digest"])
    assert first["payload"] == second["payload"]


@case
def entry_points_are_ordered_paths():
    record = loader.build(tree(FILES), "secure-shell-openlock-shell", 1)
    points = record["manifest"]["entry_points"]
    assert points == sorted(points) == list(FILES.keys())


@case
def a_changed_byte_changes_the_identity():
    base = loader.build(tree(FILES), "secure-shell-openlock-shell", 1)
    changed = dict(FILES, **{"scripts/openlock_shell.js": b"function boot() { return 2; }\n"})
    assert loader.build(tree(changed), "secure-shell-openlock-shell", 1)["digest"] != base["digest"]


@case
def generated_directories_are_not_admitted():
    noise = dict(FILES)
    noise["node_modules/pkg/index.js"] = b"noise"
    noise["dist/bundle.js"] = b"noise"
    assert loader.build(tree(noise), "secure-shell-openlock-shell", 1)["files"] == 3


@case
def an_empty_tree_is_refused():
    try:
        loader.build(tree({}), "secure-shell-openlock-shell", 1)
    except idn.Refused as error:
        assert error.refusal == "manifest-malformed"
        return
    raise AssertionError("an empty tree produced a package")


@case
def the_package_digest_matches_the_canonical_path():
    record = loader.build(tree(FILES), "secure-shell-openlock-shell", 1)
    assert record["digest"] == cn.package_digest(record["manifest"], record["payload"])


def main() -> int:
    failures = 0
    for function in CASES:
        try:
            function()
        except Exception:  # noqa: BLE001
            failures += 1
            detail = traceback.format_exc(limit=1).strip().splitlines()[-1]
            print(f"FAIL {function.__name__}: {detail}")
        else:
            print(f"ok   {function.__name__}")
    print(f"\n{len(CASES)} cases, {failures} failed")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
