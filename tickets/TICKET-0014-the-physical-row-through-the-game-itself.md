# TICKET-0014 — the physical row, verified from the game's own state

Status: done (2026-11-05). Supersedes the PARTIAL verdict in `TICKET-0013` for CGA-14 / CGA-28.

## Why this is a ticket

`TICKET-0013` lowered three rows to `HELD` and left physical outcome verification at `PARTIAL`,
because the only adapter was `loopback-world`, a world this build wrote. A protocol enforced against
an adapter of our own is not evidence that a world we did not author confirmed anything. This ticket
records the adapter that closed that gap and changes the row's verdict.

## What was built

`../secure-shell/tools/game-adapter` — a Rust crate that depends on the game's own
`shploingus-voxel-world` by path, at its own workspace version (`0.1.0`), and serves three endpoints:

| Route | What it answers |
|---|---|
| `GET /version` | `{adapter: "shploingus-voxel", version, crate}` — the version the axis registers |
| `GET /state` | the body's position and the game's identity of the field it stands in |
| `POST /act` | `{actor, action, input:{x,y,z}}` — move the body, re-sample, answer the new observation |

The observation digest is `FieldSampleSet::identity()` computed inside the game crate. The adapter
does not hash anything: it asks the world and reports what the world says.

`server/world.mjs` gained one rule: an adapter that declares its own digest has that digest recorded
as the evidence (`source: adapter`), with the axis's own hash kept beside it as `stateDigest` for
integrity. The axis verifies the frame against the game's digest instead of substituting its own
hash of the game's state — otherwise the evidence would be the axis's again.

## Evidence

```
cargo build                                   -> Finished, exit 0
node --test server/test/*.test.mjs            -> 79 tests, 79 pass, 0 fail
node tools/axis-scale.mjs --drivers 1000 --game http://127.0.0.1:8788  -> exit 0
```

The scale run on 2026-11-05: 1 000 drivers, 1 000 cellframes, `actions {witness: 959, move: 40}`,
`tickets 1001`, `receipts 1000`, `verified 41` (40 loopback + 1 through the game), `witnessed 959`,
and four refusals firing (`cellframe-owner`, `world-not-verified`, `world-adapter-unknown`,
`cellframe-digest`). The game frame:

```
game: { adapter: "shploingus-voxel", version: "0.1.0", source: "adapter",
        digest: "sha256:4677a45c9339a88c4c5e9228b85f64e1bf4a41d5e1fc5a29c297d986f78bc008",
        state: { family: "lithology", rung: 3, samples: 4, seed: 20261105, x: 12, y: 0, z: 0 },
        cellframe: "sha256:347e45ade3b9160a7199d47cb889914551440f9678c8fe4b22257b0b9a29c3b9",
        ticket: "civ-0000:ticket:1" }
```

The digest moved from `sha256:47f2f53b…` at the origin to `sha256:4677a45c…` at `(12, 0, 0)`: the
outcome is the game's field identity after the body moved, not a frame the axis authored.

## What remains absent

A running Minecraft server and the mineflayer residents are not part of this run. The world
substrate is the game's own code and its identities are its own; the live multiplayer path needs a
server jar, a Java runtime for the mod, and `tools/headlessmc` to be started. No claim is made about
a body on a live server, and the report says exactly that instead of folding it into the pass.
