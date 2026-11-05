#!/usr/bin/env python3
"""The cold restore drill: a real Debian host, the real install script, a real package.

This is a local capability, like `hg_check7` and `hg_check10`: it needs a WSL Debian distro and
the family checkouts on this machine, so CI cannot run it and does not pretend to. It prints one
line per step with the exit status of the command behind it, and exits non-zero if any step fails.

Every status here is a process exit status from `wsl.exe`, which returns the status of the command
it ran. Nothing is read from an echoed `$?`: a shell that blanks the expansion makes a refusal look
like a pass, and a drill that reports its own echo as evidence proves nothing.

What it proves, in order:

  1. the host is Debian and reports its own identity;
  2. `secure-shell/deploy/install-debian.sh` installs the axis on that host;
  3. the service is up and `/api/axis/state` answers over HTTP;
  4. `openlock/tools/gen_shell_data.py` regenerates the shell twice with identical bytes;
  5. `impl/packages/loader.py` turns that fresh output into a package identity;
  6. `dl-enclave`'s addon store installs and verifies a package, and refuses a tampered one;
  7. a cold directory adopts the whole stream and reaches the same digest;
  8. a digest-corrupt, a reordered and a truncated stream each refuse by name, leaving the
     cold directory's admitted state byte-identical.

Nothing here signs anything. A BLAKE3 digest proves bytes, never authorship.
"""

from __future__ import annotations

import os as _os
import sys as _sys

_sys.path.insert(0, _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))))


import hashlib
import json

from blake3 import blake3

from impl.packages.toolstream import ToolStream
import os
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = Path("C:/Users/ala/Documents")
OPENLOCK = DOCS / "openlock"
SECURE_SHELL = DOCS / "secure-shell"
ENCLAVE = DOCS / "dl-enclave"
DISTRO = "Debian"
VENV = "/opt/drill-venv/bin/python"
STORE = "/srv/drill/store"
COLD = "/srv/drill/cold"
CHUNK = 64


def mount(path: Path) -> str:
    win = str(path).replace("\\", "/")
    return "/mnt/" + win[0].lower() + win[2:]


WSL_ROOT = mount(ROOT)
WSL_SHELL = mount(SECURE_SHELL)
STORE_CLI = mount(ENCLAVE) + "/tools/port/src/addon-store.mjs"

results: list[tuple[str, int]] = []
STREAM = ToolStream("restore-drill")


def wsl(script: str, timeout: int = 300) -> tuple[int, str]:
    proc = subprocess.run(
        ["wsl.exe", "-d", DISTRO, "-u", "root", "--", "sh", "-c", script],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        timeout=timeout,
    )
    return proc.returncode, (proc.stdout + proc.stderr).replace("\x00", "").strip()


def step(name: str, ok: bool, detail: str) -> bool:
    """One event on the stream, one human line on stderr; stdout stays adoptable."""
    results.append((name, 0 if ok else 1))
    STREAM.emit({
        "event": "step",
        "name": name,
        "state": "held" if ok else "refused",
        "detail": detail.splitlines()[:12],
    })
    print(f"{'ok  ' if ok else 'REFUSED'} {name}", file=sys.stderr)
    for line in detail.splitlines()[:12]:
        print(f"       {line}", file=sys.stderr)
    return ok


