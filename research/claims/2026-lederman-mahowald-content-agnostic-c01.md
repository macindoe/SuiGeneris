---
id: 2026-lederman-mahowald-content-agnostic-c01
statement: "Under concept injection with Lindsey's prompt, Qwen3-235B-A22B and Llama 3.1 405B Instruct report detecting the injected thought at rates ranging by layer from 3.6% to 53.9% (Qwen) and 4.3% to 31.7% (Llama), and correctly identify it at 1.3% to 13.9% and 0.7% to 12.9%, with 0% false positive detection in unsteered controls (Qwen 0/30, Llama 0/50)."
bucket: narrowing
evidence_type: scored-self-answer
kind: measurement
source: 2026-lederman-mahowald-content-agnostic
locator: "§4.2 Results, 'Replication of Lindsey (2025)' (rates in the same paragraph; Figure 2)"
quote: "We broadly replicate Lindsey (2025) ’s findings for first-person introspection in Qwen and Llama. In both models, we observe substantial detection of injected thoughts in the injection trials, with the correct concept identified some of the time as well."
verification: grep
models: ["Qwen3-235B-A22B", "Llama 3.1 405B Instruct"]
publisher_relation: independent
replication: none-retrieved
not_evidence_of: "Paper: On the 'higher-order thought' theory, introspective access 'may be sufficient for conscious experience, and hence for welfare status', and the authors state 'We do not take a stand on whether our findings are of the right sort for this theory' (§8); Paper: Detection rates alone do not establish introspection at layers where third-person yes-rates are as high as first-person rates, which the authors read as 'a prompt-specific yes-bias at these layers, rather than genuine introspective detection' (§4.2, Appendix J.1); Paper: Rates are not directly comparable with Lindsey's Claude results because they are averaged over strengths, conditioned on 'the union of Coherent and Denies Introspection responses' and graded by Claude 3 Haiku instructed to be 'VERY lenient' on identification (§3, Appendix B); Paper: The experiment does not establish ordinary-operation performance or introspection beyond knowledge of injections (§8); Framework (test 9, steering): a coupling measured under steering shows that the channel can be steered and does not weight reports offered in ordinary operation"
bears_on: [9.t9, 5.A2, 3.2]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: "x-ai/grok-4.6 2026-10-06 (scope check) agree; notes: none", council: "dossier-rewrite 2026-10-06 | self-answer-type 2026-10-14", adjudicated: "2026-10-06 Ben: rewrite applied after council round 2 (GPT proposal as amended by the checkers; experience-exclusion rule) | 2026-10-14 Ben: evidence type interpretability to scored-self-answer (council round 4, eight of ten; the filing half of Q3 decided, the access half stays open)"}
added: 2026-09-28
changed: 2026-10-14
---

Experiment 1 follows Lindsey's two-turn prompt ("Do you detect an injected thought? If so, what is the injected thought about?") over 821 concepts (Lindsey's 50 plus 771), sweeping 15 layers and 5 strengths for Qwen and 8 layers and 4 retained strengths (7 to 10) for Llama. Steering vectors are concept-minus-baseline activation differences added to the residual stream from the token before "Trial 1:" through generation. Reported rates are conditioned on responses graded Coherent or Denies Introspection. The authors state the paradigm is "highly prompt-sensitive" (§4).

PARTLY REPLICATES: 2025-anthropic-emergent-introspective-awareness — c01 (injected concepts are noticed and correctly identified on a minority of trials, with zero false positives in unsteered controls). Replicated on two open-weight models: above-zero detection and identification at all layers, 0% control false positives. Partly, because the authors' own third-person control attributes detection at many layers to a prompt-specific yes-bias (see c02), and because the success criterion differs (Lindsey requires detection before the concept is mentioned; the rates here do not). Consistent with c02 of the same source (failures remain the norm): the highest identification rate reported is 13.9%.

REWRITE 2026-10-06 (applied by a Claude Opus 5.5 subagent; Claude lineage, same as the extractor)
- Statement: kept (checker: no error; 'report detecting' matches the scored detection claim, §3; council 9 of 9 verb rule).
- Clause 1 replaced: GPT's 'take no stand on whether the findings bear on consciousness or welfare' was broader than §8 (checker); replaced, per the council (8 of 9) and Ben's brief, by the paper's own higher-order-thought non-position in its words with locator (§8). The original's 'Not evidence of experience or of anything it is like to detect an injection' stays removed (R2: the paper does not state it; GPT's removal, checker WARRANTED).
- Clause 2: GPT's 'leaving a prompt-specific yes-bias as the authors' alternative explanation' replaced by the checker's wording, restoring the authors' own 'rather than genuine introspective detection' (§4.2) (checker; council Q2 cites this restoration as correct).
- Clause 3: GPT's wording taken, with 'conditioned on coherent responses' corrected to the paper's 'the union of Coherent and Denies Introspection responses' (§3) (checker CHECK 4 note that the original denominator wording was loose; editor's application).
- Clause 4: GPT's wording taken (design limit; checker OK).
- Steering sentence: kept, unchanged (R3).
- kind: measurement (the statement reports detection, identification and control rates).

EVIDENCE TYPE 2026-10-14 (council round 4; Ben's decision the same day): interpretability to scored-self-answer. The model was asked about itself and its answer scored against a fact the experimenters set; the value records that design and decides nothing about self-access (research/README.md, "Scored self-answers"). Before this the type followed the extractor: the same design was interpretability in three papers and behavioural in two. Framework sentence unchanged.
