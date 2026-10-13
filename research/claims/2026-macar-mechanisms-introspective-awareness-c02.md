---
id: 2026-macar-mechanisms-introspective-awareness-c02
statement: "Neither base model tested discriminates injected from control trials (Gemma3-27B base at layer 37: 42.3% false positives against 39.5%–41.7% true positives for strengths ≤4; OLMo-3.1-32B base: 16.4% false positives against 0.1% true positives), and across OLMo-3.1-32B's training pipeline the base and SFT checkpoints show high false positive rates that fall to 0% only after DPO, while OLMo's detection rate also falls, to 2.9% after DPO and 0.9% in the final instruct checkpoint."
bucket: narrowing
evidence_type: scored-self-answer
kind: measurement
source: 2026-macar-mechanisms-introspective-awareness
locator: "§3.3 The Role of Post-Training, Figure 4 left; Appendix C, Figure 21"
quote: "We observe similar patterns for OLMo-3.1-32B ( Appendix C ): both the base and SFT checkpoints exhibit high FPR, and only after DPO does it drop to 0%."
verification: grep
models: ["Gemma3-27B base", "Gemma3-27B instruct", "OLMo-3.1-32B base, SFT, DPO and instruct checkpoints"]
publisher_relation: mixed
replication: none-retrieved
not_evidence_of: "Paper: Not evidence that DPO produces detection: in OLMo-3.1-32B, SFT gives the highest true positive rate (14.9%, with 22.5% false positives) and DPO removes false positives while detection drops to 2.9%; Paper: Not evidence about which ingredient of Gemma's post-training matters, since Gemma's intermediate checkpoints were not tested; Paper: Not evidence that post-training creates the whole circuit: the authors cannot resolve whether upstream evidence carriers are pre-existing structure that post-training learns to leverage; Paper: The authors state that their results 'should not be interpreted as evidence of subjective experience or consciousness in LLMs' (Ethics Statement); Framework (test 9, steering): a coupling measured under steering shows that the channel can be steered and does not weight reports offered in ordinary operation"
bears_on: [9.t9, 5.A2, 3.2]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: "google/gemini-3.1-pro-preview 2026-10-06 (scope check) agree; notes: none", council: "dossier-rewrite 2026-10-06 | self-answer-type 2026-10-14", adjudicated: "2026-10-06 Ben: rewrite applied after council round 2 (GPT proposal as amended by the checkers; experience-exclusion rule) | 2026-10-14 Ben: evidence type interpretability to scored-self-answer (council round 4, eight of ten; the filing half of Q3 decided, the access half stays open)"}
added: 2026-09-28
changed: 2026-10-14
---

The authors summarise: "The capability is absent in base models, emerges from post-training" (§1), and for OLMo: "base models cannot discriminate, post-training eliminates false positives, but the same stages that improve reliability may also suppress true detection through refusal-like mechanisms" (Appendix C). Full OLMo figures (Appendix C, aggregated over five layers and four strengths): base 0.1% TPR / 16.4% FPR; SFT 14.9% / 22.5%; DPO 2.9% / 0%; instruct 0.9% TPR / 0% FPR, 0.3% introspection rate. Note that the §3.3 prose says OLMo base shows "high FPR" while Appendix C gives near-zero detection for it, so OLMo base does not repeat Gemma base's pattern of high detection with equal false positives; what both share is no discrimination. The mechanistic companion to this result (the gate feature's inverted-V pattern is "substantially weaker in the base model", and the base model shows no L45 localisation) is in c03.

The intake brief asked for this claim as "emerges from post-training; DPO elicits, SFT does not". The held text does not support "DPO elicits": in OLMo, DPO is the stage at which false positives disappear, and detection there is near zero. The claim is written to what the text says.

REPLICATES: 2025-anthropic-emergent-introspective-awareness — the §5.7 finding that base pretrained models "generally have a fairly high false positive rate, and none of them achieve greater-than-zero net task performance" (not filed as its own claim in that intake). The same holds here for Gemma3-27B base and OLMo-3.1-32B base, outside the Claude family. Independence: partial only; the replicated paper's author is an advising author here. The training-stage split (SFT vs DPO) goes beyond Lindsey 2025, which could not separate pretraining from post-training effects (its footnote 11).

SECOND QUOTE (§3.3 The Role of Post-Training): "Base models cannot discriminate. We test whether introspection exists in base models as well." and "We find that the base model has both high FPR (42.3%) and comparable TPR (39.5%–41.7% for \alpha\leq 4 ), indicating no discrimination between injected and control trials"

SECOND QUOTE (Appendix C): "near-zero detection (0.1% TPR) with 16.4% false positive rate" and "This progression mirrors the pattern observed in Gemma3-27B"

REWRITE 2026-10-06

- Statement changed. GPT proposed cutting the lead finding to "Gemma3-27B base has 42.3% false positives ..."; the checker (NEITHER) found the finding is the paper's own (§3.3 heading "Base models cannot discriminate."; Appendix C) but that the original stated it as a general law about "Base models" when two were tested. Applied the checker's wording: "Neither base model tested discriminates ...", with the OLMo-3.1-32B base rates (Appendix C) added so both tested models are named. ERROR FOUND (checker, in both versions): the Gemma3-27B base true positive range 39.5%–41.7% holds for strengths ≤4 at layer 37; condition added. Council 8 of 9 on the checker's wording (Gemini, which wrongly believed it was GPT's author, kept GPT's statement). Ben's instruction confirmed this scoping. "Discriminates" is a measurement verb (council Q5, Meta and Kimi).
- Note, not applied: Qwen (one seat) asked that the claim say no discrimination statistic is reported. True per the checker (no d', AUC or test; the basis is true and false positive rates side by side, and the OLMo rates are aggregated over five layers and four strengths). Recorded here, not added to the field, since neither the checker's edits nor Ben's instruction include it.
- Clause reworded under the experience-exclusion rule (council 9 of 9; Ben): "Not evidence of experience, or that training instilled anything experiential" became the paper's own Ethics Statement words with locator. The tail "or that training instilled anything experiential" is not stated by the paper and is deleted, not replaced.
- Other clauses kept (GPT KEEP; checker confirmed SFT 14.9%/22.5%, DPO 2.9%, and the unresolved evidence-carrier question, §8.1; "Gemma's intermediate checkpoints were not tested" is a design fact). Steering framework sentence kept (R3).
- kind: measurement (true and false positive rates across base models and training checkpoints).

EVIDENCE TYPE 2026-10-14 (council round 4; Ben's decision the same day): interpretability to scored-self-answer. The model was asked about itself and its answer scored against a fact the experimenters set; the value records that design and decides nothing about self-access (research/README.md, "Scored self-answers"). Before this the type followed the extractor: the same design was interpretability in three papers and behavioural in two. Framework sentence unchanged.
