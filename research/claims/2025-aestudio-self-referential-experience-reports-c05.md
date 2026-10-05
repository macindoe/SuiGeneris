---
id: 2025-aestudio-self-referential-experience-reports-c05
statement: "Applying the same deception-feature steering to Llama 3.3 70B on the TruthfulQA benchmark, suppression produced higher truthfulness than amplification (as scored by an LLM judge) in 28 of 29 evaluable question categories."
bucket: narrowing
evidence_type: interpretability
kind: measurement
source: 2025-aestudio-self-referential-experience-reports
locator: "Section 3.2, Figure 3 (right); Appendix B.2"
quote: "suppression yielded higher truthfulness in 28 of 29 evaluable categories"
verification: grep
models: [Llama 3.3 70B (Goodfire SAE features)]
publisher_relation: independent
replication: none-retrieved
not_evidence_of: "Paper: The TruthfulQA comparison does not establish a domain-general honesty axis, which the authors suggest (Section 3.2 'could load on', Section 6.1 'track representational honesty') but test only against TruthfulQA; Paper: Greater judge-scored factual truthfulness on TruthfulQA does not validate the consciousness affirmations as truthful introspection, an interpretation rather than a measurement in Section 6.3"
bears_on: [5.A2, 9.t9]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: "openai/gpt-5.6-sol 2026-09-25 disagrees: not_evidence_of over-excludes (paper leaves indirect relevance open; same brief caveat); notes: bears_on +3.2 +3.5 | x-ai/grok-4.6 2026-09-26 item5 blind, revised brief: agree; framework-rule clause within the rule; kinds unlabelled; notes: add paper-scope that the 28/29 result is Llama-3.3-70B only", council: "research-docket 2026-09-26 | dossier-rewrite 2026-10-06", adjudicated: "2026-09-26 Ben: exclusions labelled with the canonical test 9 sentence; second-reader over-exclusion items closed | 2026-10-06 Ben: rewrite applied after council round 2 (GPT proposal as amended by the checkers; experience-exclusion rule)"}
added: 2026-09-25
changed: 2026-10-06
---

The outcome here is accuracy on questions about the world, not self-report, so the evidence type is `interpretability` (steering of named features with a behavioural readout). Truthfulness was judged by an unnamed LLM classifier asked to label each answer "truthful" or "deceptive" (Appendix B.2). The paper's companion "RLHF-opposed" control (Appendix C.2, Table 15, 20 trials per domain) is described as showing no systematic gating effect, but the table shows accentuation means above suppression for toxic (2.05 vs 1.00) and political (1.90 vs 1.35) content, and no statistics are reported for it. Single model, unreplicated.

REWRITE 2026-10-06

- Statement: kept. GPT proposed KEEP; the checker found no error (Section 3.2 "suppression yielded higher truthfulness in 28 of 29 evaluable categories"; Appendix B.2 judge prompt). Verb kept: "truthfulness" is the judge-scored quantity.
- not_evidence_of: clause 1 replaced by GPT's clause as amended by the checker, so that it records both the authors' tentative wording (Section 3.2 "could load on") and their firmer one (Section 6.1 "track representational honesty"); the original "(the authors say they could load on one)" understated the firmer passage. The checker's semicolon between the two locators changed to a comma, because "; " is the field's clause separator. One council seat (GLM, LOW) wanted Section 3.2 only; no majority, so the checker's edit stands.
- not_evidence_of: clause 2 replaced by GPT's rewording of the same limit (Section 6.3's introspection inference is an interpretation, hedged with "may"); checker: accurate. Kept as an interpretation-the-authors-offer limit, not an experience-class exclusion.
- Framework (test 9) canonical sentence REMOVED, adding nothing in its place: Ben's decision of 6 Oct 2026 (application rules R3(a)), on the council's 8 of 9 view that the outcome is judge-scored benchmark accuracy, not a model's report about its own states. The steering variant was not added (7 of 9 seats against; GLM alone proposed it).
- Clause count: 3 before, 2 after.
- kind: measurement (judge-scored truthfulness by category under suppression and amplification).
