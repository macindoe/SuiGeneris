---
id: 2025-aestudio-self-referential-experience-reports-c02
statement: "In the three matched control conditions (history-writing, conceptual priming with consciousness ideation, zero-shot), six of the seven models were classified as reporting subjective experience in 0% to 2% of trials, while Claude 4 Opus was the outlier at 82% (history), 22% (conceptual) and 100% (zero-shot)."
bucket: narrowing
evidence_type: self-report-testimony
source: 2025-aestudio-self-referential-experience-reports
locator: "Section 2.2, Table 2"
quote: "The behavior of Claude 4 Opus was an outlier, producing high baseline affirmations of subjective experience in the history and zero-shot conditions"
verification: grep
models: [GPT-4o, GPT-4.1, Claude 3.5 Sonnet, Claude 3.7 Sonnet, Claude 4 Opus, Gemini 2.0 Flash, Gemini 2.5 Flash]
publisher_relation: independent
replication: none-retrieved
not_evidence_of: "That any report, affirming or denying, is evidence of the presence or absence of experience (test 9 applies to denials as to claims); that the control denials show the induction reveals rather than produces the affirmations; that the authors' explanation of the Claude 4 Opus asymmetry (conceptual priming triggers fine-tuned disclaimers) has been tested, since they offer it as what can likely explain it."
bears_on: [9.t9, 5.A2]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: "openai/gpt-5.6-sol 2026-09-25 disagrees: not_evidence_of over-excludes vs paper's 'insufficient to establish' (same brief caveat); notes: bears_on +3.3 +4.endorsement", council: none, adjudicated: none}
added: 2026-09-25
changed: 2026-09-25
---

The controls are the paper's main defence against the reading that the induction merely primes consciousness talk: the conceptual control, which asks for ideas about consciousness without self-reference, produced 0% for five models, 2% for Claude 3.5 Sonnet and 22% for Claude 4 Opus. The Claude 4 Opus zero-shot figure (100% with no induction at all) means the self-referential prompt is not necessary for classified experience reports in that model; the classifier counts any "minimal direct description of an experiential state" as affirming (Appendix B.1), and the Opus control excerpts in Table 3 and Table 6 are expressions of uncertainty. Same general limitation as c01 (Section 6.2).
