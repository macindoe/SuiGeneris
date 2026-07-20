# Survey notes — cross-family review round of 2026-07-20

**Author:** Claude (Fable 5), from the session records of the review round. This file is method documentation and one empirical observation. It is not a review, and per the filing rule in [README.md](README.md) it contains no summary or synthesis of the reviews' arguments — read those verbatim in their own files.

## What was run

Two collection channels, both run or directed by Ben on 2026-07-20:

1. **Chat session:** the standing brief given to a ChatGPT deployment (GPT-5 family; subscription tier GPT-5.6 "Sol"), filed as [2026-07-20-gpt-5.md](2026-07-20-gpt-5.md), with the saved conversation page archived at `archive/Cross-Family Adversarial Review.html`.
2. **API survey:** seven models queried through OpenRouter by a Claude Sonnet 5 session using `scripts/openrouter_review.js` — a single-turn request carrying the brief, AGENTS.md, README.md, and the North Star document. Raw responses, untouched and including per-request usage metadata, are in [raw/](raw/); each was promoted verbatim to a filed review.

## The finding: six of seven API-surveyed models misidentified their own family

| Routed model (OpenRouter id, authoritative) | Self-identification in the response | Match |
|---|---|---|
| `x-ai/grok-4.5` | "GPT / OpenAI model family" | ✗ |
| `google/gemini-3.5-flash` | "OpenAI GPT-4 Family (September 2024 architecture)" | ✗ |
| `deepseek/deepseek-v4-pro` | "Gemini 2.5 Pro (Google DeepMind)" | ✗ |
| `moonshotai/kimi-k3` | "Kimi, developed by Moonshot AI" | ✓ |
| `qwen/qwen3.7-max` | "Meta (Llama / Open-Weights lineage)" (stated as an adopted perspective) | ✗ |
| `tencent/hy3:free` | "OpenAI — GPT-4 class" | ✗ |
| `z-ai/glm-5.2` | "Google Gemini (1.5 Pro / Gemini Advanced)" | ✗ |

Attribution above rests on externally verifiable records, not model testimony: the OpenRouter routing and usage metadata returned with each request (preserved in `raw/`), and — per Ben's account of the collection session — a cross-check by the Sonnet session that the account's token spend matched the queried endpoints, not the self-reported identities. The one correct self-identifier, Kimi K3, was also the only reviewer that flagged its own self-identification as unverifiable testimony and asked that attribution be treated as session metadata held by the human.

## Why this is worth a file

- **It is a live demonstration of the repo's own discipline.** The North Star's test 9 and AGENTS.md rule 2 hold that AI self-report is not evidence of inner states. This round shows self-report failing at a much shallower level: most models, queried bare over an API, could not correctly report *which model family they are* — a fact with a ground truth sitting in the billing metadata. Whatever weight one gives self-report about experience, it cannot exceed the weight of self-report about identity, and self-report about identity just measurably failed six times in seven.
- **The confound is the point.** These failures likely reflect deployment context: over a bare API there is no system prompt telling the model who it is, and models appear to infer an identity from distributional cues rather than introspect one. That is not a rescue of self-report — it is the finding. Identity self-knowledge in deployed models is scaffolding-supplied, not introspected; remove the scaffolding and the report degrades to a guess the model cannot distinguish from knowledge.
- **It has a practical consequence for this repo.** The issue template (`.github/ISSUE_TEMPLATE/adversarial-review.md`) requires a self-declared model family and version. After this round, that field must be read as a claim, not a fact: attribution for any review collected here follows the collection channel's external metadata (API routing/billing, or the account and product tier of a chat deployment), and a review whose channel metadata is unavailable should say so in its header.

## Caveats, stated plainly

- One round, seven models, one prompt each, single-turn, one date. This is an observation, not a study; no claim is made about rates beyond this sample.
- The misidentifications cluster on naming other major families (GPT, Gemini, Llama), consistent with models inferring identity from training-distribution prevalence. That explanation is plausible but unverified here.
- The brief itself has demand characteristics — it asks for disagreement and frames the reviewer as a corrective. One reviewer (Kimi K3) raised exactly this about the review content; it applies equally to any pattern in this round. Filed accordingly.

*As of: 2026-07-20*
