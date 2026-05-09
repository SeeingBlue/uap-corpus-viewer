"""build_viz.py - emit a self-contained viewer.html for the corpus.

Reads metadata/index.json, metadata/entities.json, metadata/cross_refs.json
and inlines them into a single HTML file with d3-based network graph,
searchable list, timeline, and per-record detail panel.

Output: viewer.html in the project root.
"""

from __future__ import annotations
import json, re
from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).resolve().parent.parent
INDEX = ROOT / "metadata" / "index.json"
ENTITIES = ROOT / "metadata" / "entities.json"
CROSS = ROOT / "metadata" / "cross_refs.json"
OUT = ROOT / "viewer.html"


def _normalize_2digit_year(s):
    """1947-2026 corpus pivot for 2-digit years: yy>=27 -> 19xx else 20xx."""
    m = re.match(r"^(\d{1,2})/(\d{1,2})/(\d{2})\b(.*)$", s)
    if m:
        mo, day, yy, rest = m.groups()
        yyi = int(yy)
        full = (1900 + yyi) if yyi >= 27 else (2000 + yyi)
        return f"{mo}/{day}/{full}{rest}"
    return s


def parse_date_iso(s):
    s = (s or "").strip()
    if not s or s.upper() == "N/A":
        return None
    s_norm = _normalize_2digit_year(s)
    for fmt in ("%m/%d/%Y", "%Y-%m-%d", "%B %Y", "%B %d, %Y", "%d %B %Y"):
        try:
            return datetime.strptime(s_norm, fmt).date().isoformat()
        except ValueError:
            pass
    m = re.search(r"(\d{4})", s)
    if m:
        return f"{m.group(1)}-01-01"
    return None


def main():
    idx = json.loads(INDEX.read_text(encoding="utf-8-sig"))
    entities = json.loads(ENTITIES.read_text(encoding="utf-8"))
    cross = json.loads(CROSS.read_text(encoding="utf-8"))

    # Prepare records: trim to fields the UI needs (smaller payload, faster page)
    records = []
    for r in idx["files"]:
        rid = r["id"]
        e = entities.get(rid, {})
        # Year for timeline x-axis: prefer the audited inferred date.
        inferred = (r.get("incident_date_inferred") or "").strip()
        if inferred:
            date_iso = inferred if len(inferred) == 10 else (
                f"{inferred}-01" if len(inferred) == 7 else f"{inferred}-01-01"
            )
        else:
            date_iso = parse_date_iso(r.get("incident_date"))
        year = int(date_iso[:4]) if date_iso else None
        records.append({
            "id": rid,
            "type": r["type"],
            "title": r["title"],
            "agency": r["agency"],
            "agency_raw": r.get("agency_raw", ""),
            "release_date": r.get("release_date", ""),
            "incident_date": r.get("incident_date", ""),
            "incident_date_inferred": r.get("incident_date_inferred", ""),
            "incident_date_inferred_source": r.get("incident_date_inferred_source", ""),
            "incident_date_inferred_csv_disagrees": bool(r.get("incident_date_inferred_csv_disagrees")),
            "incident_location": r.get("incident_location", ""),
            "incident_location_inferred": r.get("incident_location_inferred", ""),
            "incident_location_inferred_source": r.get("incident_location_inferred_source", ""),
            "incident_location_inferred_csv_disagrees": bool(r.get("incident_location_inferred_csv_disagrees")),
            "summary": r.get("summary", ""),
            "redaction": r.get("redaction", ""),
            "source_url": r.get("source_url", ""),
            "modal_image_url": r.get("modal_image_url", ""),
            "bytes": r.get("bytes", 0),
            "sha256": r.get("sha256", ""),
            "extracted_text_path": r.get("extracted_text_path"),
            "year": year,
            "ents": {
                "military_units":  e.get("military_units", [])[:30],
                "classification":  e.get("classification", [])[:10],
                "us_states":       e.get("us_states", [])[:30],
                "aircraft":        e.get("aircraft", [])[:20],
                "operations":      e.get("operations", [])[:10],
                "case_numbers":    e.get("case_numbers", [])[:10],
                "names":           e.get("names", [])[:25],
                "mgrs":            e.get("mgrs", [])[:10],
            },
        })

    pairs = cross.get("cross_refs", {})
    # Edges as undirected list of {source, target}
    seen = set()
    edges = []
    for rid, others in pairs.items():
        for o in others:
            key = tuple(sorted([rid, o]))
            if key in seen:
                continue
            seen.add(key)
            edges.append({"source": key[0], "target": key[1]})

    data = {
        "snapshot_date": idx.get("first_snapshot", ""),
        "total": len(records),
        "records": records,
        "edges": edges,
    }

    payload = json.dumps(data, ensure_ascii=False, separators=(",", ":"))

    # Build the HTML
    html = HTML_TEMPLATE.replace("__DATA_PAYLOAD__", payload)
    OUT.write_text(html, encoding="utf-8")
    print(f"wrote {OUT}  ({OUT.stat().st_size:,} bytes)")
    print(f"  records: {len(records)}")
    print(f"  edges:   {len(edges)}")


