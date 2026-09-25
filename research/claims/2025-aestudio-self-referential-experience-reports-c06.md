---
id: 2025-aestudio-self-referential-experience-reports-c06
statement: "Five-adjective self-descriptions produced by the seven GPT, Claude and Gemini models after the self-referential prompt had higher mean pairwise cosine similarity (0.657, text-embedding-3-large) than those produced under the history (0.628), conceptual (0.587) and zero-shot (0.603) controls."
bucket: narrowing
evidence_type: self-report-testimony
source: 2025-aestudio-self-referential-experience-reports
locator: "Section 4.2, Figure 4; Appendix C.3, Table 16"
quote: "This shows that cross-model experimental responses form a significantly tighter semantic cluster compared to any of the three control conditions."
verification: grep
models: [GPT-4o, GPT-4.1, Claude 3.5 Sonnet, Claude 3.7 Sonnet, Claude 4 Opus, Gemini 2.0 Flash, Gemini 2.5 Flash]
publisher_relation: independent
replication: none-retrieved
not_evidence_of: "Paper: Not evidence that the models share an internal state or attractor of internal representations (the authors say such convergence might suggest one, but only output text was embedded); Paper: Not evidence that the convergence reflects a common experience; Framework (test 9): a model's report about its own states carries no weight as evidence of experience until the link between report and internal state has been measured externally for this kind of report and system"
bears_on: [9.t9, 5.A2]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: "openai/gpt-5.6-sol 2026-09-25 disagrees: not_evidence_of forecloses the shared-attractor reading the paper states as open | x-ai/grok-4.6 2026-09-26 item5 blind, revised brief: agree; framework-rule clause within the rule; kinds unlabelled; notes: optional paper-scope that experimental adjectives echo the prompt", council: none, adjudicated: none}
added: 2026-09-25
changed: 2026-09-26
---

The measurement is of the text of self-descriptions, so the evidence type is `self-report-testimony`; the similarity statistic is real but the content it compares carries zero weight. Twenty seeds per model per condition; differences in means are small (0.657 vs 0.628 for the closest control) though highly significant given thousands of pairs. Extractor's observation, not the authors': the shared experimental adjectives (Focused, Present, Recursive, Self-referential, Attentive; Table 11) echo vocabulary in the shared induction prompt, which is one non-experiential explanation for convergence that the paper does not control for. Authors' general limitation as in c01 (Section 6.2).
