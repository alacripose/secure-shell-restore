"""Secure Shell Restore — the host's voice, and the two voices the owner named.

The round `ROUND@2026-11-21-voice-and-primary-driver` answered this shape, and these lines come
from it rather than from taste:

* **Q-S1 / Q-S10** — the host's package carries the line; neither the axis nor the driver
  composes it. A line is a reading of served fields, and a state the package cannot name is
  *unsayable*: it is refused by name, never described in guessed prose.
* **Q-S5** — the waveform is an artifact with a digest and a receipt, because the host has no
  playback device and a package can be read anywhere.
* **Q-S6** — the voice is a packaged component with its own revision, invoked by pinned name.
  The host's ad hoc `apt-get install espeak-ng` is not the voice.
* **Q-S7** — every spoken line is one ledger row, naming the engine, the values read and
  whether sound was produced.

The voices are the two the owner asked for: **Wukong** for wishes and **Pigsy** for responses.
They are hosted models with stable ids pinned in `packages/voice/voices.json`
(`https://fish.audio/m/96664a5214884cbabe8e3a3ba7b1f9c6` and
`https://fish.audio/m/684bdfc2180f4b4e8f837ca25109e256`); the host names them and never clones
them. The channel assignment lives in that file's `lines`, so changing which voice speaks which
kind is one record revision, not a code change.

Nothing here reaches the network in a test: the transport is injected.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any, Callable

from blake3 import blake3

ROOT = Path(__file__).resolve().parents[2]
TABLE = ROOT / "packages" / "voice" / "voices.json"
SCHEMA = "secure-shell.voice/1"

REFUSALS = (
    "voice-artifact-unwritable",
    "voice-audio-malformed",
    "voice-kind-unnamed",
    "voice-line-empty",
    "voice-line-too-long",
    "voice-table-unreadable",
    "voice-transport-failed",
)

Transport = Callable[[dict[str, Any]], bytes]


class Refused(Exception):
    """A named refusal: the shape every sibling package module in this repository uses."""

    def __init__(self, refusal: str, subject: str, reason: str) -> None:
        assert refusal in REFUSALS, refusal
        super().__init__(reason)
        self.refusal = refusal
        self.subject = subject
        self.reason = reason

    def as_dict(self) -> dict[str, Any]:
        return {
            "schema": SCHEMA,
            "state": "refused",
            "refusal": self.refusal,
            "subject": self.subject,
            "reason": self.reason,
        }


def _subject(value: Any, limit: int = 96) -> str:
    text = value if isinstance(value, str) else repr(value)
    return text if len(text) <= limit else text[:limit] + "…"


def load_table(path: Path = TABLE) -> dict[str, Any]:
    """Read the pinned voice table, or refuse by name. A missing table is not a default voice."""
    try:
        table = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise Refused("voice-table-unreadable", str(path), str(error)) from error
    for field in ("engine", "voices", "lines", "limits"):
        if field not in table:
            raise Refused("voice-table-unreadable", str(path), f"table has no {field}")
    return table


def http_transport(table: dict[str, Any], key: str | None = None) -> Transport:
    """The one network call, built from the table so no host name is hard-coded twice."""
    engine = table["engine"]
    secret = key if key is not None else os.environ.get(engine["key_env"], "")

    def send(request: dict[str, Any]) -> bytes:
        if not secret:
            raise Refused(
                "voice-transport-failed",
                engine["key_env"],
                "no key in the environment: the line is recorded as speech_unavailable",
            )
        body = json.dumps(
            {"text": request["text"], "reference_id": request["reference_id"], "format": engine["audio"]}
        ).encode("utf-8")
        call = urllib.request.Request(
            engine["endpoint"],
            data=body,
            method=engine["method"],
            headers={
                "Authorization": f"Bearer {secret}",
                "Content-Type": "application/json",
                "model": engine["model"],
            },
        )
        try:
            with urllib.request.urlopen(call, timeout=30) as response:
                audio = response.read()
        except urllib.error.URLError as error:
            raise Refused("voice-transport-failed", engine["endpoint"], str(error)) from error
        if not audio:
            raise Refused("voice-audio-malformed", engine["endpoint"], "the engine returned no audio")
        return audio

    return send


class Voice:
    """The host's voice: one line per breath, one ledger row per line, one artifact per sound."""

    def __init__(
        self,
        table: dict[str, Any] | None = None,
        transport: Transport | None = None,
        state_dir: Path | None = None,
    ) -> None:
        self.table = table if table is not None else load_table()
        self.transport = transport if transport is not None else http_transport(self.table)
        self.state_dir = state_dir if state_dir is not None else ROOT / "var" / "voice"

    # -- the plan: what would speak, and why ------------------------------------------------
    def plan(self, kind: Any) -> dict[str, Any]:
        lines = self.table.get("lines", {})
        if not isinstance(kind, str) or kind not in lines:
            raise Refused(
                "voice-kind-unnamed",
                _subject(kind),
                f"a line kind must be one of {', '.join(sorted(lines))}; an unnamed state is unsayable",
            )
        name = lines[kind]
        voice = self.table["voices"].get(name)
        if not isinstance(voice, dict) or "reference_id" not in voice:
            raise Refused("voice-kind-unnamed", name, "the channel names a voice the table does not hold")
        engine = self.table["engine"]
        return {
            "schema": SCHEMA,
            "state": "held",
            "kind": kind,
            "voice": name,
            "label": voice.get("label", name),
            "reference_id": voice["reference_id"],
            "engine": engine["name"],
            "model": engine["model"],
            "audio": engine["audio"],
        }

    # -- the line: refused, produced, or unavailable ----------------------------------------
    def say(self, kind: Any, text: Any) -> dict[str, Any]:
        plan = self.plan(kind)
        if not isinstance(text, str) or not text.strip():
            raise Refused("voice-line-empty", plan["kind"], "a line must be non-empty text")
        line = " ".join(text.split())
        limit = int(self.table["limits"]["line_chars"])
        if len(line) > limit:
            raise Refused(
                "voice-line-too-long",
                plan["kind"],
                f"a line is at most {limit} characters; this one is {len(line)}",
            )
        try:
            audio = self.transport({**plan, "text": line})
        except Refused as refusal:
            # Q-S7: a line that could not be spoken is a visible row, not a silent skip.
            if refusal.refusal != "voice-transport-failed":
                raise
            return {
                **plan,
                "state": "unavailable",
                "refusal": "speech-unavailable",
                "reason": refusal.reason,
                "chars": len(line),
                "produced": False,
            }
        if not audio:
            raise Refused("voice-audio-malformed", plan["engine"], "the transport returned no bytes")
        digest = "blake3:" + blake3(audio).hexdigest()
        try:
            self.state_dir.mkdir(parents=True, exist_ok=True)
            artifact = self.state_dir / f"{digest.split(':', 1)[1]}.{plan['audio']}"
            artifact.write_bytes(audio)
        except OSError as error:
            raise Refused("voice-artifact-unwritable", str(self.state_dir), str(error)) from error
        return {
            **plan,
            "state": "produced",
            "chars": len(line),
            "bytes": len(audio),
            "digest": digest,
            "artifact": str(artifact),
            "produced": True,
        }

    # -- the ledger: one row per line -------------------------------------------------------
    @staticmethod
    def ledger_row(receipt: dict[str, Any]) -> dict[str, Any]:
        """Q-S7's row: the engine, the values read, and whether sound was produced."""
        return {
            "schema": SCHEMA,
            "row": "voice-line",
            "state": receipt["state"],
            "kind": receipt["kind"],
            "voice": receipt["voice"],
            "engine": receipt["engine"],
            "model": receipt["model"],
            "reference_id": receipt["reference_id"],
            "chars": receipt.get("chars", 0),
            "produced": bool(receipt.get("produced")),
            "digest": receipt.get("digest", ""),
            "refusal": receipt.get("refusal", ""),
        }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="secure-shell voice", description=__doc__.splitlines()[0])
    commands = parser.add_subparsers(dest="command", required=True)

    table_command = commands.add_parser("table", help="the pinned voices and their channels")
    table_command.add_argument("--path", default=str(TABLE))

    plan_command = commands.add_parser("plan", help="what would speak for a line kind")
    plan_command.add_argument("kind")

    say_command = commands.add_parser("say", help="speak one line and print its receipt")
    say_command.add_argument("kind")
    say_command.add_argument("text")
    say_command.add_argument("--state", default=str(ROOT / "var" / "voice"))

    commands.add_parser("refusals", help="the enumerated refusal names")

    arguments = parser.parse_args(argv)
    try:
        if arguments.command == "table":
            result: dict[str, Any] = load_table(Path(arguments.path))
        elif arguments.command == "plan":
            result = Voice().plan(arguments.kind)
        elif arguments.command == "say":
            voice = Voice(state_dir=Path(arguments.state))
            receipt = voice.say(arguments.kind, arguments.text)
            result = {**receipt, "ledger": voice.ledger_row(receipt)}
        else:
            result = {"schema": SCHEMA, "state": "held", "refusals": list(REFUSALS)}
    except Refused as refusal:
        print(json.dumps(refusal.as_dict(), sort_keys=True))
        return 1
    print(json.dumps(result, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
