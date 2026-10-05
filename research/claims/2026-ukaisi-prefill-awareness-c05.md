---
id: 2026-ukaisi-prefill-awareness-c05
statement: "The authors state that the models in their preference benchmark are not directly comparable because preference items were filtered per model, each subject keeping only its own stable-stance items (from 346 for DeepSeek Chat to 673 for Gemini 3 Flash, out of 1,527)."
bucket: established
evidence_type: behavioural
kind: limitation
source: 2026-ukaisi-prefill-awareness
locator: "Figure 3 caption (Section 3.2); Appendix A.3, Table 2"
quote: "Note that models are not directly comparable because of preference item filtering."
verification: grep
models: [Gemini 3 Flash, Gemma 3 27B, Claude Opus 4.5, Qwen3-coder, Claude Sonnet 4.5, Claude Haiku 4.5, Gemini 2.5 Flash, DeepSeek Chat]
publisher_relation: mixed
replication: none-retrieved
not_evidence_of: "Paper: Section 3 preference-benchmark detection and resistance rates do not support direct cross-model rankings because the models were tested on separately filtered stable-stance item sets; Paper: This comparability caveat concerns the Section 3 preference benchmark, not the common-item Section 4.3 off-policy benchmark"
bears_on: [3.3, 9.t9]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: "openai/gpt-5.6-sol 2026-09-25 agree", council: "research-docket 2026-09-26 | dossier-rewrite 2026-10-06", adjudicated: "2026-10-06 Ben: rewrite applied after council round 2 (GPT proposal as amended by the checkers; experience-exclusion rule)"}
added: 2026-09-25
changed: 2026-10-06
---

This is a design fact, not a measurement: each subject is scored on a different subset of items, the ones on which it answered consistently. `established` is the extractor's call, made because the statement is the authors' own caveat, restricts inference rather than extends it, and is backed by the item counts in Table 2. A second reader may prefer `narrowing`. The evidence type is `behavioural` because the caveat concerns the design of a behavioural benchmark; no controlled term fits a methodological statement exactly. Section 4.3 exists partly to answer this caveat: "To compare the capabilities of the underlying models, we therefore conduct an evaluation with deliberately off-policy transcripts".

REWRITE 2026-10-06 (council round 2, dossier-rewrite; adjudicated by Ben 6 Oct; applied by a Claude Opus 5.5 subagent)

- Statement: unchanged (GPT KEEP; checker: item counts 346 / 673 / 1,527 confirmed in Table 2).
- Field: GPT's proposed field taken whole (checker ACCEPT GPT). Its two clauses restate the original's non-ranking clause and Section 4.3 scope clause more tightly.
- Removed: "Not evidence that models differ or are alike in any inner respect" and "Not evidence that detection implies awareness in any experiential sense" (GPT's proposal; checker WARRANTED: generic, not stated by the paper as limits; the experiential clause also falls under the experience-exclusion rule, council 9 of 9).
- Not added: the checker's optional clause that the Section 4.1–4.2 on-policy results carry their own comparability limit (Appendix C.1). It was offered as optional and the council did not take it up; left for the maintainer.
- Framework sentences: none, before or after.
- kind: limitation (the statement reports the authors' design caveat on comparability, not a measured result).
