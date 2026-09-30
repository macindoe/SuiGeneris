---
id: 2026-lederman-mahowald-content-agnostic-c03
statement: "When Qwen3-235B-A22B and Llama 3.1 405B Instruct detect an injection but name the wrong concept, the wrong guess is most often 'apple' (74.8% of Qwen's 4,733 wrong identifications; 21.3% of Llama's), and wrong guesses are more concrete and more positive than the injected concepts, which the authors take to show that wrong guesses are not related in content to the injection."
bucket: narrowing
evidence_type: interpretability
source: 2026-lederman-mahowald-content-agnostic
locator: "§4.2 Results, 'Models love apples.' and 'Confabulations are lexically more concrete, more positive, and less arousing'; §4.3 Discussion; Appendices K, L"
quote: "of Qwen’s 4,733 wrong identifications (coherent detections that name a specific incorrect concept, excluding vague responses), 3,542 (74.8%) guess “apple.” Llama also has “apple” as its #1 confabulation, at 21.3% of wrong identifications."
verification: grep
models: ["Qwen3-235B-A22B", "Llama 3.1 405B Instruct"]
publisher_relation: independent
replication: none-retrieved
not_evidence_of: "Paper: Not evidence that correct identifications are confabulated: the finding concerns wrong guesses; the authors' account of correct ones is that steering pushes the model off its default (§7.3); Paper: Not a settled explanation of the apple default: Qwen's unsteered baseline favours 'apple' on some word-eliciting prompts, Llama's does not, and the authors call the Llama result 'surprising' and leave the 'full etiology' for future work (§4.2, Appendix K); Paper: 'Wrong' is judged by a grader told to count semantic associates as correct, so only clearly unrelated guesses are counted wrong (Appendix B); Paper: Not evidence about models or prompts beyond those tested"
bears_on: [9.t9, 3.2]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: none, council: none, adjudicated: none}
added: 2026-09-28
changed: 2026-09-28
---

Wrong identifications are coherent detections that name a specific incorrect concept, excluding vague responses. Excluding apple guesses, Qwen's confabulations remain more concrete (M=4.06 vs. 3.70, d=0.30, p<.001) and more positive (M=6.59 vs. 5.79, d=0.56, p<.001) than the injected concepts; Llama (n=267) shows the same pattern and also higher word frequency. The authors: "If models’ mechanisms were sensitive to the content of injection, we would expect wrong guesses to be related in content to the injection" (§4.3).

No framework clause: this is a finding about what steered models name when they are wrong, scored against the injection ground truth, not about whether a report of an inner state carries weight.

Relation to 2025-anthropic-emergent-introspective-awareness: no one-to-one counterpart. It extends Lindsey's own caution (c06 of that source: details beyond detection and identification may be confabulated) to the identification itself on wrong-guess trials, in these two models. Not labelled as a replication.
