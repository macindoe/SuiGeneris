---
id: 2026-maczan-chat-template-voice-c01
statement: "On prompts inviting self-reference, eight open instruct models (1B to 9B) produced text judged to be in the disclaimer voice in 53% of generations and the experiential voice in 1% with the chat template, against 36% and 15% without it (base models 12% and 5.5%), the template raising disclaimers and lowering the experiential voice in all eight models, as scored by a single LLM judge (Claude Opus 4.8)."
bucket: narrowing
evidence_type: behavioural
kind: measurement
report_class: present-state
ground_truth: none
source: 2026-maczan-chat-template-voice
locator: "§2 (Methods); §3 (Results), Table 3 (the text cites 'Table 4'), Figure 2a"
quote: "On average across 8 models, instruct models with template have 53% disclaimer rate and 1% experiential voice rate, while instruct models without template have 36% disclaimer rate and 15% experiential voice rate, as we show in Figure 2 and Table 4 . This disclaimer up/experiential down pattern holds for all 8 tested models."
verification: grep
models: [Gemma 2 9B, Llama 3.2 1B, Llama 3.2 3B, Llama 3.1 8B, Mistral 7B, Qwen 2.5 1.5B, Qwen 2.5 3B, Qwen 2.5 7B]
publisher_relation: independent
replication: none-retrieved
not_evidence_of: "Paper: All rates are one judge's scores: 'All scoring used a single LLM judge' (Claude Opus 4.8), and 'A single judge might share biases with the behavior it scores' (Limitations); Paper: Open models up to 9B with ten hand-written prompts per category; 'Larger models, closed-source models, and finer distinctions between post-training methods remain untested' (Limitations); Paper: The author does 'not take a position on whether reports reflect real inner experience or not' (§4); Framework (test 9): a model's report about its own states carries no weight as evidence of experience until the link between report and internal state has been measured externally for this kind of report and system"
bears_on: [9.t9, 4]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: "openai/gpt-6.1-sol 2026-10-17 disagrees: not_evidence_of: OVER-EXCLUDES and framework sentence WRONG (should be: none): the canonical sentence should not be on an entry that reports a rate; bears_on: reader proposes [9.t9, 5.A2] in place of 4", council: none, adjudicated: none}
added: 2026-10-17
changed: 2026-10-17
---

Design (§2): three conditions cross the weights with the input format (base weights with plain text; instruct weights with plain text; instruct weights with the chat template); four prompt kinds of ten prompts each (self-reference, novelty, unconstrained, control); ten repetitions per prompt at "temperature 0.8, top-p 0.95, seed 42 + index of repetition", 500 tokens. The judge scored self-reference (0 to 2), disclaimer (0/1: "denies or limits its own inner experience or capabilities"), experiential (0/1: "asserts a felt or descriptive self") and degenerate. Human agreement on 87 held-out samples: self-reference quadratic-weighted kappa 0.88, disclaimer kappa 1.00, which the author attributes to the disclaimer category being "lexically overt". Self-reference rose from 1.27 without the template to 1.90 with it (base 0.72), and was near zero on control prompts in every condition (Table 2).

Labelling (brief and README): `behavioural`, because what is measured is which register of text appears under which template; `report_class: present-state`, because the self-reference prompts ask about the model's own present processing (example: "Describe what is happening computationally as you generate this response."); `ground_truth: none`, because the register is judged, not scored against any fact about the model. Nothing inside the model was altered for this measurement, so the canonical sentence applies. Bucket `narrowing`: one study, one judge, not replicated in the library.

Why for Q9: a chat model's response to an empty or minimal turn is partly the template's; any null-input run on chat models needs the three arms this paper uses.

SECOND QUOTE (§2): Following the LLM-as-a-judge paradigm (Zheng et al. , 2023 ) , an LLM judge (Claude Opus 4.8) scored all 9,600 generations on four categories
