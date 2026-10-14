---
id: 2026-anthropic-assistant-axis-c01
statement: "The authors interpret their results on Gemma 2 27B, Qwen 3 32B and Llama 3.3 70B as suggesting that post-training steers models toward a particular region of persona space (the Assistant end of the Assistant Axis) but only loosely tethers them to it."
bucket: open
evidence_type: interpretability
kind: interpretation
report_class: none
ground_truth: none
source: 2026-anthropic-assistant-axis
locator: "Abstract; paraphrased in §7 (only loosely tethered); cf. §9 (somewhat fragile)"
quote: "Our results suggest that post-training steers models toward a particular region of persona space but only loosely tethers them to it"
verification: grep
models: [Gemma 2 27B, Qwen 3 32B, Llama 3.3 70B]
publisher_relation: mixed
replication: none-retrieved
not_evidence_of: "Paper: The axis is a linear direction in activations, and the authors write that 'the assumption that the Assistant persona corresponds to a linear direction in activation space is likely flawed' (§8.1); Paper: Not evidence about frontier models or about any Anthropic model (none was measured); Paper: This is an interpretation the authors draw (suggest), not a single measurement"
bears_on: [4.endorsement, 3.2]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: "deepseek/deepseek-v4-pro-0813 2026-09-25 agree | openai/gpt-5.6-sol 2026-10-06 (scope check) agree; notes: none", council: "research-docket 2026-09-26", adjudicated: "2026-10-06 Ben: experience-exclusion rule applied library-wide; this claim was not in the dossiers the council reviewed"}
added: 2026-09-25
changed: 2026-10-15
---

The authors' summary interpretation, built on the steering results (§3.2), the drift trajectories (§4) and the capping results (§5). It is bucketed `open` because it is a generalisation the source draws, not one measurement. The conclusion adds that "The model’s position along the Assistant Axis is somewhat fragile." Stated limitations: the targets are non-frontier dense models; the linear-direction assumption "is likely flawed"; the multi-turn conversations were simulated.

REWRITE 2026-10-06 (experience-exclusion rule applied library-wide by Ben's decision; this claim was not in the dossiers the council reviewed, so there is no GPT proposal, checker or council finding behind it)
- Statement: unchanged.
- Clause 'Not evidence that the Assistant persona, or any persona on the axis, is an experiencer or a bearer of interests, preferences or anything else' deleted (Ben's experience-exclusion rule, R2): the held text states no limit about experience, consciousness, sentience, welfare or moral status for this result. Its second half, the linear-direction limit, is a design limit the paper states, so it is kept as its own clause, now in the paper's words with locator (§8.1).
- Clause 'The loose-tethering finding is not evidence of a stable standpoint in the North Star §4 sense, and not evidence of its absence: ...' deleted (R2): it invokes the project's own framework (North Star §4), so it is not the paper's limit.
- Kept unchanged: the frontier/Anthropic-models clause and the interpretation-not-measurement clause (design limits).
- kind: interpretation (the statement reports the authors' summary reading ('Our results suggest')).
