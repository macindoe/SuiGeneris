---
slug: 2024-luick-universal-response
title: "Universal Response and Emergence of Induction in LLMs"
authors: [Niclas Luick]
date: 2024-11-11
venue: "arXiv preprint (cs.LG), v1"
url: "https://arxiv.org/abs/2411.07071"
identifiers: {arxiv: "2411.07071v1", doi: ""}
models_studied: [Gemma-2-2B, Llama-3.2-3B-Instruct, GPT-2-XL]
publisher_relation: independent
status: verified
retrieved: {date: "2026-10-17", method: "curl.exe arXiv HTML", by: "claude-opus-5.5 (Agent tool model=opus)", sha256: "a7da85fb38d8e16ba706db03c61d3eac015da8d4bada3fea70b7393d4f4570ea", text_location: "research/texts/2024-luick-universal-response/text.txt (gitignored; raw.html alongside; re-fetch and compare sha256 if absent)"}
related: [research/scans/2026-10-15-q9-null-input-response.md]
system_conditions: {modality: text, state: none, operation: per-call, world: none, access: open-weights}
intake: summary
---

# Universal Response and Emergence of Induction in LLMs

Luick. arXiv 2411.07071v1 [cs.LG], 11 November 2024 (the only version listed on the abstract page on retrieval; comments "14 pages, 5 figures"). Licence as printed on the held HTML: **CC BY 4.0**.

**Abstract** (author's words, quoted verbatim from the held text; the HTML breaks it into lines, joined here with spaces):

> While induction is considered a key mechanism for in-context learning in LLMs, understanding its precise circuit decomposition beyond toy models remains elusive. Here, we study the emergence of induction behavior within LLMs by probing their response to weak single-token perturbations of the residual stream. We find that LLMs exhibit a robust, universal regime in which their response remains scale-invariant under changes in perturbation strength, thereby allowing us to quantify the build-up of token correlations throughout the model. By applying our method, we observe signatures of induction behavior within the residual stream of Gemma-2-2B, Llama-3.2-3B, and GPT-2-XL. Across all models, we find that these induction signatures gradually emerge within intermediate layers and identify the relevant model sections composing this behavior. Our results provide insights into the collective interplay of components within LLMs and serve as a benchmark for large-scale circuit analysis.

**Intake level: summary** (17 October 2026; research/README.md, "Summary-level intake"). Three claims: the scale-invariant response to a single-position perturbation on a repeated random-token background (c01); the induction signature's emergence across layers (c02); the author's Limitations section (c03).

**Why it is in the library:** taken in for Q9 as the scan's recommended anchor for its section 4, response-theoretic treatments (entry 4.1); it was also a candidate in the Q2 scan (entry 15). It is the nearest published instance of the measurement Q9 describes: a small perturbation applied at one input position of the residual stream, with the response read at every later position and layer, on open weights in three families, on a background of random tokens.

**Publisher relation:** `independent`. Affiliation as printed: "University of Hamburg", "22761 Hamburg, Germany", with an address at physnet.uni-hamburg.de. The studied models are Google's, Meta's and OpenAI's.

**Author's stated scope and limits:** a section headed "Limitations" is printed after the Conclusion (quoted in c03). The models are listed in Appendix A, Table 1, with licences.

**Conflicted-party note:** the extractor is Claude Opus 5.5 (Anthropic). The paper studies no Anthropic model; it informs a project experiment (Q9) designed by a Claude-lineage model on a class of systems that includes the extractor's lineage. Claims keep to the author's words. The paper measures token correlations (induction), not anything about a model's account of itself.

**Notes on retrieval and verification:**

- Abstract page `https://arxiv.org/abs/2411.07071` fetched 17 Oct 2026 with `curl.exe` (HTTP 200; held as `abs.html`). Full text `https://arxiv.org/html/2411.07071` fetched the same day (HTTP 200, 218,356 bytes, served as v1). SHA-256 of `raw.html`: `a7da85fb38d8e16ba706db03c61d3eac015da8d4bada3fea70b7393d4f4570ea`. Stripped by `strip_q9c_luick.py` (same directory, `python -I`) to `text.txt`, SHA-256 `033987549fc39ffe8dae9a6b61475e4539bc0625f6c847c4566865ce61025000` (51,909 bytes).
- **Correction to the Q2 scan, recorded as the Q9 scan asked.** The Q2 scan (entry 15) gave the affiliation as "not extracted", the publisher relation as inferred from a single-author arXiv paper, and the limitations as "not available from the abstract page". The held full text prints the affiliation **University of Hamburg** and has a section headed **Limitations** (c03). The Q9 scan's correction is confirmed.
- Scan checks (entry 4.1): title, author, date and arXiv id match; the scan's quotations from Figure 1, §2, §3 and the Limitations section were found in the held text. Two precisions. (1) The model the text calls "Llama-3.2-3B" is listed in Appendix A, Table 1 as **Llama-3.2-3B-Instruct**; `models_studied` follows the table. (2) The perturbation is a scaling of one position's input vector, x to (1 − ε)·x (Figure 1, §2.1), not an added vector; the scan's word "impulse" is the scan's.
- All claim quotes and the quotes in this file checked by script (`verify_q9c_luick.py`, same directory; whitespace and quote marks normalised, exact substring match against `text.txt`). Hence `status: verified`, quote verification only. No second reader yet.

## System conditions (added 2026-10-17)

- `modality: text`: Figure 1, the input is "repeated subsequences of length T_{0}=T/2 , consisting of random tokens sampled uniformly from the vocabulary space."
- `state: none`: each response is a comparison of two forward passes (perturbed and unperturbed) over one sequence; §2.1, "comparing the evolution of the perturbed vector".
- `operation: per-call`: as for `state`.
- `world: none`: no tools or environment are described.
- `access: open-weights`: Appendix A, "The experiments described within this work were performed using the TransformerLens library [74] which enables accessing and modifying activations within transformer models."
