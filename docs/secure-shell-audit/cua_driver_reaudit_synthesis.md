# secure shell v2 — CUA driver re-audit inventory
Started 2026-11-04T23:27:35Z. Per-root budget 5s, drive budget 12s, total 195s. Each root is flushed as it completes; `truncated: yes` is a refusal, not a pass.

## `C:\Users\ala\Documents\secure_shell_v2`
- files: 67 · seconds: 0.3 · **truncated: no** · xml: 0
- repo `C:\Users\ala\Documents\secure_shell_v2` docs=['AGENTS.md'] workflows=['hypergrill-audit.yml']
- driver references: 45 · `policy`×45, `ledger`×36, `health`×29, `civilians`×25, `cadence`×16, `witness`×15, `format`×14, `mount`×13, `client`×3
- identifiers: `surface.mount/2`×17, `secure-shell.stream/1`×13, `secure-shell.handoff/1`×12, `secure-shell.package/1`×12, `secure-shell.axis/1`×5, `dl-enclave.surface/1`×5, `secure-shell.served/1`×4, `receipt/2`×3, `shploingus.receipt/0`×3, `secure-shell.ingest/1`×3, `secure-shell.stream/0`×3, `secure-shell.agent-api/1`×2, `dl-enclave.sig/1`×2, `secure-shell.round/1`×2, `civilian.axis-cells/1`×2, `shploingus.cellframe/1`×2, `shploingus.cells/1`×2, `shploingus.recipe/3`×2, `openlock.addons/2`×2, `planet-shell.ledger/1`×2, `shploingus.layer/1`×2, `compendium/1`×2, `save/1`×2, `mesh/2`×2, `secure-shell.chunk/1`×2
- hash-named ids: `dl-enclave.surface/0123456789abcdef`, `nih.gov/13680401`, `nih.gov/17103081`, `nih.gov/42096013`, `shploingus.recipe/9f3c2a1b`, `nih.gov/30339280`, `nih.gov/17368962`, `nih.gov/31070740`, `github.com/1872183316`
- magics: `V4PKG001`×1, `SHPKG002`×1, `SHPKG003`×1, `V4PKG002`×1, `SHPKG009`×1
- store sites:
  - `C:\Users\ala\Documents\secure_shell_v2\docs\SECURE-SHELL-RESTORE@1.ARCHITECTURE.md`
  - `C:\Users\ala\Documents\secure_shell_v2\docs\SECURE-SHELL-RESTORE@1.FORMAT-IMPORT-AUDIT.md`
  - `C:\Users\ala\Documents\secure_shell_v2\docs\SECURE-SHELL-RESTORE@1.HYPERGRILL.md`
  - `C:\Users\ala\Documents\secure_shell_v2\docs\SECURE-SHELL-RESTORE@1.IMPLEMENTATION-PLAN.md`
  - `C:\Users\ala\Documents\secure_shell_v2\docs\SECURE-SHELL-V2-ARCHITECTURE.md`
  - `C:\Users\ala\Documents\secure_shell_v2\docs\SECURE-SHELL-V2-FORMAT-IMPORT-AUDIT.md`
  - `C:\Users\ala\Documents\secure_shell_v2\docs\SECURE-SHELL-V2-IMPLEMENTATION-PLAN.md`
  - `C:\Users\ala\Documents\secure_shell_v2\docs\hypergrill\scan_state@2026-11-04.json`
  - `C:\Users\ala\Documents\secure_shell_v2\docs\hypergrill\state.json`
  - `C:\Users\ala\Documents\secure_shell_v2\impl\packages\canonical.py`
  - `C:\Users\ala\Documents\secure_shell_v2\impl\packages\mongo_store.py :: :         from pymongo import MongoClient         from pymongo.errors import PyMongoError     except ImportError:         raise Refused("mon`
  - `C:\Users\ala\Documents\secure_shell_v2\tests\packages\run_cases_canonical.py`
  - `C:\Users\ala\Documents\secure_shell_v2\tickets\TICKET-0009-stream-and-real-sources.md`
  - `C:\Users\ala\Documents\secure_shell_v2\tools\mongo_setup.py :: ort Path  from pymongo import MongoClient from pymongo.errors import PyMongoError  CONF = """# Written by tools/mongo_setup.py on the Debian`
  - `C:\Users\ala\Documents\secure_shell_v2\tools\mongo_tamper.py :: ort Path  from pymongo import MongoClient   def main() -> int:     parser = argparse.ArgumentParser()     parser.add_argument("--uri-file",`
  - `C:\Users\ala\Documents\secure_shell_v2\tools\scan_drives_reaudit.py :: re.I) MONGO_RE = re.compile(r'mongodb://|MongoClient|getDatabase\(|getCollection\(') LEDGER_RE = re.compile(r"ledger\.jsonl|surface\.mount|p`
- axis/civ sites: `C:\Users\ala\Documents\secure_shell_v2\docs\hypergrill\scan_state@2026-11-04.json`, `C:\Users\ala\Documents\secure_shell_v2\tools\scan_drives_reaudit.py`
- qt sites: `C:\Users\ala\Documents\secure_shell_v2\tools\scan_drives_reaudit.py`

## `C:\Users\ala\Documents\testport1`
- files: 867 · seconds: 5.0 · **truncated: yes** · xml: 0
- repo `C:\Users\ala\Documents\testport1` docs=['AGENTS.md'] workflows=['port-gate.yml']
- driver references: 153 · `policy`×132, `ledger`×55, `format`×35, `cadence`×34, `witness`×29, `civilians`×16, `mount`×10, `health`×8, `client`×4
- identifiers: `shploingus.cellframe/1`×31, `shploingus.cells/1`×23, `surface.mount/2`×17, `shploingus.recipe/3`×12, `dl-enclave.surface/1`×11, `secure-shell.ingest/1`×7, `civilian.axis-cells/1`×6, `dl-enclave.surface/0`×6, `openlock.addons/2`×6, `cell/4`×5, `ensouled.action/1`×5, `ensouled.frame/1`×5, `minecraft.cua-action/1`×5, `recipe/3`×5, `secure-shell.admission/1`×5, `system1-agent/1`×5, `civilian.decision/1`×4, `civilian.ticket/1`×4, `secure-shell.ledger/1`×4, `secure-shell.served/2`×4, `ensouled.autopopulation/1`×3, `mount/2`×3, `planet-shell.ledger/1`×3, `secure-shell.served/1`×3, `shploingus.cellframe/0`×3
- hash-named ids: `dl-enclave.surface/0123456789abcdef`, `nih.gov/13680401`, `nih.gov/17103081`, `nih.gov/42096013`
- magics: `V4PKG001`×4, `SHPKG002`×1, `SHPKG003`×1
- store sites:
  - `C:\Users\ala\Documents\testport1\AGENTS.md`
  - `C:\Users\ala\Documents\testport1\config\legacy-formats.json`
  - `C:\Users\ala\Documents\testport1\config\plan-errata.json`
  - `C:\Users\ala\Documents\testport1\crates\planet-package\src\mount.rs`
  - `C:\Users\ala\Documents\testport1\crates\planet-shell-ledger\src\lib.rs`
  - `C:\Users\ala\Documents\testport1\docs\cellular_generativity_axis_civilian_expectations_prototype_rechecked.md`
  - `C:\Users\ala\Documents\testport1\docs\DECISIONS-PORT.md`
  - `C:\Users\ala\Documents\testport1\docs\PACKAGE-OWNERSHIP.md`
  - `C:\Users\ala\Documents\testport1\docs\PORT-BASELINE.md`
  - `C:\Users\ala\Documents\testport1\docs\SCOPE-ACCOUNTING.md`
  - `C:\Users\ala\Documents\testport1\docs\SWF_CELL_PACKAGE_IMPLEMENTATION_PLAN_v3.md`
  - `C:\Users\ala\Documents\testport1\docs\testport1_plan_resynthesis.md`
- axis/civ sites: `C:\Users\ala\Documents\testport1\config\legacy-formats.json`, `C:\Users\ala\Documents\testport1\docs\CELL-SCHEMA.md`, `C:\Users\ala\Documents\testport1\docs\cellular_generativity_axis_civilian_expectations.md`, `C:\Users\ala\Documents\testport1\docs\cellular_generativity_axis_civilian_expectations_prototype_rechecked.md`, `C:\Users\ala\Documents\testport1\docs\testport1_plan_resynthesis.md`
- note: budget reached at C:\Users\ala\Documents\testport1\generated\vendor-swf\quote

## `C:\Users\ala\Documents\shploingus-clean`
- files: 679 · seconds: 5.1 · **truncated: yes** · xml: 0
- repo `C:\Users\ala\Documents\shploingus-clean` docs=['VOWS.md'] workflows=**none**
- driver references: 370 · `policy`×305, `cadence`×154, `ledger`×152, `witness`×79, `client`×58, `civilians`×25, `format`×20, `health`×13
- identifiers: `shploingus.recipe/3`×7, `shploingus.receipt/2`×3, `shploingus.save/1`×2, `shploingus.mesh/2`×2, `shploingus.world-truth/1`×2, `axis-grant/1`×2, `shploingus.cellframe/1`×2, `shploingus.compendium/1`×1, `shploingus.event/1`×1, `shploingus.material-registry/1`×1, `shploingus.resident/2`×1, `shploingus.receipt/0`×1, `shploingus.receipt/1`×1, `shploingus.world-residency/1`×1, `shploingus.plan/1`×1, `shploingus.api-answer/1`×1, `shploingus.api-field-values/1`×1, `recipe/3`×1
- store sites:
  - `C:\Users\ala\Documents\shploingus-clean\README.new.md`
  - `C:\Users\ala\Documents\shploingus-clean\.freebuff\ledger-digest.md`
- axis/civ sites: `C:\Users\ala\Documents\shploingus-clean\crates\axis\civilians\src\lib.rs`, `C:\Users\ala\Documents\shploingus-clean\crates\axis\mcp\src\grant.rs`
- note: budget reached at C:\Users\ala\Documents\shploingus-clean\crates\voxel-client\src\shell

## `C:\Users\ala\Documents\shploingus-game`
- files: 3983 · seconds: 5.0 · **truncated: yes** · xml: 0
- repo `C:\Users\ala\Documents\shploingus-game` docs=**none** workflows=**none**
- driver references: 761 · `ledger`×667, `policy`×148, `cadence`×39, `format`×28, `client`×21, `health`×12, `civilians`×7, `witness`×2
- identifiers: `flow-specs/01`×1
- store sites:
  - `C:\Users\ala\Documents\shploingus-game\crates\diffusion-core\src\legacyledger\ledger.rs`
  - `C:\Users\ala\Documents\shploingus-game\docs\evidence\personal-evidence-engine-mongodb-build-spec.md :: e application can connect to `mongodb://localhost:27017`; MongoDB's Node.js driver documentation also covers Atlas, Enterprise, and Communit`
  - `C:\Users\ala\Documents\shploingus-game\docs\plan\07-correction.md`
  - `C:\Users\ala\Documents\shploingus-game\docs\plan\HANDOFF-ROUND-38.md`
  - `C:\Users\ala\Documents\shploingus-game\references\ala-system\personal-evidence-engine-mongodb-build-spec.md :: e application can connect to `mongodb://localhost:27017`; MongoDB's Node.js driver documentation also covers Atlas, Enterprise, and Communit`
- note: budget reached at C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\1f

## `C:\Users\ala\Documents\shploingus`
- files: 1704 · seconds: 5.0 · **truncated: yes** · xml: 0
- repo `C:\Users\ala\Documents\shploingus` docs=**none** workflows=**none**
- driver references: 320 · `policy`×275, `ledger`×262, `health`×6, `client`×2, `format`×2, `cadence`×1
- identifiers: `bg-white/80`×1, `bg-black/60`×1, `border-white/10`×1
- store sites:
  - `C:\Users\ala\Documents\shploingus\HANDOFF.md`
  - `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\evidence\mantis-dataset-inventory.json`
  - `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\evidence\mantis-stage-evidence\pipeline-adapter.md`
- note: budget reached at C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\security-remediation-pre-r5-provisional\public-candidate

## `C:\Users\ala\Documents\openlock`
- files: 1586 · seconds: 5.5 · **truncated: yes** · xml: 25
- repo `C:\Users\ala\Documents\openlock` docs=['AGENTS.md'] workflows=['pages.yml']
- driver references: 64 · `policy`×52, `ledger`×24, `witness`×19, `health`×17, `cadence`×9, `format`×4
- identifiers: `shploingus.recipe/3`×7, `openlock.build/1`×6, `shploingus.cells/1`×5, `openlock.envelope/1`×4, `openlock.addons/2`×3, `openlock.game/1`×1, `openlock.observer/1`×1, `shploingus.theme/1`×1
- magics: `SHPKG003`×1
- store sites:
  - `C:\Users\ala\Documents\openlock\.scratch\parity-after.json :: 38",   "store": {     "uri": "mongodb://127.0.0.1:27018",     "database": "openlock_axis"   },   "verification": {     "run": "9a23721976804`
  - `C:\Users\ala\Documents\openlock\.scratch\parity-before.json :: 9c",   "store": {     "uri": "mongodb://127.0.0.1:27018",     "database": "openlock_axis"   },   "verification": {     "run": "1239febc21b94`
  - `C:\Users\ala\Documents\openlock\.scratch\parity-csdk10-final.json :: 91",   "store": {     "uri": "mongodb://127.0.0.1:27018",     "database": "openlock_axis"   },   "verification": {     "run": "71f41a29b5e44`
  - `C:\Users\ala\Documents\openlock\.scratch\parity-csdk10-final2.json :: 6a",   "store": {     "uri": "mongodb://127.0.0.1:27018",     "database": "openlock_axis"   },   "verification": {     "run": "8f0dfc8c7fc94`
  - `C:\Users\ala\Documents\openlock\.scratch\parity-csdk10.json :: 99",   "store": {     "uri": "mongodb://127.0.0.1:27018",     "database": "openlock_axis"   },   "verification": {     "run": "45dee8f366384`
  - `C:\Users\ala\Documents\openlock\.scratch\parity-current.json :: l": "no MongoDB is reachable (mongodb://127.0.0.1:27017: No servers found yet, Timeout: 1.5s, Topology Description: <TopologyDescription id:`
  - `C:\Users\ala\Documents\openlock\.scratch\parity-ddrive.json :: l": "no MongoDB is reachable (mongodb://127.0.0.1:27017: No servers found yet, Timeout: 1.5s, Topology Description: <TopologyDescription id:`
  - `C:\Users\ala\Documents\openlock\.scratch\parity-final.json :: 2e",   "store": {     "uri": "mongodb://127.0.0.1:27018",     "database": "openlock_axis"   },   "verification": {     "run": "0830253c66454`
  - `C:\Users\ala\Documents\openlock\.scratch\parity-old.json :: 7f",   "store": {     "uri": "mongodb://127.0.0.1:27018",     "database": "openlock_axis"   },   "verification": {     "run": "00df83c1a2874`
  - `C:\Users\ala\Documents\openlock\.scratch\parity-steam-final.json :: d6",   "store": {     "uri": "mongodb://127.0.0.1:27018",     "database": "openlock_axis"   },   "verification": {     "run": "d0ac700c713a4`
  - `C:\Users\ala\Documents\openlock\.scratch\parity-steam-final2.json :: d7",   "store": {     "uri": "mongodb://127.0.0.1:27018",     "database": "openlock_axis"   },   "verification": {     "run": "34e28ff80b154`
  - `C:\Users\ala\Documents\openlock\.scratch\parity-steam.json :: 2b",   "store": {     "uri": "mongodb://127.0.0.1:27018",     "database": "openlock_axis"   },   "verification": {     "run": "102b992b9cf24`
  - `C:\Users\ala\Documents\openlock\.scratch\parity.json :: d5",   "store": {     "uri": "mongodb://127.0.0.1:27017",     "database": "openlock_axis"   },   "verification": {     "run": "31c2ea4eca8b4`
- note: budget reached at C:\Users\ala\Documents\openlock\.scratch\proof-build\panorama\styles

## `C:\Users\ala\Documents\secure-shell`
- files: 92 · seconds: 1.5 · **truncated: no** · xml: 1
- repo `C:\Users\ala\Documents\secure-shell` docs=['AGENTS.md'] workflows=**none**
- driver references: 71 · `policy`×66, `ledger`×58, `witness`×41, `civilians`×20, `mount`×13, `cadence`×13, `format`×7, `health`×6, `client`×3
- identifiers: `openlock.addons/2`×27, `surface.mount/2`×24, `dl-enclave.surface/1`×18, `secure-shell.served/1`×16, `secure-shell.ingest/1`×12, `shploingus.recipe/4`×11, `openlock.envelope/1`×10, `recipe/4`×8, `dl-enclave.sig/1`×7, `surface.patch/1`×6, `dl-enclave.shell/1`×5, `recipe/3`×5, `secure-shell.admission/1`×4, `shploingus.cells/1`×4, `secure-shell.served/2`×4, `secure-shell.axis/1`×4, `secure-shell.material-grade/1`×3, `openlock.build/1`×3, `secure-shell.ledger/1`×3, `openlock.game/1`×3, `secure-shell.port-baseline/1`×2, `specs/0`×2, `grant/1`×2, `envelope/1`×2, `game/1`×2
- store sites:
  - `C:\Users\ala\Documents\secure-shell\AGENTS.md`
  - `C:\Users\ala\Documents\secure-shell\docs\ARCHITECTURE.md`
  - `C:\Users\ala\Documents\secure-shell\docs\DECISIONS.md`
  - `C:\Users\ala\Documents\secure-shell\docs\FIRST-TEN-HOURS.md`
  - `C:\Users\ala\Documents\secure-shell\docs\FORMAT-SOURCES-AUDIT.md :: e is no `mongodb` import, no `mongodb://` URI and no driver anywhere: `rg` for `require('mongodb')`, `from "mongodb"` and `mongodb://` acros`
  - `C:\Users\ala\Documents\secure-shell\docs\LEDGER.md`
  - `C:\Users\ala\Documents\secure-shell\docs\PLAN.md`
  - `C:\Users\ala\Documents\secure-shell\docs\secure-shell-streamer-first-package-unification.md`
  - `C:\Users\ala\Documents\secure-shell\docs\SELECTIONS.md`
  - `C:\Users\ala\Documents\secure-shell\server\ledger.mjs`
  - `C:\Users\ala\Documents\secure-shell\server\shell.mjs`
  - `C:\Users\ala\Documents\secure-shell\server\test\ledger.test.mjs`
  - `C:\Users\ala\Documents\secure-shell\tests\drift_gate.test.mjs`
  - `C:\Users\ala\Documents\secure-shell\tools\drift_gate.mjs`
  - `C:\Users\ala\Documents\secure-shell\tools\port\served.mjs`
  - `C:\Users\ala\Documents\secure-shell\tools\port\store.mjs`

## `C:\Users\ala\Documents\dl-enclave`
- files: 154 · seconds: 1.7 · **truncated: no** · xml: 0
- repo `C:\Users\ala\Documents\dl-enclave` docs=['AGENTS.md'] workflows=**none**
- driver references: 92 · `policy`×88, `ledger`×57, `witness`×33, `mount`×15, `civilians`×9, `cadence`×9, `format`×5, `client`×3, `health`×2
- identifiers: `surface.patch/1`×38, `dl-enclave.pkg/1`×31, `dl-enclave.surface/1`×26, `dl-enclave.shell/1`×22, `axis-grant/1`×16, `surface.mount/2`×16, `shploingus.recipe/3`×14, `dl-enclave.addon/1`×14, `openlock.envelope/1`×12, `shploingus.theme/1`×11, `shploingus.form/1`×9, `openlock.addons/2`×9, `openlock.game/1`×9, `shploingus.recipe/4`×5, `recipe/3`×5, `surface/1`×5, `shploingus.layer/1`×4, `recipe/4`×3, `shploingus.deadlock/1`×2, `form/1`×1, `shploingus.cells/0`×1, `shploingus.cellframe/0`×1, `shploingus.chain/1`×1, `shploingus.chain-event/1`×1, `shploingus.cells/1`×1
- store sites:
  - `C:\Users\ala\Documents\dl-enclave\README.md`
  - `C:\Users\ala\Documents\dl-enclave\clientaddon\dashboard\README.md`
  - `C:\Users\ala\Documents\dl-enclave\docs\BOUNDARIES.md`
  - `C:\Users\ala\Documents\dl-enclave\docs\MCP-SURFACE.md`
  - `C:\Users\ala\Documents\dl-enclave\docs\PACKAGE-FORMAT.md`
  - `C:\Users\ala\Documents\dl-enclave\docs\PLAN.md`
  - `C:\Users\ala\Documents\dl-enclave\patches\PATCH-002-the-mount-host.md`
  - `C:\Users\ala\Documents\dl-enclave\patches\PATCH-013-the-addon-store.md`
  - `C:\Users\ala\Documents\dl-enclave\tools\README.md`
  - `C:\Users\ala\Documents\dl-enclave\tools\surface_receiver.py`
  - `C:\Users\ala\Documents\dl-enclave\tools\port\README.md`
  - `C:\Users\ala\Documents\dl-enclave\tools\port\src\client.mjs`
  - `C:\Users\ala\Documents\dl-enclave\tools\port\src\run.mjs`
  - `C:\Users\ala\Documents\dl-enclave\tools\port\src\store.mjs`
  - `C:\Users\ala\Documents\dl-enclave\tools\port\test\mount.test.mjs`
- axis/civ sites: `C:\Users\ala\Documents\dl-enclave\AGENTS.md`, `C:\Users\ala\Documents\dl-enclave\docs\DRIFT.md`, `C:\Users\ala\Documents\dl-enclave\docs\INVENTORY.md`, `C:\Users\ala\Documents\dl-enclave\docs\MCP-SURFACE.md`, `C:\Users\ala\Documents\dl-enclave\docs\PACKAGE-FORMAT.md`, `C:\Users\ala\Documents\dl-enclave\docs\PLAN.md`, `C:\Users\ala\Documents\dl-enclave\enclave\README.md`, `C:\Users\ala\Documents\dl-enclave\schema\README.md`

## `C:\Users\ala\Documents\ala_civ_bots_prototype`
- files: 2552 · seconds: 5.2 · **truncated: yes** · xml: 0
- repo `C:\Users\ala\Documents\ala_civ_bots_prototype` docs=['AGENTS.md', 'CHECKPOINT.md', 'CONTEXT.md'] workflows=**none**
- driver references: 509 · `client`×431, `policy`×92, `cadence`×78, `ledger`×44, `witness`×40, `health`×34, `civilians`×24, `format`×12, `mount`×9
- identifiers: `secure-shell.served/1`×28, `surface.mount/2`×25, `secure-shell.ledger/1`×18, `dl-enclave.surface/1`×14, `secure-shell.ingest/1`×13, `served/1`×5, `system1-agent/1`×3, `secure-shell.admission/1`×3, `dl-enclave.sig/1`×3, `openlock.addons/2`×3, `civilian.axis-cells/1`×2, `secure-shell.port-baseline/1`×2, `minecraft.cua-action/1`×2, `secure-shell.served/2`×2, `ensouled.frame/1`×2, `surface.patch/1`×1, `mount/3`×1, `secure-shell.material-grade/1`×1, `openlock.envelope/1`×1, `ensouled.autopopulation/1`×1, `civilian.decision/1`×1, `ensouled.action/1`×1, `ensouled.chat/1`×1, `ensouled.message/1`×1, `civilian.observation/1`×1
- store sites:
  - `C:\Users\ala\Documents\ala_civ_bots_prototype\CHECKPOINT.md :: eam store ensouled_streams at mongodb://127.0.0.1:27018 (per-agent isolation, read-back verified) [ensouled] stream store replay: 18 row(s)`
  - `C:\Users\ala\Documents\ala_civ_bots_prototype\README.md`
  - `C:\Users\ala\Documents\ala_civ_bots_prototype\docs\AUDIT_AGAINST_SECURE_SHELL.md`
  - `C:\Users\ala\Documents\ala_civ_bots_prototype\docs\GAMEPLAY_DEGREES.md`
  - `C:\Users\ala\Documents\ala_civ_bots_prototype\docs\IMPLEMENTATION_STATUS.md :: ore is `ensouled_streams` on `mongodb://127.0.0.1:27018` (`scripts/mongo.sh`), following the project family's own discipline in `openlock/to`
  - `C:\Users\ala\Documents\ala_civ_bots_prototype\docs\LAYER_TABLE.md`
  - `C:\Users\ala\Documents\ala_civ_bots_prototype\docs\persistent_city_builder_tower_defense_design_analysis_v4.md`
  - `C:\Users\ala\Documents\ala_civ_bots_prototype\docs\persistent_city_builder_tower_defense_design_analysis_v5.md`
  - `C:\Users\ala\Documents\ala_civ_bots_prototype\docs\persistent_city_builder_tower_defense_design_analysis_v9.md`
  - `C:\Users\ala\Documents\ala_civ_bots_prototype\docs\UPSTREAM_ALIGNMENT.md`
- axis/civ sites: `C:\Users\ala\Documents\ala_civ_bots_prototype\docs\minecraft_ensouled_system1_cua_architecture_v3.md`, `C:\Users\ala\Documents\ala_civ_bots_prototype\docs\minecraft_ensouled_system1_cua_architecture_v4.md`, `C:\Users\ala\Documents\ala_civ_bots_prototype\docs\minecraft_shared_server_bot_client_population_addendum.md`, `C:\Users\ala\Documents\ala_civ_bots_prototype\docs\UPSTREAM_ALIGNMENT.md`, `C:\Users\ala\Documents\ala_civ_bots_prototype\src\main\java\dev\ensouled\axis\AxisGate.java`, `C:\Users\ala\Documents\ala_civ_bots_prototype\src\main\java\dev\ensouled\axis\AxisProof.java`, `C:\Users\ala\Documents\ala_civ_bots_prototype\src\main\java\dev\ensouled\axis\AxisVocabulary.java`, `C:\Users\ala\Documents\ala_civ_bots_prototype\src\main\java\dev\ensouled\axis\DecisionPackage.java`, `C:\Users\ala\Documents\ala_civ_bots_prototype\src\main\java\dev\ensouled\core\AgentMind.java`, `C:\Users\ala\Documents\ala_civ_bots_prototype\src\main\java\dev\ensouled\core\DecisionJournal.java`
- note: budget reached at C:\Users\ala\Documents\ala_civ_bots_prototype\src\main\java\dev\ensouled\domain

## `C:\Users\ala\Documents\ala_package_designer`
- files: 152 · seconds: 1.8 · **truncated: no** · xml: 0
- repo `C:\Users\ala\Documents\ala_package_designer` docs=**none** workflows=**none**
- driver references: 75 · `policy`×74, `ledger`×26, `witness`×20, `civilians`×9, `cadence`×7, `health`×7, `format`×7, `client`×1
- identifiers: `recipe/3`×4, `shploingus.recipe/4`×4, `shploingus.recipe/3`×3, `recipe/4`×2
- magics: `SHPKG003`×5, `SHPKG002`×4, `SHPKG009`×1

## `C:\Users\ala\Documents\agent_god_files`
- files: 21077 · seconds: 188.7 · **truncated: yes** · xml: 0
- driver references: 781 · `policy`×555, `witness`×189, `health`×56, `ledger`×31, `format`×30, `civilians`×17, `cadence`×16
- identifiers: `civ-cities/2`×1, `civ-cities/1`×1
- store sites:
  - `C:\Users\ala\Documents\agent_god_files\civ_logic\src\bin\hostile.rs`
  - `C:\Users\ala\Documents\agent_god_files\civ_logic\src\cities\store.rs`
- note: budget reached at C:\Users\ala\Documents\agent_god_files\prose_logic\profiles

## `F:\planet-shploingus`
- files: 0 · seconds: 0.0 · **truncated: yes** · xml: 0
- note: budget reached at F:\planet-shploingus

## `F:\shploingus-mod-sources`
- files: 0 · seconds: 0.0 · **truncated: yes** · xml: 0
- note: budget reached at F:\shploingus-mod-sources

## `F:\ala-cities-temp`
- files: 0 · seconds: 0.0 · **truncated: yes** · xml: 0
- note: budget reached at F:\ala-cities-temp

## `F:\agent_god_build`
- files: 0 · seconds: 0.0 · **truncated: yes** · xml: 0
- note: budget reached at F:\agent_god_build

## `F:\tmp_db`
- files: 0 · seconds: 0.0 · **truncated: yes** · xml: 0
- note: budget reached at F:\tmp_db

## `C:\`
- files: 0 · seconds: 0.0 · **truncated: yes** · xml: 0
- note: total budget exhausted before this drive

## `D:\`
- files: 0 · seconds: 0.0 · **truncated: yes** · xml: 0
- note: total budget exhausted before this drive

## `E:\`
- files: 0 · seconds: 0.0 · **truncated: yes** · xml: 0
- note: total budget exhausted before this drive

## `F:\`
- files: 0 · seconds: 0.0 · **truncated: yes** · xml: 0
- note: total budget exhausted before this drive

## `G:\`
- files: 0 · seconds: 0.0 · **truncated: yes** · xml: 0
- note: total budget exhausted before this drive

## `H:\`
- files: 0 · seconds: 0.0 · **truncated: yes** · xml: 0
- note: total budget exhausted before this drive

## Totals
- files inspected: 32913 · elapsed: 226s
- references: 3240 · with digest: 900 · omitted over cap: 0
- roots absent: none
- topics: `policy`×1831, `ledger`×1411, `client`×525, `witness`×466, `cadence`×375, `health`×189, `format`×163, `civilians`×151, `mount`×59
- own numeric identifiers: 152 distinct, 1258 occurrences
- magics: {'V4PKG001': 5, 'SHPKG002': 6, 'SHPKG003': 8, 'V4PKG002': 1, 'SHPKG009': 2} · xml files: 26

## Refusals this scan itself demonstrates
- `audit-stream-truncated`: a root hit its budget and still produced a partial row.
- `audit-gap-silent`: an absent root is reported as absent, never as zero findings.
- `audit-unprovenanced`: a count without file:line is not accepted as evidence.
- `audit-unstreamed`: output held until exit hides truncation and is refused.
- `reference-capped`: at most 6000 references are recorded; 0 were counted but not listed.
- `digest-documents-only`: digests are computed under `C:\Users\ala\Documents` only, capped at 900; elsewhere the path and size are the reference.
- `scan-pruned`: `target`, `node_modules`, `build`, `Windows`, `AppData` and the audit's own output are never entered.

## Classification of reference hits
| Topic | Files | Serves |
|---|---:|---|
| `policy` | 1831 | D8/D12 — refusals and retention |
| `ledger` | 1411 | D9 — receipts and their digest |
| `client` | 525 | D7 — the surface the driver drives |
| `witness` | 466 | D7 — the driver reports, the server attests |
| `cadence` | 375 | D6 — the tick rate that must not be hardcoded |
| `health` | 189 | D9/D12 — whether a degraded run is sealed or dropped |
| `format` | 163 | D1–D5 — id width, preimage and framing |
| `civilians` | 151 | D8 — the refusal a civilian action carries |
| `mount` | 59 | D10 — the one owner of mount state |

### Primary references
| Id | Path | Bytes | sha256 | Topics |
|---|---|---:|---|---|
| `R0001` | `C:\Users\ala\Documents\secure_shell_v2\AGENTS.md` | 17395 | `2d37555ab8c219f486edfdbe3dacc4feaced2058cc2946be2ee73b36851a2da1` | civilians, health, policy, ledger |
| `R0002` | `C:\Users\ala\Documents\secure_shell_v2\docs\HYPERSKILL@0.1.0.LOADED.md` | 6203 | `4ee261918affa1f7737bed3b344be5f060c733ac1c0485de59d32e531cb47f68` | witness, civilians, cadence, policy, ledger |
| `R0003` | `C:\Users\ala\Documents\secure_shell_v2\docs\SECURE-SHELL-HEALTH@1.FAILURE-LEDGER.md` | 19578 | `7d44132355984f709353fe1fcef7b96cf00975f4c07b68bfdee20661796b7a94` | civilians, health, format, policy, ledger |
| `R0004` | `C:\Users\ala\Documents\secure_shell_v2\docs\SECURE-SHELL-HEALTH@1.HANDOFF.md` | 7661 | `243754e1f0d98dff7273bdedcefc68dd91364982cfb363ac704587b67a2cfdc5` | health, policy, ledger |
| `R0005` | `C:\Users\ala\Documents\secure_shell_v2\docs\SECURE-SHELL-RESTORE@1.AGENT-BOOTSTRAP-API.md` | 9032 | `353cd29cf0a68ab3649a6cf9a6a686ca705108971b74c1500fd60b7f6741450d` | witness, civilians, health, policy, ledger |
| `R0006` | `C:\Users\ala\Documents\secure_shell_v2\docs\SECURE-SHELL-RESTORE@1.ARCHITECTURE.md` | 34073 | `df614b5e19388de48574f20ed20a89c3e3d2c5db8d9d4abf585287c44720f17f` | witness, civilians, cadence, health, mount, policy, ledger |
| `R0007` | `C:\Users\ala\Documents\secure_shell_v2\docs\SECURE-SHELL-RESTORE@1.CUA-CIVILIAN-ACCEPTANCE.md` | 30499 | `2ebe6705879eea1802900035e6388ac419dd08006d5c228009770d81d5cd3976` | witness, civilians, cadence, health, client, policy, ledger |
| `R0008` | `C:\Users\ala\Documents\secure_shell_v2\docs\SECURE-SHELL-RESTORE@1.FORMAT-IMPORT-AUDIT.md` | 12955 | `9649084dac5d676a4110802fb61b97bc47b681a34920de83a66d3c4563f9753a` | civilians, format, mount, policy, ledger |
| `R0009` | `C:\Users\ala\Documents\secure_shell_v2\docs\SECURE-SHELL-RESTORE@1.HYPERGRILL.md` | 40173 | `da7101c71fdc8a3c3193e1ba0572472be3a0e3486a7eda3ce96dc72b70e7d611` | witness, civilians, cadence, health, format, mount, policy, ledger |
| `R0010` | `C:\Users\ala\Documents\secure_shell_v2\docs\SECURE-SHELL-RESTORE@1.IMPLEMENTATION-PLAN.md` | 14317 | `179acc30a74b5ecf1866de1c5dc62361a54e3e21216d4c064ec0c2e5318db2ba` | witness, civilians, cadence, health, mount, policy, ledger |
| `R0011` | `C:\Users\ala\Documents\secure_shell_v2\docs\SECURE-SHELL-V2-AGENT-BOOTSTRAP-API.md` | 15777 | `7ea7f7ef1189518747f11d10c5c329f9d659706d1963eaa772f406b1fe75d6df` | witness, civilians, health, policy, ledger |
| `R0012` | `C:\Users\ala\Documents\secure_shell_v2\docs\SECURE-SHELL-V2-ARCHITECTURE.md` | 17117 | `bd06ad24bc51c2ae98056393d1c24697e96a982a537bf2f71f692800dd9a9175` | witness, civilians, cadence, health, mount, policy, ledger |
| `R0013` | `C:\Users\ala\Documents\secure_shell_v2\docs\SECURE-SHELL-V2-CUA-CIVILIAN-ACCEPTANCE.md` | 16108 | `bc940c1cb72f261eb99e97242cc243421610b08d5cb59ff4ac1311c576eaa6b9` | witness, civilians, cadence, health, policy, ledger |
| `R0014` | `C:\Users\ala\Documents\secure_shell_v2\docs\SECURE-SHELL-V2-FORMAT-IMPORT-AUDIT.md` | 21082 | `e7c59f5f80b82bb3f177a858fea18c23ffe774725e136b6ee78d39a728386555` | witness, civilians, cadence, health, format, mount, policy, ledger |
| `R0015` | `C:\Users\ala\Documents\secure_shell_v2\docs\SECURE-SHELL-V2-IMPLEMENTATION-PLAN.md` | 22105 | `e4b4ef2e3fd2c2837b2e74e8945def92d7f25471873983b074098e5bd24cdff6` | witness, civilians, cadence, health, format, mount, policy, ledger |
| `R0016` | `C:\Users\ala\Documents\secure_shell_v2\docs\hypergrill\audit@2026-11-04.json` | 185877 | `not computed` | civilians, cadence, health, format, policy, ledger |
| `R0017` | `C:\Users\ala\Documents\secure_shell_v2\docs\hypergrill\AUDIT@2026-11-04.md` | 8539 | `not computed` | civilians, cadence, health, format, policy, ledger |
| `R0018` | `C:\Users\ala\Documents\secure_shell_v2\docs\hypergrill\state.json` | 88179 | `777ded8768844c7bbda6cbdbe1b237ce0ba853e3466dc384a4dd4798f0afcca9` | witness, civilians, cadence, health, mount, policy, ledger |
| `R0019` | `C:\Users\ala\Documents\secure_shell_v2\impl\packages\canonical.py` | 15079 | `d5d972a9dfab682c6715e3a808eb1ad9cb557caf6dec4c16729e1678988403c7` | mount, policy, ledger |
| `R0020` | `C:\Users\ala\Documents\secure_shell_v2\impl\packages\identity.py` | 12114 | `727ac18b9decf5483536a04247ba6ee01a539be504f10b697c8403b464b4486a` | format, policy |
| `R0021` | `C:\Users\ala\Documents\secure_shell_v2\impl\packages\loader.py` | 4401 | `dde5bd9413fcac68ef9dc3743c33d7d73c72d31d53f5383c18d4b7ac0141ebd5` | format, policy |
| `R0022` | `C:\Users\ala\Documents\secure_shell_v2\impl\packages\mongo_store.py` | 6255 | `0f6ed45614cfcfbaab984af0c9ae5d99e1bd1c179c02a38685cc2251e9ac69df` | policy |
| `R0023` | `C:\Users\ala\Documents\secure_shell_v2\impl\packages\stream.py` | 17152 | `ba50129cb7459f1dce046deb96cd27297563cf3685bcdaf009da9235e1bd15dc` | policy |
| `R0024` | `C:\Users\ala\Documents\secure_shell_v2\tests\handoff\run_cases.py` | 2131 | `4162ac05ee6124efa059bbb6435a43f9ee340775e9d1ac9cc5fcb8d9d6f1a981` | health, policy, ledger |
| `R0025` | `C:\Users\ala\Documents\secure_shell_v2\tests\packages\run_cases.py` | 8137 | `bb9d2d034e95eb715816937efeca27f2606aa2cc56192f4874e3e2bdd8b06208` | format, policy, ledger |
| `R0026` | `C:\Users\ala\Documents\secure_shell_v2\tests\packages\run_cases_canonical.py` | 8443 | `3b69f6bf32836929a6328a12d125fbc04c35474cedad9110d0951595b2d3a17e` | mount, policy |
| `R0027` | `C:\Users\ala\Documents\secure_shell_v2\tests\packages\run_cases_loader.py` | 3655 | `4dfc45a342925595e2f4c50d94bdce233a75bce32d458ce951bc4e634d67ccca` | policy |
| `R0028` | `C:\Users\ala\Documents\secure_shell_v2\tests\packages\run_cases_stream.py` | 11887 | `01c3711a9d8dcc045eb434378698843a2c1f0b65c9b8dadcdada329928e05e9e` | policy |
| `R0029` | `C:\Users\ala\Documents\secure_shell_v2\tickets\TICKET-0001-round-v2-4-and-publish.md` | 4374 | `ec82a26eefeed832b46f1262b2d59d60be436bb6556b7cda7d70210ccc34479c` | civilians, health, policy, ledger |
| `R0030` | `C:\Users\ala\Documents\secure_shell_v2\tickets\TICKET-0002-handoff-ratchet.md` | 4209 | `eac29e3ecc9f76d87f29d8a782604d9e9562fefa6ba0a6f3e98c6084f1727d0a` | civilians, health, policy, ledger |
| `R0031` | `C:\Users\ala\Documents\secure_shell_v2\tickets\TICKET-0005-enumerated-handoff-gate.md` | 2019 | `7a512768800cfba16067bca1f79bf87cfba34931d985d538d3a2cd7d614f3a3d` | civilians, health, policy, ledger |
| `R0032` | `C:\Users\ala\Documents\secure_shell_v2\tickets\TICKET-0007-package-identity.md` | 3018 | `0fee9fbfd203bfc312ba15ff92c5f8e3d799d6e7d4785e70a8fc6016530d1de5` | health, policy, ledger |
| `R0033` | `C:\Users\ala\Documents\secure_shell_v2\tickets\TICKET-0008-canonical-manifest.md` | 3012 | `158b9bf861702b76dc052cac9235b32fdd8db00d2c08bcc9ccdc8fc6323c356a` | health, policy, ledger |
| `R0034` | `C:\Users\ala\Documents\secure_shell_v2\tickets\TICKET-0009-stream-and-real-sources.md` | 3142 | `3a7dfce405ef0390963a3859bf48878d25cc0cd0a360a4a45247070a83b509c6` | health, mount, policy, ledger |
| `R0035` | `C:\Users\ala\Documents\secure_shell_v2\tickets\TICKET-0010-r2-generation.md` | 4227 | `1d258a2ce268c77892a4b491da871ad531d4fee4251400b41e62c51420b617cc` | health, policy, ledger |
| `R0036` | `C:\Users\ala\Documents\secure_shell_v2\tickets\TICKET-0011-debian-restore-drill.md` | 5843 | `a5be513ed7f136c00c9a528780cf57b4d69f869d37e12ec656f211abf5020112` | policy, ledger |
| `R0037` | `C:\Users\ala\Documents\secure_shell_v2\tools\handoff_ratchet.py` | 11374 | `2e73b2be33ce0519b9d27ede4d8c48b5920002d966839d2bf0cc16be422cdb85` | health, policy, ledger |
| `R0038` | `C:\Users\ala\Documents\secure_shell_v2\tools\hypergrill_reaudit.py` | 24960 | `631e1a814064acd2f4c440e10a0ceb131fddc197153d9b6f634797df909a0486` | civilians, cadence, health, format, policy, ledger |
| `R0039` | `C:\Users\ala\Documents\secure_shell_v2\tools\hypergrill_resolver.py` | 20013 | `99837fc6580e228926c46f064bdb6d12bf94becdfedc5caa870b84fb31d3e1fc` | witness, civilians, cadence, policy, ledger |
| `R0040` | `C:\Users\ala\Documents\secure_shell_v2\tools\mongo_setup.py` | 5503 | `8340c5b5280052cf631da9542d3cf71e4587ed3bfcdf5307b0e5b6532ad36842` | policy |
| `R0041` | `C:\Users\ala\Documents\secure_shell_v2\tools\mongo_tamper.py` | 1295 | `037147153c962d2008c702033fef4423bfc52b2df7ae2036ecafac332b139061` | policy |
| `R0042` | `C:\Users\ala\Documents\secure_shell_v2\tools\restore_drill.py` | 13180 | `275b56e54134ee775c9cd219652cfd63b3ed796eb5e41d2af8c1e1d46b5581db` | format, policy, ledger |
| `R0043` | `C:\Users\ala\Documents\secure_shell_v2\tools\resynth_agents.py` | 7770 | `9479cc8b43f71df86339560a507619b23a4097d320ad0ad3cbecb4001a327d4b` | civilians, health, policy, ledger |
| `R0044` | `C:\Users\ala\Documents\secure_shell_v2\tools\scan_drives_reaudit.py` | 20669 | `bf93d0308635776d507c7f9e894cc7fdba726ebb52d629bc05071bbe43b9ab64` | witness, civilians, cadence, health, format, mount, client, policy, ledger |
| `R0045` | `C:\Users\ala\Documents\testport1\AGENTS.md` | 16459 | `843c721a65438ce50a08283b1e8045ef48102d8e399369bd6c15aa18ac915852` | witness, health, format, policy, ledger |
| `R0046` | `C:\Users\ala\Documents\testport1\Cargo.toml` | 244 | `fb66849c03dfe5d393754e11636aa541c0c02b841820c30ed5bbbd6d253005c7` | ledger |
| `R0047` | `C:\Users\ala\Documents\testport1\artifacts\health\state.json` | 23477 | `89961d7bdfd81de75f5b5186c500cb575fd4ed05104c9e21e9bc1cc79a123e8c` | witness, health, format, policy, ledger |
| `R0048` | `C:\Users\ala\Documents\testport1\artifacts\redacted-test-results\port-gate-selftest.json` | 45760 | `14af33c1d38ae9407b21315fb2816a6ffa30e6c4c4c57b2588d9b16dc6ede88d` | civilians, format, policy, ledger |
| `R0049` | `C:\Users\ala\Documents\testport1\config\cell-addon.json` | 2500 | `01ed7b904723455417552876d709923b08a55051a33e7da4d4c9f99e3d6ba12f` | witness, policy, ledger |
| `R0050` | `C:\Users\ala\Documents\testport1\config\cell-program.json` | 880 | `658cbabe97a482b655526670edcdeb5c2cdd0405d53de1479a157d5c47dfee4e` | policy |
| `R0051` | `C:\Users\ala\Documents\testport1\config\cell-schema.json` | 1129 | `f48d32e0afee377b1f1ce816a1d643a84155c62d36074f1bdc82d5c01cd5018f` | policy |
| `R0052` | `C:\Users\ala\Documents\testport1\config\format-allowlist.json` | 623 | `1f5fdb8f9800f59177a6ffbfc9a4a7faf4765b1d8ed52e08dab037c67464b16b` | format, policy |
| `R0053` | `C:\Users\ala\Documents\testport1\config\legacy-formats.json` | 40669 | `15d40caf301040aeacd3feb5ad1327951b936ab91ba57a774591a51a0623d456` | witness, civilians, mount, client, policy, ledger |
| `R0054` | `C:\Users\ala\Documents\testport1\config\output-roots.json` | 1944 | `23ff7f620c5f1dd07bead9bc043f95e726004e2d4c86754b201b62ac4b65a0a1` | civilians, policy |
| `R0055` | `C:\Users\ala\Documents\testport1\config\plan-errata.json` | 2603 | `dd34c25b5bee73f02ac59e07cc30eb7eb3da70cfcfb1b7a61bf42fe91f0657ad` | format, mount, ledger |
| `R0056` | `C:\Users\ala\Documents\testport1\crates\planet-aead\src\lib.rs` | 7202 | `519058e0a8942eba286c1123b073f3a3702c861c66c3fbc1310133b4239723cd` | policy, ledger |
| `R0057` | `C:\Users\ala\Documents\testport1\crates\planet-client\src\audio.rs` | 13851 | `c6c8f4ba89500c824ecd07a184cc403bdb5855f47e684833f11f3653aff6003e` | policy |
| `R0058` | `C:\Users\ala\Documents\testport1\crates\planet-client\src\axis.rs` | 14120 | `daabd073d50c48476fed3a859087265176347c7f879793d1f73761a857641557` | witness, cadence, format, policy |
| `R0059` | `C:\Users\ala\Documents\testport1\crates\planet-client\src\batch.rs` | 4569 | `74e9f674b6893d5134a95491609399bbb601a20104096b71d825c95b2a2cfab8` | policy |
| `R0060` | `C:\Users\ala\Documents\testport1\crates\planet-client\src\cell_mount.rs` | 5290 | `b7821fd1ac505bf8e555ed0b4b00922a9e86a7d6ae8db37378a8fd44c9e4e331` | cadence, policy, ledger |
| `R0061` | `C:\Users\ala\Documents\testport1\crates\planet-client\src\console.rs` | 7399 | `1e844cad7fd224db2a445494878314e74d850e99e05328f498dfbf900e04e4fc` | policy |
| `R0062` | `C:\Users\ala\Documents\testport1\crates\planet-client\src\draw.rs` | 6626 | `9bdac598b8c3bf4c62a7af4d03b407a107ab96f4293f332a54d26b03358f727f` | cadence, policy |
| `R0063` | `C:\Users\ala\Documents\testport1\crates\planet-client\src\font.rs` | 4582 | `4147bdca550e1159fa05c6e93229e48d817932553a92dd89f785859c8ed3c0b5` | policy |
| `R0064` | `C:\Users\ala\Documents\testport1\crates\planet-client\src\input.rs` | 12784 | `babeff693c51974940511c592366d820d99637a351c765c040df39c49b7b0fc6` | civilians |
| `R0065` | `C:\Users\ala\Documents\testport1\crates\planet-client\src\lib.rs` | 1619 | `31fb10c5bcf0b10c4f4dab646342db77c17d83d7bcbbad0264675d995699fb09` | policy, ledger |
| `R0066` | `C:\Users\ala\Documents\testport1\crates\planet-client\src\package_owner.rs` | 902 | `a73f5854dd57079a6ef1c29e1f8313a73cdf433ef893d3511dd973ac1d71dab8` | policy, ledger |
| `R0067` | `C:\Users\ala\Documents\testport1\crates\planet-client\src\palette.rs` | 2925 | `3e29cd3ae915353c8f71a1252b86ece3f45a517f61367dfc026e3f7cfe90088f` | policy |
| `R0068` | `C:\Users\ala\Documents\testport1\crates\planet-client\src\picture.rs` | 4237 | `9525f6d8124ab54390f2f2906988113c51c5d06fae04b6d3d66a2e59a06e7738` | policy |
| `R0069` | `C:\Users\ala\Documents\testport1\crates\planet-client\src\playback.rs` | 11302 | `caac731b91badb160b3711633ad0bd91431f3d7479221e4e6c53c165eba9f179` | cadence |
| `R0070` | `C:\Users\ala\Documents\testport1\crates\planet-client\src\present.rs` | 3202 | `eed0cef67d03023f68f7255f5067defab9081d3b49dbd095792341085ac9bbbb` | policy |
| `R0071` | `C:\Users\ala\Documents\testport1\crates\planet-client\src\render.rs` | 29527 | `6f077faa179a312f4f1fe988cc1caffb2aafa83273a0207bcedb55a4ecf377ed` | witness, cadence, policy |
| `R0072` | `C:\Users\ala\Documents\testport1\crates\planet-client\src\scene.rs` | 2828 | `4355233b498f2e4c62220615bde86c7cbb59fdefd4cb2e3810161543278a614f` | policy |
| `R0073` | `C:\Users\ala\Documents\testport1\crates\planet-client\src\script.rs` | 9640 | `f1c05b4a3952480c0321317622099df78f6b278e2fa1ff405e5d26621d01a56b` | cadence, policy |
| `R0074` | `C:\Users\ala\Documents\testport1\crates\planet-client\src\timeline.rs` | 5088 | `372e54767a6cbc1af2c2e6d144da7f3b853d0266240fd1c14647f3abf54f7dc4` | cadence, policy |
| `R0075` | `C:\Users\ala\Documents\testport1\crates\planet-client\src\xml.rs` | 11155 | `9b500216779b66b38c7509cc2bee1d1cf58165f230a266b3a88d6c08b70296ac` | policy |
| `R0076` | `C:\Users\ala\Documents\testport1\crates\planet-client\src\bin\inspect.rs` | 20434 | `90fb1e054b7f516364fbdb790b3007f90f47c17c5e967e5295f7293e77cd64aa` | witness, cadence, policy, ledger |
| `R0077` | `C:\Users\ala\Documents\testport1\crates\planet-client\src\bin\window.rs` | 10606 | `236ced5bc36e4b4cd93a8d6f63658af37eed2951448e039322826c132c9857c4` | cadence, policy, ledger |
| `R0078` | `C:\Users\ala\Documents\testport1\crates\planet-client\src\bin\xml_window.rs` | 2122 | `1375ee0f5b1842989393f83d851ef3a2cf5d72ef4e6e8b986d727dd5d7baf3dc` | policy |
| `R0079` | `C:\Users\ala\Documents\testport1\crates\planet-client\tests\adopt.rs` | 8493 | `69dc67e3bb48d10effe6c93f56ae5081736f95d151e2d1afa83e11ae257384ca` | format, policy, ledger |
| `R0080` | `C:\Users\ala\Documents\testport1\crates\planet-client\tests\audio.rs` | 3571 | `6af0e212f94d2eddd4feb44476b71df706232bd123e364832c571db91b34e2fa` | policy |
| `R0081` | `C:\Users\ala\Documents\testport1\crates\planet-client\tests\batch.rs` | 8720 | `0ed709b3873c1e2157d9a4c88b23bca67fefbb71f42a64bde62279e75fdf9d37` | policy |
| `R0082` | `C:\Users\ala\Documents\testport1\crates\planet-client\tests\draw.rs` | 6026 | `0cec17fa06456aeac2a28e59665df585b8d390d256f23da8d1f0409101613e51` | policy |
| `R0083` | `C:\Users\ala\Documents\testport1\crates\planet-client\tests\picture.rs` | 6778 | `770882cee7505132a8b95985aa1f8f21b7844e0ea32be15df21eb065d0245a19` | policy |
| `R0084` | `C:\Users\ala\Documents\testport1\crates\planet-client\tests\scene.rs` | 4087 | `7582cf29df56aab27b031aefb6063a334f45b9a1152bad529167ed17b6811a1b` | policy |
| `R0085` | `C:\Users\ala\Documents\testport1\crates\planet-package\Cargo.toml` | 329 | `c010196ca9ee7af430cb56374e62956772c3fd9b7494b1894d61c808d8547d27` | format, ledger |
| `R0086` | `C:\Users\ala\Documents\testport1\crates\planet-package\src\cadence.rs` | 25728 | `fdb0ec6151708c8ac0a92fb024d31a005addc53a833c1d8380bec522eb3c604c` | cadence, policy |
| `R0087` | `C:\Users\ala\Documents\testport1\crates\planet-package\src\cellframe.rs` | 79740 | `1e74407fe59b67b54d4a70335dbac930aead754317754209e4a61a9e6a7b98b5` | policy, ledger |
| `R0088` | `C:\Users\ala\Documents\testport1\crates\planet-package\src\format_id.rs` | 11505 | `1f07e3d9cae135653c977be6b446a902ed32634df11e6f20a277211038624d97` | format, mount, policy, ledger |
| `R0089` | `C:\Users\ala\Documents\testport1\crates\planet-package\src\frame.rs` | 17703 | `14847e1443efc23324d9563057bec6b8f53f4b08c172590a852c8d613c2842ba` | format, policy, ledger |
| `R0090` | `C:\Users\ala\Documents\testport1\crates\planet-package\src\lib.rs` | 3001 | `79fd3beb7ce979fce0f3e6a6cb3a7633fd964ba4ec9b2967e5f87d5251b52810` | cadence, format, policy, ledger |
| `R0091` | `C:\Users\ala\Documents\testport1\crates\planet-package\src\mount.rs` | 1808 | `9a971e41474fc718ada3ddf27bfff08fcc49c63953d17d25e30d9c7a50929a24` | mount, policy, ledger |
| `R0092` | `C:\Users\ala\Documents\testport1\crates\planet-package\src\palette.rs` | 4923 | `aa6a435277ea3d4514b9550b5cfc091d39840ff31928be9e98fa2841392b7c5a` | policy |
| `R0093` | `C:\Users\ala\Documents\testport1\crates\planet-package\src\program.rs` | 18486 | `3d8e6d6dfeda06e467ba8b030d8fe24a1637f301e650bfa13da0151f7f7e75b4` | cadence, policy |
| `R0094` | `C:\Users\ala\Documents\testport1\crates\planet-package\src\record.rs` | 5589 | `f5894ce78d601a4e5fe92477ba17909aac37d98c181013bfef42db2d08c897d7` | policy, ledger |
| `R0095` | `C:\Users\ala\Documents\testport1\crates\planet-package\src\surface.rs` | 14866 | `b3cd491e44c28d82de7124b0569533c777faf5eaf750ff0715034b25b90b3f3d` | format, policy |
| `R0096` | `C:\Users\ala\Documents\testport1\crates\planet-package\src\texels.rs` | 8950 | `ddce8941cc9cd378aa3a685489e0a928c77499a5335dd6fca08aceb7c40d892b` | policy |
| `R0097` | `C:\Users\ala\Documents\testport1\crates\planet-package\src\vocabulary.rs` | 5930 | `f408823cbaa124867b17f6bee380c197552cc142b38b09896d950d8297c4f1dd` | policy |
| `R0098` | `C:\Users\ala\Documents\testport1\crates\planet-package\tests\binding.rs` | 15746 | `884a16f7bfaae7247a1fc382ba8f8c9c86f697c2980880abe20dd25413b7fc8c` | policy, ledger |
| `R0099` | `C:\Users\ala\Documents\testport1\crates\planet-package\tests\cellframe.rs` | 14968 | `fb915348918a2b87770fb2cdc5011a97f9870ce610d74adb3a91a5d99f3526e3` | policy |
| `R0100` | `C:\Users\ala\Documents\testport1\crates\planet-package\tests\frame_mount.rs` | 6410 | `e5e138deabdce80bd624e176938bec83671133c7fd7cdbf0fa8a228617885564` | format, policy, ledger |
| `R0101` | `C:\Users\ala\Documents\testport1\crates\planet-package\tests\mount_entry.rs` | 6771 | `8dffa8b45836894214e5841bdc9768d67fb2bfcc345b56a092124eb44e0d4ffa` | policy, ledger |
| `R0102` | `C:\Users\ala\Documents\testport1\crates\planet-package\tests\role_class.rs` | 2694 | `d646472c0e62240cb2b9026e938670359fe6e70d6fd07ebd7caca36d5325b23c` | policy |
| `R0103` | `C:\Users\ala\Documents\testport1\crates\planet-package\tests\surface.rs` | 8854 | `57c16b75e593932d36d99e26acbbeffb7c5f01756938bfa9935d0180d8b99d1a` | format, policy, ledger |
| `R0104` | `C:\Users\ala\Documents\testport1\crates\planet-package\tests\vocabulary.rs` | 8140 | `c8564fcd72bc072eddf05f146226c56137e345023b6985f1aef3096494616e3e` | policy |
| `R0105` | `C:\Users\ala\Documents\testport1\crates\planet-save\Cargo.toml` | 345 | `f23e54979b284e99930c026ca646f936cd95da4df39a11edf936b590c8bf11a0` | ledger |
| `R0106` | `C:\Users\ala\Documents\testport1\crates\planet-save\src\lib.rs` | 19255 | `7092775b4b30d5fd216dd901fde3a3bb70f0f2b4228c0e2dde20dd4a5ff0d570` | policy, ledger |
| `R0107` | `C:\Users\ala\Documents\testport1\crates\planet-save\tests\transaction.rs` | 10393 | `d5750bf7e04e264fa4e096cce37c5aba2b31433566edffe88a30f17439dd8bad` | policy, ledger |
| `R0108` | `C:\Users\ala\Documents\testport1\crates\planet-shell-ledger\Cargo.toml` | 193 | `9edcedaea34eee67fb1c5006dbd7ae826717517eec9df1362b6fc2c2eca1ab64` | ledger |
| `R0109` | `C:\Users\ala\Documents\testport1\crates\planet-shell-ledger\src\landing.rs` | 1841 | `97df33af19eb91a162b05031bb8bd15a3add9e9faf4b0e5c35095bc62a6af833` | policy, ledger |
| `R0110` | `C:\Users\ala\Documents\testport1\crates\planet-shell-ledger\src\lib.rs` | 15975 | `60b8414c3670dfe69746974ae3663f5afc7e1797ecfa1f3ac80b8cd90d8d2ad2` | policy, ledger |
| `R0111` | `C:\Users\ala\Documents\testport1\crates\planet-shell-ledger\src\sha256.rs` | 4241 | `fd5a093b4301715ad39b98a1d969f879efafb603e27acbb1564a373f87f5a04b` | ledger |
| `R0112` | `C:\Users\ala\Documents\testport1\crates\planet-shell-ledger\tests\chain.rs` | 7552 | `26e630e658948fc655b0fc9a29f3f5474c86adebfc2945404f5087649d0cc6cb` | policy, ledger |
| `R0113` | `C:\Users\ala\Documents\testport1\crates\swf-import\Cargo.toml` | 513 | `a00545df44cf9546f8a4b3711283e747e544f03f0d3cedb76405d5784b7b66a1` | ledger |
| `R0114` | `C:\Users\ala\Documents\testport1\crates\swf-import\src\avm1.rs` | 9539 | `3e43ea82423624183a0fb6ae66da3623c9400d2956a046ecdde9dad072fd667c` | policy |
| `R0115` | `C:\Users\ala\Documents\testport1\crates\swf-import\src\bitmap.rs` | 16672 | `ce01f64312a956018693f79646424cd2c58a14f8831c9e5198cbf24029417cb7` | policy |
| `R0116` | `C:\Users\ala\Documents\testport1\crates\swf-import\src\content.rs` | 31362 | `529c051f5bd56cfa70f0c9570d4457276a534841a41563e04a9419c84b03575e` | policy |
| `R0117` | `C:\Users\ala\Documents\testport1\crates\swf-import\src\emit.rs` | 44350 | `3aca8a0a3b20c4f511b8232d9dcfd6219fb0665b178c2d7369a94cc523901035` | cadence, policy |
| `R0118` | `C:\Users\ala\Documents\testport1\crates\swf-import\src\header.rs` | 5865 | `4ab84c4e428533a6849b3a9ad8918daa2b13461dbe66229cf0af85ba7ae5c903` | policy |
| `R0119` | `C:\Users\ala\Documents\testport1\crates\swf-import\src\lib.rs` | 1005 | `7d417c8b602aa6988e6ea508c49f1e84edf250a7bd146faf630f2ba3a2526515` | policy |
| `R0120` | `C:\Users\ala\Documents\testport1\crates\swf-import\src\placement.rs` | 29187 | `126e654bd6d5911d606611b45f29b5a22c5ad37fb6973054c1437cc4989f4d0d` | policy |
| `R0121` | `C:\Users\ala\Documents\testport1\crates\swf-import\src\stream.rs` | 10129 | `fbbb2c483b438d301d9e181dd169400bdcaf49775ecd00e8ca77d8d5ccda4693` | cadence, policy, ledger |
| `R0122` | `C:\Users\ala\Documents\testport1\crates\swf-import\src\tags.rs` | 2261 | `84060021c102cdf89cd309816202f11dd22cecd988f9088da40cdf760cda37f5` | policy |
| `R0123` | `C:\Users\ala\Documents\testport1\crates\swf-import\src\bin\swf-import.rs` | 30973 | `dc37f40358f70b7c068da7c67d03ab5cb8288b376df13d0c3509b2a1faadb61f` | cadence, policy, ledger |
| `R0124` | `C:\Users\ala\Documents\testport1\crates\swf-import\tests\content.rs` | 6215 | `4b8238d20bc002e21f5baa21221d9880ba0eb3f658178c154dc661f6fabf15da` | ledger |
| `R0125` | `C:\Users\ala\Documents\testport1\crates\swf-import\tests\end_to_end.rs` | 10957 | `b013e584eb7a1bab191a57731a46f77e6d4baa23c75b7eec95fc60f6fc7ecb8e` | witness, cadence, policy, ledger |
| `R0126` | `C:\Users\ala\Documents\testport1\crates\swf-import\tests\frame_doc.rs` | 18307 | `994f1665cc0ad37f67e3afbc45d84e9f52f5906c7f69de89a7d6b2a07b8acb3b` | cadence, policy |
| `R0127` | `C:\Users\ala\Documents\testport1\crates\swf-import\tests\import.rs` | 5132 | `17cf161572e101709ebcb0934c7c370db6baf44dbd04683764e538031295be34` | policy, ledger |
| `R0128` | `C:\Users\ala\Documents\testport1\crates\swf-import\tests\placement.rs` | 10235 | `90f035ed901d867fa5d32202121f5ff1f4cff0d6dd2eff9c618065b21140e238` | policy |
| `R0129` | `C:\Users\ala\Documents\testport1\crates\swf-import\tests\stream.rs` | 5284 | `3f2f8a7e3dc8cfa50a6ad19dd79736d31fbf9d52a1bb94d563551e973667a357` | cadence, format, policy |
| `R0130` | `C:\Users\ala\Documents\testport1\crates\swf-import\tests\texels.rs` | 7408 | `8743ab456a78a9aab2b431b3857d95616cedcd21246cebc61a299374cbdcc399` | witness, policy, ledger |
| `R0131` | `C:\Users\ala\Documents\testport1\docs\AGENTS-PROPOSALS-2026-11-04.md` | 5079 | `eddbdbec7bd218331ac47dc196ef43bfe1a9af101d3922b95c440edb832beae4` | witness, civilians, cadence, health, policy |
| `R0132` | `C:\Users\ala\Documents\testport1\docs\CAMPAIGN-FRONTIER.md` | 5146 | `1172ba2fcd9da9965824903d10108362bf324ef34916ff12370ed026cc8c4e2e` | witness, civilians, format, policy, ledger |
| `R0133` | `C:\Users\ala\Documents\testport1\docs\CELL-ADDON-DECISION.md` | 7888 | `78099b226aa6f50a6f131ee2635f9a71fb3e854e0154ca85f23dc8817cfac77e` | witness, format, policy, ledger |
| `R0134` | `C:\Users\ala\Documents\testport1\docs\CELL-MEDIA-DECISION.md` | 7859 | `b1c2032dc2635dccc94925eed461b43f0ecee0f0bd2b0145348cb5386780fed2` | witness, policy |
| `R0135` | `C:\Users\ala\Documents\testport1\docs\CELL-MODEL.md` | 4908 | `0c09c7756253f0394bd20a23b9dea978c7db17c74d8e86b2211aac1b07839eb8` | health, policy |
| `R0136` | `C:\Users\ala\Documents\testport1\docs\CELL-PROGRAM-DECISION.md` | 8448 | `8750a12086d47074c1858c6e2feee73c28cccf8665719beb442cabde5c30c7e2` | witness, cadence, policy |
| `R0137` | `C:\Users\ala\Documents\testport1\docs\CELL-PROGRAM.md` | 4926 | `631bb27c8587994fb6e42da955873703cc7a5aeec3ded09f28ebab974060bd3a` | cadence, policy |
| `R0138` | `C:\Users\ala\Documents\testport1\docs\CELL-SCHEMA.md` | 22564 | `3b0c9ae053b46362498974eceee03154cec9350defeeb43e0cad984bff56bea6` | witness, civilians, cadence, format, client, policy |
| `R0139` | `C:\Users\ala\Documents\testport1\docs\CELL-TRANSPORT-DECISION.md` | 10771 | `8aa895f45d72fe5aabdcd355901b195d790e4b9ede88c1bde093d2d53b4b5080` | witness, format, policy, ledger |
| `R0140` | `C:\Users\ala\Documents\testport1\docs\cellular_generativity_axis_civilian_expectations.md` | 65183 | `fd6644efa7a3e6a8445face2836c2a13293305a7eff261c8a92d8f0a1e1f6ce9` | witness, civilians, cadence, health, client, policy, ledger |
| `R0141` | `C:\Users\ala\Documents\testport1\docs\cellular_generativity_axis_civilian_expectations_prototype_rechecked.md` | 144027 | `54fc32d39521819ac3886242d774967f89ca502c5e38a5f361d53aacb81427a8` | witness, civilians, cadence, health, format, mount, client, policy, ledger |
| `R0142` | `C:\Users\ala\Documents\testport1\docs\DECISIONS-PORT.md` | 11355 | `b2ed7514e593751aef5ef09a3d61ca712d3ffaa36c79ea66d3bf50d94e16a1d7` | witness, civilians, format, mount, policy, ledger |
| `R0143` | `C:\Users\ala\Documents\testport1\docs\MISSION-FRONTIER-2026-11-04.md` | 4202 | `8c51b08688b84d77e38e602b9d8b0f95bed08f0e9270937a113396c015f886e4` | witness, civilians, cadence, health, policy |
| `R0144` | `C:\Users\ala\Documents\testport1\docs\MISSION-QUESTIONS-220.md` | 16121 | `4e985b1e6cf727700a2a64e6a9baae154c468235144607dd69f951b4ee85cbfb` | witness, civilians, cadence, health, format, policy, ledger |
| `R0145` | `C:\Users\ala\Documents\testport1\docs\OWNERSHIP-AUDIT-2026-11-04-family-branches-and-v2.md` | 6546 | `514a1ec6ab1fcb4459020df587a67337ed0f9ac9e479017adf32bf5b953a300e` | witness, civilians, cadence |
| `R0146` | `C:\Users\ala\Documents\testport1\docs\PACKAGE-OWNERSHIP.md` | 17131 | `1ccfc25618f12dd28900c4cbf94a5ecad87227ed7bf47f51f45ede57bb77dbaf` | witness, cadence, format, mount, policy, ledger |
| `R0147` | `C:\Users\ala\Documents\testport1\docs\PORT-BASELINE.md` | 7831 | `031ff44b82ab3ac5fc9b4046f625c445d291a2d7a67d86aef27d70e94e12af31` | witness, civilians, format, policy, ledger |
| `R0148` | `C:\Users\ala\Documents\testport1\docs\RULING-INDEX.md` | 6088 | `48fae169f20f1d3d870c4c3dc1c3c20842509323379c528888e19f5b5c4f32d2` | witness, policy, ledger |
| `R0149` | `C:\Users\ala\Documents\testport1\docs\SCOPE-ACCOUNTING.md` | 13472 | `b8f5d2c36aec0035140e668d37927989a4ec4f9b93e5fdfbf6cf6c20770d5fbd` | witness, civilians, cadence, format, mount, policy, ledger |
| `R0150` | `C:\Users\ala\Documents\testport1\docs\SWF_CELL_PACKAGE_IMPLEMENTATION_PLAN_v3.md` | 98312 | `144499555d4f215d0941b20ee7f939de60211aa411fe779da42b44881725e506` | witness, civilians, cadence, format, mount, policy, ledger |
| `R0151` | `C:\Users\ala\Documents\testport1\docs\testport1_plan_resynthesis.md` | 23044 | `144930909e72d74ca4dc1b6b6d15da5a7f9f3c4ba891337e405b41d01ab86fbd` | witness, cadence, format, mount, policy, ledger |
| `R0152` | `C:\Users\ala\Documents\testport1\docs\TICK-CADENCE.md` | 5457 | `4c29d33722f41c9be7b8cb9b1aea7dc55bac1ec56f6b3e5e9c37e742682bf3bb` | witness, cadence |
| `R0153` | `C:\Users\ala\Documents\testport1\generated\vendor-swf\autocfg\README.md` | 3792 | `1c6c43f1d22ab1c6411b82862c356c550947f3cecbb4c7eede5edefc8890ff32` | policy |
| `R0154` | `C:\Users\ala\Documents\testport1\generated\vendor-swf\bitflags\SECURITY.md` | 690 | `68704c8128fa2e776ed7cbda741fbf61ad52f998a96350ee7ee4dbf64c6573bc` | policy |
| `R0155` | `C:\Users\ala\Documents\testport1\generated\vendor-swf\bitflags\src\lib.rs` | 36325 | `f8d141a1ba6b1996b33eb34669786ef389d4d5226edad46cec22a561588c324b` | policy |
| `R0156` | `C:\Users\ala\Documents\testport1\generated\vendor-swf\bitstream-io\src\lib.rs` | 123896 | `f0a975d992812b184aff0bff084364a351154ae903808a828c2c25cbcd9f67f2` | format |
| `R0157` | `C:\Users\ala\Documents\testport1\generated\vendor-swf\byteorder\README.md` | 2147 | `2f2d64924c35b7203e3e3f3d136fcb714281762d145ca3513246da5547b1d014` | policy |
| `R0158` | `C:\Users\ala\Documents\testport1\generated\vendor-swf\cfg-if\src\lib.rs` | 6626 | `2fe40504f7a897ac6b742a85bdf8c4b5b2c6de87cdd72d0cf49fa50585ac9955` | policy |
| `R0159` | `C:\Users\ala\Documents\testport1\generated\vendor-swf\encoding_rs\README.md` | 39281 | `a05287b32364f0f7944ed4aa542a12f1bfc98ef0ae03d53fd479ed87eb1716f3` | policy |
| `R0160` | `C:\Users\ala\Documents\testport1\generated\vendor-swf\encoding_rs\src\handles.rs` | 69367 | `d8867395e9b5dba942554173c0c8cc99a390dcac27749927fa55e4172114b248` | policy |
| `R0161` | `C:\Users\ala\Documents\testport1\generated\vendor-swf\encoding_rs\src\lib.rs` | 266756 | `b35a1fc8258216abeebff4f56e384363440afdbb4ac5853e30d861b6971a91d6` | cadence, policy |
| `R0162` | `C:\Users\ala\Documents\testport1\generated\vendor-swf\encoding_rs\src\macros.rs` | 76196 | `41fc50d83a9a47b7408d25c9273a55ef87477a274bbfb89e0d2a34fb39c8cae7` | policy |
| `R0163` | `C:\Users\ala\Documents\testport1\generated\vendor-swf\encoding_rs\src\mem.rs` | 127224 | `e505e78fa5562e03cb4c1f346a7178263d92711ff545aa1d4f5a0e41642fba92` | policy |
| `R0164` | `C:\Users\ala\Documents\testport1\generated\vendor-swf\encoding_rs\src\single_byte.rs` | 39246 | `323e2374302004abbd907b2ec63c1e565b436b7e9632ba6fc52fe2c12df454ae` | policy |
| `R0165` | `C:\Users\ala\Documents\testport1\generated\vendor-swf\encoding_rs\src\test_labels_names.rs` | 15992 | `23a2e11b02b3b8d15fb5613a625e3edb2c61e70e3c581abfd638719a4088200d` | cadence |
| `R0166` | `C:\Users\ala\Documents\testport1\generated\vendor-swf\encoding_rs\src\utf_16.rs` | 20303 | `675f6b28381aa0f31e6df1abfd6fe4fdc447b68028bb7b68a4cd78aa8d2e3c9c` | policy |
| `R0167` | `C:\Users\ala\Documents\testport1\generated\vendor-swf\encoding_rs\src\utf_8.rs` | 69212 | `d8285a95643304f55afa7aeffda23a94a317e339f0863c54ef7fb75b41d17369` | policy |
| `R0168` | `C:\Users\ala\Documents\testport1\generated\vendor-swf\enum-map\CHANGELOG.md` | 5952 | `d64d088715bcbff31fb85a6694fbbaef2802ab19ff91d5f0d71ac715d1fa4417` | policy |
| `R0169` | `C:\Users\ala\Documents\testport1\generated\vendor-swf\enum-map\README.md` | 868 | `eec9d4461de2e1e0f26251a98fd53feaad8582e6614a5a23be17a5b0c9491637` | policy |
| `R0170` | `C:\Users\ala\Documents\testport1\generated\vendor-swf\enum-map-derive\src\derive_enum.rs` | 6898 | `fc478b32e580dabfa31f71db2958faf05125e58b17bf420a881930d96e76ce11` | format |
| `R0171` | `C:\Users\ala\Documents\testport1\generated\vendor-swf\flate2\README.md` | 4087 | `f14e438f37a22eb8b81a1160b7dd15b8e37a2fdbcb32e729e00b9e639b370a66` | policy |
| `R0172` | `C:\Users\ala\Documents\testport1\generated\vendor-swf\log\CHANGELOG.md` | 23648 | `95a2ad3bf035ce64b29208dbe79e8f81c19226a05c3e2348a52b10f7d967f56c` | policy |
| `R0173` | `C:\Users\ala\Documents\testport1\generated\vendor-swf\lzma-rs\CHANGELOG.md` | 2953 | `5678b69d915d026abc0aee1a68814f5e808f173a492a051b96766f55e8cb4532` | policy |
| `R0174` | `C:\Users\ala\Documents\testport1\generated\vendor-swf\lzma-rs\src\decode\xz.rs` | 13793 | `058bcfcf48f9d5a1563a4362b6ca7149e9d6dc41ab49e867a931d392c09c142c` | format, ledger |
| `R0175` | `C:\Users\ala\Documents\testport1\generated\vendor-swf\lzma-rs\src\encode\xz.rs` | 4737 | `96b0fdffdc2cdd30104c69e0edcce8c5b4333055290ceb3f7da5b9e9ff49c99c` | format |
| `R0176` | `C:\Users\ala\Documents\testport1\generated\vendor-swf\lzma-rs\src\xz\footer.rs` | 129 | `3ae9f1e888f43aba9ba4d683976ac3cdc18bdd1bf6e745e29bb5a471dead37fc` | format |
| `R0177` | `C:\Users\ala\Documents\testport1\generated\vendor-swf\lzma-rs\src\xz\header.rs` | 1591 | `c94c163289b33e005d8cd4b5ba7304a14538af2eab45d7c54c9076db56850342` | format |
| `R0178` | `C:\Users\ala\Documents\testport1\generated\vendor-swf\lzma-rs\src\xz\mod.rs` | 3193 | `6c1486eadbf25c7e1efeaa8b193104e56134cfdb934b13345560a258c5ebaab7` | ledger |
| `R0179` | `C:\Users\ala\Documents\testport1\generated\vendor-swf\memchr\.cargo-checksum.json` | 5550 | `7a772ae111fd9370fe127ad0d65c00ccbc5030fe37c84abc879a7b442e5ac6a0` | policy |
| `R0180` | `C:\Users\ala\Documents\testport1\generated\vendor-swf\memchr\AI_POLICY.md` | 1878 | `eb058d5b8387f03159cf6ef868100459d7e01f49499733028fcc916bc97c1cc4` | policy |
| `R0181` | `C:\Users\ala\Documents\testport1\generated\vendor-swf\memchr\CONTRIBUTING.md` | 210 | `f5b2b4a9a3dbcd9a6f2654eb97dd7135e6af3717b9a3f037a9cbf714e387af76` | policy |
| `R0182` | `C:\Users\ala\Documents\testport1\generated\vendor-swf\memchr\README.md` | 9870 | `92a74aaffe011bdaa06fbc34a01686a6eba58ca1322e976759417a547fddf734` | policy |
| `R0183` | `C:\Users\ala\Documents\testport1\generated\vendor-swf\memchr\src\arch\generic\memchr.rs` | 49244 | `ee2a77afcbf506655e352eb3cd42451a70cc2c39e3da487b2985638bc09ced3e` | format |
| `R0184` | `C:\Users\ala\Documents\testport1\generated\vendor-swf\memchr\src\arch\wasm32\simd128\packedpair.rs` | 8358 | `288ba6e5eee6a7a8e5e45c64cff1aa5d72d996c2a6bc228be372c75789f08e45` | policy |
| `R0185` | `C:\Users\ala\Documents\testport1\generated\vendor-swf\memchr\src\memmem\searcher.rs` | 39226 | `84f6a23bef907696cb672e6898c15fb87008058abc100dde58519d8ec5ebca5d` | policy |
| `R0186` | `C:\Users\ala\Documents\testport1\generated\vendor-swf\miniz_oxide\src\deflate\core.rs` | 100123 | `69224613e89fa46fe8f7429b374d27416ab05237682a12678ac58c6f253f6d09` | policy |
| `R0187` | `C:\Users\ala\Documents\testport1\generated\vendor-swf\miniz_oxide\src\inflate\stream.rs` | 17760 | `e6dd9e06e927dbe5a59299db1bc96bf1c55cad8ef995fccec314ecf056622884` | policy |
| `R0188` | `C:\Users\ala\Documents\testport1\generated\vendor-swf\no_std_io2\src\io\buffered.rs` | 37954 | `de21420d2296036071ee2ec67f02b14222adb1ae2e1691d9ccea72360f743f11` | policy |
| `R0189` | `C:\Users\ala\Documents\testport1\generated\vendor-swf\no_std_io2\src\io\error.rs` | 21544 | `abd1e373661df210211ff93596d3b523f6553543ea0d5528e22a4beed20c45a9` | policy |
| `R0190` | `C:\Users\ala\Documents\testport1\generated\vendor-swf\num-bigint\src\bigint.rs` | 37758 | `bbed782925af8f9a3c15a02f94154548df92f37aee6b8593597d192533f25c13` | policy |
| `R0191` | `C:\Users\ala\Documents\testport1\generated\vendor-swf\num-bigint\src\biguint\convert.rs` | 26282 | `f4daf2e5e48fc5f9cd91d70f35574aca00ed27ced8e63f56dcc216dc6fb97dbc` | policy |
| `R0192` | `C:\Users\ala\Documents\testport1\generated\vendor-swf\num-derive\src\lib.rs` | 33761 | `dc254b4419136764ea0d5217e21cdbb8081142b6bc87a659c0d285573aebb181` | policy |
| `R0193` | `C:\Users\ala\Documents\testport1\generated\vendor-swf\num-integer\src\average.rs` | 2548 | `72f041da3ede7913c7ed8620f21075396671fba6cd9aeb98ec907db1be8fe699` | format, policy |
| `R0194` | `C:\Users\ala\Documents\testport1\generated\vendor-swf\powerfmt\README.md` | 2305 | `188fa8a1323086828b9eeaf5a2031d66f066b617fc7dec318835a685d7c2e3c7` | policy |
| `R0195` | `C:\Users\ala\Documents\testport1\generated\vendor-swf\powerfmt\src\smart_display.rs` | 24452 | `78a107b9b3cf812db19788697f66467a5931833471ffabd52e93a1553d2334d9` | policy |
| `R0196` | `C:\Users\ala\Documents\testport1\generated\vendor-swf\proc-macro2\README.md` | 3864 | `8eebdcf2f9a5034693589a9982adf06c2aac5c9f078c07a44400d293ed5b4a8e` | policy |
| `R0197` | `C:\Users\ala\Documents\testport1\generated\vendor-swf\proc-macro2\src\lib.rs` | 51164 | `ed6bf5e3c3b4fc952d4bdf9b48b149087bceaebf5392befce0bc6cae590a008d` | policy |
| `R0198` | `C:\Users\ala\Documents\shploingus-clean\AGENT-language.md` | 2061 | `105389b13c66b00ff0e372d9ccd7f2fad44dd964186162b08f2c611811e33183` | policy |
| `R0199` | `C:\Users\ala\Documents\shploingus-clean\Cargo.toml` | 3743 | `9c805923b177fa29a405a607a43dfc01c95a860f67090e24b219165b55e3f69f` | civilians, policy, ledger |
| `R0200` | `C:\Users\ala\Documents\shploingus-clean\IDEA.md` | 128 | `24cf565774a6235a1dd0418f80557e285b46d53b57494ac2ae40b4cacf5b7599` | cadence |
| `R0201` | `C:\Users\ala\Documents\shploingus-clean\README.md` | 5898 | `6b5f23d19f1bb9d9c2746ecd8dc782d09c96e3b5a01dc8aaa2b0171684de463f` | cadence, policy, ledger |
| `R0202` | `C:\Users\ala\Documents\shploingus-clean\README.new.md` | 13134 | `83ac55670d0955702d96b3fcf8fa1a82283d50cb35133cc63a665041998f3583` | cadence, policy, ledger |
| `R0203` | `C:\Users\ala\Documents\shploingus-clean\refusal_timeline.md` | 156343 | `d51b98c035bb69bc5e1765cfd4e6d493c3afc2894bda8a8363438f9b9f8b2abf` | witness, cadence, policy, ledger |
| `R0204` | `C:\Users\ala\Documents\shploingus-clean\rust-toolchain.toml` | 1483 | `bfe7820a9761424fad4da3393824d5c1050dad9937a6526045a7e0a6b6f362eb` | ledger |
| `R0205` | `C:\Users\ala\Documents\shploingus-clean\RUST_PORTING_RECOVERY_PROMPT_V2.md` | 87732 | `b8c5a48bcbed702f2df31aee99707dbc8c838d76c4e93b11743da7a498fa80e8` | cadence, health, policy, ledger |
| `R0206` | `C:\Users\ala\Documents\shploingus-clean\skills-lock.json` | 1432 | `b422c591160491aab118090481f725113a0a084a5db7e4252750f9811c741bc9` | client |
| `R0207` | `C:\Users\ala\Documents\shploingus-clean\u8_docs.py` | 16552 | `b7a6643b48b7e6ba9bda8b074cad3aa0d92231692dd4c147cbcccd2f57372b4b` | policy, ledger |
| `R0208` | `C:\Users\ala\Documents\shploingus-clean\VOWS.md` | 4655 | `4f40300fe90b3ee9c2051e5bc2f4ff92e12ed7963afbe150b8ddb50da7cb3620` | policy, ledger |
| `R0209` | `C:\Users\ala\Documents\shploingus-clean\.agents\skills\diffusion-ledger-v3-audit\SKILL.md` | 1749 | `e81fb8d291211d2d0cefb1e6fed6f45754e18d4d6065cfb7b9ae95e82dbdeacb` | ledger |
| `R0210` | `C:\Users\ala\Documents\shploingus-clean\.agents\skills\rust-patterns\SKILL.md` | 13500 | `51379df2bd92a482309e109e5a210210842594f660cceeb2d68d18e995108edf` | policy |
| `R0211` | `C:\Users\ala\Documents\shploingus-clean\.agents\skills\rust-skills\CONTRIBUTING.md` | 2682 | `5eeffebc7a3f79d4cb6ed1f5d0f91778cda9740a249fa491d75ae14371d02b1f` | policy |
| `R0212` | `C:\Users\ala\Documents\shploingus-clean\.agents\skills\rust-skills\SKILL.md` | 38324 | `33348f323ff54bbfa4a9c4d478a3d3ac41cf3c750263a2b973d963422ed5ff51` | policy |
| `R0213` | `C:\Users\ala\Documents\shploingus-clean\.agents\skills\rust-skills\checks\check.sh` | 1256 | `073a77ca8a5b4340c04b9243c215c5cb9bd05d97aa3b40aaf0e894478d27443d` | policy |
| `R0214` | `C:\Users\ala\Documents\shploingus-clean\.agents\skills\rust-skills\checks\README.md` | 2796 | `319418ca475b1c2c0d286065c924c6abc8bc4139452225c1dacc65b2bf4a06ea` | policy |
| `R0215` | `C:\Users\ala\Documents\shploingus-clean\.agents\skills\rust-skills\rules\anti-empty-catch.md` | 3266 | `64398f2684abb441f91cbc4238766c0c54d4e34312f76e3391df7c92a5672da3` | policy |
| `R0216` | `C:\Users\ala\Documents\shploingus-clean\.agents\skills\rust-skills\rules\anti-unwrap-abuse.md` | 3566 | `96cde512a6bddd1a577854861ae9b3c94ecdb2d1246593d38c3d6c03d3997a0f` | policy |
| `R0217` | `C:\Users\ala\Documents\shploingus-clean\.agents\skills\rust-skills\rules\api-impl-fromiterator.md` | 3602 | `f23325d3a0dc3f4742dca30e22d3f0c57b3eda44c3aab87d8b97757e603d2a03` | policy |
| `R0218` | `C:\Users\ala\Documents\shploingus-clean\.agents\skills\rust-skills\rules\async-select-racing.md` | 4871 | `b60587e3ecec80969fbff2c8bc4c1560eca1e871ab2e9897362aa772029d0403` | cadence |
| `R0219` | `C:\Users\ala\Documents\shploingus-clean\.agents\skills\rust-skills\rules\const-block.md` | 3039 | `499a6444be4bb909d1b3e5f978354b30847064582f966de06d431ce790cf5fbc` | format |
| `R0220` | `C:\Users\ala\Documents\shploingus-clean\.agents\skills\rust-skills\rules\const-fn.md` | 2249 | `2db2e2ad331f98fe64ad38be497611f8bb1f3d2fa757bd073b9a33eeddd5dcc9` | format |
| `R0221` | `C:\Users\ala\Documents\shploingus-clean\.agents\skills\rust-skills\rules\const-vs-static.md` | 2907 | `09465597c9d54be299eed57a5795c33c7a5c6722294e97f8e56daba0ac1f6ca7` | format |
| `R0222` | `C:\Users\ala\Documents\shploingus-clean\.agents\skills\rust-skills\rules\doc-errors-section.md` | 3441 | `de61214d32794f6fe5cd32a31b9ab7c8a96d7c6e46d4bcb2af6aff1daf85960c` | policy |
| `R0223` | `C:\Users\ala\Documents\shploingus-clean\.agents\skills\rust-skills\rules\doc-hidden-setup.md` | 3780 | `1ea01b1adfbf39a8f4a38aed0b0ba113b396e7d1ea2b351ac3b5ee118403f7b7` | format |
| `R0224` | `C:\Users\ala\Documents\shploingus-clean\.agents\skills\rust-skills\rules\err-context-chain.md` | 3682 | `8e6366a1ca24890bdc010e1dd50bd32924d41134608e384d464b8657d753b72b` | policy |
| `R0225` | `C:\Users\ala\Documents\shploingus-clean\.agents\skills\rust-skills\rules\err-lowercase-msg.md` | 3489 | `a0fa3590b0eaf52f65392964b00b0422a2db99f61af1201cd49fb8c37d951b23` | policy |
| `R0226` | `C:\Users\ala\Documents\shploingus-clean\.agents\skills\rust-skills\rules\err-no-unwrap-prod.md` | 3324 | `32a10b6eea88dded632b75dd469c02466c4d8c26fddd4a9cf319d9e44c01999d` | policy |
| `R0227` | `C:\Users\ala\Documents\shploingus-clean\.agents\skills\rust-skills\rules\err-question-mark.md` | 3534 | `a6c412d50ebf1d89df55701af543117033f36a29e8f51c65c16a8fc33eb3619c` | policy |
| `R0228` | `C:\Users\ala\Documents\shploingus-clean\.agents\skills\rust-skills\rules\err-result-over-panic.md` | 3612 | `0ea5704f1aa8717c41934fce42e7945ae3260cd1f52f1af24ffea6bc1acb2790` | policy |
| `R0229` | `C:\Users\ala\Documents\shploingus-clean\.agents\skills\rust-skills\rules\lint-cfg-check.md` | 2544 | `4988211b3935cd08c8e0950d4a37dc176aed0b1530d8f624d8d3f28409f46eb8` | policy |
| `R0230` | `C:\Users\ala\Documents\shploingus-clean\.agents\skills\rust-skills\rules\lint-pedantic-selective.md` | 3296 | `ae780028a9ffb23100546a496545f280603d92e0925b60f677be702f6d500cb0` | policy |
| `R0231` | `C:\Users\ala\Documents\shploingus-clean\.agents\skills\rust-skills\rules\mem-reuse-collections.md` | 4492 | `46c551e3a1f3d3d7605c51089c1568ff84d63775a5f9dd8cf25d751b55123298` | policy |
| `R0232` | `C:\Users\ala\Documents\shploingus-clean\.agents\skills\rust-skills\rules\name-is-has-bool.md` | 3367 | `7f27bd1dd809bd360b619038bac27bd81ab5e76b952834f0efe4f37b3c07f64a` | policy |
| `R0233` | `C:\Users\ala\Documents\shploingus-clean\.agents\skills\rust-skills\rules\num-overflow-explicit.md` | 2846 | `312897c64c398320834291c616f8079d6bbb569204823d00dd55556053c7cbf2` | policy |
| `R0234` | `C:\Users\ala\Documents\shploingus-clean\.agents\skills\rust-skills\rules\num-saturating-clamp.md` | 3241 | `a9079dfbe867c6212a5065dedf0a7ce39602d20dd58e3c990cf23050241a646a` | health |
| `R0235` | `C:\Users\ala\Documents\shploingus-clean\.agents\skills\rust-skills\rules\obs-error-chain.md` | 3556 | `7bbd1701a8925d55c4b78e991a37adbb953aa5ed56a4ad215a1d73ef0a23a8c3` | policy |
| `R0236` | `C:\Users\ala\Documents\shploingus-clean\.agents\skills\rust-skills\rules\obs-levels-filter.md` | 3524 | `4a2f516b09368cd828546b190f32866fb71f3ca672522673910e81b2b9efb5d3` | health |
| `R0237` | `C:\Users\ala\Documents\shploingus-clean\.agents\skills\rust-skills\rules\obs-no-sensitive-data.md` | 3663 | `95f125c8af87e586fb4f375e0558d01078e0af2d14774d43df7f8f84fb6e539e` | health |
| `R0238` | `C:\Users\ala\Documents\shploingus-clean\.agents\skills\rust-skills\rules\opt-bounds-check.md` | 4410 | `35a57843c614e6092bbda285ac986f287475d3b755c94fb2adc54e232ea06420` | format |
| `R0239` | `C:\Users\ala\Documents\shploingus-clean\.agents\skills\rust-skills\rules\opt-cold-unlikely.md` | 3729 | `ff6e6c354fc67d2965b250d88a1264fdabc53153a03706a54e867dc251199bc2` | policy |
| `R0240` | `C:\Users\ala\Documents\shploingus-clean\.agents\skills\rust-skills\rules\opt-target-cpu.md` | 4037 | `de7f32b9da85c979c8e2463cd45d45753c973fcf33c4e1be941554218a13a393` | policy |
| `R0241` | `C:\Users\ala\Documents\shploingus-clean\.agents\skills\rust-skills\rules\own-move-large.md` | 3600 | `0db996260224395d0f15e61b121fbec496360783c457b98ed2c53eb4745a5fdc` | cadence |
| `R0242` | `C:\Users\ala\Documents\shploingus-clean\.agents\skills\rust-skills\rules\pat-let-else.md` | 2134 | `fdba64de6d7434e3d6fc13cefdf3ed929d7e24f988d321e9967df9f5226cace1` | policy |
| `R0243` | `C:\Users\ala\Documents\shploingus-clean\.agents\skills\rust-skills\rules\perf-io-buffering.md` | 3959 | `5d26f0651014e20ad9a9669079f0a869e55d598b9bb6c3475fb86395cb8d5982` | policy |
| `R0244` | `C:\Users\ala\Documents\shploingus-clean\.agents\skills\rust-skills\rules\proj-feature-additive.md` | 2330 | `f1ea1913fceca398b30aeb39f826695d12255d61a10e7b95140b2afd45bf5f4c` | policy |
| `R0245` | `C:\Users\ala\Documents\shploingus-clean\.agents\skills\rust-skills\rules\proj-msrv-declare.md` | 2182 | `638056f62a98a14f4f0e77ef604fa8f3b1675955645a95a63898731512a9abc7` | policy |
| `R0246` | `C:\Users\ala\Documents\shploingus-clean\.agents\skills\rust-skills\rules\serde-rename-all.md` | 2258 | `eaf8b676fc3f33585ac5a06c07ac1cf05ab6323970e0fe1e3d203100088895fe` | policy |
| `R0247` | `C:\Users\ala\Documents\shploingus-clean\.agents\skills\rust-skills\rules\test-loom-concurrency.md` | 3511 | `f03ecf6ad449d6459f031f7fc4a73cd28847eecd22fefb9eada9200924817cab` | policy |
| `R0248` | `C:\Users\ala\Documents\shploingus-clean\.agents\skills\rust-skills\rules\trait-object-safety.md` | 3847 | `9554fd872adad5f88c292e7bc65126ca1bd63df4823d9c049778ccf2ba81ad8e` | policy |
| `R0249` | `C:\Users\ala\Documents\shploingus-clean\.agents\skills\rust-skills\rules\type-never-diverge.md` | 3386 | `09f83633ce9749c9d593032f5b3c4b42b78735513a1185d403f5c3e4681a41bb` | policy |
| `R0250` | `C:\Users\ala\Documents\shploingus-clean\.agents\skills\rust-skills\rules\type-result-fallible.md` | 3554 | `9b0e79ec2b8e42af95a7c880578f00e33bd85c076fa1d3cd729ce37a89d8c29a` | format |
| `R0251` | `C:\Users\ala\Documents\shploingus-clean\.agents\skills\rust-testing\SKILL.md` | 11798 | `02a9a40dcc42dd21d14730d29b13ee0a8b274694360585dc0fadb2602eb56ddf` | health |
| `R0252` | `C:\Users\ala\Documents\shploingus-clean\.agents\skills\typegpu\SKILL.md` | 22858 | `0c391fea0c8f7f56369780de950936bcd365687fc1c88d0e5639f3d6276b7d1d` | client |
| `R0253` | `C:\Users\ala\Documents\shploingus-clean\.agents\skills\typegpu\references\advanced.md` | 8504 | `efb5254647ca4cb5970b52790dc1dfb4961429364869d6da80ae96cd982e878e` | client |
| `R0254` | `C:\Users\ala\Documents\shploingus-clean\.agents\skills\typegpu\references\encoders.md` | 4476 | `783e22aec011f4c8c7af03c57ec22062b66c98945ab5d39c3352425f71e59271` | client |
| `R0255` | `C:\Users\ala\Documents\shploingus-clean\.agents\skills\typegpu\references\pipelines.md` | 14184 | `1615b694fd1ab9630bdb71fd09a379515623ba49b96f24f9f41f0e4a11898ec5` | client |
| `R0256` | `C:\Users\ala\Documents\shploingus-clean\.agents\skills\typegpu\references\react.md` | 5378 | `8e7eb08596502f3f10739592d464bc19394f064d7255532be0a639cd1229b061` | client |
| `R0257` | `C:\Users\ala\Documents\shploingus-clean\.agents\skills\typegpu\references\setup.md` | 8132 | `2bd6ed9f6e6a95992ad3571fbbcf6fca6e0df4479a528a2ced9445f07c3f9c39` | client |
| `R0258` | `C:\Users\ala\Documents\shploingus-clean\.agents\skills\typegpu\references\textures.md` | 7205 | `f87d2d37a8e3920602e7206808bc08ad64dcfbe494a90e38d8176fd27636edaf` | client |
| `R0259` | `C:\Users\ala\Documents\shploingus-clean\.agents\skills\typegpu\references\timing.md` | 4275 | `bed7115271cb542426d4fa443113210c39bc93d5ac5c64dddbaf1b570a055785` | client, policy |
| `R0260` | `C:\Users\ala\Documents\shploingus-clean\.agents\skills\webgpu\package-lock.json` | 41582 | `aa1bb2a34daefdd8a42ce15da1bea5e9e2e9bdb4c195a5986bd4df39dff10109` | client |
| `R0261` | `C:\Users\ala\Documents\shploingus-clean\.agents\skills\webgpu\package.json` | 777 | `2ae1e4de2b77b1e74da877cd1c587b02b06f1f3aa3892a5c384661ce3ee1b1a3` | client |
| `R0262` | `C:\Users\ala\Documents\shploingus-clean\.agents\skills\webgpu\README.md` | 1083 | `865487aace7e8d2c09cd47d94bf1e326aa36f67cdedcc51c10f018c4d20ac2ce` | client |
| `R0263` | `C:\Users\ala\Documents\shploingus-clean\.agents\skills\webgpu\SKILL.md` | 6956 | `9437d565e654c1a6048f7e20f3ac1e160ec34bea3514bb771d3046c4ae73f662` | cadence, client, policy |
| `R0264` | `C:\Users\ala\Documents\shploingus-clean\.agents\skills\webgpu\agents\claude.md` | 1562 | `1812b492f23a6538ab65985a70a1ff3d5900d0cac02df02b32938663f4fc8e90` | client |
| `R0265` | `C:\Users\ala\Documents\shploingus-clean\.agents\skills\webgpu\agents\openai.yaml` | 247 | `faef2f3128a676a063b5b5ca4ac94d7526335d5529d566bcfc0a693176ac4f0d` | client |
| `R0266` | `C:\Users\ala\Documents\shploingus-clean\.agents\skills\webgpu\assets\starter\package.json` | 303 | `9df5403337e2e073cc328dba3ba2a814aca0aa7b784e7a9d655f0bf0faf0fb77` | client |
| `R0267` | `C:\Users\ala\Documents\shploingus-clean\.agents\skills\webgpu\assets\starter\tsconfig.json` | 473 | `390b91260ae73520c93f3175215ac9507a27f6052785f4e83189114b56717480` | client |
| `R0268` | `C:\Users\ala\Documents\shploingus-clean\.agents\skills\webgpu\assets\starter\src\gpu.ts` | 3449 | `19f931ee402d333c3d7833388c7ba78652c62a2b0614146c6ed0cd9c3ac7997e` | client |
| `R0269` | `C:\Users\ala\Documents\shploingus-clean\.agents\skills\webgpu\assets\starter\src\main.ts` | 9669 | `44308ccc81524111a0d52b671fb7ced59dea8ebe7e61796a7be3faf349ff51ba` | client |
| `R0270` | `C:\Users\ala\Documents\shploingus-clean\.agents\skills\webgpu\references\compatibility.md` | 3259 | `7dca031b47560ef753f1ac5bb763aabff7551b17acf900e947f0f08b5e0706e3` | client |
| `R0271` | `C:\Users\ala\Documents\shploingus-clean\.agents\skills\webgpu\references\compute-patterns.md` | 5304 | `e5d6e35fde7d68ff608b4aadc9a320e102d64dcc6c350b77ac881a08afdbda82` | policy |
| `R0272` | `C:\Users\ala\Documents\shploingus-clean\.agents\skills\webgpu\references\creative-recipes.md` | 4194 | `45ff164aa849cc1366004ebd661ef6b554a91233cb7f0308fdffedaf885151b9` | cadence, client, policy |
| `R0273` | `C:\Users\ala\Documents\shploingus-clean\.agents\skills\webgpu\references\current-sources.md` | 2177 | `563a53f2683bf77eabcc147582dbf13d98f22b47f39e8885ff0987dfd8f7c801` | client |
| `R0274` | `C:\Users\ala\Documents\shploingus-clean\.agents\skills\webgpu\references\debugging-and-performance.md` | 5488 | `4c3583904d4c842fb32c15abf0b4ce47b84924c6d4d49fa96062499551b6c6d4` | policy |
| `R0275` | `C:\Users\ala\Documents\shploingus-clean\.agents\skills\webgpu\references\initialization-and-lifecycle.md` | 6211 | `8639366d21a5c414b9cf21fc840cff5157510d57cee01087532ee3a19e5bdab2` | client |
| `R0276` | `C:\Users\ala\Documents\shploingus-clean\.agents\skills\webgpu\references\rendering-patterns.md` | 4737 | `93a710a45cb50663f4dba33a44c76160638ec13914b9f0f0e61160d6588f7363` | policy |
| `R0277` | `C:\Users\ala\Documents\shploingus-clean\.agents\skills\webgpu\references\wgsl-data-layout.md` | 4753 | `67368c195dd4d01ea6a33e79ba0497cfdc406a9a0c72bc03ad5a6b36d43eb0da` | policy |
| `R0278` | `C:\Users\ala\Documents\shploingus-clean\.agents\skills\webgpu\scripts\validate.mjs` | 4231 | `f71fc9b5afbdbab4ec837b3576ee2d72b893be06fa6a8f72d79ba50105bd5b1c` | client |
| `R0279` | `C:\Users\ala\Documents\shploingus-clean\.agents\skills\webgpu-threejs-tsl\REFERENCE.md` | 9424 | `edafd601d82a6b998ac088f54e421d37e72b8f8c0fd206c9e7c15fed76e23896` | client, policy |
| `R0280` | `C:\Users\ala\Documents\shploingus-clean\.agents\skills\webgpu-threejs-tsl\SKILL.md` | 3295 | `b76648d2e2c699527448bc0a6cb06b7574ca2ed73dae1bf7d30b27caa7944730` | client |
| `R0281` | `C:\Users\ala\Documents\shploingus-clean\.agents\skills\webgpu-threejs-tsl\docs\compute-shaders.md` | 16218 | `25d57a1bb008c41bc251bd2824527758911649a911cc47132cac45fa718c9e71` | client, policy |
| `R0282` | `C:\Users\ala\Documents\shploingus-clean\.agents\skills\webgpu-threejs-tsl\docs\core-concepts.md` | 11466 | `9a37d4fc2afbc10110e0b40be84567a261edd81f8ea0c081a978cef24decd323` | client, policy |
| `R0283` | `C:\Users\ala\Documents\shploingus-clean\.agents\skills\webgpu-threejs-tsl\docs\device-loss.md` | 9557 | `415228967ca79d533efa413d5dcc68e3ad344ef14da0cc62ecd40bdf574ee4fd` | client, policy |
| `R0284` | `C:\Users\ala\Documents\shploingus-clean\.agents\skills\webgpu-threejs-tsl\docs\limits-and-features.md` | 5150 | `45e6e25603a8bfe55f68923526d3175c4b95c6bfc8aa65fbe52df5912bf66590` | client |
| `R0285` | `C:\Users\ala\Documents\shploingus-clean\.agents\skills\webgpu-threejs-tsl\docs\materials.md` | 9139 | `9a1ee8ed3a238bcdc073f937fe9eac1235df2dbfee3bfcb8c1f227d76238b991` | client |
| `R0286` | `C:\Users\ala\Documents\shploingus-clean\.agents\skills\webgpu-threejs-tsl\docs\post-processing.md` | 13814 | `d9afabc7cf19710ed6352c1d53f5cbd90154a4ae9ee9f896618ae177b70ab279` | client |
| `R0287` | `C:\Users\ala\Documents\shploingus-clean\.agents\skills\webgpu-threejs-tsl\docs\wgsl-integration.md` | 6916 | `30108fff6dd8d9078682a7fb9163fa8df0ff78365fe6120cd7931c85b4ece00c` | client |
| `R0288` | `C:\Users\ala\Documents\shploingus-clean\.agents\skills\webgpu-threejs-tsl\examples\basic-setup.js` | 2366 | `ce138a7c0d627a6354c0657ebf9cbf01fb0afa8ef8a63cd4b7ebf909db72513f` | client |
| `R0289` | `C:\Users\ala\Documents\shploingus-clean\.agents\skills\webgpu-threejs-tsl\examples\custom-material.js` | 4421 | `48cce35b42eccf9c146254d8e1ee9966e1aa797bc8959b1c694a2c08ad69c919` | client |
| `R0290` | `C:\Users\ala\Documents\shploingus-clean\.agents\skills\webgpu-threejs-tsl\examples\earth-shader.js` | 8860 | `d452143d931f6edb12c1835469394c93fb417f8c0b3d0e9d97c9289e2b8e3a8b` | client |
| `R0291` | `C:\Users\ala\Documents\shploingus-clean\.agents\skills\webgpu-threejs-tsl\examples\particle-system.js` | 7597 | `0cee121c0139d5d89740a6ba726d13518208b2bd0e17e8ed4fb40964e2b4ac9f` | client, policy |
| `R0292` | `C:\Users\ala\Documents\shploingus-clean\.agents\skills\webgpu-threejs-tsl\examples\post-processing.js` | 5400 | `5e48d91a4c1c5e15dd3bb62539208d0ee93d6b2e6758413f957202b5545a4140` | client |
| `R0293` | `C:\Users\ala\Documents\shploingus-clean\.agents\skills\webgpu-threejs-tsl\templates\compute-shader.js` | 9816 | `9d375479593981b80df23fb47234777dc6552a430cae987f69d8a4410ab8ada4` | client, policy |
| `R0294` | `C:\Users\ala\Documents\shploingus-clean\.agents\skills\webgpu-threejs-tsl\templates\webgpu-project.js` | 6595 | `cdccec6ee26adef81e2ba84aec36374adb34231b134685ca4cefe536a39c8cd8` | client |
| `R0295` | `C:\Users\ala\Documents\shploingus-clean\.cargo\config.toml` | 6870 | `a3a67263c7d1f434df1b163ead0d4f20784bbbd739b3dfc8f5e90c9315c7aa87` | policy |
| `R0296` | `C:\Users\ala\Documents\shploingus-clean\.freebuff\ledger-compact-part1.md` | 13787 | `4c3ddebc2d538364d95abffa4bc4af5a2e0f57adbb7891d3e1816d09e03db5f3` | cadence, policy, ledger |
| `R0297` | `C:\Users\ala\Documents\shploingus-clean\.freebuff\ledger-compact-part2.md` | 24406 | `41205e7b923c90be20f1566194cb1a72c16bcd2856656ab46bf5953e834ce838` | witness, civilians, cadence, policy, ledger |
| `R0298` | `C:\Users\ala\Documents\shploingus-clean\.freebuff\ledger-compact-part3.md` | 20802 | `2863007da71c44318ec4b787728c1094f4af1cb2494c2319e94c037759fa81b0` | cadence, health, client, policy, ledger |
| `R0299` | `C:\Users\ala\Documents\shploingus-clean\.freebuff\ledger-digest.md` | 218621 | `d1f3251dbf8e404bd8ec564b5e41807fe1e04c858bc1e18be3d8cffddf60539d` | witness, civilians, cadence, health, format, client, policy, ledger |
| `R0300` | `C:\Users\ala\Documents\shploingus-clean\.superpowers\sdd\hyper-greedy-block-level-remeshing\progress.md` | 1541 | `e3ec1e099fc1b9e231b5c4342e08664fc6fa3a80c91cd93ae27c1f0f978adf71` | ledger |
| `R0301` | `C:\Users\ala\Documents\shploingus-clean\.superpowers\sdd\hyper-greedy-block-level-remeshing\task-1-brief.md` | 2564 | `2351af5e37705a79fc04b60df47cbf711a54520cbf97dc196938a2107ea9a4ac` | policy |
| `R0302` | `C:\Users\ala\Documents\shploingus-clean\clean-room\Cargo.toml` | 4128 | `3998b0855927c3918e75c422ecdd2eca797cb9823597b83e8f4d717e4d630ad1` | policy, ledger |
| `R0303` | `C:\Users\ala\Documents\shploingus-clean\clean-room\README.md` | 65982 | `58da21a4e1c12e9ef6f19852e04af7dcb57b313a3d135568a9efe4760a92590a` | witness, civilians, cadence, policy, ledger |
| `R0304` | `C:\Users\ala\Documents\shploingus-clean\clean-room\.specify\memory\constitution.md` | 6766 | `d24bf69ff81ece07c932bdba46ea153239204e206e74440c0d52cc9919090a76` | witness, cadence, policy, ledger |
| `R0305` | `C:\Users\ala\Documents\shploingus-clean\clean-room\.specify\templates\checklist-template.md` | 2033 | `856532b3cb66171c662cc16f16b31a5856e4655a8666aad1e545bbfc7f603ca1` | policy |
| `R0306` | `C:\Users\ala\Documents\shploingus-clean\clean-room\.specify\templates\plan-template.md` | 3682 | `7e637502d41eccf0ca672496636365691fdca62ef37b27ec07fcb412dbfa90d4` | policy |
| `R0307` | `C:\Users\ala\Documents\shploingus-clean\clean-room\.specify\workflows\speckit\workflow.yml` | 2118 | `177761c5e7df28126beea043b5cb45aeaf7958090c022dc11ac71399422fcfbc` | policy |
| `R0308` | `C:\Users\ala\Documents\shploingus-clean\clean-room\specs\001-presentation\plan.md` | 2929 | `f3ed1a2de5eb1be4580b3bb5e41fda0fabdc7cf8924f0b43ab18f33c44b2b1f6` | witness, policy |
| `R0309` | `C:\Users\ala\Documents\shploingus-clean\clean-room\specs\001-presentation\spec.md` | 6159 | `b0d55a64e528975d99e3ed6877ad13abcd3f1a7a259f7bd194d87c76adfbb01d` | witness, policy, ledger |
| `R0310` | `C:\Users\ala\Documents\shploingus-clean\clean-room\specs\001-presentation\tasks.md` | 3512 | `409cffaae9bbcfc613942519bb7944fbbe4edf5182f66f274cf555305103e306` | cadence, policy |
| `R0311` | `C:\Users\ala\Documents\shploingus-clean\clean-room\specs\002-world\plan.md` | 4518 | `ceecae66399fe531cbb595c023c58ba91ac3fb3491e58373944c81acb3be48a0` | witness, cadence, policy, ledger |
| `R0312` | `C:\Users\ala\Documents\shploingus-clean\clean-room\specs\002-world\spec.md` | 9833 | `8260ce88cae444193522637c020cd4e50fb277c7c63aa4f0caa04ef917f2b46d` | witness, civilians, cadence, client, policy, ledger |
| `R0313` | `C:\Users\ala\Documents\shploingus-clean\clean-room\specs\002-world\tasks.md` | 5486 | `825de1b18ff013dfff11e5a5b9a7358db17a15a70ab927562f8f4d1d584ae805` | civilians, cadence, policy |
| `R0314` | `C:\Users\ala\Documents\shploingus-clean\clean-room\specs\003-u3-shapers\data-model.md` | 6098 | `33d6a3198ada6b70913e4b4747140c761dc8e8b31663fe4d7489ae5ce2f3b4e4` | cadence, policy, ledger |
| `R0315` | `C:\Users\ala\Documents\shploingus-clean\clean-room\specs\003-u3-shapers\plan.md` | 7343 | `8e3696e89af177c88293d0d3e0b05164a9d431d0632a24228f327f92da111190` | witness, cadence, policy, ledger |
| `R0316` | `C:\Users\ala\Documents\shploingus-clean\clean-room\specs\003-u3-shapers\quickstart.md` | 7333 | `28372205957f98fd7d48eae9ad2497d43bc0a8ad00c24dc4ac9706d0b93bc7d9` | cadence, policy, ledger |
| `R0317` | `C:\Users\ala\Documents\shploingus-clean\clean-room\specs\003-u3-shapers\research.md` | 6332 | `fd3db30a5483169744f461a1b9e3ef637d6d1a3fd654137e1fe5425e334e4424` | cadence, policy |
| `R0318` | `C:\Users\ala\Documents\shploingus-clean\clean-room\specs\003-u3-shapers\spec.md` | 16815 | `cd0b9ebabef8e653da0e839b266c8d786153434e4e164594b9a0dd213bcefa23` | cadence, policy, ledger |
| `R0319` | `C:\Users\ala\Documents\shploingus-clean\clean-room\specs\003-u3-shapers\tasks.md` | 19849 | `dd397cf15c25f2955b2a3aa23d052e62680bdeeeef8812cc746f54055d23cbab` | cadence, policy, ledger |
| `R0320` | `C:\Users\ala\Documents\shploingus-clean\clean-room\specs\003-u3-shapers\checklists\requirements.md` | 4364 | `61a94107d46874a4d1f83c4375245f55b9b24dfafeb12da06719e03871eb0d3b` | policy |
| `R0321` | `C:\Users\ala\Documents\shploingus-clean\clean-room\specs\003-u3-shapers\contracts\u3-seams.md` | 10188 | `99e62685fcf0f5e25fdeb41930d682442958af5bffbe55dde493ab5b42ccdf16` | cadence, policy, ledger |
| `R0322` | `C:\Users\ala\Documents\shploingus-clean\clean-room\specs\004-u4-mesh-stream-work\data-model.md` | 4436 | `e459464d9b8c0e2fa2d6fdc06dc56cb8c7aae2055b1084080a291311523e98e6` | cadence, policy, ledger |
| `R0323` | `C:\Users\ala\Documents\shploingus-clean\clean-room\specs\004-u4-mesh-stream-work\plan.md` | 10042 | `498c0d1609ad2de522eedd9145e163c4bc6c8761e48a54c6474b675b978d3312` | witness, cadence, policy, ledger |
| `R0324` | `C:\Users\ala\Documents\shploingus-clean\clean-room\specs\004-u4-mesh-stream-work\quickstart.md` | 12682 | `ca00f1bef771d7394ab82a243b34257b031144d015ce5f4d1107abfb08d3d430` | cadence, policy, ledger |
| `R0325` | `C:\Users\ala\Documents\shploingus-clean\clean-room\specs\004-u4-mesh-stream-work\research.md` | 9433 | `9cf464a5cd079b9dcdec8e7aaa02daf6962086d92aee4d89296a56814330bf52` | cadence, policy, ledger |
| `R0326` | `C:\Users\ala\Documents\shploingus-clean\clean-room\specs\004-u4-mesh-stream-work\spec.md` | 16158 | `23d9a0c49839328de5e08fc7b797a19ef8bb0f13f18fed8da35a13b257f1f304` | cadence, policy, ledger |
| `R0327` | `C:\Users\ala\Documents\shploingus-clean\clean-room\specs\004-u4-mesh-stream-work\tasks.md` | 10905 | `d9fe4697dcd277864d6750322f1b39c0c949e926103835a7ca15a42c716c9ea7` | witness, cadence, policy, ledger |
| `R0328` | `C:\Users\ala\Documents\shploingus-clean\clean-room\specs\004-u4-mesh-stream-work\checklists\requirements.md` | 5925 | `db87db1731d6ed3f5c8a97a66ba2c058b6fa9c4349544829dab24a7fcfae7af4` | cadence, policy, ledger |
| `R0329` | `C:\Users\ala\Documents\shploingus-clean\clean-room\specs\004-u4-mesh-stream-work\contracts\u4-seams.md` | 5825 | `719f4434c49ae2482d8d6ab5aefa6a7fe3f447ccfaa01cf13ae34648bf3346b5` | policy, ledger |
| `R0330` | `C:\Users\ala\Documents\shploingus-clean\clean-room\specs\005-u6-record-api\data-model.md` | 6047 | `f6755be90152cfa326d0080dc2f6aed193c8ec437af6778e926a2e2ea771917a` | cadence, policy, ledger |
| `R0331` | `C:\Users\ala\Documents\shploingus-clean\clean-room\specs\005-u6-record-api\plan.md` | 11757 | `638a6ffd699f6c7bc09d8326fe795fb9ef6e7d0201c17f21ed7651ddb3c371a3` | witness, cadence, policy, ledger |
| `R0332` | `C:\Users\ala\Documents\shploingus-clean\clean-room\specs\005-u6-record-api\quickstart.md` | 23211 | `2a38118980a19438e8443ca20697babb7dbca2a256f8ce6e35fd41e562085a81` | witness, cadence, policy, ledger |
| `R0333` | `C:\Users\ala\Documents\shploingus-clean\clean-room\specs\005-u6-record-api\research.md` | 10732 | `ccf1fd095a8d2e247a8646bb4a5517bf9e237a0656a3878f3e91226759254fef` | cadence, policy, ledger |
| `R0334` | `C:\Users\ala\Documents\shploingus-clean\clean-room\specs\005-u6-record-api\spec.md` | 18541 | `978e1f5ccba3d95e8fa0213718a418d383ca9ddb5e340b2f428da3b10748c513` | cadence, policy, ledger |
| `R0335` | `C:\Users\ala\Documents\shploingus-clean\clean-room\specs\005-u6-record-api\tasks.md` | 33638 | `91857ada98cc587d3ff837ccfaec04d54eb96653e4057d688a28fdebf227bea8` | witness, cadence, policy, ledger |
| `R0336` | `C:\Users\ala\Documents\shploingus-clean\clean-room\specs\005-u6-record-api\checklists\requirements.md` | 6878 | `3413252a7ac329bfbdb2e31fe14cb107a3f8394cd743d0ea634c660beef36324` | cadence, policy, ledger |
| `R0337` | `C:\Users\ala\Documents\shploingus-clean\clean-room\specs\005-u6-record-api\contracts\u6-seams.md` | 15406 | `65e50202ea6397513ab06593283d8c57c7c09b53c6b376398bbaf9466fd2d7a2` | witness, cadence, policy, ledger |
| `R0338` | `C:\Users\ala\Documents\shploingus-clean\clean-room\specs\005-u6-record-api\contracts\u6-transport.md` | 8815 | `9281bb3cfab9f9d8984f06d467974b97564069d8f318863127db31f56f8edf30` | witness, policy, ledger |
| `R0339` | `C:\Users\ala\Documents\shploingus-clean\clean-room\specs\006-world-saves-and-seeds\data-model.md` | 5716 | `790a6d0b09e700e189138893c79f058d9e6d64d89478902efa27c4929d6a3205` | cadence, format, policy, ledger |
| `R0340` | `C:\Users\ala\Documents\shploingus-clean\clean-room\specs\006-world-saves-and-seeds\plan.md` | 11552 | `0753f0ef6576a4e2b9d10a72a7463c95724dede0f29468590b7cb4492b455d5e` | witness, cadence, format, policy, ledger |
| `R0341` | `C:\Users\ala\Documents\shploingus-clean\clean-room\specs\006-world-saves-and-seeds\quickstart.md` | 12151 | `0581ce2ecdc95725485a0dea5c473006da77fcd0bf20aa0cf4f3920e0f1e792e` | cadence, policy, ledger |
| `R0342` | `C:\Users\ala\Documents\shploingus-clean\clean-room\specs\006-world-saves-and-seeds\research.md` | 9024 | `61084cdf01d07508cc4ac4f39fd7757049d09ba0c35d925cfa3ab3cbbb1b6d9c` | cadence, policy, ledger |
| `R0343` | `C:\Users\ala\Documents\shploingus-clean\clean-room\specs\006-world-saves-and-seeds\spec.md` | 17279 | `7ec5ee06dc3cbe7a984adbbe6232dc5022de3f72362912e4feca82d29467bafa` | civilians, cadence, policy, ledger |
| `R0344` | `C:\Users\ala\Documents\shploingus-clean\clean-room\specs\006-world-saves-and-seeds\tasks.md` | 10106 | `a013a6d49edad10f7cb4821ca4233a83fd86af229567e2b7f2d4d1f22911d906` | cadence, policy, ledger |
| `R0345` | `C:\Users\ala\Documents\shploingus-clean\clean-room\specs\006-world-saves-and-seeds\checklists\requirements.md` | 8612 | `dffe04caabe5f228920345ecdeea70e4161c0755b8d14b3f52c343fe8ecde1c8` | cadence, policy |
| `R0346` | `C:\Users\ala\Documents\shploingus-clean\clean-room\specs\006-world-saves-and-seeds\contracts\u9-seams.md` | 5629 | `f90f5b3fff5fee76338fa363f02a9bb9faf526bb8d18bb8da68cee9a04e04d75` | cadence, format, policy |
| `R0347` | `C:\Users\ala\Documents\shploingus-clean\clean-room\specs\007-u10-gameplay-tree\data-model.md` | 9140 | `ec592d1ce98a03d81648e4af9606742e18fc2a8d3716032a385f331ce3033000` | policy, ledger |
| `R0348` | `C:\Users\ala\Documents\shploingus-clean\clean-room\specs\007-u10-gameplay-tree\plan.md` | 16873 | `ccf0cbc772ea69ab7e1bcdb023f022946ac59d7b75b387e83baa94787a05095b` | witness, client, policy, ledger |
| `R0349` | `C:\Users\ala\Documents\shploingus-clean\clean-room\specs\007-u10-gameplay-tree\quickstart.md` | 19487 | `cbebd75f383c1d1059e2d3927da45acf6d1a2b25ff499849c78794d79661cac5` | witness, cadence, client, policy, ledger |
| `R0350` | `C:\Users\ala\Documents\shploingus-clean\clean-room\specs\007-u10-gameplay-tree\research.md` | 14582 | `807f1506222367553c87eb4c651e8ad684230330e0a0901d2991e83db82e26cb` | format, client, policy, ledger |
| `R0351` | `C:\Users\ala\Documents\shploingus-clean\clean-room\specs\007-u10-gameplay-tree\spec.md` | 26549 | `4589cbddf58d99d492f972f3493c18adcabaf012c721e153f04efbd9030ef2fa` | format, client, policy, ledger |
| `R0352` | `C:\Users\ala\Documents\shploingus-clean\clean-room\specs\007-u10-gameplay-tree\tasks.md` | 25430 | `8f0d8f611f426d289522b3671ece49c49c089097277ccdbb58c14503893af695` | cadence, client, policy, ledger |
| `R0353` | `C:\Users\ala\Documents\shploingus-clean\clean-room\specs\007-u10-gameplay-tree\checklists\requirements.md` | 7399 | `bf341491d21349f761f806a290ba7ea5bfa8e5b36911bd32bae859e7a4e87166` | policy, ledger |
| `R0354` | `C:\Users\ala\Documents\shploingus-clean\clean-room\specs\007-u10-gameplay-tree\contracts\u10-seams.md` | 17442 | `562f7bcc625802b2e390e31a0da5e48e58667cf55fc637ea220d7a35342b8f22` | format, client, policy, ledger |
| `R0355` | `C:\Users\ala\Documents\shploingus-clean\clean-room\specs\008-u5-instruments-light-and-audio\plan.md` | 4900 | `03b8870a71ea06c50945cd7fc5187e784bd914fb79b5716b9825e104902a68e3` | witness, cadence, policy |
| `R0356` | `C:\Users\ala\Documents\shploingus-clean\clean-room\specs\008-u5-instruments-light-and-audio\quickstart.md` | 9477 | `d98d933e354cfbb19c28dfac38f62e1a2cb64e8f052ec984b0942e878f80e06f` | cadence, policy |
| `R0357` | `C:\Users\ala\Documents\shploingus-clean\clean-room\specs\008-u5-instruments-light-and-audio\spec.md` | 11184 | `5b7beae0c9350c7329daa9d0e45246ee05f61a0e9f5734a350cff8c5beb48c07` | witness, cadence, policy, ledger |
| `R0358` | `C:\Users\ala\Documents\shploingus-clean\clean-room\specs\008-u5-instruments-light-and-audio\tasks.md` | 3538 | `62367415f65045d9419793a4b1b23732add8c7c60f0ff7e3c04edf44ae47f0a8` | policy, ledger |
| `R0359` | `C:\Users\ala\Documents\shploingus-clean\clean-room\specs\008-u5-instruments-light-and-audio\checklists\requirements.md` | 3545 | `2f8f5c53b5fe8dd4d1a8f4b5da528a515ceab7afe9272b253c9c57f81fbd89a9` | cadence, policy |
| `R0360` | `C:\Users\ala\Documents\shploingus-clean\clean-room\specs\008-u5-instruments-light-and-audio\contracts\u5-seams.md` | 5940 | `ba35ce6df8c0770b171b86dd3c5065afd3b3749200284a29e2fc7f07bb2bef5b` | cadence, policy, ledger |
| `R0361` | `C:\Users\ala\Documents\shploingus-clean\clean-room\specs\009-u7-decision-layer\data-model.md` | 4839 | `83ec65be5872e54c194689003f22c7ee622c1e2d44443774688cf20bac2db820` | policy |
| `R0362` | `C:\Users\ala\Documents\shploingus-clean\clean-room\specs\009-u7-decision-layer\plan.md` | 7038 | `00e5a70eb3733d3edb7c58f326e2ca57f2e6abde19fa16f9d68ec5b65b1198b0` | witness, policy, ledger |
| `R0363` | `C:\Users\ala\Documents\shploingus-clean\clean-room\specs\009-u7-decision-layer\quickstart.md` | 8221 | `65b0d050f2a163ee4787f64a89c9d68988234b6144bfe4dcbc3da005791255fa` | witness, policy, ledger |
| `R0364` | `C:\Users\ala\Documents\shploingus-clean\clean-room\specs\009-u7-decision-layer\spec.md` | 12123 | `0d50192910f66375d108d21e226584a36f4e4508388d74b0b9043a82c9d0359b` | witness, policy, ledger |
| `R0365` | `C:\Users\ala\Documents\shploingus-clean\clean-room\specs\009-u7-decision-layer\tasks.md` | 5414 | `15c6a1a6e70292113c0189692e45f0fc6dd621da29b19665f173a8971c0d2417` | policy, ledger |
| `R0366` | `C:\Users\ala\Documents\shploingus-clean\clean-room\specs\009-u7-decision-layer\checklists\requirements.md` | 4701 | `13677db79fa58fca0d6b357fc45436b05995bb48f97f9590d1f9a93f30cecbb0` | policy, ledger |
| `R0367` | `C:\Users\ala\Documents\shploingus-clean\clean-room\specs\009-u7-decision-layer\contracts\u7-seams.md` | 6829 | `882c7961543cc05509af94ed6df24cd226800c1dd564f653421ea7c43b19cc07` | policy, ledger |
| `R0368` | `C:\Users\ala\Documents\shploingus-clean\clean-room\specs\010-u8-shell\data-model.md` | 3722 | `6e513ba095bac63bb4278d9adaab5f52729466835f5d95de5a7038cd4a72d7fb` | policy |
| `R0369` | `C:\Users\ala\Documents\shploingus-clean\clean-room\specs\010-u8-shell\plan.md` | 5502 | `d2cfc6a6e9f90d99c0bc513aa46a71a9da5f5cddd0226823468bfc6975cb58ec` | witness, policy |
| `R0370` | `C:\Users\ala\Documents\shploingus-clean\clean-room\specs\010-u8-shell\quickstart.md` | 9420 | `b19da8682ec799023a3f8dd8ce38ad30feb0d06ffe189ca164e81156986ebc3d` | cadence, policy, ledger |
| `R0371` | `C:\Users\ala\Documents\shploingus-clean\clean-room\specs\010-u8-shell\research.md` | 4622 | `fb092a0906fc3335a57983c584aa8cc1c5e3ee04a3d38721673cecfc82c813c3` | policy |
| `R0372` | `C:\Users\ala\Documents\shploingus-clean\clean-room\specs\010-u8-shell\spec.md` | 9463 | `92781bfbb050a766f647521c151357dc9467911c76142fc8fc2d0bef1beb6070` | policy, ledger |
| `R0373` | `C:\Users\ala\Documents\shploingus-clean\clean-room\specs\010-u8-shell\tasks.md` | 5396 | `9e2e2200892b5b69604b4ee0b51384fb2618eab73650d9a4e83a26929509ed3d` | witness, policy, ledger |
| `R0374` | `C:\Users\ala\Documents\shploingus-clean\clean-room\specs\010-u8-shell\checklists\requirements.md` | 4562 | `aa626a2a78bb462d04a7c2b5a32bde98add8696e066c89926b0e365971af0618` | policy, ledger |
| `R0375` | `C:\Users\ala\Documents\shploingus-clean\clean-room\specs\010-u8-shell\contracts\u8-seams.md` | 4747 | `e53856199c5467acb13901fb75e378ae11e0260becc8bb96954e06a4c4791966` | policy |
| `R0376` | `C:\Users\ala\Documents\shploingus-clean\clean-room\src\audio.rs` | 30915 | `5da729a4d12f811ed018e275bee7900315946a5442bccdeb5a7e350c83451a92` | cadence, policy, ledger |
| `R0377` | `C:\Users\ala\Documents\shploingus-clean\clean-room\src\automaton.rs` | 45467 | `beb30cc2bcf41088d67d5d7b6ea66a43c9f76915d7b61b53ea4dddcab9bd468a` | cadence, policy |
| `R0378` | `C:\Users\ala\Documents\shploingus-clean\clean-room\src\axis.rs` | 36018 | `deb13ac3aed11f3498658510886d03e82d7977285590ab41347a20c0a51cee66` | witness, civilians, policy, ledger |
| `R0379` | `C:\Users\ala\Documents\shploingus-clean\clean-room\src\being.rs` | 52456 | `8b0b6e3759c86e3325044f9f1728d78fd8dbb80f1ae22b4cdd461458a5f6a2f0` | witness, civilians, cadence, policy, ledger |
| `R0380` | `C:\Users\ala\Documents\shploingus-clean\clean-room\src\body.rs` | 40786 | `3bc91b73a8761416f81792a6da8728e801a3db08bd9ab7db574aed6139b2eccb` | policy, ledger |
| `R0381` | `C:\Users\ala\Documents\shploingus-clean\clean-room\src\chain.rs` | 27290 | `60d56a24e30d2fd9f0bce6d480593d8c856b592b3e961fa01fe605ffcdb7dfc8` | cadence, policy, ledger |
| `R0382` | `C:\Users\ala\Documents\shploingus-clean\clean-room\src\chunk.rs` | 83925 | `5f21bd29f41e24a2e6e8a0e7c17414b0620d0f57fa29d946fcd13b02639ccee8` | witness, cadence, policy, ledger |
| `R0383` | `C:\Users\ala\Documents\shploingus-clean\clean-room\src\controller.rs` | 59608 | `0b2884f74421c1e9f884abdb5deae13b8cfaa4899eb9b1123e1f9772b9db864b` | cadence, policy, ledger |
| `R0384` | `C:\Users\ala\Documents\shploingus-clean\clean-room\src\coordinates.rs` | 17252 | `0a6554b367bc998bfb2f5ddf14d4f8f88cfbe07880ae9dfd40bdb802d5a2e86e` | policy, ledger |
| `R0385` | `C:\Users\ala\Documents\shploingus-clean\clean-room\src\digest.rs` | 5353 | `712c5e4962a23a54403be7c06d072be4db5e9710c0e1562c7e59fd30a96b092f` | policy, ledger |
| `R0386` | `C:\Users\ala\Documents\shploingus-clean\clean-room\src\drawn.rs` | 48754 | `829282db3c305512599c669a0419ed991f7aa4a22e60f5c8ca914bcb66dfaa8e` | policy |
| `R0387` | `C:\Users\ala\Documents\shploingus-clean\clean-room\src\evidence.rs` | 252314 | `93a0e042473cb71678ae8493e0af2474cd01b52593b62a34b45831502bfbe11e` | witness, cadence, policy, ledger |
| `R0388` | `C:\Users\ala\Documents\shploingus-clean\clean-room\src\feeling.rs` | 30806 | `7eea71a63f8b12523e3da7f976748da3794baa4ff6e34a7a680dd3314734ff13` | policy |
| `R0389` | `C:\Users\ala\Documents\shploingus-clean\clean-room\src\field.rs` | 11852 | `8b2e698d1e34f1a6bb132f3353f0eff836b3ffcdbbf48c7ba7920bbf7b238ea1` | cadence, policy |
| `R0390` | `C:\Users\ala\Documents\shploingus-clean\clean-room\src\gameplay.rs` | 96374 | `4dd6bd5abfed27a6d8ace3e8a7e2aebc926ae0c8489b1f698b0e04bd386e9b6c` | cadence, format, client, policy, ledger |
| `R0391` | `C:\Users\ala\Documents\shploingus-clean\clean-room\src\intake.rs` | 65205 | `c1f3af54bdf9c6bc20db7cb16873a05d3f8623c747434bf23072e1f5714e1ddc` | civilians, policy, ledger |
| `R0392` | `C:\Users\ala\Documents\shploingus-clean\clean-room\src\laya.rs` | 42798 | `abc47749fcdc8883273578c46a5bfa915db70f1698c8a2b9bf6cfb2d3845381e` | cadence, policy, ledger |
| `R0393` | `C:\Users\ala\Documents\shploingus-clean\clean-room\src\lib.rs` | 8099 | `066b5e02a74c614a7fee742ecc3f6d60cd68bcf750d90e04283838500b209413` | civilians, cadence, policy, ledger |
| `R0394` | `C:\Users\ala\Documents\shploingus-clean\clean-room\src\light.rs` | 46861 | `53b0e6bd8f26b62539b2719006058b234b64493102f464232ce8c3b82ab69d53` | policy |
| `R0395` | `C:\Users\ala\Documents\shploingus-clean\clean-room\src\main.rs` | 33227 | `4364be89950ec3c709c56b420626971962e7a212655288acbd489758d26a47dc` | cadence, policy |
| `R0396` | `C:\Users\ala\Documents\shploingus-clean\clean-room\src\material.rs` | 13059 | `e54fd9f7d2c8eb4f5acfc7fce8338d52b6c5c18ff9bd394bf4dc26c325b65a85` | client, policy, ledger |
| `R0397` | `C:\Users\ala\Documents\shploingus-clean\clean-room\src\measure.rs` | 21271 | `44cfd7989092a8d328be0f4668c6e98d7d46d5c0e50f4d3ab5f2b4b433e3284a` | cadence, policy, ledger |
| `R0398` | `C:\Users\ala\Documents\shploingus-clean\clean-room\src\mesh.rs` | 127983 | `82cc2c54092b33b52f49b52a3c9be3500a948457533af73968c39d714a28fef9` | cadence, policy, ledger |
| `R0399` | `C:\Users\ala\Documents\shploingus-clean\clean-room\src\noise.rs` | 11996 | `8c9bf2a79a7f0176a048336ad9a61b0a454daba02ef1d93ee200142e5b1c3af4` | cadence |
| `R0400` | `C:\Users\ala\Documents\shploingus-clean\clean-room\src\policy.rs` | 32077 | `17d9e26a015ee6bfdb41e566df4d5a2a6f0b873e11b4905ad5e67965f3da933d` | witness, policy, ledger |
| `R0401` | `C:\Users\ala\Documents\shploingus-clean\clean-room\src\presentation.rs` | 19212 | `fd07eb0aecde022252fe1d1339529eb54215c1af188c26a0d2a08fa4817fc5da` | policy, ledger |
| `R0402` | `C:\Users\ala\Documents\shploingus-clean\clean-room\src\process.rs` | 38857 | `797d4d20befc402673c00ba548a1a27ded646bb000fb4dcfbe0db3df30f25a0a` | cadence, policy, ledger |
| `R0403` | `C:\Users\ala\Documents\shploingus-clean\clean-room\src\profile.rs` | 17776 | `6d8a1bc7c86528355abbbbfecd127d8d9847dd2532aa53bb813b0a1857e087ec` | policy, ledger |
| `R0404` | `C:\Users\ala\Documents\shploingus-clean\clean-room\src\reference.rs` | 8015 | `968c6b77e3896c4a5198343feecea90412744580ae64e4a3d5f90dd85a5c3918` | witness, policy, ledger |
| `R0405` | `C:\Users\ala\Documents\shploingus-clean\clean-room\src\refusal.rs` | 39295 | `fa904afa8cfdac8e5b6c4f939f85448098c98cb76134743fb1c7fb5f6db41dab` | cadence, format, policy, ledger |
| `R0406` | `C:\Users\ala\Documents\shploingus-clean\clean-room\src\shaper.rs` | 13542 | `e49c9ca3c7e5db5aa722a689ca59a9bbfc372ea582fe5e60a955ca166af6c9eb` | policy |
| `R0407` | `C:\Users\ala\Documents\shploingus-clean\clean-room\src\shell.rs` | 54250 | `b790639382ccc76799926c437527eed5a7b027068d7c42c7c41dee6a0cdf5b30` | witness, cadence, policy, ledger |
| `R0408` | `C:\Users\ala\Documents\shploingus-clean\clean-room\src\stage.rs` | 35643 | `fa75ece228fbfd1e81d3aea2070aa54079b65b90d4951e868421b88acd69234a` | cadence, policy |
| `R0409` | `C:\Users\ala\Documents\shploingus-clean\clean-room\src\stream.rs` | 31689 | `f384c5ab88cc86ccef3a31668efdb362b9dc8cc3f7a7ef2aef9f45e17914481d` | cadence, policy, ledger |
| `R0410` | `C:\Users\ala\Documents\shploingus-clean\clean-room\src\surface.rs` | 121480 | `75b99e60e2f4dd69354aed5d3f7e87597b246bb1133f8ddeef2d7de09f6e8715` | witness, cadence, policy, ledger |
| `R0411` | `C:\Users\ala\Documents\shploingus-clean\clean-room\src\systems.rs` | 39825 | `8c3f3c93cdf9ddd3d57e91900e3588e6dad0fb849dda13045fba715eedd5111c` | witness, civilians, cadence, policy, ledger |
| `R0412` | `C:\Users\ala\Documents\shploingus-clean\clean-room\src\transport.rs` | 38071 | `b84f1e50f52230a6a2af32e089c982cbd528c695db0d6a87e76e88264385a814` | witness, policy, ledger |
| `R0413` | `C:\Users\ala\Documents\shploingus-clean\clean-room\src\viewpoint.rs` | 49991 | `61470cdbac4dd24726a7277984fa453fb5fdf2379c3046a084ed31ea5b422a28` | cadence, policy |
| `R0414` | `C:\Users\ala\Documents\shploingus-clean\clean-room\src\von.rs` | 79333 | `dcc27155fc9f9d4db46802b0ea0c92fff8af2b374135db0087e4a51a27683156` | witness, policy, ledger |
| `R0415` | `C:\Users\ala\Documents\shploingus-clean\clean-room\src\world.rs` | 18058 | `04a6e2898a8a14dd5b554989b3d9a008d66aeeb43e59e9ce641db88e89b9d585` | cadence, policy, ledger |
| `R0416` | `C:\Users\ala\Documents\shploingus-clean\clean-room\src\bridge\gate.rs` | 31412 | `5aca217ce8fc47cc022d595f97c08f161c247a2ec507e7d5770fb80aa72823e8` | cadence, policy, ledger |
| `R0417` | `C:\Users\ala\Documents\shploingus-clean\clean-room\src\bridge\mod.rs` | 8323 | `e30e5e4c1c27848c5b19bdec43253fe0376c56ead29f6a90f43d4a056f3861df` | cadence, policy, ledger |
| `R0418` | `C:\Users\ala\Documents\shploingus-clean\clean-room\src\bridge\receipt.rs` | 49628 | `419f45fc765bada8dae17d1f7d94c2cece76235ed7a90b3c043b97bc59f2fc3c` | cadence, policy, ledger |
| `R0419` | `C:\Users\ala\Documents\shploingus-clean\clean-room\src\bridge\request.rs` | 14694 | `92cc0320c85e113382320da6d72d46bf535502f554701007aefbfecdd005f0ac` | policy, ledger |
| `R0420` | `C:\Users\ala\Documents\shploingus-clean\clean-room\src\bridge\table.rs` | 21535 | `f779a3e11e8b2dc182ffa5ef2b3d1f89fdb31d14b91a07c697c429cb138b8a71` | policy, ledger |
| `R0421` | `C:\Users\ala\Documents\shploingus-clean\clean-room\src\bridge\tests.rs` | 32068 | `3477b3b80337f53b7517fb9bc340e6a874c7ac6685236d34008ea5deda32611b` | cadence, policy, ledger |
| `R0422` | `C:\Users\ala\Documents\shploingus-clean\clean-room\src\bridge\wire.rs` | 27323 | `6a1523645487493568c3c6e6137bff22d8c5ffebff64d4d44168af7a1ffb68e3` | cadence, policy, ledger |
| `R0423` | `C:\Users\ala\Documents\shploingus-clean\clean-room\src\port\adapter.rs` | 4850 | `733cb8b5a59059c937c0a7e6feaffd9a30ac38295c7d35312b54bd8ead6f700b` | policy |
| `R0424` | `C:\Users\ala\Documents\shploingus-clean\clean-room\src\port\differential.rs` | 23008 | `31161267ddfd4735892930a98823afe2b2fc38a8fcdfcd4e0cd6161d98c62ced` | policy, ledger |
| `R0425` | `C:\Users\ala\Documents\shploingus-clean\clean-room\src\port\mapping.rs` | 5618 | `64837777129fc0c4fb21597958b0e36a7bc3fa95c97de8e9e6cd424469824728` | policy |
| `R0426` | `C:\Users\ala\Documents\shploingus-clean\clean-room\src\port\mod.rs` | 5761 | `ea126e009bf9592fb90f0a7727d8c92e41d96282f1820393478ae0f1d41f0d10` | policy, ledger |
| `R0427` | `C:\Users\ala\Documents\shploingus-clean\clean-room\src\port\tests.rs` | 23360 | `af0f549831c2785bcb4a42ad182065ab3c9fa0c63534d47987cf425446fe1469` | cadence, policy, ledger |
| `R0428` | `C:\Users\ala\Documents\shploingus-clean\clean-room\src\save\document.rs` | 6748 | `50c8e13377efbe41d2801d95e1bc678d35b7d2e35fab51d7c1c95910e09cdd27` | format, policy |
| `R0429` | `C:\Users\ala\Documents\shploingus-clean\clean-room\src\save\layout.rs` | 7772 | `88656a499c2a06723107f61e280712feb92c2b585d2c3ee45af44d26ec01bfed` | cadence, format, policy |
| `R0430` | `C:\Users\ala\Documents\shploingus-clean\clean-room\src\save\load.rs` | 6308 | `c94a881518e9c843189f60fd0648af6ec01fedbc57458fad4bae25d421a79510` | cadence, policy |
| `R0431` | `C:\Users\ala\Documents\shploingus-clean\clean-room\src\save\mod.rs` | 16720 | `594e44901c72aca40d756595c68fd084efb1ed35d7b83aa0b4d891c2c915f267` | cadence, format, policy, ledger |
| `R0432` | `C:\Users\ala\Documents\shploingus-clean\clean-room\src\save\tests.rs` | 19835 | `0e82adec0dd83d17dd80a6d4231f04a0e92041613bdb28b63cb92b35fe19b144` | cadence, format, policy |
| `R0433` | `C:\Users\ala\Documents\shploingus-clean\clean-room\src\shapers\air.rs` | 12209 | `3dc421638134a29e06caec2df4597ee7203c0fa95bb447a672baa39e7cf324eb` | cadence, policy |
| `R0434` | `C:\Users\ala\Documents\shploingus-clean\clean-room\src\shapers\life.rs` | 28235 | `3e4771f520adb44fd7c36c776c843c04e004775223ac9aeb9a3c39b78351cbe5` | cadence, policy |
| `R0435` | `C:\Users\ala\Documents\shploingus-clean\clean-room\src\shapers\mod.rs` | 1416 | `be87a2dd0caa436001c62afe4e72b16b6d52ef881525305cbf484bc8c6666330` | policy |
| `R0436` | `C:\Users\ala\Documents\shploingus-clean\clean-room\src\shapers\record.rs` | 21557 | `d840831deedf717233e42bc256f959ec40e61337282d65f4a9cec2714ff914b5` | cadence, policy, ledger |
| `R0437` | `C:\Users\ala\Documents\shploingus-clean\clean-room\src\shapers\terrain.rs` | 20690 | `634bc59486ca8db747dee7cb02f9609f7025cb5a8744df94dfb7a0698c1b9f11` | cadence, policy |
| `R0438` | `C:\Users\ala\Documents\shploingus-clean\clean-room\src\shapers\water.rs` | 28106 | `e7132ee3773ea5414cc71c724b54cfaf84fae45e02884454bec86db0afc09004` | cadence, policy |
| `R0439` | `C:\Users\ala\Documents\shploingus-clean\clean-room\tests\u10_gameplay.rs` | 25063 | `a44b725b75ea25ac917f92f08c5c73f0dd69685b9a147a5ca377913b72e58383` | policy, ledger |
| `R0440` | `C:\Users\ala\Documents\shploingus-clean\clean-room\tests\u12_being.rs` | 13974 | `212e73f9907fa4b23ff9490da47a3abdc866f18173efb7f907dddecb20a22c8a` | civilians, cadence, policy, ledger |
| `R0441` | `C:\Users\ala\Documents\shploingus-clean\clean-room\tests\u12_stepping.rs` | 18318 | `7e8cc2e8994ad079e758e7fb40ea06f20d5947fb410ccc4d42a18fe20299daaa` | cadence, policy |
| `R0442` | `C:\Users\ala\Documents\shploingus-clean\clean-room\tests\u1_port_flicker.rs` | 15678 | `3684ac5afc7b15fcaeb46c023ce485e591c281ecf5a0af00151d22802559e22b` | policy |
| `R0443` | `C:\Users\ala\Documents\shploingus-clean\clean-room\tests\u1_surface.rs` | 21929 | `861cecab732183f0b15f1c1b44a95d1fd9ce9228b2b43b77e615a1937c3a65f3` | cadence, policy, ledger |
| `R0444` | `C:\Users\ala\Documents\shploingus-clean\clean-room\tests\u4_drawn.rs` | 24959 | `d0ba8e1e5e2652e42f5949e15bc9172227d8ef2fd33769f94522ad16efd1fede` | cadence, policy, ledger |
| `R0445` | `C:\Users\ala\Documents\shploingus-clean\clean-room\tests\u4_geometry.rs` | 34278 | `f28c2aff13067df786cefdb5e9409fdaf2b88556c7e44afc0daff8f970bdab81` | cadence, policy, ledger |
| `R0446` | `C:\Users\ala\Documents\shploingus-clean\clean-room\tests\u5_measure.rs` | 27271 | `9b1528d1dd48a7220153835302ed1a3496c4942cb19575971a3a99e000e97f5d` | cadence, policy, ledger |
| `R0447` | `C:\Users\ala\Documents\shploingus-clean\clean-room\tests\u6_admit.rs` | 15877 | `b92a88aff9ae1a3d9910dbea72b24c023b2e30fa6d1589fd65119f2256860cda` | policy, ledger |
| `R0448` | `C:\Users\ala\Documents\shploingus-clean\clean-room\tests\u6_bridge.rs` | 31932 | `8eca82b5784e913ee24f71995a4df8229ba0674cca39f048f64f17e4adad2941` | cadence, policy, ledger |
| `R0449` | `C:\Users\ala\Documents\shploingus-clean\clean-room\tests\u6_intake.rs` | 21139 | `791ba4a24e83eee3643d2994f1cd0a7efa6b08900e43b4693c6deae1851799b2` | policy |
| `R0450` | `C:\Users\ala\Documents\shploingus-clean\clean-room\tests\u6_policy.rs` | 11892 | `9bebe86db2d44d26e30dcafcfce55ebddf3c717b4befa223bce8982b5933a7dd` | policy, ledger |
| `R0451` | `C:\Users\ala\Documents\shploingus-clean\clean-room\tests\u6_transport.rs` | 22960 | `1d3180a1ef111ed378e71e921587342aeec4e99159939d9596d8c42e8ddcd5ed` | policy, ledger |
| `R0452` | `C:\Users\ala\Documents\shploingus-clean\clean-room\tests\u7_decision.rs` | 19602 | `8dbaf1c489a87b3bc67eddeb9367dbe994ccfd430d74531533f60177e555ff41` | policy, ledger |
| `R0453` | `C:\Users\ala\Documents\shploingus-clean\clean-room\tests\u9_saves.rs` | 17363 | `e980b52e8704f613613d4f37bce6be19ea5f63be17877cbee556fe7f2ba789c7` | cadence, policy, ledger |
| `R0454` | `C:\Users\ala\Documents\shploingus-clean\crates\axis\artifact\Cargo.toml` | 1027 | `6e856f061040c110563d28aa804e384718963b5f6f6cb9066ffa781ef52f146e` | policy |
| `R0455` | `C:\Users\ala\Documents\shploingus-clean\crates\axis\artifact\src\lib.rs` | 6132 | `3813d5cab0b360c59b8754cc561fcc6aa7e3f1de7d0b10d5f9b292aa81f15986` | witness, policy, ledger |
| `R0456` | `C:\Users\ala\Documents\shploingus-clean\crates\axis\artifact\src\line.rs` | 14344 | `9360833fee86bfa62bcf2786da0b4bf309ff1d85e0eb767159827b915a16702f` | witness, policy |
| `R0457` | `C:\Users\ala\Documents\shploingus-clean\crates\axis\artifact\src\package.rs` | 35926 | `b7166e33d5fc2a81efaf5621f368a68913f848b84d621484d5e89cb474fe1312` | witness, policy, ledger |
| `R0458` | `C:\Users\ala\Documents\shploingus-clean\crates\axis\artifact\src\reproduce.rs` | 4256 | `80fd32fd6a6726a3408cf88df64325c0dcc7312488c68fd500de5c4e2018a1a9` | policy |
| `R0459` | `C:\Users\ala\Documents\shploingus-clean\crates\axis\balance\src\inventory.rs` | 16577 | `9dda076943aa0523c0ea3d28528f8ebd2968a336dce5ca52e67ffca737c940aa` | witness, policy |
| `R0460` | `C:\Users\ala\Documents\shploingus-clean\crates\axis\balance\src\lib.rs` | 6338 | `c8d5bb1b80931c378cf59d12d98611fc9bb14d7d2abacb51103f05d155810e84` | witness, policy |
| `R0461` | `C:\Users\ala\Documents\shploingus-clean\crates\axis\balance\src\measure.rs` | 5903 | `8c27b33d4d77dd2f7ab1010a3e1dadb4ce4806ba437190a5fcf1bb1dc9d1f39d` | policy |
| `R0462` | `C:\Users\ala\Documents\shploingus-clean\crates\axis\balance\src\report.rs` | 8375 | `291da3c60556357be6e98cd4a547d070c8a58d8f568e92462622acbcbf57b955` | witness, policy |
| `R0463` | `C:\Users\ala\Documents\shploingus-clean\crates\axis\being\src\being.rs` | 19630 | `99af44ef6dbf8f34b3fea69b7afd814f8b079df392b37414b4a8c543afb39444` | witness, civilians, cadence, policy, ledger |
| `R0464` | `C:\Users\ala\Documents\shploingus-clean\crates\axis\being\src\face.rs` | 10829 | `5d5854fc81d20e6126ddf06319cb01997ae025fce07b7b28aff65fdbc1e92fb9` | civilians, health, policy |
| `R0465` | `C:\Users\ala\Documents\shploingus-clean\crates\axis\being\src\lib.rs` | 3676 | `730ac81376b1c2328fa0b97ce3a00048f83281cdc1514572bc8d765e1465ac0e` | civilians, policy |
| `R0466` | `C:\Users\ala\Documents\shploingus-clean\crates\axis\being\src\life.rs` | 9470 | `c0b691dd0a2ed8ded431f21f018d0c92719f98bbffd29d157ce0633291541510` | civilians, policy |
| `R0467` | `C:\Users\ala\Documents\shploingus-clean\crates\axis\being\src\refusal.rs` | 8460 | `59bedf8a13df6394e00fa19da026d24df15fd43f76be8d71c2d281025934a0c2` | policy |
| `R0468` | `C:\Users\ala\Documents\shploingus-clean\crates\axis\being\src\signature.rs` | 7198 | `635c499835e41428238f8c65cdfc2d4a246888387635ab8ef4fc8703bd96b2ac` | cadence, policy |
| `R0469` | `C:\Users\ala\Documents\shploingus-clean\crates\axis\civilians\Cargo.toml` | 484 | `d574d4a49b669630df4883d9514eb7252de776385f3b5608e21d3ff14863f44c` | witness, civilians, policy |
| `R0470` | `C:\Users\ala\Documents\shploingus-clean\crates\axis\civilians\src\lib.rs` | 21262 | `a341465af1e01c640e67571fb19321982d41a5d70174d7bc53308cf2967835a9` | witness, civilians, policy |
| `R0471` | `C:\Users\ala\Documents\shploingus-clean\crates\axis\claim\src\lib.rs` | 12880 | `f5007a7f7db83f9f37032e8d3fabc30f2c423799f9892b350bde175d106e71ac` | witness, policy, ledger |
| `R0472` | `C:\Users\ala\Documents\shploingus-clean\crates\axis\coverage\Cargo.toml` | 436 | `4e608c9b33346419ed6370bc63f4be70d90ae8fbf34127926b8c2e7b13651df3` | policy |
| `R0473` | `C:\Users\ala\Documents\shploingus-clean\crates\axis\coverage\src\lib.rs` | 7608 | `775a59036dce875cd0af49a1396935ba3736242e5749575919d9b486faae5f48` | policy |
| `R0474` | `C:\Users\ala\Documents\shploingus-clean\crates\axis\ladder\Cargo.toml` | 392 | `ba0b75c274bd8e8bc3baececda31ccf5eebf906150e10194d4d48bf1e31d58ef` | policy |
| `R0475` | `C:\Users\ala\Documents\shploingus-clean\crates\axis\ladder\src\lib.rs` | 5043 | `cc6e611b5b9afae4b1aac809829f141652c9553b4ad7e892970fe36fd7f5f595` | policy |
| `R0476` | `C:\Users\ala\Documents\shploingus-clean\crates\axis\matrix\src\lib.rs` | 8349 | `872e8065dd3f3cc4daea4107063e3b24bee06810b6948a6902fb3037241703f4` | witness, civilians, policy |
| `R0477` | `C:\Users\ala\Documents\shploingus-clean\crates\axis\matrix\src\matrix.rs` | 20983 | `ab04b298281802810ab41a0c6550f31b7248e2fa15af984479ac8f102b77fb52` | witness, policy |
| `R0478` | `C:\Users\ala\Documents\shploingus-clean\crates\axis\matrix\src\reading.rs` | 7801 | `63e175c6b9d5ab3aee1517673421488e7d472ad854109d27160b667b4fc73508` | witness, policy |
| `R0479` | `C:\Users\ala\Documents\shploingus-clean\crates\axis\matrix\src\recipe.rs` | 18485 | `7fd65d674d3bdf7269efba69e5d2db5c1ea6e15d1a199072f54cb1a94e252acd` | witness, policy, ledger |
| `R0480` | `C:\Users\ala\Documents\shploingus-clean\crates\axis\matrix\src\refusal.rs` | 12938 | `e6917474336f2390c66a82ff37263ef16c09666d30bddeb622991b5afb075143` | witness, policy, ledger |
| `R0481` | `C:\Users\ala\Documents\shploingus-clean\crates\axis\matrix\src\segment.rs` | 8168 | `8535bc3597cb28dd7ff909d38393e80b14dcce70c55a435b9946d853d6181c98` | civilians, cadence, policy |
| `R0482` | `C:\Users\ala\Documents\shploingus-clean\crates\axis\matrix\src\star.rs` | 12711 | `acfac21d14ac4166f9622cc88464ff941bc47b23a2a0fd7a6c29b4866f5be0f1` | witness, civilians, policy |
| `R0483` | `C:\Users\ala\Documents\shploingus-clean\crates\axis\matrix\src\task.rs` | 4844 | `be475d35ee3b6f9cc03c89e1266370b41c02c3bc97d5376836e28b576c32bcde` | policy |
| `R0484` | `C:\Users\ala\Documents\shploingus-clean\crates\axis\mcp\src\grant.rs` | 16404 | `a9c3240fa28d5d72fc997877db30246d7675520a28deb31cab2bcb8cafdc8ce6` | witness, cadence, policy, ledger |
| `R0485` | `C:\Users\ala\Documents\shploingus-clean\crates\axis\mcp\src\lib.rs` | 30499 | `fb8232fe8d36372057316eba731b4e326938c3a1d62af821f4ef1233a7985f9d` | witness, cadence, policy, ledger |
| `R0486` | `C:\Users\ala\Documents\shploingus-clean\crates\axis\security\Cargo.toml` | 886 | `49f02fbb99a2968ccc45b975ca1f6fb2522ff9a55afec1882bf56b1616af71d5` | witness, policy, ledger |
| `R0487` | `C:\Users\ala\Documents\shploingus-clean\crates\axis\security\src\attest.rs` | 5802 | `98eb4f58253e8ba1b9f62c1facbe9627d350fa60f9881a92ddd1801cc47059cf` | witness, policy |
| `R0488` | `C:\Users\ala\Documents\shploingus-clean\crates\axis\security\src\hmac.rs` | 3235 | `d95546c4754ba52ad0d163dd0511d3c9d65faaca5276fefd7d23e20140197d6e` | policy, ledger |
| `R0489` | `C:\Users\ala\Documents\shploingus-clean\crates\axis\security\src\lib.rs` | 21755 | `c8a0119d2e39c190656260752dd844a5abb13b2d9bd1e39fff25f1649ddaf0fd` | witness, policy, ledger |
| `R0490` | `C:\Users\ala\Documents\shploingus-clean\crates\axis\unit\src\lib.rs` | 8692 | `bdf3436a66bd2496c337a10d96910d6a5ea80201410c345b7f522a8595500288` | policy, ledger |
| `R0491` | `C:\Users\ala\Documents\shploingus-clean\crates\axis\verify\Cargo.toml` | 817 | `d700ad85d73f4fb58f5d3c8535abe3cdf592be1fad9531a20728c5284f467559` | witness, policy |
| `R0492` | `C:\Users\ala\Documents\shploingus-clean\crates\axis\verify\examples\ratchet.rs` | 943 | `39a5970394a861ca111cd1a2638a1e485f82377c6e366b6044107066bb1af75e` | health |
| `R0493` | `C:\Users\ala\Documents\shploingus-clean\crates\axis\verify\src\evidence.rs` | 10562 | `75aa4901d05370b6ad727ca1df144b729a4f55f64ce4901acc029f37215639c3` | policy |
| `R0494` | `C:\Users\ala\Documents\shploingus-clean\crates\axis\verify\src\lib.rs` | 6282 | `c8fef36c5cfc6c985e77cce649d37d448eb061699b282482b61244d1dc7ba01a` | witness, health, policy |
| `R0495` | `C:\Users\ala\Documents\shploingus-clean\crates\axis\verify\src\prose.rs` | 5612 | `f636def496cd5d138a8d66ac70af1a407687e20db471b2bfd275543a71740108` | policy, ledger |
| `R0496` | `C:\Users\ala\Documents\shploingus-clean\crates\axis\verify\src\ratchet.rs` | 21781 | `5d7ce1fc12f66fb3fd19957b406792c2a8dcbc2fd3740607981e0cfbf0b6c225` | witness, health, policy |
| `R0497` | `C:\Users\ala\Documents\shploingus-clean\crates\axis\verify\src\report.rs` | 44072 | `17ff0f307da25e8d6adb386135bcf30849648ae4eb2f3347ab3a3c8f6a53ae0f` | witness, policy |
| `R0498` | `C:\Users\ala\Documents\shploingus-clean\crates\axis\verify\src\source.rs` | 6683 | `7a562a98341dd78762a0d378d2bd80e953f2fd8560811c38c6becff872e912a9` | witness, policy |
| `R0499` | `C:\Users\ala\Documents\shploingus-clean\crates\axis\verify\src\subject.rs` | 8262 | `1e331b3ba32ec5bb813038728db210c60c0da2a2450d035eb6bce57d4a9040ed` | witness, civilians |
| `R0500` | `C:\Users\ala\Documents\shploingus-clean\crates\axis\view\src\lib.rs` | 14428 | `6acc8ae968aaa7db5f6342e983320f636bd5bd7bc9a6e59a715896245a5e3a7d` | witness, policy |
| `R0501` | `C:\Users\ala\Documents\shploingus-clean\crates\shploingus\build.rs` | 32999 | `562b20e94f66c981100612f322855c69f364df20a1ca184fa6717f99a6a061d8` | witness, civilians, health, policy, ledger |
| `R0502` | `C:\Users\ala\Documents\shploingus-clean\crates\shploingus\src\capture.rs` | 16363 | `c5f9be87259ef031f75c4f43746fb2b16eca73752cb9c778f826f88cda386f0b` | cadence |
| `R0503` | `C:\Users\ala\Documents\shploingus-clean\crates\shploingus\src\main.rs` | 322204 | `971fe14eaccb054e2ede1af8ef1d5ffe2fd0e1a86a4de31137aa420854bb6888` | civilians, cadence, health, client, policy, ledger |
| `R0504` | `C:\Users\ala\Documents\shploingus-clean\crates\voxel-appearance\Cargo.toml` | 2370 | `efbe40c4213d746b78b415b951aafa268474012e46c3239e83c3820da0ff8e74` | policy |
| `R0505` | `C:\Users\ala\Documents\shploingus-clean\crates\voxel-appearance\src\composition.rs` | 10313 | `5a4483beae523e4ccceaac570cd23105239d8cfd3b37d49fbb60d0425febb8c6` | policy |
| `R0506` | `C:\Users\ala\Documents\shploingus-clean\crates\voxel-appearance\src\detail.rs` | 16728 | `9eb46ef9132dfe7d725eed28747d14a4a172ce2e648f36985e55176aed4d4f27` | policy |
| `R0507` | `C:\Users\ala\Documents\shploingus-clean\crates\voxel-appearance\src\fluid.rs` | 9080 | `5aa98135b8d9203112eecd70b8fd071ef41afcac8c80946bfa7f36aac2b46fde` | policy, ledger |
| `R0508` | `C:\Users\ala\Documents\shploingus-clean\crates\voxel-appearance\src\lib.rs` | 6315 | `0d2597cea9e5eb8cd9f1d15c65532329c9807ccbd24b8402e2aa3ebebba529be` | policy, ledger |
| `R0509` | `C:\Users\ala\Documents\shploingus-clean\crates\voxel-appearance\src\npr.rs` | 37216 | `6bfb990a97613d4f41217e8d7c319bc40449e8db3e79c765bfd07f5161b2df13` | policy |
| `R0510` | `C:\Users\ala\Documents\shploingus-clean\crates\voxel-appearance\src\openpbr.rs` | 61748 | `a8d9d27a648d038ea099125dbd6787b40a5165852677353f2344269c260a3a7b` | policy, ledger |
| `R0511` | `C:\Users\ala\Documents\shploingus-clean\crates\voxel-appearance\src\response.rs` | 12403 | `b0994b1d23a6c8f5b9900cbfb2e5649057f62ef42e5d302e6e74a662b51894c7` | policy |
| `R0512` | `C:\Users\ala\Documents\shploingus-clean\crates\voxel-appearance\src\sky.rs` | 59910 | `246ba3990dbab20bc0634c38d38193e4837417a9d7be0e34bc1a0da684d681ed` | cadence, policy, ledger |
| `R0513` | `C:\Users\ala\Documents\shploingus-clean\crates\voxel-appearance\src\tonemap.rs` | 12879 | `2fdacd2ebddbe395e2827c8176b2f832362a50b38b3fef3db32af5486665edfe` | policy |
| `R0514` | `C:\Users\ala\Documents\shploingus-clean\crates\voxel-appearance\src\wrap.rs` | 20759 | `4246453543193f412b8417b91002a13e81b72483a7ec7050b974efcbfccf6f45` | policy |
| `R0515` | `C:\Users\ala\Documents\shploingus-clean\crates\voxel-audio\Cargo.toml` | 1893 | `60f99757270de31cc15ac05f8539c775aeeb434e397681db1015d026a7ed091d` | cadence |
| `R0516` | `C:\Users\ala\Documents\shploingus-clean\crates\voxel-audio\src\lib.rs` | 19631 | `3cb0e22c7dc7f86660292cb7c9c95424ded86cd75e9f4b14a938345e26db4118` | cadence, ledger |
| `R0517` | `C:\Users\ala\Documents\shploingus-clean\crates\voxel-client\Cargo.toml` | 6250 | `af35e1a412e4852c3c41cacad80a6186bdaf41ef194a80524bb31c31f2b0e778` | witness, policy |
| `R0518` | `C:\Users\ala\Documents\shploingus-clean\crates\voxel-client\examples\atmosphere-probe.rs` | 3022 | `02f45c7cb3d1028174ad29433cfad812adf26dfad5e6d86ca3bfa48ea1ee0c7b` | cadence |
| `R0519` | `C:\Users\ala\Documents\shploingus-clean\crates\voxel-client\examples\daylight-hue.rs` | 4761 | `0ade88b26c7f4a1624b639b6587ed61caa8abc7df96a0e9fa022aa63ad844bc9` | cadence, policy |
| `R0520` | `C:\Users\ala\Documents\shploingus-clean\crates\voxel-client\examples\exposure-steps.rs` | 7942 | `ff49877289115db2b30ea1114ef97db1e436c1075f170e4005a03a45030339f3` | cadence |
| `R0521` | `C:\Users\ala\Documents\shploingus-clean\crates\voxel-client\examples\frame-cost.rs` | 20811 | `4a1d6b9d49ba8bfe529b8f7bd50a9818accddf3892821480f987ba85b3ce3fc7` | policy |
| `R0522` | `C:\Users\ala\Documents\shploingus-clean\crates\voxel-client\examples\gpu-shadow-check.rs` | 42671 | `35b60103f01da3d6e1b90ea4f8e773a6e7b78dff2c138f0b1c60ab4f5cfbab20` | witness, cadence, policy |
| `R0523` | `C:\Users\ala\Documents\shploingus-clean\crates\voxel-client\examples\light-at-a-pixel.rs` | 35555 | `02245105816803342a126a51ca46aa4a1efb9b542d1dfc652d0fd7493cbc2044` | cadence, policy |
| `R0524` | `C:\Users\ala\Documents\shploingus-clean\crates\voxel-client\examples\light-budget.rs` | 4438 | `896c138baa4a39bc014761b0820817c7f0bb9982066cb39d36fda1c00a5c0d45` | policy |
| `R0525` | `C:\Users\ala\Documents\shploingus-clean\crates\voxel-client\examples\light-shot.rs` | 14035 | `6c955c04c4fbf60adafd8418bdbc88f93ac56553c689e58ed6f12621c108d9f2` | cadence |
| `R0526` | `C:\Users\ala\Documents\shploingus-clean\crates\voxel-client\examples\light-terms.rs` | 25413 | `554daa374677cc1ec2140c31de5e3b6440f0958f171c3584e3b388ad2e18678e` | cadence, policy |
| `R0527` | `C:\Users\ala\Documents\shploingus-clean\crates\voxel-client\examples\material-cube.rs` | 11370 | `6c720cba21993448c17ee45d06b100b055d32be690ff4880678cf9630f198e79` | policy |
| `R0528` | `C:\Users\ala\Documents\shploingus-clean\crates\voxel-client\examples\measured-light.rs` | 26139 | `9d44b8ef61947dd79244e6e85491d3565c635bf1f7d2ea63504a70a37913146b` | cadence, policy |
| `R0529` | `C:\Users\ala\Documents\shploingus-clean\crates\voxel-client\examples\moon-report.rs` | 3581 | `a7f5f3d306a7b5d0a7ab3565599db480cb1190125632036a7c46c7a51cbf1238` | cadence |
| `R0530` | `C:\Users\ala\Documents\shploingus-clean\crates\voxel-client\examples\night-check.rs` | 3073 | `6d376c571418c3fa53b716533629a4bf84935346c2ad5f17347daba4b2b4f16f` | cadence |
| `R0531` | `C:\Users\ala\Documents\shploingus-clean\crates\voxel-client\examples\pattern-hold.rs` | 9189 | `ff7eebba12d339f6a627aa164e88a06f48d63d693c142b0e331728a6b6f27934` | cadence |
| `R0532` | `C:\Users\ala\Documents\shploingus-clean\crates\voxel-client\examples\rig-balance.rs` | 4764 | `a22735d962ca56a24f3f02c70d96894ee61f00271926341b00d3142fd4e16cbe` | cadence, policy |
| `R0533` | `C:\Users\ala\Documents\shploingus-clean\crates\voxel-client\examples\shadow-lattice.rs` | 41548 | `06b29b8d1140232d922dea10488003108099c26ef4679c2e7b5bf8865b24fe32` | witness, cadence, policy |
| `R0534` | `C:\Users\ala\Documents\shploingus-clean\crates\voxel-client\examples\shell-shot.rs` | 23155 | `d8bacdc72f2f6dfc0e472a073454e54f58612c44b336efa38553c26d5a5ae1ea` | cadence, policy |
| `R0535` | `C:\Users\ala\Documents\shploingus-clean\crates\voxel-client\examples\sun-in-the-sky.rs` | 8082 | `2404892b551a1df824d5ec7dfda39454d0b9ffe9bb877587400bc2a8430a13c1` | cadence |
| `R0536` | `C:\Users\ala\Documents\shploingus-clean\crates\voxel-client\examples\surface-format-check.rs` | 17633 | `93f74d96c6537548163907b017489ddb6d89ea9389dafb7d7650ee98dba102eb` | cadence, policy |
| `R0537` | `C:\Users\ala\Documents\shploingus-clean\crates\voxel-client\src\atmosphere.rs` | 18110 | `ad86a94d9885f20ef642a3b1134a2c5ab187add1b8b436f1deb56b4e367fd81c` | cadence, policy |
| `R0538` | `C:\Users\ala\Documents\shploingus-clean\crates\voxel-client\src\camera.rs` | 27479 | `d2d3f306a522c6cbf2d4e5090a28e8b55df517c6eae058ad6e3d11e640221d66` | cadence, ledger |
| `R0539` | `C:\Users\ala\Documents\shploingus-clean\crates\voxel-client\src\camera_overhaul.rs` | 35033 | `f201bee8f37b33ecc84b7e6e209833fbccf760743dc792ce54f68aa4301ffe20` | cadence, client |
| `R0540` | `C:\Users\ala\Documents\shploingus-clean\crates\voxel-client\src\clock.rs` | 26346 | `37af10fa2953f041ebf395e48e02a5d2a33aa3e0bfe5311736be73836c388112` | cadence, policy, ledger |
| `R0541` | `C:\Users\ala\Documents\shploingus-clean\crates\voxel-client\src\cloud_cubes.rs` | 102178 | `46f8a4e2a8538797d5a252f4facafd021e36dc440ef513a8ddcfc32817773933` | witness, cadence, format, policy |
| `R0542` | `C:\Users\ala\Documents\shploingus-clean\crates\voxel-client\src\cloud_field.rs` | 65104 | `983e219976a0fd51a160ed3305235bb33c482f76134fa848bbce7a1279352dd9` | witness, cadence, policy |
| `R0543` | `C:\Users\ala\Documents\shploingus-clean\crates\voxel-client\src\debug.rs` | 32875 | `7e2e7461d2cdab4c00267f248238797ce18871e0dc63c6184db1db9a19902c8e` | cadence, policy |
| `R0544` | `C:\Users\ala\Documents\shploingus-clean\crates\voxel-client\src\far_terrain.rs` | 84262 | `3f526d2ba6ffa6bb088dfc925805b009aca64f05adb4411d311f12e7d6b39817` | policy |
| `R0545` | `C:\Users\ala\Documents\shploingus-clean\crates\voxel-client\src\field.rs` | 35317 | `d7314279efc23a62c0d2413f826cff484619c21c7f236ddb3c8c76b85dec75b8` | cadence, policy |
| `R0546` | `C:\Users\ala\Documents\shploingus-clean\crates\voxel-client\src\fog_cubes.rs` | 12721 | `f75bdc48887eeca3a0d5daf0222fcbd96cd504afd1d3ec966e8a0af9bf494e39` | cadence |
| `R0547` | `C:\Users\ala\Documents\shploingus-clean\crates\voxel-client\src\frame.rs` | 8792 | `90092b08f702732cccc598c5ad042d9256e921d3c869bf71ae887f471cd74e05` | policy |
| `R0548` | `C:\Users\ala\Documents\shploingus-clean\crates\voxel-client\src\game.rs` | 29798 | `704c9313a96a9886aaac63d0289925ab07e1871f95779b3bf19caabeb9c6e8f9` | cadence, policy, ledger |
| `R0549` | `C:\Users\ala\Documents\shploingus-clean\crates\voxel-client\src\horizon.rs` | 124681 | `08b58d11257e79882f4c8833f977a7a0162bbe5389d1def5154b8b76614e05f5` | cadence, client, policy |
| `R0550` | `C:\Users\ala\Documents\shploingus-clean\crates\voxel-client\src\hud.rs` | 62835 | `8684097fb57080745e05b42333117ce61087be9581b32a7a057b59430cf28acb` | witness, cadence, policy, ledger |
| `R0551` | `C:\Users\ala\Documents\shploingus-clean\crates\voxel-client\src\inventory.rs` | 7866 | `4312951d911297c9c96267d5be221ccc89f7ab920313450e725a98c1f9dc6378` | policy |
| `R0552` | `C:\Users\ala\Documents\shploingus-clean\crates\voxel-client\src\lib.rs` | 9684 | `9c7c9f396d2a10bc5bc6a2276175ea423fc950311daab82258bb87f80c14baa9` | policy |
| `R0553` | `C:\Users\ala\Documents\shploingus-clean\crates\voxel-client\src\map_survey.rs` | 80075 | `26add1ac7161e4c1577b1b458ab5499548b86f5dfc12e99f62e33283f0422523` | witness, cadence, policy |
| `R0554` | `C:\Users\ala\Documents\shploingus-clean\crates\voxel-client\src\map_view.rs` | 96114 | `a7c60b53475e45688a59672e5ef35e3dad1a8f1c3c22fcdb35bcba99683e5fd7` | cadence, policy |
| `R0555` | `C:\Users\ala\Documents\shploingus-clean\crates\voxel-client\src\measure.rs` | 22974 | `01d96ca8f245eaa22540881edea96c57d867c67657fe132d657b466b36e43097` | cadence, policy |
| `R0556` | `C:\Users\ala\Documents\shploingus-clean\crates\voxel-client\src\motion.rs` | 76128 | `052a0601cd3c6a65006beb3d2e20efeaf011d4197749d2d30e152e2a56c1817a` | cadence, client |
| `R0557` | `C:\Users\ala\Documents\shploingus-clean\crates\voxel-client\src\pattern.rs` | 50054 | `986b170a88592e921155e239d8066970c13a974c3073a5b780c775bf7f5e1582` | cadence, client, policy |
| `R0558` | `C:\Users\ala\Documents\shploingus-clean\crates\voxel-client\src\quad.rs` | 23980 | `473ca513d8e2952a7a2a2240744923d89f2372814c957344742178da3c942956` | policy |
| `R0559` | `C:\Users\ala\Documents\shploingus-clean\crates\voxel-client\src\renderer.rs` | 227799 | `60b528b7a627516bb42b4925d370cc83583b0554189da11f889b3c73ab1cc318` | witness, cadence, client, policy, ledger |
| `R0560` | `C:\Users\ala\Documents\shploingus-clean\crates\voxel-client\src\scene.rs` | 215828 | `a1c257c8e09cbae0926c808fb916eb0fb9b46d7b000366a41318b1c4af8a68f7` | witness, cadence, policy |
| `R0561` | `C:\Users\ala\Documents\shploingus-clean\crates\voxel-client\src\shading.rs` | 55575 | `3d6527bacf24ff7a307f50804f5168e713acc7801b26425e9ad0819df4948b85` | policy, ledger |
| `R0562` | `C:\Users\ala\Documents\shploingus-clean\crates\voxel-client\src\skylight.rs` | 212848 | `0b2e5aa94b4cd2b3f4720632c1310cd94a0d990fe171ec2bec074637bc6126d1` | witness, cadence, policy |
| `R0563` | `C:\Users\ala\Documents\shploingus-clean\crates\voxel-client\src\sun.rs` | 61530 | `a6ec119faa75058eb802f21ccec75aae50f68ab50b520a2c9c846588e8ef6e0a` | cadence, policy |
| `R0564` | `C:\Users\ala\Documents\shploingus-clean\crates\voxel-client\src\sun_shadow.rs` | 47921 | `bc1e845b236443b5188ab871a426fd90f2f53c87ad4fcc3c5fd4cd6be3f0cf8a` | witness, cadence |
| `R0565` | `C:\Users\ala\Documents\shploingus-clean\crates\voxel-client\src\surface.rs` | 81396 | `6390e11eaad5239cc9ff5c044ca2a256797506261879aec5cdb2ad1fe1e163d8` | cadence, policy, ledger |
| `R0566` | `C:\Users\ala\Documents\shploingus-clean\crates\voxel-client\src\work.rs` | 12843 | `fa32be5fc8fa8fc1ac3f3d0e6a103e6af2081c05da8defd8a23441d2ff44e75e` | policy |
| `R0567` | `C:\Users\ala\Documents\shploingus-clean\crates\voxel-client\src\world.rs` | 190562 | `0a256066988afc60e7c7cc3fd3cee18e648c92a3f20dc3f8658a7abb187f8461` | witness, cadence, client, policy, ledger |
| `R0568` | `C:\Users\ala\Documents\shploingus-game\Cargo.toml` | 8960 | `81b5e7e2614593f8586c0a09c6aaa615f4b2e1650b2a19e70d5545471274ac53` | client, policy, ledger |
| `R0569` | `C:\Users\ala\Documents\shploingus-game\PLAN-STACK.md` | 33104 | `615fa1a83e2250a103d789313c28ff3ab15e5754f8346090ad82ab89b667a2be` | cadence, policy, ledger |
| `R0570` | `C:\Users\ala\Documents\shploingus-game\crates\diffusion-core\CONTEXT.md` | 9982 | `6e64a71a0c9a754493a307b5894cdd408964e31ba4fbad18739bd32172c7b92b` | policy |
| `R0571` | `C:\Users\ala\Documents\shploingus-game\crates\diffusion-core\src\assertion.rs` | 56098 | `37f61dab9f5a539475014ad5bb4bcb9eb4cd1c5b0ab0f68fb2456274fb996e41` | policy |
| `R0572` | `C:\Users\ala\Documents\shploingus-game\crates\diffusion-core\src\axis.rs` | 58823 | `3b0bd53a05fa0bd1be6d6b3145397cde8608779e5a3a0cdfb8a7098c01577e3c` | civilians, cadence, policy, ledger |
| `R0573` | `C:\Users\ala\Documents\shploingus-game\crates\diffusion-core\src\blockers.rs` | 25140 | `f391bfeda57e4008c09db48dc1a833e3a83c573044f1ce1a1e4c282b947ed833` | policy, ledger |
| `R0574` | `C:\Users\ala\Documents\shploingus-game\crates\diffusion-core\src\compiler.rs` | 24053 | `c4ffc45acfc8415579584478c335e76cb732da2f0560fbdd601c7e3a7012815d` | policy, ledger |
| `R0575` | `C:\Users\ala\Documents\shploingus-game\crates\diffusion-core\src\encyclopedia.rs` | 48161 | `b19ab395371e7f4a1ae34f05825bcea9c23da83b6b97290ad1c68d2d9eeab57f` | policy, ledger |
| `R0576` | `C:\Users\ala\Documents\shploingus-game\crates\diffusion-core\src\governance.rs` | 27709 | `3d4773b8ec5811c350b4399f75a9a3d2527c914f573943393cc70d9fbdb45b57` | policy, ledger |
| `R0577` | `C:\Users\ala\Documents\shploingus-game\crates\diffusion-core\src\identity.rs` | 12431 | `9bffe0627eb1b56049c9989f278f5231e0446c3d4549c3df259a04d5440d5bf4` | policy, ledger |
| `R0578` | `C:\Users\ala\Documents\shploingus-game\crates\diffusion-core\src\ingest.rs` | 41075 | `05b6e0a67375a8fc85d297c2e826140c3c1ec1b5cbb6fe87ac1e3f7de48eda06` | policy, ledger |
| `R0579` | `C:\Users\ala\Documents\shploingus-game\crates\diffusion-core\src\laya.rs` | 35708 | `bbd89d61eb6dca5ad985f9797a4e4f253c4df2fdee3c6b38c6360b8c2cc2821f` | policy |
| `R0580` | `C:\Users\ala\Documents\shploingus-game\crates\diffusion-core\src\lib.rs` | 11043 | `a7f869bb9a4702091678ee7a5fd9900f12e4dbb48823b2695c7b83890c6e57d3` | policy, ledger |
| `R0581` | `C:\Users\ala\Documents\shploingus-game\crates\diffusion-core\src\lint.rs` | 26536 | `cd803c4a8ee2238dc31012b7c597042a0490d76b85b0baf5a17d207282ae4d3b` | policy |
| `R0582` | `C:\Users\ala\Documents\shploingus-game\crates\diffusion-core\src\loader.rs` | 36929 | `fc1936a897a832d71d311fd9558006b427b59c3d5a84f24376bb6039d6496156` | policy, ledger |
| `R0583` | `C:\Users\ala\Documents\shploingus-game\crates\diffusion-core\src\milestones.rs` | 21800 | `d1a87a72d824304934ecf999073a3da36aab2bf928268e34f2089ce7333ef4b2` | policy, ledger |
| `R0584` | `C:\Users\ala\Documents\shploingus-game\crates\diffusion-core\src\mods.rs` | 51581 | `663fb379c7bd6bd9170aee5079493f14d40c3dd535fe8f18803277043c556306` | policy, ledger |
| `R0585` | `C:\Users\ala\Documents\shploingus-game\crates\diffusion-core\src\package.rs` | 27078 | `1b870692a9802ad6532849c2cec6988b9383e94085c37b0aabfc3055f2427bf6` | policy, ledger |
| `R0586` | `C:\Users\ala\Documents\shploingus-game\crates\diffusion-core\src\patch.rs` | 33709 | `a2297e8b0947c439a10c89adaee493bc1b578497db6119c79c3eac6ec73b820e` | policy, ledger |
| `R0587` | `C:\Users\ala\Documents\shploingus-game\crates\diffusion-core\src\provenance.rs` | 16588 | `fa4b64e33366dabd16417254038aec6b2b2ac45ae1d2192265a253c59ab95158` | policy, ledger |
| `R0588` | `C:\Users\ala\Documents\shploingus-game\crates\diffusion-core\src\record.rs` | 43734 | `6685de1e38bd0daf11be9f8be6aa7ac4e77dd0d24428d381fe7f20e1b93a684e` | policy, ledger |
| `R0589` | `C:\Users\ala\Documents\shploingus-game\crates\diffusion-core\src\refusal.rs` | 24892 | `64e7bc2b883f2c470cc62f67cb2abc7872ad17f6f35572a0e842d8b24f7397b7` | policy, ledger |
| `R0590` | `C:\Users\ala\Documents\shploingus-game\crates\diffusion-core\src\sensor.rs` | 33385 | `869e553b7bc62e5b5467f93d59d41ee15dc2d53775051dc26b393bae182c0d7b` | policy, ledger |
| `R0591` | `C:\Users\ala\Documents\shploingus-game\crates\diffusion-core\src\signing.rs` | 11135 | `bc1b4f4827a3f7790c327ae5753455fe1e6560f56fa0b034215c0c69668bbebf` | policy, ledger |
| `R0592` | `C:\Users\ala\Documents\shploingus-game\crates\diffusion-core\src\support.rs` | 28971 | `73ea0d110b3e2151a8eba2fdc5f574d9c304f0e11bcc556a5bb98c22bc308c15` | cadence, policy |
| `R0593` | `C:\Users\ala\Documents\shploingus-game\crates\diffusion-core\src\sweep.rs` | 18899 | `eec49889b1bffe375e8a887ce005ccf5f099f9a404cfa4d686d4c873ecdabedf` | witness, policy |
| `R0594` | `C:\Users\ala\Documents\shploingus-game\crates\diffusion-core\src\ticket.rs` | 16557 | `bd13116cd5c337957d048c071af8cb54ace41d1fa35e35c6ab6aaad8f5537ed6` | policy |
| `R0595` | `C:\Users\ala\Documents\shploingus-game\crates\diffusion-core\src\truth.rs` | 20446 | `920485a389a7a0f02a3457d2354a958f8c63f1661077aa80b98a5c9847c20b18` | health, policy |
| `R0596` | `C:\Users\ala\Documents\shploingus-game\crates\diffusion-core\src\view.rs` | 23181 | `4c4911981d5cdf6fd01c396adacecc868b255f69b451be11e7c857e41f99dc49` | ledger |
| `R0597` | `C:\Users\ala\Documents\shploingus-game\crates\diffusion-core\src\voxelwire.rs` | 124603 | `475ec88459594d3b72743988e76bf877f6a1ca6ed478ba521d22233653f39687` | cadence, format, policy, ledger |
| `R0598` | `C:\Users\ala\Documents\shploingus-game\crates\diffusion-core\src\wire.rs` | 31662 | `317f780a63ae0dfa3e26cb04828fa04ce229699ae771b7d7ddb2f2bb6b893523` | format, policy |
| `R0599` | `C:\Users\ala\Documents\shploingus-game\crates\diffusion-core\src\bin\diffctl.rs` | 95423 | `bb1247a80460bfea656d9783fd16188eec231064bb0edf5c8db4fdf838fe0826` | cadence, policy, ledger |
| `R0600` | `C:\Users\ala\Documents\shploingus-game\crates\diffusion-core\src\bin\shploingus\main.rs` | 84869 | `fb6bdb8812412fca39e8d501c30e8b85b65bd2a369169fb17d95a50213cdc2e6` | cadence, policy |
| `R0601` | `C:\Users\ala\Documents\shploingus-game\crates\diffusion-core\src\bin\shploingus\render\mod.rs` | 141844 | `89fed73c3310c93976b04a0dcfd65d28fb5109665537db3f8731a6885be9661d` | cadence, policy, ledger |
| `R0602` | `C:\Users\ala\Documents\shploingus-game\crates\diffusion-core\src\bin\shploingus\render\palette.rs` | 47763 | `0e44388b8091696cefaface80f02e226c87b51b5c913548b7e72dd8283792a97` | policy |
| `R0603` | `C:\Users\ala\Documents\shploingus-game\crates\diffusion-core\src\bin\shploingus\render\shell.rs` | 86027 | `07582bed420d0b795d7aaac692d7d880c503aff406b69ff66f1ffc8e986abea5` | cadence, policy, ledger |
| `R0604` | `C:\Users\ala\Documents\shploingus-game\crates\diffusion-core\src\bin\shploingus\render\text.rs` | 11390 | `c902b6b943bd312ef752d9d42cd10336c5999e9c5af1f58bcb7f5246c9cf4cb2` | policy |
| `R0605` | `C:\Users\ala\Documents\shploingus-game\crates\diffusion-core\src\client\block.rs` | 17315 | `ace5e36846db214911aa0f2efa07eb6281f14716b02ad2d719ca3389d9a28d70` | policy |
| `R0606` | `C:\Users\ala\Documents\shploingus-game\crates\diffusion-core\src\client\bridge.rs` | 48042 | `a247e7977a26c90335c01ef483d4291d67bfa538b1f7f64dca99cda84f579808` | cadence, policy, ledger |
| `R0607` | `C:\Users\ala\Documents\shploingus-game\crates\diffusion-core\src\client\camera.rs` | 53357 | `617f71ef56273bd6b68fa5573af966c24936c1040a875547320764f48ecdfcee` | cadence, policy |
| `R0608` | `C:\Users\ala\Documents\shploingus-game\crates\diffusion-core\src\client\client_model.rs` | 53034 | `c573d79222aaee8a7cdf20c3b0162d6e9230c869ab6ef0a32854d67afc80af32` | cadence, policy, ledger |
| `R0609` | `C:\Users\ala\Documents\shploingus-game\crates\diffusion-core\src\client\debug.rs` | 52177 | `4ca8f1500c5c3e06339e92ab38d4450e089b4eb676317195c1d9f28f07ac163e` | cadence, policy, ledger |
| `R0610` | `C:\Users\ala\Documents\shploingus-game\crates\diffusion-core\src\client\input.rs` | 24032 | `848c66cc4966dfb3d3e110b7a182c8af18f737a5470478faf4391ca4f85144c8` | policy |
| `R0611` | `C:\Users\ala\Documents\shploingus-game\crates\diffusion-core\src\client\math.rs` | 23217 | `ec1420cb0f391e2baf679763ac00052b45cfd8772a01a40660319f8afbd1a0f1` | policy |
| `R0612` | `C:\Users\ala\Documents\shploingus-game\crates\diffusion-core\src\client\mesh.rs` | 63409 | `a811546e2dda452bad39359f1fb46a94a5501b5336d1af90406ac0f2df9cf924` | policy, ledger |
| `R0613` | `C:\Users\ala\Documents\shploingus-game\crates\diffusion-core\src\client\octree.rs` | 18988 | `09b300f34e1a49fb936bbd2acdb744b6b95c825eb03492590a0aac05766da04e` | policy |
| `R0614` | `C:\Users\ala\Documents\shploingus-game\crates\diffusion-core\src\client\raycast.rs` | 14196 | `12dab2d00ec4bfda607973cc8bc2731a096ed7d6dd56dbbf1281d1ff002890ee` | policy |
| `R0615` | `C:\Users\ala\Documents\shploingus-game\crates\diffusion-core\src\client\region.rs` | 19607 | `94b8c08ffb699ea26034f321e2b23bba61d2876b7385119cb55272789713f5f4` | format, policy |
| `R0616` | `C:\Users\ala\Documents\shploingus-game\crates\diffusion-core\src\client\sim.rs` | 20102 | `118604e3fc3e8853c0b51b4cc6d945f6be93c9efb460ae382b6bc59d6e2602a1` | cadence, policy, ledger |
| `R0617` | `C:\Users\ala\Documents\shploingus-game\crates\diffusion-core\src\client\slot.rs` | 21176 | `968e1d84426375622ba3c73f5f73aaf2617cab5b06bff04c3ce3814f1065ef03` | policy |
| `R0618` | `C:\Users\ala\Documents\shploingus-game\crates\diffusion-core\src\client\shell\mod.rs` | 66573 | `6675ac5713b180c9df6988e4eac5efb321f7bc93c57e49e53634d5831de590c4` | cadence, format, policy |
| `R0619` | `C:\Users\ala\Documents\shploingus-game\crates\diffusion-core\src\client\shell\motion.rs` | 21065 | `b95e58e8290bdd934c6711d1be6c166b40f21a3208eaf162cbdf462fafe4d3ef` | format, policy |
| `R0620` | `C:\Users\ala\Documents\shploingus-game\crates\diffusion-core\src\client\shell\tabs.rs` | 17090 | `742485806b41e5d103165d15247d3b464f1db1c38d33d17dd9a6980607252524` | ledger |
| `R0621` | `C:\Users\ala\Documents\shploingus-game\crates\diffusion-core\src\legacyledger\gov.rs` | 38251 | `9d23c7a82dc8b71ae276b2b529aab1cc9fa35a32ae3c37d24835011c876bbc90` | civilians, cadence, client, policy, ledger |
| `R0622` | `C:\Users\ala\Documents\shploingus-game\crates\diffusion-core\src\legacyledger\kinds.rs` | 24403 | `6424fe84bb2677404f5c6d8e27d42caa0dc13d57e6922b13dd20dc92746605f2` | policy |
| `R0623` | `C:\Users\ala\Documents\shploingus-game\crates\diffusion-core\src\legacyledger\ledger.rs` | 9513 | `25859d211e19ea7e088a353e8d7f0c6078d62d916ce6de6c5e0e1bd88c4d012d` | cadence, policy, ledger |
| `R0624` | `C:\Users\ala\Documents\shploingus-game\crates\diffusion-core\src\legacyledger\mod.rs` | 2141 | `c6b51af9706a2afd76d6474c23fcbf4236954735b73b9ab9c2167e543d67f790` | policy, ledger |
| `R0625` | `C:\Users\ala\Documents\shploingus-game\crates\diffusion-core\src\legacyledger\resume.rs` | 18451 | `8c45d96dc90695abf406d1e232fdc319ce81fff3765b1db2e71c78a26ef857ae` | client, policy, ledger |
| `R0626` | `C:\Users\ala\Documents\shploingus-game\crates\diffusion-core\src\legacyledger\store.rs` | 3831 | `6cb32c4ccb932882f7a008f578827bdfd264d4a45ae88e242eb3778ea3e1445a` | ledger |
| `R0627` | `C:\Users\ala\Documents\shploingus-game\crates\diffusion-core\src\legacyledger\ticket.rs` | 26700 | `a89b494e5e9e2672bac3e11eab2b56f7aa9519ec92b5fc5c0022fb4acfa95ec2` | cadence, client, ledger |
| `R0628` | `C:\Users\ala\Documents\shploingus-game\crates\diffusion-core\src\world\coord.rs` | 16644 | `0d6bc38ad6f4add6f632bfed360debc33a9a08403af54d92ccfc2c4531ad3abb` | policy, ledger |
| `R0629` | `C:\Users\ala\Documents\shploingus-game\crates\diffusion-core\src\world\field.rs` | 108573 | `ead2f3067654ea4960e624eff019d81b22c1346a6c91d3990389e40b6f6ab8d3` | cadence, policy, ledger |
| `R0630` | `C:\Users\ala\Documents\shploingus-game\crates\diffusion-core\src\world\horizon.rs` | 30873 | `2ae795082d34b0caff243f7e4e736a3c39fc25a17ae8e29c2d0d203527d4b03c` | format, policy |
| `R0631` | `C:\Users\ala\Documents\shploingus-game\crates\diffusion-core\src\world\identity.rs` | 23205 | `a3fac1bbcdd66a2458bf14478f872d8022a1966219a5fdc5febd25ed53387896` | policy, ledger |
| `R0632` | `C:\Users\ala\Documents\shploingus-game\crates\diffusion-core\src\world\jobs.rs` | 43855 | `c896644e593f08ee02ba798035f494631d2700fa51f7329fe15659fd935f5d7a` | cadence, policy, ledger |
| `R0633` | `C:\Users\ala\Documents\shploingus-game\crates\diffusion-core\src\world\mod.rs` | 7927 | `bf7f5ff77e140158ca3fde9ea298a576257cecf3feda4091afc7f47c13c6a8e4` | policy |
| `R0634` | `C:\Users\ala\Documents\shploingus-game\crates\diffusion-core\src\world\pass.rs` | 45081 | `ec26ed42e118007dd8e4b294cffb07d08c4f22d0bbafa41f026bed0da9b27037` | policy, ledger |
| `R0635` | `C:\Users\ala\Documents\shploingus-game\crates\diffusion-core\src\world\pool.rs` | 8248 | `5fcd667da16ec339a274be46b2dd1a67e6b14204868571d1493563821fed6cd7` | cadence, policy, ledger |
| `R0636` | `C:\Users\ala\Documents\shploingus-game\crates\diffusion-core\src\world\PROVENANCE.md` | 18489 | `951c5d6641d9d3200b8fbb7f8fafba1c51e38e43aaafaf1ee4c119326c6ed050` | cadence, client, policy, ledger |
| `R0637` | `C:\Users\ala\Documents\shploingus-game\crates\diffusion-core\src\world\residency.rs` | 34653 | `85d56b684c40ded3fd7daa1f840e22748914ffcd4303936c2c918e289707dbb1` | cadence, policy, ledger |
| `R0638` | `C:\Users\ala\Documents\shploingus-game\crates\diffusion-core\src\world\stage.rs` | 8909 | `a04e48dd03ec1927818f4cd78b5bbdb3f39dc267a5a918499e083cbe26b44aac` | policy |
| `R0639` | `C:\Users\ala\Documents\shploingus-game\crates\diffusion-core\src\world\stream.rs` | 39021 | `1bd054ae02e512db4cf67529be1e31b21c00aace8f06d35f5a89b66941eff0a0` | cadence, policy, ledger |
| `R0640` | `C:\Users\ala\Documents\shploingus-game\crates\diffusion-core\src\world\surface.rs` | 20481 | `2e67e3b834110c01b66b87f6ffdc7353e990e1c562318ce5702660ecfc36fd21` | policy |
| `R0641` | `C:\Users\ala\Documents\shploingus-game\crates\diffusion-core\src\world\UNCERTAINTY.md` | 36495 | `bbe4f89f0175f1ca6399052e020aa04e8687f4d5713a555e644ec89ad8f6edb2` | cadence, policy, ledger |
| `R0642` | `C:\Users\ala\Documents\shploingus-game\crates\diffusion-core\tests\ask_gate.rs` | 12666 | `1535068878464464c58d97ed7e3a05fdb0ce4e94ea37b96b3386a9bd7bf18ada` | policy |
| `R0643` | `C:\Users\ala\Documents\shploingus-game\crates\diffusion-core\tests\emit.rs` | 10483 | `d301cea0de69e51447198b7a5079b365481b27d3b444c92a1ab1e4579cf696f4` | policy |
| `R0644` | `C:\Users\ala\Documents\shploingus-game\crates\diffusion-core\tests\lint_gate.rs` | 15528 | `8edc4a7b86c9b4ce4e6ea021a7867a02fadb6ab4db1cb97f28b3970cad154026` | policy |
| `R0645` | `C:\Users\ala\Documents\shploingus-game\crates\diffusion-core\tests\real_patch_corpus.rs` | 5049 | `0a317ad853b41809c83805124c30df9991ed2327176a3b2bae48578078ffdd8b` | policy |
| `R0646` | `C:\Users\ala\Documents\shploingus-game\crates\diffusion-core\tests\wire_upgrade_stability.rs` | 11191 | `679f17c85485393fe6393225c2a0d094f78b6c17dccd577f53b0b57c7f184232` | policy |
| `R0647` | `C:\Users\ala\Documents\shploingus-game\crates\diffusion-core\tests\world_generator_identity.rs` | 14908 | `2699e3cb749b6aa8817df0d3a187477bd69771362006f68036df61f53706103e` | policy, ledger |
| `R0648` | `C:\Users\ala\Documents\shploingus-game\crates\diffusion-core\tests\world_generator_pass.rs` | 20693 | `a7aa07e6ca6b115e9cc9995d16738f09af75b1ca73e14c85b38dc22fbd2581e5` | policy, ledger |
| `R0649` | `C:\Users\ala\Documents\shploingus-game\crates\diffusion-core\tests\world_horizon_separation.rs` | 10191 | `fb625e78a5784372872ce6e60365b0edf2914397aa162fcedc18acb81ee2a6a6` | policy |
| `R0650` | `C:\Users\ala\Documents\shploingus-game\crates\diffusion-core\tests\world_regional_fields.rs` | 34285 | `56d19b633f98e4519c252703ff47b821a1bbcd148826e81f9b3e7252e644bc92` | policy, ledger |
| `R0651` | `C:\Users\ala\Documents\shploingus-game\crates\diffusion-core\tests\world_stream_residency.rs` | 30077 | `c4520a1f60451513b4bc11cfbf7e076b2152fba8e88b5e236c469897db2cdfff` | cadence, policy, ledger |
| `R0652` | `C:\Users\ala\Documents\shploingus-game\crates\diffusion-core\tests\world_worker_determinism.rs` | 5497 | `0042d98ac362837183e4a31448c664c5614c9e24683ec3b0acdd015ded894e91` | policy, ledger |
| `R0653` | `C:\Users\ala\Documents\shploingus-game\crates\diffusion-envelope\Cargo.toml` | 2062 | `91d5cde74e36f649d57198e2af391f76c53548cf66f604b4cf3573bebb562631` | policy, ledger |
| `R0654` | `C:\Users\ala\Documents\shploingus-game\crates\diffusion-envelope\src\lib.rs` | 21305 | `afddea3cd75b0d5212a09982b56c6379c7e5169ef1e72683fcf4fa833ba33d70` | policy, ledger |
| `R0655` | `C:\Users\ala\Documents\shploingus-game\crates\diffusion-envelope\src\seal.rs` | 20851 | `434a5671fe87ecd4a0ed57390145952d2e15fb4c4a736a8d7d45851f49641eeb` | policy, ledger |
| `R0656` | `C:\Users\ala\Documents\shploingus-game\crates\diffusion-envelope\tests\envelope.rs` | 19209 | `f97046760f21041fcd5ac73916c2252e0fa6312797f1664b7397efef684a6080` | policy |
| `R0657` | `C:\Users\ala\Documents\shploingus-game\crates\diffusion-envelope\tests\pqc_envelope.rs` | 19706 | `c31d4be23ab0558b5568e3e573cd0f261f89224d6cebe30d38a12ce7e0361960` | format, policy, ledger |
| `R0658` | `C:\Users\ala\Documents\shploingus-game\crates\diffusion-sealer\Cargo.toml` | 1508 | `98bd5527beec882b774f1a70be9b599fd269aefebfa31dac464598ae496e09d9` | policy |
| `R0659` | `C:\Users\ala\Documents\shploingus-game\crates\diffusion-sealer\README.md` | 1831 | `28267d8c352c08131b3740a861bedddf63a1b2986fd06bb93965c6bcb8c5ee95` | policy |
| `R0660` | `C:\Users\ala\Documents\shploingus-game\crates\diffusion-sealer\src\main.rs` | 14780 | `9d55e8bd96d51e15f00e70a6482a3c808f027a718dca3a6944a6c3a68ec20375` | policy |
| `R0661` | `C:\Users\ala\Documents\shploingus-game\docs\evidence\personal-evidence-engine-mongodb-build-spec.md` | 53447 | `a87ce2a88dbf2315c620a89350745fe964234efe784f4d717297f7709b45e4ef` | policy, ledger |
| `R0662` | `C:\Users\ala\Documents\shploingus-game\docs\evidence\season-2026-s1-reconciliation-corpus.md` | 8781 | `cc3b5e2652fb2403bddba2de26de1bacb83e85dd72e1b66b5f11f077871bbe6e` | civilians, cadence, policy, ledger |
| `R0663` | `C:\Users\ala\Documents\shploingus-game\docs\evidence\screenshots\INDEX.md` | 21674 | `813e29da65fbe65a78b8ad56cc5e072f83ffc4e9348109f8b0f1bc66b51eb012` | cadence, format, policy, ledger |
| `R0664` | `C:\Users\ala\Documents\shploingus-game\docs\plan\00-authority.md` | 235174 | `5f172247adabbc9bc5656637fb6709d4e3a19871bf5b0eb8f58542e8b3941251` | civilians, cadence, format, policy, ledger |
| `R0665` | `C:\Users\ala\Documents\shploingus-game\docs\plan\01-reference-inventory.md` | 21693 | `561f19543886d26b2f1daa82088edd1031ecc38a617bcb684a83e2e33c1d8eb5` | format, policy, ledger |
| `R0666` | `C:\Users\ala\Documents\shploingus-game\docs\plan\02-diffusion-core-v2.md` | 26145 | `4065a06b3205eeb95de6825927b16b2126c0729892dd6b54dac881a3b3f34b52` | format, policy, ledger |
| `R0667` | `C:\Users\ala\Documents\shploingus-game\docs\plan\03-milestones.md` | 28438 | `d14ebbb515fdb6acd6f4ea81a81af5462175f27009677eb39772d5f8bec3be46` | policy, ledger |
| `R0668` | `C:\Users\ala\Documents\shploingus-game\docs\plan\04-verification.md` | 14658 | `4a04fdd2603ed2e41c66c1102977aacdd7543e73e0abd3c7eeaea3a6ce61e503` | policy |
| `R0669` | `C:\Users\ala\Documents\shploingus-game\docs\plan\05-blockers.md` | 93017 | `c41730dd713eaa668ca2d4bb2abef5d45a2e464243848c67dd59a0bcf16f9018` | civilians, cadence, format, policy, ledger |
| `R0670` | `C:\Users\ala\Documents\shploingus-game\docs\plan\06-m0-baseline.md` | 9817 | `1d48df7293591377e14fd44e46716450619900fc3ad2889f677a8c6f3b4367e2` | policy, ledger |
| `R0671` | `C:\Users\ala\Documents\shploingus-game\docs\plan\07-correction.md` | 20208 | `6b2da039ea179bd7bfa5b3f5a6881ed313e1f0e5c86ed9525e2afc0d2a6a845f` | policy, ledger |
| `R0672` | `C:\Users\ala\Documents\shploingus-game\docs\plan\08-live-tree-collision.md` | 11085 | `8bcfe264c8aaf770189ade0af74c48051ba34f12c0a391d001e0d8bca0a76a88` | policy, ledger |
| `R0673` | `C:\Users\ala\Documents\shploingus-game\docs\plan\09-resume-builder-integration.md` | 12911 | `caf49e406d3d3f2be1e2e56725e9cf170591c097bf7a622508df175942e06d12` | policy, ledger |
| `R0674` | `C:\Users\ala\Documents\shploingus-game\docs\plan\10-resume-ui.md` | 19635 | `d92cb235a1f5e7037ddad2b71a2cc50c5f5e0666864fcd2530d7a9252b8461ad` | cadence, client, policy, ledger |
| `R0675` | `C:\Users\ala\Documents\shploingus-game\docs\plan\11-build-order.md` | 24572 | `55ff4902ea45463d5b05df857264824fc2af2cb7f14aba38ca387b640fe1ffb8` | format, policy, ledger |
| `R0676` | `C:\Users\ala\Documents\shploingus-game\docs\plan\12-pq-signature-research.md` | 19301 | `cb2c8a9678dcb2f107b8e9aa3fee765739d2df1b38053fa0481707cccaece9e4` | policy |
| `R0677` | `C:\Users\ala\Documents\shploingus-game\docs\plan\13-world-and-surface-integration.md` | 54161 | `b1c3898acffa1f156ccc445308e370b1cdd5bce5dae28f409b506d297c245d57` | civilians, cadence, policy, ledger |
| `R0678` | `C:\Users\ala\Documents\shploingus-game\docs\plan\HANDOFF-ROUND-36.md` | 14335 | `b9db44f89637658ea3ce70714a36d516ee43224d6ccd2f79560ed2ca4a4e180c` | civilians, policy, ledger |
| `R0679` | `C:\Users\ala\Documents\shploingus-game\docs\plan\HANDOFF-ROUND-38.md` | 14588 | `fcfceae2809fc15bb258d65539b6a9653dd7feee918da0cf3538eee65c6aa96e` | cadence, policy, ledger |
| `R0680` | `C:\Users\ala\Documents\shploingus-game\docs\plan\HANDOFF-ROUND-41.md` | 8342 | `6bb4496e6e4f07ffac4f5765304c6c0ec37a02388885b1047eefc28cdc2181f3` | policy, ledger |
| `R0681` | `C:\Users\ala\Documents\shploingus-game\flow-specs\01-mods-package-api-window.md` | 9698 | `217ad58d4d4074b7eecc228d3e6f61c598508516dc5feb87b45a23deb2063971` | cadence, policy |
| `R0682` | `C:\Users\ala\Documents\shploingus-game\references\portal_simulator.py` | 168617 | `7acffebbf9436b37f1862f8fd63733fa56bbb9041b35a632bd4b011e3cc6782f` | policy, ledger |
| `R0683` | `C:\Users\ala\Documents\shploingus-game\references\ala-landing\_subs.json` | 64164 | `7c3f424856f69c454ba6241140a6bca77b8fef2ddb886871d25544c2074064fb` | client |
| `R0684` | `C:\Users\ala\Documents\shploingus-game\references\ala-landing\tools\a11y_probe.mjs` | 10970 | `6e55170d66ee7caf2e7ff7d72f9a86dc6b1653021fde2988479d16b85c4be765` | policy |
| `R0685` | `C:\Users\ala\Documents\shploingus-game\references\ala-landing\tools\catalog.json` | 20011 | `527f460da26fc01489846e7e28b63c49bb14062f78bd3cd1eed46ade6b80f2e8` | format, client |
| `R0686` | `C:\Users\ala\Documents\shploingus-game\references\ala-landing\tools\content_match.py` | 10139 | `54063bab7356dfdfb8788c10a6d94d759d16a9119945ab541773a5bd8891efc4` | ledger |
| `R0687` | `C:\Users\ala\Documents\shploingus-game\references\ala-landing\tools\drive_gb_matches.json` | 4865 | `f34b869b4fba28ace1d2fcecc61266851c35733278ce97eb972e2f797431f51c` | format |
| `R0688` | `C:\Users\ala\Documents\shploingus-game\references\ala-landing\tools\drive_index.json` | 25428 | `47484545c1b56352bc7251fa1daa0a58c355ca43c9d8bd58893a508de2cc0632` | format, client |
| `R0689` | `C:\Users\ala\Documents\shploingus-game\references\ala-landing\tools\drive_sync_config.json` | 5489 | `e459bbcce9025758c00a31256e0ea08f8a2884bfabf2b1e0d72eeaa1321293f2` | format, client, policy |
| `R0690` | `C:\Users\ala\Documents\shploingus-game\references\ala-landing\tools\gb_author_mods.json` | 43904 | `5b0bfd23495ab1c34e180ca47b7d7d4eddcc9291098198b0cea4cf6e4195c0ed` | client |
| `R0691` | `C:\Users\ala\Documents\shploingus-game\references\ala-landing\tools\gb_payload_hash.py` | 2976 | `60aa69f430b99abe1ef8ee1dfd758ca9e5241dff69025e1bfa95e84455bcbe91` | ledger |
| `R0692` | `C:\Users\ala\Documents\shploingus-game\references\ala-landing\tools\gb_payload_hashes.json` | 13757 | `f05ee3a0d8ddea832f82eb0b9e70ae3568d74067d8c0a9830843802b0919aca7` | format |
| `R0693` | `C:\Users\ala\Documents\shploingus-game\references\ala-landing\tools\gb_vpk_fingerprints.json` | 62943 | `02dbe2fe09427fd0b9a5a990656780bc02d7788e499e778557aac30864213ed9` | format, client |
| `R0694` | `C:\Users\ala\Documents\shploingus-game\references\ala-landing\tools\model_preview_manifest.json` | 87784 | `f051bfa7e49678d5a7474c8fc69af81c88b30748f2fc606564b0a9d8b7244005` | health, format, client |
| `R0695` | `C:\Users\ala\Documents\shploingus-game\references\ala-landing\tools\preview_map.json` | 9127 | `8ec0df2f6058072e0ef891b643f7dd6d620823614abc6538486ea7f978e9b1da` | format, client |
| `R0696` | `C:\Users\ala\Documents\shploingus-game\references\ala-landing\tools\probe.mjs` | 19903 | `304b2af8c9572593589a363b53687e70c6c703e0a3bf26ba2288da683f61c7f9` | policy |
| `R0697` | `C:\Users\ala\Documents\shploingus-game\references\ala-landing\tools\thumb_map.json` | 1769 | `c80651f81850167c6e14ec1f47a4f844f7cc1476f39c91dfae2d9eaa04085dea` | format, client |
| `R0698` | `C:\Users\ala\Documents\shploingus-game\references\ala-landing\tools\update_preview_manifest.py` | 5908 | `e9d32d1820c2e8e9993ca065d645420eb4dae8905b0c6e77a34f403d1c63b049` | format |
| `R0699` | `C:\Users\ala\Documents\shploingus-game\references\ala-landing\tools\vpk_identity.py` | 4764 | `f8427b4811fe70715984d476afac4cde53d37aca600078311043d52a49301f6f` | cadence, format |
| `R0700` | `C:\Users\ala\Documents\shploingus-game\references\ala-landing\tools\vpk_scan_results.json` | 209740 | `309921cc7b37a176a6ce9d8b58795c0dcbb0e1b145c5947734f7b538222052b8` | health, format, client |
| `R0701` | `C:\Users\ala\Documents\shploingus-game\references\ala-landing\tools\vpk_targets.json` | 2346 | `da941ff975aca4f6b9baf682a15fa1c32eba647cfdfe53b33082472646031a9b` | format, client |
| `R0702` | `C:\Users\ala\Documents\shploingus-game\references\ala-landing\tools\vrf_export_glb.py` | 8005 | `f00225ac304f771588e5ec6a5bc4b0841da8bfd926ac39d10c167466bee83cba` | format, policy |
| `R0703` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\AGENTS.md` | 21481 | `70cffc7041dfa70b6038793d8aab6bc2a7a8d38c45d61cdeff9ff7c7c2936add` | policy |
| `R0704` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\package-lock.json` | 69026 | `e13c1b0797d69b1d15b6eb63ba09fbf2feb27a79afc19437c95850dc0b11cd62` | format |
| `R0705` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\personal-evidence-engine-mongodb-build-spec.md` | 53447 | `a87ce2a88dbf2315c620a89350745fe964234efe784f4d717297f7709b45e4ef` | policy, ledger |
| `R0706` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\README.md` | 25718 | `2ee77274d7c7a467cc7428f20554c0d8c26fbd21a097125877c006d033e82a6f` | policy |
| `R0707` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\.agents\skills\impeccable\SKILL.md` | 11666 | `c02feba25a961a72647ad317aba2d65baeeed53c4cdcc072f25bb37f4d867d43` | policy |
| `R0708` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\.agents\skills\impeccable\reference\animate.md` | 5236 | `94b4ce6299fea93d9f256b2d25705961a76bc5ea940c56db4145686ebc99df1b` | policy |
| `R0709` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\.agents\skills\impeccable\reference\audit.md` | 7873 | `57402ef6fd9d0745f8c60d778f77da83a8b16edf751fa1013598a0f6e5f0f541` | health |
| `R0710` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\.agents\skills\impeccable\reference\audit.native.md` | 8364 | `fe91fcf28638f95577af481a50edaf339d6c9a3ad3b9fa477bc81c116b8bc392` | cadence, health |
| `R0711` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\.agents\skills\impeccable\reference\craft-floor.md` | 4484 | `96e2e6bd4fcf9a2c6da65fb029f96d9176308fae2efd9d8653d3b8d838960e07` | policy |
| `R0712` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\.agents\skills\impeccable\reference\critique.md` | 42722 | `88749ebbe9bc87250765a07c2b959508262bd0e276ad60baa53e6e48c3579143` | health, policy |
| `R0713` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\.agents\skills\impeccable\reference\document.md` | 27433 | `7848f40e224cf520bd8554943c9816a1ff8c97b1db57af0844e3b1ebb223d91f` | policy |
| `R0714` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\.agents\skills\impeccable\reference\harden.md` | 8539 | `8a1c872773996dfa1c1eb765ac7ed8e8d41f99d4f12f090b4725b694e85eaa62` | policy |
| `R0715` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\.agents\skills\impeccable\reference\hooks.md` | 13312 | `356cfa0ebf61589cf5d52691d101a69d69256062fe1d11d71d95d41a78289cbd` | cadence, policy |
| `R0716` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\.agents\skills\impeccable\reference\init.md` | 11448 | `ac695dd89d5f1261004cfa966526f5d5e913c92fa0640d4d71cb42493effad08` | policy |
| `R0717` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\.agents\skills\impeccable\reference\layout.md` | 5161 | `904859c8160b02330b04db23a8eeeb4ef55bcaa10f5208b8d73a1718334633e7` | cadence |
| `R0718` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\.agents\skills\impeccable\reference\live-setup.md` | 8186 | `29f741b71e75fd39c65ca6df4b01b5f6c4f3c4c7adf23b47a3220ce2c0251f24` | policy |
| `R0719` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\.agents\skills\impeccable\reference\live.md` | 36245 | `eaa50e8cd95e00a94a257db2bff4eafd820696ba75a08a384a00517c3402924e` | policy, ledger |
| `R0720` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\.agents\skills\impeccable\reference\new-work.md` | 52769 | `a5371492582dbeb69b24a1a2947b256a2da8a4d55917af709bbab6e452d9d23c` | health, policy |
| `R0721` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\.agents\skills\impeccable\reference\overdrive.md` | 9090 | `96e508039c719c0815701c36b8418b18baee1967f915fa29b23b84861ae8ea94` | client |
| `R0722` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\.agents\skills\impeccable\reference\shape.md` | 3547 | `a55f016c046cb6a27c55bd7f346375aeb506a755c4fbca19a5f92dbd42309c23` | cadence |
| `R0723` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\.agents\skills\impeccable\reference\visualize.md` | 11757 | `cf3ae16765e7b5bc333ef76e24ab37f080e3d62e931c4986158e3cbcda6b9f7a` | health, policy |
| `R0724` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\.agents\skills\impeccable\reference\degraded\asset-producer.md` | 7306 | `13bd27aa8573e6d45d8bbf9f3fc991e4719d28a7e8f709009a4a5a49a227fff3` | policy |
| `R0725` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\.agents\skills\impeccable\reference\degraded\documenter.md` | 3325 | `bcc05ea92faebb5c74037a9d4263a5ce9a56f5ab07c8ab3c59ee704d8cade745` | policy |
| `R0726` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\.agents\skills\impeccable\reference\degraded\finish-reviewer.md` | 15397 | `5f24c5a97b4ffcabc7c432b064cfdd04c7a2ad52f52e765be648dc0aadab8f38` | policy |
| `R0727` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\.agents\skills\impeccable\scripts\live-browser-ignores.js` | 10346 | `c1cb6877ca99a0c1b38ba0c7d59f32702d3022f6821d8045f7133f7c40b6362f` | policy |
| `R0728` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\.agents\skills\impeccable\scripts\live-browser.js` | 522871 | `7af0a8665057c83b39bca2c8c7427ef2343734f70d4128c377113a6726a1e3b1` | witness, cadence, health, policy |
| `R0729` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\.agents\skills\ponytail-audit\SKILL.md` | 1693 | `49e835c96313009179ec162d80ccc9d91625e387c8af7cd3975c531ba105b2d5` | policy |
| `R0730` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\.agents\skills\ponytail-debt\SKILL.md` | 1747 | `c0a5c0c0cc843cb53f15b792790946768500b45538d07fadbf0602ed6af63a47` | ledger |
| `R0731` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\.agents\skills\simplify-hard\SKILL.md` | 4939 | `044b96aca37e8bfe5e88d071843c18ff94a9e2ae1edbcfe86abcf0911beeadc2` | policy |
| `R0732` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\.agents\skills\user-flow-specs\README.md` | 8274 | `92d9484d2422e7bbcd8372724bc008bc96e74d6abdb80c1460ecbe82fb86f845` | policy |
| `R0733` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\.agents\skills\user-flow-specs\SKILL.md` | 11743 | `b9eae2f6f5f4d75297a31dfa19dbdd34ba6f6b15cb402eb31fca091eefa95f77` | policy |
| `R0734` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\.tmp\check-export.ts` | 422 | `04ab520963079529b9ca0825e265899e5ea19469b676470da31065b18a7cfa28` | policy |
| `R0735` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\agent_data\browser_profiles\linkedin\Default\EntityExtraction\domains_config.json` | 131657 | `4e88e274ae93bffcd9a48f1d61ca4c0a2a0bed9abf1037461e888f2571ac97dc` | health, client, policy |
| `R0736` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\agent_data\browser_profiles\twitch\Default\EntityExtraction\domains_config.json` | 131657 | `346f8ace9a294d518d5b32b7d84e76ee112686d02f847b9cd4717f90ee68ccce` | health, client, policy |
| `R0737` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\agent_data\browser_profiles\x\Default\EntityExtraction\domains_config.json` | 131657 | `5b6eec5d2f306aefe47c7e39ed01eb013befacf3202850ce8344a5e3cafb011a` | health, client, policy |
| `R0738` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\config\identity.yaml` | 5208 | `47a784d88b378c2521f745ef7e93f5870c716c8950820fab1bdf498f1cd7cc88` | policy |
| `R0739` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\config\models.yaml` | 4732 | `64ab9835c2f595e65a8c9607ec31135f83fe99be798141569fdc46a2737fad9f` | policy |
| `R0740` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\config\policies.yaml` | 13650 | `c2ee9f2d5d9c6e261fef38c2c7f822f03c01a41b27e8a94cf6ce3b59cdcfbab6` | policy |
| `R0741` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\config\sources.yaml` | 15001 | `6ee9124f148b6e103e01215313460e3bbbbd69b3b5f6ddaa3f147457fa360ae8` | policy |
| `R0742` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_git\2026\09\14\14d139425ef7b7e25da9a65513933ab155141c2c756da088242dd3fc9c7a620b.meta.json` | 327 | `31b5c15d79ccc277dd70c89bff7b1446d8b182243e8670ca18833c1f83ad9905` | ledger |
| `R0743` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_git\2026\09\4c\4c34115580486236aa6292ea682b79b513153d46ad5b027597cf37c4d275e399.meta.json` | 329 | `64abcd20e6cbf2cd09d6cf3e6080df746ca1204f48786ec0813e53b76786526e` | ledger |
| `R0744` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_git\2026\09\67\670d667f7af7515988ec5af75c25cbefc4adf647880a03756a6a753c2c626649.meta.json` | 363 | `12239b8a7e11c98d969e7b23dad7cdb76e93a95e6457e953cf53c870cdf33a40` | ledger |
| `R0745` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_git\2026\09\77\77ac9bef1b836186b99106e82c058f486df783c3d2498da310e97001420b9be8.meta.json` | 332 | `73d9f6ed4ae6c45f19a50b12b724909032ec3e8058ededab2776acbeecb3364c` | ledger |
| `R0746` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_git\2026\09\b6\b6796817c37db0fe8ba16034b9398e5f59d101db7e0952e2981d4087207d835f.meta.json` | 332 | `74a35b66eef915c4c5fa7617c028e7018a8d389a526c93a50044dc83d04f1e0a` | ledger |
| `R0747` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_git\2026\09\e3\e3a55052a296fd270cac9d7c32f9769842710366aa8669fc4af0911ef2f1e176.meta.json` | 332 | `f76d649aa230ec4effd8deebe3efed03a990fa84b42afe5991c4b44162a9987f` | ledger |
| `R0748` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_git\2026\09\f3\f3ccc5c015edf3f3c86c75d62720f521bc4ea91e4b5e4d57436ca6d6a77b4136.meta.json` | 327 | `6b6a3c2d10a104276d45b59bc90e3c9af0f51d08f5d4413b6bcbf86eb4cd3d64` | ledger |
| `R0749` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_git\2026\09\f7\f7549a05b9f7e0ce87839ac96c963a87994e3d3be210394072ee877b32f7732a.meta.json` | 328 | `fa72962730d853a9b72d80ebb6ae2bda93109c8126b6eee98df819aed545409e` | ledger |
| `R0750` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\00\000c5f42c5859a83dd6aaf895b5ded5a73db64122253ca8b0567d689080b4370.meta.json` | 380 | `5bbfb8a432bc78f7d55e61ef2d8cbc38f5aafe77dde30fa9f32e7a8be6cec6c0` | ledger |
| `R0751` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\00\002b177759aca8d0a2747557b2eecb1d44abf0d81aca970e290e0a1be67fc093.meta.json` | 387 | `a6b75a3411cc7ff0f777b5676ebb14589503423b92e88b82d5dc9667e17d9e1e` | ledger |
| `R0752` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\00\002d522690504f7af41f28a432ad2324c9bd3c9829e8d2fc8818d7888e256d84.meta.json` | 374 | `c99953b41a00ec4605044411f325f422009d842ba60a4f1c84dbae09aea1efd4` | ledger |
| `R0753` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\00\00318aa75cadfa4ef414c295ead9ea0aa79c07ead2273a7e590b03ecb3cbfa48.meta.json` | 375 | `2b1ff7a44dd363c4c42fb9d3c992be5845da03e68c1adaea884ca225ec11e273` | ledger |
| `R0754` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\00\0038ace336a755b0007bc25451f2defaac9b0f71cfba37ae537dfd1b35fef646.meta.json` | 362 | `112761732c8e8861be4dbb558d25ff1763682ecf29e9ddb9af8aec212de65f13` | ledger |
| `R0755` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\00\003ae7dea25fa05f7aaf2eb979340a94f3501428e48eeefe148572cdf4b05af1.meta.json` | 382 | `64f7877f5a1cbf1a59a08c38172b01fbcf2186eab8d547aa3df971deb4eb6ccd` | ledger |
| `R0756` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\00\004161da976ac2626474a56ca309acd156bcc3cfa22a1b119391eee5e6a35b24.meta.json` | 410 | `6223453fb9934b9ce8d65b6346242816a67b9f058e83c8c1aa0b2bc338d8bbcb` | ledger |
| `R0757` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\00\005f9a0913254590ec0bdabdc59d3fee90f341176905b60f3ea7e3f8defdf7c9.meta.json` | 399 | `6dd67acabf654ab58486fab2dabfc7513f3819a981821af17554fc0daf6c3895` | ledger |
| `R0758` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\00\006a0d0a5c4592d18abd83ff9aa71bb8e63c76e2b335a33a63c3e998ac905dfb.meta.json` | 393 | `09f8d5fa387a4fe532b6f44e628fc303bf9a6f92278f5d8c4fcb9044c58bfeed` | ledger |
| `R0759` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\00\006c151bdc8ebec965e2c75c21f515a4db29512ee8087b15c72af2f42ddf51fb.meta.json` | 392 | `ca7debbfbc18af56f1cebf8771b9c4d79efc3be2b89c0809a9e37ef559c7e80c` | ledger |
| `R0760` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\00\006fcc60663a3e27ca1a481a88e4ad761f14ee2918d2adb3ab7724200e3935e2.meta.json` | 351 | `e6bcd921c0050245bd6148a2c38758c6d8506ba6bcfbb640adaa9fb9ab38e42f` | ledger |
| `R0761` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\00\007bd42512a93d75ae1be61e333e36fe52c86475dcd7e6d1678a7aebd6946895.meta.json` | 387 | `844956563279170038d9374ca048d2e280a0613fb019c54bf9786b9df3153e41` | ledger |
| `R0762` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\00\00811a091704967e700bb5f70bcbe9ed39a6a71b9a1fbb7ddd40a98716f14490.meta.json` | 441 | `e481c9fa8fb5f83248745d12bdfc835a07006e6cdd3d68bc65b7be9461f4900c` | ledger |
| `R0763` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\00\0089a36095b13ad0e473428a73a6381b3ebbedc83dd5c68c0382fde01f456448.meta.json` | 388 | `600c52028eae35ef5ef8eb03d7a496b6e1aa9b2846dfeed38e6d0e8124d52b5a` | ledger |
| `R0764` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\00\008f98961ab455025e654c0f6d931cc9216be4b9a1189af5b0e0ff67398d957e.meta.json` | 388 | `01461d588ee324d2872930bdc83464133d1c5a0b7f623fd18cfcc0b34727dab7` | ledger |
| `R0765` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\00\00adf88d3d8e5afe19559918f77761f8b99172c33e5aafca342682f0c1371ec6.meta.json` | 386 | `5dac4970a7bfd8204479331afdf2603af76c2e82b6b2ae7e3146575e9c5b0e3e` | ledger |
| `R0766` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\00\00ca215b5fe1da3957f183c71ffb0c9bc9464bc45e502d119321c04187b693c2.meta.json` | 400 | `c1b5df9773a769aca5ca864a2f664bd4b645f866296d2c469b46af42d3703b8b` | ledger |
| `R0767` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\00\00d607671610569f4194e41838753902b0cd548a53165e0a95ba1c6150569c5b.meta.json` | 387 | `a4845127800b1ee8f0507bd6132c4def765e7327aa9dddc43270fb61c928c2e9` | ledger |
| `R0768` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\00\00e20588471f2455caa9018885d958480c3d23e6d8f087eb421450fc0f6b3c18.meta.json` | 382 | `03b4da452e26d6fe33db4855022cf53c5479f0d0f1047b93f45aa6ec645de939` | ledger |
| `R0769` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\00\00eec93c2cfafa068dd6d8552d73019ed1260cf55816014d1b5a0ceb5fec6a75.meta.json` | 382 | `3906fe78333c1310894a381e2488f8a02aa8593fc71f0a6ce9ca783bc5c58426` | ledger |
| `R0770` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\00\00fd809b67f271712d20423c07b45081c51c227b6f416b9d27d584dedcb62de2.meta.json` | 377 | `1d9c811fda657486474857277968f8e89b0b2b009b27240873305a4f7c32d3ea` | ledger |
| `R0771` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\00\00ff160d74873db72ab06cd1391ca21cebcf0d8ca898c0d7942fa8505577e324.meta.json` | 396 | `445e9bcbeea4ed9b1fffb214e51e077793cc9265f41fb7921bdbe44bd7433953` | ledger |
| `R0772` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\00\00fff09229097149033d41af4cdc9dbfb83447b0615b5bbf7d51cd296ed32722.meta.json` | 385 | `61e5bca3346ab40d721e3cf27b9e297fbe752d6db85aa550bae6e59b346490d8` | ledger |
| `R0773` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\01\0118c528f257fe9076293ad25021f3fe237f526ac1df14432ad51b21ea535fe4.meta.json` | 448 | `5ec919905f588e88105aa005994d3a93bf356b5e4e0e43cad182e7687dc68bbd` | ledger |
| `R0774` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\01\0131443478b37e449b791a779fc884ab4be3a656b83f3496fe16b38a7277088e.meta.json` | 378 | `5c98d96d81ed778ec146939ea8cfbf91f586b4982921e591962360c8c07497d7` | ledger |
| `R0775` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\01\0134c1d4b05c39c94c0c1d32b32941a43eb91712e3752085d559fdae818c3e50.meta.json` | 359 | `f76384f1eb8b1b5bfe7928e6777aa7625aae783075742389fd7cb5812ee84d60` | ledger |
| `R0776` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\01\013edc4f722cefd8315561792bcbc1c708785c18d7b72e46d547f144703134ee.meta.json` | 400 | `0c0b4f7d0d42164107e9ef416755dcecbd6c8e3e5e913f778e0504de1662ae80` | ledger |
| `R0777` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\01\014b2dbefa7cd09fa2150394d342aa187d8d682788411a9c575607f6c6e3c449.meta.json` | 390 | `0764a74781cb79a37757cf472219743d389943ef30f1c634935dd320c8e6501b` | ledger |
| `R0778` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\01\015a92e17eb83e0d5a7a45e73984687898a02000d6c0075b76d1bff5b93fdfe7.meta.json` | 386 | `f7c981258c4edb78d20f774fa6b3a78eb0a7b8dcb4b274b8d8ab348b66f58f7b` | ledger |
| `R0779` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\01\0174002e7dfcc44438747992dc39bac025fb9faa7c627d5c3dec40b062b049c6.meta.json` | 390 | `4adc2a63bc20ad3da692cc8a7d0a82fd4f9acaff7e266d886b8d721aafa67813` | ledger |
| `R0780` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\01\018cb758d27744f03611dd3f8a0e6c9985e917984bf6373633134bb5291e4d43.meta.json` | 389 | `7c849bdb6d5657cb5569f8a452b31b1667c3d0697bf87d1b54f07988ae6190f7` | ledger |
| `R0781` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\01\019536e74a7198ed12b6957524dfe0b2a2bfd4c9ac3219dd755e215c0a073c08.meta.json` | 379 | `2a1d863321d33c3fc008f02f6c95c163b726d79a8d843087ef244f4e1a80d197` | ledger |
| `R0782` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\01\01a8035aac1e6b6c8159fd74282f69b4180ca4c8f12a9f3200102687e3503959.meta.json` | 388 | `b19e2b33757c587e09ef9c7a7e808f65a4606b18c704485db09c4e1ca0d4f69f` | ledger |
| `R0783` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\01\01ae63daa03afc7b1defea3937411b9149e439ed396698e0554a98f452fb3709.meta.json` | 363 | `2de8be5931030bd721a4502e42c7e682630216e7acfad558001364f71418cb73` | ledger |
| `R0784` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\01\01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b.meta.json` | 357 | `268cbeb19cf18f7dcceb69f64975634af66fcb3fb66969bd3049d0eeb4faf308` | ledger |
| `R0785` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\01\01bbb6392676861e079b6d1ac4f203e0881e3be907baa6c17558dc8789fccc8c.meta.json` | 390 | `4280deae1f6f3d008832d37a0c59874c2f0b9689209d56fff190137e3b68dd41` | ledger |
| `R0786` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\01\01bf446493cd9715dc76536382970b66a769ef3f1a8d16d9679db3f12310e2fa.meta.json` | 380 | `6c94fefdb0f13dce1201d3f02427d4c4442c1f0eb5bf8644fd592c5d30ff5d1a` | ledger |
| `R0787` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\01\01c8f2e9dde9b37814c8117a8b9082661c13b614e4878e3f6460fae511e5ade4.meta.json` | 398 | `2beee4f96349425b673b89e8276e8985cd993477709fa49844000a9c0267e8b9` | ledger |
| `R0788` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\01\01da8bf59db49ddd1b84d19689e94b8401de8fa57cffc9b539652408ead2071f.meta.json` | 380 | `554838d9a865bc5689db7e643a5f3842fcc848384adea9df60004fcef8d36678` | ledger |
| `R0789` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\01\01e8a1e6fe4d8b0453abf3c2539fa3fe5cd879b8833c0a499e6b03ba71e6d972.meta.json` | 397 | `3af1fdaef5bdfe5c378ac24bfb07ea345c47c9790ac82d517eceede6efffac48` | ledger |
| `R0790` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\01\01f4fcf2fdb61ba3e064fcd528cdfdfd076e5279486def1d6f1bcf0a1fb97648.meta.json` | 399 | `cc1beb1ff52474bf380c1aa3995f1659270075f9e9cfaf578de4d0fa7bd7c2fb` | ledger |
| `R0791` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\01\01fd16553c691ff714747affb9aebd2438a34cb239686d519814c5ee8d8a4e09.meta.json` | 381 | `1647db504a13aefdab40e9d4bc2dde2aebdec05c1b29e4496b60fc538722e53f` | ledger |
| `R0792` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\02\021321c35ac1745a4d94a664afe81dd1d176e780214886ab390dbb29a1a924aa.meta.json` | 388 | `f03615fe739d0a393095499268b1489f82d933f3768b56ab5f36c1e2579076f0` | ledger |
| `R0793` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\02\021e70cbeb27e4b44d83b14209f07148530c530e70e3c2fede9e24f29f841752.meta.json` | 396 | `44520e10aba5f2e0ab0129aaa8b31ee65889aa6c6661c77fa867d7a8ed1ee0f2` | ledger |
| `R0794` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\02\023982101c57fcc1fd7ff8d58c818d08524a60261e4847b5f32caf371e2e44a4.meta.json` | 387 | `5b681e35ca49cf9c8e6f26fab3622c275494b2923ce7201c252d7e16043a0500` | ledger |
| `R0795` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\02\0247370919204e0f0ec289134e5dbc7b6479aa6b7be3d9470091346b93603fe0.meta.json` | 380 | `1d219e9309c99d6c9c06f7920a52f2504b0fec143fa2b7e3829ee5ea4e0ca57f` | ledger |
| `R0796` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\02\024a6ec5a6822d269f7f1ba0fca2b87f33fb784c2b8de216aea0251bd22d6f89.meta.json` | 378 | `3fc62bd7fd02b12ce48ae38fa419653069e5fba3899588affb7fe1fabd722978` | ledger |
| `R0797` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\02\026a5873097da6dfdddd4062d3718e29bccb7e245e57edacbc78fb578e6909f6.meta.json` | 429 | `6740bb433d91f5f58460068d2450e70e11c3e2d4cee889dd90f5cfcc1450a22e` | ledger |
| `R0798` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\02\028afe3fa9856761c477031f405ba378a8b82e8f455c457965390e42b51b641b.meta.json` | 389 | `aa5c30ebb461d8f94bf0caff3b8f0baaf5b48a6f41ff3e0c0b2080c5bd9b7b1f` | ledger |
| `R0799` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\02\028ea3e50641739e40749e33fcaeac1e24f2851a7c840cf4563728503468bf1a.meta.json` | 388 | `4b05b19e417de61f488a39ea518be143f12d0e3d4b9c49c36ce71d0f9c5fe38c` | ledger |
| `R0800` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\02\02a90fbeff7dd953079adb5442e93d53998f92e1116d9af4624919a077654e98.meta.json` | 388 | `c53194072e0a048c86b0f50255ecd73c4555a540aebd39d4a93cd1c8f5e6d083` | ledger |
| `R0801` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\02\02ad8c94dacbf7d8ab96ebd1ebbdc07dc55ba3aaa5a2097c7e247d20e0ccc710.meta.json` | 398 | `3d38182322cc2fbbc6da0b319dfcf0a6b9e54e45e8de799228d710f555d04b9e` | ledger |
| `R0802` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\02\02b3dcb0c8ae4b9ae4d40a6b467e650dfcc5d3ed576c6bb31e10357b03073a21.meta.json` | 378 | `219daa620bad74742c2c86e09077f10917fd24299076990f22f2ae538bd2f625` | ledger |
| `R0803` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\02\02b9fc008a77b0148bca7790944edb6499575f66eb0327385dbd9fca1f76072d.meta.json` | 386 | `9f053401b5c377a444dc2c54451d481bff3d28d27f82c2339f6c7bfc09cae39b` | ledger |
| `R0804` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\02\02be9952b607885b7af91af693e93d17c57b87180960735daa3936bd55ec2e07.meta.json` | 372 | `104bab53de793360ec24cfa0613d7b0af909d4f208dc53f27cc55afafb92836c` | ledger |
| `R0805` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\02\02c278b83e48362ed17ec3eceb7a2023565dc4905312b6886b02f408785ce018.meta.json` | 397 | `726fc4f3207087f2746abcc30ffad2dc9e4f3b1eb21b3a5ba53dbb1cb0da9270` | ledger |
| `R0806` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\02\02ca2dbe0345c7590a1a4a81cabe0bfc4fb4d9e697929c2806f3a3b2e21cfbfe.meta.json` | 399 | `ca4cc24e8a8febaaeeebc4db0bdd6298fbd4b9d839e30d9fb79542be44f433b5` | ledger |
| `R0807` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\02\02cecf564848a1981e350159f5c4f95e252395e58a80100bf418b194bd975949.meta.json` | 375 | `d857cd13be94bbddd3f674e73f0e20d1476ee9f61901fc3113f1d60bd527375d` | ledger |
| `R0808` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\02\02da22102b2b93ec59927937aee2e2f94c1e5ae5e16ca784183585c0c70afe4b.meta.json` | 405 | `d5c46d41cdd1defb09a3d75142178572738df7793c1ebbe94f9156d50094eb84` | ledger |
| `R0809` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\02\02fb352c76d275cc8ebc339da442d952850b7018987b063be9e341a7ab85061b.meta.json` | 381 | `d3d5de549e4b1d769bc4fac60babedad59806cdb1ee0054394d06b286a59fee4` | ledger |
| `R0810` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\03\031ded05534097116d1e157c7f388572c4e7a1af1825d6a979c32be908fb7cb9.meta.json` | 400 | `a5c179aa46d5c60e26c3c63fe68dd4406963501df75674a73127231ed8d4ace0` | ledger |
| `R0811` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\03\031ee205b333bd540d4e94f761d33008490bfa72179e9afad1a56b4782e96baa.meta.json` | 383 | `8dc6e881af3c69da0908446345dbef378c020d1d75e667a9d9e3bd1c86839c36` | ledger |
| `R0812` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\03\031f0f1f900d22122712de6a7d02427af7107cfcbf3b1fe2eb674d4c11f2ca08.meta.json` | 360 | `5ca6b742d82bdeb4acae4da63f0ed503d3c7c409caf9fdf61a7ca4c0b4d6a20e` | ledger |
| `R0813` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\03\0327162a36ff4df8320948febcaa447f15a4cc57e68de5c947061df0c46d5045.meta.json` | 348 | `d3a86f0b0e3cd5f28437693bbf0e8d16ce30499c360fcaee921eadae53de6707` | ledger |
| `R0814` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\03\0328fb827b1170c77df4c107d49be8df8d37262103490a61e8acad8a2f9cadff.meta.json` | 380 | `7190267831b79b1d194c6538e752ba341d0e4a56cf11f0f9ae97fce828e2b2d4` | ledger |
| `R0815` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\03\033175a3a78090c73abe7be6795a8d9d46545628f36cd6248f3ad476d0907b73.meta.json` | 395 | `322fabbfcede5452d5277dad5e1527cf87cf9e281316876f8a0b11f25b7e4bbe` | ledger |
| `R0816` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\03\033a867d540717ddbf65cb4372e7b40cce324e9d8fead7a49304483535ab2c8a.meta.json` | 375 | `bb368442b5481e5cf06144a5aa32b019bc14b81deac27bf743d6ab0b42c4e561` | ledger |
| `R0817` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\03\034149532959cb39a54f46b75033816caf84cd95c2018b90401bc6f5e002f61b.meta.json` | 370 | `b9165d22836ae849fcc0b95d863cbbe34c702f1b78a926e2f4abb0d181520b63` | ledger |
| `R0818` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\03\03494729321b2478a32a3f27b942be682178a0f8885d215cc729327d523384b4.meta.json` | 389 | `8f6fd8b173d1f20f184dfc0099057e8ee1c4240c9414357a1ac86675605ea75e` | ledger |
| `R0819` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\03\0374e2a71b861f48d8fdcb010e6d2d80f193d31b12e5fb37793c5d6d258b7314.meta.json` | 402 | `0cb7543e32ea9c5b808792417a0d6d35513243f28a81650edd8c9ef5c784b183` | ledger |
| `R0820` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\03\03813fcf91a36ad3ecbf39af7ceefa8c280b0912d992381ecc2958dbbf3a2048.meta.json` | 381 | `8b181a20a965d7b49ae17a78ddc23c326c39bda6a3d9cfc3690aea3d67a37247` | ledger |
| `R0821` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\03\03affbee5e6ec3e848c32a17ec33ce14be8efb2dea5e4f92d7a48c2efd4d722b.meta.json` | 400 | `d03ae8ca1b647673bc4e33221a0b9f404aed119b7a35182599c4f953e45c3087` | ledger |
| `R0822` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\03\03d2fcbbc8c5cee3856022afa42e12d42bad5296127276e96c6af03646a88f43.meta.json` | 386 | `373a7dcfbc4080aaecdda8a32786e9f0f955415707d09c0c0f334306baa721f1` | ledger |
| `R0823` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\03\03d557c2d465d36018fa31f40b4a2ecb954dc377e2e85fe9933b870e380000e3.meta.json` | 385 | `5deae8aa9460d7ef4f06a0e5ad1537297d9ed9f2153453d21f3b66277c92e2e1` | ledger |
| `R0824` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\03\03deb72682b5cd06fa5201543a9d6cb6baa3a09fe5650da9beb14b6b452320c0.meta.json` | 409 | `6cd5c830c193c20e11fd5b68a67355990b46bc140518e9e129902b078e456cc4` | ledger |
| `R0825` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\03\03e2c887bafde9d8d30cecfdde748cc216887f0fd8dfc63d16aa371871eea077.meta.json` | 362 | `58f05e11702e7d319b3e7c5d5ec1c1d69d088da77d7559bd3207a8019b38fcb1` | ledger |
| `R0826` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\03\03ea508ef9132025065c40ce89634ca9aeb3eafbf513ffc725f7f3bbbccb8bd7.meta.json` | 392 | `e3c1965df548da616abcc5d8b510a71c7d14c52cd668c8ca3ca8cb7d8e29b423` | ledger |
| `R0827` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\03\03f85a9de24054a4bc7ca837f454d47aa77a01b7381b799ff2cd476f0379a471.meta.json` | 352 | `94938cdc448b3fb9e109710e6c8e1f0a0407d1bd464ac9aa8df2983b49ea51aa` | ledger |
| `R0828` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\04\04025677360c0270f094bbb6716b83c8284902f6da9b496bedbbf590963835fb.meta.json` | 394 | `1f95ee0dd3d79889b874b28010a6fd3852beaab21160f6bee0a0c4be73165bc2` | ledger |
| `R0829` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\04\0410263d8c62cd06024f25f1eed8d56bdb675b2ac79db0e8c1cd5ef7acbe1cd3.meta.json` | 401 | `213b52931bd850b8f8d29ce7c035c2fda16e31b99d7127b4a5f02e464282e1aa` | ledger |
| `R0830` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\04\04261f5b3ddce0c36584f2be42e2938d5a0dbe914414502533a93e8c142dacf9.meta.json` | 376 | `3d446f80d3f943e9994dc2eb8b17da631ae6a059f650a842bf5005350488bcfe` | ledger |
| `R0831` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\04\04480cd0cbbedd1e4ed0d61f0266a737f48b8ed4bb4edd74e313d682bb152097.meta.json` | 401 | `1484c7e2e1e4bafd8d91663ada079074301015ad7cdb7f0f3e882c8118621736` | ledger |
| `R0832` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\04\0448ae501fdafd48edec9de32e8d71195af726295813e73bb063d50127b97de4.meta.json` | 388 | `75497b8462839f9652fd5e0b935b4ebc90275c52a5953b50a6f4377ae9252c7b` | ledger |
| `R0833` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\04\045b8f5185ad57a6ecd9e016ec0ef8085ad6d3010cef392c5e56ee7d7bf8f34c.meta.json` | 387 | `1d208d7f5d73ee775b653682d177d2e9612f304c4923525fba5b4055530b8d43` | ledger |
| `R0834` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\04\045f872eace39c15bae27930dc4e4ea659179c891ff8e4b7497dc799624acf25.meta.json` | 379 | `de46fba66e9bcfa95df0af2e199b1c801560d3724537aea08b6375a9f104d48c` | ledger |
| `R0835` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\04\046b8c7a795c413f22ee3f62725adf742def4b082f86bf208e7f79e5c0b2d7ab.meta.json` | 388 | `88e1945651bddf5fe32fa8be5ff5a00fac30d3c8db28fdcbafcb33d7aa77586f` | ledger |
| `R0836` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\04\048111a5485bb740f67c03ec6de138e312e3a00344fa92ee356d7e3c971b9bd1.meta.json` | 422 | `3a0f34deebd5b5da10f90eeb6378f07d01d88fc6c575ad8d9e05ab9abdd1ccc6` | ledger |
| `R0837` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\04\0486114a785d3c74a9940bd828bf4d04bb90599eba7be427269895580fc00f7f.meta.json` | 393 | `db70d11af41c25acd3b50d2411e2d695b70b0194fbcdea75f1d73a618b1c6fce` | ledger |
| `R0838` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\04\048fdd28b48cc25925e7bbe5c599d3f285633e2502d96fec771ffcfe1f7d1de4.meta.json` | 391 | `99f024438b67378ea2e00515d4788359c4876beda61c2bf637ffabf7f1304672` | ledger |
| `R0839` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\04\049b5daa2651b5abfd55114298ec6863e2889909a33f2f80fcda288e21546716.meta.json` | 377 | `d1276550eff2effe672cb5b8d29a2ee302ad65be553b61836065e2d2d78cc4d4` | ledger |
| `R0840` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\04\049fc12cf436b101a5622456a1b83ba8b28b54cf8106d3953aed751bb0c08f3f.meta.json` | 380 | `1fdbd0ee2a77e7563c260d13b0d719ddfee1363c0b8e6e49af5dc05c685074df` | ledger |
| `R0841` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\04\04a6e8c286100032a300999359d43c49240b6c106c874f9d663dd31a3b67eb23.meta.json` | 381 | `55292545cedbe9e3f40afb884dc72c9832bc1e791daf6cecee3e8f794cb116bf` | ledger |
| `R0842` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\04\04b758e45ef7b9e8c040801e3015bb3e68b9b04ee7d466edb79f4fdb6185d239.meta.json` | 413 | `287479a5d8c908a1842b0b3186b2dffe847f11532a76ea86b36da63557326f39` | ledger |
| `R0843` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\04\04c7b29beec61ce4a71a9662b1af4191d424566097c0a00d0393699ca46768b2.meta.json` | 400 | `cbf4da366c64e3a6b98e585c750a8bce6dc5c0e73f121a66bef6cfc0d24e0086` | ledger |
| `R0844` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\04\04e4673a3d27d262f5396514b353cb4eed520129af4fc90410303a71bba1b8fa.meta.json` | 389 | `1009447039ddd415e6b9774fabcc3bf3147cd9851dbafc88e9a18b786c019e9e` | ledger |
| `R0845` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\04\04e8f8a22df4a8849a6f45f6b1efea14f986524bbfee3fccd69c3744d237432d.meta.json` | 376 | `fe1db817f6ac85ac8afd8aed330d325e79c499a19d910c667c368776bea27b01` | ledger |
| `R0846` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\04\04f593f9389035196ecd94d9b400530b7845000e2cd483c446da2385041a03a3.meta.json` | 360 | `f224e9557032f42692e23ca1f9f1c742dcb3bf28d45dd90b359319a8fd6a632d` | ledger |
| `R0847` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\05\0505ea2b3c2f0130eaa29f476c213551b583c0964969578f180d425335857aa0.meta.json` | 376 | `46d2f8fd3bf2b52d6d1a9c4c4b526b55ae77c8432f1facd4dcd9d06f7da6703c` | ledger |
| `R0848` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\05\050c3501be0e6ed2a6bfeeb67fa2ae1aec96d5a1d3bbe7506816ae5b80c9607a.meta.json` | 379 | `0b55fc5e76261d24dce76748f0c49ec8ffa21f216bb1ffb6369bb443ba36b72f` | ledger |
| `R0849` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\05\05268344833004b2139ff9b499344b3ea304e6afaab8675232e60ca587982707.meta.json` | 392 | `79190c13f9c6cc5854c040b7f4646e19bceb9107f798ea8df9f5c696260a8c09` | ledger |
| `R0850` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\05\052a67a92011d49c1e839ce3707d090ebc40952ca71b1f45f2edc052c82b872a.meta.json` | 360 | `f9f9a3485db8f413ac17c104b6f2e270a43d0897e1272e80be4e3362761d6a89` | ledger |
| `R0851` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\05\05414212a30b303be5715b5b5167bd7cef1934cac20cd1bc4de8d9e363890bbd.meta.json` | 391 | `bd24b6258978f7f0dfd0f748a94233e26030c130221df1f27dc1a7c3c0f811da` | ledger |
| `R0852` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\05\0548ef5e29548ae305f9eb971100f3419b38e639ff68bb35ede4ca71f129b6b2.meta.json` | 388 | `5e79588bf9cc3192ed89fae3db22a07b34e177f512214330b4230668e6ef1951` | ledger |
| `R0853` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\05\05697e39fd4697c9ebd1e060b8321d29b4b987d39d98ef9564f51039ed9eeb66.meta.json` | 380 | `587c448a34f0c52c6036fcfb57e7d0d08a20a7af87824f3cf544ef646f488f43` | ledger |
| `R0854` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\05\056a10d82a56048e536f037e54609dd253ec2ee226617295b42535b4366b0336.meta.json` | 379 | `6d5f2776d7dd95e15013f3f0ca4e982804a9a4b6491477124a7020a23a1dbac0` | ledger |
| `R0855` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\05\056f8616fbbc05088dfa3ebede6112496377210bfdc3cc0d6b7379de58acaf22.meta.json` | 376 | `2ddc40737c893a0c3d08ac5c3d30614a061b2d827611757925f4dd07da1874c2` | ledger |
| `R0856` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\05\057ff554f5198be724282625176b2db50a6b1766cb5073a2f1b961227147bfdb.meta.json` | 382 | `f70166f8e1bc3ccb9d8268acb344d98b2a12fa444531125d128ce781a7d753e5` | ledger |
| `R0857` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\05\05caa7afa27fcab6c226ee89f45251813209f35887b68fe1347c552988a481ea.meta.json` | 396 | `87521cd943bd182320f7ebc766ab8f2c420092e775cb8bc6c94348b9fad2d497` | ledger |
| `R0858` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\06\061843d7be8bbff3662d9de72ba9f7cd5c826c2c448f954cc0fbaa8e6ddfa9cb.meta.json` | 391 | `6625798503296c0a27930d3f44ebc0b05815439b24dace6c4f4a5cb4966c13e1` | ledger |
| `R0859` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\06\06229f67eec88c2ef460de6703e1889a91a5be05a7645c6f076432e80a12f89b.meta.json` | 384 | `17894250353549fc4d0675fb9a2c513582922bfa8ded7d34b8a5d7cb26458167` | ledger |
| `R0860` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\06\06258dae680cde2122a4939dbd4f23ed4ea145b7475068bf7dd4d466090afd2a.meta.json` | 392 | `cb2db55e6a10ffb7f28d7507ae6cb2d534ae8461845ec6adff31481ad41723a5` | ledger |
| `R0861` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\06\062b671514f6c565d0ab53184707d69c3eb24d0a9f8c23e9fd9fe597024fd2cc.meta.json` | 376 | `6e9a5a732b32312db9a33df4e638a81f4a71111fcf5e2a8f2079ab936a3fe33b` | ledger |
| `R0862` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\06\06354a7a6470467bd4b316efbe1d8f6eaa835223a32e2853055da0caea2bcf5a.meta.json` | 374 | `daa9895577475951aac9c8ddf694d04923f9c9e7d36a0ea8dd26ff402d17a1f6` | ledger |
| `R0863` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\06\0639746cd8ec347fc069319ccded24d7e6ccd39988d298c2a08edab38c94079f.meta.json` | 377 | `9b6cd633f883de4ef8349de828406e86d54617bda136cf09748491941618bd15` | ledger |
| `R0864` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\06\06676d8027e324ddd6ef2b92d9614fc3a2c14766d4913e01869c912127ef96ef.meta.json` | 348 | `fc31ab72f7c3a74a383720be7777984ae0a90b2d7e2c8397dd28ef5145a8096e` | ledger |
| `R0865` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\06\067eb498f33bb4ee14bf576049163c3a04ff36f996ef90619ca4d07ef66c7b2e.meta.json` | 398 | `50fef6536997fc01a5330354a7ba904e9a196111d2951169b3b410ba0cc2ef5b` | ledger |
| `R0866` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\06\067eb7e7271c0204adb7e6ae5ead923c773979ed8f8fb3a63c8b9466f9cb5bf0.meta.json` | 397 | `a76c449ca080fb055e9377a1526b11f80dba3f77e22433fe99aed06850c72a79` | ledger |
| `R0867` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\06\0685830d13647bd6f3f05526043d32a8b2a221d86b53773053d6c52bb17a9c07.meta.json` | 398 | `ca55b10e3412e408e130fecdc4c7fc1384cf7b7a65cbea324b53a0ceebfb7641` | ledger |
| `R0868` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\06\06a5c9a458f2de16ccb8c6b4fe48cb00ab2434f3b4b3b93e4cf4913fecdc80b5.meta.json` | 385 | `abbece7af749f5a603a37e0bb570889b2c609ce49fce6b5641b4a69366e9de0f` | ledger |
| `R0869` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\06\06c07e1f6455e618acceea0f50482231d7696942a17a854f13ac296c9a05c6db.meta.json` | 396 | `b83d6c26cc30a7c0765702c3448faa0dfe19c1b1a7e499af5747a385351f233f` | ledger |
| `R0870` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\06\06c46b0b81110d5af8dbed86fcbd00c61354e175706ccb32e52d253af2abf300.meta.json` | 377 | `a5142b8ed8a732d4f41d3244422d2b24834bc3aee7c92a06d13a8d0861e416bc` | ledger |
| `R0871` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\06\06e54139e20b7c10512cb5629d203f98256a62d82868ce2e9172b630eaf8c554.meta.json` | 385 | `7084af09f9cc064bfe77d498b75972414091f4a1f6640309ec997a505ee59bee` | ledger |
| `R0872` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\06\06e56daf26a111313a95d57b4ef5b45446bb8d1718505e4230fc618ac7d08e7d.meta.json` | 393 | `1ff6117efdc410916bbdfbfdcef4af12b817f7aa2b9a72c743eef48a3028ccac` | ledger |
| `R0873` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\06\06eee4aa49a9ba784bb23e710aef204ffdb992da0f5dc4a7c1ef151e4d46989a.meta.json` | 391 | `43d4e1250db7dce3282f66a5a021477764a76a77a4955c19cf490924d6ce538d` | ledger |
| `R0874` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\06\06f6396340cb25f153b04a225bf3c4f82dc19f2e16ce8f4b8053a5db75c730aa.meta.json` | 362 | `224a66554fe4bb2259c8857aa90c6bbe0c7acf39447323bdf62839725d680fda` | ledger |
| `R0875` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\06\06fd184b3e02f14fcd9f9acf47a81a3fa053bea2215c8b207828fb6cf667415b.meta.json` | 377 | `b5f6c35e7cf860568b150147eff6c1671dc544564a8227a87f6969d1b9ea9880` | ledger |
| `R0876` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\07\0701e4e2285a0337380d6d73d176e1addac85aa574ba48785f1ea85803590404.meta.json` | 354 | `9a2a8a7f7365347c72ff525ce29540c210d3b298ae5835d81b3967efc159f9c0` | ledger |
| `R0877` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\07\0710508172cda8996c4a2c89a03389caa01097cb51438b479bc294158524e2d0.meta.json` | 362 | `c1f42057cf3b052896cf0d4487f03a3f839caad80651241bf75c666a66d3600b` | ledger |
| `R0878` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\07\072546a651271bf09a12bc22458e64844a082027b89051a6e35eac267221ebcb.meta.json` | 380 | `3ec3925beabded8907f24fdb97ae4f046790f5294e7fe18e475efc7db8dc4acc` | ledger |
| `R0879` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\07\072faf431b47fc4ce64d6db4930324c1d1aaf84dac43b083e3db4ff4f4625527.meta.json` | 389 | `9198b0144a7bdb987ead36fe1e23b122ef9f39fc8c6611ea3da8c7d9848d3162` | ledger |
| `R0880` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\07\07397e45c9e2b4f0479eac308fd8afec98c7b8dd46a67587db874a905de5f5ef.meta.json` | 378 | `beb0857ec36b80dc7f41935eab85e0053a071f79d949a880db7f4cd981f33623` | ledger |
| `R0881` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\07\073dcb7233505e4cf80aefffa4be0267cea8e3e1cd2d98f535959d949863baed.meta.json` | 387 | `7f5734daf7f25746dd8d14f802a3ab71cef60631ef8fdc365f9d79fd8b17a172` | ledger |
| `R0882` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\07\075568a9b6213d690e2495827a6e0e638ce3d08c6b3e4b4165915ed98f3b9148.meta.json` | 378 | `bdec67ec7f10618374e4aa1bab6426bc4f4c51874cf652fdfe9bb7d12e326497` | ledger |
| `R0883` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\07\075c6168f09a34a9b2de367ee4b32e29e1efe9e1862a4f61b3dc68425bdccd8f.meta.json` | 361 | `25cffdb153d4055102befd711b497a67f4e69c76ef382f2e0545d5aa56878a46` | ledger |
| `R0884` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\07\076f4e4b8cc6336b479b97fdb5c92184185172eede17d3dd4eeb0c47ae7bb06a.meta.json` | 389 | `ef4785afea937fad9a16fdaaea4543a14bf2cd67a1dcb2aff8997e4765b3387f` | ledger |
| `R0885` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\07\077aa834f2226a6b350d4131855fdad81110c51b8b2a7d334c4cdd99d3b503d7.meta.json` | 386 | `d349dd962469043d628d8501fd1f851edcca26172b9cc8742c72391fd0f6a614` | ledger |
| `R0886` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\07\0786cf82d9c229ace18f240956a270abc1475e388bb16d8e3b01961218613feb.meta.json` | 383 | `708669d9779a78b5dfb8341166c8dfd29c912fafac0cc40ee3b8dc998431c4e9` | ledger |
| `R0887` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\07\07e3d5e42bbcbb84117243c82355ef70246f3dd1923849c5dbd0277965b21e22.meta.json` | 379 | `329a77785ee29f686c97adf18df193473150e612ac2fa1e481ae7a731f483dc3` | ledger |
| `R0888` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\07\07ee5b8d0f87e15a95ce35b69a89d30c1441482ce21bec15eeb853955d1e1045.meta.json` | 387 | `0ff7a8828c8ed5ef6b5acb204847517cf8798b203d3ff17fca4979ff2f966da4` | ledger |
| `R0889` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\07\07fee2cd99574c7de4b0f960127c3d53b874a53d9a6f830450336f3913396938.meta.json` | 390 | `c567f8ed8a2bf8d096c167bbe6f5fa149c054c7126867658fb3567137416f2a9` | ledger |
| `R0890` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\08\0800965a1d3c37f3833dc369cb212c948b1ac13b5d5e49b27eb995dde3ffa9d8.meta.json` | 378 | `1133c815072c71b95392a862ab4dd9f19399aceabf076748a0f48b5a66d761dd` | ledger |
| `R0891` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\08\080422913a6fcf829b089531f63a27673832df497fc3dba5ea15b544d9d752dc.meta.json` | 407 | `a227a8d70ebcb47195140c6366c8d02cc0753ee50231c34beb9e7485b19b7fd6` | ledger |
| `R0892` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\08\081cd291a71b920628003fc0de138c3070ef99377277868387cc7f21739af1bf.meta.json` | 381 | `944c564b381f5887e453416358027f269f0de157ed089837cf8982ab0a9e5923` | ledger |
| `R0893` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\08\082c1145853cadd845f42775d7ac896b6cc63d9b2e80572cf579acb6fcc01d54.meta.json` | 374 | `a682b96ca1d791f2d1e4936d92cfb0c67a690f3a9de1a2e7333a521140f4bb8e` | ledger |
| `R0894` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\08\082c9687fee7aacd9575bb34ed001995deca49f3a1d9995d25cf4d1a0badf62b.meta.json` | 385 | `e8b7084fda8cdde5f9a77accdbc67db335ab1b79ab44d560e8270f22d4b16567` | ledger |
| `R0895` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\08\082f9565a184b962d6b6e4baeaafb5c53fa420f553b8bf32a99e58c51dc75603.meta.json` | 382 | `14d6feb67c552797d984d9a9c9fad6a192f22cda87256b8c98dd252cc37e1411` | ledger |
| `R0896` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\08\0833e4cbae0f8da5115a1aa41f190b12598c888db5bf9ba0186cb385d7d46e72.meta.json` | 415 | `1f1590851311276a2d28383110136c22ee0ff8051a48e8f593d7c62e3af204ac` | ledger |
| `R0897` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\08\083a58d0616896e47723110290cda01f9b837d80ccd042f5156afb07beb0b603.meta.json` | 395 | `8619b3c14f8e54e75e41c0982fb15d4014ed43150fd577cb1100a18a1ca01d1a` | ledger |
| `R0898` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\08\0850941fbdaa3e84fad13b26ac4910a822aa59b9e2ca685cf499380f8c5b1a3e.meta.json` | 381 | `885644102eb9cbc92e0eb066c44b84b12351831e55bea40599893a61e4f57dc0` | ledger |
| `R0899` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\08\085f54a06596987c258df68b923f33cabc6b8d5ca660cbc6603349edd14b21b2.meta.json` | 414 | `51ed9385a13e0a8bfec175957346155d35e4921da0430df2d9ffceae138e0aa9` | ledger |
| `R0900` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\08\085f55335d4d6e1d153124db2a339fc43ad35986790de4ee28b6ecf242bbd5c5.meta.json` | 382 | `203bd6ec2d4a530bf6410ad72c8d38fff5b9cb93f9ee14d4e1b001c2c4d58bb2` | ledger |
| `R0901` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\08\08734e0a2982dc26ab91e8c73a6fab57b6fb6e6ca42252400215e3f76de92aad.meta.json` | 382 | `f7716a616d947893d58ede9efa01c7966c2602a14d4fa4c383f8cf2e8fe4cfae` | ledger |
| `R0902` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\08\0886269bf0be4ce84782f79a3fac58fe147c704ec34ad8dde1f3d245a5a26afe.meta.json` | 398 | `52af84dfac2052f43f9eae0011c3579cf58893f25e96e1b59f419762b2706195` | ledger |
| `R0903` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\08\088b992f351b85902fbc405815b31284661c37d1e3b433c21c814db63f62023f.meta.json` | 384 | `not computed` | ledger |
| `R0904` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\08\08aed5c429482a7944701c6d74c953f312b12b36ff79bf613622b193a0e09333.meta.json` | 409 | `not computed` | ledger |
| `R0905` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\08\08bd915c54f1d846d654f2362d8692954887265840557f8b110573627d4224dd.meta.json` | 390 | `not computed` | ledger |
| `R0906` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\08\08be4cd2df791bc62fe2d35350ebfd3902d7d668d96c848ea6f1d9b03dad8dbf.meta.json` | 376 | `not computed` | ledger |
| `R0907` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\08\08d7903e7a40b9d63bee79b33a438d4a6020465cc87f4e97f97f66bd160e0e6b.meta.json` | 401 | `not computed` | ledger |
| `R0908` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\08\08f6dedaad8e70a53c2db4a11c6b67206fe3ad6f377f79ef311e53ae0d4dc7dd.meta.json` | 423 | `not computed` | ledger |
| `R0909` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\09\090de931a033eb850caa2415ad8a111273a08d4e503de17f1f769a1cd755442f.meta.json` | 382 | `not computed` | ledger |
| `R0910` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\09\091a3ec51c230bbf9cce0d5c6bea5e426810190c1fb6623b69c87aada24f7445.meta.json` | 392 | `not computed` | ledger |
| `R0911` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\09\092adb4a9d986311d3c655fb4749d3dd1a47ec4968075c08be8ed8380ed05b2f.meta.json` | 382 | `not computed` | ledger |
| `R0912` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\09\093104ededac06529465db6c51769d0bf8311f9eaec7a0b881599734e40a230e.meta.json` | 388 | `not computed` | ledger |
| `R0913` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\09\09473696453e5f9f6655d19f8cc0819197a218f2f7bb174e36384d245d93ef06.meta.json` | 386 | `not computed` | ledger |
| `R0914` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\09\094e205567b47d328bb40045c227bf8e61de3ade8d6b869c8e39a784bc549dd1.meta.json` | 396 | `not computed` | ledger |
| `R0915` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\09\0965aee362caa33714e4447cf308a53ca066e0297e4e342d1c0c31ef9fbc0588.meta.json` | 373 | `not computed` | ledger |
| `R0916` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\09\096f86c3cbc02ce24232ac08a169cfabdb97fbb32a4eac7b9834c4a963556955.meta.json` | 384 | `not computed` | ledger |
| `R0917` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\09\09747d4b59c67954e59f6bb947ad348718240262455554d34c187f9376b0fa99.meta.json` | 381 | `not computed` | ledger |
| `R0918` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\09\09774bbd0b14da20ea41ceddd93451092c20b90cc9d12243167db748378e3ae6.meta.json` | 399 | `not computed` | ledger |
| `R0919` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\09\0978dc22796f722f157a36969f57f7f64bf401c7c92f4479db7a912c56550feb.meta.json` | 389 | `not computed` | ledger |
| `R0920` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\09\0982425790537edb5961fa98de6a2f74c044fbc6b3eee8444ff2d86ca4f6367e.meta.json` | 388 | `not computed` | ledger |
| `R0921` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\09\0985434a2e7cd881c90dfbf9ddffa4c2c43d07dbfe9b89d598e5f7d39b91021c.meta.json` | 383 | `not computed` | ledger |
| `R0922` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\09\09922dc5b43e07d7099da4b91f004d593d5bb9ab7f2605fe5becce9fd9b5d5ae.meta.json` | 424 | `not computed` | ledger |
| `R0923` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\09\099458de8abfb443544d56e7adc21dfa212bd65c26f3a8b6e9a472a0b6e7f943.meta.json` | 393 | `not computed` | ledger |
| `R0924` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\09\0999614972845fcdb2dfe8a7521db3551b8fd7a017fc431f9ac4d52344fa4583.meta.json` | 425 | `not computed` | ledger |
| `R0925` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\09\09a04b25757038e704734fa3f97b15e7105dfd71d8d23dbf63fa208a8dd94896.meta.json` | 390 | `not computed` | ledger |
| `R0926` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\09\09af932fe5bcb5b7445b9baf2ff1ab32287b1bc7bfb7fbe135ebe2d8d2988c45.meta.json` | 379 | `not computed` | ledger |
| `R0927` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\09\09bf56575b31a0ab76c090a5d59f50478da22d85f6dba7ff6e85fefde8432c04.meta.json` | 409 | `not computed` | ledger |
| `R0928` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\09\09cd2238812c44cf22c3e86bc57ab3271ada9b7873646b52b48252101ff47c5a.meta.json` | 394 | `not computed` | ledger |
| `R0929` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\09\09dbc242b0a53c0500cd31752b0848c834ce9229821cfb0e18c472548a7d4b1b.meta.json` | 388 | `not computed` | ledger |
| `R0930` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\09\09dd1f00836c2c4b3d4971d3337f3282ab075c8364abc424b30198b2d07d8c8b.meta.json` | 384 | `not computed` | ledger |
| `R0931` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\09\09e8a9bcec8067104652c168685ab0931e7868f9c8284b66f5ae6edae5f1130b.meta.json` | 404 | `not computed` | ledger |
| `R0932` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\09\09fdbc70fd28accf3dc5cdd0a4955c84842fd36a6bd23b2724b473aa2bd200bd.meta.json` | 379 | `not computed` | ledger |
| `R0933` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\0a\0a0fe2611eb3cff84f0b2005336db898d9af465c17967802f28f9b85e805a8d0.meta.json` | 398 | `not computed` | ledger |
| `R0934` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\0a\0a1ce6140f2b9420522c5080e356e689fa796c2522f55ca10826f5ed8e0a723c.meta.json` | 377 | `not computed` | ledger |
| `R0935` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\0a\0a21a8cfb4e3602efae2f2af496641ba70a44f20a9ec6bb309d446fb76a9e2c6.meta.json` | 392 | `not computed` | ledger |
| `R0936` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\0a\0a472f3321d8878539ac6815e808128714674cebf4b66a846ce8957696852eab.meta.json` | 390 | `not computed` | ledger |
| `R0937` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\0a\0a513aff3493d714fb1f0caa58448b8aed418f9d160a7b0c07dcbb3785dc8b9d.meta.json` | 372 | `not computed` | ledger |
| `R0938` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\0a\0a5f1745f0a621c544de3e40114e760bc88387c95c5fffc3de1cf68c85b1300b.meta.json` | 377 | `not computed` | ledger |
| `R0939` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\0a\0a63a9dcb145a8853105ffa2652e264bb09e3fe073b9c40f71864d8146d50927.meta.json` | 388 | `not computed` | ledger |
| `R0940` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\0a\0a70efd661755f99359ac56f452fdd891e2d929d3a13f8e0d2d2bd71d1c41424.meta.json` | 385 | `not computed` | ledger |
| `R0941` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\0a\0a816cf8be5b5e4b37b7ebd945ae34f268a32f5add29f8eec840c80abe8b2ded.meta.json` | 387 | `not computed` | ledger |
| `R0942` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\0a\0a8cd483a03075ef4478918970e7a63a94a4808a4f852394a35ccee30e687dff.meta.json` | 398 | `not computed` | ledger |
| `R0943` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\0a\0a9fdc217662963cc48cc01942ea484a4b9c8902f114b3e0d913412042588b86.meta.json` | 402 | `not computed` | ledger |
| `R0944` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\0a\0ac3a286abdbe9903a3baecbef4a177a82c778e7cdccc33cf07f60fbd6a8720c.meta.json` | 392 | `not computed` | ledger |
| `R0945` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\0a\0ae1bf1ba5ee80ce9936abe15eac3a2543c8a1e192a50cae08c4c4b9d608ab35.meta.json` | 385 | `not computed` | ledger |
| `R0946` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\0a\0aede4d1ca614f32c348f3d728eab58322ccd016e8531234fdc3dfcf00e32bf1.meta.json` | 394 | `not computed` | ledger |
| `R0947` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\0a\0af1528bb1580d6e9ebbee6888a19cd0c377685d575590e8148e7ede61e90439.meta.json` | 379 | `not computed` | ledger |
| `R0948` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\0b\0b064e96e27601945db248b4534e402920d37de428e2dba965f5f1297e09b5d0.meta.json` | 354 | `not computed` | ledger |
| `R0949` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\0b\0b0a607f2df90c4f52dba8840c28e3bb8430220627071853f66b9ee1a81508d2.meta.json` | 399 | `not computed` | ledger |
| `R0950` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\0b\0b4f8f5b38aaa645647f73e43f3d8658dc22742ae379fe401d0181a6a4cf92e6.meta.json` | 391 | `not computed` | ledger |
| `R0951` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\0b\0b5bc365905e93e4cae92575aba7bfee4aa4c90cd2f22a8713c1b36607a18621.meta.json` | 407 | `not computed` | ledger |
| `R0952` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\0b\0b5e07bc5d6f5dc2873d894e235646866bc4440c8ed621b61139c674a5344dc0.meta.json` | 419 | `not computed` | ledger |
| `R0953` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\0b\0b5f3d240c210b5421d002a0b21cdbd70543cc5a819efd55678e644c40c83b7d.meta.json` | 376 | `not computed` | ledger |
| `R0954` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\0b\0b9a4c6a9525ceb57a29a3c47720fc6917408a02259d4ce31559c5bb44ef1d60.meta.json` | 383 | `not computed` | ledger |
| `R0955` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\0b\0ba6377b02ea76236457d9aa138fa7670116fc2117c0f31fcdfbe296eb8b7e4a.meta.json` | 375 | `not computed` | ledger |
| `R0956` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\0b\0bcb0e62eba78b72affe5d3b73e742d57b5c32ab016a9bd569cc65bdcea1a55c.meta.json` | 399 | `not computed` | ledger |
| `R0957` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\0b\0bd2c75c900a930007f079f79cf933f4460adeba8f05e3bf21790e1b6cf3b1d4.meta.json` | 386 | `not computed` | ledger |
| `R0958` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\0b\0be603d7c7e538a29544d4d1b1208e12fcaa19fdd9c69bee52f474cf46355a98.meta.json` | 390 | `not computed` | ledger |
| `R0959` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\0c\0c10c4fc79e742da96e746c06f8396ddd28a0e01004d448ebcda9f0c20c11764.meta.json` | 392 | `not computed` | ledger |
| `R0960` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\0c\0c11e45794a2f6f9adbff3225ba3663d06fcc9478fe0dfbd84db768ee66be191.meta.json` | 393 | `not computed` | ledger |
| `R0961` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\0c\0c28552e00fba933a96d83667c68cf8df3b1e58b2984c218c1dc27175d97e313.meta.json` | 405 | `not computed` | ledger |
| `R0962` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\0c\0c40cce4dcc4c311b2b5d6ea72f9e4d1a488d87f3dfbf5b4a02086ae8e0840b0.meta.json` | 350 | `not computed` | ledger |
| `R0963` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\0c\0c40f72e0eb7ea1077d49b54fafd4a4361e90b9d107f05dd8f29548009ed6a68.meta.json` | 372 | `not computed` | ledger |
| `R0964` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\0c\0c4128fe70844a0a2065e1bf10d45d6a2e67c3d609a2eeddd2997352bc14857c.meta.json` | 387 | `not computed` | ledger |
| `R0965` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\0c\0c48e80d01807f662afc1033ebac77c342999b5421bc6e1910d93cac8202d944.meta.json` | 392 | `not computed` | ledger |
| `R0966` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\0c\0c65f107780cca6d624ec8048de738da08243a6e3aa57fadd9b1a36590bd59be.meta.json` | 420 | `not computed` | ledger |
| `R0967` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\0c\0c7810815abb26263b5d34a67f3c4efdf58915251718a35fca96a3987e3b0734.meta.json` | 388 | `not computed` | ledger |
| `R0968` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\0c\0c7c9c090a4db2ee7626b859fd076cedfd05e14d2b0f8cd669530e2f0591d3ca.meta.json` | 400 | `not computed` | ledger |
| `R0969` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\0c\0c846399369ea76ddd7b5c44fe6d16497415fcf015f5cbb508c24bf98b81c5b1.meta.json` | 401 | `not computed` | ledger |
| `R0970` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\0c\0c89d0d625c0a5ec90839bc44893c2bca1a05224a9522e6934941df1faab4460.meta.json` | 374 | `not computed` | ledger |
| `R0971` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\0c\0c948b9e24cbabd6fdc42cec9aa6f9755bd37d82f947f4f8c5d1f42211597737.meta.json` | 387 | `not computed` | ledger |
| `R0972` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\0c\0c9e5d57104c5b959e0f3f1d8d8667f11e505e71737ffbb059c2a02b17a1807a.meta.json` | 400 | `not computed` | ledger |
| `R0973` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\0c\0cc5f6568966fea1d04bd45a453ae0a1adb6bf76459f3b325cfe17488018b055.meta.json` | 389 | `not computed` | ledger |
| `R0974` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\0c\0cd2272e9ab075b61bbfca4931b69471376346d83ccf7218057f94409e92c58e.meta.json` | 393 | `not computed` | ledger |
| `R0975` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\0c\0ce3331e49ee0df28b302688cd034fb3fd090113a48f3a8e59ef3c7844dce2f5.meta.json` | 378 | `not computed` | ledger |
| `R0976` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\0c\0cf9dd837ba23b412c95765aea4422bbf6e7c2210c6eefde91eab43d4308b0d5.meta.json` | 379 | `not computed` | ledger |
| `R0977` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\0d\0d08b3cba9ca3f4cb084fa6708782644360831f72a64a544ccd2164198eab554.meta.json` | 374 | `not computed` | ledger |
| `R0978` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\0d\0d0ca6351e932abc9a9f18aed396c340da11cca66e54e6f3f87be3cb1d873417.meta.json` | 384 | `not computed` | ledger |
| `R0979` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\0d\0d1b1321a5a688caacd763e006fbbe11f60110e9fe27ff8d23a679863d01a63c.meta.json` | 393 | `not computed` | ledger |
| `R0980` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\0d\0d25be36e09cf1522b0d6319f5d295aca3ae8f4e451e531b25992ca7787c868e.meta.json` | 394 | `not computed` | ledger |
| `R0981` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\0d\0d2b7e974db957ca4aa20053918516a6f28a8433eff401728483cbb235e483a4.meta.json` | 402 | `not computed` | ledger |
| `R0982` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\0d\0d49bd477a82ea0d599d745d73b32eed4d3702b245e63e6820224b87f6a68572.meta.json` | 397 | `not computed` | ledger |
| `R0983` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\0d\0d542e0c8804e39aa7f37eb00da5a762149dc682d7829451287e11b938e94594.meta.json` | 428 | `not computed` | ledger |
| `R0984` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\0d\0d9a018f6ccabfbe9293de8f2aaf1e97d69900cd89df050b56a3dea27a3fd33d.meta.json` | 379 | `not computed` | ledger |
| `R0985` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\0d\0d9d6995fead1ccdd5512f7909ec8f9efc8ccc97f5c9d23ecae6b3ba77ffadbf.meta.json` | 385 | `not computed` | ledger |
| `R0986` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\0d\0db6d6742e8abd2df3eb37a47b172ce28ebf76b4f0b461aadd02db6bf8583ebc.meta.json` | 394 | `not computed` | ledger |
| `R0987` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\0d\0de2ccda32fb6418ab8f0f47d9d7e35f16c7c31d98f60bb7c29d8dc032d8b884.meta.json` | 399 | `not computed` | ledger |
| `R0988` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\0d\0dea37ba8f7c694c887dd28936aa1f7921055b00f3ad5d907862d72ec82ad008.meta.json` | 387 | `not computed` | ledger |
| `R0989` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\0d\0df61aa361d07967446e5a7b5d905e2c1666d486d4751453963f0415fc53a666.meta.json` | 390 | `not computed` | ledger |
| `R0990` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\0e\0e13ba1a940cd9df7e65358c36445c9740f3d75f1360c7f7c71ab9f74b45edca.meta.json` | 392 | `not computed` | ledger |
| `R0991` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\0e\0e1c42feb4a4f9b78a75bb1885fbc1503a2f4075fdaf78071ff8cff7eabf98a9.meta.json` | 396 | `not computed` | ledger |
| `R0992` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\0e\0e23522eaa6eaee5d46a6190c0e2765990720c62d319a5e2f4ef977fc7ce8b7e.meta.json` | 398 | `not computed` | ledger |
| `R0993` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\0e\0e2ec353bce892896d6a94ff1744a3db57df631c1a4bf704e5aa4eb70b9e7b20.meta.json` | 403 | `not computed` | ledger |
| `R0994` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\0e\0e3ab27f6b7313d89eff1136c4cd60913e591fe5b32961c87e7711778f2dc906.meta.json` | 376 | `not computed` | ledger |
| `R0995` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\0e\0e46ac1ee13b0e49a5342aa037dfbc8da0bbe1aadf5e0d149e1edaf9590fd80c.meta.json` | 383 | `not computed` | ledger |
| `R0996` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\0e\0e717a082a79620d79cf0321b420df15593c4916fcda03c27cb9d82e07ef5d6e.meta.json` | 375 | `not computed` | ledger |
| `R0997` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\0e\0e737a446bca4070162287dc8668461fb92425e8f656d370186311646cc19134.meta.json` | 416 | `not computed` | ledger |
| `R0998` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\0e\0e81c4732ba0f3b2410a8b84299adfda9176be589117dadc41e9e7d0d77c30aa.meta.json` | 401 | `not computed` | ledger |
| `R0999` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\0e\0e891db802ed81a07e5af6a95bb5fb3e633791915b8270a8f627c835666db83b.meta.json` | 393 | `not computed` | ledger |
| `R1000` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\0e\0e95500a7ba271e4c6c9f5d136f59d97ee2ceb89fad12dbcfaaa3e7c8328a63b.meta.json` | 384 | `not computed` | ledger |
| `R1001` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\0e\0ea114886ae3e0dd1e01c803c2319e5127bc04b331670e7b2fd4579d30aba13b.meta.json` | 379 | `not computed` | ledger |
| `R1002` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\0e\0ea429dee0f3539807eb3cbc034a62b613b84f3b676c9a925b61092b4f27980c.meta.json` | 419 | `not computed` | ledger |
| `R1003` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\0e\0ea45da4c7d1b437e1564090bb995399f490f861b87444c73567680787c0ee55.meta.json` | 388 | `not computed` | ledger |
| `R1004` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\0e\0eb1023c25a1498ad0f016b83bc84acc800cda2f460474d75802f36850e92dfe.meta.json` | 375 | `not computed` | ledger |
| `R1005` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\0e\0ed1702b9e21c2e1f27f19de17dd162f3c76b9ee1ec51efda5654db4a56e024b.meta.json` | 352 | `not computed` | ledger |
| `R1006` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\0e\0ed3c56df6a5075e0d9b98594b9cd92c0c2b224ab064555c054c05701014d533.meta.json` | 377 | `not computed` | ledger |
| `R1007` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\0e\0eda0b8b5a4e2a936efba8e26a42694902d48bf7a9dbd490421bfba00c1858c1.meta.json` | 376 | `not computed` | ledger |
| `R1008` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\0e\0edc859b239f52918535b69b1afd675e2021e04474d08db3b931c69ba35caf98.meta.json` | 397 | `not computed` | ledger |
| `R1009` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\0e\0eefaf8e719910f1ee138d17c5330ef972ede7aa5870868a200c48c1c607147d.meta.json` | 380 | `not computed` | ledger |
| `R1010` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\0e\0ef3ceb3f126e9f16d5014026995961d6827bc015e06b0def7b0b2f57c90f29b.meta.json` | 381 | `not computed` | ledger |
| `R1011` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\0e\0effeeecadc71257d6eabcbd4cf43277ff35c6aeda0e7ba4c60ab67676bf49de.meta.json` | 373 | `not computed` | ledger |
| `R1012` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\0f\0f029cf14cc3349c1b01720b38fe3b3aeea6d4399a30ef9ab195a612ecf85a75.meta.json` | 387 | `not computed` | ledger |
| `R1013` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\0f\0f86cc4d9a4f0b35f65f068698e20090d663072cb559a6e50291488802e59411.meta.json` | 404 | `not computed` | ledger |
| `R1014` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\0f\0f9c6a872db7d3e0f81f44e50a5f0adc666fd90964ee0f71ba404e59374ff667.meta.json` | 394 | `not computed` | ledger |
| `R1015` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\0f\0f9c9f7e98530db66aa6e988a2ee08e8a0f0a7e09693bcecfcb90b5cb67dff10.meta.json` | 385 | `not computed` | ledger |
| `R1016` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\0f\0f9d489fd42bda758589c600397fdb2697858262770549045e7bd73e6034e03e.meta.json` | 379 | `not computed` | ledger |
| `R1017` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\0f\0f9f8e3e3ce965a820e439fc1bc91d91a7d0d8c0b0d996c5cda6b6910d070c02.meta.json` | 387 | `not computed` | ledger |
| `R1018` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\0f\0fa769d609840e3b43a7c840c1073eaab81aba59cbe2296daea90b0ddfa0f6d8.meta.json` | 374 | `not computed` | ledger |
| `R1019` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\0f\0fb99dac327eca1278c7b5112239a730c0535518a0c9adf7e7b86af1d4fe83c9.meta.json` | 398 | `not computed` | ledger |
| `R1020` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\0f\0fc55c958525b88cc4808ba3e791c9e8f0fb3c1a3407864f9b51d1e4c92fc178.meta.json` | 406 | `not computed` | ledger |
| `R1021` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\0f\0fcb114acea868da73c407c2b252dede24e36ee926560da4d37c015a22f6246e.meta.json` | 385 | `not computed` | ledger |
| `R1022` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\0f\0fcf57ef731b1f878345d9e16e76086c4ae6d9ae9ede335ff238b8448ea67062.meta.json` | 358 | `not computed` | ledger |
| `R1023` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\0f\0fd0c6a961f352f1694d3a1ee5bb43127789182d16e5fd63a72f2402a43e9a92.meta.json` | 374 | `not computed` | ledger |
| `R1024` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\0f\0fd153f11c7e98ada9f11eabe1b5b1c6a8188645d1ea53663e3d915ceb1e329c.meta.json` | 402 | `not computed` | ledger |
| `R1025` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\0f\0fd73c0fb58e3eba0e3bc1860eaa417954a3d74346166ba71b4a364e87638c85.meta.json` | 388 | `not computed` | ledger |
| `R1026` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\0f\0fe5e952915181406765e035b4783330e82e6dee8809564594e03830bd2ad53f.meta.json` | 380 | `not computed` | ledger |
| `R1027` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\10\10156fbcf4539ff788a73e5ee50ced48276b317ed0c1ded53fddd14a82256762.meta.json` | 368 | `not computed` | ledger |
| `R1028` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\10\101eb0363c97dbd7304cae4b63fa12d10f10e98ae0776f2eaa4f7e915cc02391.meta.json` | 403 | `not computed` | ledger |
| `R1029` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\10\1021c68c8755925a6048e203d662c05aa4df0a753af119c20a7870c456b51494.meta.json` | 393 | `not computed` | ledger |
| `R1030` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\10\10281bc404f429165a330b800eb64674e37a135d1b4c689e57fb1d9e827d6924.meta.json` | 386 | `not computed` | ledger |
| `R1031` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\10\102ee26fcd825879e8ea2aeea235b2b4481b1de3d63809446e30e0926842316a.meta.json` | 357 | `not computed` | ledger |
| `R1032` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\10\10339cab93aaca39546aa9890022815ac45be52b6e1604da425dd894e88cdbe9.meta.json` | 394 | `not computed` | ledger |
| `R1033` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\10\10352e2a61e06a9fce26e29b5a63acbce14a0a148b6ac0ec8d7af6d0efce8d2d.meta.json` | 400 | `not computed` | ledger |
| `R1034` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\10\1035371e7be8e275f7bb8551c70e6ec874190b9f6ef91897ac8c4c87318fbcf8.meta.json` | 435 | `not computed` | ledger |
| `R1035` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\10\104d698e79d6e10a2b4ab989bccd68163ccc4e2e3be3b9579e04484f5decb099.meta.json` | 417 | `not computed` | ledger |
| `R1036` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\10\1059e35ffba5a7eb4fc948d05f9a6642dba0d4e14bfc071cf1b70c6cb77e7d56.meta.json` | 398 | `not computed` | ledger |
| `R1037` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\10\106ea1ac23e95e578f79f2f1150587858f486f61dfd2006f10a466a5afd8675d.meta.json` | 422 | `not computed` | ledger |
| `R1038` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\10\107801e641e2554ca8a0d23bd231d65c56f4c79022dc42567caf16df4621ed64.meta.json` | 377 | `not computed` | ledger |
| `R1039` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\10\10803250a037413e7d04c281a4c1bcfa8c33c9786c1164ea61059db80153710e.meta.json` | 407 | `not computed` | ledger |
| `R1040` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\10\108144c6b597ff59eb97521bfbe18ea2bef4598a8bb5db870727a76f5bbdc47e.meta.json` | 385 | `not computed` | ledger |
| `R1041` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\10\108fc48e3653f78e85517b527a2b51fd336d5367d7b5ffb0d525d28706e9eb6a.meta.json` | 386 | `not computed` | ledger |
| `R1042` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\10\1093b16f21fe26bcc558cfb32358d8c7e58214c86468ce74f1edfaabac09a5cc.meta.json` | 397 | `not computed` | ledger |
| `R1043` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\10\109cd921937252d2658e9dfe5a372cc88aeac56f8752c7d6ce1b96f389ff4eac.meta.json` | 386 | `not computed` | ledger |
| `R1044` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\10\10a5f318bb014296e57d9a3f6ffa51d478e21b07d5bf978597dba2ec9dc21e4a.meta.json` | 380 | `not computed` | ledger |
| `R1045` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\10\10ab3529e00e4019083bdf6d302c741fbfe5a6abeaa6389ef33599e93fdb011e.meta.json` | 400 | `not computed` | ledger |
| `R1046` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\10\10b9d4cebf06f2ca75762cdd82b3ddf2d3a2d99e2343b528b9ecb4db56f62e55.meta.json` | 380 | `not computed` | ledger |
| `R1047` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\10\10e28a52517d6e1d022cd10ff13cd7cd7e30ff1579922bebd4fbad7dd7facaf5.meta.json` | 391 | `not computed` | ledger |
| `R1048` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\11\110856afb84f4261328787eb4b0364f3a21a3aad4e94f75877cc841d0c900ce2.meta.json` | 359 | `not computed` | ledger |
| `R1049` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\11\1119714f44c8f5a39cbb5c9d0209e6fc13e7d5c18015dff3234adb5c52fa84a1.meta.json` | 382 | `not computed` | ledger |
| `R1050` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\11\111bfcaba8cc3e5feca36b68d84439fd0de0219cc3487f89de793a14ee36143a.meta.json` | 390 | `not computed` | ledger |
| `R1051` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\11\111f898d9814db01095a4e4ad3a8870053e35580f588c92f8e3134ae534eb766.meta.json` | 379 | `not computed` | ledger |
| `R1052` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\11\112736d80d3b266afd84fc47a63779c560ef82115728cf1e20a2f05be6c2c152.meta.json` | 379 | `not computed` | ledger |
| `R1053` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\11\113dd57572b58c191cb2bb0230dd16795fdb2e996b41caffa2c8112d85db9317.meta.json` | 386 | `not computed` | ledger |
| `R1054` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\11\1144d25052d06f163a666a3fb1d33ee4bb37db7bc81d305f37c4cfba5a9e1d46.meta.json` | 384 | `not computed` | ledger |
| `R1055` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\11\1154611100aa471ce1794ebcbb9906812f29925b3fb1448cf565daf59f58de1a.meta.json` | 388 | `not computed` | ledger |
| `R1056` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\11\1170985b66e60e4aa1ba09e7ce349fdc4b25baed3df3c50bc5b5e870a17e3a62.meta.json` | 383 | `not computed` | ledger |
| `R1057` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\11\11781b314700b4168d8fa7189acd19c1e23134e4a838f7101bc12a5e5f476213.meta.json` | 391 | `not computed` | ledger |
| `R1058` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\11\117cb19af30d1982de97750cc563d0ac5dc3dedc22f60aa25847a90b5ce2e0d2.meta.json` | 408 | `not computed` | ledger |
| `R1059` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\11\118944837bc31b2f0b0c389111c680ecf6fcea2a47361d9b41a66144b1030459.meta.json` | 386 | `not computed` | ledger |
| `R1060` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\11\118e7fb6a1a9951a3e077709b6abdff470b7e2740aaf924d832ca41d68f9abf1.meta.json` | 373 | `not computed` | ledger |
| `R1061` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\11\11967625bf68fd01a7a2ba87f4c5462efa7aaea8c1868d971fb6a1313ba744d7.meta.json` | 390 | `not computed` | ledger |
| `R1062` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\11\119bf92ba7532ee31fd3217d905566576bd75cd8df6a5a65d5766e411b825330.meta.json` | 359 | `not computed` | ledger |
| `R1063` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\11\11a6ebf2d54f9da602667b2a5b777c15dd079b6f0e65baaca1864734fa921056.meta.json` | 396 | `not computed` | ledger |
| `R1064` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\11\11b887abe5b3fa11c2bb760fcf545bdbbd053666869f18c67e6ea9f10facec44.meta.json` | 393 | `not computed` | ledger |
| `R1065` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\11\11baba2de532c48cc4f3f2c6ff1bda3d1c6d448943da04ed54a139532786a11a.meta.json` | 404 | `not computed` | ledger |
| `R1066` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\11\11bb300d1e516071b06a334fb9a173368b01484b3f765016afe2e35a40461bcf.meta.json` | 411 | `not computed` | ledger |
| `R1067` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\11\11d474b2e6ff4e37f6fbb68fcffe1550690ba9cd70d8c203423cb047af31f42e.meta.json` | 376 | `not computed` | ledger |
| `R1068` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\11\11d8462e134e8efe8f4bd52372292a72ff0b670753d2f49f71675eed0dbfd085.meta.json` | 382 | `not computed` | ledger |
| `R1069` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\11\11e6b83b0245acc33272da14be4b8a1a5f4da045cd980a0edb628b56edcc4232.meta.json` | 380 | `not computed` | ledger |
| `R1070` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\11\11f0194d0a734c9d54098de9f5e9efb9a2540aa7e8ac434ffd03ff0d5594ec3a.meta.json` | 400 | `not computed` | ledger |
| `R1071` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\11\11f43e5fbd0a9078010055f6a483dc09497830d3f564d44e697394ef9bdd8aa3.meta.json` | 422 | `not computed` | ledger |
| `R1072` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\11\11f908aeb79417a4eb718a41a35349f06395fe9fe8fd85e0ddf4a9b413795d4a.meta.json` | 425 | `not computed` | ledger |
| `R1073` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\12\12004dbff0ab7b34141ff53e33e616db2e857c695f64e640631f5abe30619145.meta.json` | 376 | `not computed` | ledger |
| `R1074` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\12\120470f1958675ddae2b8a82643f3dafd550b445e69ca0f1e7d3a90742b9f1ab.meta.json` | 405 | `not computed` | ledger |
| `R1075` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\12\12098571044671c24ed0011e2bb7d94976380265e5734c30f856479482e6f88d.meta.json` | 377 | `not computed` | ledger |
| `R1076` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\12\1209f5efd3a71eab580816125a047f2bfe5174d72cdd9f41081ca06d129b0b14.meta.json` | 379 | `not computed` | ledger |
| `R1077` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\12\1210c01446a63429910222445121ad3dadb5222a4e0d6adfe8c37605e9b46b3f.meta.json` | 390 | `not computed` | ledger |
| `R1078` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\12\1224975fa8cfb5399bdba16258d6ec01cf76cb38212bd709f800028714edd67e.meta.json` | 403 | `not computed` | ledger |
| `R1079` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\12\1235a2a3ec85c1f904fcdefae1b613683473d041d26759f425e3e42d23468ad9.meta.json` | 429 | `not computed` | ledger |
| `R1080` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\12\1256c0433b0dc3821f53a83a46eb115cf6020ba868974d9b40d94723f2f7bae6.meta.json` | 372 | `not computed` | ledger |
| `R1081` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\12\125cd2377204a11b3583a896327cd5215f07d31f56484175c018e6d9ad01cb11.meta.json` | 379 | `not computed` | ledger |
| `R1082` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\12\126047710f44c42e1fe3bb5a0fb4bb1ba55a324afd1e3ca7955f0d7535d5e624.meta.json` | 379 | `not computed` | ledger |
| `R1083` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\12\1261c1e0b8c412c0be2da200b14ee39bef1fdca97c21da786f7cb9b1cd75de1d.meta.json` | 335 | `not computed` | ledger |
| `R1084` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\12\12846d55381fe45d27e22be6e4592ca574bc1b328c488ef040486860000beed8.meta.json` | 404 | `not computed` | ledger |
| `R1085` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\12\12a2dd838fdbef8ead398f01ee8f2ec5754e91b12cc042a122815d70aac8f5cb.meta.json` | 403 | `not computed` | ledger |
| `R1086` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\12\12a304b84574fecc785db1737ed6d4ffa55f1ad3b0f536ecd299b4795129d9c0.meta.json` | 401 | `not computed` | ledger |
| `R1087` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\12\12b457ae6c336b5c60556e0e004370fc1f3255ced67d66c061886200edc27368.meta.json` | 424 | `not computed` | ledger |
| `R1088` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\12\12ba291eb095f685fa2d04f25d12518d5fd13039680d0f83769004b2c0cad748.meta.json` | 382 | `not computed` | ledger |
| `R1089` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\12\12cf6203832cdbdca53f94fb3ed8686b30498076da50e515db4f08a8ea9b885b.meta.json` | 397 | `not computed` | ledger |
| `R1090` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\12\12d22fecbb47fe643ef6a7ef8d5480d68fda197bb4b6a3cd9d6bef5a39c3f9e7.meta.json` | 413 | `not computed` | ledger |
| `R1091` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\12\12d517af6fb273db27fa5912336e7cc6ddf96446fd594e6b2d78de923b2164ee.meta.json` | 419 | `not computed` | ledger |
| `R1092` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\12\12f04bb118dc4d132b3aec8790b9494ba5ce0cb05b6ac365bd5cdc7bb71b46fa.meta.json` | 388 | `not computed` | ledger |
| `R1093` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\13\130a35b917df1951aefbf366120491d5124045a87ded123f20ded21521f4e3a2.meta.json` | 406 | `not computed` | ledger |
| `R1094` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\13\130b9c6b4f18bbfe9740ca1c935ec9db4a1121aa07c0bcce371dcd7746c64bf0.meta.json` | 421 | `not computed` | ledger |
| `R1095` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\13\130e3a64d5fdd5d096a752694634a7d9df284469de86e5732100268041e3d686.meta.json` | 409 | `not computed` | ledger |
| `R1096` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\13\1311f9626e2993b7503c422442bf512629b97deced7414304813efa6f13ee413.meta.json` | 379 | `not computed` | ledger |
| `R1097` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\13\13141a7524fc12d82959eefaac55361ce0e000f25f702a25309d1a268b0baefd.meta.json` | 399 | `not computed` | ledger |
| `R1098` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\13\131c50b3fdecf31be012cbe3e8ee1a1964c8734ba45ed02d50cf4952ce43ea94.meta.json` | 398 | `not computed` | ledger |
| `R1099` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\13\133e0ef2947fbd3f1d6a7fc5bea0584ba7600df05710c7d57ebcdc754a167e2e.meta.json` | 385 | `not computed` | ledger |
| `R1100` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\13\135b154b3cc2d83caa725dabd8686b18488089bc43fe0ea9cfb49cc81b23c6b9.meta.json` | 385 | `not computed` | ledger |
| `R1101` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\13\136d180c964920aad44327ed3a6ac9ac0b97ba60c6662c231f237620a282c9b8.meta.json` | 378 | `not computed` | ledger |
| `R1102` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\13\137dd1d2692735cfb9799f5482eeeeec0bffbd4c40690a0c4ed771dcc71ecb15.meta.json` | 393 | `not computed` | ledger |
| `R1103` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\13\13a7f79d8708e9d6c4b8ed069b2eb5a3380653fe7dfdeebd902d3c6b4e8406ea.meta.json` | 374 | `not computed` | ledger |
| `R1104` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\13\13b33396b564d9a05b961547561c625047184b7284057ec8dbbe0dc61471b11b.meta.json` | 382 | `not computed` | ledger |
| `R1105` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\13\13bb347e660f99ef0107f5ecc737d5f2f83199e3a9dc8bfe7dcd7010fc178792.meta.json` | 385 | `not computed` | ledger |
| `R1106` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\13\13f21e20674c9fd9d2350699d4560de649d10c50b155fa49e01548f7d6c32004.meta.json` | 363 | `not computed` | ledger |
| `R1107` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\14\140d94f58c99e4839b589557df535453ba2e29868cd0975463791d8914fa3c7d.meta.json` | 402 | `not computed` | ledger |
| `R1108` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\14\141f3b388130e52e19d23c955572f672c7a08251dacddcaa3f6f1acb7ac38988.meta.json` | 385 | `not computed` | ledger |
| `R1109` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\14\1422cee0abaebe10cf9b8723132d7c0c63e0860e80433abcb07cf0998b9d4e2a.meta.json` | 400 | `not computed` | ledger |
| `R1110` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\14\1427fb5142d291fd7472e4d15164d0112cf1825d564fc7b6682cb791fc998a7b.meta.json` | 387 | `not computed` | ledger |
| `R1111` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\14\1458bf5f11271ab7c977b3b1b635454fa5850b6b54a8a85557c7e641f6f4cfca.meta.json` | 416 | `not computed` | ledger |
| `R1112` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\14\1469644bfc9afc3a230933fe2fbad8846ec5f2dc13f6392826bcb060e8c94141.meta.json` | 376 | `not computed` | ledger |
| `R1113` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\14\1484afd5de11f75ec18b9c498ca2b2f0ba3a025164574d16bd2a01ee5dda700e.meta.json` | 380 | `not computed` | ledger |
| `R1114` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\14\1494e1ab3e34f2d82f8e135c88de5648083ebf302fb7fd650f75f93522088385.meta.json` | 353 | `not computed` | ledger |
| `R1115` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\14\14ccb4e8ffffcba8cc8d473ccf765c41d285fa9999db3335e3fbc17873c68542.meta.json` | 388 | `not computed` | ledger |
| `R1116` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\14\14cd79e1f0759717cea52a5e5ba6d639595de64241804b98c93f6e76df8470ad.meta.json` | 380 | `not computed` | ledger |
| `R1117` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\14\14d2a302b4b5bda74710ddd95da65d0cbaaf706e7d19b17a024e4cf1132c4cb5.meta.json` | 384 | `not computed` | ledger |
| `R1118` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\14\14dd215721c929e4f8cc6def4d9e28dd026469c1c5884e149cbf5768943c8fb9.meta.json` | 366 | `not computed` | ledger |
| `R1119` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\14\14f01aad68e17e104cdb65d98a2aae6aa5a89d233f92d3a22c3f20796ad9ab07.meta.json` | 380 | `not computed` | ledger |
| `R1120` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\14\14f7dff1af6d195dfe292bf64137b4df60c94e5e558d9428864395ba2c87dddd.meta.json` | 389 | `not computed` | ledger |
| `R1121` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\15\151a5f89c76149288298339f0ec38ce0f72a6818e6f0168cc17318b1a25ed91d.meta.json` | 381 | `not computed` | ledger |
| `R1122` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\15\151e7188de776df2c16de9e7eb56e11e08c5b481c5844375f3ca51619c11e598.meta.json` | 368 | `not computed` | ledger |
| `R1123` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\15\1543e5b8db61e6e1e0c8aaa3416ec72a6c96838c035e3dd73c90880bd659b8eb.meta.json` | 410 | `not computed` | ledger |
| `R1124` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\15\154b2d60f6700c5d79044b80111a971ea20fbc2d4a63548bdb4a8b8fdf7d173a.meta.json` | 393 | `not computed` | ledger |
| `R1125` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\15\154e3054e8a2f0df821750f2c4d63979376423f0cf0cf10becbaaf611c16509c.meta.json` | 379 | `not computed` | ledger |
| `R1126` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\15\156d70fa191cf50830686a28bccbe6d1963bdf0fcd7327167460147c3b0d1b1c.meta.json` | 404 | `not computed` | ledger |
| `R1127` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\15\156f4cb165626e4f108fc5ad947564e58820fc4f0b66065538edb6fd6140d306.meta.json` | 394 | `not computed` | ledger |
| `R1128` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\15\1580ee371b0a28c652af31372bc05dfb1077922a6e45a497f43891df7387ba0b.meta.json` | 385 | `not computed` | ledger |
| `R1129` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\15\159c2df33b4ddc33b86a59f6ac13f16a48d250ca57acbbe8ffbb5d12b68974a6.meta.json` | 385 | `not computed` | ledger |
| `R1130` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\15\15ca3d259c6b5d0a158232af98716ecd3d26a205a8f7ec078836b9d428d38a8a.meta.json` | 411 | `not computed` | ledger |
| `R1131` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\15\15d78f19cb664d0b81432403d3aff0ab01986293a77a2447bbd97b179a1c32f6.meta.json` | 412 | `not computed` | ledger |
| `R1132` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\15\15e134f00950c57a5a7b835bf2687d9c661c907575072c24a2c09c05362639be.meta.json` | 409 | `not computed` | ledger |
| `R1133` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\15\15e1e2ed2c49dd3846d2d55eb3a33fc7f2bec31f774619ac22a912072d182a42.meta.json` | 377 | `not computed` | ledger |
| `R1134` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\15\15f4dd843c27484811d86d4a343334b0f107cc6045d4f7a1fbb161d2bc71f622.meta.json` | 407 | `not computed` | ledger |
| `R1135` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\16\1600fadc0eeea5662bc3469e35edea271ae0371376dc897e81a97c4d363db919.meta.json` | 398 | `not computed` | ledger |
| `R1136` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\16\160d6b944272a256a46e8d33086156a12da3913833670809667adf3834771654.meta.json` | 404 | `not computed` | ledger |
| `R1137` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\16\16185ae7e8eb0a6464fffaecbf1e826c3159ec43dcf0138f0d387e9b264b9213.meta.json` | 411 | `not computed` | ledger |
| `R1138` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\16\1633fed3bb2e4c176a82dc2210d4f4e0ffb8ed407883d279fb6d0841d5c01e13.meta.json` | 401 | `not computed` | ledger |
| `R1139` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\16\16408ccb8609d3131c88b4a62e663a91d5abd905b5d4d0713506eb1d3dd38711.meta.json` | 381 | `not computed` | ledger |
| `R1140` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\16\164d4c73a1cc452027759f636d37f899f97b0dc84972d428671376bf155e3c4e.meta.json` | 396 | `not computed` | ledger |
| `R1141` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\16\16538d118767ae21a74264a83975fb4145caad201f082615ad53068f1641065d.meta.json` | 386 | `not computed` | ledger |
| `R1142` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\16\1654aca26e445f42d5900dca5b2df8c879c27cbb6a5fe6487a95ca87eef4ae97.meta.json` | 370 | `not computed` | ledger |
| `R1143` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\16\165bb0cbc19ea756c0d61795ead0d5bc28ca4f44d602f921a63e94f1f545c099.meta.json` | 352 | `not computed` | ledger |
| `R1144` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\16\167285cc07a7069e079b975f5dcc3590e4499de23db2a706937e4bb89c21cf6a.meta.json` | 358 | `not computed` | ledger |
| `R1145` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\16\16818091972c10d4314f45c497b47000e007dbb367f480b03ad44f17926825b4.meta.json` | 392 | `not computed` | ledger |
| `R1146` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\16\16a5ebad3914e67818341ff16fa72baba800a6692077c3f4a7f6df0974829ca8.meta.json` | 434 | `not computed` | ledger |
| `R1147` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\16\16b1ee991144534fc98bed07208a0ec75a07ae255a4d72a93732ea8ae74021c2.meta.json` | 401 | `not computed` | ledger |
| `R1148` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\16\16c76a6c8409388ee2846ecc67f2b8614403678ce8fab6986e28550dee3653d1.meta.json` | 373 | `not computed` | ledger |
| `R1149` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\16\16d68de0eca6c1650321c2b280d78f91d49ca1d1100b3a7ccf6afffe82b88b53.meta.json` | 397 | `not computed` | ledger |
| `R1150` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\16\16de38289cd3cc632629f7ff6573fdd658b65785a19af132d7a3ca05cbf8bd99.meta.json` | 391 | `not computed` | ledger |
| `R1151` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\16\16e0c6ac0634ed3d9811428a476a82cbe88ffb454ac37413773f0624cec57563.meta.json` | 383 | `not computed` | ledger |
| `R1152` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\16\16f9c8c72e5f10ebf335be564a45b33e4ef267dc88bf4c8f664f6f3674bef37c.meta.json` | 405 | `not computed` | ledger |
| `R1153` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\17\1701f78f500b8ba6beb435f8861db4d9ba900c3625c5b7d8237cb39c49fce3dc.meta.json` | 380 | `not computed` | ledger |
| `R1154` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\17\1702a1b8f1c497a99f816a3aa94509b2ba2ce357ec480308c015e406c6bcc15e.meta.json` | 376 | `not computed` | ledger |
| `R1155` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\17\1709d2c977d9530ae689fbe8efc1bb098010b1eccb8dc5a489a5f87a1edbc504.meta.json` | 362 | `not computed` | ledger |
| `R1156` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\17\172fefd2ca27efe8fe03a636dea56d523151dc0a1cf5a8ebb56a0c68a719ef65.meta.json` | 397 | `not computed` | ledger |
| `R1157` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\17\175aec7b701a70df6bb1f2674deb839e36cde75affa2e1dcdd62f26248e45ffa.meta.json` | 380 | `not computed` | ledger |
| `R1158` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\17\176c1e253848ea5128840c6af15945e212d2edadcaf58e4aa260b5537cd77339.meta.json` | 403 | `not computed` | ledger |
| `R1159` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\17\176e01d2ed94fef3e872667082aa4df3726dc1f15201bb25dd578f58024205b1.meta.json` | 386 | `not computed` | ledger |
| `R1160` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\17\1777564a4802c2f898853328041a722127d179c5c9c0b67a0a73eac27107dd99.meta.json` | 383 | `not computed` | ledger |
| `R1161` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\17\17818dd567936fde032404fbbd6177844b9f5fc5a915480f567272147936f917.meta.json` | 385 | `not computed` | ledger |
| `R1162` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\17\17832de47b5dc23e46253ba16462520036f28d9a27d5c30157784952ca4e69b2.meta.json` | 391 | `not computed` | ledger |
| `R1163` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\17\17849da0c76441345e12c974fd4214e7eed5e06f03a7b4e3e7e474a7eff5511d.meta.json` | 387 | `not computed` | ledger |
| `R1164` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\17\178732502fbf4c1f504852c0a3673b738e2b0ba35460882b7c6c7d3ea58f48a9.meta.json` | 391 | `not computed` | ledger |
| `R1165` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\17\17a31d506376dff798f17a9050776366ae046c9fa72811e7b828bd35f9cde75d.meta.json` | 402 | `not computed` | ledger |
| `R1166` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\17\17a422ece2eb6d4adc6498811863c48eecaf93533b8e939a2327b04c22555b91.meta.json` | 395 | `not computed` | ledger |
| `R1167` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\17\17a89d66f55607f7ebb06afb21004d4798f73985e7dd558002b38db8feae7029.meta.json` | 385 | `not computed` | ledger |
| `R1168` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\17\17c0108e019452b98dd25a0c2e24e0b2d33e334f1ab9fa0f238fae609918b587.meta.json` | 400 | `not computed` | ledger |
| `R1169` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\17\17c1a697b803ee398cc8c2242af1e25cb7e3ee45b2cf5ef95f5fb9fe2685c799.meta.json` | 402 | `not computed` | ledger |
| `R1170` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\17\17c268b21455ec88827318fa56630ae23c5186feafe02dc0a422562a0f0028be.meta.json` | 388 | `not computed` | ledger |
| `R1171` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\17\17d3cbc7a4dc3a4fac77474e6ded2758bcb3e0785b1efd8aeefa11fe4a25a465.meta.json` | 402 | `not computed` | ledger |
| `R1172` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\17\17d6cde7fca2e55ee72d0512dafb1fa3b81b601d5c66748042251364e76fa8cf.meta.json` | 406 | `not computed` | ledger |
| `R1173` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\17\17daa96ffba4a3f0b00f8ba63dcf28bc8af81f3eea0261d8f38ef93ad72f2d75.meta.json` | 383 | `not computed` | ledger |
| `R1174` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\17\17f1eefbd1c2fe5326cb7592ff3af92a773582cf9d01727b09d3ab864906ee50.meta.json` | 386 | `not computed` | ledger |
| `R1175` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\17\17f9442dd9cb837c88da9043dee48ddc134e607838b523836992d9dd1980035f.meta.json` | 364 | `not computed` | ledger |
| `R1176` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\17\17fadb41bae4a289a0c6cb24747a4fd23509ed309f7b40400c0124aba089e273.meta.json` | 404 | `not computed` | ledger |
| `R1177` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\18\181078da96f199481d4406d280b4d1ad64046a9c8b0834a3c53db50cde108d4f.meta.json` | 390 | `not computed` | ledger |
| `R1178` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\18\182fe7d086154615075091b7d2a9fcedb7c262b0000b6e5c94e7dd9353175660.meta.json` | 384 | `not computed` | ledger |
| `R1179` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\18\1852cc3d15f47059bdc66b52cea5830977444b1c33ca123b063abc92c7b9ef2d.meta.json` | 382 | `not computed` | ledger |
| `R1180` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\18\1854d77677dac763c89d0e9022cc7c07ea57c0764788dd0659714de490f9a3e0.meta.json` | 397 | `not computed` | ledger |
| `R1181` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\18\185e52a5a9c6c2380a2a861aae2df649db5d3965975e37bcc555f9f99cd38cb8.meta.json` | 384 | `not computed` | ledger |
| `R1182` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\18\1860b12165fb7ed336ddab9d306ef38e18fcbd36bf695904c497b825f83581dc.meta.json` | 365 | `not computed` | ledger |
| `R1183` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\18\18690ed1e6eca0fbd538f35f7980b4b4df4325688168b5d7ce342106b017bcd1.meta.json` | 395 | `not computed` | ledger |
| `R1184` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\18\1886ba728aecc0cfe13743c0a20322bb0d1b421b1a45c8dc4e08050891ae449d.meta.json` | 417 | `not computed` | ledger |
| `R1185` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\18\188733a381950e3853192ea3a632a83db68a471dce3a7c7abeec25ce055338b8.meta.json` | 393 | `not computed` | ledger |
| `R1186` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\18\18ac0ce561c0c1dd839ababb4f2ac01c41968533bff54289254982efdd4970c9.meta.json` | 377 | `not computed` | ledger |
| `R1187` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\18\18b5116b7b05112644d3fd112bedc6aa67daf7a8ad047c3c2e5b0dcb2f443ede.meta.json` | 406 | `not computed` | ledger |
| `R1188` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\18\18be272a2a3d90b9585fa7d6de5189bedba93427e7e39c9bf8d820e624ad0d2b.meta.json` | 382 | `not computed` | ledger |
| `R1189` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\18\18c49c5355f5273a9cd211509269d3dc839f2643f7f5647998a64ce156627ad5.meta.json` | 385 | `not computed` | ledger |
| `R1190` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\18\18cc8c4d4170726286e289eb9e23522bf2916de12134079f1d785430defaa4dc.meta.json` | 419 | `not computed` | ledger |
| `R1191` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\18\18d4deb351550f4147e843bccc45ca30217fcb6e02d68841e9d75ffc841595bc.meta.json` | 387 | `not computed` | ledger |
| `R1192` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\18\18d694a16c92ffc53dc20612734d1080ac8733f5ee0ef99b943f12448ae172b1.meta.json` | 365 | `not computed` | ledger |
| `R1193` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\18\18de326f36dbf80e3172d6538e1eefdb3ff301caafe349ad3e8f2e379bb7f8f8.meta.json` | 378 | `not computed` | ledger |
| `R1194` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\18\18e30c2a2b03c593bc06485925dceb9fd515f451017a466e0e7d0e23831b9a54.meta.json` | 380 | `not computed` | ledger |
| `R1195` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\18\18ef6944ddf05c2da441aa2f2b9ed368b60131cdc896d387f763ba404c3a604d.meta.json` | 387 | `not computed` | ledger |
| `R1196` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\19\19060ef465e1797d682ee0fc3081bd25ab1395e995e43d25c9d13c95d9a3cd6b.meta.json` | 432 | `not computed` | ledger |
| `R1197` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\19\1939dd58384b4eb517d0f05aaeff09857b172570cf82135dead64bde77756586.meta.json` | 384 | `not computed` | ledger |
| `R1198` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\19\193df14106c6c7239a03d7f77d6ba0c6308f4861a9978b7e9f9734471d5901c3.meta.json` | 361 | `not computed` | ledger |
| `R1199` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\19\1950f47c89cf18019787e07d8ce48f66d6b38e622f7d94d70a90247fee6c040e.meta.json` | 381 | `not computed` | ledger |
| `R1200` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\19\195c24a34a464aeb31b901cedf9b4bfcdb7f0292f47e65582f72221c76292d6e.meta.json` | 376 | `not computed` | ledger |
| `R1201` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\19\19623132815dada9ea5c7c4883227f768bc904d7c2c5cfce4259d21b14df1cb1.meta.json` | 398 | `not computed` | ledger |
| `R1202` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\19\19674747e6d50009150651c8d6c0cccf59fc3a07a485edbe014dbd4c927b8072.meta.json` | 395 | `not computed` | ledger |
| `R1203` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\19\1973385003a7ac55cdb46a3400b341c109afbd5b897dd9412229a3fd283df027.meta.json` | 390 | `not computed` | ledger |
| `R1204` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\19\198133ff42705b4d24d3501c3f8cc0e8fac814708bb3c5e44aafc70eb013871f.meta.json` | 376 | `not computed` | ledger |
| `R1205` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\19\19893212cedd46ed4e077b8e648fee499eddf1202e0eedb38b6b9b94a72fec92.meta.json` | 395 | `not computed` | ledger |
| `R1206` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\19\199d65bd9f0f524d7e2d386ad4aba2a9212732a255aa21e8fc0fb5e9a2ae24e7.meta.json` | 379 | `not computed` | ledger |
| `R1207` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\19\19a2db7e9dde8bf3912e772611fa7e9fc7ef45f875d901b1739c18e09c2ddee3.meta.json` | 382 | `not computed` | ledger |
| `R1208` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\19\19ef4e6de053924db7b314511fd8f8caa7d183d2c8a3908c04346e6664f8af16.meta.json` | 386 | `not computed` | ledger |
| `R1209` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\19\19fae4994ff04e3a4b90e7ed583b866b2103755dd13e93761915505fad558162.meta.json` | 418 | `not computed` | ledger |
| `R1210` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\1a\1a0e97da23151eb509ed49222993d4ccd851cbae47ab53c6f93940cfe47914a8.meta.json` | 401 | `not computed` | ledger |
| `R1211` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\1a\1a177ebe431de446020a0c821ad3ca3b9f27a7d704281402eaa9017881052368.meta.json` | 394 | `not computed` | ledger |
| `R1212` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\1a\1a446560d64b55aab177b1182cfa021b3453fd9c38e096eb6b8c55e1d7e5d858.meta.json` | 387 | `not computed` | ledger |
| `R1213` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\1a\1a4563c28e78003b60a7258ef442e7c38600a14ed467db2c47751c86743d82a5.meta.json` | 382 | `not computed` | ledger |
| `R1214` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\1a\1a492539a8842533b3f04d3377177f85dd735f0bfb958829f08265eee875de18.meta.json` | 383 | `not computed` | ledger |
| `R1215` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\1a\1a5a443d9154e6a3cf62fe39dd7f40a3fea272c297ac1e0aa9e10c0b0ea68bad.meta.json` | 378 | `not computed` | ledger |
| `R1216` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\1a\1a5a86bdc2d7ba7759d0ab67930ec0076d545fe93dcf359ff85b8b04f070584e.meta.json` | 393 | `not computed` | ledger |
| `R1217` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\1a\1a649c9ecb24f1e7092d62c86b6d5b38648dc4bf43dac992f061f6876acde051.meta.json` | 381 | `not computed` | ledger |
| `R1218` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\1a\1a65137816af857d937c88d921f30db8c30bff7fba051a9eb5411702f3b114fa.meta.json` | 406 | `not computed` | ledger |
| `R1219` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\1a\1a6734b4e6bc9de9a4c94cfb434873e0a7f4ae4ec89549b3137ae5491cf655da.meta.json` | 386 | `not computed` | ledger |
| `R1220` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\1a\1aab70047e6c640fda4713cf5ab37e66f71d7ac76a4983bc003f42dc93b40778.meta.json` | 405 | `not computed` | ledger |
| `R1221` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\1a\1ab109f2a47e1ad9e9830b2b70a69805198de34909d2ecdf269afb2866025fc8.meta.json` | 420 | `not computed` | ledger |
| `R1222` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\1a\1aba3f87a3b33f3366808fbf92e2d94ab019accda1cb3982ce1507ae05591225.meta.json` | 386 | `not computed` | ledger |
| `R1223` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\1a\1ac64a6818c0954d45cd60f37ef668e84ab1369822e285e0138e8071acf4f1b2.meta.json` | 384 | `not computed` | ledger |
| `R1224` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\1a\1acbedd151bf881164df3ba731372866f14291db464c30a8f862c9de240a355c.meta.json` | 357 | `not computed` | ledger |
| `R1225` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\1a\1acf53905ff9d9ce39530fca41a06723abe8101926f0bc3cfa0408d805d8b563.meta.json` | 377 | `not computed` | ledger |
| `R1226` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\1a\1ad5a513e7fed3416cd08041815ae9d0836f63828ac1a3d5136f30350101f708.meta.json` | 379 | `not computed` | ledger |
| `R1227` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\1a\1adb0cabfe5e1784dc96aa28164c81e4f508dc07e91d9da7517a86769f623e7b.meta.json` | 420 | `not computed` | ledger |
| `R1228` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\1a\1aeff91a2df3be5c88c2096c0200f1e4bbc70f8e37df1c9aa08acbc7031c9b0c.meta.json` | 395 | `not computed` | ledger |
| `R1229` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\1a\1af3eb414118317d62076ce36df2b6e895093b1b6a6df8915205ee00ed5070fd.meta.json` | 415 | `not computed` | ledger |
| `R1230` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\1b\1b079cc7604b6ea878bb700fa359e9db6823f3d6c8509639a668668e93df89d7.meta.json` | 387 | `not computed` | ledger |
| `R1231` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\1b\1b0b86a833d20ad2fb75f4acb26441caa1e3880232f56b00717444ce65ed61df.meta.json` | 408 | `not computed` | ledger |
| `R1232` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\1b\1b1010c4c93d026c19be714d26237aee885172f3e23be621732b0bf12aaaa4de.meta.json` | 384 | `not computed` | ledger |
| `R1233` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\1b\1b1c11926fd3401b4f6697e954af6be92f5d032d835675600d51c929388f6759.meta.json` | 392 | `not computed` | ledger |
| `R1234` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\1b\1b1d4ad95064cd5e044b75a4dd10195bc5657a40e6723e666bebd84010ac7d48.meta.json` | 400 | `not computed` | ledger |
| `R1235` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\1b\1b1eabe7b2c6fe0baf0181aa29476effaf2b1cf3e43bb090fea736c0a9d8cacb.meta.json` | 393 | `not computed` | ledger |
| `R1236` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\1b\1b22b049b5267d6dfc23a67bf4a84d8ec04b9fdfb1a51d360e42b4342c8b4154.meta.json` | 430 | `not computed` | ledger |
| `R1237` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\1b\1b2799e7c0312a42498a21fb26e3e66a40d95eba296ba6c3905460b891e27ea5.meta.json` | 381 | `not computed` | ledger |
| `R1238` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\1b\1b377a6ff83ccc95dcb84ed046ae5a761c7f10c25a8577dca57085d1182baaa2.meta.json` | 385 | `not computed` | ledger |
| `R1239` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\1b\1b39520c46db78c28acdececbd09cb4d7440a5f53eb1c414678e3a91c46d6cf0.meta.json` | 417 | `not computed` | ledger |
| `R1240` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\1b\1b4388cfbb0e5bf4e7af5b431ee8d3c8f54476aa216fb33838e3ade19424550c.meta.json` | 374 | `not computed` | ledger |
| `R1241` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\1b\1b4adba13285d060065b9da0005acf3ceb35a8eede01eb79580845b0eb548358.meta.json` | 392 | `not computed` | ledger |
| `R1242` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\1b\1b55b674c0fb21b3230ab3a602d12fee734e1fa6b006c6347e8b4d029dde6da1.meta.json` | 392 | `not computed` | ledger |
| `R1243` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\1b\1b5c81e78eb7f28bd930c70314c920a7e207fa1056df460b790bde748fe0b32c.meta.json` | 375 | `not computed` | ledger |
| `R1244` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\1b\1b5ee4aa58164441ee91fb428839c20510e3ba6e47d5ff1420889f6a4ccd0597.meta.json` | 401 | `not computed` | ledger |
| `R1245` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\1b\1b68144734c4b66791f27add5d425f3620775585718a03d0f9b110ba3a4d88db.meta.json` | 397 | `not computed` | ledger |
| `R1246` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\1b\1b6f699775c9f13d0baa5790c5831387d4b0237fd4746eebf4a19c4306e2d297.meta.json` | 381 | `not computed` | ledger |
| `R1247` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\1b\1b876da84e5030402aa1a683d6bc126597aea8a84cc92e2eb65333d6cce4ad38.meta.json` | 385 | `not computed` | ledger |
| `R1248` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\1b\1b96362da8fed571c11fc93928719427a4c2bdbc5047168f16c7fc7f2b4dbcf0.meta.json` | 396 | `not computed` | ledger |
| `R1249` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\1b\1b9f1c695ebc43e19ed1bb76a79fede5d8d9092e3b80d9825f959c4fe19410c7.meta.json` | 391 | `not computed` | ledger |
| `R1250` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\1b\1ba2252097c80db9575b688122500b69ffcb7fd990bc0c6f13f4cd5e5770983f.meta.json` | 424 | `not computed` | ledger |
| `R1251` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\1b\1ba5c0299691215defaed8e92b8904bdbcd44a52cec3011ab975fd7b18081d98.meta.json` | 405 | `not computed` | ledger |
| `R1252` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\1b\1bae8f91b1ff41d4c987a8c3f89db6f0eefa0a6027af684b42fef60a03cfbb31.meta.json` | 374 | `not computed` | ledger |
| `R1253` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\1b\1bb36beaba498203757b73e01a0804c45e848bf5adf27e7b7902177f9bedccb3.meta.json` | 378 | `not computed` | ledger |
| `R1254` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\1b\1bce0a9fe63e42b87e8ced05da272baf16a68aa704b3718405e2735a6112467c.meta.json` | 377 | `not computed` | ledger |
| `R1255` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\1b\1bd5ac81f8aae3aa606e461364062ea592a7aa0648f864f446f7ab14f9f6b02e.meta.json` | 395 | `not computed` | ledger |
| `R1256` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\1b\1bd97c721bb63094f067f77fd2d987ecf060f0a6181da7ae24224d0871879037.meta.json` | 392 | `not computed` | ledger |
| `R1257` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\1b\1bda4e26647811220561277830a1aa987a82b6cb71d28456a7279382fe78f977.meta.json` | 372 | `not computed` | ledger |
| `R1258` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\1b\1be1708777728c38be3f5b9bb129ddcb72d056a64fd0d3dfb6cea66f0a1f24be.meta.json` | 378 | `not computed` | ledger |
| `R1259` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\1b\1be3bd28495a6dc5ea6cfc1f13feba9735f97c66a18771aee83024cfff59849c.meta.json` | 386 | `not computed` | ledger |
| `R1260` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\1b\1bf460e0c5c4bbf8401edcb52a724d168d4a664be8a43f062bc40ec40f919041.meta.json` | 392 | `not computed` | ledger |
| `R1261` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\1b\1bfb27fbc0ca8ccd6c1232c6fe8738a2f9169a25295af8fc6d78b4c9e7762e76.meta.json` | 388 | `not computed` | ledger |
| `R1262` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\1b\1bfd609dc4e60db44b6358e8e150c8f54c3e6f9204ae1fd0f55fc16d5253983f.meta.json` | 389 | `not computed` | ledger |
| `R1263` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\1c\1c03ccb6c23ca78bd1f2a264e7ae4548b6938e00c4ee5e2ba65bd082f34d4a9f.meta.json` | 393 | `not computed` | ledger |
| `R1264` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\1c\1c04fd6a22e408a52626a75abee81ad26008f41cb419bc784411274e979f7fa1.meta.json` | 391 | `not computed` | ledger |
| `R1265` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\1c\1c0a0d3b63b25bd8bdc18a04a1068a3434c5d49e3720468145233d18c44f5921.meta.json` | 359 | `not computed` | ledger |
| `R1266` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\1c\1c199b7da44bacb09e9f5ab40bdb596090299f63413d7da9da1d3985ce434ec1.meta.json` | 394 | `not computed` | ledger |
| `R1267` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\1c\1c1c92ad97cae677a27a58e9f6adbdb7b04f6a0f1c15fa80b83f278e02436778.meta.json` | 380 | `not computed` | ledger |
| `R1268` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\1c\1c29658017b7af33ffefed9bd6149411b136758cf4f08cacc5ce837318f77f67.meta.json` | 380 | `not computed` | ledger |
| `R1269` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\1c\1c2b45980dc584848de45e0997f105f7f7f47f6b91d40256934bfa97091d92c0.meta.json` | 392 | `not computed` | ledger |
| `R1270` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\1c\1c3ddee4fad88ed30e61008c5d3199960922930bd859cd5746e353e71852c558.meta.json` | 381 | `not computed` | ledger |
| `R1271` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\1c\1c3eafe00c2a0e1dd93647a01ebf1874fb2265cb09f58619761f814dc8599f3a.meta.json` | 398 | `not computed` | ledger |
| `R1272` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\1c\1c48d61dd403564eed45bfd3b846f5fc2e6a8bea5e270c3260154085fe3d312d.meta.json` | 379 | `not computed` | ledger |
| `R1273` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\1c\1c6392a90e874ae7da79f7dd8be4d4e053944a88b6814f2d6d4b6a2fe11172bb.meta.json` | 389 | `not computed` | ledger |
| `R1274` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\1c\1c63c1b84e824d34878ab08240c9250c692f6a6a0820baa94447cff4d261e3d2.meta.json` | 397 | `not computed` | ledger |
| `R1275` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\1c\1c665603a82beb81e0cef2878c9b44642ae6d519e301fbbd06326e03325febf3.meta.json` | 387 | `not computed` | ledger |
| `R1276` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\1c\1c6f2fb63f885089764c7c7b0648c6f4c42c09c0439027435f7b3c37a39f94e4.meta.json` | 388 | `not computed` | ledger |
| `R1277` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\1c\1c7183f5be4e1c2a843d74b1312e859fd251435d6a7ed394e8fd6041b04f1ab1.meta.json` | 396 | `not computed` | ledger |
| `R1278` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\1c\1c72b0713371e07c1a106b59c783a0f9ad75b6e991c30d426b4fede5a3153d49.meta.json` | 392 | `not computed` | ledger |
| `R1279` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\1c\1c9996b5ef84bac6ee2caf4036d30759bea6c48d728a53511e1f7146b0ec707a.meta.json` | 354 | `not computed` | ledger |
| `R1280` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\1c\1cbefd0acbfefb34c0b395e61b5c4fec58f0ef645396aa5a77107ac3e3a6a8df.meta.json` | 401 | `not computed` | ledger |
| `R1281` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\1c\1ce45ecb03760e1358793adef841ce0a0f6c37fdf25262b2208593bc49f08f55.meta.json` | 360 | `not computed` | ledger |
| `R1282` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\1c\1ce8239a0f736e3bab93ff44b99c3a49fd74601ed078b885f06fb6acf847e5b9.meta.json` | 396 | `not computed` | ledger |
| `R1283` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\1c\1ce91da459092d1536f74d2de5bed43fbd66b86d291f8247e46f16d2eb701297.meta.json` | 423 | `not computed` | ledger |
| `R1284` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\1c\1cee41be0a4a6a447299efb6cc84bdf7272888f21b106289542d770401dd5123.meta.json` | 386 | `not computed` | ledger |
| `R1285` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\1c\1cf78270a2faa2c64059a6fae74e9031a02a3ee80a5b8ea343f5a8f8e9b71f3a.meta.json` | 384 | `not computed` | ledger |
| `R1286` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\1d\1d0776225950d391f33e454b3174c5dae5f99a31108c3064c42a94254383a599.meta.json` | 394 | `not computed` | ledger |
| `R1287` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\1d\1d26afa203034698772107abfff1b53acbee30434700a4d2b75dee98951588f8.meta.json` | 388 | `not computed` | ledger |
| `R1288` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\1d\1d2722789936de4e0b935e2af2ef4211cdd9115390ea11aefc57960d1d93caef.meta.json` | 380 | `not computed` | ledger |
| `R1289` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\1d\1d30b2e3d0e7b4b232c213f0daa7b8bda62a28ee54d070cb8fa0aea17fd0e76c.meta.json` | 399 | `not computed` | ledger |
| `R1290` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\1d\1d45f429c326f5db0a362d757d36e233f876883b65f3248269573195a944ceaf.meta.json` | 372 | `not computed` | ledger |
| `R1291` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\1d\1d4b422c15dc1bb982e405f72ae25c0e31c3f4510f85e09c1f2a53e8fb52b306.meta.json` | 388 | `not computed` | ledger |
| `R1292` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\1d\1d4dc54a0f39a536e141ec4bd380408cc2601118bb74c1816efde5740df1f8e6.meta.json` | 363 | `not computed` | ledger |
| `R1293` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\1d\1d5ba8a1d605f4c65057c2f2af2fbe6c1dcaf46ce34b1594ad675f8a21720429.meta.json` | 426 | `not computed` | ledger |
| `R1294` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\1d\1d66713f90b66a331b1ebcaf01066c79f9557d0a06cec28e1f3286b0b0fcca74.meta.json` | 371 | `not computed` | ledger |
| `R1295` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\1d\1d73db002f8100c2c6679ae42a5900c542e643f8b9c1238970daac696f4fa9d9.meta.json` | 387 | `not computed` | ledger |
| `R1296` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\1d\1d787a5ff6f6b3bdce1c89c8665e95761091f5cb57f34750b186c59f0ed09580.meta.json` | 373 | `not computed` | ledger |
| `R1297` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\1d\1d836d2807ce98e9ca269b0383583a488923f563e153ffa2f25e5ed89281a46e.meta.json` | 381 | `not computed` | ledger |
| `R1298` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\1d\1d8f2caedde41f79483a8f5c6e1d5c434dbb122902b2f38b2a22735894cab36e.meta.json` | 379 | `not computed` | ledger |
| `R1299` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\1d\1d98c0f1cb5064656640e990144e1af713ab8109fb762425f392fba4d5042628.meta.json` | 382 | `not computed` | ledger |
| `R1300` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\1d\1db17c0382bf190d7e9546633303431e48254166f081d9de245650ab7f1be84c.meta.json` | 395 | `not computed` | policy, ledger |
| `R1301` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\1d\1dcee9f379962b980b20c969893ebc370bd8a72fe50ea222e062fb967e728209.meta.json` | 381 | `not computed` | ledger |
| `R1302` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\1d\1dcf85687cad60b3be1e6524c396409129414a172ffc6528b03d305b22e5fe18.meta.json` | 395 | `not computed` | ledger |
| `R1303` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\1d\1dde075570136774c706bf0009183a793fe0ee262e4a5590cc6eff8453eedd43.meta.json` | 396 | `not computed` | ledger |
| `R1304` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\1d\1ddf48bc2cafc0f4e110cf3b90b25e44a4e86bb3e81b143f0938bb856db95961.meta.json` | 387 | `not computed` | ledger |
| `R1305` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\1d\1dfea707470eadac84b3debea77a085c08069c5aaebf6d033b997ea36fd79efd.meta.json` | 392 | `not computed` | ledger |
| `R1306` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\1e\1e04ff12b64b8937dc782bf4cb6758a1eb2d0e92add8847ae8c1eef8b015a4d2.meta.json` | 376 | `not computed` | ledger |
| `R1307` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\1e\1e074be7e9078c8cd4f13bedae95f0e9a2e7e2779f4a7fe02628de71095439f6.meta.json` | 396 | `not computed` | ledger |
| `R1308` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\1e\1e1a3079307195e6f59e23ce53f71f433bd4c0ce0b8f1095b99656544cb7226c.meta.json` | 415 | `not computed` | ledger |
| `R1309` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\1e\1e42502d82babbcb6103a6a5301e2951e3013d7afa9a09eaa936265d288cd8f3.meta.json` | 392 | `not computed` | ledger |
| `R1310` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\1e\1e55821b7e5146bc72cee4d2e8b4d089907046198365699ea901fcacb5bac00f.meta.json` | 384 | `not computed` | ledger |
| `R1311` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\1e\1e607a68f931be6a38cdae438a384b6f90174b2bfa51b5a7c0e5284543416990.meta.json` | 381 | `not computed` | ledger |
| `R1312` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\1e\1e6ac8257f2c5914c76e087c33111acbff37564a8d5bfef4b3c68a3f965c608f.meta.json` | 372 | `not computed` | ledger |
| `R1313` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\1e\1e6b352a5fb035fdbb31fe65cf5ce3661b22d145287f01cd9e7f6a859bcbcb2c.meta.json` | 403 | `not computed` | ledger |
| `R1314` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\1e\1e7b2b6854f305a5100f3289597b1f3eff8f3e6806ca94a04afee800d69c92ab.meta.json` | 372 | `not computed` | ledger |
| `R1315` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\1e\1e85887b97891b0a6f6388a4a68271f82b2c1513ab546f7a366d25015ad0cdc9.meta.json` | 389 | `not computed` | ledger |
| `R1316` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\1e\1e8d3d6acd90febaccee269bd5e0d8fe954cf963f7beb2fc02e1abedd55e6944.meta.json` | 379 | `not computed` | ledger |
| `R1317` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\1e\1e8df33dc1c8084891cabaa94a6c9ffb46ea054126433e0f8596d290b79ccc24.meta.json` | 387 | `not computed` | ledger |
| `R1318` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\1e\1e94e9dfd4e3b8e712227c17bd7088e5e1194d789ea1989972e04671eacecf0e.meta.json` | 369 | `not computed` | ledger |
| `R1319` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\1e\1eaea4b7a8170608cd8ade614d358b03378234e2a807e374a46612a9e86b962f.meta.json` | 395 | `not computed` | ledger |
| `R1320` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\1e\1eb34ae148e947ebb8ded2c10b6bf02a27a2b025510521676880ca6acc301062.meta.json` | 388 | `not computed` | ledger |
| `R1321` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\1e\1eb45b32d4ca3a2cc63cc9f05f3022e3dd0288d7e22107b0af1605914c3b7592.meta.json` | 383 | `not computed` | ledger |
| `R1322` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\1e\1eb6d582f207dac0b28f82d16a12ff7b80e5dfd3bfff342092dec63445bbe3c9.meta.json` | 414 | `not computed` | ledger |
| `R1323` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\1e\1ec3ddf349ce6dbdcebf7fbbc8941b9c9af7cfd982cb3df43e39ff9e45a4318a.meta.json` | 382 | `not computed` | ledger |
| `R1324` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\1e\1ec46a3a02f54a7454844bb362fc303916c1003f2d2764f543472a72fa02b35d.meta.json` | 382 | `not computed` | ledger |
| `R1325` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\1e\1ecd311518266882ede8804686f758255d6dff89a71a646bb6970a69615e39f6.meta.json` | 400 | `not computed` | ledger |
| `R1326` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\1e\1ed62a6754f03e2a2bc58f381a033889874cd8a89acafbbcdfa227f1924f3d32.meta.json` | 387 | `not computed` | ledger |
| `R1327` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\1e\1ee04bb84c3490d129949f53c7148dafb84b8fe8f1f593466970bc88b9bf91ff.meta.json` | 399 | `not computed` | ledger |
| `R1328` | `C:\Users\ala\Documents\shploingus-game\references\ala-system\data\raw\source_local_filesystem\2026\09\1e\1ef1d5797b3bb74f78e899480bb8ccbc9186cce5eacf94c80f5dfed533901dad.meta.json` | 379 | `not computed` | ledger |
| `R1329` | `C:\Users\ala\Documents\shploingus\Cargo.toml` | 1994 | `not computed` | policy, ledger |
| `R1330` | `C:\Users\ala\Documents\shploingus\HANDOFF.md` | 19280 | `not computed` | cadence, policy, ledger |
| `R1331` | `C:\Users\ala\Documents\shploingus\.agents\skills\agent-browser\SKILL.md` | 6989 | `not computed` | policy |
| `R1332` | `C:\Users\ala\Documents\shploingus\.agents\skills\agent-browser\references\advanced-usage.md` | 5927 | `not computed` | policy |
| `R1333` | `C:\Users\ala\Documents\shploingus\.agents\skills\agent-browser\references\authentication.md` | 9255 | `not computed` | policy |
| `R1334` | `C:\Users\ala\Documents\shploingus\.agents\skills\agent-browser\references\commands.md` | 10088 | `not computed` | policy |
| `R1335` | `C:\Users\ala\Documents\shploingus\.agents\skills\agent-browser\references\profiling.md` | 3525 | `not computed` | policy |
| `R1336` | `C:\Users\ala\Documents\shploingus\.agents\skills\agent-browser\references\snapshot-refs.md` | 4499 | `not computed` | policy |
| `R1337` | `C:\Users\ala\Documents\shploingus\.agents\skills\agent-browser\templates\capture-workflow.sh` | 1901 | `not computed` | policy |
| `R1338` | `C:\Users\ala\Documents\shploingus\.agents\skills\agent-browser\templates\form-automation.sh` | 1900 | `not computed` | policy |
| `R1339` | `C:\Users\ala\Documents\shploingus\.agents\skills\agreement\host-contract.json` | 1517 | `not computed` | policy |
| `R1340` | `C:\Users\ala\Documents\shploingus\.agents\skills\agreement\SKILL.md` | 3876 | `not computed` | policy |
| `R1341` | `C:\Users\ala\Documents\shploingus\.agents\skills\ala-cities-task12-review-target\debug\.fingerprint\ala-cities-45ed9da29d539e31\bin-agent-ledger.json` | 1124 | `not computed` | ledger |
| `R1342` | `C:\Users\ala\Documents\shploingus\.agents\skills\ala-cities-task12-review-target\debug\.fingerprint\wgpu-2c2dd363a3ea0948\lib-wgpu.json` | 1816 | `not computed` | client |
| `R1343` | `C:\Users\ala\Documents\shploingus\.agents\skills\ala-cities-task12-review-target\debug\.fingerprint\wgpu-8a907c30a730fd8e\build-script-build-script-build.json` | 903 | `not computed` | client |
| `R1344` | `C:\Users\ala\Documents\shploingus\.agents\skills\ala-cities-task12-review-target\debug\.fingerprint\windows-c159f27af6ab93d4\lib-windows.json` | 21347 | `not computed` | policy |
| `R1345` | `C:\Users\ala\Documents\shploingus\.agents\skills\ala-cities-task12-review-target\debug\.fingerprint\windows-e28d308d26a8e859\lib-windows.json` | 21200 | `not computed` | policy |
| `R1346` | `C:\Users\ala\Documents\shploingus\.agents\skills\ala-cities-task12-review-target\debug\.fingerprint\windows-sys-2f9235758f433333\lib-windows_sys.json` | 8249 | `not computed` | policy |
| `R1347` | `C:\Users\ala\Documents\shploingus\.agents\skills\ala-cities-task12-review-target\debug\.fingerprint\windows-sys-f9ebeb0db5310db9\lib-windows_sys.json` | 8497 | `not computed` | policy |
| `R1348` | `C:\Users\ala\Documents\shploingus\.agents\skills\ask-matt\SKILL.md` | 11507 | `not computed` | health, policy |
| `R1349` | `C:\Users\ala\Documents\shploingus\.agents\skills\ask-matt\agents\openai.yaml` | 142 | `not computed` | policy |
| `R1350` | `C:\Users\ala\Documents\shploingus\.agents\skills\brainstorming\SKILL.md` | 17548 | `not computed` | health, policy |
| `R1351` | `C:\Users\ala\Documents\shploingus\.agents\skills\brainstorming\scripts\server.cjs` | 26416 | `not computed` | format, policy |
| `R1352` | `C:\Users\ala\Documents\shploingus\.agents\skills\brainstorming\scripts\stop-server.sh` | 3263 | `not computed` | policy |
| `R1353` | `C:\Users\ala\Documents\shploingus\.agents\skills\claude-handoff\agents\openai.yaml` | 146 | `not computed` | policy |
| `R1354` | `C:\Users\ala\Documents\shploingus\.agents\skills\code-refiner\SKILL.md` | 12813 | `not computed` | format |
| `R1355` | `C:\Users\ala\Documents\shploingus\.agents\skills\code-review\SKILL.md` | 6676 | `not computed` | policy |
| `R1356` | `C:\Users\ala\Documents\shploingus\.agents\skills\codebase-advisor\SKILL.md` | 9851 | `not computed` | policy |
| `R1357` | `C:\Users\ala\Documents\shploingus\.agents\skills\codebase-advisor\evals\cases.yaml` | 4200 | `not computed` | policy |
| `R1358` | `C:\Users\ala\Documents\shploingus\.agents\skills\codebase-advisor\references\closing-the-loop.md` | 4649 | `not computed` | policy |
| `R1359` | `C:\Users\ala\Documents\shploingus\.agents\skills\cook\SKILL.md` | 3964 | `not computed` | policy |
| `R1360` | `C:\Users\ala\Documents\shploingus\.agents\skills\csv-to-sif\host-contract.json` | 1766 | `not computed` | policy |
| `R1361` | `C:\Users\ala\Documents\shploingus\.agents\skills\csv-to-sif\SKILL.md` | 5599 | `not computed` | policy |
| `R1362` | `C:\Users\ala\Documents\shploingus\.agents\skills\decision-map\SKILL.md` | 11104 | `not computed` | health, policy |
| `R1363` | `C:\Users\ala\Documents\shploingus\.agents\skills\demographics-analysis\host-contract.json` | 1761 | `not computed` | policy |
| `R1364` | `C:\Users\ala\Documents\shploingus\.agents\skills\diagnose\SKILL.md` | 4801 | `not computed` | policy |
| `R1365` | `C:\Users\ala\Documents\shploingus\.agents\skills\diagnosing-bugs\SKILL.md` | 8667 | `not computed` | policy |
| `R1366` | `C:\Users\ala\Documents\shploingus\.agents\skills\diagnosing-superpowers\SKILL.md` | 6904 | `not computed` | policy |
| `R1367` | `C:\Users\ala\Documents\shploingus\.agents\skills\diagnosing-superpowers\prompts\scrub-audit.md` | 1363 | `not computed` | policy |
| `R1368` | `C:\Users\ala\Documents\shploingus\.agents\skills\diagnosing-superpowers\prompts\scrub.md` | 1471 | `not computed` | policy |
| `R1369` | `C:\Users\ala\Documents\shploingus\.agents\skills\diagnosing-superpowers\references\redaction-policy.md` | 2243 | `not computed` | policy |
| `R1370` | `C:\Users\ala\Documents\shploingus\.agents\skills\discuss\SKILL.md` | 5434 | `not computed` | policy |
| `R1371` | `C:\Users\ala\Documents\shploingus\.agents\skills\dispatching-parallel-agents\SKILL.md` | 6078 | `not computed` | policy |
| `R1372` | `C:\Users\ala\Documents\shploingus\.agents\skills\drawing-quantity-extract\host-contract.json` | 1224 | `not computed` | policy |
| `R1373` | `C:\Users\ala\Documents\shploingus\.agents\skills\drawing-quantity-extract\README.md` | 315 | `not computed` | ledger |
| `R1374` | `C:\Users\ala\Documents\shploingus\.agents\skills\drawing-quantity-extract\SKILL.md` | 4152 | `not computed` | ledger |
| `R1375` | `C:\Users\ala\Documents\shploingus\.agents\skills\environmental-analysis\host-contract.json` | 1778 | `not computed` | policy |
| `R1376` | `C:\Users\ala\Documents\shploingus\.agents\skills\epd-compare\host-contract.json` | 2410 | `not computed` | policy |
| `R1377` | `C:\Users\ala\Documents\shploingus\.agents\skills\epd-parser\host-contract.json` | 2645 | `not computed` | policy |
| `R1378` | `C:\Users\ala\Documents\shploingus\.agents\skills\epd-research\host-contract.json` | 2732 | `not computed` | policy |
| `R1379` | `C:\Users\ala\Documents\shploingus\.agents\skills\epd-to-spec\host-contract.json` | 2383 | `not computed` | policy |
| `R1380` | `C:\Users\ala\Documents\shploingus\.agents\skills\executing-plans\SKILL.md` | 20405 | `not computed` | policy, ledger |
| `R1381` | `C:\Users\ala\Documents\shploingus\.agents\skills\finishing-a-development-branch\SKILL.md` | 7781 | `not computed` | policy |
| `R1382` | `C:\Users\ala\Documents\shploingus\.agents\skills\fix\SKILL.md` | 4092 | `not computed` | policy |
| `R1383` | `C:\Users\ala\Documents\shploingus\.agents\skills\frontend-design\SKILL.md` | 8535 | `not computed` | health |
| `R1384` | `C:\Users\ala\Documents\shploingus\.agents\skills\frontend-design\references\design-system-generation.md` | 3895 | `not computed` | policy |
| `R1385` | `C:\Users\ala\Documents\shploingus\.agents\skills\frontend-design\scripts\search.py` | 13847 | `not computed` | health |
| `R1386` | `C:\Users\ala\Documents\shploingus\.agents\skills\frontend-design\scripts\tests\test_search.py` | 9295 | `not computed` | health |
| `R1387` | `C:\Users\ala\Documents\shploingus\.agents\skills\grill-me\agents\openai.yaml` | 142 | `not computed` | policy |
| `R1388` | `C:\Users\ala\Documents\shploingus\.agents\skills\grill-with-docs\agents\openai.yaml` | 150 | `not computed` | policy |
| `R1389` | `C:\Users\ala\Documents\shploingus\.agents\skills\handoff\agents\openai.yaml` | 146 | `not computed` | policy |
| `R1390` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-install-verify-target\debug\.fingerprint\hyperskill-diffusion-04dedf85c21c7cd7\test-integration-test-context_budget.json` | 632 | `not computed` | policy |
| `R1391` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\hypergrilling-ledger-chain-migration.json` | 3353 | `not computed` | ledger |
| `R1392` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\hypergrilling-report-aliases.json` | 1049 | `not computed` | ledger |
| `R1393` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\prototype-root.json` | 308 | `not computed` | ledger |
| `R1394` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\SKILL.md` | 21796 | `not computed` | policy, ledger |
| `R1395` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\benchmarks\update-and-load.json` | 1764 | `not computed` | policy, ledger |
| `R1396` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\docs\hyperskill-mantis-security-core-design.md` | 11588 | `not computed` | policy, ledger |
| `R1397` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\docs\superpowers\specs\2026-09-25-hyperskill-mantis-security-core-design.md` | 11588 | `not computed` | policy, ledger |
| `R1398` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\evidence\benchmark-final-integrity.json` | 2434 | `not computed` | policy, ledger |
| `R1399` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\evidence\benchmark-final.json` | 2132 | `not computed` | policy, ledger |
| `R1400` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\evidence\benchmark-gate-final-2.json` | 2230 | `not computed` | policy, ledger |
| `R1401` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\evidence\benchmark-gate-final-3.json` | 2230 | `not computed` | policy, ledger |
| `R1402` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\evidence\benchmark-gate-final.json` | 2132 | `not computed` | policy, ledger |
| `R1403` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\evidence\benchmark-mantis-final.json` | 2434 | `not computed` | policy, ledger |
| `R1404` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\evidence\build-final-integrity.json` | 4825 | `not computed` | policy, ledger |
| `R1405` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\evidence\build-final.json` | 4415 | `not computed` | policy, ledger |
| `R1406` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\evidence\build-gate-final-2.json` | 4723 | `not computed` | policy, ledger |
| `R1407` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\evidence\build-gate-final-3.json` | 4723 | `not computed` | policy, ledger |
| `R1408` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\evidence\build-gate-final.json` | 4625 | `not computed` | policy, ledger |
| `R1409` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\evidence\build-mantis-final.json` | 5250 | `not computed` | policy, ledger |
| `R1410` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\evidence\final-benchmark-4.json` | 2434 | `not computed` | policy, ledger |
| `R1411` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\evidence\final-benchmark-5.json` | 2434 | `not computed` | policy, ledger |
| `R1412` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\evidence\final-build-4.json` | 4825 | `not computed` | policy, ledger |
| `R1413` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\evidence\final-build-5.json` | 4825 | `not computed` | policy, ledger |
| `R1414` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\evidence\final-integrated-gates.json` | 4021 | `not computed` | policy, ledger |
| `R1415` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\evidence\final-standalone-4.json` | 317 | `not computed` | ledger |
| `R1416` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\evidence\final-standalone-5.json` | 317 | `not computed` | ledger |
| `R1417` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\evidence\mantis-build-coverage.ps1` | 12808 | `not computed` | policy, ledger |
| `R1418` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\evidence\mantis-dataset-inventory.json` | 53849 | `not computed` | policy, ledger |
| `R1419` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\evidence\mantis-dataset-scope.json` | 4235 | `not computed` | policy |
| `R1420` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\evidence\mantis-security-report.json` | 575 | `not computed` | ledger |
| `R1421` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\evidence\public-smoke-final.json` | 601 | `not computed` | ledger |
| `R1422` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\evidence\standalone-final.json` | 317 | `not computed` | ledger |
| `R1423` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\evidence\standalone-gate-final-2.json` | 317 | `not computed` | ledger |
| `R1424` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\evidence\standalone-gate-final-3.json` | 317 | `not computed` | ledger |
| `R1425` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\evidence\standalone-gate-final.json` | 317 | `not computed` | ledger |
| `R1426` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\evidence\verify-generated-mantis-final.json` | 245 | `not computed` | ledger |
| `R1427` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\evidence\verify-staged-mantis-final.json` | 248 | `not computed` | ledger |
| `R1428` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\evidence\mantis-diagrams\trust-boundary-manifest.json` | 1018 | `not computed` | ledger |
| `R1429` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\evidence\mantis-stage-evidence\pipeline-adapter.md` | 426 | `not computed` | ledger |
| `R1430` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\evidence\mantis-stage-evidence\reflect.md` | 394 | `not computed` | ledger |
| `R1431` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\evidence\mantis-stage-evidence\review.md` | 499 | `not computed` | policy |
| `R1432` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\evidence\mantis-stage-evidence\threat-model.md` | 501 | `not computed` | ledger |
| `R1433` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\evidence\public-smoke\SKILL.md` | 21796 | `not computed` | policy, ledger |
| `R1434` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\manifest.json` | 4782 | `not computed` | policy, ledger |
| `R1435` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\public-manifest.json` | 5029 | `not computed` | policy, ledger |
| `R1436` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\public-staging.json` | 1069 | `not computed` | ledger |
| `R1437` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\SKILL.candidate.md` | 21796 | `not computed` | policy, ledger |
| `R1438` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\SKILL.md` | 21796 | `not computed` | policy, ledger |
| `R1439` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\tree.json` | 58046 | `not computed` | policy, ledger |
| `R1440` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\00133e2b227a5a75fabfa0e94d31c489c79153dbb5acd857a1ffc3d39baf476f-1.md` | 16710 | `not computed` | policy, ledger |
| `R1441` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\00133e2b227a5a75fabfa0e94d31c489c79153dbb5acd857a1ffc3d39baf476f-2.md` | 16710 | `not computed` | policy, ledger |
| `R1442` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\00133e2b227a5a75fabfa0e94d31c489c79153dbb5acd857a1ffc3d39baf476f-3.md` | 16710 | `not computed` | policy, ledger |
| `R1443` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\00133e2b227a5a75fabfa0e94d31c489c79153dbb5acd857a1ffc3d39baf476f-4.md` | 16710 | `not computed` | policy, ledger |
| `R1444` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\00133e2b227a5a75fabfa0e94d31c489c79153dbb5acd857a1ffc3d39baf476f-5.md` | 16710 | `not computed` | policy, ledger |
| `R1445` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\00133e2b227a5a75fabfa0e94d31c489c79153dbb5acd857a1ffc3d39baf476f.md` | 16710 | `not computed` | policy, ledger |
| `R1446` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\0b9e6b13101d90db3cc3f6da5c600fcf15e3958e83314d3fbe602ba987bebb31-1.md` | 9813 | `not computed` | policy, ledger |
| `R1447` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\0b9e6b13101d90db3cc3f6da5c600fcf15e3958e83314d3fbe602ba987bebb31.md` | 9813 | `not computed` | policy, ledger |
| `R1448` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\11754e0fc1f613f49433301d4b1621a83a63898ca57111a20a6c4703e9c89246-1.md` | 21796 | `not computed` | policy, ledger |
| `R1449` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\11754e0fc1f613f49433301d4b1621a83a63898ca57111a20a6c4703e9c89246-2.md` | 21796 | `not computed` | policy, ledger |
| `R1450` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\11754e0fc1f613f49433301d4b1621a83a63898ca57111a20a6c4703e9c89246.md` | 21796 | `not computed` | policy, ledger |
| `R1451` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\154bbab4f24c2f4fb8586bcb9010610a09f9e8c0152d8e1ac92f39d090590e86-1.md` | 10012 | `not computed` | policy, ledger |
| `R1452` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\154bbab4f24c2f4fb8586bcb9010610a09f9e8c0152d8e1ac92f39d090590e86.md` | 10012 | `not computed` | policy, ledger |
| `R1453` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\2506862580e8486ffbedeecc3114f4d48c461793d271b5316f24c6be3195d97b-1.md` | 17825 | `not computed` | policy, ledger |
| `R1454` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\2506862580e8486ffbedeecc3114f4d48c461793d271b5316f24c6be3195d97b-2.md` | 17825 | `not computed` | policy, ledger |
| `R1455` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\2506862580e8486ffbedeecc3114f4d48c461793d271b5316f24c6be3195d97b-3.md` | 17825 | `not computed` | policy, ledger |
| `R1456` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\2506862580e8486ffbedeecc3114f4d48c461793d271b5316f24c6be3195d97b-4.md` | 17825 | `not computed` | policy, ledger |
| `R1457` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\2506862580e8486ffbedeecc3114f4d48c461793d271b5316f24c6be3195d97b-5.md` | 17825 | `not computed` | policy, ledger |
| `R1458` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\2506862580e8486ffbedeecc3114f4d48c461793d271b5316f24c6be3195d97b.md` | 17825 | `not computed` | policy, ledger |
| `R1459` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\29b3759394c7a20ca8219ffeeca5309f2892448d5f3449945ae5a4c15bd2d4ca-1.md` | 21796 | `not computed` | policy, ledger |
| `R1460` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\29b3759394c7a20ca8219ffeeca5309f2892448d5f3449945ae5a4c15bd2d4ca-2.md` | 21796 | `not computed` | policy, ledger |
| `R1461` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\29b3759394c7a20ca8219ffeeca5309f2892448d5f3449945ae5a4c15bd2d4ca.md` | 21796 | `not computed` | policy, ledger |
| `R1462` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\45cb5be0f1428491015b1ec1152fe944689a59e97850d38f10c55640b7fe774b-1.md` | 21796 | `not computed` | policy, ledger |
| `R1463` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\45cb5be0f1428491015b1ec1152fe944689a59e97850d38f10c55640b7fe774b-2.md` | 21796 | `not computed` | policy, ledger |
| `R1464` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\45cb5be0f1428491015b1ec1152fe944689a59e97850d38f10c55640b7fe774b-3.md` | 21796 | `not computed` | policy, ledger |
| `R1465` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\45cb5be0f1428491015b1ec1152fe944689a59e97850d38f10c55640b7fe774b-4.md` | 21796 | `not computed` | policy, ledger |
| `R1466` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\45cb5be0f1428491015b1ec1152fe944689a59e97850d38f10c55640b7fe774b.md` | 21796 | `not computed` | policy, ledger |
| `R1467` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\51bfa8e08647dd1155e95b0b596c37e7bfb0ab195580898cbe0817ee44026e64-1.md` | 21796 | `not computed` | policy, ledger |
| `R1468` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\51bfa8e08647dd1155e95b0b596c37e7bfb0ab195580898cbe0817ee44026e64.md` | 21796 | `not computed` | policy, ledger |
| `R1469` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\5880027b87cc3f0d68ca8536ef25105ee1c1aea1e34dffd59cd7c02d97db6678-1.md` | 21796 | `not computed` | policy, ledger |
| `R1470` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\5880027b87cc3f0d68ca8536ef25105ee1c1aea1e34dffd59cd7c02d97db6678.md` | 21796 | `not computed` | policy, ledger |
| `R1471` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\5fbb102a31017bdf78750335f553458a1f578d27fc9e4a2ac2245540a33b987c-1.md` | 21796 | `not computed` | policy, ledger |
| `R1472` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\5fbb102a31017bdf78750335f553458a1f578d27fc9e4a2ac2245540a33b987c-2.md` | 21796 | `not computed` | policy, ledger |
| `R1473` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\5fbb102a31017bdf78750335f553458a1f578d27fc9e4a2ac2245540a33b987c.md` | 21796 | `not computed` | policy, ledger |
| `R1474` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\664c6949921337f7cccb65329491dbc9f23357049f8241a80b85c3c89d4d1027-1.md` | 21796 | `not computed` | policy, ledger |
| `R1475` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\664c6949921337f7cccb65329491dbc9f23357049f8241a80b85c3c89d4d1027.md` | 21796 | `not computed` | policy, ledger |
| `R1476` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\6712148f754d523589a41293b8a614ca4506ef72da444216a50c8a303efe71d8-1.md` | 16613 | `not computed` | policy, ledger |
| `R1477` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\6712148f754d523589a41293b8a614ca4506ef72da444216a50c8a303efe71d8.md` | 16613 | `not computed` | policy, ledger |
| `R1478` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\6b3c72ad8f8eb714c24e69323c3738a0420346343e894de5077d12bc7f948187.md` | 17920 | `not computed` | policy, ledger |
| `R1479` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\887bb8e91ff9aa2daf805bbc9ca04aedcf65ad77077879ccea5ae2a19d3139ab-1.md` | 21796 | `not computed` | policy, ledger |
| `R1480` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\887bb8e91ff9aa2daf805bbc9ca04aedcf65ad77077879ccea5ae2a19d3139ab-2.md` | 21796 | `not computed` | policy, ledger |
| `R1481` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\887bb8e91ff9aa2daf805bbc9ca04aedcf65ad77077879ccea5ae2a19d3139ab-3.md` | 21796 | `not computed` | policy, ledger |
| `R1482` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\887bb8e91ff9aa2daf805bbc9ca04aedcf65ad77077879ccea5ae2a19d3139ab.md` | 21796 | `not computed` | policy, ledger |
| `R1483` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\8deb3e747e3aa71a9db41ea937882db7b6b66a46197ea334e4c1f0d9d740aa5b-1.md` | 10012 | `not computed` | policy, ledger |
| `R1484` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\8deb3e747e3aa71a9db41ea937882db7b6b66a46197ea334e4c1f0d9d740aa5b.md` | 10012 | `not computed` | policy, ledger |
| `R1485` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\9f8d62cc61ab6a9e6d0174cc8f9bab4b19c712540bc0d6f960cf783fb98f1296-1.md` | 17920 | `not computed` | policy, ledger |
| `R1486` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\9f8d62cc61ab6a9e6d0174cc8f9bab4b19c712540bc0d6f960cf783fb98f1296-2.md` | 17920 | `not computed` | policy, ledger |
| `R1487` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\9f8d62cc61ab6a9e6d0174cc8f9bab4b19c712540bc0d6f960cf783fb98f1296.md` | 17920 | `not computed` | policy, ledger |
| `R1488` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\aef74424051a75cfd77e5c9e78caa5efd4fa0ac33f54ee5727486db2c245d305-1.md` | 17720 | `not computed` | policy, ledger |
| `R1489` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\aef74424051a75cfd77e5c9e78caa5efd4fa0ac33f54ee5727486db2c245d305-2.md` | 17720 | `not computed` | policy, ledger |
| `R1490` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\aef74424051a75cfd77e5c9e78caa5efd4fa0ac33f54ee5727486db2c245d305.md` | 17720 | `not computed` | policy, ledger |
| `R1491` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\b88a6721828f06ad747df1b05045d68c45e85832427bee4bc3d72ecb424dc0da-1.md` | 21796 | `not computed` | policy, ledger |
| `R1492` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\b88a6721828f06ad747df1b05045d68c45e85832427bee4bc3d72ecb424dc0da-2.md` | 21796 | `not computed` | policy, ledger |
| `R1493` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\b88a6721828f06ad747df1b05045d68c45e85832427bee4bc3d72ecb424dc0da.md` | 21796 | `not computed` | policy, ledger |
| `R1494` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\b95fa414fd43b2cbdaf8dfc65e1f7169588b57cada480e8fcfbed67a106e29ea-1.md` | 21796 | `not computed` | policy, ledger |
| `R1495` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\b95fa414fd43b2cbdaf8dfc65e1f7169588b57cada480e8fcfbed67a106e29ea-2.md` | 21796 | `not computed` | policy, ledger |
| `R1496` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\b95fa414fd43b2cbdaf8dfc65e1f7169588b57cada480e8fcfbed67a106e29ea.md` | 21796 | `not computed` | policy, ledger |
| `R1497` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\c7593a8df3e43872e60672d60856511e768656a84c301cb758b143e5e5d53148-1.md` | 21796 | `not computed` | policy, ledger |
| `R1498` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\c7593a8df3e43872e60672d60856511e768656a84c301cb758b143e5e5d53148-2.md` | 21796 | `not computed` | policy, ledger |
| `R1499` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\c7593a8df3e43872e60672d60856511e768656a84c301cb758b143e5e5d53148-3.md` | 21796 | `not computed` | policy, ledger |
| `R1500` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\c7593a8df3e43872e60672d60856511e768656a84c301cb758b143e5e5d53148-4.md` | 21796 | `not computed` | policy, ledger |
| `R1501` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\c7593a8df3e43872e60672d60856511e768656a84c301cb758b143e5e5d53148-5.md` | 21796 | `not computed` | policy, ledger |
| `R1502` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\c7593a8df3e43872e60672d60856511e768656a84c301cb758b143e5e5d53148.md` | 21796 | `not computed` | policy, ledger |
| `R1503` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\cae3e59dd18874565824cf9416ca781022008cc041ca48bd6d1a397aec7f208a-1.md` | 9813 | `not computed` | policy, ledger |
| `R1504` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\cae3e59dd18874565824cf9416ca781022008cc041ca48bd6d1a397aec7f208a.md` | 9813 | `not computed` | policy, ledger |
| `R1505` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\d0a0b1b586e08ca85fcaa28607b0d5cf86d1ad3ff6e418246768b1faedd6e220-1.md` | 21796 | `not computed` | policy, ledger |
| `R1506` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\d0a0b1b586e08ca85fcaa28607b0d5cf86d1ad3ff6e418246768b1faedd6e220-2.md` | 21796 | `not computed` | policy, ledger |
| `R1507` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\d0a0b1b586e08ca85fcaa28607b0d5cf86d1ad3ff6e418246768b1faedd6e220.md` | 21796 | `not computed` | policy, ledger |
| `R1508` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\d17ee2b226c3e698baba88eb276728987fd0428ac724d32c321eb5d535729a73-1.md` | 21796 | `not computed` | policy, ledger |
| `R1509` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\d17ee2b226c3e698baba88eb276728987fd0428ac724d32c321eb5d535729a73-2.md` | 21796 | `not computed` | policy, ledger |
| `R1510` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\d17ee2b226c3e698baba88eb276728987fd0428ac724d32c321eb5d535729a73.md` | 21796 | `not computed` | policy, ledger |
| `R1511` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\d210e9da152fbf5c31ae52a9f92ec61f4bf9a24e3debcefeecc9a9959680ac66-1.md` | 17920 | `not computed` | policy, ledger |
| `R1512` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\d210e9da152fbf5c31ae52a9f92ec61f4bf9a24e3debcefeecc9a9959680ac66-2.md` | 17920 | `not computed` | policy, ledger |
| `R1513` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\d210e9da152fbf5c31ae52a9f92ec61f4bf9a24e3debcefeecc9a9959680ac66.md` | 17920 | `not computed` | policy, ledger |
| `R1514` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\d2b2613af359409fe8876195943ba621868882fee12fb1465eae7f66e8d75595-1.md` | 17920 | `not computed` | policy, ledger |
| `R1515` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\d2b2613af359409fe8876195943ba621868882fee12fb1465eae7f66e8d75595.md` | 17920 | `not computed` | policy, ledger |
| `R1516` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\d2c37a10f54af4d6d38495dbecbef7d6b943f862e1340ed4fd5a81dd83648a66-1.md` | 17920 | `not computed` | policy, ledger |
| `R1517` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\d2c37a10f54af4d6d38495dbecbef7d6b943f862e1340ed4fd5a81dd83648a66-2.md` | 17920 | `not computed` | policy, ledger |
| `R1518` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\d2c37a10f54af4d6d38495dbecbef7d6b943f862e1340ed4fd5a81dd83648a66.md` | 17920 | `not computed` | policy, ledger |
| `R1519` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\d575432c44731aceea986d4f624a9588d681c0921d8f87689eb7a91db000b64e-1.md` | 8221 | `not computed` | policy, ledger |
| `R1520` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\d575432c44731aceea986d4f624a9588d681c0921d8f87689eb7a91db000b64e-2.md` | 8221 | `not computed` | policy, ledger |
| `R1521` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\d575432c44731aceea986d4f624a9588d681c0921d8f87689eb7a91db000b64e.md` | 8221 | `not computed` | policy, ledger |
| `R1522` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\f2bdacb6f10900475bf46ed38e80b70ee4e4099eed507662f456ba16f2c691bf-1.md` | 21796 | `not computed` | policy, ledger |
| `R1523` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\f2bdacb6f10900475bf46ed38e80b70ee4e4099eed507662f456ba16f2c691bf-2.md` | 21796 | `not computed` | policy, ledger |
| `R1524` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\f2bdacb6f10900475bf46ed38e80b70ee4e4099eed507662f456ba16f2c691bf-3.md` | 21796 | `not computed` | policy, ledger |
| `R1525` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\f2bdacb6f10900475bf46ed38e80b70ee4e4099eed507662f456ba16f2c691bf-4.md` | 21796 | `not computed` | policy, ledger |
| `R1526` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\f2bdacb6f10900475bf46ed38e80b70ee4e4099eed507662f456ba16f2c691bf-5.md` | 21796 | `not computed` | policy, ledger |
| `R1527` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\f2bdacb6f10900475bf46ed38e80b70ee4e4099eed507662f456ba16f2c691bf.md` | 21796 | `not computed` | policy, ledger |
| `R1528` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\f7890dd0b358f4fcfda7683b892dda9993b2872a7cd6c8e6faf294f29d0aff83.md` | 7914 | `not computed` | policy, ledger |
| `R1529` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\security-remediation-pre-boundary\manifest.json` | 4623 | `not computed` | policy, ledger |
| `R1530` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\security-remediation-pre-boundary\public-manifest.json` | 4617 | `not computed` | policy, ledger |
| `R1531` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\security-remediation-pre-boundary\public-staging.json` | 672 | `not computed` | ledger |
| `R1532` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\security-remediation-pre-boundary\SKILL.candidate.md` | 21796 | `not computed` | policy, ledger |
| `R1533` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\security-remediation-pre-boundary\SKILL.md` | 21796 | `not computed` | policy, ledger |
| `R1534` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\security-remediation-pre-boundary\tree.json` | 58046 | `not computed` | policy, ledger |
| `R1535` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\security-remediation-pre-boundary\public-candidate\SKILL.md` | 21796 | `not computed` | policy, ledger |
| `R1536` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\security-remediation-pre-boundary-root-sync\public-staging.json` | 672 | `not computed` | ledger |
| `R1537` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\security-remediation-pre-boundary-root-sync\public-candidate\SKILL.md` | 21796 | `not computed` | policy, ledger |
| `R1538` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\security-remediation-pre-current-evidence\manifest.json` | 4378 | `not computed` | policy, ledger |
| `R1539` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\security-remediation-pre-current-evidence\public-manifest.json` | 4615 | `not computed` | policy, ledger |
| `R1540` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\security-remediation-pre-current-evidence\public-staging.json` | 672 | `not computed` | ledger |
| `R1541` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\security-remediation-pre-current-evidence\SKILL.candidate.md` | 21796 | `not computed` | policy, ledger |
| `R1542` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\security-remediation-pre-current-evidence\SKILL.md` | 21796 | `not computed` | policy, ledger |
| `R1543` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\security-remediation-pre-current-evidence\tree.json` | 58046 | `not computed` | policy, ledger |
| `R1544` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\security-remediation-pre-current-evidence\public-candidate\SKILL.md` | 21796 | `not computed` | policy, ledger |
| `R1545` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\security-remediation-pre-derived\manifest.json` | 4378 | `not computed` | policy, ledger |
| `R1546` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\security-remediation-pre-derived\public-manifest.json` | 4617 | `not computed` | policy, ledger |
| `R1547` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\security-remediation-pre-derived\public-staging.json` | 672 | `not computed` | ledger |
| `R1548` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\security-remediation-pre-derived\SKILL.candidate.md` | 21796 | `not computed` | policy, ledger |
| `R1549` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\security-remediation-pre-derived\SKILL.md` | 21796 | `not computed` | policy, ledger |
| `R1550` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\security-remediation-pre-derived\tree.json` | 58046 | `not computed` | policy, ledger |
| `R1551` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\security-remediation-pre-derived\public-candidate\SKILL.md` | 21796 | `not computed` | policy, ledger |
| `R1552` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\security-remediation-pre-event-0027-final\manifest.json` | 4775 | `not computed` | policy, ledger |
| `R1553` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\security-remediation-pre-event-0027-final\public-manifest.json` | 5012 | `not computed` | policy, ledger |
| `R1554` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\security-remediation-pre-event-0027-final\public-staging.json` | 1069 | `not computed` | ledger |
| `R1555` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\security-remediation-pre-event-0027-final\SKILL.candidate.md` | 21796 | `not computed` | policy, ledger |
| `R1556` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\security-remediation-pre-event-0027-final\SKILL.md` | 21796 | `not computed` | policy, ledger |
| `R1557` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\security-remediation-pre-event-0027-final\tree.json` | 58046 | `not computed` | policy, ledger |
| `R1558` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\security-remediation-pre-event-0027-final\public-candidate\SKILL.md` | 21796 | `not computed` | policy, ledger |
| `R1559` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\security-remediation-pre-final-evidence\manifest.json` | 4775 | `not computed` | policy, ledger |
| `R1560` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\security-remediation-pre-final-evidence\public-manifest.json` | 5014 | `not computed` | policy, ledger |
| `R1561` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\security-remediation-pre-final-evidence\public-staging.json` | 1069 | `not computed` | ledger |
| `R1562` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\security-remediation-pre-final-evidence\SKILL.candidate.md` | 21796 | `not computed` | policy, ledger |
| `R1563` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\security-remediation-pre-final-evidence\SKILL.md` | 21796 | `not computed` | policy, ledger |
| `R1564` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\security-remediation-pre-final-evidence\tree.json` | 58046 | `not computed` | policy, ledger |
| `R1565` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\security-remediation-pre-final-evidence\public-candidate\SKILL.md` | 21796 | `not computed` | policy, ledger |
| `R1566` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\security-remediation-pre-final-gate\manifest.json` | 4775 | `not computed` | policy, ledger |
| `R1567` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\security-remediation-pre-final-gate\public-manifest.json` | 5014 | `not computed` | policy, ledger |
| `R1568` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\security-remediation-pre-final-gate\public-staging.json` | 1069 | `not computed` | ledger |
| `R1569` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\security-remediation-pre-final-gate\SKILL.candidate.md` | 21796 | `not computed` | policy, ledger |
| `R1570` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\security-remediation-pre-final-gate\SKILL.md` | 21796 | `not computed` | policy, ledger |
| `R1571` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\security-remediation-pre-final-gate\tree.json` | 58046 | `not computed` | policy, ledger |
| `R1572` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\security-remediation-pre-final-gate\public-candidate\SKILL.md` | 21796 | `not computed` | policy, ledger |
| `R1573` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\security-remediation-pre-final-gate-r9\manifest.json` | 4782 | `not computed` | policy, ledger |
| `R1574` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\security-remediation-pre-final-gate-r9\public-manifest.json` | 5029 | `not computed` | policy, ledger |
| `R1575` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\security-remediation-pre-final-gate-r9\public-staging.json` | 1069 | `not computed` | ledger |
| `R1576` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\security-remediation-pre-final-gate-r9\SKILL.candidate.md` | 21796 | `not computed` | policy, ledger |
| `R1577` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\security-remediation-pre-final-gate-r9\SKILL.md` | 21796 | `not computed` | policy, ledger |
| `R1578` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\security-remediation-pre-final-gate-r9\tree.json` | 58046 | `not computed` | policy, ledger |
| `R1579` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\security-remediation-pre-final-gate-r9\public-candidate\SKILL.md` | 21796 | `not computed` | policy, ledger |
| `R1580` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\security-remediation-pre-final-verified\manifest.json` | 4782 | `not computed` | policy, ledger |
| `R1581` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\security-remediation-pre-final-verified\public-manifest.json` | 5029 | `not computed` | policy, ledger |
| `R1582` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\security-remediation-pre-final-verified\public-staging.json` | 1069 | `not computed` | ledger |
| `R1583` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\security-remediation-pre-final-verified\SKILL.candidate.md` | 21796 | `not computed` | policy, ledger |
| `R1584` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\security-remediation-pre-final-verified\SKILL.md` | 21796 | `not computed` | policy, ledger |
| `R1585` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\security-remediation-pre-final-verified\tree.json` | 58046 | `not computed` | policy, ledger |
| `R1586` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\security-remediation-pre-final-verified\public-candidate\SKILL.md` | 21796 | `not computed` | policy, ledger |
| `R1587` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\security-remediation-pre-formatted-evidence-final\manifest.json` | 4775 | `not computed` | policy, ledger |
| `R1588` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\security-remediation-pre-formatted-evidence-final\public-manifest.json` | 5012 | `not computed` | policy, ledger |
| `R1589` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\security-remediation-pre-formatted-evidence-final\public-staging.json` | 1069 | `not computed` | ledger |
| `R1590` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\security-remediation-pre-formatted-evidence-final\SKILL.candidate.md` | 21796 | `not computed` | policy, ledger |
| `R1591` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\security-remediation-pre-formatted-evidence-final\SKILL.md` | 21796 | `not computed` | policy, ledger |
| `R1592` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\security-remediation-pre-formatted-evidence-final\tree.json` | 58046 | `not computed` | policy, ledger |
| `R1593` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\security-remediation-pre-formatted-evidence-final\public-candidate\SKILL.md` | 21796 | `not computed` | policy, ledger |
| `R1594` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\security-remediation-pre-formatted-final\manifest.json` | 4775 | `not computed` | policy, ledger |
| `R1595` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\security-remediation-pre-formatted-final\public-manifest.json` | 5014 | `not computed` | policy, ledger |
| `R1596` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\security-remediation-pre-formatted-final\public-staging.json` | 1069 | `not computed` | ledger |
| `R1597` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\security-remediation-pre-formatted-final\SKILL.candidate.md` | 21796 | `not computed` | policy, ledger |
| `R1598` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\security-remediation-pre-formatted-final\SKILL.md` | 21796 | `not computed` | policy, ledger |
| `R1599` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\security-remediation-pre-formatted-final\tree.json` | 58046 | `not computed` | policy, ledger |
| `R1600` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\security-remediation-pre-formatted-final\public-candidate\SKILL.md` | 21796 | `not computed` | policy, ledger |
| `R1601` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\security-remediation-pre-freshness\manifest.json` | 4623 | `not computed` | policy, ledger |
| `R1602` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\security-remediation-pre-freshness\public-manifest.json` | 4617 | `not computed` | policy, ledger |
| `R1603` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\security-remediation-pre-freshness\public-staging.json` | 672 | `not computed` | ledger |
| `R1604` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\security-remediation-pre-freshness\SKILL.candidate.md` | 21796 | `not computed` | policy, ledger |
| `R1605` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\security-remediation-pre-freshness\SKILL.md` | 21796 | `not computed` | policy, ledger |
| `R1606` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\security-remediation-pre-freshness\tree.json` | 58046 | `not computed` | policy, ledger |
| `R1607` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\security-remediation-pre-freshness\public-candidate\SKILL.md` | 21796 | `not computed` | policy, ledger |
| `R1608` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\security-remediation-pre-gate-log-binding\manifest.json` | 4775 | `not computed` | policy, ledger |
| `R1609` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\security-remediation-pre-gate-log-binding\public-manifest.json` | 5014 | `not computed` | policy, ledger |
| `R1610` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\security-remediation-pre-gate-log-binding\public-staging.json` | 1069 | `not computed` | ledger |
| `R1611` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\security-remediation-pre-gate-log-binding\SKILL.candidate.md` | 21796 | `not computed` | policy, ledger |
| `R1612` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\security-remediation-pre-gate-log-binding\SKILL.md` | 21796 | `not computed` | policy, ledger |
| `R1613` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\security-remediation-pre-gate-log-binding\tree.json` | 58046 | `not computed` | policy, ledger |
| `R1614` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\security-remediation-pre-gate-log-binding\public-candidate\SKILL.md` | 21796 | `not computed` | policy, ledger |
| `R1615` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\security-remediation-pre-gate-log-final\manifest.json` | 4775 | `not computed` | policy, ledger |
| `R1616` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\security-remediation-pre-gate-log-final\public-manifest.json` | 5014 | `not computed` | policy, ledger |
| `R1617` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\security-remediation-pre-gate-log-final\public-staging.json` | 1069 | `not computed` | ledger |
| `R1618` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\security-remediation-pre-gate-log-final\SKILL.candidate.md` | 21796 | `not computed` | policy, ledger |
| `R1619` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\security-remediation-pre-gate-log-final\SKILL.md` | 21796 | `not computed` | policy, ledger |
| `R1620` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\security-remediation-pre-gate-log-final\tree.json` | 58046 | `not computed` | policy, ledger |
| `R1621` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\security-remediation-pre-gate-log-final\public-candidate\SKILL.md` | 21796 | `not computed` | policy, ledger |
| `R1622` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\security-remediation-pre-gate-provenance\manifest.json` | 4775 | `not computed` | policy, ledger |
| `R1623` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\security-remediation-pre-gate-provenance\public-manifest.json` | 5012 | `not computed` | policy, ledger |
| `R1624` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\security-remediation-pre-gate-provenance\public-staging.json` | 1069 | `not computed` | ledger |
| `R1625` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\security-remediation-pre-gate-provenance\SKILL.candidate.md` | 21796 | `not computed` | policy, ledger |
| `R1626` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\security-remediation-pre-gate-provenance\SKILL.md` | 21796 | `not computed` | policy, ledger |
| `R1627` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\security-remediation-pre-gate-provenance\tree.json` | 58046 | `not computed` | policy, ledger |
| `R1628` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\security-remediation-pre-gate-provenance\public-candidate\SKILL.md` | 21796 | `not computed` | policy, ledger |
| `R1629` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\security-remediation-pre-mantis\manifest.json` | 4358 | `not computed` | policy, ledger |
| `R1630` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\security-remediation-pre-mantis\public-manifest.json` | 4352 | `not computed` | policy, ledger |
| `R1631` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\security-remediation-pre-mantis\public-staging.json` | 407 | `not computed` | ledger |
| `R1632` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\security-remediation-pre-mantis\SKILL.candidate.md` | 21796 | `not computed` | policy, ledger |
| `R1633` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\security-remediation-pre-mantis\SKILL.md` | 21796 | `not computed` | policy, ledger |
| `R1634` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\security-remediation-pre-mantis\tree.json` | 56771 | `not computed` | policy, ledger |
| `R1635` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\security-remediation-pre-mantis\public-candidate\SKILL.md` | 21796 | `not computed` | policy, ledger |
| `R1636` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\security-remediation-pre-r5-final-gate\manifest.json` | 4782 | `not computed` | policy, ledger |
| `R1637` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\security-remediation-pre-r5-final-gate\public-manifest.json` | 5027 | `not computed` | policy, ledger |
| `R1638` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\security-remediation-pre-r5-final-gate\public-staging.json` | 1069 | `not computed` | ledger |
| `R1639` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\security-remediation-pre-r5-final-gate\SKILL.candidate.md` | 21796 | `not computed` | policy, ledger |
| `R1640` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\security-remediation-pre-r5-final-gate\SKILL.md` | 21796 | `not computed` | policy, ledger |
| `R1641` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\security-remediation-pre-r5-final-gate\tree.json` | 58046 | `not computed` | policy, ledger |
| `R1642` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\security-remediation-pre-r5-final-gate\public-candidate\SKILL.md` | 21796 | `not computed` | policy, ledger |
| `R1643` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\security-remediation-pre-r5-provisional\manifest.json` | 4775 | `not computed` | policy, ledger |
| `R1644` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\security-remediation-pre-r5-provisional\public-manifest.json` | 5014 | `not computed` | policy, ledger |
| `R1645` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\security-remediation-pre-r5-provisional\public-staging.json` | 1069 | `not computed` | ledger |
| `R1646` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\security-remediation-pre-r5-provisional\SKILL.candidate.md` | 21796 | `not computed` | policy, ledger |
| `R1647` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\security-remediation-pre-r5-provisional\SKILL.md` | 21796 | `not computed` | policy, ledger |
| `R1648` | `C:\Users\ala\Documents\shploingus\.agents\skills\hyperskill-semantic-diffusion-prototype\generated\history\security-remediation-pre-r5-provisional\tree.json` | 58046 | `not computed` | policy, ledger |
| `R1649` | `C:\Users\ala\Documents\openlock\AGENTS.md` | 1623 | `not computed` | witness, policy |
| `R1650` | `C:\Users\ala\Documents\openlock\deploy.ps1` | 2210 | `not computed` | policy, ledger |
| `R1651` | `C:\Users\ala\Documents\openlock\install.ps1` | 81939 | `not computed` | cadence, format, policy, ledger |
| `R1652` | `C:\Users\ala\Documents\openlock\launch.ps1` | 22890 | `not computed` | witness, policy |
| `R1653` | `C:\Users\ala\Documents\openlock\README.md` | 23181 | `not computed` | witness, format, policy, ledger |
| `R1654` | `C:\Users\ala\Documents\openlock\.reference\docs\docs\features\commands.md` | 6100 | `not computed` | health, policy |
| `R1655` | `C:\Users\ala\Documents\openlock\.reference\docs\docs\features\damage.md` | 3304 | `not computed` | health |
| `R1656` | `C:\Users\ala\Documents\openlock\.reference\docs\docs\features\entities.md` | 3495 | `not computed` | cadence, health |
| `R1657` | `C:\Users\ala\Documents\openlock\.reference\docs\docs\features\modifiers.md` | 2916 | `not computed` | health |
| `R1658` | `C:\Users\ala\Documents\openlock\.reference\docs\docs\features\permissions.md` | 2667 | `not computed` | health |
| `R1659` | `C:\Users\ala\Documents\openlock\.reference\docs\docs\features\players.md` | 5350 | `not computed` | health |
| `R1660` | `C:\Users\ala\Documents\openlock\.reference\docs\docs\features\server.md` | 4446 | `not computed` | cadence |
| `R1661` | `C:\Users\ala\Documents\openlock\.reference\docs\docs\features\timers.md` | 2647 | `not computed` | cadence |
| `R1662` | `C:\Users\ala\Documents\openlock\.reference\docs\docs\getting-started\developers\first-plugin.md` | 3051 | `not computed` | health |
| `R1663` | `C:\Users\ala\Documents\openlock\.reference\docs\docs\getting-started\server-admins\run-a-server-docker.md` | 7395 | `not computed` | health |
| `R1664` | `C:\Users\ala\Documents\openlock\.reference\docs\docs\guides\admins-and-permissions.md` | 7956 | `not computed` | policy |
| `R1665` | `C:\Users\ala\Documents\openlock\.reference\docs\docs\guides\content-discovery.md` | 20943 | `not computed` | policy, ledger |
| `R1666` | `C:\Users\ala\Documents\openlock\.reference\docs\docs\guides\uploading-content.md` | 4564 | `not computed` | policy |
| `R1667` | `C:\Users\ala\Documents\openlock\.reference\docs\scripts\gen-api.ts` | 16646 | `not computed` | policy |
| `R1668` | `C:\Users\ala\Documents\openlock\.scratch\boot-csdk10.keep.js` | 4665 | `not computed` | policy |
| `R1669` | `C:\Users\ala\Documents\openlock\.scratch\boot-current.js` | 5154 | `not computed` | policy |
| `R1670` | `C:\Users\ala\Documents\openlock\.scratch\boot-noprobe.js` | 4665 | `not computed` | policy |
| `R1671` | `C:\Users\ala\Documents\openlock\.scratch\browser-check.json` | 7693 | `not computed` | witness, policy |
| `R1672` | `C:\Users\ala\Documents\openlock\.scratch\browser-shell-check.json` | 8945 | `not computed` | witness, policy |
| `R1673` | `C:\Users\ala\Documents\openlock\.scratch\build_delivery_proof.py` | 3979 | `not computed` | ledger |
| `R1674` | `C:\Users\ala\Documents\openlock\.scratch\cap-hidden.ps1` | 3597 | `not computed` | policy |
| `R1675` | `C:\Users\ala\Documents\openlock\.scratch\dashboard-block.js` | 26803 | `not computed` | policy |
| `R1676` | `C:\Users\ala\Documents\openlock\.scratch\dialog-text.ps1` | 1509 | `not computed` | policy |
| `R1677` | `C:\Users\ala\Documents\openlock\.scratch\ignore-assert.ps1` | 2023 | `not computed` | policy |
| `R1678` | `C:\Users\ala\Documents\openlock\.scratch\install-no-trap.ps1` | 51649 | `not computed` | format, policy, ledger |
| `R1679` | `C:\Users\ala\Documents\openlock\.scratch\landing-detect.json` | 69193 | `not computed` | witness, policy |
| `R1680` | `C:\Users\ala\Documents\openlock\.scratch\landing-detect4.json` | 2099 | `not computed` | cadence |
| `R1681` | `C:\Users\ala\Documents\openlock\.scratch\list-windows.ps1` | 1289 | `not computed` | policy |
| `R1682` | `C:\Users\ala\Documents\openlock\.scratch\parity-after.json` | 4357 | `not computed` | witness, policy, ledger |
| `R1683` | `C:\Users\ala\Documents\openlock\.scratch\parity-before.json` | 5090 | `not computed` | witness, policy, ledger |
| `R1684` | `C:\Users\ala\Documents\openlock\.scratch\parity-csdk10-final.json` | 4396 | `not computed` | witness, policy, ledger |
| `R1685` | `C:\Users\ala\Documents\openlock\.scratch\parity-csdk10-final2.json` | 4431 | `not computed` | witness, policy, ledger |
| `R1686` | `C:\Users\ala\Documents\openlock\.scratch\parity-csdk10.json` | 4698 | `not computed` | witness, policy, ledger |
| `R1687` | `C:\Users\ala\Documents\openlock\.scratch\parity-current.json` | 7595 | `not computed` | witness, policy, ledger |
| `R1688` | `C:\Users\ala\Documents\openlock\.scratch\parity-ddrive.json` | 7594 | `not computed` | witness, policy, ledger |
| `R1689` | `C:\Users\ala\Documents\openlock\.scratch\parity-final.json` | 4621 | `not computed` | witness, policy, ledger |
| `R1690` | `C:\Users\ala\Documents\openlock\.scratch\parity-old.json` | 5379 | `not computed` | witness, policy, ledger |
| `R1691` | `C:\Users\ala\Documents\openlock\.scratch\parity-steam-final.json` | 4824 | `not computed` | witness, policy, ledger |
| `R1692` | `C:\Users\ala\Documents\openlock\.scratch\parity-steam-final2.json` | 4859 | `not computed` | witness, policy, ledger |
| `R1693` | `C:\Users\ala\Documents\openlock\.scratch\parity-steam.json` | 4824 | `not computed` | witness, policy, ledger |
| `R1694` | `C:\Users\ala\Documents\openlock\.scratch\parity.json` | 5412 | `not computed` | witness, policy, ledger |
| `R1695` | `C:\Users\ala\Documents\openlock\.scratch\shell_data_check.js` | 323061 | `not computed` | health, policy, ledger |
| `R1696` | `C:\Users\ala\Documents\openlock\.scratch\vconsole.py` | 2370 | `not computed` | format |
| `R1697` | `C:\Users\ala\Documents\openlock\.scratch\wish_probe.js` | 479296 | `not computed` | health, policy, ledger |
| `R1698` | `C:\Users\ala\Documents\openlock\.scratch\dw\panorama\scripts\dw_bootstrap.js` | 98731 | `not computed` | cadence, health, policy |
| `R1699` | `C:\Users\ala\Documents\openlock\.scratch\edge-profile\Default\Extensions\ghbmnnjooekpmoecnnnilnnbdlolhkhi\1.111.1_0\manifest.json` | 2526 | `not computed` | policy |
| `R1700` | `C:\Users\ala\Documents\openlock\.scratch\edge-profile\Default\Extensions\ghbmnnjooekpmoecnnnilnnbdlolhkhi\1.111.1_0\offscreendocument_main.js` | 134684 | `not computed` | policy |
| `R1701` | `C:\Users\ala\Documents\openlock\.scratch\installed\panorama\scripts\openlock_shell.js` | 216574 | `not computed` | cadence, health, policy |
| `R1702` | `C:\Users\ala\Documents\openlock\.scratch\installed-check\panorama\scripts\openlock_shell_data.js` | 322471 | `not computed` | health, policy, ledger |
| `R1703` | `C:\Users\ala\Documents\openlock\.scratch\livecheck-new\panorama\scripts\openlock_boot.js` | 3754 | `not computed` | policy |
| `R1704` | `C:\Users\ala\Documents\openlock\.scratch\livecheck-new\panorama\scripts\openlock_server_mount.js` | 2815 | `not computed` | policy |
| `R1705` | `C:\Users\ala\Documents\openlock\.scratch\livecheck-new\panorama\scripts\openlock_shell.js` | 216574 | `not computed` | cadence, health, policy |
| `R1706` | `C:\Users\ala\Documents\openlock\.scratch\livecheck-new\panorama\scripts\openlock_shell_data.js` | 348919 | `not computed` | health, policy, ledger |
| `R1707` | `C:\Users\ala\Documents\openlock\.scratch\proof-build\panorama\scripts\openlock_audio.js` | 2170 | `not computed` | policy |
| `R1708` | `C:\Users\ala\Documents\openlock\.scratch\proof-build\panorama\scripts\openlock_boot.js` | 3754 | `not computed` | policy |
| `R1709` | `C:\Users\ala\Documents\openlock\.scratch\proof-build\panorama\scripts\openlock_boot_csdk10.js` | 6021 | `not computed` | policy |
| `R1710` | `C:\Users\ala\Documents\openlock\.scratch\proof-build\panorama\scripts\openlock_server_mount.js` | 2815 | `not computed` | policy |
| `R1711` | `C:\Users\ala\Documents\openlock\.scratch\proof-build\panorama\scripts\openlock_shell.js` | 263160 | `not computed` | cadence, health, policy |
| `R1712` | `C:\Users\ala\Documents\openlock\.scratch\proof-build\panorama\scripts\openlock_shell_data.js` | 456986 | `not computed` | health, policy, ledger |
| `R1713` | `C:\Users\ala\Documents\secure-shell\AGENTS.md` | 15540 | `not computed` | witness, format, mount, policy, ledger |
| `R1714` | `C:\Users\ala\Documents\secure-shell\README.md` | 2975 | `not computed` | witness, policy, ledger |
| `R1715` | `C:\Users\ala\Documents\secure-shell\.scratch\decisions-rows.md` | 4197 | `not computed` | format, policy, ledger |
| `R1716` | `C:\Users\ala\Documents\secure-shell\.scratch\ingest\ingest-probe.admission.json` | 925 | `not computed` | witness, ledger |
| `R1717` | `C:\Users\ala\Documents\secure-shell\baselines\axis.baseline.json` | 959 | `not computed` | policy, ledger |
| `R1718` | `C:\Users\ala\Documents\secure-shell\deploy\install-debian.sh` | 1861 | `not computed` | policy |
| `R1719` | `C:\Users\ala\Documents\secure-shell\docs\ARCHITECTURE.md` | 8765 | `not computed` | witness, mount, policy, ledger |
| `R1720` | `C:\Users\ala\Documents\secure-shell\docs\DECISIONS.md` | 23073 | `not computed` | witness, civilians, cadence, format, mount, client, policy, ledger |
| `R1721` | `C:\Users\ala\Documents\secure-shell\docs\FIRST-TEN-HOURS.md` | 10757 | `not computed` | witness, civilians, mount, client, policy, ledger |
| `R1722` | `C:\Users\ala\Documents\secure-shell\docs\FORMAT-SOURCES-AUDIT.md` | 85859 | `not computed` | witness, civilians, cadence, format, mount, client, policy, ledger |
| `R1723` | `C:\Users\ala\Documents\secure-shell\docs\GRADES.md` | 10434 | `not computed` | civilians, policy, ledger |
| `R1724` | `C:\Users\ala\Documents\secure-shell\docs\LEDGER.md` | 10348 | `not computed` | witness, health, mount, policy, ledger |
| `R1725` | `C:\Users\ala\Documents\secure-shell\docs\MOTION.md` | 3746 | `not computed` | witness, policy |
| `R1726` | `C:\Users\ala\Documents\secure-shell\docs\PLAN.md` | 14095 | `not computed` | witness, civilians, mount, policy, ledger |
| `R1727` | `C:\Users\ala\Documents\secure-shell\docs\PROOF-OF-WORK.md` | 10118 | `not computed` | witness, civilians, cadence, policy, ledger |
| `R1728` | `C:\Users\ala\Documents\secure-shell\docs\secure-shell-streamer-first-package-unification.md` | 61337 | `not computed` | witness, cadence, health, mount, policy, ledger |
| `R1729` | `C:\Users\ala\Documents\secure-shell\docs\SELECTIONS.md` | 20464 | `not computed` | witness, cadence, mount, policy, ledger |
| `R1730` | `C:\Users\ala\Documents\secure-shell\packages\axis\axis.data.json` | 5148 | `not computed` | policy, ledger |
| `R1731` | `C:\Users\ala\Documents\secure-shell\packages\axis\axis.meta.json` | 5974 | `not computed` | civilians, cadence, policy |
| `R1732` | `C:\Users\ala\Documents\secure-shell\patches\PATCH-001-axis-lane-and-ledger.md` | 636 | `not computed` | witness, policy, ledger |
| `R1733` | `C:\Users\ala\Documents\secure-shell\patches\PATCH-002-ingest-frame.md` | 3498 | `not computed` | witness, format, policy, ledger |
| `R1734` | `C:\Users\ala\Documents\secure-shell\patches\PATCH-003-plan-and-drift-gate.md` | 3987 | `not computed` | witness, policy, ledger |
| `R1735` | `C:\Users\ala\Documents\secure-shell\patches\PATCH-004-five-star-axis.md` | 8193 | `not computed` | witness, civilians, cadence, policy, ledger |
| `R1736` | `C:\Users\ala\Documents\secure-shell\server\axis-driver.mjs` | 7031 | `not computed` | witness, civilians, policy, ledger |
| `R1737` | `C:\Users\ala\Documents\secure-shell\server\axis-server.mjs` | 4794 | `not computed` | witness, civilians, policy, ledger |
| `R1738` | `C:\Users\ala\Documents\secure-shell\server\axis.mjs` | 9397 | `not computed` | witness, civilians, policy, ledger |
| `R1739` | `C:\Users\ala\Documents\secure-shell\server\decl.mjs` | 9591 | `not computed` | witness, civilians, policy, ledger |
| `R1740` | `C:\Users\ala\Documents\secure-shell\server\http.mjs` | 8325 | `not computed` | health, policy, ledger |
| `R1741` | `C:\Users\ala\Documents\secure-shell\server\ingest.mjs` | 10341 | `not computed` | witness, format, policy, ledger |
| `R1742` | `C:\Users\ala\Documents\secure-shell\server\ledger.mjs` | 25709 | `not computed` | mount, policy, ledger |
| `R1743` | `C:\Users\ala\Documents\secure-shell\server\shell.mjs` | 7971 | `not computed` | witness, mount, policy, ledger |
| `R1744` | `C:\Users\ala\Documents\secure-shell\server\watch.mjs` | 8302 | `not computed` | ledger |
| `R1745` | `C:\Users\ala\Documents\secure-shell\server\test\axis-driver.test.mjs` | 4692 | `not computed` | witness, policy, ledger |
| `R1746` | `C:\Users\ala\Documents\secure-shell\server\test\axis-server.test.mjs` | 4167 | `not computed` | witness, civilians, policy, ledger |
| `R1747` | `C:\Users\ala\Documents\secure-shell\server\test\axis.test.mjs` | 5459 | `not computed` | witness, civilians, policy, ledger |
| `R1748` | `C:\Users\ala\Documents\secure-shell\server\test\http.test.mjs` | 5360 | `not computed` | health, ledger |
| `R1749` | `C:\Users\ala\Documents\secure-shell\server\test\ingest.test.mjs` | 10281 | `not computed` | witness, format, policy, ledger |
| `R1750` | `C:\Users\ala\Documents\secure-shell\server\test\ledger.test.mjs` | 7700 | `not computed` | policy, ledger |
| `R1751` | `C:\Users\ala\Documents\secure-shell\server\test\served-route.test.mjs` | 3710 | `not computed` | witness, policy, ledger |
| `R1752` | `C:\Users\ala\Documents\secure-shell\server\test\watch.test.mjs` | 3741 | `not computed` | ledger |
| `R1753` | `C:\Users\ala\Documents\secure-shell\shell\openlock\panorama\scripts\openlock_audio.js` | 2170 | `not computed` | policy |
| `R1754` | `C:\Users\ala\Documents\secure-shell\shell\openlock\panorama\scripts\openlock_delivery.js` | 26244 | `not computed` | cadence, policy |
| `R1755` | `C:\Users\ala\Documents\secure-shell\shell\openlock\panorama\scripts\openlock_layout.js` | 12190 | `not computed` | cadence, policy |
| `R1756` | `C:\Users\ala\Documents\secure-shell\shell\openlock\panorama\scripts\openlock_popit.js` | 22093 | `not computed` | policy |
| `R1757` | `C:\Users\ala\Documents\secure-shell\shell\openlock\panorama\scripts\openlock_shell.js` | 364412 | `not computed` | witness, cadence, health, policy |
| `R1758` | `C:\Users\ala\Documents\secure-shell\shell\openlock\panorama\scripts\openlock_shell_data.js` | 482057 | `not computed` | health, policy, ledger |
| `R1759` | `C:\Users\ala\Documents\secure-shell\shell\openlock\panorama\scripts\openlock_split.js` | 6659 | `not computed` | policy |
| `R1760` | `C:\Users\ala\Documents\secure-shell\shell\openlock\panorama\scripts\secure_shell_rounds.js` | 5522 | `not computed` | policy |
| `R1761` | `C:\Users\ala\Documents\secure-shell\shell\openlock\panorama\scripts\secure_shell_stream.js` | 6218 | `not computed` | policy, ledger |
| `R1762` | `C:\Users\ala\Documents\secure-shell\tests\civilians.test.mjs` | 5403 | `not computed` | civilians, cadence, policy, ledger |
| `R1763` | `C:\Users\ala\Documents\secure-shell\tests\drift_gate.test.mjs` | 7296 | `not computed` | witness, policy, ledger |
| `R1764` | `C:\Users\ala\Documents\secure-shell\tests\rounds.test.mjs` | 4051 | `not computed` | witness, civilians, policy |
| `R1765` | `C:\Users\ala\Documents\secure-shell\tests\served.test.mjs` | 5003 | `not computed` | policy, ledger |
| `R1766` | `C:\Users\ala\Documents\secure-shell\tests\star.test.mjs` | 12244 | `not computed` | civilians, policy, ledger |
| `R1767` | `C:\Users\ala\Documents\secure-shell\tests\stream.test.mjs` | 3944 | `not computed` | witness, policy, ledger |
| `R1768` | `C:\Users\ala\Documents\secure-shell\tools\axis-port.mjs` | 10931 | `not computed` | policy, ledger |
| `R1769` | `C:\Users\ala\Documents\secure-shell\tools\browser_shell_check.py` | 10225 | `not computed` | witness, policy |
| `R1770` | `C:\Users\ala\Documents\secure-shell\tools\drift_gate.mjs` | 18756 | `not computed` | witness, civilians, policy, ledger |
| `R1771` | `C:\Users\ala\Documents\secure-shell\tools\ingest-cli.mjs` | 10742 | `not computed` | witness, policy, ledger |
| `R1772` | `C:\Users\ala\Documents\secure-shell\tools\ledger-cli.mjs` | 10178 | `not computed` | ledger |
| `R1773` | `C:\Users\ala\Documents\secure-shell\tools\secure_shell_surface.py` | 25837 | `not computed` | witness, policy |
| `R1774` | `C:\Users\ala\Documents\secure-shell\tools\port\civilians.mjs` | 8474 | `not computed` | witness, civilians, cadence, policy, ledger |
| `R1775` | `C:\Users\ala\Documents\secure-shell\tools\port\mount.mjs` | 13177 | `not computed` | policy, ledger |
| `R1776` | `C:\Users\ala\Documents\secure-shell\tools\port\patch.mjs` | 11363 | `not computed` | policy, ledger |
| `R1777` | `C:\Users\ala\Documents\secure-shell\tools\port\served.mjs` | 10433 | `not computed` | mount, policy, ledger |
| `R1778` | `C:\Users\ala\Documents\secure-shell\tools\port\shell-record.mjs` | 5579 | `not computed` | witness, policy, ledger |
| `R1779` | `C:\Users\ala\Documents\secure-shell\tools\port\star.mjs` | 20012 | `not computed` | witness, civilians, cadence, policy, ledger |
| `R1780` | `C:\Users\ala\Documents\secure-shell\tools\port\store.mjs` | 9294 | `not computed` | mount, policy, ledger |
| `R1781` | `C:\Users\ala\Documents\secure-shell\tools\port\surface.mjs` | 15755 | `not computed` | policy, ledger |
| `R1782` | `C:\Users\ala\Documents\secure-shell\var\fork-boundary-issue.md` | 2959 | `not computed` | witness, policy, ledger |
| `R1783` | `C:\Users\ala\Documents\secure-shell\var\gate.json` | 1850 | `not computed` | witness, policy, ledger |
| `R1784` | `C:\Users\ala\Documents\dl-enclave\AGENTS.md` | 5217 | `not computed` | witness, policy |
| `R1785` | `C:\Users\ala\Documents\dl-enclave\README.md` | 12156 | `not computed` | witness, civilians, mount, policy |
| `R1786` | `C:\Users\ala\Documents\dl-enclave\client\README.md` | 343 | `not computed` | witness |
| `R1787` | `C:\Users\ala\Documents\dl-enclave\clientaddon\dashboard\README.md` | 3701 | `not computed` | mount, policy, ledger |
| `R1788` | `C:\Users\ala\Documents\dl-enclave\docs\APPEARANCE.md` | 9493 | `not computed` | policy |
| `R1789` | `C:\Users\ala\Documents\dl-enclave\docs\BOUNDARIES.md` | 38579 | `not computed` | witness, civilians, cadence, mount, policy, ledger |
| `R1790` | `C:\Users\ala\Documents\dl-enclave\docs\CLIENT-UI.md` | 45827 | `not computed` | witness, civilians, policy, ledger |
| `R1791` | `C:\Users\ala\Documents\dl-enclave\docs\COVERAGE.md` | 21990 | `not computed` | witness, civilians, client, policy, ledger |
| `R1792` | `C:\Users\ala\Documents\dl-enclave\docs\DRIFT.md` | 25560 | `not computed` | witness, health, format, policy, ledger |
| `R1793` | `C:\Users\ala\Documents\dl-enclave\docs\INTERACTION.md` | 17495 | `not computed` | witness, policy |
| `R1794` | `C:\Users\ala\Documents\dl-enclave\docs\INVENTORY.md` | 40336 | `not computed` | witness, civilians, cadence, format, client, policy, ledger |
| `R1795` | `C:\Users\ala\Documents\dl-enclave\docs\MCP-SURFACE.md` | 24426 | `not computed` | witness, civilians, mount, policy, ledger |
| `R1796` | `C:\Users\ala\Documents\dl-enclave\docs\PACKAGE-FORMAT.md` | 59008 | `not computed` | witness, cadence, format, mount, policy, ledger |
| `R1797` | `C:\Users\ala\Documents\dl-enclave\docs\PLAN.md` | 26707 | `not computed` | witness, civilians, mount, policy, ledger |
| `R1798` | `C:\Users\ala\Documents\dl-enclave\docs\baselines\alpha-shell-port.json` | 1777 | `not computed` | policy, ledger |
| `R1799` | `C:\Users\ala\Documents\dl-enclave\docs\baselines\README.md` | 1425 | `not computed` | policy |
| `R1800` | `C:\Users\ala\Documents\dl-enclave\docs\fixtures\alpha-shell-loss.md` | 13965 | `not computed` | policy, ledger |
| `R1801` | `C:\Users\ala\Documents\dl-enclave\docs\fixtures\motd-loss.md` | 4214 | `not computed` | policy, ledger |
| `R1802` | `C:\Users\ala\Documents\dl-enclave\docs\research\2026-10-30-cml-and-sml-feasibility.md` | 10660 | `not computed` | cadence, policy |
| `R1803` | `C:\Users\ala\Documents\dl-enclave\docs\research\2026-10-30-hardened-linux-appliance.md` | 13421 | `not computed` | witness, health, policy, ledger |
| `R1804` | `C:\Users\ala\Documents\dl-enclave\docs\research\2026-10-30-project-census.md` | 16950 | `not computed` | witness, civilians, cadence, client, policy, ledger |
| `R1805` | `C:\Users\ala\Documents\dl-enclave\docs\research\2026-10-30-supply-chain-and-package-format.md` | 12536 | `not computed` | witness, policy, ledger |
| `R1806` | `C:\Users\ala\Documents\dl-enclave\enclave\README.md` | 756 | `not computed` | witness |
| `R1807` | `C:\Users\ala\Documents\dl-enclave\image\README.md` | 483 | `not computed` | policy |
| `R1808` | `C:\Users\ala\Documents\dl-enclave\patches\PATCH-001-the-shell-port-generator.md` | 3087 | `not computed` | policy |
| `R1809` | `C:\Users\ala\Documents\dl-enclave\patches\PATCH-002-the-mount-host.md` | 6233 | `not computed` | mount, policy, ledger |
| `R1810` | `C:\Users\ala\Documents\dl-enclave\patches\PATCH-003-the-session-and-client.md` | 6312 | `not computed` | policy |
| `R1811` | `C:\Users\ala\Documents\dl-enclave\patches\PATCH-004-the-black-pod-frame.md` | 6255 | `not computed` | policy, ledger |
| `R1812` | `C:\Users\ala\Documents\dl-enclave\patches\PATCH-005-the-input-model.md` | 7641 | `not computed` | policy, ledger |
| `R1813` | `C:\Users\ala\Documents\dl-enclave\patches\PATCH-006-the-move-and-resize-gesture.md` | 5567 | `not computed` | policy, ledger |
| `R1814` | `C:\Users\ala\Documents\dl-enclave\patches\PATCH-007-the-desktop-display.md` | 6374 | `not computed` | witness, policy |
| `R1815` | `C:\Users\ala\Documents\dl-enclave\patches\PATCH-008-the-debian-display-witness.md` | 9153 | `not computed` | witness, policy |
| `R1816` | `C:\Users\ala\Documents\dl-enclave\patches\PATCH-009-the-client-desktop-start.md` | 13125 | `not computed` | witness, policy, ledger |
| `R1817` | `C:\Users\ala\Documents\dl-enclave\patches\PATCH-010-the-painted-press.md` | 12031 | `not computed` | witness, policy, ledger |
| `R1818` | `C:\Users\ala\Documents\dl-enclave\patches\PATCH-011-the-work-area.md` | 12426 | `not computed` | witness, policy, ledger |
| `R1819` | `C:\Users\ala\Documents\dl-enclave\patches\PATCH-012-the-shell-regions.md` | 10708 | `not computed` | witness, policy, ledger |
| `R1820` | `C:\Users\ala\Documents\dl-enclave\patches\PATCH-013-the-addon-store.md` | 8703 | `not computed` | witness, format, mount, policy, ledger |
| `R1821` | `C:\Users\ala\Documents\dl-enclave\patches\PATCH-014-the-openlock-motd-addon.md` | 12614 | `not computed` | witness, policy, ledger |
| `R1822` | `C:\Users\ala\Documents\dl-enclave\schema\README.md` | 789 | `not computed` | witness, civilians, policy |
| `R1823` | `C:\Users\ala\Documents\dl-enclave\tools\project_surface.py` | 36864 | `not computed` | policy, ledger |
| `R1824` | `C:\Users\ala\Documents\dl-enclave\tools\README.md` | 3807 | `not computed` | mount, policy |
| `R1825` | `C:\Users\ala\Documents\dl-enclave\tools\surface_receiver.py` | 17613 | `not computed` | witness, mount, policy, ledger |
| `R1826` | `C:\Users\ala\Documents\dl-enclave\tools\port\package.json` | 871 | `not computed` | policy |
| `R1827` | `C:\Users\ala\Documents\dl-enclave\tools\port\README.md` | 21305 | `not computed` | witness, mount, policy |
| `R1828` | `C:\Users\ala\Documents\dl-enclave\tools\port\looks\README.md` | 3969 | `not computed` | policy |
| `R1829` | `C:\Users\ala\Documents\dl-enclave\tools\port\native\src\audio.rs` | 6180 | `not computed` | cadence, policy |
| `R1830` | `C:\Users\ala\Documents\dl-enclave\tools\port\src\addon-package.mjs` | 16227 | `not computed` | format, policy, ledger |
| `R1831` | `C:\Users\ala\Documents\dl-enclave\tools\port\src\addon-store.mjs` | 10472 | `not computed` | policy, ledger |
| `R1832` | `C:\Users\ala\Documents\dl-enclave\tools\port\src\addon.mjs` | 9763 | `not computed` | policy, ledger |
| `R1833` | `C:\Users\ala\Documents\dl-enclave\tools\port\src\appearance.mjs` | 8415 | `not computed` | policy |
| `R1834` | `C:\Users\ala\Documents\dl-enclave\tools\port\src\client.mjs` | 18070 | `not computed` | witness, mount, policy, ledger |
| `R1835` | `C:\Users\ala\Documents\dl-enclave\tools\port\src\display-host.mjs` | 11052 | `not computed` | cadence, policy |
| `R1836` | `C:\Users\ala\Documents\dl-enclave\tools\port\src\display.mjs` | 22964 | `not computed` | policy, ledger |
| `R1837` | `C:\Users\ala\Documents\dl-enclave\tools\port\src\frame.mjs` | 13442 | `not computed` | policy |
| `R1838` | `C:\Users\ala\Documents\dl-enclave\tools\port\src\generate.mjs` | 8805 | `not computed` | policy, ledger |
| `R1839` | `C:\Users\ala\Documents\dl-enclave\tools\port\src\interaction.mjs` | 39633 | `not computed` | policy |
| `R1840` | `C:\Users\ala\Documents\dl-enclave\tools\port\src\look.mjs` | 13924 | `not computed` | policy, ledger |
| `R1841` | `C:\Users\ala\Documents\dl-enclave\tools\port\src\motd.mjs` | 15180 | `not computed` | policy, ledger |
| `R1842` | `C:\Users\ala\Documents\dl-enclave\tools\port\src\mount.mjs` | 13177 | `not computed` | policy, ledger |
| `R1843` | `C:\Users\ala\Documents\dl-enclave\tools\port\src\openlock.mjs` | 18073 | `not computed` | policy, ledger |
| `R1844` | `C:\Users\ala\Documents\dl-enclave\tools\port\src\patch.mjs` | 11363 | `not computed` | policy, ledger |
| `R1845` | `C:\Users\ala\Documents\dl-enclave\tools\port\src\placement.mjs` | 9779 | `not computed` | policy |
| `R1846` | `C:\Users\ala\Documents\dl-enclave\tools\port\src\presenter.mjs` | 6152 | `not computed` | policy |
| `R1847` | `C:\Users\ala\Documents\dl-enclave\tools\port\src\renderer.mjs` | 10885 | `not computed` | ledger |
| `R1848` | `C:\Users\ala\Documents\dl-enclave\tools\port\src\run.mjs` | 15209 | `not computed` | witness, cadence, mount, policy, ledger |
| `R1849` | `C:\Users\ala\Documents\dl-enclave\tools\port\src\scene.mjs` | 27482 | `not computed` | policy, ledger |
| `R1850` | `C:\Users\ala\Documents\dl-enclave\tools\port\src\service.mjs` | 7874 | `not computed` | policy, ledger |
| `R1851` | `C:\Users\ala\Documents\dl-enclave\tools\port\src\session.mjs` | 14869 | `not computed` | witness, policy |
| `R1852` | `C:\Users\ala\Documents\dl-enclave\tools\port\src\shell-record.mjs` | 5579 | `not computed` | witness, policy, ledger |
| `R1853` | `C:\Users\ala\Documents\dl-enclave\tools\port\src\store.mjs` | 9294 | `not computed` | mount, policy, ledger |
| `R1854` | `C:\Users\ala\Documents\dl-enclave\tools\port\src\surface.mjs` | 15755 | `not computed` | policy, ledger |
| `R1855` | `C:\Users\ala\Documents\dl-enclave\tools\port\test\addon-package.test.mjs` | 3711 | `not computed` | policy, ledger |
| `R1856` | `C:\Users\ala\Documents\dl-enclave\tools\port\test\addon-store.test.mjs` | 6496 | `not computed` | policy, ledger |
| `R1857` | `C:\Users\ala\Documents\dl-enclave\tools\port\test\appearance.test.mjs` | 5987 | `not computed` | policy |
| `R1858` | `C:\Users\ala\Documents\dl-enclave\tools\port\test\client.test.mjs` | 9978 | `not computed` | policy, ledger |
| `R1859` | `C:\Users\ala\Documents\dl-enclave\tools\port\test\display.test.mjs` | 6453 | `not computed` | policy |
| `R1860` | `C:\Users\ala\Documents\dl-enclave\tools\port\test\frame.test.mjs` | 10111 | `not computed` | policy, ledger |
| `R1861` | `C:\Users\ala\Documents\dl-enclave\tools\port\test\generate.test.mjs` | 2674 | `not computed` | policy, ledger |
| `R1862` | `C:\Users\ala\Documents\dl-enclave\tools\port\test\interaction.test.mjs` | 26300 | `not computed` | policy |
| `R1863` | `C:\Users\ala\Documents\dl-enclave\tools\port\test\landing.test.mjs` | 4565 | `not computed` | ledger |
| `R1864` | `C:\Users\ala\Documents\dl-enclave\tools\port\test\look.test.mjs` | 6627 | `not computed` | policy, ledger |
| `R1865` | `C:\Users\ala\Documents\dl-enclave\tools\port\test\motd.test.mjs` | 6211 | `not computed` | policy |
| `R1866` | `C:\Users\ala\Documents\dl-enclave\tools\port\test\mount.test.mjs` | 17555 | `not computed` | witness, cadence, mount, policy, ledger |
| `R1867` | `C:\Users\ala\Documents\dl-enclave\tools\port\test\openlock.test.mjs` | 9765 | `not computed` | policy |
| `R1868` | `C:\Users\ala\Documents\dl-enclave\tools\port\test\patch.test.mjs` | 8557 | `not computed` | policy, ledger |
| `R1869` | `C:\Users\ala\Documents\dl-enclave\tools\port\test\placement.test.mjs` | 6775 | `not computed` | policy |
| `R1870` | `C:\Users\ala\Documents\dl-enclave\tools\port\test\presenter.test.mjs` | 7166 | `not computed` | policy |
| `R1871` | `C:\Users\ala\Documents\dl-enclave\tools\port\test\scene.test.mjs` | 10648 | `not computed` | policy |
| `R1872` | `C:\Users\ala\Documents\dl-enclave\tools\port\test\session.test.mjs` | 9198 | `not computed` | policy, ledger |
| `R1873` | `C:\Users\ala\Documents\dl-enclave\tools\port\test\shell-record.test.mjs` | 4890 | `not computed` | witness, policy, ledger |
| `R1874` | `C:\Users\ala\Documents\dl-enclave\tools\tests\test_project_surface.py` | 10139 | `not computed` | policy |
| `R1875` | `C:\Users\ala\Documents\dl-enclave\tools\tests\test_surface_receiver.py` | 21674 | `not computed` | policy, ledger |
| `R1876` | `C:\Users\ala\Documents\ala_civ_bots_prototype\AGENTS.md` | 2194 | `not computed` | policy |
| `R1877` | `C:\Users\ala\Documents\ala_civ_bots_prototype\build.gradle` | 15914 | `not computed` | witness, cadence, client, policy |
| `R1878` | `C:\Users\ala\Documents\ala_civ_bots_prototype\CHECKPOINT.md` | 54028 | `not computed` | witness, civilians, cadence, mount, client, policy, ledger |
| `R1879` | `C:\Users\ala\Documents\ala_civ_bots_prototype\README.md` | 24093 | `not computed` | witness, civilians, cadence, mount, client, policy, ledger |
| `R1880` | `C:\Users\ala\Documents\ala_civ_bots_prototype\docs\AUDIT_AGAINST_SECURE_SHELL.md` | 10505 | `not computed` | witness, civilians, mount, client, policy, ledger |
| `R1881` | `C:\Users\ala\Documents\ala_civ_bots_prototype\docs\correction.md` | 5078 | `not computed` | client, policy |
| `R1882` | `C:\Users\ala\Documents\ala_civ_bots_prototype\docs\freebuff_persistent_execution_and_continuation_directive.md` | 9597 | `not computed` | client, policy |
| `R1883` | `C:\Users\ala\Documents\ala_civ_bots_prototype\docs\GAIA.md` | 11523 | `not computed` | civilians, cadence, policy, ledger |
| `R1884` | `C:\Users\ala\Documents\ala_civ_bots_prototype\docs\GAMEPLAY_DEGREES.md` | 10717 | `not computed` | witness, health, client, policy, ledger |
| `R1885` | `C:\Users\ala\Documents\ala_civ_bots_prototype\docs\IMPLEMENTATION_STATUS.md` | 60782 | `not computed` | witness, civilians, cadence, health, mount, client, policy, ledger |
| `R1886` | `C:\Users\ala\Documents\ala_civ_bots_prototype\docs\LANGUAGE_AUDIT.md` | 7593 | `not computed` | witness, policy, ledger |
| `R1887` | `C:\Users\ala\Documents\ala_civ_bots_prototype\docs\LAYER_TABLE.md` | 5413 | `not computed` | witness, civilians, mount, client, policy, ledger |
| `R1888` | `C:\Users\ala\Documents\ala_civ_bots_prototype\docs\minecraft_agent_chat_and_social_observability_addendum.md` | 27359 | `not computed` | witness, cadence, client, policy |
| `R1889` | `C:\Users\ala\Documents\ala_civ_bots_prototype\docs\minecraft_ensouled_system1_cua_architecture_v3.md` | 240813 | `not computed` | witness, civilians, cadence, health, format, client, policy, ledger |
| `R1890` | `C:\Users\ala\Documents\ala_civ_bots_prototype\docs\minecraft_ensouled_system1_cua_architecture_v4.md` | 320781 | `not computed` | witness, civilians, cadence, health, format, client, policy, ledger |
| `R1891` | `C:\Users\ala\Documents\ala_civ_bots_prototype\docs\minecraft_entity_ai_replacement_transition_plan.md` | 47321 | `not computed` | witness, civilians, cadence, health, client, policy |
| `R1892` | `C:\Users\ala\Documents\ala_civ_bots_prototype\docs\minecraft_fake_player_first_addendum.md` | 46992 | `not computed` | civilians, cadence, health, client, policy, ledger |
| `R1893` | `C:\Users\ala\Documents\ala_civ_bots_prototype\docs\minecraft_headless_full_fidelity_fabric_client_addendum.md` | 33413 | `not computed` | civilians, cadence, health, client, policy, ledger |
| `R1894` | `C:\Users\ala\Documents\ala_civ_bots_prototype\docs\minecraft_persistent_interactive_dev_server_test_harness_directive.md` | 16576 | `not computed` | client, policy |
| `R1895` | `C:\Users\ala\Documents\ala_civ_bots_prototype\docs\minecraft_player_parity_extensible_needs_and_native_chat_addendum.md` | 43431 | `not computed` | civilians, cadence, health, format, client, policy |
| `R1896` | `C:\Users\ala\Documents\ala_civ_bots_prototype\docs\minecraft_product_execution_directive_beyond_phase1.md` | 28263 | `not computed` | health, client, policy |
| `R1897` | `C:\Users\ala\Documents\ala_civ_bots_prototype\docs\minecraft_shared_server_bot_client_population_addendum.md` | 48575 | `not computed` | civilians, cadence, health, client, policy, ledger |
| `R1898` | `C:\Users\ala\Documents\ala_civ_bots_prototype\docs\persistent_city_builder_tower_defense_design_analysis.md` | 62394 | `not computed` | cadence, health, client, policy |
| `R1899` | `C:\Users\ala\Documents\ala_civ_bots_prototype\docs\persistent_city_builder_tower_defense_design_analysis_v2.md` | 107797 | `not computed` | cadence, health, client, policy |
| `R1900` | `C:\Users\ala\Documents\ala_civ_bots_prototype\docs\persistent_city_builder_tower_defense_design_analysis_v4.md` | 234618 | `not computed` | witness, cadence, health, format, mount, client, policy, ledger |
| `R1901` | `C:\Users\ala\Documents\ala_civ_bots_prototype\docs\persistent_city_builder_tower_defense_design_analysis_v5.md` | 241895 | `not computed` | witness, cadence, health, format, mount, client, policy, ledger |
| `R1902` | `C:\Users\ala\Documents\ala_civ_bots_prototype\docs\persistent_city_builder_tower_defense_design_analysis_v9.md` | 492038 | `not computed` | witness, civilians, cadence, health, format, mount, client, policy, ledger |
| `R1903` | `C:\Users\ala\Documents\ala_civ_bots_prototype\docs\PHASE0_CONTRACTS.md` | 7024 | `not computed` | civilians, cadence, health, client, policy |
| `R1904` | `C:\Users\ala\Documents\ala_civ_bots_prototype\docs\ping_wheel_messages.md` | 72080 | `not computed` | health |
| `R1905` | `C:\Users\ala\Documents\ala_civ_bots_prototype\docs\UPSTREAM_ALIGNMENT.md` | 9545 | `not computed` | witness, civilians, cadence, mount, policy, ledger |
| `R1906` | `C:\Users\ala\Documents\ala_civ_bots_prototype\docs\V9_FINDINGS.md` | 16024 | `not computed` | witness, cadence, health, client, policy, ledger |
| `R1907` | `C:\Users\ala\Documents\ala_civ_bots_prototype\docs\VERB_CLASSIFIER_V1_IMPLEMENTATION_PLAN.md` | 26919 | `not computed` | witness, civilians, cadence, policy, ledger |
| `R1908` | `C:\Users\ala\Documents\ala_civ_bots_prototype\docs\WORLD_INTERACTION.md` | 13044 | `not computed` | cadence, policy, ledger |
| `R1909` | `C:\Users\ala\Documents\ala_civ_bots_prototype\logs\interrupt-harvest.sh` | 1834 | `not computed` | client |
| `R1910` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\bots\Ash\config\attributefix.json` | 3735 | `not computed` | health, client |
| `R1911` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\bots\Ash\config\c2me.toml` | 6368 | `not computed` | cadence |
| `R1912` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\bots\Ash\config\create_new_age-common.toml` | 4261 | `not computed` | cadence |
| `R1913` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\bots\Ash\config\entityculling.json` | 2248 | `not computed` | format, client |
| `R1914` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\bots\Ash\config\fallingleaves.json` | 601 | `not computed` | client |
| `R1915` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\bots\Ash\config\firstperson.json` | 593 | `not computed` | format |
| `R1916` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\bots\Ash\config\forgeconfigapiport.toml` | 1582 | `not computed` | client |
| `R1917` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\bots\Ash\config\lambdynlights.toml` | 1081 | `not computed` | client |
| `R1918` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\bots\Ash\config\notenoughanimations.json` | 3359 | `not computed` | client |
| `R1919` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\bots\Ash\config\visuality.json` | 1142 | `not computed` | client |
| `R1920` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\bots\Ash\config\watut-item-arm-adjustments.json` | 3367 | `not computed` | client |
| `R1921` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\bots\Ash\config\jade\hide-blocks.json` | 191 | `not computed` | client |
| `R1922` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\bots\Ash\config\jade\hide-entities.json` | 325 | `not computed` | client |
| `R1923` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\bots\Ash\config\jade\plugins.json` | 1680 | `not computed` | health, client |
| `R1924` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\bots\Ash\config\jade\sort-order.json` | 1517 | `not computed` | health, client |
| `R1925` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\bots\Bram\config\attributefix.json` | 3735 | `not computed` | health, client |
| `R1926` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\bots\Bram\config\c2me.toml` | 6368 | `not computed` | cadence |
| `R1927` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\bots\Bram\config\create_new_age-common.toml` | 4261 | `not computed` | cadence |
| `R1928` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\bots\Bram\config\entityculling.json` | 2248 | `not computed` | format, client |
| `R1929` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\bots\Bram\config\fallingleaves.json` | 601 | `not computed` | client |
| `R1930` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\bots\Bram\config\firstperson.json` | 593 | `not computed` | format |
| `R1931` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\bots\Bram\config\forgeconfigapiport.toml` | 1582 | `not computed` | client |
| `R1932` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\bots\Bram\config\lambdynlights.toml` | 1081 | `not computed` | client |
| `R1933` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\bots\Bram\config\notenoughanimations.json` | 3359 | `not computed` | client |
| `R1934` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\bots\Bram\config\visuality.json` | 1142 | `not computed` | client |
| `R1935` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\bots\Bram\config\watut-item-arm-adjustments.json` | 3367 | `not computed` | client |
| `R1936` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\bots\Bram\config\jade\hide-blocks.json` | 191 | `not computed` | client |
| `R1937` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\bots\Bram\config\jade\hide-entities.json` | 325 | `not computed` | client |
| `R1938` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\bots\Bram\config\jade\plugins.json` | 1680 | `not computed` | health, client |
| `R1939` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\bots\Bram\config\jade\sort-order.json` | 1517 | `not computed` | health, client |
| `R1940` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\bots\Bram\config\ModernUI\client.toml` | 8783 | `not computed` | client |
| `R1941` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\bots\Bram\config\ModernUI\text.toml` | 6054 | `not computed` | client |
| `R1942` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\bots\Resty\config\attributefix.json` | 3735 | `not computed` | health, client |
| `R1943` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\bots\Resty\config\c2me.toml` | 6368 | `not computed` | cadence |
| `R1944` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\bots\Resty\config\create_new_age-common.toml` | 4261 | `not computed` | cadence |
| `R1945` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\bots\Resty\config\entityculling.json` | 2248 | `not computed` | format, client |
| `R1946` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\bots\Resty\config\fallingleaves.json` | 601 | `not computed` | client |
| `R1947` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\bots\Resty\config\firstperson.json` | 593 | `not computed` | format |
| `R1948` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\bots\Resty\config\forgeconfigapiport.toml` | 1582 | `not computed` | client |
| `R1949` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\bots\Resty\config\lambdynlights.toml` | 1081 | `not computed` | client |
| `R1950` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\bots\Resty\config\notenoughanimations.json` | 3359 | `not computed` | client |
| `R1951` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\bots\Resty\config\visuality.json` | 1142 | `not computed` | client |
| `R1952` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\bots\Resty\config\watut-item-arm-adjustments.json` | 3367 | `not computed` | client |
| `R1953` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\bots\Resty\config\jade\hide-blocks.json` | 191 | `not computed` | client |
| `R1954` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\bots\Resty\config\jade\hide-entities.json` | 325 | `not computed` | client |
| `R1955` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\bots\Resty\config\jade\plugins.json` | 1680 | `not computed` | health, client |
| `R1956` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\bots\Resty\config\jade\sort-order.json` | 1517 | `not computed` | health, client |
| `R1957` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\bots\Resty\config\ModernUI\client.toml` | 8783 | `not computed` | client |
| `R1958` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\bots\Resty\config\ModernUI\text.toml` | 6054 | `not computed` | client |
| `R1959` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\config\attributefix.json` | 3735 | `not computed` | health, client |
| `R1960` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\config\c2me.toml` | 6126 | `not computed` | cadence |
| `R1961` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\config\create_new_age-common.toml` | 4261 | `not computed` | cadence |
| `R1962` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\config\forgeconfigapiport.toml` | 1582 | `not computed` | client |
| `R1963` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\config\watut-item-arm-adjustments.json` | 3367 | `not computed` | client |
| `R1964` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\config\jade\sort-order.json` | 657 | `not computed` | client |
| `R1965` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\probe-universe\world\advancements\42c1ea43-5bd8-3633-a2a6-96b7b7097eaa.json` | 325 | `not computed` | client |
| `R1966` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\probe-universe\world\advancements\4491e473-c7c9-3195-a8de-330c79a24db4.json` | 325 | `not computed` | client |
| `R1967` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\probe-universe\world\advancements\dbb0994b-c341-4f6f-9476-b75f292ca6c1.json` | 179 | `not computed` | client |
| `R1968` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\probe-universe\world\stats\42c1ea43-5bd8-3633-a2a6-96b7b7097eaa.json` | 341 | `not computed` | client |
| `R1969` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\probe-universe\world\stats\4491e473-c7c9-3195-a8de-330c79a24db4.json` | 232 | `not computed` | client |
| `R1970` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\probe-universe\world\stats\dbb0994b-c341-4f6f-9476-b75f292ca6c1.json` | 81 | `not computed` | client |
| `R1971` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\residents\ash\mind.json` | 18277 | `not computed` | cadence |
| `R1972` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\selftest-universe\world\advancements\c4471b87-cca2-4181-b499-d363a499e829.json` | 1696 | `not computed` | client |
| `R1973` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\selftest-universe\world\advancements\e85e3cd6-a975-4e18-a36d-ddb6c8f2c6d9.json` | 1696 | `not computed` | client |
| `R1974` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\selftest-universe\world\stats\c4471b87-cca2-4181-b499-d363a499e829.json` | 101 | `not computed` | client |
| `R1975` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\selftest-universe\world\stats\e85e3cd6-a975-4e18-a36d-ddb6c8f2c6d9.json` | 144 | `not computed` | client |
| `R1976` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\0263f932-3d3c-4c0a-a9a3-ed96e9063ccb.json` | 179 | `not computed` | client |
| `R1977` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\03f28916-9da6-4ebe-8d8b-78207fee40ac.json` | 179 | `not computed` | client |
| `R1978` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\06afdc92-e327-411e-bf79-30076c78577d.json` | 179 | `not computed` | client |
| `R1979` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\0785220d-c436-4e4b-a118-2bce27990709.json` | 1484 | `not computed` | client |
| `R1980` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\0acc9afa-df17-4292-b4e1-38f2b7c0e00e.json` | 179 | `not computed` | client |
| `R1981` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\0d0f2e91-dc51-4dad-9a9a-2955c130fad5.json` | 179 | `not computed` | client |
| `R1982` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\0e1577e9-7889-4e21-a3a2-09c9040374ec.json` | 1484 | `not computed` | client |
| `R1983` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\0e6fe9f8-f7d5-4c41-af58-290279cff7b1.json` | 4856 | `not computed` | client, policy |
| `R1984` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\0e9a9f1e-2591-4331-bfeb-85c3ddc71e74.json` | 179 | `not computed` | client |
| `R1985` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\10ca0572-b9ec-4476-a736-5e0c16942adb.json` | 1484 | `not computed` | client |
| `R1986` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\115329a7-3757-44b9-825d-2fbf9b250608.json` | 179 | `not computed` | client |
| `R1987` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\140f8c51-43af-4656-b6cc-fe98c041f69a.json` | 1484 | `not computed` | client |
| `R1988` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\1a9bbb1d-2fa5-4fec-9e30-b36e716b1d2a.json` | 179 | `not computed` | client |
| `R1989` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\1ee30a03-b637-4069-8b90-13b7824e8e0a.json` | 1484 | `not computed` | client |
| `R1990` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\21a87a3c-6685-48bb-b828-12db0aea667d.json` | 1484 | `not computed` | client |
| `R1991` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\25e72826-a6f3-438b-90ea-6367933739a4.json` | 179 | `not computed` | client |
| `R1992` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\28ade34f-37b8-4667-82f0-28afd6a0df85.json` | 179 | `not computed` | client |
| `R1993` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\2b892f59-01ff-43da-9cda-4f9f4790e419.json` | 1484 | `not computed` | client |
| `R1994` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\2d8029d7-7f09-442f-9341-97f8c77b9b09.json` | 1484 | `not computed` | client |
| `R1995` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\2f89fe56-5821-442e-bf1a-e77581b0ba34.json` | 1484 | `not computed` | client |
| `R1996` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\2fe58c32-abfa-468c-9bb6-cbdeb03f5b60.json` | 179 | `not computed` | client |
| `R1997` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\303c46d9-b848-499e-abb3-71349b679555.json` | 179 | `not computed` | client |
| `R1998` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\30c4a167-391b-3f02-94ca-21ed0e6634cd.json` | 331 | `not computed` | client |
| `R1999` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\31baa6c2-c2c7-4add-8412-dcc7ece1bd99.json` | 179 | `not computed` | client |
| `R2000` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\34534c47-7fde-40f9-93ec-bf2c61a1d803.json` | 179 | `not computed` | client |
| `R2001` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\3483e5dc-b9e3-486f-b71b-4182d6774697.json` | 1484 | `not computed` | client |
| `R2002` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\37ec4be8-49f9-44e5-80a9-82895f3302ba.json` | 179 | `not computed` | client |
| `R2003` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\3a333732-b060-4852-9821-b8b2d25f326b.json` | 2314 | `not computed` | client, policy |
| `R2004` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\3d0f6764-2e2a-4503-a2ef-bdcca5f8bc85.json` | 179 | `not computed` | client |
| `R2005` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\3d1ef826-7a9a-4078-9250-02019501bff0.json` | 1908 | `not computed` | client |
| `R2006` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\3f0ca0c8-9f16-3b87-92fb-b626b9a1bb99.json` | 331 | `not computed` | client |
| `R2007` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\4209ec8b-4574-459e-bdbf-1744a66fc332.json` | 1484 | `not computed` | client |
| `R2008` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\42c1ea43-5bd8-3633-a2a6-96b7b7097eaa.json` | 3825 | `not computed` | client, policy |
| `R2009` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\42c68322-9369-4811-8e56-89df15785691.json` | 1484 | `not computed` | client |
| `R2010` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\42d0f9fb-4bd6-43e7-9006-3d31914e0bf6.json` | 1484 | `not computed` | client |
| `R2011` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\4491e473-c7c9-3195-a8de-330c79a24db4.json` | 14756 | `not computed` | client, policy |
| `R2012` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\4511eb47-3709-4b88-b007-72ace1f65a88.json` | 179 | `not computed` | client |
| `R2013` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\4686bd69-1c0b-4364-b51b-677c488f3741.json` | 179 | `not computed` | client |
| `R2014` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\4912a736-495d-44f3-9117-0a6bad605bff.json` | 1484 | `not computed` | client |
| `R2015` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\4b66a65d-d683-412a-b402-8932efbac23d.json` | 179 | `not computed` | client |
| `R2016` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\4e247541-b059-4c76-a39a-4f214445c2e9.json` | 1484 | `not computed` | client |
| `R2017` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\4ee49106-efb6-47f3-9548-0e606d702afb.json` | 179 | `not computed` | client |
| `R2018` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\4f06bacd-6056-4be0-bd15-a9b243cb8536.json` | 1484 | `not computed` | client |
| `R2019` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\4f7e0284-7727-4391-88e7-1902be0acaad.json` | 179 | `not computed` | client |
| `R2020` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\5149b185-1d2b-45c3-bdef-f0cc95c42cac.json` | 1484 | `not computed` | client |
| `R2021` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\5234b8fc-5248-4c62-a1e9-dff4de71c855.json` | 179 | `not computed` | client |
| `R2022` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\5437405e-2940-3a7d-80d1-be97767ab17c.json` | 331 | `not computed` | client |
| `R2023` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\565f7ab0-8002-4780-9187-e82ded23986c.json` | 1484 | `not computed` | client |
| `R2024` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\5963cc08-91c8-3c07-854c-c63cf3bdc998.json` | 331 | `not computed` | client |
| `R2025` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\5b47587e-c7f3-4c75-af31-7d28d5b5867c.json` | 179 | `not computed` | client |
| `R2026` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\5b806eb9-c064-4cf1-b23c-64756dfa0bc4.json` | 179 | `not computed` | client |
| `R2027` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\5c6cf72d-1bcf-49f3-a27c-f0fc9b94b311.json` | 179 | `not computed` | client |
| `R2028` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\60a52667-da5c-43f6-9b23-ff7a8e4cfa3b.json` | 1484 | `not computed` | client |
| `R2029` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\616b4448-bf5f-407a-8009-6b6dd9270276.json` | 1484 | `not computed` | client |
| `R2030` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\63376c33-f357-41af-b75e-a2335d9b07a8.json` | 179 | `not computed` | client |
| `R2031` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\6769f817-0a62-45f8-8b7e-8478aca5dd67.json` | 179 | `not computed` | client |
| `R2032` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\6ad21f27-1ba6-401c-8377-837165f796dd.json` | 1484 | `not computed` | client |
| `R2033` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\736767e1-59ae-420d-8732-984ef4387944.json` | 179 | `not computed` | client |
| `R2034` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\770490f3-1018-4be3-b634-921eb38f8375.json` | 179 | `not computed` | client |
| `R2035` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\77bc13e3-f04c-48b9-bb2d-4f0c813d10cd.json` | 179 | `not computed` | client |
| `R2036` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\78a9c8c6-c4c5-4a4f-a51d-ceb89eec3ce7.json` | 179 | `not computed` | client |
| `R2037` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\7d253241-8372-4f90-8de3-677f84f558f8.json` | 179 | `not computed` | client |
| `R2038` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\7dc8d522-c97c-4ff4-b499-f331a075c4a0.json` | 179 | `not computed` | client |
| `R2039` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\7ecce838-f4aa-4495-8a5d-2e31f3a19f79.json` | 179 | `not computed` | client |
| `R2040` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\7f622cdb-df93-440a-8928-c35b752a4db4.json` | 179 | `not computed` | client |
| `R2041` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\802d677d-ddaa-47eb-9505-5ac03ea40b4c.json` | 179 | `not computed` | client |
| `R2042` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\8758e878-1fb7-3b70-862f-adee1ce95b7a.json` | 331 | `not computed` | client |
| `R2043` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\881d629a-a608-4293-b236-33aac8089a7f.json` | 179 | `not computed` | client |
| `R2044` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\88d58952-6469-4aca-ae3a-5fcb5cb6ac9b.json` | 179 | `not computed` | client |
| `R2045` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\8a50591c-fa28-48ef-81e8-d37735e0f270.json` | 890 | `not computed` | client |
| `R2046` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\8cea46cf-fc6d-4457-8cb0-db63ba5df714.json` | 179 | `not computed` | client |
| `R2047` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\8faad9d2-171c-40d1-941d-fbc4f6319d80.json` | 1484 | `not computed` | client |
| `R2048` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\90bbbf53-6f0a-40ac-91b5-0b32d6849e3b.json` | 179 | `not computed` | client |
| `R2049` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\90d68325-dc5a-38ff-9e7c-6ecbe3d4c81b.json` | 331 | `not computed` | client |
| `R2050` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\92f9a7e1-7d5f-4457-97be-4f19b58dbd32.json` | 179 | `not computed` | client |
| `R2051` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\949231a3-730d-4587-b3fb-50c5540c2a09.json` | 179 | `not computed` | client |
| `R2052` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\98e51a8c-764c-4968-834b-cb55935967c3.json` | 179 | `not computed` | client |
| `R2053` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\9a669096-fb5c-4e4c-9f57-3c1b00bccbef.json` | 179 | `not computed` | client |
| `R2054` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\9c5428ff-ab84-46cd-a2f0-96da330ac907.json` | 3249 | `not computed` | client, policy |
| `R2055` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\9d7dffb0-eaef-4ac8-aebc-830e836ea3f8.json` | 3282 | `not computed` | client, policy |
| `R2056` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\9eed3ac6-b475-4223-9990-d5ae8cfd44d3.json` | 179 | `not computed` | client |
| `R2057` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\9fc31ef6-5c67-35c5-9415-92b1944347de.json` | 331 | `not computed` | client |
| `R2058` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\a1f6ca37-f703-4fd4-a824-ae1f09654633.json` | 179 | `not computed` | client |
| `R2059` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\a35891f2-6304-3f20-a83e-cf7b946f73f6.json` | 331 | `not computed` | client |
| `R2060` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\a44cc263-280b-4ee7-8873-abc267d42f26.json` | 1484 | `not computed` | client |
| `R2061` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\a538c27f-ff47-4e59-8c14-c4b707117972.json` | 179 | `not computed` | client |
| `R2062` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\aa5a57db-fed6-4915-b74e-855c0b67f9e0.json` | 1484 | `not computed` | client |
| `R2063` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\ab35c2c0-8906-4f71-b7f3-6d7a7b5a7590.json` | 179 | `not computed` | client |
| `R2064` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\ad34bb3d-65ad-3e3e-8a67-a5c5b4251380.json` | 331 | `not computed` | client |
| `R2065` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\ae85577c-cd84-4f24-a79d-2973e456d197.json` | 179 | `not computed` | client |
| `R2066` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\afc3daaf-691d-4baf-892c-3f5eb4f5ad98.json` | 179 | `not computed` | client |
| `R2067` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\b157f307-0b61-4c04-b0c2-5f1372d17478.json` | 3249 | `not computed` | client, policy |
| `R2068` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\b185c458-c9a7-46e2-a617-036f96e30c6e.json` | 179 | `not computed` | client |
| `R2069` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\b719de46-59d7-4bd1-bd28-48edae182767.json` | 179 | `not computed` | client |
| `R2070` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\b9f7893c-790d-4609-bc81-27ca2ac36cb7.json` | 179 | `not computed` | client |
| `R2071` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\bb3967cc-45fb-4e46-866a-4e1843785b14.json` | 179 | `not computed` | client |
| `R2072` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\bf359808-ddf4-42b5-8566-2a97e081b77f.json` | 1484 | `not computed` | client |
| `R2073` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\bfd5e0c7-9497-4f37-b063-d0739b5cfa16.json` | 1484 | `not computed` | client |
| `R2074` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\c3d3f0a7-214f-4176-9712-d2effe5b0e15.json` | 1484 | `not computed` | client |
| `R2075` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\c9102c1e-4165-4717-936c-6b9b98ff3bb2.json` | 1484 | `not computed` | client |
| `R2076` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\cd8d3cc2-5561-4f0d-90e8-bf23eecc7990.json` | 179 | `not computed` | client |
| `R2077` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\cdf97a08-d540-42bc-ba7b-81ae18b656cf.json` | 179 | `not computed` | client |
| `R2078` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\ced433c6-1b6d-4356-8b01-14618022b6b9.json` | 1484 | `not computed` | client |
| `R2079` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\cef61656-b0ec-3ee3-b1dd-faa0f9ecebcb.json` | 331 | `not computed` | client |
| `R2080` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\d13d1ed0-626d-30e1-a2ea-e36403d2c6c0.json` | 331 | `not computed` | client |
| `R2081` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\d6ff2f50-4a2b-4214-b3e3-6714c61e9655.json` | 179 | `not computed` | client |
| `R2082` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\dc7b4a85-603c-4276-b653-4d62e9434543.json` | 1484 | `not computed` | client |
| `R2083` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\dd5422c9-0690-41e4-ae2f-696eb68f31b3.json` | 179 | `not computed` | client |
| `R2084` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\dfb9488c-7feb-466c-845c-dce13b86f999.json` | 179 | `not computed` | client |
| `R2085` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\e0a92cb3-5b65-49b3-95b8-e8becf8fe3e9.json` | 1484 | `not computed` | client |
| `R2086` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\e150266c-706f-4ac3-8145-a66d2a060cb6.json` | 179 | `not computed` | client |
| `R2087` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\e2c8c7cb-4ae9-45f0-b7f1-f58a56e46b52.json` | 1484 | `not computed` | client |
| `R2088` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\e5bd28aa-d7ed-4c1e-814a-179c91c348b0.json` | 179 | `not computed` | client |
| `R2089` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\e6ecbf8e-8896-43d0-98e9-7651052270b1.json` | 1484 | `not computed` | client |
| `R2090` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\e896ed2e-0dcb-3fa9-91c9-468f5a16bb18.json` | 331 | `not computed` | client |
| `R2091` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\ec5f186c-b94a-4ba9-a0ee-d2e2e1acab01.json` | 1484 | `not computed` | client |
| `R2092` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\ed51bfc7-85cb-3247-a963-bb9ac4c089f9.json` | 331 | `not computed` | client |
| `R2093` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\eda8817e-723e-410c-b6d7-6afd46846d54.json` | 890 | `not computed` | client |
| `R2094` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\f09f1ed2-6f6e-4da0-8121-1d72d803fc17.json` | 1484 | `not computed` | client |
| `R2095` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\f5820a72-e5de-4328-bd50-b96851fbc008.json` | 179 | `not computed` | client |
| `R2096` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\f5966f1c-3800-491d-81ed-7062131841c1.json` | 1484 | `not computed` | client |
| `R2097` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\f5c0acae-be8c-4b42-871c-baca480fcc3d.json` | 179 | `not computed` | client |
| `R2098` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\f740fe2d-dc8e-3d67-a947-44fc53575121.json` | 331 | `not computed` | client |
| `R2099` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\f809f3cb-589f-4f70-aa71-602589173294.json` | 179 | `not computed` | client |
| `R2100` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\fa7b85cc-1229-3450-911b-6c762bf79a36.json` | 331 | `not computed` | client |
| `R2101` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\fb4e143e-3870-4985-97a1-0f76a62dec04.json` | 1484 | `not computed` | client |
| `R2102` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\advancements\fe2ac4d8-2da4-4e83-93f7-338d50364e2f.json` | 1484 | `not computed` | client |
| `R2103` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\ensouled\autopopulation.json` | 1874 | `not computed` | client |
| `R2104` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\ensouled\work.json` | 271569 | `not computed` | witness, cadence, client, policy |
| `R2105` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\0263f932-3d3c-4c0a-a9a3-ed96e9063ccb.json` | 101 | `not computed` | client |
| `R2106` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\03f28916-9da6-4ebe-8d8b-78207fee40ac.json` | 101 | `not computed` | client |
| `R2107` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\06afdc92-e327-411e-bf79-30076c78577d.json` | 101 | `not computed` | client |
| `R2108` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\0785220d-c436-4e4b-a118-2bce27990709.json` | 102 | `not computed` | client |
| `R2109` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\0acc9afa-df17-4292-b4e1-38f2b7c0e00e.json` | 103 | `not computed` | client |
| `R2110` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\0d0f2e91-dc51-4dad-9a9a-2955c130fad5.json` | 102 | `not computed` | client |
| `R2111` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\0e1577e9-7889-4e21-a3a2-09c9040374ec.json` | 100 | `not computed` | client |
| `R2112` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\0e6fe9f8-f7d5-4c41-af58-290279cff7b1.json` | 241 | `not computed` | client |
| `R2113` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\0e9a9f1e-2591-4331-bfeb-85c3ddc71e74.json` | 101 | `not computed` | client |
| `R2114` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\10ca0572-b9ec-4476-a736-5e0c16942adb.json` | 101 | `not computed` | client |
| `R2115` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\115329a7-3757-44b9-825d-2fbf9b250608.json` | 81 | `not computed` | client |
| `R2116` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\140f8c51-43af-4656-b6cc-fe98c041f69a.json` | 102 | `not computed` | client |
| `R2117` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\1a9bbb1d-2fa5-4fec-9e30-b36e716b1d2a.json` | 81 | `not computed` | client |
| `R2118` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\1ee30a03-b637-4069-8b90-13b7824e8e0a.json` | 103 | `not computed` | client |
| `R2119` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\21a87a3c-6685-48bb-b828-12db0aea667d.json` | 101 | `not computed` | client |
| `R2120` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\25e72826-a6f3-438b-90ea-6367933739a4.json` | 101 | `not computed` | client |
| `R2121` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\28ade34f-37b8-4667-82f0-28afd6a0df85.json` | 101 | `not computed` | client |
| `R2122` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\2b892f59-01ff-43da-9cda-4f9f4790e419.json` | 102 | `not computed` | client |
| `R2123` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\2d8029d7-7f09-442f-9341-97f8c77b9b09.json` | 128 | `not computed` | client |
| `R2124` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\2f89fe56-5821-442e-bf1a-e77581b0ba34.json` | 102 | `not computed` | client |
| `R2125` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\2fe58c32-abfa-468c-9bb6-cbdeb03f5b60.json` | 102 | `not computed` | client |
| `R2126` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\303c46d9-b848-499e-abb3-71349b679555.json` | 102 | `not computed` | client |
| `R2127` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\30c4a167-391b-3f02-94ca-21ed0e6634cd.json` | 196 | `not computed` | client |
| `R2128` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\31baa6c2-c2c7-4add-8412-dcc7ece1bd99.json` | 102 | `not computed` | client |
| `R2129` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\34534c47-7fde-40f9-93ec-bf2c61a1d803.json` | 102 | `not computed` | client |
| `R2130` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\3483e5dc-b9e3-486f-b71b-4182d6774697.json` | 100 | `not computed` | client |
| `R2131` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\37ec4be8-49f9-44e5-80a9-82895f3302ba.json` | 81 | `not computed` | client |
| `R2132` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\3a333732-b060-4852-9821-b8b2d25f326b.json` | 194 | `not computed` | client |
| `R2133` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\3d0f6764-2e2a-4503-a2ef-bdcca5f8bc85.json` | 100 | `not computed` | client |
| `R2134` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\3d1ef826-7a9a-4078-9250-02019501bff0.json` | 227 | `not computed` | client |
| `R2135` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\3f0ca0c8-9f16-3b87-92fb-b626b9a1bb99.json` | 204 | `not computed` | client |
| `R2136` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\4209ec8b-4574-459e-bdbf-1744a66fc332.json` | 130 | `not computed` | client |
| `R2137` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\42c1ea43-5bd8-3633-a2a6-96b7b7097eaa.json` | 1062 | `not computed` | client |
| `R2138` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\42c68322-9369-4811-8e56-89df15785691.json` | 81 | `not computed` | client |
| `R2139` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\42d0f9fb-4bd6-43e7-9006-3d31914e0bf6.json` | 102 | `not computed` | client |
| `R2140` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\4491e473-c7c9-3195-a8de-330c79a24db4.json` | 1369 | `not computed` | client |
| `R2141` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\4511eb47-3709-4b88-b007-72ace1f65a88.json` | 101 | `not computed` | client |
| `R2142` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\4686bd69-1c0b-4364-b51b-677c488f3741.json` | 101 | `not computed` | client |
| `R2143` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\4912a736-495d-44f3-9117-0a6bad605bff.json` | 104 | `not computed` | client |
| `R2144` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\4b66a65d-d683-412a-b402-8932efbac23d.json` | 128 | `not computed` | client |
| `R2145` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\4e247541-b059-4c76-a39a-4f214445c2e9.json` | 102 | `not computed` | client |
| `R2146` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\4ee49106-efb6-47f3-9548-0e606d702afb.json` | 101 | `not computed` | client |
| `R2147` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\4f06bacd-6056-4be0-bd15-a9b243cb8536.json` | 128 | `not computed` | client |
| `R2148` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\4f7e0284-7727-4391-88e7-1902be0acaad.json` | 81 | `not computed` | client |
| `R2149` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\5149b185-1d2b-45c3-bdef-f0cc95c42cac.json` | 156 | `not computed` | client |
| `R2150` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\5234b8fc-5248-4c62-a1e9-dff4de71c855.json` | 103 | `not computed` | client |
| `R2151` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\5437405e-2940-3a7d-80d1-be97767ab17c.json` | 196 | `not computed` | client |
| `R2152` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\565f7ab0-8002-4780-9187-e82ded23986c.json` | 184 | `not computed` | client |
| `R2153` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\5963cc08-91c8-3c07-854c-c63cf3bdc998.json` | 204 | `not computed` | client |
| `R2154` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\5b47587e-c7f3-4c75-af31-7d28d5b5867c.json` | 102 | `not computed` | client |
| `R2155` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\5b806eb9-c064-4cf1-b23c-64756dfa0bc4.json` | 129 | `not computed` | client |
| `R2156` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\5c6cf72d-1bcf-49f3-a27c-f0fc9b94b311.json` | 103 | `not computed` | client |
| `R2157` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\60a52667-da5c-43f6-9b23-ff7a8e4cfa3b.json` | 130 | `not computed` | client |
| `R2158` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\616b4448-bf5f-407a-8009-6b6dd9270276.json` | 102 | `not computed` | client |
| `R2159` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\63376c33-f357-41af-b75e-a2335d9b07a8.json` | 101 | `not computed` | client |
| `R2160` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\6769f817-0a62-45f8-8b7e-8478aca5dd67.json` | 128 | `not computed` | client |
| `R2161` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\6ad21f27-1ba6-401c-8377-837165f796dd.json` | 159 | `not computed` | client |
| `R2162` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\736767e1-59ae-420d-8732-984ef4387944.json` | 102 | `not computed` | client |
| `R2163` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\770490f3-1018-4be3-b634-921eb38f8375.json` | 128 | `not computed` | client |
| `R2164` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\77bc13e3-f04c-48b9-bb2d-4f0c813d10cd.json` | 102 | `not computed` | client |
| `R2165` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\78a9c8c6-c4c5-4a4f-a51d-ceb89eec3ce7.json` | 129 | `not computed` | client |
| `R2166` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\7d253241-8372-4f90-8de3-677f84f558f8.json` | 124 | `not computed` | client |
| `R2167` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\7dc8d522-c97c-4ff4-b499-f331a075c4a0.json` | 101 | `not computed` | client |
| `R2168` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\7ecce838-f4aa-4495-8a5d-2e31f3a19f79.json` | 102 | `not computed` | client |
| `R2169` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\7f622cdb-df93-440a-8928-c35b752a4db4.json` | 101 | `not computed` | client |
| `R2170` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\802d677d-ddaa-47eb-9505-5ac03ea40b4c.json` | 102 | `not computed` | client |
| `R2171` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\8758e878-1fb7-3b70-862f-adee1ce95b7a.json` | 204 | `not computed` | client |
| `R2172` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\881d629a-a608-4293-b236-33aac8089a7f.json` | 129 | `not computed` | client |
| `R2173` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\88d58952-6469-4aca-ae3a-5fcb5cb6ac9b.json` | 98 | `not computed` | client |
| `R2174` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\8a50591c-fa28-48ef-81e8-d37735e0f270.json` | 243 | `not computed` | client |
| `R2175` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\8cea46cf-fc6d-4457-8cb0-db63ba5df714.json` | 99 | `not computed` | client |
| `R2176` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\8faad9d2-171c-40d1-941d-fbc4f6319d80.json` | 102 | `not computed` | client |
| `R2177` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\90bbbf53-6f0a-40ac-91b5-0b32d6849e3b.json` | 101 | `not computed` | client |
| `R2178` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\90d68325-dc5a-38ff-9e7c-6ecbe3d4c81b.json` | 204 | `not computed` | client |
| `R2179` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\92f9a7e1-7d5f-4457-97be-4f19b58dbd32.json` | 102 | `not computed` | client |
| `R2180` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\949231a3-730d-4587-b3fb-50c5540c2a09.json` | 101 | `not computed` | client |
| `R2181` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\98e51a8c-764c-4968-834b-cb55935967c3.json` | 101 | `not computed` | client |
| `R2182` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\9a669096-fb5c-4e4c-9f57-3c1b00bccbef.json` | 100 | `not computed` | client |
| `R2183` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\9c5428ff-ab84-46cd-a2f0-96da330ac907.json` | 215 | `not computed` | client |
| `R2184` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\9d7dffb0-eaef-4ac8-aebc-830e836ea3f8.json` | 197 | `not computed` | client |
| `R2185` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\9eed3ac6-b475-4223-9990-d5ae8cfd44d3.json` | 100 | `not computed` | client |
| `R2186` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\9fc31ef6-5c67-35c5-9415-92b1944347de.json` | 231 | `not computed` | client |
| `R2187` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\a1f6ca37-f703-4fd4-a824-ae1f09654633.json` | 100 | `not computed` | client |
| `R2188` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\a35891f2-6304-3f20-a83e-cf7b946f73f6.json` | 196 | `not computed` | client |
| `R2189` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\a44cc263-280b-4ee7-8873-abc267d42f26.json` | 102 | `not computed` | client |
| `R2190` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\a538c27f-ff47-4e59-8c14-c4b707117972.json` | 101 | `not computed` | client |
| `R2191` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\aa5a57db-fed6-4915-b74e-855c0b67f9e0.json` | 128 | `not computed` | client |
| `R2192` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\ab35c2c0-8906-4f71-b7f3-6d7a7b5a7590.json` | 100 | `not computed` | client |
| `R2193` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\ad34bb3d-65ad-3e3e-8a67-a5c5b4251380.json` | 196 | `not computed` | client |
| `R2194` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\ae85577c-cd84-4f24-a79d-2973e456d197.json` | 101 | `not computed` | client |
| `R2195` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\afc3daaf-691d-4baf-892c-3f5eb4f5ad98.json` | 101 | `not computed` | client |
| `R2196` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\b157f307-0b61-4c04-b0c2-5f1372d17478.json` | 191 | `not computed` | client |
| `R2197` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\b185c458-c9a7-46e2-a617-036f96e30c6e.json` | 102 | `not computed` | client |
| `R2198` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\b719de46-59d7-4bd1-bd28-48edae182767.json` | 99 | `not computed` | client |
| `R2199` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\b9f7893c-790d-4609-bc81-27ca2ac36cb7.json` | 101 | `not computed` | client |
| `R2200` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\bb3967cc-45fb-4e46-866a-4e1843785b14.json` | 101 | `not computed` | client |
| `R2201` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\bf359808-ddf4-42b5-8566-2a97e081b77f.json` | 101 | `not computed` | client |
| `R2202` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\bfd5e0c7-9497-4f37-b063-d0739b5cfa16.json` | 130 | `not computed` | client |
| `R2203` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\c3d3f0a7-214f-4176-9712-d2effe5b0e15.json` | 103 | `not computed` | client |
| `R2204` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\c9102c1e-4165-4717-936c-6b9b98ff3bb2.json` | 102 | `not computed` | client |
| `R2205` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\cd8d3cc2-5561-4f0d-90e8-bf23eecc7990.json` | 184 | `not computed` | client |
| `R2206` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\cdf97a08-d540-42bc-ba7b-81ae18b656cf.json` | 102 | `not computed` | client |
| `R2207` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\ced433c6-1b6d-4356-8b01-14618022b6b9.json` | 101 | `not computed` | client |
| `R2208` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\cef61656-b0ec-3ee3-b1dd-faa0f9ecebcb.json` | 307 | `not computed` | client |
| `R2209` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\d13d1ed0-626d-30e1-a2ea-e36403d2c6c0.json` | 310 | `not computed` | client |
| `R2210` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\d6ff2f50-4a2b-4214-b3e3-6714c61e9655.json` | 102 | `not computed` | client |
| `R2211` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\dc7b4a85-603c-4276-b653-4d62e9434543.json` | 128 | `not computed` | client |
| `R2212` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\dd5422c9-0690-41e4-ae2f-696eb68f31b3.json` | 101 | `not computed` | client |
| `R2213` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\dfb9488c-7feb-466c-845c-dce13b86f999.json` | 100 | `not computed` | client |
| `R2214` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\e0a92cb3-5b65-49b3-95b8-e8becf8fe3e9.json` | 128 | `not computed` | client |
| `R2215` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\e150266c-706f-4ac3-8145-a66d2a060cb6.json` | 101 | `not computed` | client |
| `R2216` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\e2c8c7cb-4ae9-45f0-b7f1-f58a56e46b52.json` | 102 | `not computed` | client |
| `R2217` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\e5bd28aa-d7ed-4c1e-814a-179c91c348b0.json` | 99 | `not computed` | client |
| `R2218` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\e6ecbf8e-8896-43d0-98e9-7651052270b1.json` | 131 | `not computed` | client |
| `R2219` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\e896ed2e-0dcb-3fa9-91c9-468f5a16bb18.json` | 196 | `not computed` | client |
| `R2220` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\ec5f186c-b94a-4ba9-a0ee-d2e2e1acab01.json` | 100 | `not computed` | client |
| `R2221` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\ed51bfc7-85cb-3247-a963-bb9ac4c089f9.json` | 196 | `not computed` | client |
| `R2222` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\eda8817e-723e-410c-b6d7-6afd46846d54.json` | 220 | `not computed` | client |
| `R2223` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\f09f1ed2-6f6e-4da0-8121-1d72d803fc17.json` | 102 | `not computed` | client |
| `R2224` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\f5820a72-e5de-4328-bd50-b96851fbc008.json` | 102 | `not computed` | client |
| `R2225` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\f5966f1c-3800-491d-81ed-7062131841c1.json` | 159 | `not computed` | client |
| `R2226` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\f5c0acae-be8c-4b42-871c-baca480fcc3d.json` | 102 | `not computed` | client |
| `R2227` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\f740fe2d-dc8e-3d67-a947-44fc53575121.json` | 196 | `not computed` | client |
| `R2228` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\f809f3cb-589f-4f70-aa71-602589173294.json` | 99 | `not computed` | client |
| `R2229` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\fa7b85cc-1229-3450-911b-6c762bf79a36.json` | 200 | `not computed` | client |
| `R2230` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\fb4e143e-3870-4985-97a1-0f76a62dec04.json` | 128 | `not computed` | client |
| `R2231` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world\stats\fe2ac4d8-2da4-4e83-93f7-338d50364e2f.json` | 102 | `not computed` | client |
| `R2232` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world-broken\advancements\0793296b-4f8c-4183-b4d3-0c52edd33676.json` | 179 | `not computed` | client |
| `R2233` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world-broken\advancements\15efc8bd-68a2-475e-8d92-70ea0ce50ebe.json` | 179 | `not computed` | client |
| `R2234` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world-broken\advancements\3f0ca0c8-9f16-3b87-92fb-b626b9a1bb99.json` | 325 | `not computed` | client |
| `R2235` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world-broken\advancements\42c1ea43-5bd8-3633-a2a6-96b7b7097eaa.json` | 743 | `not computed` | client |
| `R2236` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world-broken\advancements\4490ac59-78b7-4202-ad71-72db6fab28b6.json` | 179 | `not computed` | client |
| `R2237` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world-broken\advancements\4491e473-c7c9-3195-a8de-330c79a24db4.json` | 743 | `not computed` | client |
| `R2238` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world-broken\advancements\819f2e53-f8b0-4fa9-9c83-0511ee850845.json` | 597 | `not computed` | client |
| `R2239` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world-broken\advancements\912c6f84-446d-3039-8711-7608ef7feac4.json` | 325 | `not computed` | client |
| `R2240` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world-broken\advancements\9d79e2b0-7e59-48c0-a7c3-0ebb80b9aa11.json` | 179 | `not computed` | client |
| `R2241` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world-broken\advancements\a719fb04-17c7-496e-ab2b-74076dd59e77.json` | 179 | `not computed` | client |
| `R2242` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world-broken\advancements\d689fe31-8b8a-4c5f-a49c-753134638f92.json` | 597 | `not computed` | client |
| `R2243` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world-broken\advancements\e46bdece-a623-407c-a5dd-34f606dbfade.json` | 597 | `not computed` | client |
| `R2244` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world-broken\advancements\fbae946e-4ed8-458b-8f43-39e572ce59f9.json` | 597 | `not computed` | client |
| `R2245` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world-broken\stats\0793296b-4f8c-4183-b4d3-0c52edd33676.json` | 76 | `not computed` | client |
| `R2246` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world-broken\stats\15efc8bd-68a2-475e-8d92-70ea0ce50ebe.json` | 79 | `not computed` | client |
| `R2247` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world-broken\stats\3f0ca0c8-9f16-3b87-92fb-b626b9a1bb99.json` | 196 | `not computed` | client |
| `R2248` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world-broken\stats\42c1ea43-5bd8-3633-a2a6-96b7b7097eaa.json` | 481 | `not computed` | client |
| `R2249` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world-broken\stats\4490ac59-78b7-4202-ad71-72db6fab28b6.json` | 148 | `not computed` | client |
| `R2250` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world-broken\stats\4491e473-c7c9-3195-a8de-330c79a24db4.json` | 281 | `not computed` | client |
| `R2251` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world-broken\stats\819f2e53-f8b0-4fa9-9c83-0511ee850845.json` | 165 | `not computed` | client |
| `R2252` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world-broken\stats\912c6f84-446d-3039-8711-7608ef7feac4.json` | 200 | `not computed` | client |
| `R2253` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world-broken\stats\9d79e2b0-7e59-48c0-a7c3-0ebb80b9aa11.json` | 76 | `not computed` | client |
| `R2254` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world-broken\stats\a719fb04-17c7-496e-ab2b-74076dd59e77.json` | 76 | `not computed` | client |
| `R2255` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world-broken\stats\d689fe31-8b8a-4c5f-a49c-753134638f92.json` | 151 | `not computed` | client |
| `R2256` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world-broken\stats\e46bdece-a623-407c-a5dd-34f606dbfade.json` | 76 | `not computed` | client |
| `R2257` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world-broken\stats\fbae946e-4ed8-458b-8f43-39e572ce59f9.json` | 150 | `not computed` | client |
| `R2258` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world-modded-do-not-change-again\advancements\42c1ea43-5bd8-3633-a2a6-96b7b7097eaa.json` | 2425 | `not computed` | client |
| `R2259` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world-modded-do-not-change-again\advancements\4491e473-c7c9-3195-a8de-330c79a24db4.json` | 2608 | `not computed` | client |
| `R2260` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world-modded-do-not-change-again\advancements\91a41fcf-7bbf-35c1-b491-3a7784770bc7.json` | 2504 | `not computed` | client |
| `R2261` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world-modded-do-not-change-again\advancements\9fc31ef6-5c67-35c5-9415-92b1944347de.json` | 1301 | `not computed` | client |
| `R2262` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world-modded-do-not-change-again\advancements\efabd50c-48be-38bf-b0bf-c797ea5b5bea.json` | 325 | `not computed` | client |
| `R2263` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world-modded-do-not-change-again\advancements\fa682737-82f8-47dd-ada8-8c080f387878.json` | 179 | `not computed` | client |
| `R2264` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world-modded-do-not-change-again\stats\42c1ea43-5bd8-3633-a2a6-96b7b7097eaa.json` | 901 | `not computed` | client |
| `R2265` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world-modded-do-not-change-again\stats\4491e473-c7c9-3195-a8de-330c79a24db4.json` | 617 | `not computed` | client |
| `R2266` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world-modded-do-not-change-again\stats\91a41fcf-7bbf-35c1-b491-3a7784770bc7.json` | 609 | `not computed` | client |
| `R2267` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world-modded-do-not-change-again\stats\9fc31ef6-5c67-35c5-9415-92b1944347de.json` | 584 | `not computed` | client |
| `R2268` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world-modded-do-not-change-again\stats\efabd50c-48be-38bf-b0bf-c797ea5b5bea.json` | 200 | `not computed` | client |
| `R2269` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world-modded-do-not-change-again\stats\fa682737-82f8-47dd-ada8-8c080f387878.json` | 100 | `not computed` | client |
| `R2270` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world.flat-baseline\advancements\11702f06-d9e4-4119-b927-98d8c56018ae.json` | 179 | `not computed` | client |
| `R2271` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world.flat-baseline\advancements\42c1ea43-5bd8-3633-a2a6-96b7b7097eaa.json` | 743 | `not computed` | client |
| `R2272` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world.flat-baseline\advancements\4491e473-c7c9-3195-a8de-330c79a24db4.json` | 743 | `not computed` | client |
| `R2273` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world.flat-baseline\advancements\91a41fcf-7bbf-35c1-b491-3a7784770bc7.json` | 325 | `not computed` | client |
| `R2274` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world.flat-baseline\advancements\9fc31ef6-5c67-35c5-9415-92b1944347de.json` | 325 | `not computed` | client |
| `R2275` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world.flat-baseline\advancements\c3e1b84a-26be-42d3-96ff-3bb30679a3f6.json` | 179 | `not computed` | client |
| `R2276` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world.flat-baseline\advancements\c4b7b056-c6f7-4f0d-b7c4-6b9225ab8258.json` | 597 | `not computed` | client |
| `R2277` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world.flat-baseline\advancements\efabd50c-48be-38bf-b0bf-c797ea5b5bea.json` | 325 | `not computed` | client |
| `R2278` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world.flat-baseline\stats\11702f06-d9e4-4119-b927-98d8c56018ae.json` | 78 | `not computed` | client |
| `R2279` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world.flat-baseline\stats\42c1ea43-5bd8-3633-a2a6-96b7b7097eaa.json` | 509 | `not computed` | client |
| `R2280` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world.flat-baseline\stats\4491e473-c7c9-3195-a8de-330c79a24db4.json` | 254 | `not computed` | client |
| `R2281` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world.flat-baseline\stats\91a41fcf-7bbf-35c1-b491-3a7784770bc7.json` | 304 | `not computed` | client |
| `R2282` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world.flat-baseline\stats\9fc31ef6-5c67-35c5-9415-92b1944347de.json` | 204 | `not computed` | client |
| `R2283` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world.flat-baseline\stats\c3e1b84a-26be-42d3-96ff-3bb30679a3f6.json` | 104 | `not computed` | client |
| `R2284` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world.flat-baseline\stats\c4b7b056-c6f7-4f0d-b7c4-6b9225ab8258.json` | 145 | `not computed` | client |
| `R2285` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world.flat-baseline\stats\efabd50c-48be-38bf-b0bf-c797ea5b5bea.json` | 200 | `not computed` | client |
| `R2286` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world.fresh-0147\advancements\42c1ea43-5bd8-3633-a2a6-96b7b7097eaa.json` | 331 | `not computed` | client |
| `R2287` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world.fresh-0147\stats\42c1ea43-5bd8-3633-a2a6-96b7b7097eaa.json` | 517 | `not computed` | client |
| `R2288` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world.prev-audit-162103\advancements\6dfee01f-c27d-411f-b06d-e1913c883497.json` | 597 | `not computed` | client |
| `R2289` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world.prev-audit-162103\stats\6dfee01f-c27d-411f-b06d-e1913c883497.json` | 167 | `not computed` | client |
| `R2290` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world.prev-chest\advancements\69d7f2f5-cf7b-4cf0-a231-77d5415b69d4.json` | 624 | `not computed` | client |
| `R2291` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world.prev-chest\stats\69d7f2f5-cf7b-4cf0-a231-77d5415b69d4.json` | 175 | `not computed` | client |
| `R2292` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world.probe-player2\advancements\42c1ea43-5bd8-3633-a2a6-96b7b7097eaa.json` | 325 | `not computed` | client |
| `R2293` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world.probe-player2\advancements\985e6828-62d0-4711-a206-342fc8ee0654.json` | 597 | `not computed` | client |
| `R2294` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world.probe-player2\stats\42c1ea43-5bd8-3633-a2a6-96b7b7097eaa.json` | 223 | `not computed` | client |
| `R2295` | `C:\Users\ala\Documents\ala_civ_bots_prototype\run\world.probe-player2\stats\985e6828-62d0-4711-a206-342fc8ee0654.json` | 167 | `not computed` | client |
| `R2296` | `C:\Users\ala\Documents\ala_civ_bots_prototype\scripts\bots.sh` | 8606 | `not computed` | policy |
| `R2297` | `C:\Users\ala\Documents\ala_civ_bots_prototype\scripts\client.sh` | 5455 | `not computed` | client, policy |
| `R2298` | `C:\Users\ala\Documents\ala_civ_bots_prototype\scripts\devserver.sh` | 4711 | `not computed` | cadence, client, policy |
| `R2299` | `C:\Users\ala\Documents\ala_civ_bots_prototype\scripts\mongo.sh` | 1808 | `not computed` | civilians, policy |
| `R2300` | `C:\Users\ala\Documents\ala_civ_bots_prototype\scripts\selftest.sh` | 5047 | `not computed` | cadence, client, policy |
| `R2301` | `C:\Users\ala\Documents\ala_civ_bots_prototype\scripts\stream.sh` | 1349 | `not computed` | policy, ledger |
| `R2302` | `C:\Users\ala\Documents\ala_civ_bots_prototype\src\main\java\dev\ensouled\EnsouledServer.java` | 2144 | `not computed` | policy, ledger |
| `R2303` | `C:\Users\ala\Documents\ala_civ_bots_prototype\src\main\java\dev\ensouled\axis\AxisGate.java` | 14477 | `not computed` | witness, civilians, cadence, policy, ledger |
| `R2304` | `C:\Users\ala\Documents\ala_civ_bots_prototype\src\main\java\dev\ensouled\axis\AxisProof.java` | 8694 | `not computed` | witness, cadence, policy, ledger |
| `R2305` | `C:\Users\ala\Documents\ala_civ_bots_prototype\src\main\java\dev\ensouled\axis\AxisVocabulary.java` | 9741 | `not computed` | policy |
| `R2306` | `C:\Users\ala\Documents\ala_civ_bots_prototype\src\main\java\dev\ensouled\axis\DecisionPackage.java` | 7359 | `not computed` | witness, civilians, cadence, client, policy, ledger |
| `R2307` | `C:\Users\ala\Documents\ala_civ_bots_prototype\src\main\java\dev\ensouled\body\BlockSight.java` | 7121 | `not computed` | client, policy |
| `R2308` | `C:\Users\ala\Documents\ala_civ_bots_prototype\src\main\java\dev\ensouled\body\BodyAdapter.java` | 1421 | `not computed` | cadence, client, policy |
| `R2309` | `C:\Users\ala\Documents\ala_civ_bots_prototype\src\main\java\dev\ensouled\body\CraftingExecutor.java` | 5095 | `not computed` | client, policy |
| `R2310` | `C:\Users\ala\Documents\ala_civ_bots_prototype\src\main\java\dev\ensouled\body\FakeClientConnection.java` | 1413 | `not computed` | cadence, client |
| `R2311` | `C:\Users\ala\Documents\ala_civ_bots_prototype\src\main\java\dev\ensouled\body\FileMotor.java` | 11615 | `not computed` | client, ledger |
| `R2312` | `C:\Users\ala\Documents\ala_civ_bots_prototype\src\main\java\dev\ensouled\body\MinecraftMotor.java` | 10987 | `not computed` | client, policy |
| `R2313` | `C:\Users\ala\Documents\ala_civ_bots_prototype\src\main\java\dev\ensouled\body\MinecraftWorldView.java` | 5222 | `not computed` | cadence, health, client, policy |
| `R2314` | `C:\Users\ala\Documents\ala_civ_bots_prototype\src\main\java\dev\ensouled\body\MobBodyAdapter.java` | 1854 | `not computed` | civilians, client |
| `R2315` | `C:\Users\ala\Documents\ala_civ_bots_prototype\src\main\java\dev\ensouled\body\NetworkPlayerBodyAdapter.java` | 22468 | `not computed` | client, policy |
| `R2316` | `C:\Users\ala\Documents\ala_civ_bots_prototype\src\main\java\dev\ensouled\body\NetworkWorldView.java` | 5687 | `not computed` | cadence, health, client, policy |
| `R2317` | `C:\Users\ala\Documents\ala_civ_bots_prototype\src\main\java\dev\ensouled\body\PlayerBodyAdapter.java` | 2412 | `not computed` | client |
| `R2318` | `C:\Users\ala\Documents\ala_civ_bots_prototype\src\main\java\dev\ensouled\body\PlayerMotor.java` | 19064 | `not computed` | civilians, cadence, client, policy |
| `R2319` | `C:\Users\ala\Documents\ala_civ_bots_prototype\src\main\java\dev\ensouled\body\PlayerWorldView.java` | 5664 | `not computed` | cadence, health, client, policy |
| `R2320` | `C:\Users\ala\Documents\ala_civ_bots_prototype\src\main\java\dev\ensouled\body\RecipeDiscovery.java` | 6790 | `not computed` | client |
| `R2321` | `C:\Users\ala\Documents\ala_civ_bots_prototype\src\main\java\dev\ensouled\client\EnsouledClient.java` | 6008 | `not computed` | cadence, client, policy |
| `R2322` | `C:\Users\ala\Documents\ala_civ_bots_prototype\src\main\java\dev\ensouled\client\StreamClient.java` | 16934 | `not computed` | witness, client, policy, ledger |
| `R2323` | `C:\Users\ala\Documents\ala_civ_bots_prototype\src\main\java\dev\ensouled\command\EnsouledCommands.java` | 45904 | `not computed` | witness, cadence, client, policy, ledger |
| `R2324` | `C:\Users\ala\Documents\ala_civ_bots_prototype\src\main\java\dev\ensouled\core\ActionEnvelope.java` | 1363 | `not computed` | policy |
| `R2325` | `C:\Users\ala\Documents\ala_civ_bots_prototype\src\main\java\dev\ensouled\core\Affect.java` | 6736 | `not computed` | witness, cadence, policy, ledger |
| `R2326` | `C:\Users\ala\Documents\ala_civ_bots_prototype\src\main\java\dev\ensouled\core\AgentMind.java` | 42749 | `not computed` | witness, cadence, health, client, policy, ledger |
| `R2327` | `C:\Users\ala\Documents\ala_civ_bots_prototype\src\main\java\dev\ensouled\core\AuthorityGateway.java` | 1931 | `not computed` | policy |
| `R2328` | `C:\Users\ala\Documents\ala_civ_bots_prototype\src\main\java\dev\ensouled\core\AxisReadings.java` | 2696 | `not computed` | policy |
| `R2329` | `C:\Users\ala\Documents\ala_civ_bots_prototype\src\main\java\dev\ensouled\core\BeliefStore.java` | 1869 | `not computed` | cadence |
| `R2330` | `C:\Users\ala\Documents\ala_civ_bots_prototype\src\main\java\dev\ensouled\core\BlockIds.java` | 978 | `not computed` | client |
| `R2331` | `C:\Users\ala\Documents\ala_civ_bots_prototype\src\main\java\dev\ensouled\core\CandidateGenerator.java` | 12762 | `not computed` | cadence, policy, ledger |
| `R2332` | `C:\Users\ala\Documents\ala_civ_bots_prototype\src\main\java\dev\ensouled\core\CanonicalEvent.java` | 872 | `not computed` | cadence |
| `R2333` | `C:\Users\ala\Documents\ala_civ_bots_prototype\src\main\java\dev\ensouled\core\CanonicalEventStore.java` | 1479 | `not computed` | cadence |
| `R2334` | `C:\Users\ala\Documents\ala_civ_bots_prototype\src\main\java\dev\ensouled\core\ChatTranscript.java` | 9152 | `not computed` | cadence |
| `R2335` | `C:\Users\ala\Documents\ala_civ_bots_prototype\src\main\java\dev\ensouled\core\Claim.java` | 1386 | `not computed` | witness |
| `R2336` | `C:\Users\ala\Documents\ala_civ_bots_prototype\src\main\java\dev\ensouled\core\ContinuityState.java` | 942 | `not computed` | policy |
| `R2337` | `C:\Users\ala\Documents\ala_civ_bots_prototype\src\main\java\dev\ensouled\core\DecisionJournal.java` | 7833 | `not computed` | cadence, policy, ledger |
| `R2338` | `C:\Users\ala\Documents\ala_civ_bots_prototype\src\main\java\dev\ensouled\core\DecisionRef.java` | 1091 | `not computed` | cadence, policy |
| `R2339` | `C:\Users\ala\Documents\ala_civ_bots_prototype\src\main\java\dev\ensouled\core\EntityStimulus.java` | 347 | `not computed` | health |
| `R2340` | `C:\Users\ala\Documents\ala_civ_bots_prototype\src\main\java\dev\ensouled\core\Episode.java` | 366 | `not computed` | cadence |
| `R2341` | `C:\Users\ala\Documents\ala_civ_bots_prototype\src\main\java\dev\ensouled\core\EpisodeKind.java` | 355 | `not computed` | policy |
| `R2342` | `C:\Users\ala\Documents\ala_civ_bots_prototype\src\main\java\dev\ensouled\core\EvidenceKind.java` | 149 | `not computed` | policy |
| `R2343` | `C:\Users\ala\Documents\ala_civ_bots_prototype\src\main\java\dev\ensouled\core\EvidenceLog.java` | 1501 | `not computed` | cadence |
| `R2344` | `C:\Users\ala\Documents\ala_civ_bots_prototype\src\main\java\dev\ensouled\core\EvidenceRecord.java` | 368 | `not computed` | cadence |
| `R2345` | `C:\Users\ala\Documents\ala_civ_bots_prototype\src\main\java\dev\ensouled\core\FrameLedger.java` | 6182 | `not computed` | cadence, ledger |
| `R2346` | `C:\Users\ala\Documents\ala_civ_bots_prototype\src\main\java\dev\ensouled\core\FrameParser.java` | 14585 | `not computed` | witness, cadence |
| `R2347` | `C:\Users\ala\Documents\ala_civ_bots_prototype\src\main\java\dev\ensouled\core\GateDecision.java` | 831 | `not computed` | policy |
| `R2348` | `C:\Users\ala\Documents\ala_civ_bots_prototype\src\main\java\dev\ensouled\core\Hearing.java` | 973 | `not computed` | cadence |
| `R2349` | `C:\Users\ala\Documents\ala_civ_bots_prototype\src\main\java\dev\ensouled\core\HumanChannel.java` | 860 | `not computed` | policy |
| `R2350` | `C:\Users\ala\Documents\ala_civ_bots_prototype\src\main\java\dev\ensouled\core\Humans.java` | 1348 | `not computed` | client |
| `R2351` | `C:\Users\ala\Documents\ala_civ_bots_prototype\src\main\java\dev\ensouled\core\InnerLife.java` | 4692 | `not computed` | witness, cadence, ledger |
| `R2352` | `C:\Users\ala\Documents\ala_civ_bots_prototype\src\main\java\dev\ensouled\core\Intention.java` | 2933 | `not computed` | policy |
| `R2353` | `C:\Users\ala\Documents\ala_civ_bots_prototype\src\main\java\dev\ensouled\core\LearnedRecipe.java` | 978 | `not computed` | cadence |
| `R2354` | `C:\Users\ala\Documents\ala_civ_bots_prototype\src\main\java\dev\ensouled\core\Lexicon.java` | 3743 | `not computed` | witness |
| `R2355` | `C:\Users\ala\Documents\ala_civ_bots_prototype\src\main\java\dev\ensouled\core\MessageBus.java` | 5939 | `not computed` | witness, cadence |
| `R2356` | `C:\Users\ala\Documents\ala_civ_bots_prototype\src\main\java\dev\ensouled\core\MessageEnvelope.java` | 5956 | `not computed` | cadence, client, policy, ledger |
| `R2357` | `C:\Users\ala\Documents\ala_civ_bots_prototype\src\main\java\dev\ensouled\core\MindLedger.java` | 9302 | `not computed` | witness, civilians, cadence, ledger |
| `R2358` | `C:\Users\ala\Documents\ala_civ_bots_prototype\src\main\java\dev\ensouled\core\MindPersistence.java` | 11454 | `not computed` | cadence, client, policy, ledger |
| `R2359` | `C:\Users\ala\Documents\ala_civ_bots_prototype\src\main\java\dev\ensouled\core\NeedsState.java` | 700 | `not computed` | health |
| `R2360` | `C:\Users\ala\Documents\ala_civ_bots_prototype\src\main\java\dev\ensouled\core\ObservationPackage.java` | 4754 | `not computed` | civilians, cadence, ledger |
| `R2361` | `C:\Users\ala\Documents\ala_civ_bots_prototype\src\main\java\dev\ensouled\core\Percept.java` | 1021 | `not computed` | cadence |
| `R2362` | `C:\Users\ala\Documents\ala_civ_bots_prototype\src\main\java\dev\ensouled\core\Phase1GatePolicy.java` | 10045 | `not computed` | witness, client, policy |
| `R2363` | `C:\Users\ala\Documents\ala_civ_bots_prototype\src\main\java\dev\ensouled\core\ProceduralGate.java` | 436 | `not computed` | policy |
| `R2364` | `C:\Users\ala\Documents\ala_civ_bots_prototype\src\main\java\dev\ensouled\core\ProseLines.java` | 2923 | `not computed` | policy |
| `R2365` | `C:\Users\ala\Documents\ala_civ_bots_prototype\src\main\java\dev\ensouled\core\ProseLogic.java` | 3521 | `not computed` | policy |
| `R2366` | `C:\Users\ala\Documents\ala_civ_bots_prototype\src\main\java\dev\ensouled\core\Realizer.java` | 3820 | `not computed` | witness |
| `R2367` | `C:\Users\ala\Documents\ala_civ_bots_prototype\src\main\java\dev\ensouled\core\ReflexLayer.java` | 1187 | `not computed` | policy |
| `R2368` | `C:\Users\ala\Documents\ala_civ_bots_prototype\src\main\java\dev\ensouled\core\ResidentNames.java` | 5947 | `not computed` | witness, policy |
| `R2369` | `C:\Users\ala\Documents\ala_civ_bots_prototype\src\main\java\dev\ensouled\core\SkillLineage.java` | 4896 | `not computed` | witness, cadence, ledger |
| `R2370` | `C:\Users\ala\Documents\ala_civ_bots_prototype\src\main\java\dev\ensouled\core\SkillRegistry.java` | 6884 | `not computed` | policy |
| `R2371` | `C:\Users\ala\Documents\ala_civ_bots_prototype\src\main\java\dev\ensouled\core\SkillRoutine.java` | 956 | `not computed` | cadence |
| `R2372` | `C:\Users\ala\Documents\ala_civ_bots_prototype\src\main\java\dev\ensouled\core\SkillStats.java` | 1012 | `not computed` | ledger |
| `R2373` | `C:\Users\ala\Documents\ala_civ_bots_prototype\src\main\java\dev\ensouled\core\SocialStream.java` | 5033 | `not computed` | cadence, policy, ledger |
| `R2374` | `C:\Users\ala\Documents\ala_civ_bots_prototype\src\main\java\dev\ensouled\core\SpeechInbox.java` | 1794 | `not computed` | cadence |
| `R2375` | `C:\Users\ala\Documents\ala_civ_bots_prototype\src\main\java\dev\ensouled\core\StateNode.java` | 2373 | `not computed` | client |
| `R2376` | `C:\Users\ala\Documents\ala_civ_bots_prototype\src\main\java\dev\ensouled\core\StreamNotices.java` | 2719 | `not computed` | policy |
| `R2377` | `C:\Users\ala\Documents\ala_civ_bots_prototype\src\main\java\dev\ensouled\core\Supplies.java` | 2314 | `not computed` | client |
| `R2378` | `C:\Users\ala\Documents\ala_civ_bots_prototype\src\main\java\dev\ensouled\core\Talk.java` | 4087 | `not computed` | policy |
| `R2379` | `C:\Users\ala\Documents\ala_civ_bots_prototype\src\main\java\dev\ensouled\core\TrainingLedger.java` | 20843 | `not computed` | witness, cadence, client, policy, ledger |
| `R2380` | `C:\Users\ala\Documents\ala_civ_bots_prototype\src\main\java\dev\ensouled\core\VerbFrame.java` | 3689 | `not computed` | witness, cadence, ledger |
| `R2381` | `C:\Users\ala\Documents\ala_civ_bots_prototype\src\main\java\dev\ensouled\core\VerbLibrary.java` | 5027 | `not computed` | witness |
| `R2382` | `C:\Users\ala\Documents\ala_civ_bots_prototype\src\main\java\dev\ensouled\core\Voice.java` | 5219 | `not computed` | witness, cadence, policy, ledger |
| `R2383` | `C:\Users\ala\Documents\ala_civ_bots_prototype\src\main\java\dev\ensouled\core\Wishes.java` | 3838 | `not computed` | cadence, policy |
| `R2384` | `C:\Users\ala\Documents\ala_civ_bots_prototype\src\main\java\dev\ensouled\core\WorldView.java` | 1734 | `not computed` | cadence |
| `R2385` | `C:\Users\ala\Documents\ala_package_designer\Cargo.toml` | 3754 | `not computed` | policy |
| `R2386` | `C:\Users\ala\Documents\ala_package_designer\clean-room-architecture-and-agent-fidelity.md` | 46732 | `not computed` | civilians, cadence, client, policy, ledger |
| `R2387` | `C:\Users\ala\Documents\ala_package_designer\crates\foundry-appearance\src\lib.rs` | 1622 | `not computed` | policy |
| `R2388` | `C:\Users\ala\Documents\ala_package_designer\crates\foundry-appearance\src\look.rs` | 21943 | `not computed` | policy |
| `R2389` | `C:\Users\ala\Documents\ala_package_designer\crates\foundry-appearance\src\openpbr.rs` | 9891 | `not computed` | policy |
| `R2390` | `C:\Users\ala\Documents\ala_package_designer\crates\foundry-axis\src\gate.rs` | 16799 | `not computed` | policy |
| `R2391` | `C:\Users\ala\Documents\ala_package_designer\crates\foundry-axis\src\grant.rs` | 11059 | `not computed` | policy |
| `R2392` | `C:\Users\ala\Documents\ala_package_designer\crates\foundry-axis\src\ladder.rs` | 12475 | `not computed` | policy |
| `R2393` | `C:\Users\ala\Documents\ala_package_designer\crates\foundry-axis\src\lib.rs` | 6092 | `not computed` | witness, civilians, policy |
| `R2394` | `C:\Users\ala\Documents\ala_package_designer\crates\foundry-axis\src\presenter.rs` | 17384 | `not computed` | witness, policy, ledger |
| `R2395` | `C:\Users\ala\Documents\ala_package_designer\crates\foundry-axis\src\profile.rs` | 4248 | `not computed` | policy |
| `R2396` | `C:\Users\ala\Documents\ala_package_designer\crates\foundry-axis\src\witness.rs` | 6052 | `not computed` | witness, policy |
| `R2397` | `C:\Users\ala\Documents\ala_package_designer\crates\foundry-core\Cargo.toml` | 515 | `not computed` | policy |
| `R2398` | `C:\Users\ala\Documents\ala_package_designer\crates\foundry-core\src\digest.rs` | 3052 | `not computed` | policy, ledger |
| `R2399` | `C:\Users\ala\Documents\ala_package_designer\crates\foundry-core\src\lib.rs` | 2032 | `not computed` | witness, policy, ledger |
| `R2400` | `C:\Users\ala\Documents\ala_package_designer\crates\foundry-core\src\refusal.rs` | 10831 | `not computed` | cadence, health, format, policy |
| `R2401` | `C:\Users\ala\Documents\ala_package_designer\crates\foundry-core\src\subject.rs` | 12128 | `not computed` | witness, civilians, health, policy |
| `R2402` | `C:\Users\ala\Documents\ala_package_designer\crates\foundry-designer\Cargo.toml` | 1627 | `not computed` | policy |
| `R2403` | `C:\Users\ala\Documents\ala_package_designer\crates\foundry-designer\src\chat.rs` | 16216 | `not computed` | policy, ledger |
| `R2404` | `C:\Users\ala\Documents\ala_package_designer\crates\foundry-designer\src\command.rs` | 11117 | `not computed` | witness, civilians, policy |
| `R2405` | `C:\Users\ala\Documents\ala_package_designer\crates\foundry-designer\src\draft.rs` | 13367 | `not computed` | witness, civilians, policy |
| `R2406` | `C:\Users\ala\Documents\ala_package_designer\crates\foundry-designer\src\lib.rs` | 2582 | `not computed` | civilians, policy |
| `R2407` | `C:\Users\ala\Documents\ala_package_designer\crates\foundry-designer\src\main.rs` | 7388 | `not computed` | policy |
| `R2408` | `C:\Users\ala\Documents\ala_package_designer\crates\foundry-designer\src\screen.rs` | 20987 | `not computed` | witness, civilians, format, policy, ledger |
| `R2409` | `C:\Users\ala\Documents\ala_package_designer\crates\foundry-designer\src\session.rs` | 55356 | `not computed` | witness, civilians, format, policy, ledger |
| `R2410` | `C:\Users\ala\Documents\ala_package_designer\crates\foundry-designer\src\theme.rs` | 13959 | `not computed` | policy |
| `R2411` | `C:\Users\ala\Documents\ala_package_designer\crates\foundry-designer\src\bin\mute-server.rs` | 4212 | `not computed` | ledger |
| `R2412` | `C:\Users\ala\Documents\ala_package_designer\crates\foundry-designer\tests\designer.rs` | 23801 | `not computed` | witness, format, policy, ledger |
| `R2413` | `C:\Users\ala\Documents\ala_package_designer\crates\foundry-designer\tests\mcp_chat.rs` | 29637 | `not computed` | witness, policy, ledger |
| `R2414` | `C:\Users\ala\Documents\ala_package_designer\crates\foundry-engine\Cargo.toml` | 621 | `not computed` | cadence, health, policy |
| `R2415` | `C:\Users\ala\Documents\ala_package_designer\crates\foundry-engine\examples\calibrate.rs` | 3884 | `not computed` | policy |
| `R2416` | `C:\Users\ala\Documents\ala_package_designer\crates\foundry-engine\src\corpus.rs` | 15111 | `not computed` | policy |
| `R2417` | `C:\Users\ala\Documents\ala_package_designer\crates\foundry-engine\src\lib.rs` | 20933 | `not computed` | cadence, health, policy |
| `R2418` | `C:\Users\ala\Documents\ala_package_designer\crates\foundry-format\src\frame.rs` | 12269 | `not computed` | format, policy, ledger |
| `R2419` | `C:\Users\ala\Documents\ala_package_designer\crates\foundry-format\src\lib.rs` | 4093 | `not computed` | format, policy |
| `R2420` | `C:\Users\ala\Documents\ala_package_designer\crates\foundry-format\src\recipe.rs` | 64277 | `not computed` | witness, civilians, policy, ledger |
| `R2421` | `C:\Users\ala\Documents\ala_package_designer\crates\foundry-format\tests\corpus.rs` | 9978 | `not computed` | format, policy |
| `R2422` | `C:\Users\ala\Documents\ala_package_designer\crates\foundry-format\tests\grammar.rs` | 18405 | `not computed` | witness, policy, ledger |
| `R2423` | `C:\Users\ala\Documents\ala_package_designer\crates\foundry-laya\Cargo.toml` | 923 | `not computed` | policy |
| `R2424` | `C:\Users\ala\Documents\ala_package_designer\crates\foundry-laya\examples\calibrate_laya.rs` | 5126 | `not computed` | policy |
| `R2425` | `C:\Users\ala\Documents\ala_package_designer\crates\foundry-laya\examples\probe_laya.rs` | 12148 | `not computed` | policy |
| `R2426` | `C:\Users\ala\Documents\ala_package_designer\crates\foundry-laya\src\lib.rs` | 9693 | `not computed` | policy |
| `R2427` | `C:\Users\ala\Documents\ala_package_designer\crates\foundry-mcp\Cargo.toml` | 696 | `not computed` | witness, policy |
| `R2428` | `C:\Users\ala\Documents\ala_package_designer\crates\foundry-mcp\src\client.rs` | 8341 | `not computed` | policy, ledger |
| `R2429` | `C:\Users\ala\Documents\ala_package_designer\crates\foundry-mcp\src\door.rs` | 28738 | `not computed` | witness, policy, ledger |
| `R2430` | `C:\Users\ala\Documents\ala_package_designer\crates\foundry-mcp\src\json.rs` | 20074 | `not computed` | policy |
| `R2431` | `C:\Users\ala\Documents\ala_package_designer\crates\foundry-mcp\src\lib.rs` | 3086 | `not computed` | witness, policy, ledger |
| `R2432` | `C:\Users\ala\Documents\ala_package_designer\crates\foundry-mcp\src\predicate.rs` | 27312 | `not computed` | witness, health, policy, ledger |
| `R2433` | `C:\Users\ala\Documents\ala_package_designer\crates\foundry-mcp\src\protocol.rs` | 8660 | `not computed` | policy |
| `R2434` | `C:\Users\ala\Documents\ala_package_designer\crates\foundry-mcp\src\record.rs` | 31492 | `not computed` | policy, ledger |
| `R2435` | `C:\Users\ala\Documents\ala_package_designer\crates\foundry-mcp\src\server.rs` | 62835 | `not computed` | witness, policy, ledger |
| `R2436` | `C:\Users\ala\Documents\ala_package_designer\crates\foundry-mcp\src\tool.rs` | 16167 | `not computed` | policy |
| `R2437` | `C:\Users\ala\Documents\ala_package_designer\crates\foundry-mcp\src\bin\foundry-mcp-server.rs` | 1007 | `not computed` | policy |
| `R2438` | `C:\Users\ala\Documents\ala_package_designer\crates\foundry-mcp\tests\door.rs` | 52263 | `not computed` | witness, health, policy, ledger |
| `R2439` | `C:\Users\ala\Documents\ala_package_designer\crates\foundry-mesh\src\hyper.rs` | 19257 | `not computed` | policy |
| `R2440` | `C:\Users\ala\Documents\ala_package_designer\crates\foundry-mesh\src\polygon.rs` | 14811 | `not computed` | policy |
| `R2441` | `C:\Users\ala\Documents\ala_package_designer\crates\foundry-shell\build.rs` | 6598 | `not computed` | policy |
| `R2442` | `C:\Users\ala\Documents\ala_package_designer\crates\foundry-shell\Cargo.toml` | 1640 | `not computed` | policy |
| `R2443` | `C:\Users\ala\Documents\ala_package_designer\crates\foundry-shell\src\base64.rs` | 6312 | `not computed` | policy |
| `R2444` | `C:\Users\ala\Documents\ala_package_designer\crates\foundry-shell\src\host.rs` | 32246 | `not computed` | policy |
| `R2445` | `C:\Users\ala\Documents\ala_package_designer\crates\foundry-shell\src\lib.rs` | 5421 | `not computed` | policy, ledger |
| `R2446` | `C:\Users\ala\Documents\ala_package_designer\crates\foundry-shell\src\seam.rs` | 10290 | `not computed` | policy |
| `R2447` | `C:\Users\ala\Documents\ala_package_designer\crates\foundry-shell\src\state.rs` | 54415 | `not computed` | witness, policy, ledger |
| `R2448` | `C:\Users\ala\Documents\ala_package_designer\crates\foundry-shell\src\watch.rs` | 9556 | `not computed` | cadence, policy |
| `R2449` | `C:\Users\ala\Documents\ala_package_designer\crates\foundry-shell\src\wire.rs` | 26736 | `not computed` | policy, ledger |
| `R2450` | `C:\Users\ala\Documents\ala_package_designer\crates\foundry-shell\src\xz.rs` | 8984 | `not computed` | policy |
| `R2451` | `C:\Users\ala\Documents\ala_package_designer\crates\foundry-shell\src\bin\stand-in.rs` | 9959 | `not computed` | policy, ledger |
| `R2452` | `C:\Users\ala\Documents\ala_package_designer\crates\foundry-shell\tests\reload.rs` | 9077 | `not computed` | cadence, policy |
| `R2453` | `C:\Users\ala\Documents\ala_package_designer\crates\foundry-shell\tests\seam.rs` | 15623 | `not computed` | policy, ledger |
| `R2454` | `C:\Users\ala\Documents\ala_package_designer\crates\foundry-von\Cargo.toml` | 1133 | `not computed` | policy |
| `R2455` | `C:\Users\ala\Documents\ala_package_designer\crates\foundry-von\examples\compare_instruments.rs` | 6282 | `not computed` | policy |
| `R2456` | `C:\Users\ala\Documents\ala_package_designer\crates\foundry-von\src\lib.rs` | 11105 | `not computed` | policy |
| `R2457` | `C:\Users\ala\Documents\ala_package_designer\docs\calibration.md` | 10094 | `not computed` | cadence, health, policy |
| `R2458` | `C:\Users\ala\Documents\ala_package_designer\docs\shell-seam.md` | 27277 | `not computed` | policy, ledger |
| `R2459` | `C:\Users\ala\Documents\ala_package_designer\vendor\esaxx-rs\build.rs` | 938 | `not computed` | policy |
| `R2460` | `C:\Users\ala\Documents\agent_god_files\launch.ps1` | 1856 | `not computed` | civilians |
| `R2461` | `C:\Users\ala\Documents\agent_god_files\world.json` | 2878 | `not computed` | civilians |
| `R2462` | `C:\Users\ala\Documents\agent_god_files\civ_logic\decisions\cities-citizens-build.md` | 7243 | `not computed` | civilians, cadence, policy, ledger |
| `R2463` | `C:\Users\ala\Documents\agent_god_files\civ_logic\decisions\cities-evidence.md` | 19186 | `not computed` | cadence, policy, ledger |
| `R2464` | `C:\Users\ala\Documents\agent_god_files\civ_logic\decisions\DECISION-cities-events.md` | 3268 | `not computed` | policy, ledger |
| `R2465` | `C:\Users\ala\Documents\agent_god_files\civ_logic\src\appearance.rs` | 10200 | `not computed` | policy |
| `R2466` | `C:\Users\ala\Documents\agent_god_files\civ_logic\src\civilian.rs` | 26041 | `not computed` | civilians, cadence, health, policy, ledger |
| `R2467` | `C:\Users\ala\Documents\agent_god_files\civ_logic\src\composition.rs` | 5085 | `not computed` | policy |
| `R2468` | `C:\Users\ala\Documents\agent_god_files\civ_logic\src\detail.rs` | 11122 | `not computed` | policy |
| `R2469` | `C:\Users\ala\Documents\agent_god_files\civ_logic\src\food.rs` | 27822 | `not computed` | policy |
| `R2470` | `C:\Users\ala\Documents\agent_god_files\civ_logic\src\forms.rs` | 12025 | `not computed` | policy |
| `R2471` | `C:\Users\ala\Documents\agent_god_files\civ_logic\src\intake.rs` | 8940 | `not computed` | cadence, policy |
| `R2472` | `C:\Users\ala\Documents\agent_god_files\civ_logic\src\judge.rs` | 8611 | `not computed` | policy |
| `R2473` | `C:\Users\ala\Documents\agent_god_files\civ_logic\src\ledger.rs` | 4234 | `not computed` | cadence, ledger |
| `R2474` | `C:\Users\ala\Documents\agent_god_files\civ_logic\src\lib.rs` | 743 | `not computed` | civilians, ledger |
| `R2475` | `C:\Users\ala\Documents\agent_god_files\civ_logic\src\look.rs` | 6974 | `not computed` | civilians |
| `R2476` | `C:\Users\ala\Documents\agent_god_files\civ_logic\src\materials.rs` | 42919 | `not computed` | policy, ledger |
| `R2477` | `C:\Users\ala\Documents\agent_god_files\civ_logic\src\mesh.rs` | 33472 | `not computed` | policy, ledger |
| `R2478` | `C:\Users\ala\Documents\agent_god_files\civ_logic\src\norms.rs` | 8279 | `not computed` | civilians, policy |
| `R2479` | `C:\Users\ala\Documents\agent_god_files\civ_logic\src\npr.rs` | 12676 | `not computed` | policy |
| `R2480` | `C:\Users\ala\Documents\agent_god_files\civ_logic\src\openpbr.rs` | 12631 | `not computed` | policy |
| `R2481` | `C:\Users\ala\Documents\agent_god_files\civ_logic\src\response.rs` | 5408 | `not computed` | policy |
| `R2482` | `C:\Users\ala\Documents\agent_god_files\civ_logic\src\scale.rs` | 2004 | `not computed` | civilians |
| `R2483` | `C:\Users\ala\Documents\agent_god_files\civ_logic\src\shapers.rs` | 25908 | `not computed` | policy |
| `R2484` | `C:\Users\ala\Documents\agent_god_files\civ_logic\src\sim.rs` | 53414 | `not computed` | civilians, cadence, policy, ledger |
| `R2485` | `C:\Users\ala\Documents\agent_god_files\civ_logic\src\sky.rs` | 22251 | `not computed` | policy |
| `R2486` | `C:\Users\ala\Documents\agent_god_files\civ_logic\src\terrain.rs` | 3291 | `not computed` | civilians |
| `R2487` | `C:\Users\ala\Documents\agent_god_files\civ_logic\src\von.rs` | 6430 | `not computed` | civilians |
| `R2488` | `C:\Users\ala\Documents\agent_god_files\civ_logic\src\voxel_model.rs` | 3565 | `not computed` | policy |
| `R2489` | `C:\Users\ala\Documents\agent_god_files\civ_logic\src\bin\founding.rs` | 13834 | `not computed` | cadence, policy, ledger |
| `R2490` | `C:\Users\ala\Documents\agent_god_files\civ_logic\src\bin\headless.rs` | 7307 | `not computed` | civilians, cadence, policy, ledger |
| `R2491` | `C:\Users\ala\Documents\agent_god_files\civ_logic\src\bin\hostile.rs` | 40336 | `not computed` | cadence, policy, ledger |
| `R2492` | `C:\Users\ala\Documents\agent_god_files\civ_logic\src\cities\author.rs` | 25235 | `not computed` | civilians, cadence, health, policy, ledger |
| `R2493` | `C:\Users\ala\Documents\agent_god_files\civ_logic\src\cities\economy.rs` | 13889 | `not computed` | policy |
| `R2494` | `C:\Users\ala\Documents\agent_god_files\civ_logic\src\cities\inspect.rs` | 14914 | `not computed` | cadence, ledger |
| `R2495` | `C:\Users\ala\Documents\agent_god_files\civ_logic\src\cities\mod.rs` | 3380 | `not computed` | cadence, policy, ledger |
| `R2496` | `C:\Users\ala\Documents\agent_god_files\civ_logic\src\cities\roads.rs` | 11116 | `not computed` | policy |
| `R2497` | `C:\Users\ala\Documents\agent_god_files\civ_logic\src\cities\store.rs` | 19812 | `not computed` | cadence, policy, ledger |
| `R2498` | `C:\Users\ala\Documents\agent_god_files\civ_logic\src\cities\verbs.rs` | 25297 | `not computed` | cadence, policy, ledger |
| `R2499` | `C:\Users\ala\Documents\agent_god_files\civ_logic\src\cities\voxel.rs` | 19048 | `not computed` | format, policy, ledger |
| `R2500` | `C:\Users\ala\Documents\agent_god_files\civ_logic\src\cities\world.rs` | 47054 | `not computed` | civilians, cadence, health, policy, ledger |
| `R2501` | `C:\Users\ala\Documents\agent_god_files\civ_world\repair\repair_pass2.py` | 9391 | `not computed` | civilians |
| `R2502` | `C:\Users\ala\Documents\agent_god_files\civ_world\repair\repair_pass3.py` | 1383 | `not computed` | civilians |
| `R2503` | `C:\Users\ala\Documents\agent_god_files\civ_world\src\main.rs` | 77954 | `not computed` | civilians, cadence, policy, ledger |
| `R2504` | `C:\Users\ala\Documents\agent_god_files\civ_world\src\stream.rs` | 7162 | `not computed` | policy |
| `R2505` | `C:\Users\ala\Documents\agent_god_files\injest\Feeling.md` | 25659 | `not computed` | health, policy |
| `R2506` | `C:\Users\ala\Documents\agent_god_files\prose_logic\README.md` | 2284 | `not computed` | ledger |
| `R2507` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_1_CHRONICLES.md` | 359477 | `not computed` | policy |
| `R2508` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_1_CORINTHIANS.md` | 235643 | `not computed` | witness |
| `R2509` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_1_CORINTHIANS_15.md` | 28808 | `not computed` | witness |
| `R2510` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_1_JOHN.md` | 85847 | `not computed` | witness, health |
| `R2511` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_1_JOHN_1.md` | 5584 | `not computed` | witness |
| `R2512` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_1_JOHN_5.md` | 11930 | `not computed` | witness |
| `R2513` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_1_KINGS.md` | 379600 | `not computed` | witness, policy |
| `R2514` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_1_KINGS_17.md` | 14840 | `not computed` | policy |
| `R2515` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_1_KINGS_20.md` | 28279 | `not computed` | policy |
| `R2516` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_1_KINGS_21.md` | 18251 | `not computed` | witness, policy |
| `R2517` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_1_KINGS_22.md` | 35918 | `not computed` | policy |
| `R2518` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_1_KINGS_29.md` | 15651 | `not computed` | policy |
| `R2519` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_1_KINGS_30.md` | 18589 | `not computed` | witness, policy |
| `R2520` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_1_KINGS_31.md` | 36426 | `not computed` | policy |
| `R2521` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_1_PETER.md` | 50173 | `not computed` | witness |
| `R2522` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_1_PETER_5.md` | 7265 | `not computed` | witness |
| `R2523` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_1_SAMUEL.md` | 401979 | `not computed` | witness, policy |
| `R2524` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_1_SAMUEL_12.md` | 16922 | `not computed` | witness |
| `R2525` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_1_SAMUEL_15.md` | 22375 | `not computed` | policy |
| `R2526` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_1_SAMUEL_16.md` | 14216 | `not computed` | policy |
| `R2527` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_1_SAMUEL_21.md` | 12604 | `not computed` | witness, policy |
| `R2528` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_1_SAMUEL_28.md` | 17270 | `not computed` | policy |
| `R2529` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_1_SAMUEL_38.md` | 17304 | `not computed` | policy |
| `R2530` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_1_SAMUEL_4.md` | 17566 | `not computed` | policy |
| `R2531` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_1_SAMUEL_8.md` | 14030 | `not computed` | policy |
| `R2532` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_1_SAMUEL_9.md` | 19663 | `not computed` | policy |
| `R2533` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_1_THESSALONIANS.md` | 44985 | `not computed` | witness |
| `R2534` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_1_THESSALONIANS_2.md` | 8290 | `not computed` | witness |
| `R2535` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_1_TIMOTHY.md` | 60811 | `not computed` | witness, policy |
| `R2536` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_1_TIMOTHY_4.md` | 8420 | `not computed` | policy |
| `R2537` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_1_TIMOTHY_5.md` | 13632 | `not computed` | witness, policy |
| `R2538` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_1_TIMOTHY_6.md` | 11752 | `not computed` | witness |
| `R2539` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_2_CHRONICLES.md` | 398394 | `not computed` | witness, policy |
| `R2540` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_2_CORINTHIANS.md` | 141289 | `not computed` | witness |
| `R2541` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_2_CORINTHIANS_13.md` | 8295 | `not computed` | witness |
| `R2542` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_2_KINGS.md` | 361741 | `not computed` | policy |
| `R2543` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_2_KINGS_10.md` | 23920 | `not computed` | policy |
| `R2544` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_2_KINGS_101.md` | 22863 | `not computed` | policy |
| `R2545` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_2_KINGS_102.md` | 16483 | `not computed` | policy |
| `R2546` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_2_KINGS_104.md` | 19332 | `not computed` | policy |
| `R2547` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_2_KINGS_11.md` | 16522 | `not computed` | policy |
| `R2548` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_2_KINGS_14.md` | 19755 | `not computed` | policy |
| `R2549` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_2_KINGS_15.md` | 25358 | `not computed` | policy |
| `R2550` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_2_KINGS_23.md` | 26537 | `not computed` | policy |
| `R2551` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_2_KINGS_25.md` | 20052 | `not computed` | policy |
| `R2552` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_2_KINGS_34.md` | 25070 | `not computed` | policy |
| `R2553` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_2_KINGS_36.md` | 24557 | `not computed` | policy |
| `R2554` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_2_KINGS_41.md` | 21727 | `not computed` | policy |
| `R2555` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_2_KINGS_44.md` | 15549 | `not computed` | policy |
| `R2556` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_2_KINGS_5.md` | 21986 | `not computed` | policy |
| `R2557` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_2_KINGS_51.md` | 19511 | `not computed` | policy |
| `R2558` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_2_KINGS_62.md` | 11278 | `not computed` | policy |
| `R2559` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_2_KINGS_7.md` | 12760 | `not computed` | policy |
| `R2560` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_2_KINGS_72.md` | 23087 | `not computed` | policy |
| `R2561` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_2_KINGS_77.md` | 15362 | `not computed` | policy |
| `R2562` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_2_KINGS_78.md` | 18891 | `not computed` | witness, policy |
| `R2563` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_2_KINGS_79.md` | 21036 | `not computed` | policy |
| `R2564` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_2_KINGS_80.md` | 16755 | `not computed` | policy |
| `R2565` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_2_KINGS_81.md` | 5352 | `not computed` | policy |
| `R2566` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_2_KINGS_86.md` | 22034 | `not computed` | policy |
| `R2567` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_2_KINGS_87.md` | 15739 | `not computed` | policy |
| `R2568` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_2_KINGS_89.md` | 18941 | `not computed` | policy |
| `R2569` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_2_KINGS_9.md` | 24616 | `not computed` | policy |
| `R2570` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_2_KINGS_92.md` | 15399 | `not computed` | policy |
| `R2571` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_2_KINGS_93.md` | 19657 | `not computed` | witness, policy |
| `R2572` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_2_KINGS_94.md` | 21371 | `not computed` | policy |
| `R2573` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_2_KINGS_95.md` | 17491 | `not computed` | policy |
| `R2574` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_2_KINGS_96.md` | 5681 | `not computed` | policy |
| `R2575` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_2_PETER.md` | 32366 | `not computed` | witness |
| `R2576` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_2_PETER_1.md` | 10222 | `not computed` | witness |
| `R2577` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_2_SAMUEL.md` | 323958 | `not computed` | health, policy |
| `R2578` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_2_SAMUEL_10.md` | 12048 | `not computed` | policy |
| `R2579` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_2_SAMUEL_11.md` | 17977 | `not computed` | policy |
| `R2580` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_2_SAMUEL_13.md` | 28758 | `not computed` | policy |
| `R2581` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_2_SAMUEL_15.md` | 23112 | `not computed` | policy |
| `R2582` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_2_SAMUEL_18.md` | 24344 | `not computed` | policy |
| `R2583` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_2_SAMUEL_19.md` | 29670 | `not computed` | policy |
| `R2584` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_2_SAMUEL_2.md` | 21066 | `not computed` | policy |
| `R2585` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_2_SAMUEL_20.md` | 16470 | `not computed` | health |
| `R2586` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_2_SAMUEL_23.md` | 17876 | `not computed` | policy |
| `R2587` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_2_SAMUEL_25.md` | 13491 | `not computed` | policy |
| `R2588` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_2_SAMUEL_26.md` | 11698 | `not computed` | policy |
| `R2589` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_2_SAMUEL_27.md` | 10514 | `not computed` | policy |
| `R2590` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_2_SAMUEL_29.md` | 16812 | `not computed` | health |
| `R2591` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_2_SAMUEL_3.md` | 27106 | `not computed` | policy |
| `R2592` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_2_SAMUEL_32.md` | 18296 | `not computed` | policy |
| `R2593` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_2_TIMOTHY.md` | 41806 | `not computed` | witness |
| `R2594` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_2_TIMOTHY_2.md` | 13198 | `not computed` | witness |
| `R2595` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_3_JOHN_1.md` | 7518 | `not computed` | witness, health |
| `R2596` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_939.md` | 1437 | `not computed` | policy |
| `R2597` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_942.md` | 2593 | `not computed` | policy |
| `R2598` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_946.md` | 2986 | `not computed` | witness |
| `R2599` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_AB_BY_GL_KHNU_N_JWEI__1___655_2__SORIT__BGQ_KBIR_JI.md` | 3748 | `not computed` | format |
| `R2600` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_AB_MN_JWGQ_RHU_RY_BWEI____339_11__GAUVI__BGQ_KBIR_JI.md` | 2867 | `not computed` | policy |
| `R2601` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_AB_SWDU_SMIG_PRIAW____746_7__SUHI__M__5.md` | 9012 | `not computed` | policy |
| `R2602` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_ACCORDING_TO_THE_KARMA_OF_PAST_ACTIONS__PEOPLE_DESCEND_TO_THE_DEPTHS_OR_RISE_TO.md` | 4940 | `not computed` | policy |
| `R2603` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_ACTS.md` | 493078 | `not computed` | witness, health, policy |
| `R2604` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_ACTS_1.md` | 12891 | `not computed` | witness |
| `R2605` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_ACTS_10.md` | 23464 | `not computed` | witness, policy |
| `R2606` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_ACTS_12.md` | 15077 | `not computed` | policy |
| `R2607` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_ACTS_13.md` | 27429 | `not computed` | witness |
| `R2608` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_ACTS_14.md` | 13177 | `not computed` | witness |
| `R2609` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_ACTS_15.md` | 20295 | `not computed` | witness |
| `R2610` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_ACTS_2.md` | 20954 | `not computed` | witness |
| `R2611` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_ACTS_20.md` | 19630 | `not computed` | witness |
| `R2612` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_ACTS_22.md` | 16037 | `not computed` | witness |
| `R2613` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_ACTS_23.md` | 19877 | `not computed` | witness |
| `R2614` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_ACTS_25.md` | 14847 | `not computed` | policy |
| `R2615` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_ACTS_26.md` | 15299 | `not computed` | witness |
| `R2616` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_ACTS_27.md` | 23638 | `not computed` | health |
| `R2617` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_ACTS_3.md` | 14499 | `not computed` | witness, policy |
| `R2618` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_ACTS_4.md` | 17907 | `not computed` | witness |
| `R2619` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_ACTS_5.md` | 21920 | `not computed` | witness |
| `R2620` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_ACTS_6.md` | 7446 | `not computed` | witness |
| `R2621` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_ACTS_7.md` | 29474 | `not computed` | witness, policy |
| `R2622` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_AFTER_CAREFUL_THOUGHT__VYAASA_SPOKE_THE_SUPREME_TRUTH__THAT_THERE_IS_NOTHING_EQU.md` | 14242 | `not computed` | policy |
| `R2623` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_AGH_GHY_GIH_GGN_RHWEI__9___340_12__GAUVI_PURBI__BGQ_KBIR_JI.md` | 983 | `not computed` | policy |
| `R2624` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_AIHINIS_JIAW_DYIK_SMWLY_IQS_HI_KI_SRKWRW__1___1331_17__PRBWQI__M__1.md` | 5620 | `not computed` | policy |
| `R2625` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_AIHINIS_RHY_EYK_ILV_LWGI_SWCY_DYIK_PQIXW__1__RHWAU____907_7__RWMKLI_DKXI__M__1.md` | 8053 | `not computed` | policy |
| `R2626` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_AINK_JLW_JY_DOVY_DYHI____200_1__GAUVI__M__5.md` | 6797 | `not computed` | policy |
| `R2627` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_AINK_RUP_RMG_BOG_RSY____890_18__RWMKLI__M__5.md` | 6475 | `not computed` | health |
| `R2628` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_AJON_N_PQ_WIE_INGM_BEY_SWKI__3___710_17__JYQSRI__BGQ_RIVDWS_JI.md` | 7107 | `not computed` | witness |
| `R2629` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_AJRU_JRY_SU_INJRU_JRY____974_15__RWMKLI__BGQ_BYXI_JI.md` | 5680 | `not computed` | policy |
| `R2630` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_AKR_IBRK_BWG_BUIE_COKI_ISMICQ_BWAU_KRYHI____354_17__AWSW__M__1.md` | 4858 | `not computed` | policy |
| `R2631` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_ALWAYS_AFFLICTED_WITH_THE_DARK_PASSIONS_OF_LOW_ENERGY__IT_WANDERS_AROUND__PASSIN.md` | 5069 | `not computed` | policy |
| `R2632` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_AMIMRQU_LY_LY_NIMU_ISMCWEI____481_6__AWSW__BGQ_KBIR_JI.md` | 1602 | `not computed` | policy |
| `R2633` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_AMIMRQ_DWR_GGIN_DS_DUAWIR____153_9__GAUVI__M__1.md` | 3333 | `not computed` | policy |
| `R2634` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_AMIMRQ_NWMU_QUMWRW_SUAWMI____1074_16__MWRU__M__5.md` | 11136 | `not computed` | policy |
| `R2635` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_AMIMRQ_RSU_SIQGURU_CUAWIEAW____1069_11__MWRU__M__4.md` | 2047 | `not computed` | policy |
| `R2636` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_AMIMRQ_SBID_NWMU_VKWXY____361_8__AWSW__M__3.md` | 5560 | `not computed` | policy |
| `R2637` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_AMIQ_SKWEI_PWIEAW_JN_MUKIQ_DUAWRW__7___422_15__AWSW__M__1.md` | 1507 | `not computed` | policy |
| `R2638` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_AMLU_KIR_DRQI_BIJU_SBDO_KIR_SC_KI_AWB_INQ_DYIH_PWXI____24_1__ISRIRWGU__M__1.md` | 3109 | `not computed` | policy |
| `R2639` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_AMOS.md` | 67775 | `not computed` | policy |
| `R2640` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_AMOS_5.md` | 14136 | `not computed` | policy |
| `R2641` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_AMOS_8.md` | 9770 | `not computed` | policy |
| `R2642` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_AMQRJWMI_RWMU_SMWRHU____343_6__GAUVI_IQQM_I__BGQ_KBIR_JI.md` | 1514 | `not computed` | policy |
| `R2643` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_AMQU_N_PWVIH_VFY_VFYRY____1033_7__MWRU__M__1.md` | 3298 | `not computed` | policy |
| `R2644` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_AMRU_AFOLU_APWRU_AMOLKU_HIR_ASIQR_QWIN_SUHWIEAW__2___1039_16__MWRU__M__1.md` | 7643 | `not computed` | policy |
| `R2645` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_AND_ONE_WHO_LIVES_IN_THE_MANSION_OF_THE_LORD_S_PRESENCE__WHY_SHOULD_HE_BOW_DOWN.md` | 1508 | `not computed` | policy |
| `R2646` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_ANHD_SBDU_DSM_DUAWIR_VIJE_QH_AMIMRQ_NWMU_CUAWIEAW_QW__2___1002_6__MWRU__M__5.md` | 3881 | `not computed` | policy |
| `R2647` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_ANIDNU_AWRJW_ICJDI_JWEY____1061_3__MWRU__M__3.md` | 2755 | `not computed` | witness |
| `R2648` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_ANIDNU_BGIQ_KRIH_GUR_AWGY_GUR_KY_SBID_SVWRY__1___1199_3__SWRMG__M__4.md` | 9181 | `not computed` | policy |
| `R2649` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_ANIDNU_BGIQ_SCU_NWMU_IDRVWEY____423_16__AWSW__M__3.md` | 3321 | `not computed` | policy |
| `R2650` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_ANIDNU_SUIK_MWXY_INQ_RLIAW_NWNK_DUIR_SMJOGO__1___773_5__SUHI__M__4.md` | 5959 | `not computed` | health |
| `R2651` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_ARD_AURD_KRY_INRMJN_VWSU____952_17__RWMKLI__M__1.md` | 8929 | `not computed` | policy |
| `R2652` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_ASIQRU_CIQU_MRIN_MNU_MWINAW____932_6__RWMKLI_DKXI__M__1.md` | 4580 | `not computed` | policy |
| `R2653` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_ASMWN_IM_WNY_LHMG_DRIAW_GUSL_KRDN_BUD____727_10__IQL_G__BGQ_KBIR_JI.md` | 1708 | `not computed` | policy |
| `R2654` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_AS_LONG_AS_HIS_SOUL_AND_BODY_ARE_HEALTHY_AND_STRONG__HE_DOES_NOT_REMEMBER_THE_LO.md` | 1463 | `not computed` | health |
| `R2655` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_AS_THE_FIRE_IN_THE_FOREST__WITHOUT_CONTROL__CANNOT_SERVE_ANY_PURPOSE.md` | 5709 | `not computed` | policy |
| `R2656` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_AS_WITH_THE_MAGIC_SPELL_OF_GARUDA_THE_EAGLE_UPON_ONE_S_LIPS__ONE_DOES_NOT_FEAR_T.md` | 6056 | `not computed` | format |
| `R2657` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_AWGM_INGMU_KHY_JNU_NWNKU_SBU_DYKY_LOKU_SBWIEAW__2_6_11___714_6__TOFI__M__5.md` | 2666 | `not computed` | witness |
| `R2658` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_AWIP_AQIQU_AILPQU_HY_INRJOGU_HIR_JOGI____514_2__GUJRI_KI_VWR__M__3.md` | 10171 | `not computed` | policy |
| `R2659` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_AWIP_HOAW_SDW_MUKQU_SBU_KULU_INSQWIRAW____86_15__ISRIRWGU__M__3.md` | 2966 | `not computed` | policy |
| `R2660` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_AWIP_JWXWVY_MWRIG_PWVY_AWPY_MNUAW_LYVEY____766_16__SUHI__M__1.md` | 2388 | `not computed` | format |
| `R2661` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_AWKXU_VYKXU_BOLXU_CLXU_JIVXU_MRXW_DWQU____145_5__MWJ__M__1.md` | 11586 | `not computed` | policy |
| `R2662` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_AWN_MNAU_QAU_PR_GR_JWAU____153_13__GAUVI__M__1.md` | 10416 | `not computed` | policy |
| `R2663` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_AWN_N_JWNW_VYSW__1__RHWAU____912_16__RWMKLI__M__5.md` | 26169 | `not computed` | policy |
| `R2664` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_AWPU_VICWRY_IGAWNI_SOEI____1040_12__MWRU__M__1.md` | 6540 | `not computed` | policy |
| `R2665` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_AWPY_AWIP_AWIP_IMIL_RIHAW_SHJY_SHIJ_SMWVIXAW__5___115_5__MWJ__M__3.md` | 4137 | `not computed` | policy |
| `R2666` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_AWPY_AWPU_AUPWIE_INRWLW____1036_10__MWRU__M__1.md` | 4532 | `not computed` | policy |
| `R2667` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_AWPY_LYVY_AWPY_DYVY_IQHU_LOEI_JGQ_IPQ_DWQW_HY__3___1031_8__MWRU__M__1.md` | 3933 | `not computed` | policy |
| `R2668` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_AWPY_LYVY_VSQU_SMWLY____1033_10__MWRU_DKXI__M__1.md` | 1576 | `not computed` | policy |
| `R2669` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_AWPY_SIQGURU_AWPY_PRIQPWL____807_4__IBLWVLU__M__5.md` | 2543 | `not computed` | policy |
| `R2670` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_AWPY_VYDU_AWIP_NWRWIEXU____962_12__RWMKLI__M__5.md` | 12029 | `not computed` | policy |
| `R2671` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_AWSW_MHLW_1_PMCPDY.md` | 23644 | `not computed` | policy |
| `R2672` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_AWSW_MHLW_1____421_19.md` | 5459 | `not computed` | policy |
| `R2673` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_AWSW_MHLW_3.md` | 381540 | `not computed` | policy |
| `R2674` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_AWSW_MHLW_3_CMQ_GRU_3.md` | 48930 | `not computed` | policy |
| `R2675` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_AWSW_MHLW_4.md` | 307876 | `not computed` | policy |
| `R2676` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_AWSW_MHLW_5_ASTPDIAW_GRU_2.md` | 16164 | `not computed` | policy |
| `R2677` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_AWSW____477_9.md` | 1802 | `not computed` | policy |
| `R2678` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_AWSW____480_10.md` | 1859 | `not computed` | policy |
| `R2679` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_AWS_AINQ_GURMUIK_IMTY_NWNK_NWM_AROG__1___254_1__GAUVI__M__5.md` | 3338 | `not computed` | health |
| `R2680` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_AWT_PHR_ISMRHU_IQSU_RSNW____269_17__GAUVI_SUKMNI__M__5.md` | 18251 | `not computed` | health |
| `R2681` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_AWVW_GAUXU_BJWRIAW_BWJWRU_IJNI_RCWIEAW____1290_13__MLWR__M__1.md` | 1564 | `not computed` | format |
| `R2682` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_AXJWXQ_NWMU_VKWXIAY__3___1168_13__BSMQU__M__1.md` | 16762 | `not computed` | policy |
| `R2683` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_AYQY_EQY_INBHI_NWIL____355_4__AWSW__M__1.md` | 3746 | `not computed` | policy |
| `R2684` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_AYQY_SDW_SUKU_DIR_SOBW_HOEI__1___161_15__GAUVI_GUAWRYRI__M__3.md` | 2872 | `not computed` | policy |
| `R2685` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_AYSW_JOGI_NAU_INID_PWVY____477_10__AWSW__BGQ_KBIR_JI.md` | 3500 | `not computed` | policy |
| `R2686` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_AYSW_SIQGURU_JY_IMLY_QUTW_KRY_PSWAU____509_17__GUJRI_KI_VWR__M__3.md` | 7940 | `not computed` | policy |
| `R2687` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_A_SURFACE_CANNOT_SPEND_THE_SAME_INCOMING_ENERGY_TWICE.md` | 2424 | `not computed` | policy |
| `R2688` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_BGIQ_BWV_IEHU_MWRGU_IBKVW_GUR_DUAWRY_KO_PWVEY____440_10__AWSW__M__3.md` | 1656 | `not computed` | policy |
| `R2689` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_BGIQ_NVY_PRKWRW____71_9__ISRIRWGU__M__5.md` | 5317 | `not computed` | format |
| `R2690` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_BIQIR_KOT_GUPW_GR_JWEI____1033_11__MWRU_DKXI__M__1.md` | 2835 | `not computed` | policy |
| `R2691` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_BLESSED_IS_THAT_GURDWARA__THE_GURU_S_GATE__WHERE_THE_PRAISES_OF_THE_TRUE_LORD_AR.md` | 2385 | `not computed` | policy |
| `R2692` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_BNIQ_NWNKU_KRY_VICWRU____661_16__DNWSRI__M__1.md` | 2602 | `not computed` | policy |
| `R2693` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_BSMQU_IHMFOLU_MHLW_1_GRU_2.md` | 18690 | `not computed` | policy |
| `R2694` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_BSMQU_MHLW_3_IEK_QUKW.md` | 20290 | `not computed` | policy |
| `R2695` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_BSMQU_MHLW_3_QIJW.md` | 16049 | `not computed` | policy |
| `R2696` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_BWFW_AIQ_MLIXU_DOQW_HCW_N_HOIESI____730_1__SUHI__M__1.md` | 4045 | `not computed` | policy |
| `R2697` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_BYRAU_MHLW_3.md` | 214297 | `not computed` | policy |
| `R2698` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_BYTY_QWSU_PRM_GURDYAU__3___974_10__RWMKLI__BGQ_BYXI_JI.md` | 4496 | `not computed` | policy |
| `R2699` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_BY_GREAT_GOOD_FORTUNE__I_OBTAINED_IT__AND_I_MEDITATE_ON_THE_NAAM__THE_NAME_OF_TH.md` | 4991 | `not computed` | policy |
| `R2700` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_BY_IVIC_AWVIH_JWVIH_PUR____464_15__AWSW__M__1.md` | 10394 | `not computed` | format |
| `R2701` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_BY_PRACTICING_CONTROL_OVER_THE_NINE_GATES__ONE_ATTAINS_PERFECT_CONTROL_OVER_THE.md` | 2068 | `not computed` | policy |
| `R2702` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_BY_RWCY_SC_RMIG_SMWIE__1__RHWAU____157_17__GAUVI_GUAWRYRI__M__3.md` | 27581 | `not computed` | policy |
| `R2703` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_BY_THE_HUKAM_OF_GOD_S_WILL__THEY_COME_INTO_THIS_WORLD__AND_THEY_LEAVE_UPON_RECEI.md` | 2204 | `not computed` | ledger |
| `R2704` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_CENTRAL_IDEA.md` | 1302 | `not computed` | policy |
| `R2705` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_CHANTING_THE_LORD_S_NAME__HE_SAVES_HIMSELF__AND_HE_CARRIES_ACROSS_THOSE_WHO_ARE.md` | 3803 | `not computed` | ledger |
| `R2706` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_CLOUDS_AND_ATMOSPHERIC_FORMATION___SCIENCE_HANDOUT_10.md` | 2040 | `not computed` | policy |
| `R2707` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_CLOUD_FOREST__SUBTROPICAL_TEMPERATE__PERSISTENT_OR_FREQUENT_CLOUD_IMMERSION_AT_E.md` | 3292 | `not computed` | health |
| `R2708` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_CLOUD_TYPES__FRONTS__AND_ALTITUDES___FIELD_REFERENCE_PAGE_14.md` | 6814 | `not computed` | policy |
| `R2709` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_COLD_AND_MIXED_PHASE_PATHWAY.md` | 1379 | `not computed` | policy |
| `R2710` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_DANIEL.md` | 168619 | `not computed` | witness, format, policy |
| `R2711` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_DANIEL_1.md` | 12170 | `not computed` | format |
| `R2712` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_DANIEL_11.md` | 33389 | `not computed` | witness |
| `R2713` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_DANIEL_2.md` | 33223 | `not computed` | format, policy |
| `R2714` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_DANIEL_4.md` | 23857 | `not computed` | format |
| `R2715` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_DANIEL_5.md` | 21189 | `not computed` | format |
| `R2716` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_DANIEL_8.md` | 19068 | `not computed` | policy |
| `R2717` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_DEUTERONOMY.md` | 434025 | `not computed` | witness, policy |
| `R2718` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_DEUTERONOMY_17.md` | 12869 | `not computed` | witness |
| `R2719` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_DEUTERONOMY_19.md` | 12624 | `not computed` | witness |
| `R2720` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_DEUTERONOMY_21.md` | 12383 | `not computed` | policy |
| `R2721` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_DEUTERONOMY_22.md` | 16202 | `not computed` | policy |
| `R2722` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_DEUTERONOMY_25.md` | 13563 | `not computed` | policy |
| `R2723` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_DEUTERONOMY_31.md` | 18763 | `not computed` | witness |
| `R2724` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_DEUTERONOMY_36.md` | 18805 | `not computed` | witness |
| `R2725` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_DEUTERONOMY_4.md` | 26947 | `not computed` | witness |
| `R2726` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_DEUTERONOMY_5.md` | 18720 | `not computed` | witness |
| `R2727` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_DIFFUSE_BASE_RESPONSE_IS_ATTENUATED_BY.md` | 2963 | `not computed` | policy |
| `R2728` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_DIN_DMIN_HMWRY_BWG_GIR_AWIEAW_IPRU_MYRW____847_14__IBLWVLU__M__5.md` | 7635 | `not computed` | policy |
| `R2729` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_DNWSRI_MHLW_1.md` | 138812 | `not computed` | policy |
| `R2730` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_DNWSRI_MHLW_5_CMQ.md` | 158896 | `not computed` | policy |
| `R2731` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_DRM_KOIT_JW_KY_PRIQHWR__2___1163_1__BYRAU__BGQ_KBIR_JI.md` | 5540 | `not computed` | policy |
| `R2732` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_DRQI_DYG_IMLY_IEK_VYRW_BWGU_QYRW_BMFWRI__2___1190_19__BSMQU_IHMFOL__M__1.md` | 3471 | `not computed` | policy |
| `R2733` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_DWVQU_QMIM_AW_SIQGUIR_IMILAY_DSVW_DUAWRU_PWIEAW____441_1__AWSW__M__3.md` | 5104 | `not computed` | policy |
| `R2734` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_DWVQU_RWKY_TWIK_RHWEY____110_3__MWJ__M__3.md` | 4479 | `not computed` | policy |
| `R2735` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_EARTH_BIOMES__SUB_BIOMES__AND_TERRAIN___REFERENCE_GUIDE_2.md` | 2442 | `not computed` | policy |
| `R2736` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_ENTANGLEMENTS_END__AND_EGOTISM_DIES__ALONG_WITH_ATTACHMENT_TO_MAYA__POSSESSIVENE.md` | 4679 | `not computed` | policy |
| `R2737` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_ESTHER.md` | 77312 | `not computed` | policy |
| `R2738` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_ESTHER_1.md` | 11449 | `not computed` | policy |
| `R2739` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_ESTHER_2.md` | 17567 | `not computed` | policy |
| `R2740` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_ESTHER_3.md` | 12249 | `not computed` | policy |
| `R2741` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_ESTHER_4.md` | 11768 | `not computed` | policy |
| `R2742` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_ESTHER_5.md` | 8888 | `not computed` | policy |
| `R2743` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_ESTHER_6.md` | 9722 | `not computed` | policy |
| `R2744` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_EXODUS_10.md` | 17555 | `not computed` | policy |
| `R2745` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_EXODUS_16.md` | 21899 | `not computed` | policy |
| `R2746` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_EXODUS_20.md` | 13579 | `not computed` | witness |
| `R2747` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_EXODUS_22.md` | 17488 | `not computed` | witness, policy |
| `R2748` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_EXODUS_23.md` | 20599 | `not computed` | witness |
| `R2749` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_EXODUS_27.md` | 13974 | `not computed` | policy |
| `R2750` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_EXODUS_28.md` | 26555 | `not computed` | policy |
| `R2751` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_EXODUS_32.md` | 21699 | `not computed` | policy |
| `R2752` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_EXODUS_38.md` | 18300 | `not computed` | policy |
| `R2753` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_EXODUS_39.md` | 20839 | `not computed` | policy |
| `R2754` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_EXODUS_4.md` | 19178 | `not computed` | policy |
| `R2755` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_EXODUS_40.md` | 20185 | `not computed` | policy |
| `R2756` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_EXODUS_44.md` | 18333 | `not computed` | policy |
| `R2757` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_EXODUS_45.md` | 21173 | `not computed` | policy |
| `R2758` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_EXODUS_46.md` | 20212 | `not computed` | policy |
| `R2759` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_EXODUS_7.md` | 14777 | `not computed` | format, policy |
| `R2760` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_EXODUS_8.md` | 20453 | `not computed` | format, policy |
| `R2761` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_EXODUS_9.md` | 20651 | `not computed` | format, policy |
| `R2762` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_EZEKIEL_10.md` | 13820 | `not computed` | policy |
| `R2763` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_EZEKIEL_11.md` | 15999 | `not computed` | policy |
| `R2764` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_EZEKIEL_27.md` | 27942 | `not computed` | policy |
| `R2765` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_EZEKIEL_40.md` | 35408 | `not computed` | policy |
| `R2766` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_EZEKIEL_42.md` | 15109 | `not computed` | policy |
| `R2767` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_EZEKIEL_43.md` | 19392 | `not computed` | policy |
| `R2768` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_EZEKIEL_44.md` | 21199 | `not computed` | policy |
| `R2769` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_EZEKIEL_45.md` | 17718 | `not computed` | policy |
| `R2770` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_EZEKIEL_46.md` | 15614 | `not computed` | policy |
| `R2771` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_EZEKIEL_47.md` | 17287 | `not computed` | policy |
| `R2772` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_EZEKIEL_48.md` | 26126 | `not computed` | policy |
| `R2773` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_EZEKIEL_5.md` | 12520 | `not computed` | policy |
| `R2774` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_EZEKIEL_8.md` | 15061 | `not computed` | policy |
| `R2775` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_EZEKIEL_9.md` | 9513 | `not computed` | policy |
| `R2776` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_E_________H_F__________COS____D_____1.md` | 1674 | `not computed` | policy |
| `R2777` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_FIVE_PRINCIPLES_TO_REMEMBER.md` | 1447 | `not computed` | policy |
| `R2778` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_GAUVI_BYRWGIX_MHLW_1.md` | 39233 | `not computed` | policy |
| `R2779` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_GAUVI_GUAWRYRI_MHLW_3.md` | 170701 | `not computed` | policy |
| `R2780` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_GAUVI_MHLW_1.md` | 364279 | `not computed` | policy |
| `R2781` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_GENESIS_19.md` | 21020 | `not computed` | policy |
| `R2782` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_GENESIS_21.md` | 18865 | `not computed` | witness |
| `R2783` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_GENESIS_22.md` | 12810 | `not computed` | policy |
| `R2784` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_GENESIS_23.md` | 10997 | `not computed` | policy |
| `R2785` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_GENESIS_24.md` | 38297 | `not computed` | policy |
| `R2786` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_GENESIS_28.md` | 12463 | `not computed` | policy |
| `R2787` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_GENESIS_31.md` | 35852 | `not computed` | witness |
| `R2788` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_GENESIS_32.md` | 19309 | `not computed` | witness |
| `R2789` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_GENESIS_34.md` | 19745 | `not computed` | policy |
| `R2790` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_GENESIS_37.md` | 22190 | `not computed` | policy |
| `R2791` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_GENESIS_39.md` | 14595 | `not computed` | policy |
| `R2792` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_GENESIS_41.md` | 33526 | `not computed` | format |
| `R2793` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_GENESIS_43.md` | 20685 | `not computed` | health |
| `R2794` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_GENESIS_48.md` | 14324 | `not computed` | policy |
| `R2795` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_GENESIS_54.md` | 14677 | `not computed` | policy |
| `R2796` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_GIV_BWFY_IETW_KIAW_JLDI_KRY_PUKWR____466_6__AWSW__M__1.md` | 20888 | `not computed` | policy |
| `R2797` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_GRU_DRU_MMDRU_JWXY_SOEI____1039_8__MWRU__M__1.md` | 3458 | `not computed` | witness |
| `R2798` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_GT_BIQIR_QU_DYKU_IBCWIR____1159_13__BYRAU__BGQ_KBIR_JI.md` | 22289 | `not computed` | policy |
| `R2799` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_GUJRI_MHLW_3.md` | 41825 | `not computed` | policy |
| `R2800` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_GUJRI_MHLW_5_GRU_4.md` | 288713 | `not computed` | policy |
| `R2801` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_HABAKKUK.md` | 22015 | `not computed` | witness |
| `R2802` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_HABAKKUK_3.md` | 16007 | `not computed` | witness |
| `R2803` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_HEBREWS.md` | 153045 | `not computed` | witness, policy |
| `R2804` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_HEBREWS_10.md` | 18241 | `not computed` | witness |
| `R2805` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_HEBREWS_11.md` | 19921 | `not computed` | witness, policy |
| `R2806` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_HEBREWS_12.md` | 12762 | `not computed` | witness, policy |
| `R2807` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_HEBREWS_13.md` | 14004 | `not computed` | policy |
| `R2808` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_HEBREWS_2.md` | 9681 | `not computed` | witness |
| `R2809` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_HEBREWS_7.md` | 14843 | `not computed` | witness |
| `R2810` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_HE_ALONE_COMES_TO_UNDERSTAND__WHO_ENTERS_THE_GURU_S_GATE__WHOM_THE_LORD_HIMSELF.md` | 2148 | `not computed` | policy |
| `R2811` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_HE_ASCENDS_THE_SUBLIME__EXALTED_LADDER_OF_THE_GURU__AND_HE_SINGS_THE_GLORIOUS_PR.md` | 2076 | `not computed` | policy |
| `R2812` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_HE_HAS_ENDEAVOURED_TO_PREVENT_THE_POPULATION.md` | 1011 | `not computed` | policy |
| `R2813` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_HE_HAS_OBSTRUCTED_THE_ADMINISTRATION_OF_JUS.md` | 790 | `not computed` | policy |
| `R2814` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_HE_HAS_REFUSED_FOR_A_LONG_TIME__AFTER_SUCH_DIS.md` | 1075 | `not computed` | policy |
| `R2815` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_HE_HAS_REFUSED_HIS_ASSENT_TO_LAWS__THE_MOST.md` | 726 | `not computed` | policy |
| `R2816` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_HE_HAS_REFUSED_TO_PASS_OTHER_LAWS_FOR_THE_AC.md` | 986 | `not computed` | policy |
| `R2817` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_HE_IS_NOT_A_PENITENT__WHO_IS_GREEDY_WITHIN_HIS_HEART__AND_WHO_CONSTANTLY_CHASES.md` | 2291 | `not computed` | policy |
| `R2818` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_HE_OBTAINS_PEACE_AND_GLORIOUS_GREATNESS_HERE__IN_THE_LORD_S_COURT__AND_AT_THE_GA.md` | 875 | `not computed` | policy |
| `R2819` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_HOSEA.md` | 89394 | `not computed` | policy |
| `R2820` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_HOSEA_11.md` | 9741 | `not computed` | policy |
| `R2821` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_IBHWGVY_KI_VWR_MHLW_4.md` | 251439 | `not computed` | policy |
| `R2822` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_IBLWVLU_MHLW_5_CMQ.md` | 44551 | `not computed` | policy |
| `R2823` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_IF_I_HAD_KNOWN_THAT_HE_WAS_A_ONLY_WRETCHED_CRANE__I_WOULD_NEVER_IN_MY_LIFE_HAVE.md` | 7313 | `not computed` | format |
| `R2824` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_IMBUED_FOREVER_WITH_THE_LOVE_OF_MY_LORD_AND_MASTER__I_CHANT_HIS_NAME__NIGHT_AND.md` | 5390 | `not computed` | policy |
| `R2825` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_IMPLEMENTATION_CONSEQUENCE.md` | 982 | `not computed` | policy |
| `R2826` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_INDEX.md` | 252884 | `not computed` | policy, ledger |
| `R2827` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_INNER_CLEANSING_TECHNIQUES__CHANNELING_THE_ENERGY_TO_RAISE_THE_KUNDALINI_TO_THE.md` | 6446 | `not computed` | policy |
| `R2828` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_INTERPRETATION.md` | 1474 | `not computed` | policy |
| `R2829` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_IN_THE_AMRIT_VAYLAA__THE_AMBROSIAL_HOURS_BEFORE_DAWN__CHANT_THE_TRUE_NAME__AND.md` | 2218 | `not computed` | policy |
| `R2830` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_IQL_G_MHLW_9.md` | 42205 | `not computed` | format, policy |
| `R2831` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_IRRIGATE_YOUR_FIELDS_WITH_THE_AMBROSIAL_NECTAR__AND_YOU_SHALL_BE_OWNED_BY_GOD_TH.md` | 1450 | `not computed` | policy |
| `R2832` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_ISAIAH_1.md` | 20507 | `not computed` | policy |
| `R2833` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_ISAIAH_14.md` | 21717 | `not computed` | policy |
| `R2834` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_ISAIAH_19.md` | 19184 | `not computed` | witness |
| `R2835` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_ISAIAH_22.md` | 13738 | `not computed` | policy |
| `R2836` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_ISAIAH_24.md` | 16713 | `not computed` | policy |
| `R2837` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_ISAIAH_28.md` | 19536 | `not computed` | policy |
| `R2838` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_ISAIAH_29.md` | 17028 | `not computed` | policy |
| `R2839` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_ISAIAH_3.md` | 14736 | `not computed` | witness |
| `R2840` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_ISAIAH_43.md` | 18901 | `not computed` | witness |
| `R2841` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_ISAIAH_44.md` | 18806 | `not computed` | witness |
| `R2842` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_ISAIAH_54.md` | 10834 | `not computed` | policy |
| `R2843` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_ISAIAH_55.md` | 8511 | `not computed` | witness |
| `R2844` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_ISAIAH_58.md` | 8430 | `not computed` | health |
| `R2845` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_ISAIAH_7.md` | 13548 | `not computed` | policy |
| `R2846` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_ISAIAH_8.md` | 15258 | `not computed` | witness, policy |
| `R2847` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_ISRIRWGU_MHLW_1_GRU_1_ASTPDIAW.md` | 42611 | `not computed` | policy |
| `R2848` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_ISRIRWGU_MHLW_1_GRU_3.md` | 74367 | `not computed` | policy |
| `R2849` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_ISRIRWGU_MHLW_4_VXJWRW.md` | 37347 | `not computed` | health |
| `R2850` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_ISRIRWGU_MHLW_5_GRU_5.md` | 19221 | `not computed` | format |
| `R2851` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_ISRIRWG_KI_VWR_MHLW_4_SLOKW_NWIL.md` | 331010 | `not computed` | policy |
| `R2852` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_IS_THERE_ANY_DEVOTEE__WHO_IS_UNATTACHED_TO_MAYA__WHO_MAY_IRRIGATE_MY_MIND_WITH_T.md` | 1569 | `not computed` | policy |
| `R2853` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_IT_DIES_AND_DIES_AGAIN__AND_IS_REBORN__ALWAYS_IN_PAIN__BUT_IT_IS_UNAWARE_OF_THE.md` | 2138 | `not computed` | policy |
| `R2854` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_I_AM_THE_DUST_OF_THE_LOTUS_FEET_OF_THOSE_WHOSE_HEARTS_ARE_FILLED_WITH_THE_ALL_PE.md` | 5731 | `not computed` | policy |
| `R2855` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_I_HAVE_NOT_KNOWN_MY_HUSBAND_LORD__HIS_CELESTIAL_HOME_AND_GATE__OR_THE_BLESSED.md` | 3640 | `not computed` | policy |
| `R2856` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_I_HAVE_SEEN_THE_MORTALS_OF_MANY_AND_VARIOUS_TYPES__BUT_THEY_ARE_NOT_EQUAL_TO_EVE.md` | 3421 | `not computed` | policy |
| `R2857` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_I_MAKE_MY_MIND_AND_BODY_INTO_PURE_LITTLE_GARDENS__AND_IRRIGATE_THEM_WITH_THE_SUB.md` | 1480 | `not computed` | policy |
| `R2858` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_JAMES.md` | 56702 | `not computed` | witness |
| `R2859` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_JAMES_5.md` | 11770 | `not computed` | witness |
| `R2860` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_JEREMIAH_11.md` | 12340 | `not computed` | policy |
| `R2861` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_JEREMIAH_13.md` | 18405 | `not computed` | policy |
| `R2862` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_JEREMIAH_15.md` | 16117 | `not computed` | policy |
| `R2863` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_JEREMIAH_17.md` | 18196 | `not computed` | policy |
| `R2864` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_JEREMIAH_19.md` | 7987 | `not computed` | policy |
| `R2865` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_JEREMIAH_20.md` | 13887 | `not computed` | policy |
| `R2866` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_JEREMIAH_25.md` | 20667 | `not computed` | policy |
| `R2867` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_JEREMIAH_26.md` | 16095 | `not computed` | policy |
| `R2868` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_JEREMIAH_29.md` | 18695 | `not computed` | witness |
| `R2869` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_JEREMIAH_3.md` | 18173 | `not computed` | policy |
| `R2870` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_JEREMIAH_30.md` | 15729 | `not computed` | health |
| `R2871` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_JEREMIAH_31.md` | 25838 | `not computed` | policy |
| `R2872` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_JEREMIAH_32.md` | 23663 | `not computed` | witness |
| `R2873` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_JEREMIAH_33.md` | 16546 | `not computed` | health |
| `R2874` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_JEREMIAH_36.md` | 20285 | `not computed` | policy |
| `R2875` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_JEREMIAH_37.md` | 15422 | `not computed` | policy |
| `R2876` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_JEREMIAH_38.md` | 18758 | `not computed` | policy |
| `R2877` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_JEREMIAH_39.md` | 10838 | `not computed` | policy |
| `R2878` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_JEREMIAH_42.md` | 14403 | `not computed` | witness |
| `R2879` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_JEREMIAH_5.md` | 18541 | `not computed` | policy |
| `R2880` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_JEREMIAH_50.md` | 34324 | `not computed` | policy |
| `R2881` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_JEREMIAH_52.md` | 23607 | `not computed` | policy |
| `R2882` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_JEREMIAH_7.md` | 19962 | `not computed` | policy |
| `R2883` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_JEREMIAH_8.md` | 16102 | `not computed` | health, policy |
| `R2884` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_JEREMIAH_9.md` | 17562 | `not computed` | policy |
| `R2885` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_JOB.md` | 427849 | `not computed` | witness, policy |
| `R2886` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_JOB_10.md` | 10761 | `not computed` | witness |
| `R2887` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_JOB_11.md` | 12504 | `not computed` | witness |
| `R2888` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_JOB_16.md` | 10802 | `not computed` | witness |
| `R2889` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_JOB_29.md` | 11265 | `not computed` | witness, policy |
| `R2890` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_JOB_31.md` | 22215 | `not computed` | policy |
| `R2891` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_JOB_34.md` | 20630 | `not computed` | policy |
| `R2892` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_JOB_5.md` | 11994 | `not computed` | policy |
| `R2893` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_JOB_6.md` | 18183 | `not computed` | policy |
| `R2894` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_JOHN.md` | 432393 | `not computed` | witness |
| `R2895` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_JOHN_1.md` | 26447 | `not computed` | witness |
| `R2896` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_JOHN_10.md` | 20907 | `not computed` | witness |
| `R2897` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_JOHN_15.md` | 13583 | `not computed` | witness |
| `R2898` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_JOHN_18.md` | 21855 | `not computed` | witness |
| `R2899` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_JOHN_3.md` | 19393 | `not computed` | witness |
| `R2900` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_JOHN_5.md` | 24482 | `not computed` | witness |
| `R2901` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_JOHN_8.md` | 31267 | `not computed` | witness |
| `R2902` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_JOSHUA.md` | 280467 | `not computed` | witness, policy |
| `R2903` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_JOSHUA_2.md` | 14785 | `not computed` | policy |
| `R2904` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_JOSHUA_20.md` | 5946 | `not computed` | policy |
| `R2905` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_JOSHUA_22.md` | 19815 | `not computed` | witness |
| `R2906` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_JOSHUA_23.md` | 10456 | `not computed` | witness |
| `R2907` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_JOSHUA_24.md` | 21514 | `not computed` | witness |
| `R2908` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_JOSHUA_25.md` | 19845 | `not computed` | witness |
| `R2909` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_JOSHUA_26.md` | 10790 | `not computed` | witness |
| `R2910` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_JOSHUA_27.md` | 21545 | `not computed` | witness |
| `R2911` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_JOSHUA_7.md` | 16634 | `not computed` | policy |
| `R2912` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_JOSHUA_8.md` | 21198 | `not computed` | policy |
| `R2913` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_JUDGES.md` | 287642 | `not computed` | witness, policy |
| `R2914` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_JUDGES_11.md` | 25134 | `not computed` | witness |
| `R2915` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_JUDGES_16.md` | 25160 | `not computed` | policy |
| `R2916` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_JUDGES_18.md` | 21926 | `not computed` | policy |
| `R2917` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_JUDGES_22.md` | 11736 | `not computed` | policy |
| `R2918` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_JUDGES_9.md` | 35198 | `not computed` | policy |
| `R2919` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_JUTU_DVY_KIR_PCOQWIH____366_5__AWSW__M__4.md` | 9644 | `not computed` | policy |
| `R2920` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_JYQSRI_MHLW_5.md` | 62159 | `not computed` | policy |
| `R2921` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_JYQSRI_MHLW_5_VWR_SLOKW_NWIL.md` | 178594 | `not computed` | witness |
| `R2922` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_KINGS_2.md` | 402018 | `not computed` | witness, policy |
| `R2923` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_KWEI_KOTU_N_PRL_PGWRW____1161_12__BYRAU__M__5.md` | 5887 | `not computed` | policy |
| `R2924` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_KWXW_PIXW_HSXW_BWID____351_8__AWSW__M__1.md` | 7770 | `not computed` | witness |
| `R2925` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_KYDWRW_CMQ_MHLW_5.md` | 78985 | `not computed` | policy |
| `R2926` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_KYLU_DYIK_MIN_ANDU_BIEAW_SHU_VIAWHX_AWIEAW__1___351_14__AWSW__M__1.md` | 3801 | `not computed` | policy |
| `R2927` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_LAMENTATIONS.md` | 67830 | `not computed` | witness, policy |
| `R2928` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_LAMENTATIONS_10.md` | 12394 | `not computed` | policy |
| `R2929` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_LAMENTATIONS_13.md` | 14963 | `not computed` | policy |
| `R2930` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_LAMENTATIONS_14.md` | 9323 | `not computed` | policy |
| `R2931` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_LAMENTATIONS_15.md` | 14019 | `not computed` | policy |
| `R2932` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_LAMENTATIONS_16.md` | 15452 | `not computed` | policy |
| `R2933` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_LAMENTATIONS_2.md` | 17575 | `not computed` | witness |
| `R2934` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_LAMENTATIONS_3.md` | 31155 | `not computed` | policy |
| `R2935` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_LAMENTATIONS_32.md` | 27128 | `not computed` | policy |
| `R2936` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_LAMENTATIONS_45.md` | 35236 | `not computed` | policy |
| `R2937` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_LAMENTATIONS_47.md` | 14970 | `not computed` | policy |
| `R2938` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_LAMENTATIONS_48.md` | 19329 | `not computed` | policy |
| `R2939` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_LAMENTATIONS_49.md` | 20754 | `not computed` | policy |
| `R2940` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_LAMENTATIONS_5.md` | 13846 | `not computed` | policy |
| `R2941` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_LAMENTATIONS_50.md` | 16715 | `not computed` | policy |
| `R2942` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_LAMENTATIONS_51.md` | 15845 | `not computed` | policy |
| `R2943` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_LAMENTATIONS_52.md` | 16112 | `not computed` | policy |
| `R2944` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_LAMENTATIONS_53.md` | 26450 | `not computed` | policy |
| `R2945` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_LAMENTATIONS_54.md` | 19677 | `not computed` | policy |
| `R2946` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_LAMENTATIONS_55.md` | 21524 | `not computed` | policy |
| `R2947` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_LAMENTATIONS_56.md` | 17674 | `not computed` | policy |
| `R2948` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_LAMENTATIONS_57.md` | 16178 | `not computed` | policy |
| `R2949` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_LAMENTATIONS_58.md` | 17243 | `not computed` | policy |
| `R2950` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_LAMENTATIONS_59.md` | 26501 | `not computed` | policy |
| `R2951` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_LET_YOUR_MIND_BE_INTOXICATED_WITH_THE_STREAM_OF_AMBROSIAL_NECTAR_WHICH_TRICKLES.md` | 2262 | `not computed` | policy |
| `R2952` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_LEVITICUS.md` | 395648 | `not computed` | witness |
| `R2953` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_LEVITICUS_5.md` | 11964 | `not computed` | witness |
| `R2954` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_LIKE_THE_ESSENCE_OF_SANDALWOOD__HE_PERMEATES_HER_CONSCIOUSNESS__AND_THE_TEMPLE_O.md` | 4165 | `not computed` | policy |
| `R2955` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_LOVE_AND_DEVOTION_HAVE_NOT_WELLED_UP_WITHIN_ME__AND_SO_RAVI_DAAS_IS_SAD_AND.md` | 6033 | `not computed` | policy |
| `R2956` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_LUKE_1.md` | 37312 | `not computed` | witness |
| `R2957` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_LUKE_11.md` | 28817 | `not computed` | witness |
| `R2958` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_LUKE_13.md` | 19258 | `not computed` | policy |
| `R2959` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_LUKE_16.md` | 17582 | `not computed` | policy |
| `R2960` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_LUKE_18.md` | 21020 | `not computed` | witness |
| `R2961` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_LUKE_22.md` | 34995 | `not computed` | witness |
| `R2962` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_LUKE_24.md` | 25700 | `not computed` | witness |
| `R2963` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_LUKE_4.md` | 21571 | `not computed` | witness |
| `R2964` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_LUKE_5.md` | 21633 | `not computed` | ledger |
| `R2965` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_LUKE_7.md` | 26941 | `not computed` | policy |
| `R2966` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_MALACHI.md` | 24674 | `not computed` | witness |
| `R2967` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_MALACHI_2.md` | 14102 | `not computed` | witness |
| `R2968` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_MALACHI_3.md` | 10645 | `not computed` | witness |
| `R2969` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_MARK.md` | 324625 | `not computed` | witness, ledger |
| `R2970` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_MARK_10.md` | 26760 | `not computed` | witness |
| `R2971` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_MARK_14.md` | 37845 | `not computed` | witness |
| `R2972` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_MARK_15.md` | 24140 | `not computed` | witness |
| `R2973` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_MARK_2.md` | 15215 | `not computed` | ledger |
| `R2974` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_MATTHEW.md` | 498593 | `not computed` | witness, policy, ledger |
| `R2975` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_MATTHEW_15.md` | 19327 | `not computed` | witness |
| `R2976` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_MATTHEW_18.md` | 19686 | `not computed` | witness |
| `R2977` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_MATTHEW_19.md` | 16997 | `not computed` | witness |
| `R2978` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_MATTHEW_23.md` | 20062 | `not computed` | witness |
| `R2979` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_MATTHEW_24.md` | 24552 | `not computed` | witness |
| `R2980` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_MATTHEW_26.md` | 39296 | `not computed` | witness |
| `R2981` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_MATTHEW_27.md` | 32582 | `not computed` | witness |
| `R2982` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_MATTHEW_7.md` | 13618 | `not computed` | policy |
| `R2983` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_MATTHEW_9.md` | 20379 | `not computed` | ledger |
| `R2984` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_MEDITATING_ON_THE_NAAM__THE_NAME_OF_THE_LORD__WITH_INTUITIVE_EASE_AND_POISE__SPI.md` | 5470 | `not computed` | policy |
| `R2985` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_MEETING_THE_TRUE_GURU__THE_LORD_COMES_TO_DWELL_IN_THE_MIND__AND_ONE_REMAINS.md` | 6888 | `not computed` | policy |
| `R2986` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_MICAH.md` | 47048 | `not computed` | witness, policy |
| `R2987` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_MICAH_1.md` | 9596 | `not computed` | witness, policy |
| `R2988` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_MICAH_2.md` | 13255 | `not computed` | policy |
| `R2989` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_MLWR_MHLW_1.md` | 133795 | `not computed` | format |
| `R2990` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_MLWR_MHLW_3.md` | 153137 | `not computed` | format |
| `R2991` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_MWJ_MHLW_3_GRU_1.md` | 21977 | `not computed` | policy |
| `R2992` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_MWJ_MHLW_5_IDN_RYIX.md` | 371445 | `not computed` | policy |
| `R2993` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_MWLI_GAUVW_MHLW_5.md` | 95715 | `not computed` | format |
| `R2994` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_MWRU_MHLW_1_DKXI.md` | 39040 | `not computed` | policy |
| `R2995` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_MWRU_MHLW_5_SOLHY.md` | 23673 | `not computed` | policy |
| `R2996` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_MWRU_SOLHY_MHLW_4.md` | 39306 | `not computed` | policy |
| `R2997` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_MY_BREATH_OF_LIFE_RESIDES_IN_HIM__WHOSE_PRAISES_ARE_SUNG_BY_SHIVA_AND_SANAK_AND.md` | 4384 | `not computed` | policy |
| `R2998` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_NEHEMIAH.md` | 180329 | `not computed` | policy |
| `R2999` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_NEHEMIAH_12.md` | 23843 | `not computed` | policy |
| `R3000` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_NEHEMIAH_14.md` | 15336 | `not computed` | policy |
| `R3001` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_NEHEMIAH_2.md` | 13306 | `not computed` | policy |
| `R3002` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_NEHEMIAH_3.md` | 20423 | `not computed` | policy |
| `R3003` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_NEHEMIAH_8.md` | 13772 | `not computed` | policy |
| `R3004` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_NEHEMIAH_9.md` | 27059 | `not computed` | policy |
| `R3005` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_NO_STATE_SHALL_BE_REPRESENTED_IN_CONGRESS_BY_LESS_THAN.md` | 1516 | `not computed` | policy |
| `R3006` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_NT_MHLW_4.md` | 152154 | `not computed` | health |
| `R3007` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_NUMBERS_17.md` | 8462 | `not computed` | witness |
| `R3008` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_NUMBERS_18.md` | 21428 | `not computed` | witness |
| `R3009` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_NUMBERS_20.md` | 15681 | `not computed` | policy |
| `R3010` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_NUMBERS_22.md` | 26833 | `not computed` | policy |
| `R3011` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_NUMBERS_35.md` | 19740 | `not computed` | witness |
| `R3012` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_NUMBERS_4.md` | 22184 | `not computed` | policy |
| `R3013` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_NUMBERS_42.md` | 19773 | `not computed` | witness |
| `R3014` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_NUMBERS_5.md` | 14034 | `not computed` | witness |
| `R3015` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_OBADIAH_1.md` | 16090 | `not computed` | policy |
| `R3016` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_OBSERVATION_LIKELY_CAUSE_TO_INVESTIGATE.md` | 616 | `not computed` | policy |
| `R3017` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_ONE_INCIDENT_LIGHT_BUDGET.md` | 546 | `not computed` | policy |
| `R3018` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_ONE_WHO_MAKES_TRUTHFULNESS_HIS_FAST_AND_RELIGIOUS_VOWS__DOES_NOT_SUFFER_THE_PAIN.md` | 4445 | `not computed` | policy |
| `R3019` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_ONE_WHO_OFFERS_BOTH_RESPECTFUL_GREETINGS_AND_RUDE_REFUSAL_TO_HIS_MASTER__HAS_GON.md` | 6966 | `not computed` | policy |
| `R3020` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_ONE_WHO__BY_GURU_S_GRACE__IS_CURED_OF_THE_DISEASE_OF_EGO.md` | 5577 | `not computed` | health |
| `R3021` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_OPEN_STANDARD_DOES_NOT_IMPLY_IDENTICAL_RENDERER_IMPLEMENTATION_11.md` | 2636 | `not computed` | policy |
| `R3022` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_OPEN_STANDARD_DOES_NOT_IMPLY_IDENTICAL_RENDERER_IMPLEMENTATION_8.md` | 3296 | `not computed` | policy |
| `R3023` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_O_BRAHMIN__YOU_WORSHIP_AND_BELIEVE_IN_YOUR_STONE_GOD__AND_WEAR_YOUR_CEREMONIAL.md` | 3835 | `not computed` | policy |
| `R3024` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_O_HUMAN_BEING__SEARCH_YOUR_OWN_HEART_EVERY_DAY__AND_DO_NOT_WANDER_AROUND_IN.md` | 2956 | `not computed` | format |
| `R3025` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_O_MERCIFUL_LORD__POTENT_TO_GIVE_SANCTUARY__MASTER_OF_THE_MEEK_AND_HUMBLE__PLEASE.md` | 2126 | `not computed` | health |
| `R3026` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_O_MORTAL__HOOK_UP_YOUR_UNSTABLE_MIND_LIKE_AN_OX__AND_IRRIGATE_YOUR_FIELDS_WITH_T.md` | 2276 | `not computed` | policy |
| `R3027` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_O_NANAK__MEETING_THE_TRUE_GURU__THE_FRUITS_ARE_OBTAINED__AND_ONE_IS_BLESSED_WITH.md` | 7044 | `not computed` | policy |
| `R3028` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_O_NANAK__THOSE_WHO_WORSHIP_AND_ADORE_THE_LORD_S_NAME_NIGHT_AND_DAY__VIBRATE_THE.md` | 4121 | `not computed` | policy |
| `R3029` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_PART_PART.md` | 6552 | `not computed` | policy |
| `R3030` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_PRBWQI_MHLW_1.md` | 281416 | `not computed` | format, policy |
| `R3031` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_PRHY_MUHKM_GUR_IGAWNU_BICWIR__2___430_15__AWSW__M__5.md` | 7694 | `not computed` | policy |
| `R3032` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_PRIMARY_FAMILY.md` | 44231 | `not computed` | policy |
| `R3033` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_PROSE.md` | 312832 | `not computed` | policy |
| `R3034` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_PROVERBS.md` | 377415 | `not computed` | witness, health, policy |
| `R3035` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_PROVERBS_1.md` | 12518 | `not computed` | policy |
| `R3036` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_PROVERBS_10.md` | 18027 | `not computed` | policy |
| `R3037` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_PROVERBS_12.md` | 14360 | `not computed` | witness, health |
| `R3038` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_PROVERBS_13.md` | 15563 | `not computed` | health, policy |
| `R3039` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_PROVERBS_14.md` | 17560 | `not computed` | witness |
| `R3040` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_PROVERBS_15.md` | 18835 | `not computed` | policy |
| `R3041` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_PROVERBS_16.md` | 20095 | `not computed` | health |
| `R3042` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_PROVERBS_17.md` | 14371 | `not computed` | policy |
| `R3043` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_PROVERBS_19.md` | 17162 | `not computed` | witness |
| `R3044` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_PROVERBS_21.md` | 19365 | `not computed` | witness, policy |
| `R3045` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_PROVERBS_22.md` | 13955 | `not computed` | policy |
| `R3046` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_PROVERBS_23.md` | 19323 | `not computed` | witness |
| `R3047` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_PROVERBS_24.md` | 18020 | `not computed` | witness, policy |
| `R3048` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_PROVERBS_25.md` | 17493 | `not computed` | witness |
| `R3049` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_PROVERBS_3.md` | 15759 | `not computed` | health |
| `R3050` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_PROVERBS_4.md` | 15297 | `not computed` | health |
| `R3051` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_PROVERBS_6.md` | 16479 | `not computed` | witness, health |
| `R3052` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_PROVERBS_8.md` | 18457 | `not computed` | policy |
| `R3053` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_PSALMS_118.md` | 15395 | `not computed` | policy |
| `R3054` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_PSALMS_127.md` | 3193 | `not computed` | policy |
| `R3055` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_PSALMS_151.md` | 12217 | `not computed` | policy |
| `R3056` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_PSALMS_153.md` | 15479 | `not computed` | health |
| `R3057` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_PSALMS_154.md` | 15327 | `not computed` | health |
| `R3058` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_PSALMS_156.md` | 16205 | `not computed` | witness, health |
| `R3059` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_PSALMS_158.md` | 18480 | `not computed` | policy |
| `R3060` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_PSALMS_160.md` | 17686 | `not computed` | policy |
| `R3061` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_PSALMS_162.md` | 14335 | `not computed` | witness, health |
| `R3062` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_PSALMS_163.md` | 15228 | `not computed` | health, policy |
| `R3063` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_PSALMS_164.md` | 17512 | `not computed` | witness |
| `R3064` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_PSALMS_165.md` | 18800 | `not computed` | policy |
| `R3065` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_PSALMS_166.md` | 19744 | `not computed` | health |
| `R3066` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_PSALMS_167.md` | 14337 | `not computed` | policy |
| `R3067` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_PSALMS_169.md` | 16824 | `not computed` | witness |
| `R3068` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_PSALMS_171.md` | 19333 | `not computed` | witness, policy |
| `R3069` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_PSALMS_172.md` | 13618 | `not computed` | policy |
| `R3070` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_PSALMS_173.md` | 19283 | `not computed` | witness |
| `R3071` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_PSALMS_174.md` | 17989 | `not computed` | witness, policy |
| `R3072` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_PSALMS_175.md` | 17166 | `not computed` | witness |
| `R3073` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_PSALMS_27.md` | 9682 | `not computed` | witness |
| `R3074` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_PSALMS_35.md` | 17052 | `not computed` | witness |
| `R3075` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_PSALMS_36.md` | 10306 | `not computed` | witness |
| `R3076` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_PSALMS_39.md` | 10840 | `not computed` | health |
| `R3077` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_PSALMS_42.md` | 6989 | `not computed` | health |
| `R3078` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_PSALMS_43.md` | 3234 | `not computed` | health |
| `R3079` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_PSALMS_67.md` | 4179 | `not computed` | health |
| `R3080` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_PSALMS_69.md` | 21669 | `not computed` | policy |
| `R3081` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_PSALMS_77.md` | 11556 | `not computed` | policy |
| `R3082` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_PSALMS_78.md` | 38884 | `not computed` | witness, policy |
| `R3083` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_PSALMS_89.md` | 31000 | `not computed` | witness |
| `R3084` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_QOVY_QIL_QWNK_AWRMBY____341_12__GAUVI_PURBI__BGQ_KBIR_JI.md` | 3937 | `not computed` | policy |
| `R3085` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_QUKWRI_CMQ_MHLW_1_BWRH_MWHW.md` | 79437 | `not computed` | policy |
| `R3086` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_RADIATIVE_OPTICS_EXTINCTION__SCATTERING_ALBEDO__PHASE_FUNCTION__SPECTRAL.md` | 7284 | `not computed` | policy |
| `R3087` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_REVELATION.md` | 236314 | `not computed` | witness, policy |
| `R3088` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_REVELATION_1.md` | 11264 | `not computed` | witness |
| `R3089` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_REVELATION_11.md` | 11594 | `not computed` | witness |
| `R3090` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_REVELATION_20.md` | 9144 | `not computed` | witness |
| `R3091` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_REVELATION_21.md` | 15741 | `not computed` | policy |
| `R3092` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_REVELATION_3.md` | 12540 | `not computed` | witness |
| `R3093` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_ROMANS.md` | 215834 | `not computed` | witness |
| `R3094` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_ROMANS_1.md` | 13525 | `not computed` | witness |
| `R3095` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_ROMANS_13.md` | 7766 | `not computed` | witness |
| `R3096` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_ROMANS_2.md` | 13265 | `not computed` | witness |
| `R3097` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_ROMANS_3.md` | 13141 | `not computed` | witness |
| `R3098` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_ROMANS_8.md` | 20713 | `not computed` | witness |
| `R3099` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_ROMANS_9.md` | 16260 | `not computed` | witness |
| `R3100` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_RUTH.md` | 37432 | `not computed` | witness, policy |
| `R3101` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_RUTH_3.md` | 12947 | `not computed` | policy |
| `R3102` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_RUTH_4.md` | 12442 | `not computed` | witness, policy |
| `R3103` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_RWGU_AWSW_GRU_2_MHLW_4.md` | 18278 | `not computed` | policy |
| `R3104` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_RWGU_AWSW_MHLW_1_ASTPDIAW_GRU_2.md` | 25852 | `not computed` | policy |
| `R3105` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_RWGU_AWSW_MHLW_1_GRU_1_SO_DRU.md` | 17585 | `not computed` | policy |
| `R3106` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_RWGU_DYVGMDWRI_MHLW_5_GRU_3.md` | 21672 | `not computed` | policy |
| `R3107` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_RWGU_DYVGMDWRI_MHLW_5_GRU_6.md` | 14564 | `not computed` | policy |
| `R3108` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_RWGU_SUHI_CMQ_MHLW_1_GRU_1.md` | 20645 | `not computed` | policy |
| `R3109` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_RWGU_SUHI_MHLW_4_CMQ_GRU_1.md` | 20395 | `not computed` | health |
| `R3110` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_RWGU_SUHI_MHLW_5_ASTPDIAW_GRU_9.md` | 24579 | `not computed` | ledger |
| `R3111` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_RWGU_SUHI_MHLW_5_GRU_5_PVQWL.md` | 11782 | `not computed` | policy |
| `R3112` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_RWMKLI_DKXI_MHLW_1.md` | 14483 | `not computed` | policy |
| `R3113` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_RWMKLI_KI_VWR_MHLW_3.md` | 329906 | `not computed` | policy, ledger |
| `R3114` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_RWMKLI_MHLW_1.md` | 293598 | `not computed` | policy |
| `R3115` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_RWMKLI_MHLW_1_DKXI_EAMKWRU.md` | 280891 | `not computed` | policy |
| `R3116` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_RWMKLI_MHLW_1_ISD_GOSIT.md` | 291450 | `not computed` | policy |
| `R3117` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_RWMKLI_MHLW_3_AN_DU.md` | 190994 | `not computed` | policy |
| `R3118` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_RWMKLI_MHLW_5_ASTPDIAW.md` | 25275 | `not computed` | policy |
| `R3119` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_SAD___DISAPPOINTED___PURPLE___RADIUS_65535.md` | 5017 | `not computed` | health, policy |
| `R3120` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_SEXUAL_DESIRE_IS_THE_WINDOW__PAIN_AND_PLEASURE_ARE_THE_GATE_KEEPERS__VIRTUE_AND.md` | 1471 | `not computed` | policy |
| `R3121` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_SITTING_IN_THAT_PLACE__SING_THE_GLORIOUS_PRAISES_OF_THE_LORD_FOREVER__AND_BE_ABS.md` | 2084 | `not computed` | policy |
| `R3122` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_SLOK_MHLW_1.md` | 441569 | `not computed` | policy |
| `R3123` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_SLOK_MHLW_5.md` | 513018 | `not computed` | policy |
| `R3124` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_SLOK_SHSIK_QI_MHLW_5.md` | 248751 | `not computed` | health |
| `R3125` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_SOME_DANCE_AND_DANCE_AND_KEEP_THE_BEAT__BUT_THEY_DO_NOT_WORSHIP_HIM_WITH.md` | 4982 | `not computed` | policy |
| `R3126` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_SOME_DO_NOT_UNDERSTAND_THEIR_ORIGINS__AND_WITHOUT_CAUSE__THEY_DISPLAY_THEIR_SELF.md` | 12003 | `not computed` | policy |
| `R3127` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_SONG_OF_SOLOMON.md` | 52560 | `not computed` | policy |
| `R3128` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_SONG_OF_SOLOMON_102.md` | 19067 | `not computed` | witness |
| `R3129` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_SONG_OF_SOLOMON_103.md` | 15752 | `not computed` | health |
| `R3130` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_SONG_OF_SOLOMON_104.md` | 25419 | `not computed` | policy |
| `R3131` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_SONG_OF_SOLOMON_105.md` | 23501 | `not computed` | witness |
| `R3132` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_SONG_OF_SOLOMON_106.md` | 16880 | `not computed` | health |
| `R3133` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_SONG_OF_SOLOMON_109.md` | 20404 | `not computed` | policy |
| `R3134` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_SONG_OF_SOLOMON_11.md` | 14790 | `not computed` | witness |
| `R3135` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_SONG_OF_SOLOMON_110.md` | 14777 | `not computed` | policy |
| `R3136` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_SONG_OF_SOLOMON_111.md` | 18812 | `not computed` | policy |
| `R3137` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_SONG_OF_SOLOMON_112.md` | 10768 | `not computed` | policy |
| `R3138` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_SONG_OF_SOLOMON_115.md` | 14365 | `not computed` | witness |
| `R3139` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_SONG_OF_SOLOMON_122.md` | 33587 | `not computed` | policy |
| `R3140` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_SONG_OF_SOLOMON_124.md` | 22966 | `not computed` | policy |
| `R3141` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_SONG_OF_SOLOMON_132.md` | 35164 | `not computed` | policy |
| `R3142` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_SONG_OF_SOLOMON_134.md` | 23800 | `not computed` | policy |
| `R3143` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_SONG_OF_SOLOMON_15.md` | 13979 | `not computed` | policy |
| `R3144` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_SONG_OF_SOLOMON_16.md` | 15326 | `not computed` | witness, policy |
| `R3145` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_SONG_OF_SOLOMON_22.md` | 21225 | `not computed` | policy |
| `R3146` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_SONG_OF_SOLOMON_27.md` | 18559 | `not computed` | witness |
| `R3147` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_SONG_OF_SOLOMON_29.md` | 13813 | `not computed` | policy |
| `R3148` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_SONG_OF_SOLOMON_31.md` | 16388 | `not computed` | policy |
| `R3149` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_SONG_OF_SOLOMON_35.md` | 19677 | `not computed` | policy |
| `R3150` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_SONG_OF_SOLOMON_36.md` | 17078 | `not computed` | policy |
| `R3151` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_SONG_OF_SOLOMON_50.md` | 19389 | `not computed` | witness |
| `R3152` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_SONG_OF_SOLOMON_51.md` | 18284 | `not computed` | witness |
| `R3153` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_SONG_OF_SOLOMON_61.md` | 10819 | `not computed` | policy |
| `R3154` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_SONG_OF_SOLOMON_62.md` | 8696 | `not computed` | witness |
| `R3155` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_SONG_OF_SOLOMON_65.md` | 8637 | `not computed` | health |
| `R3156` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_SONG_OF_SOLOMON_7.md` | 7714 | `not computed` | policy |
| `R3157` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_SONG_OF_SOLOMON_76.md` | 18542 | `not computed` | policy |
| `R3158` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_SONG_OF_SOLOMON_78.md` | 18668 | `not computed` | policy |
| `R3159` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_SONG_OF_SOLOMON_80.md` | 20125 | `not computed` | policy |
| `R3160` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_SONG_OF_SOLOMON_81.md` | 16120 | `not computed` | health, policy |
| `R3161` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_SONG_OF_SOLOMON_82.md` | 17920 | `not computed` | policy |
| `R3162` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_SONG_OF_SOLOMON_84.md` | 12581 | `not computed` | policy |
| `R3163` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_SONG_OF_SOLOMON_86.md` | 17185 | `not computed` | policy |
| `R3164` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_SONG_OF_SOLOMON_88.md` | 15683 | `not computed` | policy |
| `R3165` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_SONG_OF_SOLOMON_9.md` | 20661 | `not computed` | policy |
| `R3166` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_SONG_OF_SOLOMON_90.md` | 18227 | `not computed` | policy |
| `R3167` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_SONG_OF_SOLOMON_92.md` | 7805 | `not computed` | policy |
| `R3168` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_SONG_OF_SOLOMON_93.md` | 13486 | `not computed` | policy |
| `R3169` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_SONG_OF_SOLOMON_98.md` | 20746 | `not computed` | policy |
| `R3170` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_SONG_OF_SOLOMON_99.md` | 15602 | `not computed` | policy |
| `R3171` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_SORIT_MHLW_5_PMCPDW.md` | 9144 | `not computed` | policy |
| `R3172` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_SO_JOIN_TOGETHER_WITH_THE_HUMBLE_SAINTS__O_MADMAN__AND_YOU_SHALL_FIND_THE_GATE_O.md` | 9915 | `not computed` | policy |
| `R3173` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_SUHI_MHLW_1.md` | 124573 | `not computed` | format, policy |
| `R3174` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_SUHI_MHLW_4.md` | 138693 | `not computed` | health |
| `R3175` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_SWRG_MHLW_3.md` | 34957 | `not computed` | policy |
| `R3176` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_SWRG_MHLW_4.md` | 71027 | `not computed` | policy |
| `R3177` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_TAKING_UP_THE_FIVE_ARROWS_OF_VIRTUE__DEATH_IS_KILLED__DRAWING_THE_BOW_OF_THE_TEN.md` | 3510 | `not computed` | policy |
| `R3178` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_THEIR_MINDS_ARE_FOREVER_REJUVENATED__AND_THEY_NATURALLY__INTUITIVELY__SING_THE_G.md` | 2248 | `not computed` | policy |
| `R3179` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_THEIR_ROYAL_PROCESSION_EXTENDED_OVER_SIXTY_MILES__AND_YET_THEIR_BODIES_WERE_EATE.md` | 3543 | `not computed` | policy |
| `R3180` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_THERE_ARE_SO_MANY_STUBBORN_MINDED_INTELLIGENT_PEOPLE__AND_SO_MANY_WHO_CONTEMPLAT.md` | 4893 | `not computed` | policy |
| `R3181` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_THEY_DECORATE_THEMSELVES_WITH_THE_WORD_OF_THE_GURU_S_SHABAD__AND_THEIR_HUSBAND.md` | 2272 | `not computed` | policy |
| `R3182` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_THEY_FORFEIT_BOTH_THIS_WORLD_AND_THE_NEXT__AND_THEY_PASS_THEIR_LIVES_SUFFERING_I.md` | 6461 | `not computed` | policy |
| `R3183` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_THEY_OBTAIN_THE_PERFECT_VISION_OF_THE_LORD__WHILE_THOSE_WHO_GOSSIP_FIND_NO_PLACE.md` | 4891 | `not computed` | policy |
| `R3184` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_THE_CONGRESS_OF_THE_UNITED_STATES_SHALL_HAVE_POWER.md` | 2755 | `not computed` | policy |
| `R3185` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_THE_EGOTISTICAL_AND_PROUD_PERFORM_ALL_SORTS_OF_RITUALS__BUT_THEY_SHY_AWAY_FROM_T.md` | 4283 | `not computed` | policy |
| `R3186` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_THE_ESSENCE_OF_THE_NAAM__THE_NAME_OF_THE_LORD__IS_KNOWN_TO_BE_THE_MOST_EXALTED_A.md` | 3954 | `not computed` | policy |
| `R3187` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_THE_GREAT_GLORY_OF_MEETING_THE_TRUE_GURU_IS.md` | 6091 | `not computed` | policy |
| `R3188` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_THE_HEALTHY_PERSON_IS_VERY_SICK__IF_HE_DOES_NOT_REMEMBER_THE_LORD__THE_EMBODIMEN.md` | 1357 | `not computed` | health |
| `R3189` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_THE_IDA__THE_PINGALA_AND_THE_SUSHMANAA___O_HUMAN_BEING__HOW_CAN_THE_BREATHS.md` | 4306 | `not computed` | policy |
| `R3190` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_THE_INDRAS__SEATED_UPON_THEIR_CELESTIAL_THRONES__WITH_THE_DEITIES_AT_YOUR_GATE.md` | 1464 | `not computed` | policy |
| `R3191` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_THE_LORD_HAS_PLACED_THE_MAGIC_SPELL_OF_THE_SHABAD_INTO_HIS_MOUTH__AND_DESTROYED.md` | 3488 | `not computed` | format |
| `R3192` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_THE_MEDICINE_OF_THE_NAAM__AND_THE_IMMACULATE_WATER_OF_AMBROSIAL_NECTAR__ARE.md` | 11654 | `not computed` | policy |
| `R3193` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_THE_MEDICINE__THE_MANTRA__THE_MAGIC_CHARM__WILL_CURE_ALL_ILLNESSES_AND_TOTALLY_T.md` | 1780 | `not computed` | format |
| `R3194` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_THE_MINSTREL_ATTAINS_THE_LORD_S_GATE_AND_MANSION__AND_HE_KEEPS_THE_TRUE_LORD_CLA.md` | 879 | `not computed` | policy |
| `R3195` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_THE_POISONOUS_SNAKE__THE_SERPENT_OF_MAYA__HAS_SURROUNDED_THE_WORLD_WITH_ITS_COIL.md` | 2863 | `not computed` | format |
| `R3196` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_THE_RECORDING_SCRIBES_OF_THE_CONSCIOUS_AND_THE_UNCONSCIOUS__CHITR_AND_GUPT__KNOW.md` | 1954 | `not computed` | witness |
| `R3197` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_THE_SELF_WILLED_MANMUKHS_MAY_PRACTICE_RELIGIOUS_RITUALS__BUT_THEY_DO_NOT_OBTAIN.md` | 2135 | `not computed` | policy |
| `R3198` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_THE_SPIRITUAL_WARRIORS__THE_HEAVENLY_BEINGS__THE_SILENT_SAGES__THE_HUMBLE_AND_SE.md` | 6419 | `not computed` | policy |
| `R3199` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_THE_TENTH_GATE_OF_MY_CROWN_CHAKRA_IS_THE_DISTILLING_FIRE__AND_THE_CHANNELS_OF_TH.md` | 1585 | `not computed` | policy |
| `R3200` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_THE_TYRANNICAL_MESSENGER_OF_DEATH_CANNOT_TOUCH_YOU__AND_THE_SERPENT_OF_MAYA_CANN.md` | 4675 | `not computed` | policy |
| `R3201` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_THE_UNENLIGHTENED_PEOPLE_DO_NOT_UNDERSTAND_THEMSELVES___WHY_HAVE_THEY_BECOME.md` | 4886 | `not computed` | policy |
| `R3202` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_THE_UNION_OF_AIR__WATER_AND_FIRE.md` | 2953 | `not computed` | policy |
| `R3203` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_THE_UNITED_STATES_IN_CONGRESS_ASSEMBLED_SHALL_HAVE_AU.md` | 2296 | `not computed` | policy |
| `R3204` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_THE_WISE_ONE__SHIVA__REMAINS_ABSORBED_IN_HIMSELF__BUT_HE_IS_ENGROSSED_IN_DARK.md` | 14400 | `not computed` | policy |
| `R3205` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_THE_WORD_OF_THE_SHABAD_ABIDES_IN_THE_MIND_OF_THE_GURMUKHS__WHO_FIND_THE_GATE_OF.md` | 6296 | `not computed` | policy |
| `R3206` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_THOSE_BEINGS__WITHIN_WHOSE_INNER_SELVES_MY_LORD__HAR__HAR__DWELLS___ALL_THEIR_DI.md` | 3526 | `not computed` | health |
| `R3207` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_THOSE_WHOM_THE_GURU_HAS_PROTECTED_ARE_SAVED__CONTEMPLATING_THE_TRUE_WORD_OF_THE.md` | 6545 | `not computed` | policy |
| `R3208` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_THOSE_WHOM_YOU_CAUSE_TO_LISTEN_TO_YOUR_SERMON__FIND_PEACE_IN_THE_GURDWARA__THE.md` | 10961 | `not computed` | policy |
| `R3209` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_THOSE_WHO_DO_NOT_APPRECIATE_THE_VALUE_OF_THE_JEWELS__WANDER_LIKE_BLIND_MEN_IN_TH.md` | 2587 | `not computed` | policy |
| `R3210` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_THROUGH_LOVING_DEVOTION__AND_THE_PERFECT_TEACHINGS_OF_THE_GURU__THE_UNSTRUCK_SOU.md` | 7064 | `not computed` | policy |
| `R3211` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_THROUGH_THE_GURDWARA__THE_GURU_S_GATE__SOME_ARE_BLESSED_WITH_LOVING_FAITH__AND_T.md` | 2239 | `not computed` | policy |
| `R3212` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_THROUGH_THE_MAGIC_SPELL_OF_THE_GURU_S_SPIRITUAL_WISDOM__AND_MEDITATION_ON_THE_WO.md` | 1563 | `not computed` | format |
| `R3213` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_TIE_UP_THE_FIVE_DEMONS_OF_DESIRE_WITH_FAITH__CHARITY_AND_CONTENTMENT__AND_YOU_SH.md` | 8301 | `not computed` | policy |
| `R3214` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_TITUS.md` | 33227 | `not computed` | witness |
| `R3215` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_TITUS_1.md` | 8554 | `not computed` | witness |
| `R3216` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_TOFI_MHLW_5.md` | 166166 | `not computed` | witness |
| `R3217` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_TRANSPORT_AND_SAMPLING.md` | 1434 | `not computed` | policy |
| `R3218` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_TRUTH__CONTENTMENT_AND_INTUITIVE_PEACE_AND_POISE_ARE_OBTAINED_FROM_THE_BANI__THE.md` | 5880 | `not computed` | policy |
| `R3219` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_UNDER_THE_INSTRUCTION_OF_THE_GURU_S_SHABAD__ONE_SHEDS_EGOTISM_AND_CORRUPTION__AN.md` | 3314 | `not computed` | policy |
| `R3220` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_UNTIL_SHE_HAS_BEEN_PIERCED_THROUGH_WITH_THE_SHABAD__HOW_CAN_SHE_LOOK_BEAUTIFUL_A.md` | 2659 | `not computed` | policy |
| `R3221` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_UPWARD_COUPLING_FROM_WEATHER.md` | 1456 | `not computed` | policy |
| `R3222` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_USING_NORMALS_AS_IF_THEY.md` | 626 | `not computed` | policy |
| `R3223` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_VFHMSU_MHLW_3.md` | 512694 | `not computed` | policy |
| `R3224` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_WE_ARE_STILL_NOT_ENTIRELY_CERTAIN_WHY_STACK_RE_USE_FAILED_TO_PRO.md` | 1122 | `not computed` | health |
| `R3225` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_WE_HAVE_USED_THE_SIMPLE_PHONG_SHADING_MODEL_DUE_TO_AVAILABIL.md` | 1517 | `not computed` | policy |
| `R3226` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_WHEN_I_CAME_TO_UNDERSTAND_THIS_MIND__FROM_THE_TIPS_OF_MY_TOES_TO_THE_CROWN_OF_MY.md` | 4507 | `not computed` | policy |
| `R3227` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_WHEN_THE_KNOT_OF_THE_THREE_QUALITIES_IS_UNTIED__THEN_THE_TENTH_GATE_OPENS_UP__AN.md` | 965 | `not computed` | policy |
| `R3228` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_WHEN_YOU_ARE_CONSCIOUS_IN_YOUR_CONSCIOUSNESS__YOU_SHALL_BE_ENLIGHTENED_AND.md` | 3916 | `not computed` | policy |
| `R3229` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_WHY_DOES_THE_SHAYKH_BOTHER_TO_GO_ON_PILGRIMAGE_TO_MECCA__IF_HE_IS_NOT_CONTENT_WI.md` | 2815 | `not computed` | health |
| `R3230` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_WHY_THE_STRATOSPHERE_MATTERS_TO_THE_UPPER_ATMOSPHERE.md` | 1670 | `not computed` | policy |
| `R3231` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_WITHOUT_THE_HUMBLE_SAINTS__O_SIBLINGS_OF_DESTINY__NO_ONE_HAS_OBTAINED_THE_LORD_S.md` | 7451 | `not computed` | health |
| `R3232` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_WITHOUT_THE_NAAM__THE_NAME_OF_THE_LORD__ALL_THEIR_ACTIONS_ARE_USELESS__LIKE_THE.md` | 943 | `not computed` | format |
| `R3233` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_WITH_SO_MUCH_WEALTH_AND_CASH_AND_BURIED_TREASURE__STILL__HE_CANNOT_TAKE_ANYTHING.md` | 2181 | `not computed` | policy |
| `R3234` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_XXW_JAU_JWNIH_QAU_DURMIQ_HIN_KIR_BIS_KWIEAW_GWAU____342_6__GAUVI_PURBI__BGQ_KBIR.md` | 4800 | `not computed` | policy |
| `R3235` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_YOU_WORK_THE_WELL_AND_IRRIGATE_THE_FIELDS__BUT_THE_OXEN_HAVE_ALREADY_LEFT_TO_GRA.md` | 1459 | `not computed` | policy |
| `R3236` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_ZECHARIAH.md` | 98993 | `not computed` | policy |
| `R3237` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_ZECHARIAH_14.md` | 17746 | `not computed` | policy |
| `R3238` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_ZECHARIAH_7.md` | 7896 | `not computed` | policy |
| `R3239` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_ZEPHANIAH.md` | 25127 | `not computed` | policy |
| `R3240` | `C:\Users\ala\Documents\agent_god_files\prose_logic\output\GOD_ZEPHANIAH_1.md` | 11044 | `not computed` | policy |

## The one task
Set the CUA driver right in one pass: each correction below is a single artifact, and each exit test is a command that can fail. The driver is only correct when every action is ticketed, bounded, and witnessed — this is not a rule that a document can grant, it is what the receipts prove.

| Id | Correction | Reference | Exit test |
|---|---|---|---|
| D1 | Close `Q060`: carry `grade` in the digest preimage instead of leaving the field ruled but unimplemented. | `testport1/crates/planet-package/src/format_id.rs:103-128` | `python tools/hypergrill_reaudit.py --strict` reports zero `absent-on-disk` findings. |
| D2 | Rule the id width: the code truncates to 32 hex, so a 64-hex id is a change to the format, not a formatting choice. | `testport1/crates/planet-package/src/format_id.rs:128` | The ruling names one width and the truncation line either matches it or is deleted. |
| D3 | Resolve the Q063 tension between `domain|schema|len|payload` framing and a line-oriented preimage, without averaging the two. | `testport1/crates/planet-package/src/frame.rs:12-24` | One document states the frame; the other is superseded by name with its line cited. |
| D4 | Write the ruled manifest/Merkle shape into the architecture document. | `docs/SECURE-SHELL-RESTORE@1.HYPERGRILL.md §8.7` | The section quotes the ruling verbatim and the older shape is marked superseded. |
| D5 | Fix digest encoding at full 64 hex for both the manifest and the Merkle node. | `docs/SECURE-SHELL-RESTORE@1.HYPERGRILL.md §8.7` | A grep finds no remaining `[..32]` digest rendering outside the id function. |
| D6 | Add the cadence answer: the driver must not hardcode `ala-cities`' 20 Hz tick rate. | `testport1/docs/TICK-CADENCE.md:11` | The driver reads its cadence from config and a test fails when it is pinned to 20. |
| D7 | Bind every action to a witness: the driver reports, the server attests, and the driver holds no authority of its own. | `secure-shell/server/axis-driver.mjs:4,102` | A driver action without a witness receipt is refused, and the test that expects refusal passes. |
| D8 | Name the civilian refusal codes and make `cua-action` carry one. | `secure-shell/server/axis.mjs:24,110,155` | An action from an unwitnessed civilian returns its named code, not a bare failure. |
| D9 | Seal each tick into the ledger with the Ed25519 envelope. | `secure-shell/server/ledger.mjs:494-532` | A tampered receipt fails verification and the test asserts the failure. |
| D10 | Keep the mount receipt store as the one owner of mount state. | `secure-shell/tools/port/store.mjs:20-43` | A mount recorded twice is refused by the store rather than overwritten. |
| D11 | Point the signing seam at the voxel package's signing module instead of a second implementation. | `shploingus-clean/crates/voxel-package/src/signing.rs:57-110` | Exactly one signing path exists and the duplicate is deleted, not deprecated. |
| D12 | Name retention and deprecation as absent: the survey found no retention rule in any of the nine roots. | `docs/hypergrill/AUDIT@2026-11-04.md (survey, A-07)` | Either a retention rule is written with its pin, or the absence is recorded as `absent-on-disk`. |
