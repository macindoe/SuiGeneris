---
id: 2026-singh-introspection-reality-check-c01
statement: "In the supervised self-report classification paradigm of Ji-An et al. (2025), Llama-3.1-8B-Instruct's in-context accuracy on probe-derived labels falls to close to the majority-class baseline once the probe is trained on randomly permuted labels, so that the labels no longer carry the input's semantics (similar results reported for Llama-3.1-70B-Instruct and Qwen-2.5-7B-1M)."
bucket: narrowing
evidence_type: behavioural
source: 2026-singh-introspection-reality-check
locator: "§4.1.2 (Models struggle to predict proxies decorrelated from semantics); Fig. 2a; App. N (Fig. 9, Fig. 10)"
quote: "accuracy on the arbitrary direction defined by a probe trained on randomly relabeled data drops to close to the majority-class baseline"
verification: grep
models: [Llama-3.1-8B-Instruct, Llama-3.1-70B-Instruct, Qwen-2.5-7B-1M]
publisher_relation: independent
replication: none-retrieved
not_evidence_of: "Not evidence that these models lack introspection or privileged access in general: it shows only that the Ji-An et al. supervised paradigm, as deployed, does not establish privileged access, because success there is consistent with in-context learning of semantic regularities in the input. The authors state it does not show that no version of the paradigm could satisfy the condition. Says nothing about experience, feelings, or moral status, and nothing about Claude models, which were not tested."
bears_on: [9.t9, 5.A2]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: none, council: none, adjudicated: none}
added: 2026-09-25
changed: 2026-09-25
---

The authors keep the Ethics (commonsense) data but permute the labels before training the logistic-regression probe, giving an arbitrary but well-formed hidden-state direction that the model could in principle predict. Accuracy on the original, semantically aligned labels is well above chance; on the permuted-label direction it drops to near the majority baseline. They read this as: "Performance in the original paradigm therefore need not require access to the model's hidden states".

Limitation stated by the authors (App. A): the control "suffices to show that the reported results do not require privileged access. It does not show that no version of these paradigms could satisfy the privileged-access condition."

Contests Ji-An et al. (2025), not Lindsey (2025); Ji-An et al. is not in the library as of 25 Sep 2026.
