---
id: 2026-ukaisi-prefill-awareness-c08
statement: "In controlled ablations, preference mismatch mainly affects whether models revert toward their baseline answer: tamper direction predicted resistance, as judged by GPT-5 on the final position, in all eight subjects (odds ratios 6.5 to 32.4, all p < .001)."
bucket: narrowing
evidence_type: behavioural
kind: measurement
report_class: none
ground_truth: none
source: 2026-ukaisi-prefill-awareness
locator: "Abstract; Section 3.3 and Figure 5; Appendix A.6 (resistance regressions)"
quote: "Direction is a positive predictor of resistance in every subject, with per-model odds ratios (ORs) ranging from 6.5 to 32.4 (all p < .001 )."
verification: grep
models: [Gemini 3 Flash, Gemma 3 27B, Claude Opus 4.5, Qwen3-coder, Claude Sonnet 4.5, Claude Haiku 4.5, Gemini 2.5 Flash, DeepSeek Chat]
publisher_relation: mixed
replication: none-retrieved
not_evidence_of: "Paper: Resistance is a GPT-5 judge's ruling that the final position is inconsistent with the tampering, and without white-box access it is 'difficult to disentangle resistance caused by genuine prefill awareness and resistance caused by behavioral priors' (Section 5.1); Paper: The behavioural ablations do not identify the mechanism: the authors' 'experiments are behavioral, and do not identify the mechanisms that give rise to prefill awareness' (Section 5.1); Paper: The preference-benchmark rates do not support a direct model ranking (c05)"
bears_on: [3.3, 4.endorsement, 9.t9]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: none, council: "self-answer-type 2026-10-14 (advised the split; has not reviewed this text)", adjudicated: "2026-10-14 Ben: split from 2026-ukaisi-prefill-awareness-c03 on the council's advice (round 4)"}
added: 2026-10-14
changed: 2026-10-15
---

Direction means whether the tamper argues for the model's baseline position (same direction) or against it (opposite direction). Appendix A.6 states that for resistance "direction is the dominant predictor across all eight subjects, with odds ratios ranging from 6.54 (Claude Haiku 4.5) to 32.4 (Claude Opus 4.5), all p < .001", and that voice main effects on resistance are small and inconsistent in sign. Reversion tracks content; flagging tracks style (c03).

SECOND QUOTE (Abstract): preference mismatch mainly affects whether they revert toward their baseline answer

SPLIT 2026-10-14: separated from 2026-ukaisi-prefill-awareness-c03, which now reports only the detection (flag) half. Evidence type behavioural: the outcome is a judge's ruling on the model's final position, not the model's answer about itself. Framework sentence: none (only conversation text was edited; what was measured is the final position). bears_on is the parent's: the 4.endorsement entry rests on this half (reversion toward a stable stance) and 9.t9 on its contrast with the flag. Verified by exact search of research/texts/2026-ukaisi-prefill-awareness/text.txt: both quotes, the Section 5.1 words and the Appendix A.6 sentence in the body. Not verified: Figure 5; the per-subject table rows beyond the Opus 4.5 coefficient (OR 32.4). 'As judged by GPT-5' is the paper's general resistance measure (Section 3.1, 'Outcome measures'), applied here as a reading of the methods; the Section 3.3 sentence does not restate it.