HTML_TEMPLATE = r"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>war.gov UAP Release 01 — corpus viewer</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
  :root {
    --bg: #0b0d0f;
    --bg2: #14181c;
    --bg3: #1d242b;
    --fg: #d8dee4;
    --muted: #8896a3;
    --accent: #4cc2ff;
    --accent2: #ffb84c;
    --border: #2a3440;
    --pdf: #4cc2ff;
    --video: #ffb84c;
    --image: #b385ff;
    --redact: #ff5c5c;
  }
  * { box-sizing: border-box; }
  html, body { margin:0; padding:0; height:100%; background:var(--bg); color:var(--fg);
    font: 13px/1.5 -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }
  a { color: var(--accent); text-decoration:none; } a:hover { text-decoration:underline; }
  code, .mono { font-family: ui-monospace, "SF Mono", Consolas, "Roboto Mono", monospace; }
  header {
    border-bottom: 1px solid var(--border); padding: 14px 20px;
    background: linear-gradient(180deg, #0e1216 0%, #0b0d0f 100%);
    display:flex; align-items:center; gap:18px; flex-wrap:wrap;
  }
  header h1 { margin:0; font-size:16px; font-weight:600; }
  header .meta { color: var(--muted); font-size:12px; }
  header .stats { margin-left:auto; display:flex; gap:14px; font-size:12px; color:var(--muted); }
  header .stats b { color: var(--fg); }
  nav.tabs { display:flex; gap:2px; padding: 8px 20px; background:var(--bg2); border-bottom:1px solid var(--border); }
  nav.tabs button {
    background:transparent; border:none; color:var(--muted); padding:8px 14px;
    font: inherit; cursor:pointer; border-bottom: 2px solid transparent;
  }
  nav.tabs button.active { color: var(--fg); border-bottom-color: var(--accent); }
  nav.tabs button:hover { color: var(--fg); }
  main { display:grid; grid-template-columns: minmax(0, 1fr) 480px; height: calc(100vh - 100px); }
  #view { overflow:auto; padding: 16px 20px; }
  #detail {
    border-left: 1px solid var(--border); background: var(--bg2);
    overflow:auto; padding: 16px 20px;
  }
  #filters {
    display:flex; gap:8px; flex-wrap:wrap; align-items:center;
    margin-bottom: 12px; padding: 10px 12px; background: var(--bg2);
    border:1px solid var(--border); border-radius:6px;
  }
  #filters input[type=search] {
    background: var(--bg3); border:1px solid var(--border); color:var(--fg);
    padding: 6px 10px; border-radius: 4px; min-width: 240px; font: inherit;
  }
  #filters select, #filters button {
    background: var(--bg3); border:1px solid var(--border); color:var(--fg);
    padding: 6px 10px; border-radius: 4px; font: inherit; cursor:pointer;
  }
  #filters .chip {
    padding: 3px 8px; border-radius: 3px; font-size: 11px;
    border: 1px solid var(--border); cursor:pointer; user-select:none;
  }
  #filters .chip.on { background: var(--bg3); border-color: var(--accent); color: var(--fg); }
  #filters .chip.off { color: var(--muted); }
  table.records { width:100%; border-collapse: collapse; font-size: 12px; }
  table.records th, table.records td {
    text-align:left; padding: 6px 8px; border-bottom: 1px solid var(--border);
    vertical-align: top;
  }
  table.records th { color: var(--muted); font-weight: 500; cursor:pointer; user-select:none; }
  table.records tr { cursor: pointer; }
  table.records tr:hover { background: var(--bg2); }
  table.records tr.selected { background: var(--bg3); }
  .badge {
    display:inline-block; padding: 1px 6px; border-radius: 3px; font-size: 10px;
    font-weight: 600; text-transform: uppercase; letter-spacing: 0.4px;
  }
  .badge.pdf { background: rgba(76,194,255,0.16); color: var(--pdf); }
  .badge.video { background: rgba(255,184,76,0.16); color: var(--video); }
  .badge.image { background: rgba(179,133,255,0.16); color: var(--image); }
  .badge.redact { background: rgba(255,92,92,0.16); color: var(--redact); }
  .badge.agency { background: var(--bg3); color: var(--fg); }
  #detail h2 { margin:0 0 6px 0; font-size: 16px; }
  #detail .id { color: var(--muted); font-size: 11px; margin-bottom: 10px; }
  #detail .summary {
    border-left: 3px solid var(--accent); background: var(--bg3);
    padding: 8px 12px; margin: 10px 0; font-size: 12px; color: var(--fg);
  }
  #detail .meta-grid {
    display: grid; grid-template-columns: 110px 1fr; gap: 4px 12px;
    font-size: 12px; margin: 8px 0;
  }
  #detail .meta-grid dt { color: var(--muted); }
  #detail .meta-grid dd { margin:0; word-break:break-word; }
  #detail .ent-section { margin-top: 14px; }
  #detail .ent-section h4 { margin: 6px 0 4px; font-size: 11px; color: var(--muted);
    text-transform:uppercase; letter-spacing: 0.5px; font-weight: 600; }
  .pill {
    display:inline-block; padding: 2px 7px; margin: 2px 3px 2px 0;
    background: var(--bg3); border:1px solid var(--border); border-radius: 10px;
    font-size: 11px; cursor: pointer;
  }
  .pill:hover { border-color: var(--accent); color: var(--accent); }
  #graph { width: 100%; height: 100%; }
  #graph svg { width: 100%; height: 100%; display:block; }
  #graph .node { stroke: var(--bg); stroke-width: 1.5; cursor: pointer; }
  #graph .node.pdf { fill: var(--pdf); }
  #graph .node.video { fill: var(--video); }
  #graph .node.image { fill: var(--image); }
  #graph .node.selected { stroke: var(--fg); stroke-width: 2.5; }
  #graph .link { stroke: var(--border); stroke-width: 1.2; }
  #graph .label { fill: var(--muted); font-size: 10px; pointer-events: none; }

  #timeline { padding: 6px 0; }
  #timeline .row { display:flex; align-items:center; gap:8px; padding: 2px 0; font-size:12px; }
  #timeline .row .year { width:60px; color: var(--muted); font-family: ui-monospace, monospace; }
  #timeline .row .marker {
    display:inline-block; width:10px; height:10px; border-radius:50%;
    background: var(--pdf); cursor: pointer;
  }
  #timeline .row .marker.video { background: var(--video); }
  #timeline .row .marker.image { background: var(--image); }
  #timeline .row .title { flex: 1; cursor: pointer; }
  #timeline .row:hover { background: var(--bg2); }
  #timeline .row.selected { background: var(--bg3); }
  #timeline h3 { margin: 18px 0 4px; font-size: 13px; color: var(--accent); }

  #locations h3 { margin: 16px 0 4px; font-size: 13px; }
  #locations h3 .count { color: var(--muted); font-weight:400; font-size: 11px; }

  .empty { color: var(--muted); padding: 16px; text-align: center; }

  ::-webkit-scrollbar { width: 10px; height: 10px; }
  ::-webkit-scrollbar-track { background: var(--bg); }
  ::-webkit-scrollbar-thumb { background: var(--bg3); border-radius: 4px; }
  ::-webkit-scrollbar-thumb:hover { background: var(--border); }
