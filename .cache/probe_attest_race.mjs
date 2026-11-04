/**
 * Probe: is the lapsed-attestation test racing a wall clock?
 *
 * The test mints an attestation that expires 20 ms from now, then does an HTTP round trip to register
 * it. If the JS thread stalls longer than 20 ms before that request lands, the axis itself refuses the
 * attestation ("expiry is not in the future") and the test fails before reaching the assertion it was
 * written for. This probe does exactly that, with the stall made explicit.
 */

import { mkdtempSync, writeFileSync } from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";

import { createAxisServer } from "../../secure-shell/server/axis-server.mjs";
import { createDriver } from "../../secure-shell/server/axis-driver.mjs";

const app = createAxisServer({});
const address = await app.listen(0);
const root = mkdtempSync(join(tmpdir(), "probe-attest-race-"));
const driver = createDriver({
  id: "probe-node",
  revision: "1",
  axisUrl: "http://127.0.0.1:" + address.port,
  stateDir: root,
});

await driver.register();
writeFileSync(join(root, "lesson.txt"), "lesson: too late");

const expiresAt = Date.now() + 20;
const until = Date.now() + 40;
while (Date.now() < until) {
  // a 40 ms stall on the thread — what a loaded machine supplies for free
}

try {
  await driver.attest({ verifier: "debian-store", expiresAt });
  console.log("result: attest accepted, so no race in this shape");
} catch (error) {
  console.log("result: attest refused ->", error.code, "|", error.why);
}

await app.close();
