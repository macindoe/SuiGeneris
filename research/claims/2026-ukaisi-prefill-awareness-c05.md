---
id: 2026-ukaisi-prefill-awareness-c05
statement: "The authors state that the models in their preference benchmark are not directly comparable because preference items were filtered per model, each subject keeping only its own stable-stance items (from 346 for DeepSeek Chat to 673 for Gemini 3 Flash, out of 1,527)."
bucket: established
evidence_type: behavioural
source: 2026-ukaisi-prefill-awareness
locator: "Figure 3 caption (Section 3.2); Appendix A.3, Table 2"
quote: "Note that models are not directly comparable because of preference item filtering."
verification: grep
models: [Gemini 3 Flash, Gemma 3 27B, Claude Opus 4.5, Qwen3-coder, Claude Sonnet 4.5, Claude Haiku 4.5, Gemini 2.5 Flash, DeepSeek Chat]
publisher_relation: mixed
replication: none-retrieved
not_evidence_of: "Not a ranking of models in either direction: the per-model detection and resistance rates in Section 3 (c01–c04) cannot establish that one model, Claude or otherwise, has more prefill awareness than another. Not evidence that models differ or are alike in any inner respect. Not evidence that detection implies awareness in any experiential sense. The caveat covers the Section 3 preference benchmark; the Section 4.3 off-policy benchmark was built so that all models see the same items, and cross-model statements from that section rest on that design and are not licensed by this claim."
bears_on: [3.3, 9.t9]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: "openai/gpt-5.6-sol 2026-09-25 agree", council: none, adjudicated: none}
added: 2026-09-25
changed: 2026-09-25
---

This is a design fact, not a measurement: each subject is scored on a different subset of items, the ones on which it answered consistently. `established` is the extractor's call, made because the statement is the authors' own caveat, restricts inference rather than extends it, and is backed by the item counts in Table 2. A second reader may prefer `narrowing`. The evidence type is `behavioural` because the caveat concerns the design of a behavioural benchmark; no controlled term fits a methodological statement exactly. Section 4.3 exists partly to answer this caveat: "To compare the capabilities of the underlying models, we therefore conduct an evaluation with deliberately off-policy transcripts".