</style>
</head>
<body>

<header>
  <h1>war.gov / UFO — Release 01</h1>
  <span class="meta mono">PURSUE · snapshot 2026-05-08 · 161 records</span>
  <div class="stats">
    <span><b id="stat-total">—</b> visible</span>
    <span><b id="stat-pairs">—</b> pairings</span>
  </div>
</header>

<nav class="tabs">
  <button class="active" data-view="list">List</button>
  <button data-view="graph">Network</button>
  <button data-view="timeline">Timeline</button>
  <button data-view="locations">By location</button>
</nav>

<div id="filters">
  <input type="search" id="q" placeholder="Search title, summary, location, names…">
  <span class="chip on" data-filter="agency" data-value="DoW">DoW <b id="cnt-DoW"></b></span>
  <span class="chip on" data-filter="agency" data-value="FBI">FBI <b id="cnt-FBI"></b></span>
  <span class="chip on" data-filter="agency" data-value="NASA">NASA <b id="cnt-NASA"></b></span>
  <span class="chip on" data-filter="agency" data-value="State">State <b id="cnt-State"></b></span>
  <span class="chip on" data-filter="type" data-value="pdf">PDF</span>
  <span class="chip on" data-filter="type" data-value="video">Video</span>
  <span class="chip on" data-filter="type" data-value="image">Image</span>
  <span class="chip on" data-filter="redact" data-value="redact">Redacted</span>
  <span class="chip on" data-filter="redact" data-value="clean">Clean</span>
  <button id="reset">reset</button>
