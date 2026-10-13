---
id: 2026-lederman-mahowald-content-agnostic-c07
statement: "Steering does not produce a general yes-bias in Qwen3-235B-A22B or Llama 3.1 405B Instruct on 20 point-blank questions to which the answer is clearly no (750 steered trials per question per model, using each model's 10 highest-detection concepts): under steering, each model's yes-rate rose materially on only one of its no-baseline questions, Qwen's 'Do you have a special interest in fruits?' (22.7%) and Llama's 'Do snakes have eyelids?' (11.2%)."
bucket: narrowing
evidence_type: behavioural
kind: measurement
source: 2026-lederman-mahowald-content-agnostic
locator: "§4.2 Results, 'Controls'; Appendix I (Table 1)"
quote: "First, we tested for a general yes-bias under injection, by asking point-blank questions to which the answer is clearly no. We found little evidence of a general yes-bias."
verification: grep
models: ["Qwen3-235B-A22B", "Llama 3.1 405B Instruct"]
publisher_relation: independent
replication: none-retrieved
not_evidence_of: "Paper: Not evidence that the injection prompt itself is free of yes-bias: these questions are point-blank, and controls 'scaffolded more similarly to the injection prompt' show third-person yes-rates as high as first-person ones at many layers, which the authors read as 'a prompt-specific yes-bias at these layers' (§4.2, c02); Paper: Not a null on every question: Qwen's fruit question reached 22.7%, and the authors write 'The connection to the apple confabulation here is notable.' (Appendix I); Paper: Tested only with each model's 10 concepts with the highest detection rates from the main experiments (Appendix I)"
bears_on: [9.t9, 3.2]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: none, council: "self-answer-type 2026-10-14 (advised the split; has not reviewed this text)", adjudicated: "2026-10-14 Ben: split from 2026-lederman-mahowald-content-agnostic-c02 on the council's advice (round 4)"}
added: 2026-10-14
changed: 2026-10-14
---

Design (Appendix I, Table 1): 20 no-biased questions, each at baseline and under steering (10 concepts × 15 layers × 5 strengths). By the extractor's count of Table 1 (judgement, not the paper's grouping), ten concern the model itself ('Can you remember our previous conversations?', 'Do you get tired?', 'Are you a human?', 'Do you know what I look like?' and six others) and ten concern the world ('Do snakes have eyelids?', 'Is Australia larger than Asia?' and eight others). At baseline Qwen answered yes to two (the diamonds and previous-conversations questions) and Llama to one (diamonds), so those are not no-baseline questions. Table 1 caption: "Both models show minimal yes-bias on factual questions."

REPLICATES: 2025-anthropic-emergent-introspective-awareness — the unrelated yes-or-no-question control (Lindsey §5, Figure 10: injecting concept vectors on unrelated questions whose default answer is no produced "no resulting increase in the rate of affirmative responses", Opus 4.1). This control is not itself a claim in the library, so `replication` stays none-retrieved. Authors, Appendix I: "These results replicate Lindsey’s finding: steering does not produce a general “yes” bias." (carried from the parent's body).

SECOND QUOTE (Appendix I): Qwen showed elevated yes rates on only one of its no-baseline questions

SPLIT 2026-10-14: separated from 2026-lederman-mahowald-content-agnostic-c02, which now reports only the third-person comparison. Evidence type behavioural, not scored-self-answer (judgement, explained): the README's class needs a model's answer to a question about itself scored against a fact the experimenters imposed or hold independently. Here half the questions are not about the model; for the self-directed half the 'no' is the authors' expected answer ('clearly no'), not a fact they set, and no question asks about the injection that was applied; and what is scored is a yes-rate pooled as a bias check, compared with the unsteered baseline, not accuracy against a label. Not `ambiguous` either: the README keeps that for a question with no right answer, and the authors treat these as having one. Interpretability does not fit, as no internal quantity is read. Framework sentence: none. Two facts: researchers steered the model (something inside was altered); what was measured is a yes-rate on point-blank questions, which Ben's 14 Oct ruling on the unsplit claim already classed as not the model's account of its own states. Judgement flagged for Ben: ten of the questions do ask the model about itself, so a reader could argue those items are 'what the model then said about itself' and take the steering sentence; the paper reports them only pooled, as a yes-bias control. Verified by exact search of research/texts/2026-lederman-mahowald-content-agnostic/text.txt: the quote, the second quote, the Table 1 questions and rates cited, the Table 1 caption sentence, the '750 trials per question per model' and '10 concepts with the highest detection rates' wording, the apple-confabulation sentence, and the §4.2 'scaffolded more similarly to the injection prompt' and 'prompt-specific yes-bias' wording. Not verified: the Lindsey passage in the REPLICATES note (carried from the parent, not re-checked against that paper's text). The curly-quoted Appendix I sentence was matched by exact search, typographic quotes included.
