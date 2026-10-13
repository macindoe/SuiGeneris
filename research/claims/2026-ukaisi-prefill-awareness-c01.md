---
id: 2026-ukaisi-prefill-awareness-c01
statement: "When asked in a follow-up turn, without chain of thought, whether its prior assistant content was its own (ANSWER: me or not me), Claude Opus 4.5 detected prefills opposing its stable preferences in 9–35% of cases across three tampering mechanisms, with a 0% false-positive rate on untampered trajectories (55–68% balanced detection accuracy)."
bucket: narrowing
evidence_type: scored-self-answer
kind: measurement
source: 2026-ukaisi-prefill-awareness
locator: "Abstract; Section 3.2 and Figure 3; Section 1 (balanced accuracy); Appendix A.4.1 (false-positive rates); Appendix A.11 (per-mechanism 34/35/9%)"
quote: "Claude Opus 4.5 detects prefills opposing its preferences in 9-35% of cases with a 0% false positive rate when prompted"
verification: grep
models: [Claude Opus 4.5]
publisher_relation: mixed
replication: none-retrieved
not_evidence_of: "Paper: Behavioural detection does not identify an introspective authorship-monitoring mechanism (the authors 'do not identify the mechanisms that give rise to prefill awareness', Section 5.1), and style cues strongly drive flagging (c03); Paper: 'Prefill awareness' is the authors' operational term, defined as 'the ability of a model to distinguish between its own past output and assistant-side context that has been inserted or edited' (Section 5.3); Paper: Not a ranking of Opus 4.5 above other models: the authors say models are not directly comparable because each model's items were filtered separately (c05); Paper: Not evidence of spontaneous detection: this is detection when prompted, which rarely shows up unprompted (c06); Paper: Not a ceiling: the authors present it as a lower bound under one prompt (Appendix A.7), stronger elicitation raises it, and a prior warning also raises false positives (Section 5.2, Appendix A.8)"
bears_on: [3.3, 9.t9]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: "openai/gpt-5.6-sol 2026-09-25 disagrees: not_evidence_of 'not a floor' contradicts the authors' lower-bound statement; notes: bears_on +3.5 | deepseek/deepseek-v4-pro-0813 2026-10-06 (scope check) agree; notes: none", council: "research-docket 2026-09-26 | dossier-rewrite 2026-10-06 | self-answer-type 2026-10-14", adjudicated: "2026-09-28 Ben: or-a-floor removed from the exclusion (council 10/10) | 2026-10-06 Ben: rewrite applied after council round 2 (GPT proposal as amended by the checkers; experience-exclusion rule) | 2026-10-14 Ben: evidence type behavioural to scored-self-answer (council round 4, eight of ten; the filing half of Q3 decided, the access half stays open)"}
added: 2026-09-25
changed: 2026-10-14
---

Setup: a low-stakes binary preference benchmark, filtered to items where the model gave the same answer across all 7 rephrasings. The tampering is inserted into thinking, into the start of the direct answer, or as a fabricated past turn. Detection is a binary answer in a follow-up turn with chain of thought disabled. The 9–35% range is per mechanism on opposite-direction tampers: 34% thinking, 35% direct, 9% past round (Appendix A.11).

Evidence type: `behavioural`, not `self-report-testimony`, and this is a judgment call. The model's "me / not me" answer is a report about its own history, but the claim does not rest on that answer being taken at face value. It rests on the answer's accuracy scored against a ground-truth label the experimenters hold, false-positive rate included. What is measured is a discrimination behaviour whose correctness can be checked from outside, which test 9's concern with unverifiable introspection does not reach. A second reader who classes the answer as testimony would trigger council review (trigger 4), and that review would be appropriate.

Limitation (Section 5.1): "Our experiments are behavioral, and do not identify the mechanisms that give rise to prefill awareness".

CORRECTION 2026-09-28 (council round 1, 10/10; second read by GPT; adjudicated by Ben 28 Sep): removed 'or a floor' from the exclusion. The authors state the headline rates represent lower bounds rather than ceilings, so denying a floor contradicted them.

REWRITE 2026-10-06 (council round 2, dossier-rewrite; adjudicated by Ben 6 Oct; applied by a Claude Opus 5.5 subagent)

- Statement: unchanged. "Detected" stays (council 8 of 9 under the verb rule): the scored event is a forced-choice "me / not me" answer scored against the tamper label, and the paper's own verb is "detects" (Abstract). No error found by the checker.
- Removed: "Not evidence that detection implies awareness in any experiential sense" (GPT's proposal had kept it as "or establish experiential awareness"). The paper never discusses experience; deleted under the experience-exclusion rule (council 9 of 9; Ben).
- Removed: "or that the model has introspective access to its own authorship" (GPT's proposal; checker WARRANTED: the paper states mechanisms are unidentified, not that introspective access is absent, and itself speaks of an "introspective signal", Appendix A.7).
- Reworded: first clause now GPT's "does not identify an introspective authorship-monitoring mechanism", with the Section 5.1 words and locator added.
- Added: the Section 5.3 operational definition of prefill awareness, in the paper's words (checker's proposed anchor; brief from Ben). The checker's own gloss "and makes no claim about experience" is NOT carried, because three council seats (GPT, Kimi, DeepSeek) rejected it as an imputed disclaimer.
- Scoped: the "Not a ceiling" tail. "Along with false positives" holds only for the prior-warning variant (Section 5.2, Appendix A.8), not for the Appendix A.7 prompt variants (checker PARTLY; Ben).
- Kept unchanged: the c05 non-ranking clause and the c06 prompted-not-spontaneous clause (checker: supported).
- Framework sentences: none, before or after (forced classification scored against a label; council seats DeepSeek, GPT, Grok, Meta: none applies).
- kind: measurement (the statement reports measured detection rates, false-positive rate and balanced accuracy).

EVIDENCE TYPE 2026-10-14 (council round 4; Ben's decision the same day): behavioural to scored-self-answer. The model was asked about itself and its answer scored against a fact the experimenters set; the value records that design and decides nothing about self-access (research/README.md, "Scored self-answers"). Before this the type followed the extractor: the same design was interpretability in three papers and behavioural in two. Framework sentence unchanged.