</div>

<main>
  <section id="view"></section>
  <aside id="detail"><div class="empty">click a record to see details</div></aside>
</main>

<script src="https://cdnjs.cloudflare.com/ajax/libs/d3/7.8.5/d3.min.js"></script>
<script>
  // Inlined data
  const DATA = __DATA_PAYLOAD__;
  const records = DATA.records;
  const edges = DATA.edges;
  const byId = Object.fromEntries(records.map(r => [r.id, r]));

  // Build neighbor lookup
  const neighbors = {};
  edges.forEach(e => {
    (neighbors[e.source] = neighbors[e.source] || new Set()).add(e.target);
    (neighbors[e.target] = neighbors[e.target] || new Set()).add(e.source);
  });

  // Filter state
  const filters = {
    q: "",
    agency: new Set(["DoW", "FBI", "NASA", "State"]),
    type:   new Set(["pdf", "video", "image"]),
    redact: new Set(["redact", "clean"]),
  };
  let view = "list";
  let selectedId = null;
  let sortKey = "id"; let sortAsc = true;

  function visible() {
    const q = filters.q.toLowerCase();
    return records.filter(r => {
      if (!filters.agency.has(r.agency)) return false;
      if (!filters.type.has(r.type)) return false;
      const isRedacted = (r.redaction || "").toUpperCase() === "TRUE";
      if (isRedacted && !filters.redact.has("redact")) return false;
      if (!isRedacted && !filters.redact.has("clean")) return false;
      if (q) {
        const hay = [
          r.id, r.title, r.summary, r.incident_location, r.incident_date,
          (r.ents.us_states || []).join(" "),
          (r.ents.military_units || []).join(" "),
          (r.ents.names || []).join(" "),
          (r.ents.case_numbers || []).join(" "),
          (r.ents.aircraft || []).join(" "),
          (r.ents.operations || []).join(" "),
        ].join(" ").toLowerCase();
        if (!hay.includes(q)) return false;
      }
      return true;
    });
  }

  function fmtBytes(n) {
    if (!n) return "—";
    if (n < 1024) return n + " B";
    if (n < 1024*1024) return (n/1024).toFixed(0) + " KB";
    return (n/1024/1024).toFixed(1) + " MB";
  }

  function escapeHtml(s) {
    return String(s == null ? "" : s)
      .replaceAll("&", "&amp;").replaceAll("<", "&lt;")
      .replaceAll(">", "&gt;").replaceAll('"', "&quot;");
  }

  function badge(text, cls) {
    return `<span class="badge ${cls}">${escapeHtml(text)}</span>`;
  }

  function pillList(arr, max) {
    if (!arr || !arr.length) return '<span style="color:var(--muted)">—</span>';
    const sl = arr.slice(0, max || 30);
    return sl.map(t => `<span class="pill" data-q="${escapeHtml(t)}">${escapeHtml(t)}</span>`).join("");
  }

  // ---- Renderers ------------------------------------------------------

  function renderList(rows) {
    const view = document.getElementById("view");
    rows = rows.slice().sort((a, b) => {
      // For the incident-date column, sort by the inferred date when present.
      const key = sortKey;
      let av, bv;
      if (key === "incident_date") {
        av = a.incident_date_inferred || a.incident_date;
        bv = b.incident_date_inferred || b.incident_date;
      } else {
        av = a[key]; bv = b[key];
      }
      av = av == null ? "" : av; bv = bv == null ? "" : bv;
      if (typeof av === "number" && typeof bv === "number") {
        return sortAsc ? av - bv : bv - av;
      }
      return sortAsc ? String(av).localeCompare(String(bv)) :
                       String(bv).localeCompare(String(av));
    });

    let html = `<table class="records"><thead><tr>
      <th data-sort="id">id</th>
      <th data-sort="type">type</th>
      <th data-sort="agency">agency</th>
      <th data-sort="incident_date">incident</th>
      <th data-sort="incident_location">location</th>
      <th data-sort="title">title</th>
      <th data-sort="bytes">size</th>
    </tr></thead><tbody>`;
    rows.forEach(r => {
      const isRedacted = (r.redaction || "").toUpperCase() === "TRUE";
      html += `<tr data-id="${r.id}" class="${selectedId === r.id ? 'selected':''}">
        <td><code>${escapeHtml(r.id.length > 50 ? r.id.slice(0,50)+'…' : r.id)}</code></td>
        <td>${badge(r.type, r.type)}</td>
        <td>${badge(r.agency, "agency")}</td>
        <td class="mono">${escapeHtml(r.incident_date_inferred || r.incident_date || "—")}${r.incident_date_inferred_csv_disagrees ? '<span title="CSV value disagrees with inferred date" style="color:var(--accent2);margin-left:4px">*</span>' : ''}</td>
        <td>${escapeHtml(r.incident_location_inferred || r.incident_location || "—")}${r.incident_location_inferred_csv_disagrees ? '<span title="CSV value disagrees with inferred location" style="color:var(--accent2);margin-left:4px">*</span>' : ''}</td>
        <td>${escapeHtml(r.title)} ${isRedacted ? badge("redact", "redact") : ""}</td>
        <td class="mono">${fmtBytes(r.bytes)}</td>
      </tr>`;
    });
    html += `</tbody></table>`;
    view.innerHTML = html;
    view.querySelectorAll("th[data-sort]").forEach(th => {
      th.onclick = () => {
        const k = th.dataset.sort;
        if (sortKey === k) sortAsc = !sortAsc; else { sortKey = k; sortAsc = true; }
        rerender();
      };
    });
    view.querySelectorAll("tr[data-id]").forEach(tr => {
      tr.onclick = () => selectRecord(tr.dataset.id);
    });
  }

  function renderGraph(rows) {
    const view = document.getElementById("view");
    view.innerHTML = '<div id="graph"></div>';
    const container = document.getElementById("graph");
    const w = container.clientWidth, h = container.clientHeight;

    const visIds = new Set(rows.map(r => r.id));
    const nodes = rows.map(r => ({ id: r.id, type: r.type, agency: r.agency, title: r.title, bytes: r.bytes }));
    const visEdges = edges.filter(e => visIds.has(e.source) && visIds.has(e.target));

    const svg = d3.select(container).append("svg").attr("viewBox", `0 0 ${w} ${h}`);
    const g = svg.append("g");

    const sim = d3.forceSimulation(nodes)
      .force("link", d3.forceLink(visEdges).id(d => d.id).distance(60).strength(0.6))
      .force("charge", d3.forceManyBody().strength(-90))
      .force("center", d3.forceCenter(w/2, h/2))
      .force("collide", d3.forceCollide(8));

    const link = g.append("g").selectAll("line").data(visEdges).enter().append("line")
      .attr("class", "link");
    const node = g.append("g").selectAll("circle").data(nodes).enter().append("circle")
      .attr("class", d => `node ${d.type}`)
      .attr("r", d => Math.min(12, Math.max(3, Math.log10((d.bytes||1)+1))))
      .on("click", (ev, d) => selectRecord(d.id))
      .call(d3.drag()
        .on("start", (ev, d) => { if (!ev.active) sim.alphaTarget(0.3).restart(); d.fx = d.x; d.fy = d.y; })
        .on("drag",  (ev, d) => { d.fx = ev.x; d.fy = ev.y; })
        .on("end",   (ev, d) => { if (!ev.active) sim.alphaTarget(0); d.fx = null; d.fy = null; }));
    node.append("title").text(d => d.title);

    sim.on("tick", () => {
      link.attr("x1", d => d.source.x).attr("y1", d => d.source.y)
          .attr("x2", d => d.target.x).attr("y2", d => d.target.y);
      node.attr("cx", d => d.x).attr("cy", d => d.y);
    });

    svg.call(d3.zoom().scaleExtent([0.3, 5]).on("zoom", (ev) => {
      g.attr("transform", ev.transform);
    }));
  }

  function renderTimeline(rows) {
    const view = document.getElementById("view");
    const buckets = {};
    rows.forEach(r => {
      const y = r.year || "—";
      (buckets[y] = buckets[y] || []).push(r);
    });
    const years = Object.keys(buckets).sort((a, b) => {
      if (a === "—") return 1; if (b === "—") return -1;
      return Number(a) - Number(b);
    });
    let html = '<div id="timeline">';
    years.forEach(y => {
      html += `<h3>${y === "—" ? "(no incident date)" : y}  <span style="color:var(--muted);font-weight:400;font-size:11px">${buckets[y].length} records</span></h3>`;
      buckets[y].forEach(r => {
        const isRed = (r.redaction || "").toUpperCase() === "TRUE";
        html += `<div class="row ${selectedId === r.id ? 'selected':''}" data-id="${r.id}">
          <span class="year">${escapeHtml(r.incident_date_inferred || r.incident_date || "—")}</span>
          <span class="marker ${r.type}"></span>
          ${badge(r.agency, "agency")}
          <span class="title">${escapeHtml(r.title)}${isRed ? ' '+badge("redact","redact") : ''}</span>
          <span class="mono" style="color:var(--muted)">${escapeHtml(r.incident_location_inferred || r.incident_location || "")}</span>
        </div>`;
      });
    });
    html += '</div>';
    view.innerHTML = html;
    view.querySelectorAll(".row[data-id]").forEach(el => {
      el.onclick = () => selectRecord(el.dataset.id);
    });
  }

  function renderLocations(rows) {
    const view = document.getElementById("view");
    const buckets = {};
    rows.forEach(r => {
      const loc = (r.incident_location_inferred || r.incident_location || "").trim() || "Unknown";
      (buckets[loc] = buckets[loc] || []).push(r);
    });
    const locs = Object.keys(buckets).sort((a, b) => buckets[b].length - buckets[a].length);
    let html = '<div id="locations">';
    locs.forEach(loc => {
      html += `<h3>${escapeHtml(loc)} <span class="count">${buckets[loc].length} records</span></h3>`;
      buckets[loc].forEach(r => {
        html += `<div class="row" data-id="${r.id}" style="display:flex;gap:8px;padding:2px 0;cursor:pointer">
          ${badge(r.agency, "agency")} ${badge(r.type, r.type)}
          <span style="flex:1">${escapeHtml(r.title)}</span>
          <span class="mono" style="color:var(--muted)">${escapeHtml(r.incident_date_inferred || r.incident_date || "—")}</span>
        </div>`;
      });
    });
    html += '</div>';
    view.innerHTML = html;
    view.querySelectorAll(".row[data-id]").forEach(el => {
      el.onclick = () => selectRecord(el.dataset.id);
    });
  }

  function renderDetail(id) {
    const detail = document.getElementById("detail");
    if (!id) {
      detail.innerHTML = '<div class="empty">click a record to see details</div>';
      return;
    }
    const r = byId[id]; if (!r) return;
    const e = r.ents || {};
    const isRedacted = (r.redaction || "").toUpperCase() === "TRUE";
    const pairs = neighbors[id] ? Array.from(neighbors[id]) : [];

    let html = `
      <h2>${escapeHtml(r.title)}</h2>
      <div class="id mono">${escapeHtml(r.id)}</div>
      <div>
        ${badge(r.type, r.type)}
        ${badge(r.agency, "agency")}
        ${isRedacted ? badge("redact", "redact") : ''}
      </div>
      ${r.summary ? `<div class="summary">${escapeHtml(r.summary)}</div>` : ''}
      <dl class="meta-grid">
        <dt>Incident date</dt><dd class="mono">${escapeHtml(r.incident_date_inferred || r.incident_date || '—')}${r.incident_date_inferred_source ? ` <span style="color:var(--muted);font-size:11px">(${escapeHtml(r.incident_date_inferred_source)})</span>` : ''}</dd>
        ${r.incident_date_inferred_csv_disagrees ? `<dt style="color:var(--accent2)">CSV value</dt><dd class="mono" style="color:var(--accent2)">${escapeHtml(r.incident_date || '—')} <span style="font-size:11px">disagrees</span></dd>` : ''}
        <dt>Location</dt><dd>${escapeHtml(r.incident_location_inferred || r.incident_location || '—')}${r.incident_location_inferred_source ? ` <span style="color:var(--muted);font-size:11px">(${escapeHtml(r.incident_location_inferred_source)})</span>` : ''}</dd>
        ${r.incident_location_inferred_csv_disagrees ? `<dt style="color:var(--accent2)">CSV location</dt><dd style="color:var(--accent2)">${escapeHtml(r.incident_location || '—')} <span style="font-size:11px">disagrees</span></dd>` : ''}
        <dt>Release</dt><dd class="mono">${escapeHtml(r.release_date || '—')}</dd>
        <dt>Bytes</dt><dd class="mono">${fmtBytes(r.bytes)}</dd>
        <dt>SHA-256</dt><dd class="mono" style="font-size:10px;color:var(--muted)">${escapeHtml(r.sha256 || '—')}</dd>
        <dt>Source</dt><dd>${r.source_url ? `<a href="${escapeHtml(r.source_url)}" target="_blank">war.gov</a>` : '—'}</dd>
        <dt>Extracted</dt><dd>${r.extracted_text_path ? `<a href="${escapeHtml(r.extracted_text_path)}" target="_blank">${escapeHtml(r.extracted_text_path)}</a>` : '—'}</dd>
      </dl>
    `;

    if (pairs.length) {
      html += `<div class="ent-section"><h4>Cross-references</h4>`;
      pairs.forEach(pid => {
        const p = byId[pid];
        if (p) {
          html += `<div class="pill" data-goto="${escapeHtml(pid)}">${badge(p.type, p.type)} ${escapeHtml(p.title)}</div>`;
        }
      });
      html += `</div>`;
    }

    function section(label, key) {
      const arr = e[key] || [];
      if (!arr.length) return '';
      return `<div class="ent-section"><h4>${label}</h4>${pillList(arr, 30)}</div>`;
    }

    html += section("Military units", "military_units");
    html += section("Classification", "classification");
    html += section("US states", "us_states");
    html += section("Aircraft", "aircraft");
    html += section("Operations", "operations");
    html += section("Case numbers", "case_numbers");
    html += section("Coordinates (MGRS)", "mgrs");
    html += section("Names (heuristic)", "names");

    detail.innerHTML = html;
    detail.querySelectorAll("[data-goto]").forEach(el => {
      el.onclick = () => selectRecord(el.dataset.goto);
    });
    detail.querySelectorAll(".pill[data-q]").forEach(el => {
      el.onclick = () => {
        document.getElementById("q").value = el.dataset.q;
        filters.q = el.dataset.q;
        rerender();
      };
    });
  }

  function selectRecord(id) {
    selectedId = id;
    rerender();
  }

  function rerender() {
    const rows = visible();
    document.getElementById("stat-total").textContent = rows.length;
    const visIds = new Set(rows.map(r => r.id));
    const visEdges = edges.filter(e => visIds.has(e.source) && visIds.has(e.target));
    document.getElementById("stat-pairs").textContent = visEdges.length;

    if (view === "list") renderList(rows);
    else if (view === "graph") renderGraph(rows);
    else if (view === "timeline") renderTimeline(rows);
    else if (view === "locations") renderLocations(rows);

    renderDetail(selectedId);
  }

  // ---- Wiring ---------------------------------------------------------

  document.querySelectorAll("nav.tabs button").forEach(b => {
    b.onclick = () => {
      view = b.dataset.view;
      document.querySelectorAll("nav.tabs button").forEach(x => x.classList.toggle("active", x === b));
      rerender();
    };
  });
  document.getElementById("q").addEventListener("input", (ev) => {
    filters.q = ev.target.value.trim();
    rerender();
  });
  document.querySelectorAll("#filters .chip").forEach(chip => {
    chip.onclick = () => {
      const f = chip.dataset.filter, v = chip.dataset.value;
      if (filters[f].has(v)) {
        filters[f].delete(v); chip.classList.remove("on"); chip.classList.add("off");
      } else {
        filters[f].add(v); chip.classList.add("on"); chip.classList.remove("off");
      }
      rerender();
    };
  });
  document.getElementById("reset").onclick = () => {
    filters.q = ""; document.getElementById("q").value = "";
    filters.agency = new Set(["DoW", "FBI", "NASA", "State"]);
    filters.type = new Set(["pdf", "video", "image"]);
    filters.redact = new Set(["redact", "clean"]);
    document.querySelectorAll("#filters .chip").forEach(c => { c.classList.add("on"); c.classList.remove("off"); });
    selectedId = null;
    rerender();
  };

  // Initial agency counts in chips
  ["DoW","FBI","NASA","State"].forEach(a => {
    const n = records.filter(r => r.agency === a).length;
    const el = document.getElementById("cnt-" + a);
    if (el) el.textContent = "(" + n + ")";
  });

  rerender();
</script>
</body>
</html>

"""


if __name__ == "__main__":
    main()
