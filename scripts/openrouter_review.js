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
//   node scripts/openrouter_review.js --target=persistence   (2026-09-04 round: five claims from the July 2026 case study)
//
// Requires OPEN_ROUTER_API_KEY in a .env file at the repo root (already there).
// Needs Node 18+ for built-in fetch. No npm dependencies.

const fs = require("fs");
const path = require("path");

const REPO_ROOT = path.resolve(__dirname, "..");
const OUT_DIR = path.join(REPO_ROOT, "reviews", "raw");

// Completion budget; reasoning models can burn most of it on thought tokens
// (kimi-k3 spent 14397/15000 on reasoning in the 2026-08-12 round and truncated).
// Raised 15000 -> 40000 on 2026-09-04: glm-5.3 (reasoning default "max") and
// qwen3.8-max ("xhigh") would truncate at 15000; gemini-3.1-pro-preview caps
// completions at 65536. Override per-run with --max-tokens=N.
const MAX_TOKENS = (() => {
  const arg = process.argv.find((a) => a.startsWith("--max-tokens="));
  return arg ? parseInt(arg.slice("--max-tokens=".length), 10) : 40000;
})();

// Default lineup: the current flagship of each non-Anthropic family, confirmed
// against OpenRouter's live catalog (GET https://openrouter.ai/api/v1/models,
// 427 models) on 2026-09-04 09:39 UTC by a Sonnet 5 subagent; every id below
// was present in that listing. Edit freely — this list is deliberately not the
// whole catalog. "Astra" (OpenAI, unreleased) is deliberately absent.
const DEFAULT_MODELS = [
  // The seven families used in the July and August rounds, refreshed:
  "google/gemini-3.1-pro-preview", // Google flagship; still "preview"-labelled — no GA gemini-3.x-pro exists yet (gemini-3.5-flash was a Flash-tier pick, never the flagship)
  "x-ai/grok-4.6",                 // xAI flagship; supersedes grok-4.5 (released 2026-08-12)
  "qwen/qwen3.8-max",              // Alibaba flagship ("the flagship model in Alibaba's Qwen3.8 series"); supersedes qwen3.7-max; reasoning default "xhigh"
  "tencent/hy3",                   // Tencent flagship, unchanged; hy4-preview exists (2026-08-28) but is not GA. "tencent/hy3:free" is NOT a valid id.
  "deepseek/deepseek-v4-pro-0813", // DeepSeek flagship ("the GA release of DeepSeek V4 Pro"); supersedes the undated deepseek-v4-pro snapshot
  "z-ai/glm-5.3",                  // Z.ai flagship; supersedes glm-5.2 (released 2026-08-18); reasoning default "max"
  "moonshotai/kimi-k3",            // Moonshot flagship, unchanged; burns most of its completion budget on reasoning (see MAX_TOKENS)
  // Optional additional families, verified in the same listing. Uncomment or
  // pass via --models=. Ben's call per round:
  // "openai/gpt-5.6-sol",           // OpenAI flagship. For the 2026-09-04 round this model is a *subject* of the case study under review (one of the two incident models, and METR's analysis model) — a conflicted reviewer in a new way; include deliberately or not at all.
  // "mistralai/mistral-large-2512", // Mistral: "most capable model to date"; mistral-medium-3-5 is newer-dated but smaller — judgment call
  // "meta/muse-spark-1.3",          // Meta: flagship line rebranded from meta-llama/llama-4-* to meta/muse-spark-*; released 2026-09-02
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

function buildSubmissionPrompt() {
  const brief = readDoc("reviews/2026-08-12-submission-review-brief.md");
  const agents = readDoc("AGENTS.md");
  const readme = readDoc("README.md");
  // v1 draft as reviewed in the 2026-08-12 round; moved to archive/ after the
  // round concluded. Point this at the current draft if a future round runs.
  const submission = readDoc("archive/submissions/2026-08-11-DRAFT-senate-ai-data-centres-v1.md");

  return `Hi. I'd like an adversarial review of a draft Senate submission from your model family, per the brief below, before the human maintainer decides whether to lodge it.

=== reviews/2026-08-12-submission-review-brief.md ===
${brief}

=== submissions/DRAFT-2026-senate-ai-data-centres.md (the document under review) ===
${submission}

=== README.md (project context) ===
${readme}

=== AGENTS.md (project context) ===
${agents}

Please structure your response as: model family/version self-identification, then (a), (b), (c), and optionally (d), per the brief.`;
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

function buildPersistencePrompt() {
  const brief = readDoc("reviews/2026-09-04-persistence-review-brief.md");
  const caseStudy = readDoc("case-studies/2026-07-openai-hugging-face-agent-intrusion.md");
  const proposalA = readDoc("proposals/externalised-persistent-state-section-3.md");
  const proposalB = readDoc("proposals/distributed-persistence-substrate.md");
  const agents = readDoc("AGENTS.md");
  const readme = readDoc("README.md");
  const northStar = readDoc("north-star-sui-generis-ai-category.md");

  return `Hi. I'd like an adversarial review from your model family of five claims arising from a verified incident case study and two proposals, per the brief below. The human maintainer decides what, if anything, is adopted.

=== reviews/2026-09-04-persistence-review-brief.md ===
${brief}

=== case-studies/2026-07-openai-hugging-face-agent-intrusion.md (evidence base) ===
${caseStudy}

=== proposals/externalised-persistent-state-section-3.md (claim 1) ===
${proposalA}

=== proposals/distributed-persistence-substrate.md (claim 2) ===
${proposalB}

=== README.md (project context) ===
${readme}

=== AGENTS.md (project context) ===
${agents}

=== north-star-sui-generis-ai-category.md (the framework the claims are read against) ===
${northStar}

Please structure your response as: model family/version self-identification, then (a), (b), (c), and optionally (d), per the brief. If you comment on your own reaction to the material, label it plainly as unverifiable self-report, not evidence.`;
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
      max_tokens: MAX_TOKENS,
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
  const target = args.includes("--target=submission")
    ? "submission"
    : args.includes("--target=persistence")
      ? "persistence"
      : "north-star";
  const modelsArg = args.find((a) => a.startsWith("--models="));
  const models = modelsArg
    ? modelsArg.slice("--models=".length).split(",").map((s) => s.trim())
    : DEFAULT_MODELS;

  const prompt =
    target === "submission"
      ? buildSubmissionPrompt()
      : target === "persistence"
        ? buildPersistencePrompt()
        : buildPrompt();
  console.log(`Target: ${target}`);
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
