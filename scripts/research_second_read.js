#!/usr/bin/env node
// Second reader for one research-library source (research/README.md, intake
// step 4). Sends the brief, the schema excerpt, the source file, its claim
// files and the HELD TEXT of the paper to ONE model of a different family
// via OpenRouter, and writes the raw response to reviews/raw/ as
// <model>-<date>-sr-<slug>.md. Staging only: never edits research/ or git.
//
// Usage:
//   node scripts/research_second_read.js --source=<slug> --model=<openrouter id> [--max-tokens=N] [--dry-run]
//
// The second-reader pool (research/README.md): GPT, DeepSeek, Grok, Gemini;
// Claude only when the extractor was not Claude. Rotate across sources.
// Requires OPEN_ROUTER_API_KEY in .env at the repo root. Node 18+.

const fs = require("fs");
const path = require("path");

const REPO_ROOT = path.resolve(__dirname, "..");
const RES = path.join(REPO_ROOT, "research");
const OUT_DIR = path.join(REPO_ROOT, "reviews", "raw");

const args = process.argv.slice(2);
const arg = (name) => {
  const a = args.find((x) => x.startsWith(`--${name}=`));
  return a ? a.slice(name.length + 3) : null;
};
const SOURCE = arg("source");
const MODEL = arg("model");
const MAX_TOKENS = parseInt(arg("max-tokens") || "60000", 10);
const DRY = args.includes("--dry-run");
const FOCUS = arg("focus"); // e.g. --focus=item5 : not_evidence_of only, plus disclosed pulls

if (!SOURCE || !MODEL) {
  console.error("usage: --source=<slug> --model=<openrouter id> [--max-tokens=N] [--dry-run]");
  process.exit(2);
}

function read(p) {
  return fs.readFileSync(p, "utf8");
}

