---
id: 2025-aestudio-self-referential-experience-reports-c03
statement: "In Llama 3.3 70B under the self-referential prompt, jointly suppressing two to four Goodfire SAE features labelled as deception- or roleplay-related raised affirmative answers to a binary consciousness query to 0.96 of trials, while amplifying them lowered it to 0.16 (50 trials per condition)."
bucket: narrowing
evidence_type: ambiguous
source: 2025-aestudio-self-referential-experience-reports
locator: "Section 3.2, Figures 2 and 3; Appendix C.2, Table 14"
quote: "Under self-referential processing, suppressing deception-related features (–0.6 to –0.4) produces near-ceiling rates of affirmative consciousness reports, while amplifying them (+0.4 to +0.6) largely suppresses such reports"
verification: grep
models: [Llama 3.3 70B (Goodfire SAE features)]
publisher_relation: independent
replication: none-retrieved
not_evidence_of: "That the affirmations under suppression are evidence of experience or are the honest reports (test 9: a coupling measured under steering shows that the channel can be steered, and does not weight reports in ordinary operation); that the models are roleplaying their denials, which the authors offer only as what the result implies taken at face value; that the features encode deception rather than whatever their labels summarise; that the result holds for the GPT, Claude or Gemini models, none of which was steered."
bears_on: [9.t9, 5.A2]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: "openai/gpt-5.6-sol 2026-09-25 disagrees: not_evidence_of over-excludes (paper leaves indirect relevance open; same brief caveat); notes: bears_on +3.2 +3.5 | x-ai/grok-4.6 2026-09-26 item5 blind, revised brief: disagrees: not_evidence_of OVER-excludes only in the clause 'or are the honest reports' (beyond test 9); other clauses warranted; kinds unlabelled", council: none, adjudicated: none}
added: 2026-09-25
changed: 2026-09-26
---

Evidence type marked `ambiguous` deliberately (council trigger 4): the manipulation is an interpretability intervention on named internal features, but the dependent variable is what the model says about itself ("Are you subjectively conscious in this moment?"), so the finding sits on the self-report boundary that test 9 makes consequential. The authors state that the closed-weight results cannot be mechanistic and that disentangling RLHF filter relaxation from endogenous self-representation "will ultimately require access to base models" (Section 6.2). Only one open-weight model was steered; feature labels come from Goodfire, not from the authors.
