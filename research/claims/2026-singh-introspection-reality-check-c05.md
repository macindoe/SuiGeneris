---
id: 2026-singh-introspection-reality-check-c05
statement: "When given an explicit third response option for prompt-level manipulation, the open-weight models that reproduce the Lindsey (2025) two-way effect fail to separate prompt-level from activation-level interventions: Llama-3.1-70B performs near chance with probability concentrated on the activation-intervention option, Qwen-3-32B shows a strong preference for the control response, and Gemma-3-27B-IT also fails."
bucket: narrowing
evidence_type: behavioural
source: 2026-singh-introspection-reality-check
locator: "§4.3.2 (Results); Fig. 3b; App. F; App. G.2, G.3; App. K, L (Figs. 6, 7)"
quote: "given an explicit input intervention response option, Llama-3.1-70B performs near chance, with probability concentrated disproportionately on the activation-intervention option"
verification: grep
models: [Llama-3.1-70B-Instruct, Qwen-3-32B, Gemma-3-27B-IT, Llama-3.1-8B-Instruct]
publisher_relation: independent
replication: none-retrieved
not_evidence_of: "Paper: Not evidence that these models, or Claude models, lack introspective access: the authors say models 'could likely be trained to separate the two interventions' and that they do not conclude the models 'demonstrably lack introspective capacities'; Paper: Failing the three-way test is also not the converse of a pass meaning introspection: the authors state a model passing it 'would still not thereby be shown to deploy meta-representations'; Paper: Nothing about experience or moral status"
bears_on: [9.t9, 5.A2]
contests: [2025-anthropic-emergent-introspective-awareness-c01, 2025-anthropic-emergent-introspective-awareness-c03]
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: "x-ai/grok-4.6 2026-09-25 agree; notes: bears_on +3.2; models over-includes Llama-3.1-8B-Instruct (App. K: does not clearly reproduce)", council: none, adjudicated: none}
added: 2026-09-25
changed: 2026-09-26
---

CONTESTS: 2025-anthropic-emergent-introspective-awareness — the reading of injected-thought detection as awareness of interventions on internal states specifically; the authors argue the pattern is "fully accounted for by a generic sensitivity to irregularity". Tested on open-weight models only; Lindsey's Claude results were not re-run.

The authors report that across all prompt wordings where a model passes the two-way reproduction criterion, it fails the three-way setting (App. F). Standard deviations are across concepts and detection varies considerably by concept (App. R). Limitation stated by the authors (App. A): these experiments "test a strictly weaker condition" than second-order computation. Small internal inconsistency in the paper, recorded not resolved: the Introduction says "four open-weight models", §4.3.1 lists five, and the Discussion says "two of the three models we tested replicate".
