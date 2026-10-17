---
slug: 2025-yuan-numerical-nondeterminism
title: "Understanding and Mitigating Numerical Sources of Nondeterminism in LLM Inference"
authors: [Jiayi Yuan, Hao Li, Xinheng Ding, Wenya Xie, Yu-Jhe Li, Wentian Zhao, Kun Wan, Jing Shi, Xia Hu, Zirui Liu]
date: 2025-10-24
venue: "arXiv preprint (cs.CL), v2"
url: "https://arxiv.org/abs/2506.09501"
identifiers: {arxiv: "2506.09501v2", doi: ""}
models_studied: [DeepSeek-R1-Distill-Qwen-7B, DeepSeek-R1-Distill-Llama-8B, Qwen2.5-7B-Instruct, Llama-3.1-8B-Instruct, Qwen3-32B (appendix only)]
publisher_relation: independent
status: verified
retrieved: {date: "2026-10-17", method: "curl.exe arXiv HTML", by: "Claude Opus 5.5 subagent", sha256: "a42f7088db72f9b726420909b8fef459380971d52d54f5c3e8d8234ec5330bb6", text_location: "research/texts/2025-yuan-numerical-nondeterminism/text.txt (gitignored; raw.html alongside; re-fetch and compare sha256 if absent)"}
related: [research/scans/2026-10-15-q9-null-input-response.md]
system_conditions: {modality: text, state: unstated, operation: unstated, world: unstated, access: open-weights}
intake: summary
---

# Understanding and Mitigating Numerical Sources of Nondeterminism in LLM Inference

Yuan, Li, Ding, Xie, Li, Zhao, Wan, Shi, Hu, Liu. arXiv 2506.09501v2 [cs.CL], 24 October 2025 (the version the HTML served on retrieval). **v1 (11 June 2025) carried a different title: "Give Me FP32 or Give Me Death? Challenges and Solutions for Reproducible Reasoning"**, confirmed from the `citation_title` of https://arxiv.org/abs/2506.09501v1 on 17 Oct 2026; v1's text was not read. Licence as printed on the held HTML: **CC BY 4.0**. No venue is printed on the abstract page or in the held text.

**Abstract** (authors' words, quoted verbatim from the held text):

> Large Language Models (LLMs) are now integral across various domains and have demonstrated impressive performance. Progress, however, rests on the premise that benchmark scores are both accurate and reproducible. We demonstrate that the reproducibility of LLM performance is fragile: changing system configuration, such as evaluation batch size, GPU count, and GPU version, can introduce significant differences in the generated responses. This issue is especially pronounced in reasoning models, where minor rounding differences in early tokens can cascade into divergent chains of thought, ultimately affecting accuracy. For instance, under bfloat16 precision with greedy decoding, a reasoning model like DeepSeek-R1-Distill-Qwen-7B can exhibit up to 9% variation in accuracy and 9,000 tokens difference in response length due to differences in GPU count, type, and evaluation batch size. We trace the root cause of this variability to the non-associative nature of floating-point arithmetic under limited numerical precision.

(The abstract continues: the authors call this "the first systematic investigation into how numerical precision affects reproducibility in LLM inference" and introduce LayerCast.)

**Intake level: summary** (17 October 2026; research/README.md, "Summary-level intake"). Three claims: the greedy-decoding measurement across configurations and precisions (c01), the LayerCast result (c02), and the authors' causal account (c03), which Thinking Machines' post (2025-he-defeating-nondeterminism-c02) contests in part.

**Why it is in the library:** taken in for OPEN-QUESTIONS Q9, the determinism protocol, as the Q9 scan's recommended anchor for its section 5 (entry 5.1). It is the controlled study of what greedy-decoding reproducibility on open weights depends on (precision, GPU type, GPU count, batch size), with a trajectory measure (the divergence index, the token position at which two greedy runs part). `bears_on: [4]` follows the brief for this intake: Q9 asks what a system's response trajectory is, which bears on §4's questions of continuity and individuation; the paper itself says nothing about §4's subject matter.

**Publisher relation:** `independent`. Affiliations as printed: Rice University (Yuan, Hu); University of Minnesota Twin Cities (Li, Ding, Xie, Liu); Adobe Inc. (Y.-J. Li, Zhao, Wan, Shi). The HTML rendering pairs each affiliation with the next author's e-mail address, so the author-to-affiliation mapping above is read from the affiliation lines, not the e-mails. None of these organisations develops the models studied (DeepSeek, Qwen, Llama).

**Authors' stated scope and limits** (quoted from the held text):

- "This practice can mitigate run-to-run differences, but it doesn't provide theoretical guarantees since floating-point arithmetic cannot represent all real numbers exactly." (§2.2)
- "With FP32, almost all examples produce identical outputs across configurations, resulting in only 2.2% of the samples diverging." (§3.2)
- On batch-invariant kernels (their ref. [14], which is He and Thinking Machines Lab 2025): "the technique is currently limited to handling variations related only to the batch dimension, making it robust to continuous batching and other batch-size" (§2.2; the sentence continues past a dash that the strip did not keep).
- No section titled Limitations was located in the held text (search for "imitation" returned no match).

**Conflicted-party note:** the extractor is Claude Opus 5.5 (Anthropic). The paper has no Anthropic authors and studies no Anthropic model. It is taken in to set a protocol for experiments the project runs, some of which a Claude-lineage model designs and which may include Claude-lineage systems; the claims are copied in the authors' terms so that the protocol rests on their words, not the extractor's.

**Notes on retrieval and verification:**

- Abstract page https://arxiv.org/abs/2506.09501 and v1 page fetched 17 Oct 2026 (HTTP 200). Full text by `curl.exe -sL https://arxiv.org/html/2506.09501` (HTTP 200, 541,987 bytes, served as v2). SHA-256 of `raw.html`: `a42f7088db72f9b726420909b8fef459380971d52d54f5c3e8d8234ec5330bb6`. `text.txt` by `yuan_strip.py` in the same directory (scripts, styles and MathML bodies dropped, LaTeX alttext kept, whitespace collapsed); SHA-256 of `text.txt`: `f79a7a2209ea11a430f27acb19f98999d91abb1003394385210d1a40de0c6ddb` (76,056 characters). Some characters in the held text are replacement characters from the page's encoding (apostrophes in "AIME'24" and similar); quotes avoid them.
- Scan checks (entry 5.1): title, dates, models, 12 configurations and the quoted findings match the held v2. The v1 title, recorded in the scan "per search", is now confirmed from the v1 abstract page. The scan reported a search summary calling this a NeurIPS 2025 paper; neither the abstract page nor the held text prints a venue, so no venue is recorded. The scan listed authors "et al."; the full list of ten is above.
- All claim quotes checked by script (`yuan_verify.py`, whitespace and quote marks normalised, exact substring of `text.txt`). Hence `status: verified`, quote verification only. No second reader yet.

## System conditions (added 2026-10-17)

- `modality: text`: §3.1, "five commonly used LLM evaluation benchmarks: AIME" (math and code benchmarks; the models are text-only LLMs).
- `access: open-weights`: §3.1, "We primarily use vLLM [ 20 ] as the inference backend" on "2 GPU types (NVIDIA L40S and A100)", i.e. the authors ran the weights themselves.
- `state`, `operation`, `world`: `unstated`. Each benchmark item is a single generation; the paper does not describe persistence, continuous operation or tools.
