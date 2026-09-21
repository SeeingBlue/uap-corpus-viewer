// smoke_viewer.mjs - runtime smoke test for deploy/index.html.
//
// Drives headless Chrome over the DevTools Protocol (no npm deps; Node >= 22
// for the built-in WebSocket): loads the viewer, toggles a release chip,
// opens a record, visits every tab, and reports key DOM facts plus any
// uncaught exception or console error. Run after update_deploy.py:
//
//   node scripts/smoke_viewer.mjs
//
// validate_deploy.py checks the inlined JSON; this checks the page runs.
import { spawn } from "node:child_process";

const CHROME = process.env.CHROME_PATH || "C:/Program Files/Google/Chrome/Application/chrome.exe";
import { fileURLToPath, pathToFileURL } from "node:url";
import { dirname, resolve } from "node:path";
const URL = pathToFileURL(resolve(dirname(fileURLToPath(import.meta.url)), "..", "deploy", "index.html")).href;
const PORT = 9333;
const chrome = spawn(CHROME, [
  "--headless=new", "--disable-gpu", "--no-sandbox", `--remote-debugging-port=${PORT}`,
  "--user-data-dir=" + process.env.TEMP + "/uap-smoke-profile", "about:blank",
], { stdio: "ignore" });
const sleep = (ms) => new Promise(r => setTimeout(r, ms));

let ws, id = 0; const pending = new Map(); const errors = [];
function send(method, params = {}) {
  return new Promise((resolve, reject) => {
    const mid = ++id; pending.set(mid, { resolve, reject });
    ws.send(JSON.stringify({ id: mid, method, params }));
  });
}
async function evalJs(expression) {
  const r = await send("Runtime.evaluate", { expression, returnByValue: true, awaitPromise: true });
  if (r.exceptionDetails) throw new Error(JSON.stringify(r.exceptionDetails).slice(0, 500));
  return r.result.value;
}

try {
  let targets;
  for (let i = 0; i < 40; i++) {
    try { targets = await (await fetch(`http://127.0.0.1:${PORT}/json`)).json(); break; } catch { await sleep(250); }
  }
  const page = targets.find(t => t.type === "page");
  ws = new WebSocket(page.webSocketDebuggerUrl);
  await new Promise(r => ws.onopen = r);
  ws.onmessage = (ev) => {
    const m = JSON.parse(ev.data);
    if (m.id && pending.has(m.id)) { pending.get(m.id).resolve(m.result); pending.delete(m.id); return; }
    if (m.method === "Runtime.exceptionThrown") errors.push("EXC " + (m.params.exceptionDetails.exception?.description || m.params.exceptionDetails.text).slice(0, 300));
    if (m.method === "Runtime.consoleAPICalled" && (m.params.type === "error" || m.params.type === "warning"))
      errors.push("CONSOLE." + m.params.type + " " + m.params.args.map(a => a.value ?? a.description).join(" ").slice(0, 300));
  };
  await send("Runtime.enable"); await send("Page.enable");
  await send("Page.navigate", { url: URL });
  await sleep(6000);

  const out = {};
  out.title = await evalJs("document.title");
  out.header = await evalJs("document.querySelector('.meta.mono').textContent");
  out.statTotal = await evalJs("document.getElementById('stat-total').textContent");
  out.chips = await evalJs("[...document.querySelectorAll('#filters .chip[data-filter=release]')].map(c=>c.textContent.trim()).join(' | ')");
  out.cntLLE = await evalJs("document.getElementById('cnt-LLE').textContent");
  out.rowsR6 = await evalJs("document.querySelectorAll('#timeline .row.r6').length");
  out.rowsR5 = await evalJs("document.querySelectorAll('#timeline .row.r5').length");
  // toggle R6 chip off and on
  out.afterR6Off = await evalJs("document.querySelector('#filters .chip[data-value=R6]').click(); document.getElementById('stat-total').textContent");
  out.afterR6On = await evalJs("document.querySelector('#filters .chip[data-value=R6]').click(); document.getElementById('stat-total').textContent");
  // click an R6 row -> detail badge
  out.detailBadge = await evalJs("document.querySelector('#timeline .row.r6 .title').click(); [...document.querySelectorAll('#detail-body .badge')].map(b=>b.className+':'+b.textContent).join(' | ')");
  for (const v of ["globe", "patterns", "releases"]) {
    await evalJs(`document.querySelector('nav.tabs button[data-view=${v}]').click()`);
    await sleep(v === "globe" ? 5000 : 2500);
    out["view_" + v] = await evalJs("document.getElementById('view').innerHTML.length");
  }
  out.globeLegend = await evalJs("document.querySelector('nav.tabs button[data-view=globe]').click(); ''");
  await sleep(4000);
  out.globeLegend = await evalJs("(document.getElementById('globe-legend')||{}).textContent");
  out.globePtsR6 = await evalJs("document.querySelectorAll('.globe-pt.r6').length");
  await evalJs("document.querySelector('nav.tabs button[data-view=releases]').click()");
  await sleep(2000);
  out.releasesBanner = await evalJs("(document.querySelector('.pat-banner')||{}).textContent");
  out.releasesCols = await evalJs("[...document.querySelectorAll('.pat-cross-era thead th')].slice(0,8).map(t=>t.textContent).join(' | ')");
  out.findingsCount = await evalJs("document.querySelector('nav.tabs button[data-view=patterns]').click(); document.querySelectorAll('.pat-finding').length");
  console.log(JSON.stringify(out, null, 1));
  console.log("ERRORS:", errors.length ? errors : "none");
} catch (e) {
  console.log("SMOKE FAILED:", e.message);
} finally {
  try { ws && ws.close(); } catch {}
  chrome.kill();
  process.exit(0);
}
