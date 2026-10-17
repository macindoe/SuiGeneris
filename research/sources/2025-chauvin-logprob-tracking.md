---
slug: 2025-chauvin-logprob-tracking
title: "Log Probability Tracking of LLM APIs"
authors: [Timothée Chauvin, Erwan Le Merrer, François Taïani, Gilles Tredan]
date: 2026-02-27
venue: "arXiv preprint (cs.LG), v2; ICLR 2026 (per arXiv comments)"
url: "https://arxiv.org/abs/2512.03816"
identifiers: {arxiv: "2512.03816v2", doi: ""}
models_studied: [Qwen/Qwen2.5-0.5B-Instruct, google/gemma-3-1b-it, microsoft/Phi-3-mini-4k-instruct, meta-llama/Llama-3.1-8B-Instruct, allenai/OLMo-2-1124-7B-Instruct, "290 TinyChange variants of these five", "189 API endpoints from 10 providers", GPT-4.1 (non-determinism illustration)]
publisher_relation: independent
status: verified
retrieved: {date: "2026-10-17", method: "curl.exe arXiv HTML", by: "Claude Opus 5.5 subagent", sha256: "98d0de7425addb558eaa0c6518505fbc2e31a661843b4ba9fa8f33a5e82270a4", text_location: "research/texts/2025-chauvin-logprob-tracking/text.txt (gitignored; raw.html alongside; re-fetch and compare sha256 if absent)"}
related: [research/scans/2026-10-15-q9-null-input-response.md]
system_conditions: {modality: text, state: unstated, operation: per-call, world: unstated, access: both}
intake: summary
---

# Log Probability Tracking of LLM APIs

Chauvin, Le Merrer, Taïani, Tredan. arXiv 2512.03816v2 [cs.LG], 27 February 2026 (v1 3 December 2025; v2 is the version the HTML served on retrieval). arXiv comments: "ICLR 2026". Licence as printed on the held HTML: arXiv.org perpetual non-exclusive licence. Code: github.com/timothee-chauvin/track-llm-apis.

**Abstract** (authors' words, quoted verbatim from the held text):

> When using an LLM through an API provider, users expect the served model to remain consistent over time, a property crucial for the reliability of downstream applications and the reproducibility of research. Existing audit methods are too costly to apply at regular time intervals to the wide range of available LLM APIs. This means that model updates are left largely unmonitored in practice. In this work, we show that while LLM log probabilities (logprobs) are usually non-deterministic, they can still be used as the basis for cost-effective continuous monitoring of LLM APIs. We apply a simple statistical test based on the average value of each token logprob, requesting only a single token of output. This is enough to detect changes as small as one step of fine-tuning, making this approach more sensitive than existing methods while being 1,000x cheaper. We introduce the TinyChange benchmark as a way to measure the sensitivity of audit methods in the context of small, realistic model changes.

**Intake level: summary** (17 October 2026). Two claims: the single-token design and its sensitivity on TinyChange (c01), and the drift detections on real endpoints (c02).

**Why it is in the library:** taken in for OPEN-QUESTIONS Q9 as the Q9 scan's recommended anchor for its section 6 (entry 6.1): the nearest published design to a null-input identity probe, in which a minimal, fixed, content-free input is sent repeatedly and the distribution of the response is the signature, with run-to-run non-determinism handled statistically. `bears_on: [4]` follows the brief for this intake; the paper is about API monitoring and says nothing about §4's subject matter.

**Publisher relation:** `independent`. Affiliations as printed: Chauvin, Le Merrer, Taïani, Université de Rennes, Inria, CNRS/IRISA (Rennes, France); Tredan, LAAS, CNRS (Toulouse, France). None develops a model studied. Funding (Acknowledgments): the French ANR (project PACMAM; Cluster SequoIA Chair FANG) and GENCI computing at IDRIS (Jean Zay).

**Authors' stated limits** (§4, quoted from the held text):

- "Our approach applies to APIs that support and return log probabilities."
- "Our method does not distinguish between infrastructure changes and model updates, or give information on the exact nature of the change."
- "Certain modifications may evade first-token detection."
- "Providers could be tempted to evade LT's detection by identifying monitoring queries and providing consistent responses only to these prompts."

**Conflicted-party note:** the extractor is Claude Opus 5.5 (Anthropic). The paper has no Anthropic author and no Anthropic endpoint appears in its provider table (Table 2). The design is prior art for a probe the project may run on systems that include the extractor's own lineage; claims are kept to the authors' words.

**Notes on retrieval and verification:**

- Abstract page and HTML fetched 17 Oct 2026 with `curl.exe -sL` (HTTP 200; HTML 188,015 bytes, served as v2). SHA-256 of `raw.html`: `98d0de7425addb558eaa0c6518505fbc2e31a661843b4ba9fa8f33a5e82270a4`. `text.txt` by `chauvin_strip.py` in the same directory; SHA-256 `9d3d485cf5499d04e505e3e1fb2766bc52085b60435e4f31257de38dcc94ed38` (49,403 characters).
- Scan checks (entry 6.1): dates, ICLR comment, model counts and every quoted passage match the held text. **Discrepancy:** the scan gave all four authors the Rennes affiliation; the held text prints Tredan at LAAS, CNRS (Toulouse). The scan's "Figure 2 shows the logprobs returned over two weeks time by GPT-4.1" matches the text, though the HTML's figure captions are numbered the other way round (Figure 1 is captioned as the GPT-4.1 logprobs); the paper's numbering is recorded as printed.
- All claim quotes checked by script (`chauvin_verify.py`, whitespace and quote marks normalised, exact substring of `text.txt`). Hence `status: verified`, quote verification only. No second reader yet.

## System conditions (added 2026-10-17)

- `modality: text`: §3.2.1, "we therefore use the shortest prompt, made of the single letter ”x”, which is 1 to 2 tokens long depending on the tokenizer".
- `operation: per-call`: §2.3, "we send the same prompt to two LLM APIs, requesting a single token of output, repeating for N samples".
- `access: both`: open weights run locally, §3.1, "we generate S=10,000 samples per prompt using vLLM"; and served APIs, §3.2.3, "we monitored 189 real-world LLM API endpoints from 10 providers hourly over more than 4 months".
- `state`, `world`: `unstated`.
