---
id: 2026-macar-mechanisms-introspective-awareness-c02
statement: "Base models do not discriminate injected from control trials (Gemma3-27B base: 42.3% false positives against 39.5%–41.7% true positives), and across OLMo-3.1-32B's training pipeline the base and SFT checkpoints show high false positive rates that fall to 0% only after DPO, while OLMo's detection rate also falls, to 2.9% after DPO and 0.9% in the final instruct checkpoint."
bucket: narrowing
evidence_type: interpretability
source: 2026-macar-mechanisms-introspective-awareness
locator: "§3.3 The Role of Post-Training, Figure 4 left; Appendix C, Figure 21"
quote: "We observe similar patterns for OLMo-3.1-32B ( Appendix C ): both the base and SFT checkpoints exhibit high FPR, and only after DPO does it drop to 0%."
verification: grep
models: ["Gemma3-27B base", "Gemma3-27B instruct", "OLMo-3.1-32B base, SFT, DPO and instruct checkpoints"]
publisher_relation: mixed
replication: none-retrieved
not_evidence_of: "Paper: Not evidence that DPO produces detection: in OLMo-3.1-32B, SFT gives the highest true positive rate (14.9%, with 22.5% false positives) and DPO removes false positives while detection drops to 2.9%; Paper: Not evidence about which ingredient of Gemma's post-training matters, since Gemma's intermediate checkpoints were not tested; Paper: Not evidence that post-training creates the whole circuit: the authors cannot resolve whether upstream evidence carriers are pre-existing structure that post-training learns to leverage; Paper: Not evidence of experience, or that training instilled anything experiential; Framework (test 9, steering): a coupling measured under steering shows that the channel can be steered and does not weight reports offered in ordinary operation"
bears_on: [9.t9, 5.A2, 3.2]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: none, council: none, adjudicated: none}
added: 2026-09-28
changed: 2026-09-28
---

The authors summarise: "The capability is absent in base models, emerges from post-training" (§1), and for OLMo: "base models cannot discriminate, post-training eliminates false positives, but the same stages that improve reliability may also suppress true detection through refusal-like mechanisms" (Appendix C). Full OLMo figures (Appendix C, aggregated over five layers and four strengths): base 0.1% TPR / 16.4% FPR; SFT 14.9% / 22.5%; DPO 2.9% / 0%; instruct 0.9% TPR / 0% FPR, 0.3% introspection rate. Note that the §3.3 prose says OLMo base shows "high FPR" while Appendix C gives near-zero detection for it, so OLMo base does not repeat Gemma base's pattern of high detection with equal false positives; what both share is no discrimination. The mechanistic companion to this result (the gate feature's inverted-V pattern is "substantially weaker in the base model", and the base model shows no L45 localisation) is in c03.

The intake brief asked for this claim as "emerges from post-training; DPO elicits, SFT does not". The held text does not support "DPO elicits": in OLMo, DPO is the stage at which false positives disappear, and detection there is near zero. The claim is written to what the text says.

REPLICATES: 2025-anthropic-emergent-introspective-awareness — the §5.7 finding that base pretrained models "generally have a fairly high false positive rate, and none of them achieve greater-than-zero net task performance" (not filed as its own claim in that intake). The same holds here for Gemma3-27B base and OLMo-3.1-32B base, outside the Claude family. Independence: partial only; the replicated paper's author is an advising author here. The training-stage split (SFT vs DPO) goes beyond Lindsey 2025, which could not separate pretraining from post-training effects (its footnote 11).
