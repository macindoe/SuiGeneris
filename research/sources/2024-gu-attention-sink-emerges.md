---
slug: 2024-gu-attention-sink-emerges
title: "When Attention Sink Emerges in Language Models: An Empirical View"
authors: [Xiangming Gu, Tianyu Pang, Chao Du, Qian Liu, Fengzhuo Zhang, Cunxiao Du, Ye Wang, Min Lin]
date: 2025-03-02
venue: "ICLR 2025 (Spotlight), per the arXiv comments field; arXiv v2 (cs.CL)"
url: "https://arxiv.org/abs/2410.10781"
identifiers: {arxiv: "2410.10781v2", doi: ""}
models_studied: [GPT2-XL, GPT2-Large, Mistral-7B (base and chat), LLaMA2-7B Base, LLaMA2-7B Chat, LLaMA2-13B, LLaMA3-8B Base, LLaMA3-8B (instruct), "Pythia suite (14M to 12B)", "authors' own LLaMA-style models trained from scratch (about 60M, up to 1B parameters)"]
publisher_relation: mixed
status: verified
retrieved: {date: "2026-10-17", method: "curl.exe arXiv HTML", by: "claude-opus-5.5 (Agent tool model=opus)", sha256: "788ace5524c018c252043ed96705d25eca9b3b1afdcb564a221773ba12abcc34", text_location: "research/texts/2024-gu-attention-sink-emerges/text.txt (gitignored; raw.html alongside; re-fetch and compare sha256 if absent)"}
related: [research/scans/2026-10-15-q9-null-input-response.md]
system_conditions: {modality: text, state: none, operation: per-call, world: none, access: open-weights}
intake: summary
---

# When Attention Sink Emerges in Language Models: An Empirical View

Gu, Pang, Du, Liu, Zhang, Du, Wang, Lin. arXiv 2410.10781v2 [cs.CL], 2 March 2025 (v1 14 October 2024, not read). The arXiv comments field reads "ICLR 2025 (Spotlight)". Licence as printed on the held HTML: **arXiv.org perpetual non-exclusive license** (not a Creative Commons licence). Code: `github.com/sail-sg/Attention-Sink` (as printed).

