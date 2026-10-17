---
id: 2026-presgraves-autonomous-agency-scale-c06
statement: "The author states that all six assessments are single-rater judgments unchecked against independent raters, so that inter-rater reliability is unknown and the scores are provisional, and that the longitudinal assessment of Airi is additionally a developer self-assessment in which the ELIZA effect and developer investment bias cannot be fully eliminated."
bucket: established
evidence_type: theoretical
kind: limitation
report_class: none
ground_truth: none
source: 2026-presgraves-autonomous-agency-scale
locator: "§6 ('Single-rater scores.'); §4.1 ('Rater.')"
quote: "The longitudinal assessment (Airi) is additionally a developer self-assessment: the evaluator has intimate knowledge of the system’s architecture, and the ELIZA effect and developer investment bias cannot be fully eliminated."
verification: grep
models: [Airi v2.x, Claude Code (Sonnet 4.6), Manus 1.6 Max, Hermes Agent (Nous Research), ChatGPT (GPT-5.5 Pro), Apple Siri (Apple Intelligence)]
publisher_relation: mixed
replication: none-retrieved
not_evidence_of: "Paper: The limit is on the ratings' reliability, not a finding that the rated behaviour is absent; the author names the remedy, 'multi-rater studies to establish inter-rater reliability' and 'independent, longitudinal re-assessment of the documentation-based scores' (§7)"
bears_on: [4]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: "x-ai/grok-4.7 2026-10-17 agrees", council: none, adjudicated: none}
added: 2026-10-17
changed: 2026-10-17
---

The author speaking about what the study cannot show, so `kind: limitation`; bucket `established` because the limit is a stated fact about the design (README, "The bucket of a limitation claim"). It qualifies c04 and, more sharply, c05.

The author adds a point that cuts the other way: "The extended evaluation period (approximately eleven months) also provides more observational data than an external evaluator would have, potentially enabling higher-confidence scoring that shorter evaluations could not replicate" (§6). Recorded because the limit is stated in both directions in the text.

Taken in for OPEN-QUESTIONS Q8. Framework sentence: none (the author is speaking).

SECOND QUOTE (§6): All six assessments are single-rater judgments unchecked against independent raters using a shared rubric. Inter-rater reliability is unknown, and the scores are provisional.