def windows(command: list[str], cwd: Path) -> tuple[int, str]:
    proc = subprocess.run(command, cwd=cwd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    return proc.returncode, (proc.stdout + proc.stderr).strip()


def json_line(text: str) -> dict:
    for line in reversed(text.splitlines()):
        if line.startswith("{"):
            try:
                return json.loads(line)
            except json.JSONDecodeError:
                continue
    return {}


def dir_digest(path: str = COLD) -> str:
    code, out = wsl(f"cd {path} && find . -type f -print0 | sort -z | xargs -0 sha256sum")
    return hashlib.sha256(out.encode()).hexdigest()[:16] if code == 0 else ""


def main() -> int:
    print(f"=== restore drill · {time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}", file=sys.stderr)

    code, out = wsl("grep -E '^(PRETTY_NAME|VERSION_ID)=' /etc/os-release; uname -m; node -v; id -u")
    step("host identity", code == 0 and "Debian" in out, f"exit={code}\n{out}")

    code, out = wsl(f"cd {WSL_SHELL} && sh deploy/install-debian.sh")
    step("deploy/install-debian.sh", code == 0, f"exit={code}\n{out}")
    if code != 0:
        return 1

    code, out = wsl("systemctl restart secure-shell-axis; sleep 2; systemctl is-active secure-shell-axis")
    step("axis unit active", code == 0 and out.strip() == "active", f"exit={code}\n{out}")
    if code != 0:
        return 1

    code, out = wsl("curl -fsS -m 5 -w '\\nhttp=%{http_code}' http://127.0.0.1:8787/api/axis/state")
    step("axis serves /api/axis/state", code == 0 and "secure-shell.axis/1" in out, f"exit={code}\n{out}")
    if code != 0:
        return 1

    # The epoch is pinned for both runs: the generator stamps a time into the bytes, so an
    # unpinned pair is two packages and the drill would be measuring the clock.
    os.environ["SOURCE_DATE_EPOCH"] = str(int(time.time()))
    genA = Path(tempfile.mkdtemp(prefix="drill-genA-"))
    genB = Path(tempfile.mkdtemp(prefix="drill-genB-"))
    codeA, outA = windows([sys.executable, "tools/gen_shell_data.py", "shell/alpha-shell", str(genA / "openlock_shell_data.js")], OPENLOCK)
    codeB, outB = windows([sys.executable, "tools/gen_shell_data.py", "shell/alpha-shell", str(genB / "openlock_shell_data.js")], OPENLOCK)
    a = (genA / "openlock_shell_data.js").read_bytes() if (genA / "openlock_shell_data.js").is_file() else b""
    b = (genB / "openlock_shell_data.js").read_bytes() if (genB / "openlock_shell_data.js").is_file() else b""
    step(
        "generation twice, identical bytes",
        codeA == 0 and codeB == 0 and bool(a) and a == b,
        f"exits={codeA},{codeB} bytes={len(a)} sha256={hashlib.sha256(a).hexdigest()[:16]} identical={a == b}\n"
        + (outA.splitlines()[-1] if outA else ""),
    )

    bundle = ROOT / ".cache" / "realpkg"
    shutil.rmtree(bundle, ignore_errors=True)
    code, out = windows(
        [sys.executable, "-m", "impl.packages.loader", "--root", str(genA), "--name",
         "secure-shell-openlock-shell-data", "--extensions", ".js", "--write", str(bundle)],
        ROOT,
    )
    identity = json_line(out).get("identity", "") if code == 0 else ""
    step("loader identity", bool(identity), f"exit={code}\n{identity or out}")
    if not identity:
        return 1

    code, out = wsl(f"rm -rf {STORE}; node {STORE_CLI} install {mount(ENCLAVE)}/clientaddon/dashboard --store {STORE}")
    step("store install", code == 0, f"exit={code}\n{out}")
    if code != 0:
        return 1

    code, out = wsl(f"node {STORE_CLI} verify --store {STORE}")
    step("store verify", code == 0 and "dashboard" in out, f"exit={code}\n{out}")
    if code != 0:
        return 1

    code, out = wsl(
        f"rm -rf {COLD}; mkdir -p {COLD}; cd {WSL_ROOT}; "
        f"{VENV} -m impl.packages.stream receive --manifest .cache/realpkg/manifest.json "
        f"--payload .cache/realpkg/payload.bin --chunk-size 1024 --prior ''"
    )
    adopted = json_line(out).get("digest", "") if code == 0 else ""
    step("cold restore adopts the package", bool(adopted), f"exit={code}\n{out}")
    if not adopted:
        return 1

    step(
        "cold digest equals the loader identity",
        identity.endswith(adopted.split(":", 1)[1]),
        f"{adopted} vs {identity}",
    )

    # The authority R3 names. The URI comes out of a sealed credential at run time, so the drill
    # exercises the credential path it intends to rely on rather than a plaintext file beside it.
    # The Mongo record carries the payload digest; the identity digest is over the canonical
    # package. They are two different digests, and comparing them was the drill's own bug.
    payload_digest = "blake3:" + blake3((bundle / "payload.bin").read_bytes()).hexdigest()
    code, out = wsl("systemctl is-active mongod")
    step("mongod running", code == 0 and out.strip() == "active", f"exit={code}\n{out}")

    code, out = wsl("systemd-creds decrypt --name=mongo-uri /etc/secure-shell/mongo-uri.cred /run/drill-mongo.uri")
    step("sealed credential decrypts", code == 0, f"exit={code}\n{out.splitlines()[-1] if out else ''}")

    code, out = wsl(
        f"cd {WSL_ROOT}; {VENV} -m impl.packages.mongo_store admit --uri-file /run/drill-mongo.uri "
        f"--identity '{identity}' --manifest .cache/realpkg/manifest.json "
        f"--payload .cache/realpkg/payload.bin --database secure_shell"
    )
    admitted = json_line(out) if code == 0 else {}
    step("admit into mongo", code == 0 and admitted.get("digest") == payload_digest, f"exit={code}\n{out}")

    mongo_dir = "/srv/drill/cold-mongo"
    code, out = wsl(
        f"rm -rf {mongo_dir}; mkdir -p {mongo_dir}; cd {WSL_ROOT}; "
        f"{VENV} -m impl.packages.mongo_store restore --uri-file /run/drill-mongo.uri "
        f"--identity '{identity}' --database secure_shell --out {mongo_dir}/payload.bin"
    )
    restored = json_line(out) if code == 0 else {}
    step("cold restore from mongo", code == 0 and restored.get("digest") == payload_digest, f"exit={code}\n{out}")

    local = hashlib.sha256((bundle / "payload.bin").read_bytes()).hexdigest()
    code, out = wsl(f"sha256sum {mongo_dir}/payload.bin")
    remote = out.split()[0] if code == 0 and out else ""
    step("restored bytes are the admitted bytes", code == 0 and remote == local, f"exit={code}\nrestored={remote}\nloader={local}")

    wsl(f"cp {mongo_dir}/payload.bin {WSL_ROOT}/.cache/restored-payload.bin")
    code, out = windows(
        [sys.executable, "-c", (
            "import json;from pathlib import Path;"
            "from impl.packages import canonical as cn;"
            "from impl.packages.identity import format_identity;"
            "m=json.loads(Path('.cache/realpkg/manifest.json').read_text());"
            "p=Path('.cache/restored-payload.bin').read_bytes();"
            "print(format_identity(m['name'],m['revision'],cn.package_digest(m,p)))"
        )],
        ROOT,
    )
    step(
        "restored payload re-derives the loader identity",
        code == 0 and out.strip() == identity,
        f"exit={code}\nrestored={out.strip()}\nloader={identity}",
    )

    mongo_prior = dir_digest(mongo_dir)
    code, out = wsl(
        f"{VENV} {WSL_ROOT}/tools/mongo_tamper.py --uri-file /run/drill-mongo.uri "
        f"--identity '{identity}' --database secure_shell"
    )
    step("tamper the stored record", code == 0, f"exit={code}\n{out}")
    code, out = wsl(
        f"cd {WSL_ROOT}; {VENV} -m impl.packages.mongo_store restore --uri-file /run/drill-mongo.uri "
        f"--identity '{identity}' --database secure_shell --out {mongo_dir}/tampered.bin"
    )
    refused = json_line(out)
    step(
        "mongo refuses a tampered record",
        code != 0 and refused.get("refusal") == "mongo-digest" and dir_digest(mongo_dir) == mongo_prior,
        f"exit={code} refusal={refused.get('refusal')} prior_unchanged={dir_digest(mongo_dir) == mongo_prior}",
    )

    prior = dir_digest()
    for name, flag, expected in (
        ("a digest-corrupt stream", "--corrupt 0", "stream-corrupt"),
        ("a reordered stream", "--swap 0 1", "chunk-out-of-order"),
    ):
        code, out = wsl(
            f"cd {WSL_ROOT}; {VENV} -m impl.packages.stream receive --manifest .cache/realpkg/manifest.json "
            f"--payload .cache/realpkg/payload.bin --chunk-size {CHUNK} --prior '' {flag}"
        )
        body = json_line(out)
        step(
            f"refuses {name}",
            code != 0 and body.get("refusal") == expected and body.get("prior_unchanged") is True and dir_digest() == prior,
            f"exit={code} refusal={body.get('refusal')} prior_unchanged={body.get('prior_unchanged')}",
        )

    code, out = wsl(
        f"cd {WSL_ROOT}; {VENV} -m impl.packages.stream frame --manifest .cache/realpkg/manifest.json "
        f"--payload .cache/realpkg/payload.bin --chunk-size {CHUNK}"
    )
    chunks = json_line(out).get("chunk_count", 0) if code == 0 else 0
    code, out = wsl(
        f"cd {WSL_ROOT}; {VENV} -m impl.packages.stream receive --manifest .cache/realpkg/manifest.json "
        f"--payload .cache/realpkg/payload.bin --chunk-size {CHUNK} --prior '' --drop {max(chunks - 1, 0)}"
    )
    body = json_line(out)
    step(
        "refuses a truncated stream",
        code != 0 and body.get("refusal") == "stream-truncated" and body.get("prior_unchanged") is True and dir_digest() == prior,
        f"exit={code} chunks={chunks} refusal={body.get('refusal')} prior_unchanged={body.get('prior_unchanged')}",
    )

    index_before = wsl(f"sha256sum {STORE}/index.tsv")[1]
    wsl(f"{VENV} -c \"import pathlib;p=pathlib.Path('{STORE}/packages/dashboard-1.0.0.dle');b=bytearray(p.read_bytes());b[len(b)//2]^=0xFF;p.write_bytes(b)\"")
    code, out = wsl(f"node {STORE_CLI} verify --store {STORE}")
    index_after = wsl(f"sha256sum {STORE}/index.tsv")[1]
    step(
        "store refuses a tampered package",
        code != 0 and "store-digest" in out and index_after == index_before,
        f"exit={code} index_unchanged={index_after == index_before}\n{out}",
    )

    failed = [name for name, status in results if status != 0]
    print(f"\n{len(results)} steps, {len(failed)} failed", file=sys.stderr)
    if failed:
        print("failed: " + ", ".join(failed), file=sys.stderr)
    return 1 if failed else 0


if __name__ == "__main__":
    try:
        code = main()
    finally:
        STREAM.close()
    sys.exit(code)
