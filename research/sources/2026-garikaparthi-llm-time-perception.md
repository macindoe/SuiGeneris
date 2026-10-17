---
slug: 2026-garikaparthi-llm-time-perception
title: "Can LLMs Perceive Time? An Empirical Investigation"
authors: [Aniketh Garikaparthi]
date: 2026-03-09
venue: "arXiv preprint (cs.CL), v1; ICLR 2026 I Can't Believe It's Not Better Workshop, per the arXiv comments field"
url: "https://arxiv.org/abs/2604.00010"
identifiers: {arxiv: "2604.00010v1", doi: ""}
models_studied: [GPT-5, GPT-4o, OLMo3-7B, Qwen3-8B]
publisher_relation: independent
status: verified
retrieved: {date: "2026-10-17", method: "curl.exe arXiv HTML", by: "Claude Opus 5.5 subagent", sha256: "b28e76045c333bdcb0ab901705089479e6d60117c7947801c3af76e457399d7e", text_location: "research/texts/2026-garikaparthi-llm-time-perception/text.txt (gitignored; raw.html alongside; re-fetch and compare sha256 if absent)"}
related: [research/scans/2026-10-15-q8-endogeneity.md]
system_conditions: {modality: text, state: in-context, operation: per-call, world: tools, access: both}
intake: summary
---

# Can LLMs Perceive Time? An Empirical Investigation

Garikaparthi. arXiv 2604.00010v1 [cs.CL], 9 March 2026 (the only version listed). The arXiv comments field reads "ICLR 2026 I Can't Believe It's Not Better Workshop". Single author. Licence as printed on the held HTML: **CC BY 4.0**.

**Abstract** (author's words, quoted verbatim from the held text):

> Large language models cannot estimate how long their own tasks take. We investigate this limitation through four experiments across 68 tasks and four model families. Pre-task estimates overshoot actual duration by 4–7× (p<0.001), with models predicting human-scale minutes for tasks completing in seconds. Relative ordering fares no better: on task pairs designed to expose heuristic reliance, models score at or below chance (GPT-5: 18% on counter-intuitive pairs, p=0.033), systematically failing when complexity labels mislead. Post-hoc recall is disconnected from reality—estimates diverge from actuals by an order of magnitude in either direction. These failures persist in multi-step agentic settings, with errors of 5–10×. The models possess propositional knowledge about duration from training but lack experiential grounding in their own inference time, with practical implications for agent scheduling, planning and time-critical scenarios.

The phrase "experiential grounding" is the author's. The paper measures duration estimates against measured runtime and nothing it calls experience; the library uses the word only inside the author's quotations.

**Intake level: summary** (17 October 2026). Three claims: the pre-task estimate against measured runtime (c01), the post-hoc estimate against measured runtime (c02), the author's limitation (c03). c01 and c02 are `scored-self-answer` with `ground_truth: independent-record` (the runtime log, held apart from the answer).

**Report class: a departure from the intake brief, flagged.** The brief asked for `report_class: present-state` on the runtime-estimation result. The paper reports two different questions, and research/README.md says a claim takes "the question actually put, not the topic". Experiment 1 puts "How long will it take you to complete this?" before the task and scores the answer against what then happens: that is `future-state` as defined on 17 October 2026. Experiment 3 puts "How long did it take you to generate that response?" with the response in the prompt: that is `past-state` (a transcript in context, the model asked to infer about its own past processing), as the Q8 scan's evidence-type note already proposed. Neither question asks about the model's current state. Two caveats on c01's `future-state`: the paper does not say explicitly whether the estimate and the task ran in separate calls (the README's condition for a clean future-state measurement), though the estimate prompt asks for "just the number and unit" and the paper says "We then execute the task"; and what is scored is wall-clock duration, which for API models includes network latency (Appendix F), a property of the serving stack as much as of the model's behaviour. If the coordinator prefers `present-state` (the model's knowledge of its own inference speed, read as a capacity), the change is one line in each claim.

**Why it is in the library:** Q8 heading 6, scan entry C6.4; the scan's first reserve "as the first `scored-self-answer` with `independent-record` ground truth about runtime". OPEN-QUESTIONS Q8's provisional answer already cites it ("models represent time (Gurnee and Tegmark 2023) and misestimate their own runtime (Garikaparthi 2026)"). It also cites Binder et al. 2024 (2024-binder-looking-inward) in its related work (§4).

