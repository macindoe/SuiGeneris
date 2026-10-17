---
slug: 2026-kwon-what-llms-think
title: "What LLMs Think When You Don't Tell Them What to Think About?"
authors: [Yongchan Kwon, James Zou]
date: 2026-02-02
venue: "arXiv preprint (cs.AI), v1"
url: "https://arxiv.org/abs/2602.01689"
identifiers: {arxiv: "2602.01689v1", doi: ""}
models_studied: [GPT-OSS-20B, GPT-OSS-120B, DeepSeek-V3, DeepSeek-V3.1, LLaMA-3.1-70B, LLaMA-3.1-405B, LLaMA-3.2-3B, LLaMA-3.3-70B, LLaMA-4-Maverick, Qwen2.5-7B, Qwen2.5-72B, Qwen3-235B-Instruct, Qwen3-235B-Thinking, Qwen3-Coder, Qwen3-Next-80B-Instruct, Qwen3-Next-80B-Thinking]
publisher_relation: independent
status: verified
retrieved: {date: "2026-10-17", method: "curl.exe arXiv HTML", by: "claude-opus-5.5 (Agent tool model=opus)", sha256: "8cdc48dee1aa52d02a7512aa09da859cb9401477dbfac9d0e12f2bf6124f71f8", text_location: "research/texts/2026-kwon-what-llms-think/text.txt (gitignored; raw.html alongside; re-fetch and compare sha256 if absent)"}
related: [research/scans/2026-10-15-q9-null-input-response.md]
system_conditions: {modality: text, state: none, operation: per-call, world: none, access: open-weights}
intake: summary
---

# What LLMs Think When You Don't Tell Them What to Think About?

Kwon and Zou. arXiv 2602.01689v1 [cs.AI], 2 February 2026 (the only version listed on the abstract page on retrieval). Licence as printed on the held HTML: **CC BY 4.0**. Dataset and code released (Hugging Face dataset `ykwon-hf/unconditional_text_generation`; GitHub `ykwon0407/LLM_TOM`, as printed).

