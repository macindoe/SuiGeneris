---
slug: 2025-he-defeating-nondeterminism
title: "Defeating Nondeterminism in LLM Inference"
authors: [Horace He, Thinking Machines Lab]
date: 2025-09-10
venue: "web page (Thinking Machines Lab: Connectionism blog)"
url: "https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/"
identifiers: {arxiv: "", doi: "10.64434/tml.20250910"}
models_studied: [Qwen/Qwen3-235B-A22B-Instruct-2507, Qwen-3-8B (performance only), Qwen 2.5-VL instruct 8B (RL experiment only)]
publisher_relation: independent
status: verified
retrieved: {date: "2026-10-17", method: "Windows curl.exe of the web page", by: "Claude Opus 5.5 subagent", sha256: "92e7e5913329be53ab8341bc782427e22d12c61f1bb8e5b51cc42bd0188f0654", text_location: "research/texts/2025-he-defeating-nondeterminism/text.txt (gitignored; raw.html alongside; re-fetch and compare sha256 if absent; a live page may change, so a mismatch is expected over time)"}
related: [research/scans/2026-10-15-q9-null-input-response.md]
system_conditions: {modality: text, state: unstated, operation: unstated, world: unstated, access: open-weights}
intake: summary
---

# Defeating Nondeterminism in LLM Inference

Horace He "in collaboration with others at Thinking Machines", 10 September 2025, Thinking Machines Lab blog *Connectionism*. A web page, not peer reviewed. The page's own citation block gives: He, Horace and Thinking Machines Lab, "Defeating Nondeterminism in LLM Inference", Thinking Machines Lab: Connectionism, Sep 2025, DOI 10.64434/tml.20250910 (the DOI is as printed on the page; it was not resolved).

**Summary** (paraphrase; the page has no abstract): the post argues that LLM inference is nondeterministic for users even at temperature 0, not because GPU kernels race (the forward-pass kernels are "run-to-run deterministic") but because they are not batch-invariant, so a request's numerics depend on the batch size, which depends on server load. It describes batch-invariant RMSNorm, matrix multiplication and attention kernels, releases them (`thinking-machines-lab/batch-invariant-ops`) with a vLLM demonstration, and reports that with them 1,000 temperature-0 completions of one prompt become identical.

**Intake level: summary** (17 October 2026). Two claims: the 1,000-completions measurement (c01) and the author's account of the cause (c02), which contests the account in Yuan et al. 2025 (2025-yuan-numerical-nondeterminism-c03).

**Why it is in the library:** taken in for OPEN-QUESTIONS Q9, the determinism protocol, as the companion to Yuan et al. 2025 that names batch invariance (Q9 scan, entry 5.2). `bears_on: [4]` follows the brief for this intake (Q9's response-trajectory question); the page says nothing about §4's subject matter.

**Publisher relation:** `independent`, inferred: the author's organisation, Thinking Machines Lab, did not develop the model studied (Qwen, Alibaba). On the day of retrieval the site's navigation lists models of the lab's own ("Inkling", "Inkling-Small"); none is studied in this post.

**Author's stated limits** (quoted from the held text):

- "We have not put a significant effort into optimizing the performance of the batch-invariant kernels here." (Performance; the reported times are 26 s for vLLM default, 55 s unoptimised deterministic, 42 s with an improved attention kernel, Qwen-3-8B, 1,000 sequences.)
- "This requires some internal FlexAttention changes that are not included in our code release." (Batch-invariant attention)
- "Reductions related to parallelism are out of the scope of this discussion, but the same principles apply." (How do we make kernels batch-invariant?)

**Relation to Yuan et al. 2025:** the post quotes a sentence of Yuan et al. §2.2 as "a recent arXiv preprint" exemplifying the "concurrency + floating point" hypothesis and links arXiv 2506.09501. Yuan v2 (24 Oct 2025) in turn cites this post as its ref. [14]. Recorded as a contest on the interpretation claims (c02 contests Yuan c03), not on either side's measurements.

**Conflicted-party note:** the extractor is Claude Opus 5.5 (Anthropic). The post has no Anthropic author and studies no Anthropic model. Its finding governs how the project runs experiments that a Claude-lineage model designs and that may include Claude-lineage systems; claims are kept to the author's words.

**Notes on retrieval and verification:**

- Git-Bash `curl.exe` (`/mingw64/bin/curl.exe`) failed with exit 43 on 17 Oct 2026, as the Q9 scan reported for 15 Oct; Windows `C:/Windows/System32/curl.exe -sL` succeeded (HTTP 200, 97,784 bytes). Not a refusal by the host. SHA-256 of `raw.html`: `92e7e5913329be53ab8341bc782427e22d12c61f1bb8e5b51cc42bd0188f0654`. `text.txt` by `he_strip.py` in the same directory (scripts, styles, SVG and noscript dropped, tags stripped, whitespace collapsed); SHA-256 `eeb60e6846ece7ec97a523773c5bde3424abd93581113e12e787e8bf3a350360` (38,075 characters). The page's footer reads "Thinking Machines Lab © 2026". Some mathematical symbols (the "not equal" sign) were lost in stripping; quotes avoid them.
- Scan checks (entry 5.2): date, models, and every quoted passage match the held text, including the page's spelling "occuring". The scan's statement that the post is "independent of the studied model (Qwen)" is consistent with the page. The scan did not record the DOI or that the post names Yuan et al. as its example of the hypothesis it rejects; both are added here.
- All claim quotes checked by script (`he_verify.py`, whitespace and quote marks normalised, exact substring of `text.txt`). Hence `status: verified`, quote verification only. No second reader yet.

## System conditions (added 2026-10-17)

- `modality: text`: Experiments, "sample 1000 completions at temperature 0 with the prompt “Tell me about Richard Feynman” (non-thinking mode), generating 1000 tokens each".
- `access: open-weights`: Implementation, "We provide a demonstration of deterministic inference on top of vLLM"; the author runs the Qwen weights on his own server with his own kernels.
- `state`, `operation`, `world`: `unstated`.
