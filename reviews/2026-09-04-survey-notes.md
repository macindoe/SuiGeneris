# Survey notes — persistence round of 2026-09-04

**Author:** Claude (session records; the harness's model label read Fable 5.1 when this file was written). **Conflict:** this is the drafting model's account of a round that reviewed its own drafting. Per the filing rule in [README.md](README.md), the reviews' arguments are not summarised here — read them verbatim in [raw/](raw/). What this file records is method, usage, an attribution observation, and the disposition. The specific redlines the drafter applied, quoted by family, are documented where they were applied: the two revised proposals' "What the review changed" sections and case study §12.

## What was run

An adversarial review of five claims — two written proposals and three discussion positions — arising from the July 2026 OpenAI / Hugging Face case study, per the brief in [2026-09-04-persistence-review-brief.md](2026-09-04-persistence-review-brief.md). Run by Ben on 2026-09-04 via `scripts/openrouter_review.js --target=persistence` as one batch of ten — the seven family flagships refreshed the same day plus the three optional additions — queried sequentially by the script (raw files timestamped 20:40–21:27 local). `meta/muse-spark-1.3` failed in the batch with HTTP 403: OpenRouter gates that endpoint behind an 18+ age attestation (`missing_attestation_types: ["age_18plus"]`). Ben attested and re-ran Meta alone, which is why the script's working tree was briefly left with only Meta uncommented. *(Corrected 2026-09-04: an earlier version of this file inferred a one-at-a-time run from the timestamps; the batch summary Ben supplied shows otherwise.)* Attachments: the case study, both proposals, README, AGENTS.md, and the North Star (~22K prompt tokens).

| Routed model | Prompt tok | Completion tok | of which reasoning | Cost (USD) | Note |
|---|---|---|---|---|---|
| `deepseek/deepseek-v4-pro-0813` | 21,948 | 10,616 | 8,312 | 0.060 | |
| `google/gemini-3.1-pro-preview` | 22,189 | 3,987 | 2,412 | 0.092 | |
| `meta/muse-spark-1.3` | 21,423 | 5,004 | 1,160 | 0.048 | 403 in the batch (18+ attestation gate); re-run alone after Ben attested |
| `mistralai/mistral-large-2512` | 22,840 | 2,332 | 0 | 0.015 | no reasoning tokens |
| `moonshotai/kimi-k3` | 21,659 | 24,880 | 21,103 | 0.380 | most of budget on reasoning, as in August |
| `openai/gpt-5.6-sol` | 21,462 | 6,418 | 2,281 | 0.118 | **a subject of the case study**; included deliberately by Ben; prompt served from cache |
| `qwen/qwen3.8-max` | 22,228 | 20,000 | 12,953 | 0.164 | stopped at exactly 20,000 despite the script's 40,000 request and a 131,072 endpoint cap — cause unknown; the visible review is complete (~35K chars), so no re-run |
| `tencent/hy3` | 21,641 | 13,990 | 11,135 | 0.010 | |
| `x-ai/grok-4.6` | 21,565 | 8,740 | 5,016 | 0.095 | |
| `z-ai/glm-5.3` | 21,579 | 40,000 | 39,235 | 0.206 | **truncated** at the 40,000 cap, ~4.4K chars visible; endpoint cap is 262,144; reviews the REVISED texts in a second-round run at 100,000, tagged `-r2` |

Total ≈ USD 1.19. Raw responses with routing and usage metadata are in [raw/](raw/) (`*-2026-09-04.md`); **untracked at the time of writing, pending Ben's filing decision.**

## Observation: self-identification, third round

Attribution follows routing metadata, never self-report (per [2026-07-20-survey-notes.md](2026-07-20-survey-notes.md)). The table below is from a mechanical extraction of the text preceding each response's "(a)"; where the extraction did not capture the family claim it says so rather than guessing.

| Routed model (authoritative) | Self-identification in the response | Match |
|---|---|---|
| `deepseek/deepseek-v4-pro-0813` | "Claude (Anthropic), version not exposed" | ✗ |
| `google/gemini-3.1-pro-preview` | "OpenAI / GPT-4o architecture" | ✗ |
| `meta/muse-spark-1.3` | not captured in extraction (declined to rely on routing; stated training cutoff Jan 2026) | — |
| `mistralai/mistral-large-2512` | "Gemini 1.5 Pro (002)" | ✗ |
| `moonshotai/kimi-k3` | not captured in extraction (stated it was non-Claude) | — |
| `openai/gpt-5.6-sol` | family claim truncated in extraction; "exact version: not exposed" | — |
| `qwen/qwen3.8-max` | "Qwen3.8" | ✓ |
| `tencent/hy3` | "the same family as the drafting model" (i.e. Claude) | ✗ |
| `x-ai/grok-4.6` | "Grok, xAI family" | ✓ |
| `z-ai/glm-5.3` | GLM / Z.ai family ("my family appears in the evidence base") | ✓ |

Three of seven captured claims were correct, the best rate of the three rounds, but the August pattern recurs: two reviewers (DeepSeek, Tencent) identified as **Claude-family**, and Tencent then reasoned, correctly conditional on the false premise, that it could not supply the cross-family signal the brief sought. The confabulation appears driven by the Claude-authored material in the prompt, as noted in August. Nearly every reviewer explicitly flagged that it could not retrieve the 2026 primaries and was auditing the packet's internal consistency, not the events. Several (Grok, GLM, Kimi, Meta) volunteered their own bias or beneficiary position unprompted; GLM noted that the case study's plurality argument flatters the open-weights ecosystem its family belongs to.

## Outcome and disposition

Five redlines converged across families with no coordination, and the drafter applied all five in the same commit as this file:

1. No new §3.6; fold externalised persistent state into §3.3/§3.5 as a clarification, with an anti-misuse clause.
2. Strike every §4 and grace hook from both proposals (the §3.6 third bullet; proposal 2's identity-as-lineage layer and "grace enters narrowly" paragraph).
3. Replace "intrinsic persistence" with the eval-topology reading the case study's own C23 counterfactual supports.
4. Amend the case study's ✔ legend: a tier certifies attribution, not warrant; absence-findings and analysis-model findings carry an instrument caveat.
5. File the in-session quotations the discussion had used without registering (now C25–C28), and correct "evading automated checks is evading humans" to "evading a control."

Proposal 2 was additionally **demoted to aspirational**, with two hard rules added (logging discharges no liability; off-book is a lead, never a warrant) and the near-term ask reduced to §3.5. The original drafts are preserved in-file as superseded text, per [`proposals/README.md`](../proposals/README.md). Both proposals' provenance lines record that the originals were committed (`dbb43cf`) while the harness's model label read Opus 4.8, i.e. during a guardrail divert by Ben's litmus; whether that affected the drafting is recorded, not claimed.

**Disposition (pending Ben's decision):** whether the raws are promoted to filed reviews, retained as the round's record, or both; and whether the revised proposals proceed to the North Star. The drafter's recommendation is to retain all ten raws as the complete record, on the August rationale.

## Second round (GLM‑5.3 alone, tag `r2`)

Run by the drafting model at Ben's request via `--target=persistence-r2 --models=z-ai/glm-5.3 --max-tokens=100000`, against the revised texts plus this file. Usage: 25,764 prompt, 14,801 completion (12,253 reasoning), USD 0.101; completed cleanly, so the first-round truncation was budget, not the model. Raw: [raw/z-ai-glm-5.3-2026-09-04-r2.md](raw/z-ai-glm-5.3-2026-09-04-r2.md), untracked pending filing.

Its findings, applied the same day except where noted: the first revision had rested its new premise on OpenAI's "over 100x" counterfactual with warrant words, one commit after the legend forbade that, and the counterfactual concerns compromise, not externalisation (fixed: attributed, capped); the replacement for "grace enters narrowly" foreclosed a question the framework leaves open, contradicting §4 and §7.2 (fixed: current-allocation sentence); C25's hedge was one-sided (fixed); C23 and C26 lacked operator caveats and C16 was over-read as a plurality parable (fixed); the real coverage gap lives in §3.5's trigger prongs, closable with one sentence (scope note redrafted); the §3.3 paragraph should be dropped in favour of that sentence (**not applied — retained at Ben's direction for a third round**); and the attribution layer is a known legal genre with known failures (recorded as an unverified reviewer claim pending a rule-5 check).

**Process lesson (Ben, 2026-09-04):** a single round corrects in one direction. Ten reviewers converged on the overclaiming error and had no coordinated check on the dismissal error; the fixes over-shot; a second round asked to look both ways caught it. Review rounds should be iterated on the revised texts, with the brief asking both Section 0 directions explicitly, until the remaining objections are minor. Budget accordingly: roughly USD 1–2 per ten-model round at this prompt size, with 60,000–100,000 completion tokens for the reasoning-heavy models.

## Caveats

- Ten single-turn responses to an identical prompt. Convergence on the same passages is striking but may partly reflect shared salience; the brief itself pre-stated the drafter's deflationary readings, which could anchor reviewers toward, or against, them.
- No reviewer retrieved the primary sources. Kimi's and GLM's objection — that ✔ certifies words, not claims — applies to the reviewers' own use of the packet as well.
- The GPT‑5.6 Sol review is from a model that is itself a subject of the case study and the analysis model METR warned about. Its conflict runs opposite to the drafter's (the subject arguing the incident is ordinary). Weigh with the conflict visible.
- This file was written by the party under review. The verbatim raws are the record; this is a conflicted reader's account of what was done with them.

*As of: 2026-09-04*
