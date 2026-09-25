---
id: 2026-singh-introspection-reality-check-c02
statement: "In the unsupervised (PCA) variant of the Ji-An et al. (2025) paradigm, linear probes trained only on mean-pooled layer-0 input representations of Llama-3.1-8B-Instruct (and Llama-3.1-70B-Instruct) closely track or exceed the model's own in-context prediction of the PCA-derived labels, indicating the task can be solved from input-embedding features alone."
bucket: narrowing
evidence_type: behavioural
source: 2026-singh-introspection-reality-check
locator: "§4.1.2 (PCA-derived labels are linearly predictable from input features); Fig. 2b; App. N (Fig. 9); App. O"
quote: "indicating that the task can be solved from input-embedding features alone, without privileged access to any layer's activations"
verification: grep
models: [Llama-3.1-8B-Instruct, Llama-3.1-70B-Instruct]
publisher_relation: independent
replication: none-retrieved
not_evidence_of: "Not evidence that the models have no access to their own activations: an input-only classifier matching the model shows the task does not require privileged access, not that the model lacks it. Not evidence about introspection in any other paradigm, in Claude models, or about experience or moral status of any kind."
bears_on: [9.t9, 5.A2]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: "x-ai/grok-4.6 2026-09-25 agree", council: none, adjudicated: none}
added: 2026-09-25
changed: 2026-09-25
---

Probes are fitted on layer-0 (uncontextualised) representations to predict the binary-clustered principal-component labels of each hidden layer, averaged across layers; the authors report the first principal component and say other components are similar. They also argue (same section) that Ji-An et al.'s neural-control result inherits the same confound.

Limitation stated by the authors (App. A): matching the model's accuracy with an input-only probe "does not show that no version of these paradigms could satisfy the privileged-access condition." App. N notes the original sample sizes give an under-determined system (fewer samples than hidden size); a reviewer-requested larger-sample variant was run only on Qwen-2.5-7B-1M for the supervised (LR) arm.

Contests Ji-An et al. (2025), not Lindsey (2025).