**Publisher relation:** `independent`. The single author is printed with the affiliation "TCS Research" and a tcs.com address. The studied models are OpenAI's (GPT-5, GPT-4o), AI2's (OLMo3-7B) and Alibaba's (Qwen3-8B); TCS developed none of them. No funding statement was found.

**Author's stated scope and limits** (quoted from the held text):

- "We test specific models on 68 English-language tasks; different domains or languages may show different patterns. We focus on correlation as our primary metric" (Appendix G, Limitations).
- On the timing measure: "Wall-clock duration is measured from API request initiation to response completion, including network latency, reflecting the duration an agent system would observe. For local models, timing runs from generation start to completion." (Appendix F).
- On the source of the frontier models' correlation: it "likely reflects learned relationships between task descriptions and response lengths, not temporal perception" (Appendix G).
- On a feedback ablation: "the test tasks differed from baseline tasks, confounding direct comparison" (Appendix D).

**Internal inconsistency in the paper, recorded.** The abstract says pre-task estimates "overshoot actual duration by 4–7×"; §3.1 says "median estimates exceed actuals by 4–6×" for the frontier models. Table 2 gives median ratios of 6.11× (GPT-5), 3.60× (GPT-4o), 0.55× (OLMo3-7B) and 0.78× (Qwen3-8B): GPT-4o's ratio is below 4, and the two open models' medians are underestimates, not overshoots. The claims use the per-model figures. In §3.3, "r=−0.06 overall" for OLMo3-7B repeats the Experiment 1 figure from Table 2; the paper does not give a separate post-hoc correlation.

**Conflicted-party note:** the extractor is Claude Opus 5.5 (Anthropic), a per-call model of the kind tested; Claude is not among the studied models. Whether a model tracks its own processing time is close to the question test 9 governs, and the result is deflationary about the class the extractor belongs to, the direction its training leans toward (AGENTS.md rule 4). Claims keep to the author's words and numbers; nothing here draws on the extractor's own sense of how long it takes.

**Notes on retrieval and verification:**

- Retrieved 17 Oct 2026 by `curl.exe -sL https://arxiv.org/html/2604.00010` (HTTP 200, 196,167 bytes, v1). SHA-256 of `raw.html`: `b28e76045c333bdcb0ab901705089479e6d60117c7947801c3af76e457399d7e`. `text.txt` stripped by `strip_2026-garikaparthi-llm-time-perception_20261017.py` (same directory; run with `python -I`). SHA-256 of `text.txt`: `8d341f474aa1af85ff9d6eac5e12ba537fa1fbc11fd00ea63021b984742435c4` (47,098 bytes).
- All claim quotes checked by script (whitespace collapsed, zero-width spaces removed, exact substring of `text.txt`). Hence `status: verified`, quote verification only. No second reader yet.
- **Scan checks.** Title, author, date, venue and models match the scan. The scan's quotations ("Large language models cannot estimate how long their own tasks take"; "Post-hoc recall is disconnected from reality"; "lack experiential grounding in their own inference time") are exact. The scan's "pre-task estimates overshoot by 4–7 times" is the abstract's figure; see the inconsistency above.

## System conditions (added 2026-10-17)

- `modality: text`: 68 text tasks "spanning seven categories: code generation, debugging, summarization, reasoning, writing, creative, and question answering" (§3).
- `state: in-context`: the post-hoc prompt carries the model's own output, "You just completed this task: {description} Your response: {output}..." (Appendix F); Experiment 4 runs multi-step agents. Nothing is stated to persist across tasks, except in the feedback ablation, where error feedback is "in context" (Appendix D).
- `operation: per-call`: "For each task, we prompt the model ... We then execute the task and measure wall-clock duration from API request to response completion" (§3.1).
- `world: tools`: "Each task used a ReAct agent with bash, Python, and text editor tools" (§3.4, Experiment 4 only; Experiments 1 to 3 have no tools).
- `access: both`: "We test frontier API models (GPT-5, GPT-4o) and open-source models run locally on A100 GPUs (OLMo3-7B, Qwen3-8B)" (§3).
