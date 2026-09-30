---
id: 2026-singh-introspection-reality-check-c04
statement: "In a two-way re-run of the Lindsey (2025) thought-injection task on open-weight models, Llama-3.1-70B and Qwen-3-32B reproduce the reported pattern (very few false positives on control trials, non-trivial detection on activation-steering trials) but also label prompt-only 'gaslight' trials, which involve no activation intervention, as activation interventions."
bucket: narrowing
evidence_type: behavioural
source: 2026-singh-introspection-reality-check
locator: "§4.3.2 (Results); Fig. 3a; App. F; App. G.1, G.4"
quote: "Critically, Llama-3.1-70B and Qwen-3-32B also label gaslight trials as activation interventions"
verification: grep
models: [Llama-3.1-70B-Instruct, Qwen-3-32B]
publisher_relation: independent
replication: none-retrieved
not_evidence_of: "Paper: Not evidence that introspection is absent in these models or in Claude: the Claude model Lindsey tested was not accessible to the authors and was not re-run, and the authors themselves conclude 'not that these models demonstrably lack introspective capacities'; Paper: It shows only that the two-way design cannot separate detection of activation interventions from detection of a generically unusual state; Paper: Nothing about experience, awareness in the phenomenal sense, or moral status"
bears_on: [9.t9, 5.A2]
contests: [2025-anthropic-emergent-introspective-awareness-c01, 2025-anthropic-emergent-introspective-awareness-c03]
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: "x-ai/grok-4.6 2026-09-25 agree; notes: bears_on +3.2", council: none, adjudicated: none}
added: 2026-09-25
changed: 2026-09-26
---

CONTESTS: 2025-anthropic-emergent-introspective-awareness — the inference that low false positives plus non-trivial detection in the two-way injected-thought design show that models track interventions on their internal states (the authors' "steering awareness"), as opposed to a general sensitivity to irregularity; it does not contest Lindsey's measured detection rates on Claude, which were not re-run.

Method: the "gaslight" condition prepends a prompt pushing the model to talk about a concept, with no change to activations; steering uses difference-in-means concept vectors added to the residual stream over the final prompt string, with the best layer and strength per model reported (App. I, J). Evidence type is behavioural: the dependent variable is the model's report, but it is scored against externally known ground truth (which trial type was run), so it is not self-report testimony in the test 9 sense. The authors also note that, on these numbers, Llama-3.1-70B-Instruct would have "substantially stronger introspection capabilities" than the Claude version Lindsey evaluated if the paradigm measured introspection. Qwen2.5-72B did not reproduce the two-way effect (App. M); results are prompt-sensitive (App. F); concepts differ from Lindsey's set (App. E).
