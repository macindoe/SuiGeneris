---
slug: 2026-bruckner-one-token
title: "One Token Is Enough: Fingerprinting and Verifying Large Language Models from Single-Token Output Distributions"
authors: [Tomáš Bruckner]
date: 2026-07-11
venue: "arXiv preprint (cs.CR), v1"
url: "https://arxiv.org/abs/2607.10252"
identifiers: {arxiv: "2607.10252v1", doi: ""}
models_studied: ["165 models served via OpenRouter (catalog snapshot 2026-07-06), 19 family labels including claude (12 models), gpt, qwen, llama, gemini, deepseek, mistral, glm", "31 models served by two or more providers (34 provider pairs)"]
publisher_relation: independent
status: verified
retrieved: {date: "2026-10-17", method: "curl.exe arXiv HTML", by: "Claude Opus 5.5 subagent", sha256: "40953921caa2ae02c5c931ebba8c52bf8af9b89681bbc308e3fc5b6e8256d3a4", text_location: "research/texts/2026-bruckner-one-token/text.txt (gitignored; raw.html alongside; re-fetch and compare sha256 if absent)"}
related: [research/scans/2026-10-15-q9-null-input-response.md]
system_conditions: {modality: text, state: unstated, operation: per-call, world: unstated, access: api}
intake: summary
---

# One Token Is Enough: Fingerprinting and Verifying Large Language Models from Single-Token Output Distributions

Tomáš Bruckner. arXiv 2607.10252v1 [cs.CR], 11 July 2026 (the only version on the abstract page at retrieval). Licence as printed on the held HTML: arXiv.org perpetual non-exclusive licence. The author states that the protocol, prompts, raw data and code are released (Zenodo; refs. [24], [25]) and that hypotheses were pre-registered (ref. [26]); none of these was retrieved.

**Abstract** (author's words, quoted verbatim from the held text; the en dashes are as printed):

> Large language models (LLMs) are increasingly consumed through opaque serving chains – API aggregators, resellers, and inference providers – in which the client has no technical means to confirm that the model answering is the model advertised, and recent audits show that a substantial fraction of commercial endpoints deviate from the vendor’s reference weights. Existing identification techniques require long generated texts, token-level log-probabilities, adversarially crafted prompts, or the model owner’s cooperation. We show that far weaker evidence suffices. We define a behavioral fingerprint of an LLM as the empirical distribution of its answers to trivial one-word prompts – “name a random number between 1 and 100” – collected across four languages at a cost of one output token per query.

(The abstract continues with the three results recorded in c02 and the ecosystem anomalies.)

**Intake level: summary** (17 October 2026). Two claims: the temperature-0 determinism rates (c01) and the fingerprinting result (c02).

**Why it is in the library:** taken in for OPEN-QUESTIONS Q9 (Q9 scan, entry 6.2): it measures temperature-0 determinism on OpenRouter, the aggregator the project's review rounds use, across 165 models, and shows that one-token answers to trivial prompts identify models and lineage. `bears_on: [4]` follows the brief for this intake; the paper is about API auditing and says nothing about §4's subject matter.

**Publisher relation:** `independent`. Affiliation as printed: Faculty of Informatics and Statistics, Prague University of Economics and Business, Prague, Czech Republic. Single author. Funding (Acknowledgments): "The OpenRouter API credit was funded by the author’s personal funds."

**Author's stated limits** (§VII-D and elsewhere, quoted from the held text):

- "Fingerprints drift with model updates, so reference enrollment must be refreshed; we quantify short-horizon stability but not multi-month drift." (§VII-D)
- "Finally, our census covers one aggregator; the protocol is aggregator-agnostic, but ecosystem findings may not generalize." (§VII-D)
- "For the latter we cannot certify that the answer is a direct single-pass sample rather than the output of a hidden deliberation phase" (§VII-D; such endpoints were excluded).
- "A dedicated paraphrase-invariance experiment is left to future work." (§VII-B)
- "All findings below are statistical statements about served distributions, not claims of intent" (§VI-D).

**Conflicted-party note:** the extractor is Claude Opus 5.5 (Anthropic). Two further Claude-lineage involvements, from the paper itself:

- Acknowledgments, verbatim: "Claude Code (Anthropic) was used to provide ongoing assistance with the study design, data collection, processing of results, and drafting of the manuscript. All outputs were verified and corrected by the author."
- Claude models are among those studied: the family table lists "claude 12" (Table II), and Fig. 1 shows "Claude Sonnet 5 concentrates on 47".

So a Claude-lineage tool helped design and draft a study that includes Claude-lineage models, and a Claude-lineage model is extracting it. None of this is a reason to discount the paper; it is recorded so a reader can weigh it, and claims are kept to the author's words.

**Notes on retrieval and verification:**

- Abstract page and HTML fetched 17 Oct 2026 with `curl.exe -sL` (HTTP 200; HTML 143,212 bytes). SHA-256 of `raw.html`: `40953921caa2ae02c5c931ebba8c52bf8af9b89681bbc308e3fc5b6e8256d3a4`. `text.txt` by `bruckner_strip.py` in the same directory; SHA-256 `15f4fb860c0b85f441f34614ac530dc6cfb1ad56379ed88d39e4ab4aa491cc16` (48,169 characters).
- Scan checks (entry 6.2): date, model counts and every quoted passage match the held text; the determinism sentence is in §VI-A (the scan said §VI). **Discrepancy:** the scan recorded the affiliation as "not extracted"; the held text prints the Prague University of Economics and Business (above). The scan wrote the name "Tomas"; the paper prints "Tomáš".
- All claim quotes checked by script (`bruckner_verify.py`, whitespace, quote marks and dashes normalised, exact substring of `text.txt`). Hence `status: verified`, quote verification only. No second reader yet.

## System conditions (added 2026-10-17)

- `modality: text`: §V, the census excludes identifiers that are "not plain text-to-text chat models".
- `operation: per-call`: §IV-E, "every request is a deterministic cell repetition".
- `access: api`: §IV-E, "Data collection runs against the OpenRouter aggregator API".
- `state`, `world`: `unstated`.
