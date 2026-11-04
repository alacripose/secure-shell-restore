"""Configure the Debian host's mongod, create its users, and seal the app URI with systemd-creds.

Run once, as root, on the host. It is idempotent: an existing user is not recreated, and the
credential file is rewritten only when it is absent.

Why the credential is sealed rather than exported: the restore reads the URI from a file that
`systemd-creds decrypt` writes at run time, so the connection string is encrypted at rest under the
host key and never sits in an environment variable, a unit file or a log line.
"""

from __future__ import annotations

import json
import secrets
import subprocess
import sys
import time
import urllib.parse
from pathlib import Path

from pymongo import MongoClient
from pymongo.errors import PyMongoError

CONF = """# Written by tools/mongo_setup.py on the Debian host.
# authorization: enabled, because the restore connects as the `secure_shell` user and never as an
# unauthenticated local client. bindIp stays loopback, because the axis token is the only remote
# capability this slice issues. The credential it creates is sealed with systemd-creds under the
# host key and decrypted only for the length of a restore.
storage:
  dbPath: /var/lib/mongodb
systemLog:
  destination: file
  path: /var/log/mongodb/mongod.log
  logAppend: true
net:
  port: 27017
  bindIp: 127.0.0.1
security:
  authorization: enabled
processManagement:
  timeZoneInfo: /usr/share/zoneinfo
"""

CRED_DIR = Path("/etc/secure-shell")
APP_CRED = CRED_DIR / "mongo-uri.cred"
ADMIN_CRED = CRED_DIR / "mongo-admin-uri.cred"
PLAIN = Path("/run/mongo-uri.plain")
ADMIN_PLAIN = Path("/run/mongo-admin-uri.plain")


def run(command: list[str]) -> subprocess.CompletedProcess:
    return subprocess.run(command, capture_output=True, text=True)


def wait_for_port(seconds: int = 30) -> bool:
    deadline = time.time() + seconds
    while time.time() < deadline:
        try:
            MongoClient("mongodb://127.0.0.1:27017/?directConnection=true", serverSelectionTimeoutMS=1000).admin.command("ping")
            return True
        except PyMongoError:
            time.sleep(1)
    return False


def main() -> int:
    Path("/etc/mongod.conf").write_text(CONF, encoding="utf-8")
    for directory in ("/var/lib/mongodb", "/var/log/mongodb"):
        Path(directory).mkdir(parents=True, exist_ok=True)
    subprocess.run(["chown", "-R", "mongodb:mongodb", "/var/lib/mongodb", "/var/log/mongodb"], check=True)
    run(["systemctl", "enable", "mongod"])
    run(["systemctl", "restart", "mongod"])
    if not wait_for_port():
        print("refused: mongo-absent: mongod did not answer on 127.0.0.1:27017", file=sys.stderr)
        return 1

    # A first run has no users, and the localhost exception lets exactly one be created. A rerun
    # has to authenticate first: the exception is gone, so a blind retry of createUser ends in
    # `Command createUser requires authentication` rather than in an idempotent no-op.
    if ADMIN_CRED.exists():
        subprocess.run(["systemd-creds", "decrypt", "--name=mongo-admin-uri", str(ADMIN_CRED), str(ADMIN_PLAIN)], check=True)
        admin_uri = ADMIN_PLAIN.read_text(encoding="utf-8").strip()
        ADMIN_PLAIN.unlink()
    else:
        admin_pw = secrets.token_urlsafe(24)
        local = MongoClient("mongodb://127.0.0.1:27017/?directConnection=true", serverSelectionTimeoutMS=3000)
        local.admin.command("createUser", "root_admin", pwd=admin_pw,
                            roles=[{"role": "userAdminAnyDatabase", "db": "admin"}])
        admin_uri = "mongodb://root_admin:%s@127.0.0.1:27017/?authSource=admin" % urllib.parse.quote(admin_pw, safe="")

    admin = MongoClient(admin_uri, serverSelectionTimeoutMS=3000)
    app_pw = None
    try:
        app_pw = secrets.token_urlsafe(24)
        admin["secure_shell"].command("createUser", "secure_shell", pwd=app_pw,
                                      roles=[{"role": "readWrite", "db": "secure_shell"}])
    except PyMongoError as error:
        if "already exists" not in str(error):
            raise
        app_pw = None

    if app_pw is None:
        if not APP_CRED.exists():
            print("refused: mongo-unauthorized: the app user exists but its sealed URI is gone", file=sys.stderr)
            return 1
        subprocess.run(["systemd-creds", "decrypt", "--name=mongo-uri", str(APP_CRED), str(PLAIN)], check=True)
        app_uri = PLAIN.read_text(encoding="utf-8").strip()
    else:
        app_uri = "mongodb://secure_shell:%s@127.0.0.1:27017/secure_shell?authSource=secure_shell" % urllib.parse.quote(app_pw, safe="")

    app = MongoClient(app_uri, serverSelectionTimeoutMS=3000)
    app.admin.command("ping")
    app["secure_shell"]["packages"].create_index("digest")

    CRED_DIR.mkdir(parents=True, exist_ok=True)
    PLAIN.write_text(app_uri, encoding="utf-8")
    ADMIN_PLAIN.write_text(admin_uri, encoding="utf-8")
    for plain, cred, name in ((PLAIN, APP_CRED, "mongo-uri"), (ADMIN_PLAIN, ADMIN_CRED, "mongo-admin-uri")):
        subprocess.run(["systemd-creds", "encrypt", "--with-key=host", f"--name={name}", str(plain), str(cred)], check=True)
        plain.unlink()
    APP_CRED.chmod(0o600)
    ADMIN_CRED.chmod(0o600)

    print(json.dumps({
        "mongo": "running",
        "auth": "enabled",
        "app_user": "secure_shell",
        "database": "secure_shell",
        "credential": str(APP_CRED),
        "sealed": APP_CRED.stat().st_size,
    }, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
