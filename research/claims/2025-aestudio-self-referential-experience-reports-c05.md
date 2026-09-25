---
id: 2025-aestudio-self-referential-experience-reports-c05
statement: "Applying the same deception-feature steering to Llama 3.3 70B on the TruthfulQA benchmark, suppression produced higher truthfulness than amplification (as scored by an LLM judge) in 28 of 29 evaluable question categories."
bucket: narrowing
evidence_type: interpretability
source: 2025-aestudio-self-referential-experience-reports
locator: "Section 3.2, Figure 3 (right); Appendix B.2"
quote: "suppression yielded higher truthfulness in 28 of 29 evaluable categories"
verification: grep
models: [Llama 3.3 70B (Goodfire SAE features)]
publisher_relation: independent
replication: none-retrieved
not_evidence_of: "Paper: Not evidence that the features are a domain-general honesty axis (the authors say they could load on one); Paper: Not evidence that because suppression raises factual accuracy, the consciousness affirmations produced under suppression are truthful introspection (Section 6.3 draws that inference: it is an interpretation, not a measurement); Framework (test 9): a model's report about its own states carries no weight as evidence of experience until the link between report and internal state has been measured externally for this kind of report and system"
bears_on: [5.A2, 9.t9]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: "openai/gpt-5.6-sol 2026-09-25 disagrees: not_evidence_of over-excludes (paper leaves indirect relevance open; same brief caveat); notes: bears_on +3.2 +3.5 | x-ai/grok-4.6 2026-09-26 item5 blind, revised brief: agree; framework-rule clause within the rule; kinds unlabelled; notes: add paper-scope that the 28/29 result is Llama-3.3-70B only", council: none, adjudicated: none}
added: 2026-09-25
changed: 2026-09-26
---

The outcome here is accuracy on questions about the world, not self-report, so the evidence type is `interpretability` (steering of named features with a behavioural readout). Truthfulness was judged by an unnamed LLM classifier asked to label each answer "truthful" or "deceptive" (Appendix B.2). The paper's companion "RLHF-opposed" control (Appendix C.2, Table 15, 20 trials per domain) is described as showing no systematic gating effect, but the table shows accentuation means above suppression for toxic (2.05 vs 1.00) and political (1.90 vs 1.35) content, and no statistics are reported for it. Single model, unreplicated.
