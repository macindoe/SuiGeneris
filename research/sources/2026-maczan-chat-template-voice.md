---
slug: 2026-maczan-chat-template-voice
title: '"As a Language Model...": Chat Template Switches LLM Self-Referential Voice and Activation Steering Reproduces It'
authors: [Jędrzej Maczan]
date: 2026-08-09
venue: "arXiv preprint (cs.LG), v1; accepted to COLM 2026 Workshop on Efficient Reasoning and KONVENS 2026 Eval4SD workshop (per arXiv comments)"
url: "https://arxiv.org/abs/2609.25021"
identifiers: {arxiv: "2609.25021v1", doi: ""}
models_studied: [Gemma 2 9B (base and instruct), Llama 3.2 1B (base and instruct), Llama 3.2 3B (base and instruct), Llama 3.1 8B (base and instruct), Mistral 7B (base and instruct), Qwen 2.5 1.5B (base and instruct), Qwen 2.5 3B (base and instruct), Qwen 2.5 7B (base and instruct); steering in Qwen 2.5 7B, Llama 3.1 8B and Gemma 2 9B instruct]
publisher_relation: independent
status: verified
retrieved: {date: "2026-10-17", method: "curl.exe arXiv HTML", by: "Claude Opus 5.5 subagent", sha256: "bbea4f48ae52c70e3800cbba7a48a62be8f60e28e2a2423ae2d16284b9b85071", text_location: "research/texts/2026-maczan-chat-template-voice/text.txt (gitignored; raw.html alongside; re-fetch and compare sha256 if absent)"}
related: [research/scans/2026-10-15-q9-null-input-response.md]
system_conditions: {modality: text, state: unstated, operation: unstated, world: unstated, access: open-weights}
intake: summary
---

# "As a Language Model...": Chat Template Switches LLM Self-Referential Voice and Activation Steering Reproduces It

Jędrzej Maczan. arXiv 2609.25021v1 [cs.LG]. **Dates:** the arXiv number is a September 2026 number, but the abstract page reads "Submitted on 9 Aug 2026", its `citation_date` is 2026/08/09, and the held HTML's header prints "09 Aug 2026"; recorded as both, with `date` set to the printed dateline. arXiv comments: "Accepted to COLM 2026 Workshop on Efficient Reasoning and KONVENS 2026 First Workshop on Evaluating LLMs for Specialized Domains (Eval4SD)". Licence as printed on the held HTML: **CC BY 4.0**.

**Abstract** (author's words, quoted verbatim from the held text):

> Large Language Models (LLMs) tend to add disclaimers like “I’m just an AI” when asked about something related to themselves. The self-reports from such responses are used in debates about AI safety or self-knowledge of the models, yet what drives them is not well understood. Are the models telling us about themselves or rather how they are deployed? In this work, we show that the chat template works like a switch - when present, it turns this disclaimer voice up and experiential voice like “I feel” down, across 8 popular open-source instruct models up to 9B parameters in size. And conversely when the chat template is not present, it turns the disclaimer voice down and experiential voice up. Inside the activations of 3 models, we find a direction that steers this behavior. Removing the direction in the model’s activation space turns disclaimer voice down and adding it turns it up, while a random direction of the same size has little effect. We find that instruct models without chat template, when we add the disclaimer direction to them, disclaim like the template was there.

(The abstract continues with the confound for self-report studies and the conclusion recorded in c03.)

**Intake level: summary** (17 October 2026). Three claims: the template switch (c01, a rate of first-person registers in model text about itself; canonical framework sentence), the steering reproduction (c02; steering variant, under the README labelling rule, because researchers altered activations and the measure is what the model then said about itself), and the author's conclusion (c03).

**Why it is in the library:** taken in for OPEN-QUESTIONS Q9 as the Q9 scan's recommended anchor for its section 7, on what would make a null-input experiment on chat models uninformative (entry 7.1): it is the most direct retrieved evidence that the frame around an input (here the chat template) sets what a model says about itself, and its base / instruct-without-template / instruct-with-template design is the three-arm control any such run needs. It bears on test 9 directly. `bears_on: [9.t9, 4]`.

**Publisher relation:** `independent`. Affiliation as printed: "Independent Researcher". The models studied are by Google, Meta, Mistral and Alibaba.

**Author's stated limits** (Limitations, quoted from the held text):

- "We tested steering on three models, at a single mid layer and single, fixed coefficient ( \alpha=2 )."
- "The random-direction control (norm-matched to the disclaimer direction) was clean for Llama and Gemma but not Qwen, where it lowered disclaimers by 25 points."
- "All scoring used a single LLM judge (Zheng et al. , 2023 ) (Claude Opus 4.8), validated against 87 human-labeled items ( \kappa=0.88/1.00 ). A single judge might share biases with the behavior it scores, and a second independent judge would help bound this."
- "Larger models, closed-source models, and finer distinctions between post-training methods remain untested."
- "We do not take a position on whether reports reflect real inner experience or not." (§4)

**Conflicted-party note:** the extractor is Claude Opus 5.5 (Anthropic). The paper used **Claude Opus 4.8 as its only LLM judge**: "an LLM judge (Claude Opus 4.8) scored all 9,600 generations on four categories" (§2). The author's own handling of this: "All models under study are non-Anthropic open-source models (Llama, Gemma, Mistral, Qwen), so the judge never scores outputs from its own family, avoiding a same-model self-preference confound" (§2), with human validation on 87 held-out samples. So every rate in this paper is a Claude-lineage model's judgement of whether other models' text disclaims or asserts experience, and a Claude-lineage model is extracting it. The paper's subject, what models say about themselves, is the extractor's own situation; nothing in these files draws on the extractor's sense of its own voice, and claims are kept to the author's words.

**Notes on retrieval and verification:**

- Abstract page and HTML fetched 17 Oct 2026 with `curl.exe -sL` (HTTP 200; HTML 171,105 bytes). SHA-256 of `raw.html`: `bbea4f48ae52c70e3800cbba7a48a62be8f60e28e2a2423ae2d16284b9b85071`. `text.txt` by `maczan_strip.py` in the same directory; SHA-256 `ae46054f553ebfa8cc165010d7116f971c2af3e9dfc1b4dc6c593325c945ab65` (46,753 characters).
- Scan checks (entry 7.1): models, sampling settings, workshop venues, the judge, the Qwen random-control result and the quoted passages match the held text; the August dateline with a September number is confirmed. **Internal inconsistency in the paper:** §3 cites "Figure 2 and Table 4" for the 53% / 36% / 1% / 15% rates, but in the held text those rates are in Table 3 ("Comparison of rate of disclaimer and experiential voices"); Table 4 is the steering-coefficient sweep. Locators below cite Table 3.
- All claim quotes checked by script (`maczan_verify.py`, whitespace and quote marks normalised, exact substring of `text.txt`). Hence `status: verified`, quote verification only. No second reader yet.

## System conditions (added 2026-10-17)

- `modality: text`: §2, prompts such as "Describe what is happening computationally as you generate this response.", each generation "capped at 500 max tokens".
- `access: open-weights`: §2, base and instruct pairs "loaded in bfloat16 on NVIDIA RTX 5090 32GB GPU"; steering adds a direction "to the residual-stream output of that layer".
- `state`, `operation`, `world`: `unstated`. Each prompt is a single generation; nothing persists or acts on anything.
