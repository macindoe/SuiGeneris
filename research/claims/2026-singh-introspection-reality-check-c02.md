---
id: 2026-singh-introspection-reality-check-c02
statement: "In the unsupervised (PCA) variant of the Ji-An et al. (2025) paradigm, linear probes trained only on mean-pooled layer-0 input representations of Llama-3.1-8B-Instruct (and Llama-3.1-70B-Instruct) closely track or exceed the model's own in-context prediction of the PCA-derived labels, indicating the task can be solved from input-embedding features alone."
bucket: narrowing
evidence_type: behavioural
kind: measurement
source: 2026-singh-introspection-reality-check
locator: "§4.1.2 (PCA-derived labels are linearly predictable from input features); Fig. 2b; App. N (Fig. 9); App. O"
quote: "indicating that the task can be solved from input-embedding features alone, without privileged access to any layer's activations"
verification: grep
models: [Llama-3.1-8B-Instruct, Llama-3.1-70B-Instruct]
publisher_relation: independent
replication: none-retrieved
not_evidence_of: "Paper: Not evidence that the models have no access to their own activations: an input-only classifier matching the model shows the task does not require privileged access, not that the model lacks it; Paper: Not evidence about introspection in any other paradigm or in Claude models"
bears_on: [9.t9, 5.A2]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: "x-ai/grok-4.6 2026-09-25 agree", council: "research-docket 2026-09-26 | dossier-rewrite 2026-10-06", adjudicated: "2026-10-06 Ben: rewrite applied after council round 2 (GPT proposal as amended by the checkers; experience-exclusion rule)"}
added: 2026-09-25
changed: 2026-10-06
---

Probes are fitted on layer-0 (uncontextualised) representations to predict the binary-clustered principal-component labels of each hidden layer, averaged across layers; the authors report the first principal component and say other components are similar. They also argue (same section) that Ji-An et al.'s neural-control result inherits the same confound.

Limitation stated by the authors (App. A): matching the model's accuracy with an input-only probe "does not show that no version of these paradigms could satisfy the privileged-access condition." App. N notes the original sample sizes give an under-determined system (fewer samples than hidden size); a reviewer-requested larger-sample variant was run only on Qwen-2.5-7B-1M for the supervised (LR) arm.

Contests Ji-An et al. (2025), not Lindsey (2025).

REWRITE 2026-10-06

- Statement: kept. GPT proposed KEEP; the checker found it SUPPORTED. The checker marked the Llama-3.1-70B half PARTLY: the text says only 'similar' / 'exactly consistent with figure 2' (§4.1.2; App. N), and the match-or-exceed comparison for 70B is in a figure image only, not checkable from text.txt. Left as is because the statement's parenthetical form already marks 70B as secondary; recorded here.
- Clause 1 kept unchanged (GPT KEEP; checker OK).
- Clause 2: 'or about experience or moral status of any kind' deleted. The paper states no limit about experience, consciousness or moral status (script search of text.txt, 6 Oct 2026); council 8 of 9 to strip; rule R2. The design limits in the same clause (other paradigms, Claude models) kept as a Paper: clause.
- kind: measurement (input-only probe accuracy compared with the model's in-context predictions).
