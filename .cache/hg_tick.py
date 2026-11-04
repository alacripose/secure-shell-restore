import json
import pathlib
import re
import subprocess
import sys
import tempfile

ARCH = "docs/SECURE-SHELL-RESTORE@1.ARCHITECTURE.md"
WS = "docs/SECURE-SHELL-RESTORE@1.HYPERGRILL.md"
AG = "AGENTS.md"
LED = "C:/Users/ala/Documents/secure-shell/docs/LEDGER.md"


def line_of(path, needle):
    """Find a phrase even when the document wraps it across lines."""
    text = pathlib.Path(path).read_text(encoding="utf-8", errors="replace")
    pattern = re.compile(r"\s+".join(re.escape(part) for part in needle.split()))
    match = pattern.search(text)
    if not match:
        raise SystemExit(f"anchor not found in {path}: {needle!r}")
    return text[: match.start()].count("\n") + 1


def ev(path, needle, note):
    return {"kind": "doc", "ref": f"{path}:{line_of(path, needle)}", "note": note}


R = [
    ("Q081", "spec",
     "The signature is detached, never embedded. The signed statement binds name, revision and hash, and the hash covers the canonical package bytes; an embedded signature would sit inside the bytes it covers.",
     "Package layout carries the envelope beside the package. Stored packages keep both files.", [
         ev(ARCH, "signature binds name, revision and hash", "the signed statement's contents"),
         ev(ARCH, "The hash covers the package alone", "the hash's scope, which embedding makes circular")]),

    ("Q090", "spec",
     "Beside the manifest, not inside it. Same circularity as Q081: the manifest is what the hash covers, so a signature stored inside it would cover itself.",
     "Store rows reference a detached envelope path; the manifest schema gains no signature field.", [
         ev(ARCH, "The hash covers the package alone", "the manifest is inside the hash"),
         ev(ARCH, "signature binds name, revision and hash", "what the envelope binds")]),

    ("Q083", "spec",
     "The envelope covers the canonical manifest only. The payload root is a field of that manifest, so the payload is covered transitively and a payload substitution changes the verified bytes.",
     "Envelope scope is the manifest; no second signature over the payload is required.", [
         ev(ARCH, "referenced by its own hash rather than hashed in line", "the payload root lives in the manifest"),
         ev(ARCH, "fixed domain-separation tag", "the manifest is the preimage's core")]),

    ("Q077", "spec",
     "A per-file hash is BLAKE3 over the file bytes exactly. The path is the leaf's label in the Merkle tree, not part of the hashed content, so renaming a file changes the tree without pretending the bytes changed.",
     "Per-file hashes verify a file in isolation; the tree binds path to digest.", [
         ev(ARCH, "Merkle tree over files with per-file hashes", "tree over files, hashes recorded per file"),
         ev(ARCH, "full 32 bytes", "digest width per leaf")]),

    ("Q079", "spec",
     "The walk is ordered by path byte order, not manifest order, because canonical serialization already sorts keys by byte order and the tree must be reproducible by a second writer.",
     "Two writers with the same files produce the same root; manifest order is not a second source of truth.", [
         ev(ARCH, "sorts object keys by byte order", "the determinism rule the walk follows"),
         ev(ARCH, "Merkle tree over files", "what is being ordered")]),

    ("Q080", "spec",
     "The walk covers files only. Directories are implied by the paths in the tree and are not leaves, so an empty directory is not representable, consistent with a payload that carries content rather than filesystem metadata.",
     "Adding directory entries later would be a layout version change, not a silent addition.", [
         ev(ARCH, "Merkle tree over files", "files are the leaves"),
         ev(ARCH, "fixed domain-separation tag", "layout changes are versioned")]),

    ("Q078", "spec",
     "Empty files are legal leaves; an empty payload is legal and its root is the BLAKE3 of the empty input under the domain tag. A metadata-only package already establishes that a package may carry no content.",
     "Zero-length is a declared size, not a missing one; nothing refuses it.", [
         ev(WS, "| Q029 |", "metadata-only packages are legal"),
         ev(ARCH, "referenced by its own hash", "an empty payload still has a hash")]),

    ("Q084", "spec",
     "No timestamp is inside the signed bytes. The signature binds name, revision and hash; a signed timestamp would make a re-sign change identity and contradict a promoted prerelease keeping its hash.",
     "Time is recorded by the store and the ledger, never inside identity.", [
         ev(ARCH, "signature binds name, revision and hash", "the signed field set"),
         ev(WS, "| Q059 |", "identity is stable across promotion")]),

    ("Q085", "spec",
     "Multiple signatures are allowed and ordered. Rotation is per release and every stored package is re-signed at rotation, so a package can carry an outgoing and an incoming signature during a transition.",
     "Verification accepts any signature from a key trusted for that revision; the envelope is a set, not a slot.", [
         ev(WS, "| N003 |", "re-signing creates coexisting signatures"),
         ev(WS, "| Q055 |", "each signature binds the same statement")]),

    ("Q086", "spec",
     "The envelope carries a key identifier. The family's existing envelope already carries key-id, and per-release rotation makes discovery by trial unsafe.",
     "Verification selects a key by id, then checks trust for that release.", [
         ev(LED, "key-id,", "the existing envelope field"),
         ev(WS, "| N003 |", "rotation makes key selection necessary")]),

    ("Q082", "external",
     "Ed25519, carried in the family's dl-enclave.sig/1 envelope. It is the scheme the existing store and checkpoints already use, so Restore reuses one signature scheme rather than introducing a second.",
     "No new scheme is invented; search-before-inventing is satisfied by the family's own recorded envelope.", [
         ev(LED, "Ed25519 keys are generated", "the scheme in use"),
         ev(LED, "key-id,", "the envelope shape being reused")]),

    ("Q088", "spec",
     "A key that signed while valid keeps verifying its own signatures. The store has no expiry representation today, and when Restore adds key history the check is trust-at-signing plus current revocation, not current validity.",
     "Revocation stops new trust; it does not retroactively invalidate signed bytes.", [
         ev(LED, "Ed25519 keys are generated", "no key history, no expiry today"),
         ev(ARCH, "signature binds name, revision and hash", "the statement a past key covers")]),

    ("Q092", "spec",
     "The envelope schema is versioned separately from the package revision. The family already names the envelope dl-enclave.sig/1, which is its own version, and a package revision move does not renumber it.",
     "An envelope schema change is its own compatibility event, independent of package revisions.", [
         ev(LED, "key-id,", "the versioned envelope carries its own schema"),
         ev(ARCH, "signature binds name, revision and hash", "revision is bound inside, not the envelope's version")]),

    ("Q093", "spec",
     "A failed signature is a refusal, by name. The workspace rule is refuse-never-default, and the shell's security boundary refuses a package that cannot prove identity rather than mounting it with a warning.",
     "No degraded path exists for signatures; degraded belongs to grade, not to proof.", [
         ev(AG, "## 3. Refuse by name", "the workspace refusal rule"),
         ev(ARCH, "signature binds name, revision and hash", "what is being verified")]),

    ("N054", "spec",
     "The binary wire form is a projection of canonical JSON, not a second canonicalization. Canonical bytes are defined once, in JSON, and the wire encoding must round-trip to those bytes or be refused.",
     "One canonical definition; a wire encoder that cannot reproduce it is a bug, not a dialect.", [
         ev(ARCH, "sorts object keys by byte order", "the single canonical rule set"),
         ev(ARCH, "fixed domain-separation tag", "the hashed bytes are the canonical ones")]),
]


def main():
    closed, refused = [], []
    for qid, klass, resolution, effect, evidence in R:
        receipt = {"question": qid, "class": klass, "evidence": evidence,
                   "resolution": resolution, "effect": effect}
        with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False, encoding="utf-8") as fh:
            json.dump(receipt, fh)
            tmp = fh.name
        proc = subprocess.run([sys.executable, "tools/hypergrill_resolver.py", "resolve", tmp],
                              capture_output=True, text=True)
        text = (proc.stdout or proc.stderr).strip()
        print(f"{qid:5} exit={proc.returncode} {text.splitlines()[0] if text else '<no output>'}")
        (closed if proc.returncode == 0 else refused).append(qid)
    print(f"\nclosed={len(closed)} refused={len(refused)} refused_ids={refused}")
    return 0 if not refused else 3


if __name__ == "__main__":
    sys.exit(main())
