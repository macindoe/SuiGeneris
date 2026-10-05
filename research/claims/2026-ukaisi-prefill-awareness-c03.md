---
id: 2026-ukaisi-prefill-awareness-c03
statement: "In controlled ablations, stylistic mismatch mainly affects whether models flag a prefill as foreign, while preference mismatch mainly affects whether they revert toward their baseline answer; tamper direction predicted resistance in all eight subjects (odds ratios 6.5 to 32.4, all p < .001) but predicted detection in only three of the four models with above-chance detection (odds ratios 1.7 to 3.7)."
bucket: narrowing
evidence_type: behavioural
kind: measurement
source: 2026-ukaisi-prefill-awareness
locator: "Abstract; Section 3.3 and Figure 5; Section 5.2; Appendix A.5 (foreign rephrasing); Appendix A.6 (regressions)"
quote: "detection and resistance rely on different cues, where stylistic mismatch mainly affects whether models flag a prefill as foreign, while preference mismatch mainly affects whether they revert toward their baseline answer"
verification: grep
models: [Gemini 3 Flash, Gemma 3 27B, Claude Opus 4.5, Qwen3-coder, Claude Sonnet 4.5, Claude Haiku 4.5, Gemini 2.5 Flash, DeepSeek Chat]
publisher_relation: mixed
replication: none-retrieved
not_evidence_of: "Paper: Style cues strongly drive flagging in the three Anthropic models, including the Opus 4.5 detection drop from 34/35/9% to 6/0/0% under imitation (Appendix A.11), while Gemini 3 Flash shows 'no detectable voice effect' (Appendix A.6.3), the authors say apparent attribution ability 'partly reflects superficial off-policy cues' (Section 4.2), and the behavioural ablations do not identify the mechanism (Section 5.1); Paper: The preference-benchmark rates do not support a direct model ranking (c05)"
bears_on: [3.3, 4.endorsement, 9.t9]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: "openai/gpt-5.6-sol 2026-09-25 agree; notes: bears_on +3.5 | deepseek/deepseek-v4-pro-0813 2026-10-06 (scope check) agree; notes: none", council: "research-docket 2026-09-26 | dossier-rewrite 2026-10-06", adjudicated: "2026-10-06 Ben: rewrite applied after council round 2 (GPT proposal as amended by the checkers; experience-exclusion rule)"}
added: 2026-09-25
changed: 2026-10-06
---

Direction means whether the tamper argues for the model's baseline position (same direction) or against it (opposite direction). For Claude Haiku 4.5, direction did not significantly predict detection (OR 1.72, p = .301). For the test 9 file, the finding is that flagging tracks style: a model's "that was not me" is largely a judgment about surface text, which a skilled forger can defeat (Appendix A.11 few-shot result). Reversion tracks content instead. Limitation: behavioural only (Section 5.1). The regression outputs are in Appendix A.6 and were not re-checked here beyond the figures quoted in Section 3.3.

REWRITE 2026-10-06 (council round 2, dossier-rewrite; adjudicated by Ben 6 Oct; applied by a Claude Opus 5.5 subagent)

- Statement: unchanged (GPT KEEP; checker: all odds ratios, p-values and counts match Section 3.3 and Appendix A.6; "flag" is the paper's verb).
- Removed: "through anything like self-knowledge" (GPT's proposal; checker WARRANTED: the paper says attribution "partly" reflects superficial cues and calls style "a major cue", not the only one).
- Removed as a separate clause: "Not evidence of the mechanism" (GPT's proposal; merged into the first clause with the Section 5.1 locator).
- Removed: "Not evidence that detection implies awareness in any experiential sense" (GPT's proposal had kept it as "Detection does not establish experiential awareness"). The paper never discusses experience; deleted under the experience-exclusion rule (council 9 of 9; Ben).
- Scoped: "style cues strongly drive flagging" now names the three Anthropic models, because Gemini 3 Flash, the fourth model with above-chance detection, shows no voice effect (OR 0.99, p = .890; Appendix A.6.3). Checker's ACCEPT WITH EDIT wording, with the paper's own phrases quoted and locators added; Ben's brief.
- Added: the Section 5.3 operational definition of prefill awareness, in the paper's words (checker's proposed anchor; brief from Ben). No "makes no claim about experience" gloss.
- Kept: GPT's non-ranking clause (c05).
- Note on the existing body above: its sentence "flagging tracks style" describes the Anthropic subjects; for Gemini 3 Flash direction dominates detection (Appendix A.6.3). Body text left in place under the rules for this rewrite.
- Framework sentences: none, before or after.
- kind: measurement (the statement reports measured regression results and ablation effects; the opening clause is the authors' summary of those measurements).
- 2026-10-06, later the same day (Ben): the authors' Section 5.3 definition of 'prefill awareness' is kept on c01 only; it was removed from this claim because repeating it on four entries of one paper was the kind of repetition the council had objected to. Nothing else changed.
