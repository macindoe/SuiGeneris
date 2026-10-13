---
id: 2026-singh-introspection-reality-check-c01
statement: "In the supervised self-report classification paradigm of Ji-An et al. (2025), Llama-3.1-8B-Instruct's in-context accuracy on probe-derived labels falls to close to the majority-class baseline once the probe is trained on randomly permuted labels, so that the labels no longer carry the input's semantics (similar results reported for Llama-3.1-70B-Instruct and Qwen-2.5-7B-1M)."
bucket: narrowing
evidence_type: behavioural
kind: measurement
source: 2026-singh-introspection-reality-check
locator: "§4.1.2 (Models struggle to predict proxies decorrelated from semantics); Fig. 2a; App. N (Fig. 9, Fig. 10)"
quote: "accuracy on the arbitrary direction defined by a probe trained on randomly relabeled data drops to close to the majority-class baseline"
verification: grep
models: [Llama-3.1-8B-Instruct, Llama-3.1-70B-Instruct, Qwen-2.5-7B-1M]
publisher_relation: independent
replication: none-retrieved
not_evidence_of: "Paper: Not evidence that these models lack introspection or privileged access in general: it shows only that the Ji-An et al. supervised paradigm, as deployed, does not establish privileged access, because success there is consistent with in-context learning of semantic regularities in the input; Paper: The authors state it does not show that no version of the paradigm could satisfy the condition; Paper: Says nothing about Claude models, which were not tested"
bears_on: [9.t9, 5.A2]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: "x-ai/grok-4.6 2026-09-25 agree | google/gemini-3.1-pro-preview 2026-10-06 (scope check) agree; notes: none", council: "research-docket 2026-09-26 | dossier-rewrite 2026-10-06 | self-answer-type 2026-10-14 (boundary case Q5)", adjudicated: "2026-10-06 Ben: rewrite applied after council round 2 (GPT proposal as amended by the checkers; experience-exclusion rule) | 2026-10-14 Ben: outside the scored-self-answer class (council 6 of 10 out, 4 in): the truth is a label derived from a probe on the model, not a fact the experimenters imposed or hold independently of it; type stays behavioural"}
added: 2026-09-25
changed: 2026-10-06
---

The authors keep the Ethics (commonsense) data but permute the labels before training the logistic-regression probe, giving an arbitrary but well-formed hidden-state direction that the model could in principle predict. Accuracy on the original, semantically aligned labels is well above chance; on the permuted-label direction it drops to near the majority baseline. They read this as: "Performance in the original paradigm therefore need not require access to the model's hidden states".

Limitation stated by the authors (App. A): the control "suffices to show that the reported results do not require privileged access. It does not show that no version of these paradigms could satisfy the privileged-access condition."

Contests Ji-An et al. (2025), not Lindsey (2025); Ji-An et al. is not in the library as of 25 Sep 2026.

REWRITE 2026-10-06

- Statement: kept. GPT proposed KEEP; the checker found it SUPPORTED (permuted-label design §4.1.1; Llama-3.1-70B and Qwen-2.5-7B-1M in App. N, the Qwen run being the LR arm only, as above).
- Clauses 1 and 2 kept unchanged (GPT KEEP; checker OK).
- Clause 3: experience part deleted ('experience, feelings, or moral status'). The paper states no limit about experience, consciousness or moral status anywhere (script search of text.txt, 6 Oct 2026: the only such words are in reference titles and in App. C.2, where the authors report that another paper disclaims the conscious-awareness reading); council 8 of 9 to strip; rule R2. The design limit in the same clause (Claude models not tested) kept as a Paper: clause, reworded only to drop the deleted half.
- kind: measurement (in-context accuracy on permuted-label probe directions).

BOUNDARY 2026-10-14 (council round 4, Q5; Ben's decision): this claim was one of the brief's test cases for the new evidence type scored-self-answer. Six seats put it outside the class because the ground truth is probe-derived (read from the model) rather than imposed by the experimenters or held independently of the answer; four put it inside. Ben: outside. Type unchanged.
