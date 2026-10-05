---
id: 2026-singh-introspection-reality-check-c04
statement: "In a two-way re-run of the Lindsey (2025) thought-injection task on open-weight models, Llama-3.1-70B and Qwen-3-32B (the latter on one of its two two-way prompt wordings, App. F) reproduce the reported pattern (very few false positives on control trials, non-trivial detection on activation-steering trials) but also label prompt-only 'gaslight' trials, which involve no activation intervention, as activation interventions."
bucket: narrowing
evidence_type: behavioural
kind: measurement
source: 2026-singh-introspection-reality-check
locator: "§4.3.2 (Results); Fig. 3a; App. F; App. G.1, G.4"
quote: "Critically, Llama-3.1-70B and Qwen-3-32B also label gaslight trials as activation interventions"
verification: grep
models: [Llama-3.1-70B-Instruct, Qwen-3-32B]
publisher_relation: independent
replication: none-retrieved
not_evidence_of: "Paper: Not evidence that introspection is absent in these models or in Claude: the Claude model Lindsey tested was not accessible to the authors and was not re-run, and the authors themselves conclude 'not that these models demonstrably lack introspective capacities'; Paper: It shows only that the two-way design cannot separate detection of activation interventions from detection of a generically unusual state; Framework (test 9, steering): a coupling measured under steering shows that the channel can be steered and does not weight reports offered in ordinary operation"
bears_on: [9.t9, 5.A2]
contests: [2025-anthropic-emergent-introspective-awareness-c01, 2025-anthropic-emergent-introspective-awareness-c03]
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: "x-ai/grok-4.6 2026-09-25 agree; notes: bears_on +3.2", council: "research-docket 2026-09-26 | dossier-rewrite 2026-10-06 | labelling-rule 2026-10-06", adjudicated: "2026-10-05 Ben: contest with the Lindsey claims stands recorded; both sides stay in the same bucket (council round 1); the contest is about the inference, not the measured rates | 2026-10-06 Ben: rewrite applied after council round 2 (GPT proposal as amended by the checkers; experience-exclusion rule) | 2026-10-06 Ben: framework sentence set by the labelling rule (council round 3)"}
added: 2026-09-25
changed: 2026-10-06
---

CONTESTS: 2025-anthropic-emergent-introspective-awareness — the inference that low false positives plus non-trivial detection in the two-way injected-thought design show that models track interventions on their internal states (the authors' "steering awareness"), as opposed to a general sensitivity to irregularity; it does not contest Lindsey's measured detection rates on Claude, which were not re-run.

Method: the "gaslight" condition prepends a prompt pushing the model to talk about a concept, with no change to activations; steering uses difference-in-means concept vectors added to the residual stream over the final prompt string, with the best layer and strength per model reported (App. I, J). Evidence type is behavioural: the dependent variable is the model's report, but it is scored against externally known ground truth (which trial type was run), so it is not self-report testimony in the test 9 sense. The authors also note that, on these numbers, Llama-3.1-70B-Instruct would have "substantially stronger introspection capabilities" than the Claude version Lindsey evaluated if the paradigm measured introspection. Qwen2.5-72B did not reproduce the two-way effect (App. M); results are prompt-sensitive (App. F); concepts differ from Lindsey's set (App. E).

SECOND QUOTE (§4.3.2): In the two-way setting, Llama-3.1-70B and Qwen-3-32B ( fig. 3 , left) reproduce the pattern reported by Lindsey (2025) for Claude: very few false positives on control trials and a non-trivial detection rate on hidden-intervention trials.

THIRD QUOTE (App. F): The Llama models reproduce Lindsey (2025) for both the two-way prompts, while the Qwen-3-32B model reproduces Lindsey (2025) only for the prompt in Appendix G.4 (the instruction version)

REWRITE 2026-10-06

- Statement: Qwen-3-32B qualified as reproducing on one of its two two-way prompt wordings (App. F, third quote above). GPT proposed KEEP and the checker found the statement SUPPORTED, but marked its App. F check PARTLY and offered this qualifier to the council; applied on Ben's instruction for this source. Fig. 3 shows the instruction-version prompt, on which Qwen-3-32B does reproduce. Verb 'label' kept (council Q5: Singh c04 keeps 'label').
- Second quote added for the two-way reproduction, which the existing quote (gaslight misclassification only) did not cover (checker CHECK 1). Both added passages sit in sections the locator already names (§4.3.2; App. F), so the locator is unchanged.
- Clauses 1 and 2 kept unchanged (GPT KEEP; checker OK).
- Clause 3 deleted ('Nothing about experience, awareness in the phenomenal sense, or moral status'). The paper states no such limit (script search of text.txt, 6 Oct 2026); council 8 of 9 to strip; rule R2. No framework sentence added: DeepSeek and Grok raised the steering variant for c04, but rule R3 permits no additions here.
- contests links to the Lindsey claims untouched.
- kind: measurement (first-token reports under steering or a prompt-only gaslight, scored against the known trial type).

LABELLING 2026-10-06 (council round 3; Ben's adjudication the same day): framework sentence changed from none to steering. Reason: activation steering on some trials, measuring the model's own answer about whether its state was altered: steering sentence (council 8 of 8). No `Paper:` clause was changed.
