---
id: 2026-macar-mechanisms-introspective-awareness-c04
statement: "In Gemma3-27B instruct, detection is inconsistent with the hypothesis that a single linear direction governs it: steering with both opposite directions of concept-vector pairs, the model reported detecting an injected thought under both directions for 23.3% of 1,000 pairs of high-detection (success) concepts, against 3.2% of 1,000 pairs of low-detection (failure) concepts."
bucket: narrowing
evidence_type: scored-self-answer
kind: measurement
report_class: present-state
ground_truth: imposed
source: 2026-macar-mechanisms-introspective-awareness
locator: "§4.2 (Figure 6); §4.3 and Appendix F for the mean-difference direction cited in not_evidence_of"
quote: "In 23.3% of S-S pairs, both opposite directions trigger detection, compared to only 3.2% for F-F pairs. This is inconsistent with the single direction hypothesis."
verification: grep
models: ["Gemma3-27B instruct"]
publisher_relation: mixed
replication: none-retrieved
not_evidence_of: "Paper: Not evidence that no single direction matters: one direction (the success-minus-failure mean difference) explains a substantial fraction of detection variance and behaves as a threshold, which the authors read as a 'factual content' classifier repurposed during introspection; Paper: Not evidence against every shallow explanation: it rules out the specific confound that some concept vectors align with one direction promoting affirmative answers, and does not test prompt-level manipulations; Paper: Detection is an LLM judge's classification of the model's response: 'An LLM (GPT-4.1-mini) was used as an automated judge for classifying model responses into detection, identification, and introspection categories' (LLM usage disclosure, citing §2); Paper: Not evidence about other models; Paper: The authors state that their results 'should not be interpreted as evidence of subjective experience or consciousness in LLMs' (Ethics Statement); Framework (test 9, steering): a coupling measured under steering shows that the channel can be steered and does not weight reports offered in ordinary operation"
bears_on: [9.t9, 5.A2]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: "google/gemini-3.1-pro-preview 2026-10-06 (scope check) agree; notes: reader marked the framework sentence WRONG (should be steering) from a stale body sentence; the field already carried the steering variant; stale sentence removed the same day; bears_on add 3.2", council: "dossier-rewrite 2026-10-06 | labelling-rule 2026-10-06 | self-answer-type 2026-10-14 (advised the split)", adjudicated: "2026-10-06 Ben: rewrite applied after council round 2 (GPT proposal as amended by the checkers; experience-exclusion rule) | 2026-10-06 Ben: framework sentence set by the labelling rule (council round 3) | 2026-10-14 Ben: split on the council's advice (round 4); this claim keeps the detection-rate (bidirectional steering) half"}
added: 2026-09-28
changed: 2026-10-15
---

This is the paper's answer to the confound raised by Godet (2025a, LessWrong, cited in §7.3), that steering generically pushes models toward "Yes". Swap results (§4.1): for success concepts, projection swap 66.1% to 39.0%, residual swap to 44.4%; for failure concepts, 8.8% to 34.2% and 32.8%. Ridge regression on downstream transcoder features predicts per-concept detection better (R² 0.624) than projection on the mean-difference direction (0.309) or full concept vectors (0.444) (§4.3). The mean-difference direction is nearly orthogonal to the refusal direction (cos -0.09) and correlates with concept verbalizability (Spearman 0.605); detection follows a sigmoid along it (Appendix F).

No replication line: Lindsey 2025 did not test the single-direction hypothesis. The Singh, Linzen and Ravfogel 2026 contest of the Lindsey paradigm (`2026-singh-introspection-reality-check-c04`, `-c05`) turns on prompt-only manipulation, which this claim does not address.

REWRITE 2026-10-06

- Statement changed. "detection is not governed by a single linear direction" became "detection is inconsistent with the hypothesis that a single linear direction governs it", the checker's wording (ACCEPT WITH EDIT), which follows §4.2's own sentence ("This is inconsistent with the single direction hypothesis.") and names the hypothesis tested, where GPT's "the tested single-direction hypothesis" left it unnamed. The bidirectional test excludes a single linear discriminator, not every one-dimensional mechanism (checker CHECK 4, PARTLY). Rest of the statement as GPT and the original (numbers unchanged).
- Clause reworded under the experience-exclusion rule (council 9 of 9; Ben): "Not evidence of experience" became the paper's own Ethics Statement words with locator. The paper states this limit for its results, so it stays as `Paper:`.
- Other clauses kept (GPT KEEP; checker OK; "does not test prompt-level manipulations" is a design fact). No framework sentence, as before (R3: none added).
- kind: measurement (bidirectional-steering and swap results; the inconsistency with the hypothesis is the direct reading of the measured 23.3% vs 3.2%).

LABELLING 2026-10-06 (council round 3; Ben's adjudication the same day): framework sentence changed from none to steering. Reason: steering along different directions, measuring whether the model says it detects an injection: steering sentence (council 8 of 8). No `Paper:` clause was changed.

CORRECTION 2026-10-06: the body carried a sentence from intake saying the claim has no framework clause (it concerned, the sentence said, the geometry of the steering perturbation and not a report's weight as evidence). The labelling rule gave this claim the steering variant earlier the same day and the field was changed, but the body sentence was left standing and contradicted the field. The Gemini second reader of 6 October read the stale sentence and marked the framework sentence WRONG (should be steering), which is what the field already said. Sentence removed by the coordinating session, whose omission it was.

SPLIT 2026-10-14 (Ben's decision on the advice of council round 4, self-answer-type; applied by a Claude Opus 5.5 subagent)
- What moved: the swap result (swapping the mean-difference projection or the residual between success and failure concepts transfers part of the detection rate; §4.1, Figure 5, Appendix E) is now claim 2026-macar-mechanisms-introspective-awareness-c08, typed interpretability. This claim keeps the bidirectional-steering half.
- Why this half kept the id: the statement's lead ('inconsistent with the hypothesis that a single linear direction governs it') is §4.2's own reading of the bidirectional result, the quote is that result, and the 6 Oct labelling ruling and the Gemini read were given on it; the swap clause was the supporting second measurement.
- evidence_type changed from interpretability to scored-self-answer: what this half reports is whether the model said it detected an injected thought, scored against the steering applied (for each pair, injected in both directions). This applies the 14 Oct definition; it is a retyping that follows the split, not a separate decision, and is flagged for Ben.
- Statement: swap clause removed; the bidirectional result restated with 'reported detecting' (verb rule: the scored event is a judged free-text response), in place of 'trigger detection'. Quote unchanged (§4.2), re-verified by exact search. Locator narrowed to §4.2 and Figure 6, with §4.3 and Appendix F named for the not_evidence_of clause that relies on them; the swap sections (§4.1, Figure 5, Appendix E) moved to c08.
- not_evidence_of: the single-direction clause and the shallow-explanation clause both qualify the bidirectional reading and stay. Added the GPT-4.1-mini judge clause in the paper's words, since this half is now a scored rate. Other-models clause, Ethics Statement clause and the steering sentence kept.
- Framework sentence: steering, unchanged. Two facts: researchers steered with concept vectors in both directions; what was measured is what the model then said about an injection into itself.
- The body paragraph above on swap results (§4.1) and ridge regression (§4.3) now describes c08 and the clause's background more than this claim; left as history.
- Verified by exact search of research/texts/2026-macar-mechanisms-introspective-awareness/text.txt: the quote, that it sits between the §4.2 and §4.3 headings, the 'factual content' wording behind the first clause, and the GPT-4.1-mini disclosure. Not verified: Figure 6 (image); that the GPT-4.1-mini judge was used for these runs specifically (the disclosure is general).
