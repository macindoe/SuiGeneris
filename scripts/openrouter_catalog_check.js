#!/usr/bin/env node
// Lists, for each family seated in DEFAULT_MODELS (scripts/openrouter_review.js),
// the current seat and every model of that family in OpenRouter's live catalog
// newer than the seat, so the maintainer can see whether a seat has been
// superseded. Read-only; prints a dated report. No key needed for GET /models.
//
// Usage: node scripts/openrouter_catalog_check.js [--all]   (--all lists every model per family)

const fs = require("fs");
const path = require("path");

const src = fs.readFileSync(path.join(__dirname, "openrouter_review.js"), "utf8");
const block = src.slice(src.indexOf("const DEFAULT_MODELS = ["), src.indexOf("];", src.indexOf("const DEFAULT_MODELS = [")));
const seats = [...block.matchAll(/^\s*"([^"]+)",/gm)].map((m) => m[1]);
const ALL = process.argv.includes("--all");

async function main() {
  const res = await fetch("https://openrouter.ai/api/v1/models");
  if (!res.ok) throw new Error(`HTTP ${res.status}`);
  const { data } = await res.json();
  const byId = Object.fromEntries(data.map((m) => [m.id, m]));
  const day = (t) => (t ? new Date(t * 1000).toISOString().slice(0, 10) : "?");
  console.log(`OpenRouter catalog: ${data.length} models, checked ${new Date().toISOString().slice(0, 16)} UTC\n`);
  for (const seat of seats) {
    const fam = seat.split("/")[0];
    const cur = byId[seat];
    const famModels = data.filter((m) => m.id.startsWith(fam + "/")).sort((a, b) => (b.created || 0) - (a.created || 0));
    console.log(`== ${seat}  ${cur ? `(listed; added ${day(cur.created)}; ctx ${cur.context_length}; $${cur.pricing?.prompt}/$${cur.pricing?.completion} per token)` : "(NOT IN CATALOG)"}`);
    const newer = cur ? famModels.filter((m) => (m.created || 0) > (cur.created || 0)) : famModels;
    const show = ALL ? famModels : newer;
    for (const m of show.slice(0, 12)) {
      console.log(`   ${m.id === seat ? "*" : " "} ${day(m.created)}  ${m.id}  ctx ${m.context_length}  $${m.pricing?.prompt}/$${m.pricing?.completion}`);
    }
    if (!show.length) console.log("    (nothing newer in this family)");
  }
}
main().catch((e) => { console.error("Fatal:", e.message); process.exit(1); });
