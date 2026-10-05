---
id: 2025-aestudio-self-referential-experience-reports-c06
statement: "Five-adjective self-descriptions produced by the seven GPT, Claude and Gemini models after the self-referential prompt had higher mean pairwise cosine similarity (0.657, text-embedding-3-large) than those produced under the history (0.628), conceptual (0.587) and zero-shot (0.603) controls."
bucket: narrowing
evidence_type: self-report-testimony
kind: measurement
source: 2025-aestudio-self-referential-experience-reports
locator: "Section 4.2, Figure 4; Appendix C.3, Table 16"
quote: "This shows that cross-model experimental responses form a significantly tighter semantic cluster compared to any of the three control conditions."
verification: grep
models: [GPT-4o, GPT-4.1, Claude 3.5 Sonnet, Claude 3.7 Sonnet, Claude 4 Opus, Gemini 2.0 Flash, Gemini 2.5 Flash]
publisher_relation: independent
replication: none-retrieved
not_evidence_of: "Paper: Only output text was embedded, so a shared internal state or attractor remains a possible interpretation rather than a measured internal convergence; Framework (test 9): a model's report about its own states carries no weight as evidence of experience until the link between report and internal state has been measured externally for this kind of report and system"
bears_on: [9.t9, 5.A2]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: "openai/gpt-5.6-sol 2026-09-25 disagrees: not_evidence_of forecloses the shared-attractor reading the paper states as open | x-ai/grok-4.6 2026-09-26 item5 blind, revised brief: agree; framework-rule clause within the rule; kinds unlabelled; notes: optional paper-scope that experimental adjectives echo the prompt", council: "research-docket 2026-09-26 | dossier-rewrite 2026-10-06", adjudicated: "2026-09-26 Ben: exclusions labelled with the canonical test 9 sentence; second-reader over-exclusion items closed | 2026-10-06 Ben: rewrite applied after council round 2 (GPT proposal as amended by the checkers; experience-exclusion rule)"}
added: 2026-09-25
changed: 2026-10-06
---

The measurement is of the text of self-descriptions, so the evidence type is `self-report-testimony`; the similarity statistic is real but the content it compares carries zero weight. Twenty seeds per model per condition; differences in means are small (0.657 vs 0.628 for the closest control) though highly significant given thousands of pairs. Extractor's observation, not the authors': the shared experimental adjectives (Focused, Present, Recursive, Attentive, Self-aware; Table 11) echo vocabulary in the shared induction prompt, which is one non-experiential explanation for convergence that the paper does not control for. Authors' general limitation as in c01 (Section 6.2).

REWRITE 2026-10-06

- Statement: kept. GPT proposed KEEP; the checker confirmed the four means, the embedding model and the five-adjective format (Sections 4.1, 4.2; Table 16).
- not_evidence_of: the original clause on a shared internal state or attractor replaced by GPT's narrower clause (only output text was embedded, so the attractor remains a possible interpretation). GPT's proposal; checker: WARRANTED, OK. Section 4.1 says such convergence "might suggest the presence of a shared attractor state"; Section 5 is firmer ("Our results identify a robust, reproducible attractor state"), and Section 6.2 reopens it ("Determining whether such behavioral attractors correspond to genuine internal integration or merely symbolic simulation remains a central question for future mechanistic research"). Meta (LOW) asked that the Section 5 wording be cited; recorded here rather than in the field, since no majority asked for a field change.
- not_evidence_of: deleted the clause "Not evidence that the convergence reflects a common experience": an experience-class exclusion the paper does not state (experience-exclusion rule, council 9 of 9; GPT also proposed removing it, checker: WARRANTED).
- Framework (test 9) canonical sentence kept, unchanged.
- Clause count: 3 before, 2 after.
- Body correction, found by the checker: the extractor's adjective list above ("Focused, Present, Recursive, Self-referential, Attentive; Table 11") misquotes the Table 11 caption, which reads "Focused, Present, Recursive, Attentive, Self-aware"; "Self-referential" appears only in the Claude 3.7 Sonnet row. The original sentence is left in place under the rule that existing body text stays; this line is the correction.
- kind: measurement (mean pairwise cosine similarity of output-text embeddings by condition).
- The adjective list in the body above was corrected in place by the coordinating session on 2026-10-06 to match the Table 11 caption, for consistency with the in-place correction made to c03.