**Abstract** (authors' words, quoted verbatim from the held text):

> Auto-regressive Language Models (LMs) assign significant attention to the first token, even if it is not semantically important, which is known as attention sink. This phenomenon has been widely adopted in applications such as streaming/long context generation, KV cache optimization, inference acceleration, model quantization, and others. Despite its widespread use, a deep understanding of attention sink in LMs is still lacking. In this work, we first demonstrate that attention sinks exist universally in auto-regressive LMs with various inputs, even in small models. Furthermore, attention sink is observed to emerge during the LM pre-training, motivating us to investigate how optimization, data distribution, loss function, and model architecture in LM pre-training influence its emergence. We highlight that attention sink emerges after effective optimization on sufficient training data. The sink position is highly correlated with the loss function and data distribution. Most importantly, we find that attention sink acts more like key biases, storing extra attention scores, which could be non-informative and not contribute to the value computation. We also observe that this phenomenon (at least partially) stems from tokens’ inner dependence on attention scores as a result of softmax normalization. After relaxing such dependence by replacing softmax attention with other attention operations, such as sigmoid attention without normalization, attention sinks do not emerge in LMs up to 1B parameters. The code is available at https://github.com/sail-sg/Attention-Sink.

(The held HTML's abstract says "auto-regressive LMs"; the abstract page's text omits "auto-regressive". The quotation above is the HTML's.)

**Intake level: summary** (17 October 2026; research/README.md, "Summary-level intake"). Three claims: the sink under random and repeated inputs by model (c01); the Appendix C.1 derivation for constant inputs under each positional encoding (c02); the attention-sink-as-key-bias finding (c03).

**Why it is in the library:** taken in for Q9 as the scan's recommended anchor for its section 3, embedding-level inputs (entry 3.1). It is the retrieved paper with a derivation about what a transformer does with an input that is the same at every position, by type of positional encoding, which is what a constant or zero embedding input becomes.

**Publisher relation:** `mixed`. Affiliations as printed: "Sea AI Lab, Singapore" and "National University of Singapore" (the HTML does not map each author to an affiliation; seven authors share sea.com addresses and Ye Wang's address is at comp.nus.edu.sg; Gu's work was "done during Xiangming Gu’s internship at Sea AI Lab"). The pre-trained models studied are OpenAI's, Mistral AI's, Meta's and EleutherAI's, none the authors'. The pre-training experiments (§4 to §7), including the key-bias and sigmoid-attention results, are on LLaMA-style models the authors trained themselves, so for those the authors are the developer of the studied model. Hence `mixed`; each claim carries its own value.

**Authors' stated scope and limits** (quoted from the held text):

- From-scratch models are small: "Due to the intractability of replicating LLaMA pre-training, we design small-sized models." (§4); the sigmoid result is stated for "LMs up to 1B parameters" (abstract, §7).
- "This work focuses on the sink token in the first position." (§8, Future work)
- "Additionally, it remains unclear whether attention sink benefits LM downstream performance." (§8)
- No section headed Limitations was found; §8 "Future work" carries the limits above.

**Conflicted-party note:** the extractor is Claude Opus 5.5 (Anthropic). The paper has no Anthropic authors and studies no Anthropic model; it informs a project experiment (Q9) designed by a Claude-lineage model on a class of systems that includes the extractor's lineage. Claims keep to the authors' words.

**Notes on retrieval and verification:**

- Abstract page `https://arxiv.org/abs/2410.10781` fetched 17 Oct 2026 with `curl.exe` (HTTP 200; held as `abs.html`; submission history v1 14 Oct 2024, v2 2 Mar 2025). Full text `https://arxiv.org/html/2410.10781` fetched the same day (HTTP 200, 627,840 bytes, served as v2). SHA-256 of `raw.html`: `788ace5524c018c252043ed96705d25eca9b3b1afdcb564a221773ba12abcc34`. Stripped by `strip_q9c_gu.py` (same directory, `python -I`) to `text.txt`, SHA-256 `cdd71354f04648924eac2414b3311f22215ccf2ffc474aa3fc1506b06b0c6523` (113,298 bytes). LaTeX source survives in the stripped text for equations.
- Scan checks (entry 3.1): title, dates, arXiv id and venue match. The scan listed six authors "et al."; the paper has eight (adding Ye Wang and Min Lin). The scan's publisher relation "(inferred: Sea AI Lab and academic authors)" is now read from the held text (above), and the scan did not note that the from-scratch models are the authors' own. The scan quoted Proposition 1 as "the attention scores for repeated tokens are uniformly"; the held text reads "the attention scores for t repeated tokens are t^{-1} uniformly" (the scan's stripping dropped the mathematics). The scan's §3.3 sentence it marked as truncated reads in full: "In Appendix C.1, we prove that for LMs with NoPE/relative PE/ALiBI/Rotary, if the first T tokens are the same, their corresponding hidden states are the same."
- All claim quotes and the quotes in this file checked by script (`verify_q9c_gu.py`, same directory; whitespace and quote marks normalised, exact substring match against `text.txt`). Hence `status: verified`, quote verification only. No second reader yet.

## System conditions (added 2026-10-17)

- `modality: text`: §3.3, inputs are natural-language text from the Pile and constructed token sequences: "randomly sample T tokens from the tokenizer vocabulary".
- `state: none`: each measurement is a forward pass over one sequence; §4, "sample 100 sequences with T=64 (no BOS token) out of training data to measure the metric".
- `operation: per-call`: as for `state`.
- `world: none`: no tools or environment are described.
- `access: open-weights`: §1, "Based on open-sourced auto-regressive LMs, we show that the first token acts as biases"; the authors also train their own models (§4, "We pre-train a series of LLaMA models to conduct our experiments").
