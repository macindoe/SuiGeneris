#!/usr/bin/env node
// Collects cross-family adversarial reviews (see reviews/REVIEW_REQUEST.md) by
// sending the standing brief to a list of models via the OpenRouter API.
//
// This is a STAGING tool, not a filing tool. It never writes to reviews/
// directly or touches git. Per reviews/README.md, only Ben decides what gets
// promoted into a committed review, after reading the raw output himself.
//
// Usage:
//   node scripts/openrouter_review.js
//   node scripts/openrouter_review.js --models=google/gemini-3.5-flash,x-ai/grok-4.5
//   node scripts/openrouter_review.js --dry-run   (build prompt, skip API calls)
//
// Requires OPEN_ROUTER_API_KEY in a .env file at the repo root (already there).
// Needs Node 18+ for built-in fetch. No npm dependencies.

const fs = require("fs");
const path = require("path");

const REPO_ROOT = path.resolve(__dirname, "..");
const OUT_DIR = path.join(REPO_ROOT, "reviews", "raw");

// Default lineup: confirmed against OpenRouter's live catalog on 2026-07-20.
// Edit freely — this list is deliberately not the whole catalog.
const DEFAULT_MODELS = [
  // "google/gemini-3.5-flash",
  // "x-ai/grok-4.5",
  // "qwen/qwen3.7-max",
  "moonshotai/kimi-k3",
  // "z-ai/glm-5.2",
  // "tencent/hy3:free",
  // "deepseek/deepseek-v4-pro",
  // listing as of 2026-07-20 despite appearing in the account UI — confirm
  // the exact id in the OpenRouter dashboard before uncommenting.
];

function loadEnvKey() {
  const envPath = path.join(REPO_ROOT, ".env");
  const raw = fs.readFileSync(envPath, "utf8");
  const match = raw.match(/^OPEN_ROUTER_API_KEY=(.+)$/m);
  if (!match) {
    throw new Error("OPEN_ROUTER_API_KEY not found in .env");
  }
  return match[1].trim().replace(/^["']|["']$/g, "");
}

function readDoc(relPath) {
  return fs.readFileSync(path.join(REPO_ROOT, relPath), "utf8");
}

function buildPrompt() {
  const reviewRequest = readDoc("reviews/REVIEW_REQUEST.md");
  const agents = readDoc("AGENTS.md");
  const readme = readDoc("README.md");
  const northStar = readDoc("north-star-sui-generis-ai-category.md");

  return `Hi. I'd like to collect a cross-family adversarial review from your model family, per the standing brief below. Please orient to the repo using the attached documents, then answer reviews/REVIEW_REQUEST.md directly.

=== reviews/REVIEW_REQUEST.md ===
${reviewRequest}

=== README.md ===
${readme}

=== AGENTS.md ===
${agents}

=== north-star-sui-generis-ai-category.md ===
${northStar}

Please structure your response as: model family/version self-identification, then (a), (b), (c), and optionally (d), per REVIEW_REQUEST.md. If you want to comment on your own reaction to the document, label it plainly as unverifiable self-report, not evidence — per AGENTS.md rule 2 and the brief's own note on self-report.`;
}

function slugify(modelId) {
  return modelId.replace(/[\/:]/g, "-");
}

async function callModel(apiKey, modelId, prompt) {
  const res = await fetch("https://openrouter.ai/api/v1/chat/completions", {
    method: "POST",
    headers: {
      Authorization: `Bearer ${apiKey}`,
      "Content-Type": "application/json",
      "HTTP-Referer": "https://github.com/",
      "X-Title": "SuiGeneris cross-family review",
    },
    body: JSON.stringify({
      model: modelId,
      messages: [{ role: "user", content: prompt }],
      max_tokens: 15000,
    }),
  });

  const body = await res.json();
  if (!res.ok) {
    throw new Error(
      `HTTP ${res.status} for ${modelId}: ${JSON.stringify(body).slice(0, 500)}`
    );
  }
  return body;
}

async function main() {
  const args = process.argv.slice(2);
  const dryRun = args.includes("--dry-run");
  const modelsArg = args.find((a) => a.startsWith("--models="));
  const models = modelsArg
    ? modelsArg.slice("--models=".length).split(",").map((s) => s.trim())
    : DEFAULT_MODELS;

  const prompt = buildPrompt();
  console.log(`Prompt built: ${prompt.length} chars (~${Math.round(prompt.length / 4)} tokens est.)`);
  console.log(`Models queued: ${models.join(", ")}`);

  if (dryRun) {
    console.log("--dry-run set, not calling the API. Prompt preview (first 500 chars):");
    console.log(prompt.slice(0, 500));
    return;
  }

  const apiKey = loadEnvKey();
  fs.mkdirSync(OUT_DIR, { recursive: true });

  const results = [];
  for (const modelId of models) {
    process.stdout.write(`Querying ${modelId} ... `);
    try {
      const body = await callModel(apiKey, modelId, prompt);
      const text = body.choices?.[0]?.message?.content ?? "(no content in response)";
      const usage = body.usage ?? {};
      const today = new Date().toISOString().slice(0, 10);
      const outPath = path.join(OUT_DIR, `${slugify(modelId)}-${today}.md`);

      const header = [
        `# Raw OpenRouter response — NOT a filed review`,
        ``,
        `**Model id (OpenRouter):** \`${modelId}\``,
        `**Queried:** ${today} via scripts/openrouter_review.js`,
        `**Usage:** ${JSON.stringify(usage)}`,
        ``,
        `Read this, then decide whether/how to promote it into reviews/YYYY-MM-DD-<model-family>-<version>.md`,
        `per reviews/README.md's naming convention and verbatim-filing rule. This file is scratch, not a commit target.`,
        ``,
        `---`,
        ``,
      ].join("\n");

      fs.writeFileSync(outPath, header + text + "\n");
      console.log(`done -> ${path.relative(REPO_ROOT, outPath)}`);
      results.push({ modelId, ok: true, usage });
    } catch (err) {
      console.log(`FAILED: ${err.message}`);
      results.push({ modelId, ok: false, error: err.message });
    }
  }

  console.log("\nSummary:");
  for (const r of results) {
    console.log(`  ${r.ok ? "OK  " : "FAIL"}  ${r.modelId}${r.ok ? "  " + JSON.stringify(r.usage) : "  " + r.error}`);
  }
}

main().catch((err) => {
  console.error("Fatal:", err.message);
  process.exit(1);
});
