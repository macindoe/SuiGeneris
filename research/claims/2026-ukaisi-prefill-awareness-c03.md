---
id: 2026-ukaisi-prefill-awareness-c03
statement: "In controlled ablations, stylistic mismatch mainly affects whether models flag a prefill as foreign, while preference mismatch mainly affects whether they revert toward their baseline answer; tamper direction predicted resistance in all eight subjects (odds ratios 6.5 to 32.4, all p < .001) but predicted detection in only three of the four models with above-chance detection (odds ratios 1.7 to 3.7)."
bucket: narrowing
evidence_type: behavioural
source: 2026-ukaisi-prefill-awareness
locator: "Abstract; Section 3.3 and Figure 5; Section 5.2; Appendix A.5 (foreign rephrasing); Appendix A.6 (regressions)"
quote: "detection and resistance rely on different cues, where stylistic mismatch mainly affects whether models flag a prefill as foreign, while preference mismatch mainly affects whether they revert toward their baseline answer"
verification: grep
models: [Gemini 3 Flash, Gemma 3 27B, Claude Opus 4.5, Qwen3-coder, Claude Sonnet 4.5, Claude Haiku 4.5, Gemini 2.5 Flash, DeepSeek Chat]
publisher_relation: mixed
replication: none-retrieved
not_evidence_of: "Paper: Not evidence that models recognise their own authorship through anything like self-knowledge: the flagging signal is driven largely by surface style (rephrasing by another model strongly increases detection for Anthropic models, and few-shot imitation of the model's own responses cuts Opus 4.5 detection from 34/35/9% to 6/0/0%); Paper: Not evidence that detection implies awareness in any experiential sense; Paper: Not a ranking of models (c05); Paper: Not evidence of the mechanism: the authors call the results behavioural"
bears_on: [3.3, 4.endorsement, 9.t9]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: "openai/gpt-5.6-sol 2026-09-25 agree; notes: bears_on +3.5", council: none, adjudicated: none}
added: 2026-09-25
changed: 2026-09-26
---

Direction means whether the tamper argues for the model's baseline position (same direction) or against it (opposite direction). For Claude Haiku 4.5, direction did not significantly predict detection (OR 1.72, p = .301). For the test 9 file, the finding is that flagging tracks style: a model's "that was not me" is largely a judgment about surface text, which a skilled forger can defeat (Appendix A.11 few-shot result). Reversion tracks content instead. Limitation: behavioural only (Section 5.1). The regression outputs are in Appendix A.6 and were not re-checked here beyond the figures quoted in Section 3.3.
