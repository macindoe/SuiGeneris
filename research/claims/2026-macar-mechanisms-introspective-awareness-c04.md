---
id: 2026-macar-mechanisms-introspective-awareness-c04
statement: "In Gemma3-27B instruct, detection is not governed by a single linear direction: for 23.3% of 1,000 pairs of high-detection concepts both opposite steering directions trigger detection (3.2% for low-detection pairs), and swapping either the mean-difference projection or the residual between success and failure concepts transfers part of the detection rate."
bucket: narrowing
evidence_type: interpretability
source: 2026-macar-mechanisms-introspective-awareness
locator: "§4.1 to §4.3 (Figures 5 to 7); Appendices E and F"
quote: "In 23.3% of S-S pairs, both opposite directions trigger detection, compared to only 3.2% for F-F pairs. This is inconsistent with the single direction hypothesis."
verification: grep
models: ["Gemma3-27B instruct"]
publisher_relation: mixed
replication: none-retrieved
not_evidence_of: "Paper: Not evidence that no single direction matters: one direction (the success-minus-failure mean difference) explains a substantial fraction of detection variance and behaves as a threshold, which the authors read as a 'factual content' classifier repurposed during introspection; Paper: Not evidence against every shallow explanation: it rules out the specific confound that some concept vectors align with one direction promoting affirmative answers, and does not test prompt-level manipulations; Paper: Not evidence about other models; Paper: Not evidence of experience"
bears_on: [9.t9, 5.A2]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: none, council: none, adjudicated: none}
added: 2026-09-28
changed: 2026-09-28
---

This is the paper's answer to the confound raised by Godet (2025a, LessWrong, cited in §7.3), that steering generically pushes models toward "Yes". Swap results (§4.1): for success concepts, projection swap 66.1% to 39.0%, residual swap to 44.4%; for failure concepts, 8.8% to 34.2% and 32.8%. Ridge regression on downstream transcoder features predicts per-concept detection better (R² 0.624) than projection on the mean-difference direction (0.309) or full concept vectors (0.444) (§4.3). The mean-difference direction is nearly orthogonal to the refusal direction (cos -0.09) and correlates with concept verbalizability (Spearman 0.605); detection follows a sigmoid along it (Appendix F). No framework clause: the claim concerns the geometry of the steering perturbation and not a report's weight as evidence.

No replication line: Lindsey 2025 did not test the single-direction hypothesis. The Singh, Linzen and Ravfogel 2026 contest of the Lindsey paradigm (`2026-singh-introspection-reality-check-c04`, `-c05`) turns on prompt-only manipulation, which this claim does not address.