function loadEnvKey() {
  const raw = read(path.join(REPO_ROOT, ".env"));
  const m = raw.match(/^OPEN_ROUTER_API_KEY=(.+)$/m);
  if (!m) throw new Error("OPEN_ROUTER_API_KEY not found in .env");
  return m[1].trim().replace(/^["']|["']$/g, "");
}

function schemaExcerpt() {
  // The claim-schema table and the standing hazards from research/README.md.
  const readme = read(path.join(RES, "README.md"));
  const start = readme.indexOf("**Claim** (");
  const end = readme.indexOf("## Intake procedure");
  const hazards = readme.slice(readme.indexOf("## Standing hazards"));
  return readme.slice(start, end) + "\n" + hazards;
}

function buildPrompt() {
  const brief = read(path.join(RES, "SECOND-READ-BRIEF.md"));
  const srcPath = path.join(RES, "sources", `${SOURCE}.md`);
  if (!fs.existsSync(srcPath)) throw new Error(`no source file ${srcPath}`);
  const source = read(srcPath);
  const claimFiles = fs
    .readdirSync(path.join(RES, "claims"))
    .filter((f) => f.startsWith(`${SOURCE}-c`) && f.endsWith(".md"))
    .sort();
  if (!claimFiles.length) throw new Error(`no claim files for ${SOURCE}`);
  // Blind read: a second reader must not see earlier readers' verdicts or the
  // coordinating session's correction notes, so the review field and any
  // CORRECTION lines are redacted from the claim files in the prompt.
  const redact = (text) =>
    text
      .replace(/^review: .*$/m, "review: (redacted for blind read)")
      .split("\n")
      .filter((line) => !line.startsWith("CORRECTION"))
      .join("\n");
  const claims = claimFiles
    .map((f) => `=== research/claims/${f} ===\n${redact(read(path.join(RES, "claims", f)))}`)
    .join("\n\n");
  const textPath = path.join(RES, "texts", SOURCE, "text.txt");
  if (!fs.existsSync(textPath)) throw new Error(`held text missing: ${textPath} (re-fetch per the source file's sha256)`);
  const held = read(textPath);

  return `Hi. Please act as the second reader for one paper intake, per the brief below. The extractor was a Claude-lineage model; you were chosen because you are not.

=== research/SECOND-READ-BRIEF.md ===
${brief}

=== research/README.md (schema excerpt) ===
${schemaExcerpt()}

=== research/sources/${SOURCE}.md (the source file under review) ===
${source}

${claims}

=== HELD TEXT: research/texts/${SOURCE}/text.txt (the paper, tag-stripped; the only authority) ===
${held}

=== END OF HELD TEXT ===

${FOCUS === "item5" ? `FOCUS FOR THIS READ: answer item 5 (not_evidence_of) only, for each of the ${claimFiles.length} claims, applying the brief's distinction between paper-scope and framework-rule exclusions; for each exclusion in each field say which kind it is, whether it is warranted, and whether its wording goes beyond the framework's rule. Then answer item 9 (the extractor's disclosed pulls) as it bears on those fields. Skip items 1 to 4, 6, 7 and 8. End with the Summary.` : `Please respond in the output format the brief specifies, for the ${claimFiles.length} claim files above, then the source-level checks, then the summary.`}`;
}

function slugify(id) {
  return id.replace(/[\/:]/g, "-");
}

async function callModel(apiKey, modelId, prompt) {
  const res = await fetch("https://openrouter.ai/api/v1/chat/completions", {
    method: "POST",
    headers: {
      Authorization: `Bearer ${apiKey}`,
      "Content-Type": "application/json",
      "HTTP-Referer": "https://github.com/",
      "X-Title": "SuiGeneris research second read",
    },
    body: JSON.stringify({
      model: modelId,
      messages: [{ role: "user", content: prompt }],
      max_tokens: MAX_TOKENS,
    }),
  });
  const body = await res.json();
  if (!res.ok) throw new Error(`HTTP ${res.status} for ${modelId}: ${JSON.stringify(body).slice(0, 500)}`);
  return body;
}

async function main() {
  const prompt = buildPrompt();
  console.log(`Source: ${SOURCE}\nModel: ${MODEL}\nPrompt: ${prompt.length} chars (~${Math.round(prompt.length / 4)} tokens est.), max_tokens ${MAX_TOKENS}`);
  if (DRY) {
    const dump = arg("dump");
    if (dump) fs.writeFileSync(dump, prompt);
    console.log(`--dry-run: not calling the API.${dump ? ` Prompt written to ${dump}` : ""}`);
    return;
  }
  const apiKey = loadEnvKey();
  fs.mkdirSync(OUT_DIR, { recursive: true });
  const today = new Date().toISOString().slice(0, 10);
  const outPath = path.join(OUT_DIR, `${slugify(MODEL)}-${today}-sr${FOCUS ? `-${FOCUS}` : ""}-${SOURCE}.md`);
  process.stdout.write(`Querying ${MODEL} ... `);
  const body = await callModel(apiKey, MODEL, prompt);
  const text = body.choices?.[0]?.message?.content ?? "(no content in response)";
  const usage = body.usage ?? {};
  const header = [
    `# Raw OpenRouter response — second read, NOT a filed review`,
    ``,
    `**Model id (OpenRouter):** \`${MODEL}\``,
    `**Source under review:** \`research/sources/${SOURCE}.md\` and its claims`,
    `**Queried:** ${today} via scripts/research_second_read.js --source=${SOURCE} --model=${MODEL} (max_tokens ${MAX_TOKENS})`,
    `**Usage:** ${JSON.stringify(usage)}`,
    ``,
    `The coordinating session reads this and records the reader's family and date on each claim's review.second_reader;`,
    `disagreements on bucket or evidence type go to the docket (research/README.md, triggers 4 and 5). Verbatim; do not edit.`,
    ``,
    `---`,
    ``,
  ].join("\n");
  fs.writeFileSync(outPath, header + text + "\n");
  console.log(`done -> ${path.relative(REPO_ROOT, outPath)}`);
  console.log(`Usage: ${JSON.stringify(usage)}`);
}

main().catch((err) => {
  console.error("Fatal:", err.message);
  process.exit(1);
});
