"""Exit tests for the host's voice component and the two voices the owner named.

Run: python tests/packages/run_cases_voice.py — prints one line per case and a final count,
exit 1 if any case fails. Nothing here reaches the network: the transport is injected.

What is asserted, and why each one is a contract rather than a convenience:

* the table names both voices by id, and the channel map is wish -> wukong, response -> pigsy;
* a kind outside the map is refused as unsayable instead of being spoken in a guessed voice;
* a missing key is a recorded `speech_unavailable`, not an exception and not silence;
* a produced line has an artifact whose BLAKE3 is the receipt's digest;
* every line, produced or not, yields exactly one ledger row naming the engine and values read.
"""

from __future__ import annotations

import json
import sys
import tempfile
import traceback
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from impl.packages import voice as vc  # noqa: E402

CASES: list = []


def case(function):
    CASES.append(function)
    return function


AUDIO = b"ID3\x04\x00\x00\x00\x00\x00\x00fake-mp3-bytes"


def fake_transport(request):
    return AUDIO


@case
def table_names_both_voices():
    table = vc.load_table()
    assert set(table["voices"]) == {"wukong", "pigsy"}, table["voices"].keys()
    assert table["voices"]["wukong"]["reference_id"] == "96664a5214884cbabe8e3a3ba7b1f9c6"
    assert table["voices"]["pigsy"]["reference_id"] == "684bdfc2180f4b4e8f837ca25109e256"


@case
def channels_are_wishes_wukong_and_responses_pigsy():
    table = vc.load_table()
    assert table["lines"] == {"wish": "wukong", "response": "pigsy"}, table["lines"]


@case
def plan_names_engine_and_voice():
    plan = vc.Voice(transport=fake_transport).plan("wish")
    assert plan["voice"] == "wukong" and plan["engine"] == "fish-audio", plan
    assert plan["model"] == "s2.1-pro-free" and plan["reference_id"].startswith("96664a52"), plan


@case
def unnamed_kind_is_refused():
    try:
        vc.Voice(transport=fake_transport).plan("weather")
    except vc.Refused as refusal:
        assert refusal.refusal == "voice-kind-unnamed", refusal.refusal
        return
    raise AssertionError("an unnamed kind was spoken")


@case
def empty_line_is_refused():
    try:
        vc.Voice(transport=fake_transport).say("response", "   ")
    except vc.Refused as refusal:
        assert refusal.refusal == "voice-line-empty", refusal.refusal
        return
    raise AssertionError("an empty line was spoken")


@case
def over_long_line_is_refused():
    try:
        vc.Voice(transport=fake_transport).say("wish", "x" * 301)
    except vc.Refused as refusal:
        assert refusal.refusal == "voice-line-too-long", refusal.refusal
        return
    raise AssertionError("a line over the table limit was spoken")


@case
def missing_key_is_a_recorded_unavailable():
    def no_key(request):
        raise vc.Refused("voice-transport-failed", "FISH_AUDIO_API_KEY", "no key")

    with tempfile.TemporaryDirectory() as folder:
        voice = vc.Voice(transport=no_key, state_dir=Path(folder))
        receipt = voice.say("response", "the store is mounted")
        assert receipt["state"] == "unavailable", receipt
        assert receipt["refusal"] == "speech-unavailable" and not receipt["produced"], receipt
        row = voice.ledger_row(receipt)
        assert row["row"] == "voice-line" and row["produced"] is False, row
        assert not list(Path(folder).glob("*")), "an unavailable line wrote an artifact"


@case
def produced_line_has_an_artifact_matching_its_digest():
    from blake3 import blake3

    with tempfile.TemporaryDirectory() as folder:
        voice = vc.Voice(transport=fake_transport, state_dir=Path(folder))
        receipt = voice.say("wish", "I want the contour to reach every visitor")
        assert receipt["state"] == "produced" and receipt["produced"], receipt
        artifact = Path(receipt["artifact"])
        assert artifact.exists(), artifact
        assert receipt["digest"] == "blake3:" + blake3(AUDIO).hexdigest(), receipt["digest"]
        assert artifact.read_bytes() == AUDIO


@case
def one_ledger_row_per_line():
    with tempfile.TemporaryDirectory() as folder:
        voice = vc.Voice(transport=fake_transport, state_dir=Path(folder))
        rows = [voice.ledger_row(voice.say(kind, f"line {kind}")) for kind in ("wish", "response")]
        assert len(rows) == 2, rows
        assert [row["voice"] for row in rows] == ["wukong", "pigsy"], rows
        assert all(row["engine"] == "fish-audio" and row["chars"] for row in rows), rows


@case
def a_bad_table_is_refused_not_defaulted():
    with tempfile.TemporaryDirectory() as folder:
        path = Path(folder) / "voices.json"
        path.write_text(json.dumps({"voices": {}}), encoding="utf-8")
        try:
            vc.load_table(path)
        except vc.Refused as refusal:
            assert refusal.refusal == "voice-table-unreadable", refusal.refusal
            return
    raise AssertionError("a table without engine/lines/limits was accepted")


@case
def the_manifest_validates_under_the_package_vocabulary():
    from impl.packages import canonical

    manifest = json.loads((ROOT / "packages" / "voice" / "voice.meta.json").read_text(encoding="utf-8"))
    payload = (ROOT / "packages" / "voice" / "voices.json").read_bytes()
    held = canonical.validate_manifest(manifest)
    assert held["name"] == "host-voice" and held["revision"] == 1, held
    digest = canonical.package_digest(manifest, payload)
    assert digest.startswith("blake3:") and len(digest) == 71, digest


def main() -> int:
    failures = 0
    for function in CASES:
        try:
            function()
            print(f"ok   {function.__name__}")
        except Exception:  # noqa: BLE001 — a case failure is printed, never swallowed
            failures += 1
            print(f"FAIL {function.__name__}")
            traceback.print_exc()
    print(f"{len(CASES)} cases, {failures} failed")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
