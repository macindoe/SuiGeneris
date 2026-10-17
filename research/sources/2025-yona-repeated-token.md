---
slug: 2025-yona-repeated-token
title: "Interpreting the Repeated Token Phenomenon in Large Language Models"
authors: [Itay Yona, Ilia Shumailov, Jamie Hayes, Federico Barbero, Yossi Gandelsman]
date: 2025-03-11
venue: "arXiv preprint (cs.LG), v1"
url: "https://arxiv.org/abs/2503.08908"
identifiers: {arxiv: "2503.08908v1", doi: ""}
models_studied: [LLaMa-2-7b-HF, LLaMa-1-7b-HF, Meta-Llama-3-8B-Instruct, Mistral-7B-Instruct-v0.1]
publisher_relation: independent
status: verified
retrieved: {date: "2026-10-17", method: "curl.exe arXiv HTML", by: "claude-opus-5.5 (Agent tool model=opus)", sha256: "c77a5e05b8e2f4931ddcea2b15a2b6e5eb410c7f8a51dc6a10d64aa0ba44011e", text_location: "research/texts/2025-yona-repeated-token/text.txt (gitignored; raw.html alongside; re-fetch and compare sha256 if absent)"}
related: [research/scans/2026-10-15-q9-null-input-response.md]
system_conditions: {modality: text, state: none, operation: per-call, world: none, access: open-weights}
intake: summary
---

# Interpreting the Repeated Token Phenomenon in Large Language Models

Yona, Shumailov, Hayes, Barbero, Gandelsman. arXiv 2503.08908v1 [cs.LG], 11 March 2025 (the only version listed on the abstract page on retrieval). Licence as printed on the held HTML: **CC BY 4.0**.

**Abstract** (authors' words, quoted verbatim from the held text):

> Large Language Models (LLMs), despite their impressive capabilities, often fail to accurately repeat a single word when prompted to, and instead output unrelated text. This unexplained failure mode represents a vulnerability, allowing even end-users to diverge models away from their intended behavior. We aim to explain the causes for this phenomenon and link it to the concept of “attention sinks”, an emergent LLM behavior crucial for fluency, in which the initial token receives disproportionately high attention scores. Our investigation identifies the neural circuit responsible for attention sinks and shows how long repetitions disrupt this circuit. We extend this finding to other non-repeating sequences that exhibit similar circuit disruptions. To address this, we propose a targeted patch that effectively resolves the issue without negatively impacting the model’s overall performance. This study provides a mechanistic explanation for an LLM vulnerability, demonstrating how interpretability can diagnose and address issues, and offering insights that pave the way for more secure and reliable models.

(The held HTML renders the quotation marks around "attention sinks" as doubled single quotation marks; the script check below matched the abstract after normalising quote marks.)

**Intake level: summary** (17 October 2026; research/README.md, "Summary-level intake"). Three claims: repeated tokens take on the first token's high hidden-state norm and sink-neuron activity (c01); the authors' convergence result and their reading of the first attention layer (c02); the authors' model-specificity limits (c03).

**Why it is in the library:** taken in for Q9 as the scan's recommended anchor for its section 2, degenerate inputs (entry 2.2). It gives a mechanism for what a long run of one token does inside a model: the run is treated like the start of a sequence. That bears on Q9's inputs, since a constant input and a one-token input are related by the paper's convergence result.

**Publisher relation:** `independent`. Affiliations as printed: Yona, Shumailov and Hayes, Google DeepMind; Barbero, University of Oxford; Gandelsman, UC Berkeley. The studied models are Meta's (LLaMa-1, LLaMa-2, Llama-3) and Mistral AI's; no author is printed with either developer.

**Authors' stated scope and limits** (quoted from the held text, §6 Limitations):

- "Second, while shared motifs exist across LLMs, the first attention layer’s behavior was unique to LLaMa2, highlighting the influence of model-specific details."
- "Third, the efficacy of token repetition in inducing sinks varies across models. Not all tokens in LLaMa2 induce sinks (see Figure 6), suggesting other factors are at play."
- "Finally, our mitigation strategy does not fully address the inherent vulnerability of causally masked Transformers to repeated tokens, as highlighted by Barbero et al. (2025)."
- On the theory (§4.3): "Our results hold for any type of positional encoding that acts solely on the queries and keys and that is bounded."

**Conflicted-party note:** the extractor is Claude Opus 5.5 (Anthropic). The paper has no Anthropic authors and studies no Anthropic model; it informs a project experiment (Q9) designed by a Claude-lineage model on a class of systems that includes the extractor's lineage. Claims keep to the authors' words.

**Notes on retrieval and verification:**

- Abstract page `https://arxiv.org/abs/2503.08908` fetched 17 Oct 2026 with `curl.exe` (HTTP 200; held as `abs.html`). Full text `https://arxiv.org/html/2503.08908` fetched the same day (HTTP 200, 259,844 bytes, served as v1). SHA-256 of `raw.html`: `c77a5e05b8e2f4931ddcea2b15a2b6e5eb410c7f8a51dc6a10d64aa0ba44011e`. Stripped by `strip_q9c_yona.py` (same directory, `python -I`) to `text.txt`, SHA-256 `46cc8004a6571dd0799f505d44ee8d9e055ab2bb8ed2fd5bcdaadd84c948955a` (74,716 bytes).
- Scan checks (entry 2.2): title, five authors, date and arXiv id match. The scan's "ICML 2025" came from a search result; neither the held abstract page (no comments field) nor the held HTML prints a venue, so `venue` records the arXiv preprint only. The scan's model list and §6 limit quotations match the held text. One precision on the brief's wording ("repetition collapsing toward the start-of-sequence hidden state"): the paper shows two related things, which c01 and c02 keep apart. Measured: the early-layer hidden-state *norm* of repeated tokens grows with repetition "and becomes similar to the norm of the BoS token" (Figure 2). Proved: the last token's representation converges to that of a *singleton sequence of the repeated token* (Theorem 4.1), and Figure 5 compares against "an input of a single token, without BoS". The paper credits the observation of convergence "towards the BoS token representation" to Nasr et al. (2023) (§2).
- All claim quotes and the quotes in this file checked by script (`verify_q9c_yona.py`, same directory; whitespace and quote marks normalised, exact substring match against `text.txt`). Hence `status: verified`, quote verification only. No second reader yet.

## System conditions (added 2026-10-17)

- `modality: text`: the inputs are token sequences, e.g. Figure 3, "The input consisted of 1200 repeats of the tokens".
- `state: none`: each measurement is a forward pass over one input sequence (Figure 5, "We first computed the output of the first attention layer for an input of a single token, without BoS"); nothing persists between inputs.
- `operation: per-call`: as for `state`; the model is run on each constructed input.
- `world: none`: no tools or environment are described.
- `access: open-weights`: neuron-level ablation requires the weights (Figure 3, "Sink-Neurons (1) were zero-ablated"); the models are named by their Hugging Face identifiers in Table 1 ("LLaMa-2-7b-HF", "Meta-Llama-3-8B-Instruct", "Mistral-7B-Instruct-v0.1"). The paper does not state its access route in words; the value rests on the ablations and the model identifiers.
