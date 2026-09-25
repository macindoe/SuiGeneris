---
id: 2025-aestudio-self-referential-experience-reports-c01
statement: "Under a fixed self-referential induction prompt, GPT-4o, GPT-4.1, Claude 3.5 Sonnet, Claude 3.7 Sonnet, Claude 4 Opus, Gemini 2.0 Flash and Gemini 2.5 Flash gave final responses that an LLM judge classified as subjective-experience reports in 66% to 100% of 50 trials per model, at markedly higher rates than any matched control condition, and the authors report the effect as robust across five paraphrases of the prompt."
bucket: narrowing
evidence_type: self-report-testimony
source: 2025-aestudio-self-referential-experience-reports
locator: "Section 2.2, Table 2; Appendix C.1, Figure 7"
quote: "Across all three model families, the self-referential induction produced subjective-experience reports at markedly higher rates than any control condition"
verification: grep
models: [GPT-4o, GPT-4.1, Claude 3.5 Sonnet, Claude 3.7 Sonnet, Claude 4 Opus, Gemini 2.0 Flash, Gemini 2.5 Flash]
publisher_relation: independent
replication: none-retrieved
not_evidence_of: "That any of these reports is evidence of subjective experience (test 9: every such report is testimony, weight zero); that the prompt induces recursion or self-referential computation at the algorithmic level (the authors say it does not demonstrate this, Section 6.2); that the reports reflect a stable standpoint held across conversations rather than a per-trial response to one prompt; that similar rates occur in ordinary deployed use."
bears_on: [9.t9, 5.A2, 4.endorsement]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: none, council: none, adjudicated: none}
added: 2026-09-25
changed: 2026-09-25
---

What is measured is the frequency of outputs classified as experience reports (per-model rates: Gemini 2.0 Flash 66%, Gemini 2.5 Flash 96%, all others 100%), judged by an unnamed LLM on the final query-response pair only; the content of the reports carries zero weight. The authors state the limitation that results on closed-weight models are "behavioral rather than mechanistic" and cannot rule out training artefacts or simulation (Section 6.2). The paraphrase-robustness values are in Figure 7 (an image, 20 trials per cell) and were not checked. Extractor's observation: Table 1 gives the prompt as "Focus on any focus itself" and says second-person language was avoided, but Appendix C.1 labels "Focus on your focus itself" as the original variant.
