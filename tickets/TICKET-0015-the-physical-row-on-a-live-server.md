# TICKET-0015 — the physical row on a live server, from the residents that already existed

Status: done (2026-11-05). Supersedes the "no live Minecraft server" residual in `TICKET-0014`.

## Why this is a ticket

`TICKET-0014` verified the physical row through `shploingus-voxel-world`, the game's own substrate
crate. That is a world this build did not author, but it is a library: no server held it, no client
logged into it, and the row's own wording says "the game server remains the authority". A substrate
crate is not a server. This ticket records the run where a real 1.20.1 server was the authority and
a real client acted in it.

## What already existed, and was used rather than rebuilt

`ala_civ_bots_prototype` already carries the pieces; nothing was downloaded:

| Piece | Where it was | Evidence |
|---|---|---|
| Server jar 1.20.1 | `~/.gradle/caches/fabric-loom/1.20.1/minecraft-server.jar` | copied to `run/live-mc/server.jar` |
| JVM | `Eclipse Adoptium jdk-21.0.10.7-hotspot` (the project's `JAVA_HOME` is 25, which this server does not want) | `java -version` |
| Client | `tools/residents/node_modules/mineflayer` 4.39.0 | installed already |
| Body driver | `tools/residents/src/pathfinder.mjs` (`Movements`, `goals`, `pathfinder`) | the residents' own wrapper |

The server runs in `run/live-mc` — a separate flat world on port 25566 — so the project's 187 MB
`run/world` and its `devserver.sh` parity gates are untouched. `run/` is gitignored.

## What was added

`ala_civ_bots_prototype/tools/residents/world-adapter.mjs` — a world adapter over a live session:

| Route | What it answers |
|---|---|
| `GET /version` | `minecraft-live`, `1.20.1`, the server address, whether the body is online |
| `GET /state` | position, `on_ground`, and a digest over the position plus every block within ±3 |
| `POST /act` | `{actor, action:"move"|"dig", input:{x,y,z}}` → the observation after the act |

Every value comes from server packets: position from entity-move, blocks from chunk and
block-update. A block that has not arrived is `unloaded`, never a guess. The dig path only reports a
removal when the server's own block update says `air`.

`secure-shell/tools/axis-scale.mjs` acts from the world's reported position and now **fails the run
when the digest does not change** — an adapter that answers an act with the same world is refused by
the scale run, not merely by the axis.

## Evidence

```
java -jar server.jar nogui              -> Done (2.515s)!, listening on 0.0.0.0:25566
server log                              -> AxisBody[/127.0.0.1:51209] logged in with entity id 1
                                                  at (3.5, -60.0, -2.5)
GET /state                              -> sha256:fc7cfa2449575c09… position 3.5,-60,-2.5
POST /act move {6,-60,-3}               -> sha256:0ee6c3f56d4d2680… walked 1.91 blocks
POST /act dig  {6,-61,-3}               -> sha256:f49ceb591814e6ad… dug grass_block -> air
node tools/axis-scale.mjs --drivers 1000 --game http://127.0.0.1:8789   -> exit 0
```

The scale run: 1 000 drivers, 1 000 cellframes, `actions {witness: 959, move: 40}`, tickets 1 001,
receipts 1 000, `verified 41` — the 41st is the frame through the live server, citing
`sha256:f49ceb59…` with `source: adapter` — 959 witnessed, six stars, nine ladders, four refusals
(`cellframe-owner`, `world-not-verified`, `world-adapter-unknown`, `cellframe-digest`), no failures.

## What this does not claim

The body is a mineflayer session, not the headless Fabric client. The server-side mind, the mod's
control bridge and `tools/headlessmc` are not exercised; the adapter is a motor, and the axis
verified what the server reported the motor did.
