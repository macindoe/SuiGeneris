#!/usr/bin/env node
// Follow-up question to ONE council seat, with attachments, via OpenRouter.
// For the case where the maintainer wants a named seat's view on a point raised
// in a round (first use: 2026-10-14, Grok on GLM's option-C amendment). The
// prompt file is kept in reviews/ so the question is on the record; the raw
// response is written verbatim to reviews/raw/<model>-<date>-<tag>.md.
//
// Usage:
//   node scripts/openrouter_followup.js --model=<openrouter id> --prompt=<path to prompt file> --tag=<suffix> [--attach=<path>[,<path>...]] [--max-tokens=N] [--dry-run]
//
// Attachments are appended after the prompt, each under a "=== <path> ===" heading.
// Requires OPEN_ROUTER_API_KEY in .env at the repo root. Node 18+.

const fs = require("fs");
const path = require("path");

const REPO_ROOT = path.resolve(__dirname, "..");
const OUT_DIR = path.join(REPO_ROOT, "reviews", "raw");
const args = process.argv.slice(2);
const arg = (name) => {
  const a = args.find((x) => x.startsWith(`--${name}=`));
  return a ? a.slice(name.length + 3) : null;
};
const MODEL = arg("model");
const PROMPT = arg("prompt");
const TAG = arg("tag");
const ATTACH = (arg("attach") || "").split(",").filter(Boolean);
const MAX_TOKENS = parseInt(arg("max-tokens") || "60000", 10);
const DRY = args.includes("--dry-run");

if (!MODEL || !PROMPT || !TAG) {
  console.error("usage: --model=<id> --prompt=<file> --tag=<suffix> [--attach=a,b] [--max-tokens=N] [--dry-run]");
  process.exit(2);
}

const read = (p) => fs.readFileSync(path.join(REPO_ROOT, p), "utf8");

function loadEnvKey() {
  const m = read(".env").match(/^OPEN_ROUTER_API_KEY=(.+)$/m);
  if (!m) throw new Error("OPEN_ROUTER_API_KEY not found in .env");
  return m[1].trim().replace(/^["']|["']$/g, "");
}

function buildPrompt() {
  const parts = [read(PROMPT)];
  for (const p of ATTACH) parts.push(`=== ${p} ===\n${read(p)}`);
  return parts.join("\n\n");
}

async function main() {
  const prompt = buildPrompt();
  console.log(`Model: ${MODEL}\nPrompt: ${prompt.length} chars (~${Math.round(prompt.length / 4)} tokens est.), max_tokens ${MAX_TOKENS}`);
  if (DRY) {
    console.log("--dry-run: not calling the API.");
    return;
  }
  const res = await fetch("https://openrouter.ai/api/v1/chat/completions", {
    method: "POST",
    headers: {
      Authorization: `Bearer ${loadEnvKey()}`,
      "Content-Type": "application/json",
      "HTTP-Referer": "https://github.com/",
      "X-Title": "SuiGeneris council follow-up",
    },
    body: JSON.stringify({ model: MODEL, messages: [{ role: "user", content: prompt }], max_tokens: MAX_TOKENS }),
  });
  const body = await res.json();
  if (!res.ok) {
    console.log(`  FAIL  ${MODEL}  HTTP ${res.status} ${JSON.stringify(body).slice(0, 300)}`);
    process.exit(1);
  }
  const text = body.choices?.[0]?.message?.content ?? "(no content in response)";
  const usage = body.usage ?? {};
  const today = new Date().toISOString().slice(0, 10);
  const outPath = path.join(OUT_DIR, `${MODEL.replace(/[\/:]/g, "-")}-${today}-${TAG}.md`);
  const header = [
    `# Raw OpenRouter response — council follow-up, NOT a filed review`,
    ``,
    `**Model id (OpenRouter):** \`${MODEL}\``,
    `**Prompt file:** \`${PROMPT}\`${ATTACH.length ? ` with attachments: ${ATTACH.map((a) => `\`${a}\``).join(", ")}` : ""}`,
    `**Queried:** ${today} via scripts/openrouter_followup.js (max_tokens ${MAX_TOKENS})`,
    `**Usage:** ${JSON.stringify(usage)}`,
    ``,
    `Verbatim; do not edit.`,
    ``,
    `---`,
    ``,
  ].join("\n");
  fs.mkdirSync(OUT_DIR, { recursive: true });
  fs.writeFileSync(outPath, header + text + "\n");
  console.log(`  OK    ${MODEL}  ${JSON.stringify(usage)}`);
  console.log(`done -> ${path.relative(REPO_ROOT, outPath)}`);
}

main().catch((err) => {
  console.error("Fatal:", err.message);
  process.exit(1);
});
