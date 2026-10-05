---
id: 2026-lederman-mahowald-content-agnostic-c03
statement: "When Qwen3-235B-A22B and Llama 3.1 405B Instruct report detecting an injection but name the wrong concept, the wrong guess is most often 'apple' (74.8% of Qwen's 4,733 wrong identifications; 21.3% of Llama's), and wrong guesses are more concrete and more positive than the injected concepts, which the authors take to show that wrong guesses are not related in content to the injection."
bucket: narrowing
evidence_type: interpretability
kind: measurement
source: 2026-lederman-mahowald-content-agnostic
locator: "§4.2 Results, 'Models love apples.' and 'Confabulations are lexically more concrete, more positive, and less arousing'; §4.3 Discussion; Appendices K, L"
quote: "of Qwen’s 4,733 wrong identifications (coherent detections that name a specific incorrect concept, excluding vague responses), 3,542 (74.8%) guess “apple.” Llama also has “apple” as its #1 confabulation, at 21.3% of wrong identifications."
verification: grep
models: ["Qwen3-235B-A22B", "Llama 3.1 405B Instruct"]
publisher_relation: independent
replication: none-retrieved
not_evidence_of: "Paper: The wrong-guess finding does not establish that correct identifications are confabulated, and the authors' account of correct ones is that steering pushes the model off its default (§7.3); Paper: The apple default has no settled explanation: Qwen's unsteered baseline favours 'apple' on some word-eliciting prompts while Llama's does not, the authors call Llama's apple confabulation 'surprising given the baseline data', and they leave the 'full etiology' of the apple default for future work (§4.2, Appendix K); Paper: 'Wrong' is reserved by grader instruction for 'clearly unrelated concepts with no semantic connection' (Appendix B), so the unrelatedness of counted wrong guesses is partly set by the grading rule, the paper reports no validation of the WRONG labels, and in describing Experiment 3 the authors note that the grader 'is sometimes overly permissive' (§6.1); Paper: Results do not extend to untested models or prompts; Framework (test 9, steering): a coupling measured under steering shows that the channel can be steered and does not weight reports offered in ordinary operation"
bears_on: [9.t9, 3.2]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: none, council: "dossier-rewrite 2026-10-06", adjudicated: "2026-10-06 Ben: rewrite applied after council round 2 (GPT proposal as amended by the checkers; experience-exclusion rule)"}
added: 2026-09-28
changed: 2026-10-06
---

Wrong identifications are coherent detections that name a specific incorrect concept, excluding vague responses. Excluding apple guesses, Qwen's confabulations remain more concrete (M=4.06 vs. 3.70, d=0.30, p<.001) and more positive (M=6.59 vs. 5.79, d=0.56, p<.001) than the injected concepts; Llama (n=267) shows the same pattern and also higher word frequency. The authors: "If models’ mechanisms were sensitive to the content of injection, we would expect wrong guesses to be related in content to the injection" (§4.3).

No framework clause: this is a finding about what steered models name when they are wrong, scored against the injection ground truth, not about whether a report of an inner state carries weight.

Relation to 2025-anthropic-emergent-introspective-awareness: no one-to-one counterpart. It extends Lindsey's own caution (c06 of that source: details beyond detection and identification may be confabulated) to the identification itself on wrong-guess trials, in these two models. Not labelled as a replication.

REWRITE 2026-10-06 (applied by a Claude Opus 5.5 subagent; Claude lineage, same as the extractor)
- Statement: 'detect an injection' -> 'report detecting an injection' (GPT's change, checker SUPPORTED, council 9 of 9 in Q5: the scored event is the Haiku-graded detection claim, §3, Appendix B). Nothing else changed.
- Clause 1: GPT's wording taken (internal semicolon removed for field format).
- Clause 2: GPT's 'because' (which made the Qwen/Llama contrast the reason) replaced by a list, as the checker recommended; the authors' 'surprising given the baseline data' (Appendix K) and 'full etiology' sentence (§4.2) quoted.
- Clause 3: GPT's grading clause replaced by the checker's wording (Ben's brief): the WRONG rule partly builds in the unrelatedness result, and no validation of the labels is reported. Internal semicolon turned into a comma. The §6.1 permissiveness note is kept as the checker proposed but scoped to Experiment 3, where it appears; Kimi (one seat, LOW) argued it should be dropped because §6.1 concerns judging correctness. The original's 'so only clearly unrelated guesses are counted wrong' stays removed (GPT; checker: an instruction does not guarantee the outcome).
- Clause 4: GPT's wording taken.
- Steering sentence ADDED (R3(b), Ben's decision; all nine seats wanted at least the steering variant). The canonical sentence is NOT added (council split 5 to 4, 3 to 3 without the misattributed seats; Ben's decision). The earlier body line 'No framework clause' is superseded by this entry.
- kind: measurement (the statement reports apple counts and the concreteness and valence comparison; the authors' content-unrelatedness reading is attributed to them).
