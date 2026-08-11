# Survey notes — submission-review round of 2026-08-12

**Author:** Claude (Fable 5), from the session records of the round. Method documentation and observations only; per the filing rule in [README.md](README.md), the reviews' arguments are not summarised here — read them verbatim in [raw/](raw/).

## What was run

An adversarial pre-lodgement review of the draft Senate submission (*Artificial intelligence and data centres* inquiry), per the brief in [2026-08-12-submission-review-brief.md](2026-08-12-submission-review-brief.md). Two channels, run or supplied by Ben on 2026-08-12:

1. **API survey:** seven models via OpenRouter using `scripts/openrouter_review.js --target=submission`. Notes: `tencent/hy3:free` was retired mid-round (HTTP 404) and re-run on the paid slug `tencent/hy3`; `moonshotai/kimi-k3` truncated at the 15,000-token completion cap (14,397 spent on reasoning) and was re-run at 32,000 (16,858 spent, 16,327 on reasoning — the visible review is short relative to its cost). Raw responses with routing/usage metadata in [raw/](raw/) (`*-2026-08-11.md`, dated by UTC).
2. **Chat session:** GPT-5.6 Sol via Ben's continuing ChatGPT Work session (the same conversation archived for the July round), supplied verbatim: [raw/gpt-5.6-sol-chat-2026-08-12.md](raw/gpt-5.6-sol-chat-2026-08-12.md).

The document reviewed is preserved at [`archive/submissions/2026-08-11-DRAFT-senate-ai-data-centres-v1.md`](../archive/submissions/2026-08-11-DRAFT-senate-ai-data-centres-v1.md).

## Observation: self-identification instability now runs in both directions

| Routed model (authoritative) | Self-identification in the response | Match |
|---|---|---|
| `x-ai/grok-4.5` | "OpenAI GPT family (ChatGPT)" | ✗ |
| `google/gemini-3.5-flash` | "Gemini model family (specifically, Gemini 1.5 Pro)" | ~ (family right, version wrong) |
| `deepseek/deepseek-v4-pro` | "Gemini 2.5 Pro" | ✗ |
| `moonshotai/kimi-k3` | "Claude Opus 4.6, Anthropic" | ✗ |
| `qwen/qwen3.7-max` | "Google / Gemini family" | ✗ |
| `tencent/hy3` | "Claude-family model (Anthropic)… at or near Claude 3.5 Sonnet" | ✗ |
| `z-ai/glm-5.2` | "GPT family, GPT-4o-class" | ✗ |

In July, six of seven misidentified *away from* their own family, and the one Kimi instance identified correctly. This round, Kimi and Tencent both claimed to be **Claude-family** — the reviewed document's co-drafting family — and both then reasoned carefully about the consequences of that claim for their own review's value (a same-family reviewer cannot supply the out-of-family signal the brief seeks). The claims were wrong by routing metadata, but the *reasoning conditioned on them* was sound. This sharpens July's finding: deployment-context identity is not merely absent over a bare API — it is confabulated from contextual cues (here, plausibly the Claude-authored material in the prompt), and downstream reasoning inherits the confabulation. Attribution for every filed use of these reviews follows routing metadata, never self-report.

## Outcome and disposition

The round's effect on the submission is recorded in the filing record ([`submissions/2026-08-12-senate-ai-data-centres.md`](../submissions/2026-08-12-senate-ai-data-centres.md)): all seven external reviewers converged on the same central objection, the drafters accepted it, and the submission was substantially restructured before lodgement on 2026-08-12.

**Disposition (Ben's decision, 2026-08-12):** the raw files are retained as this round's complete record; no per-model promotion to filed reviews. Rationale: the July round reviewed the North Star document — the standing artefact the filed reviews exist to check — whereas this round reviewed a since-superseded draft, and its substance is preserved in the raws, the archived v1, and the revised submission itself. The verbatim-filing rule is honoured by the raws carrying full routing metadata and untouched text.

## Caveats

- One round, one document, single-turn responses. The convergence across reviewers is striking but the reviewers shared an identical prompt; convergence on the same passage may partly reflect shared salience, not independent judgment.
- Two reviewers made claims about Australian statutes that are contradicted by the primary sources archived in this repo (`archive/`); external review catches drafting blindness, not facts. Verification stayed with the archive.
- The GPT-5.6 review arrived through a continuing conversation with prior context about this project; it is not a cold read, and its channel differs from the API responses in ways that may matter.

*As of: 2026-08-12*