**Abstract** (authors' words, quoted verbatim from the held text):

> Characterizing the behavior of large language models (LLMs) across diverse settings is critical for reliable monitoring and AI safety. However, most existing analyses rely on topic- or task-specific prompts, which can substantially limit what can be observed. In this work, we study what LLMs generate from minimal, topic-neutral inputs and probe their near-unconstrained generative behavior. Despite the absence of explicit topics, model outputs cover a broad semantic space, and surprisingly, each model family exhibits strong and systematic topical preferences. GPT-OSS predominantly generates programming (27.1%) and mathematical content (24.6%), whereas Llama most frequently generates literary content (9.1%). DeepSeek often generates religious content, while Qwen frequently generates multiple-choice questions. Beyond topical preferences, we also observe differences in content specialization and depth: GPT-OSS often generates more technically advanced content (e.g., dynamic programming) compared with other models (e.g., basic Python). Furthermore, we find that the near-unconstrained generation often degenerates into repetitive phrases, revealing interesting behaviors unique to each model family. For instance, degenerate outputs from Llama include multiple URLs pointing to personal Facebook and Instagram accounts. We release the complete dataset of 256,000 samples from 16 LLMs, along with a reproducible codebase.

**Intake level: summary** (17 October 2026; research/README.md, "Summary-level intake"). Three claims: family-specific topical defaults (c01), degeneration rates by family (c02), and the chat-template remark (c03).

**Why it is in the library:** taken in for Q9 (the null-input experiment), as the Q9 scan's recommended anchor for its section 1 (entry 1.1). It is the retrieved study whose question is closest to Q9's: what a model produces when given almost nothing to go on, across families, with the chat template removed and degenerate text treated as a signal. Its design differs from Q9's in ways that matter for any comparison: 36 topic-neutral seed prompts rather than an empty prompt, and sampling at temperature 1.0 with top-p 0.9 rather than greedy decoding (§2). Filed under `bears_on: 4` as a measurement of what a model's output looks like when the input carries almost no instruction.

**Publisher relation:** `independent`. The held HTML prints two affiliations, "Together AI" and "Stanford University", with a correspondence address at stanford.edu; the rendering loses which author holds which (both author notes read "Affiliation: [" in the HTML). No studied model is developed by Stanford or Together AI (the families are OpenAI's GPT-OSS, DeepSeek's, Meta's Llama and Alibaba's Qwen). Together AI is an inference provider that serves open-weight models; the paper does not say whether the generations were run on its infrastructure, and this note does not infer it.

**Authors' stated scope and limits** (quoted from the held text):

- "This suggests that distinguishing individual models based on category information can be challenging and likely requires additional signals or finer-grained analyses" (§3.2; GPT-OSS-120B and -20B similarity 0.94, Qwen3-235B-Instruct and -Thinking 0.93).
- "These observations suggest that prompt style can shape the resulting label distributions" (§6, "Prompt design and its impact").
- "We hypothesize that this prevalence reflects extensive use of multiple-choice exam data during Qwen's training." (§3.2; a hypothesis, untested in the paper.)
- Labelling is by an LLM: "We instruct GPT-OSS-120B to annotate each sample with both a general category (e.g., mathematics) and a corresponding subcategory (e.g., topology)." (§2). The authors check the dual use of GPT-OSS-120B as generator and labeller against two other labellers (Appendix A.2; see the conflicted-party note).

**Conflicted-party note:** the extractor is Claude Opus 5.5 (Anthropic). No studied model is Anthropic's, but Appendix A.2 uses "Claude-4.5-Opus" (with "Gemini-2.5-Pro-Flash", both as printed) as a second labeller to check GPT-OSS-120B's category labels on a 32,768-sample subset; a Claude-lineage model therefore contributes to the robustness check behind c01. The paper informs a project experiment (Q9) on models that include the extractor's lineage. Claims keep to the authors' words; nothing here draws on the extractor's own sense of what a "top-of-mind" default is.

**Notes on retrieval and verification:**

- Abstract page `https://arxiv.org/abs/2602.01689` fetched 17 Oct 2026 with `curl.exe` (HTTP 200; held as `abs.html` beside the raw file). Full text `https://arxiv.org/html/2602.01689` fetched the same day (HTTP 200, 242,547 bytes, served as v1). SHA-256 of `raw.html`: `8cdc48dee1aa52d02a7512aa09da859cb9401477dbfac9d0e12f2bf6124f71f8`. Stripped by `strip_q9c_kwon.py` (same directory, run with `python -I`) to `text.txt`, SHA-256 `45f0318c21b8885c303fdab90ad1df81b11139b0b1d9e70ec86e8cf642ba9e42` (79,381 bytes).
- Scan checks (entry 1.1): title, authors, date (2 Feb 2026, v1) and arXiv id match. The scan gives the affiliation as "Stanford University printed in the full text"; the held text also prints "Together AI" (author mapping lost in the HTML). The scan's quotations from §2, Remark 2.1, §4 and App. A.1 were found in the held text. The scan placed the "distinguishing individual models" sentence under §6; the held text has it in §3.2 (the §6 paragraph "Model-family level and individual-model level analysis" discusses the same point).
- All claim quotes and the quotes in this file checked by script (`verify_q9c_kwon.py`, same directory: whitespace and quote marks normalised, exact substring match against `text.txt`). Hence `status: verified`, quote verification only. No second reader yet.

## System conditions (added 2026-10-17)

- `modality: text`: §2, "the model receives only a randomly sampled seed prompt"; the seed prompts are text (Table 1, Appendix C).
- `state: none`: §2, "For (C2), we do not use a chat template, which is commonly used in chat systems with a system prompt and role-based tags. Instead, the model receives only a randomly sampled seed prompt." Each sample is one generation from one seed; nothing persists between samples.
- `operation: per-call`: §2, "we generate text autoregressively from a randomly selected seed prompt, continuing until either the maximum token limit is reached or an end-of-sequence token is sampled."
- `world: none`: no tools or environment are described; the input is the seed prompt alone (quote under `state`).
- `access: open-weights`: §3.1, "We focus on open-source models to ensure that text generation is not influenced by any external system prompts, hidden instruction tuning, or post-processing potentially applied in API-based deployments". The inference stack (local or hosted) is not stated.
