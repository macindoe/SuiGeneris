---
id: 2026-singh-introspection-reality-check-c03
statement: "For the Belief Dominance framework of Steinmetz Yalon et al. (2026), linear probes given only the uncontextualised layer-0 embeddings of two entities match or surpass the in-context performance reported for Llama-3-70B and Gemma-3-27B on predicting Belief Dominance cluster labels."
bucket: narrowing
evidence_type: behavioural
source: 2026-singh-introspection-reality-check
locator: "§4.2.2 (Belief Dominance labels are linearly predictable from input features); Table 1; App. S (Table 6)"
quote: "linear probes that only have access to the entities’ uncontextualized embeddings match or surpass the models’ in-context performance on the BD prediction task"
verification: grep
models: [Llama-3-70B, Gemma-3-27B]
publisher_relation: independent
replication: none-retrieved
not_evidence_of: "Not evidence that these models cannot monitor their own belief conflicts; only that the Belief Dominance task as published is solvable from entity properties without privileged access. The authors' explanation (entity frequency) is a stated hypothesis, not a finding. Not evidence about Claude models, and nothing about experience or moral status."
bears_on: [9.t9, 5.A2]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: "x-ai/grok-4.6 2026-09-25 agree", council: none, adjudicated: none}
added: 2026-09-25
changed: 2026-09-25
---

Probes see only the embeddings of subject + counter entity, or base + counter entity, with no other prompt content and no signal of a belief conflict; the in-context (ICL) figures are Steinmetz Yalon et al.'s published numbers, not re-run. On a balanced test set (App. S) the models are above the 0.33 majority baseline but "often at par or worse than" the probes. The authors "hypothesize" entity frequency as the driver, and argue the companion steering result shows causal efficacy of the representation, not introspective access to it.

Limitation stated by the authors (App. A): the probe result shows the reported results "do not require privileged access" but "does not show that no version of these paradigms could satisfy the privileged-access condition."

Contests Steinmetz Yalon et al. (2026), not Lindsey (2025).
