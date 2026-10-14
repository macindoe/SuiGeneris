---
id: 2024-anthropic-scaling-monosemanticity-c01
statement: "Among the features extracted by sparse autoencoders (about 1M, 4M and 34M features) trained on the middle-layer residual stream of Claude 3 Sonnet are features that the authors label, from the contexts in which they activate, as related to lying, deception and power-seeking (including treacherous turns), among them features for influence and manipulation, coups and treacherous turns, biding time and hiding strength, and secrecy or discreetness."
bucket: narrowing
evidence_type: interpretability
kind: measurement
report_class: none
ground_truth: none
source: 2024-anthropic-scaling-monosemanticity
locator: "Opening summary (third paragraph); section 'Deception, Power-seeking and Manipulation-related Features' (feature list)"
quote: "lying, deception, and power-seeking (including treacherous turns)"
verification: grep
models: ["Claude 3 Sonnet (3.0, finetuned production model)"]
publisher_relation: developer-of-studied-model
replication: none-retrieved
not_evidence_of: "Paper: The labels are the authors' interpretations of activating examples ('these interpretations were made based only on the contexts in which the feature activates', Influence on Behavior), and the authors allow that 'our feature interpretations slightly misrepresent the feature's actual function' (Specificity); Paper: The authors caution that the existence of such features does not show lying: 'there's a difference (for example) between knowing about lies, being capable of lying, and actually lying in the real world' (opening summary; see c03); Paper: The SAEs were trained on one middle layer, on text that 'did not include any “Human:” / “Assistant:” formatted data that we finetune Claude to operate on', and the authors do not believe they found 'anywhere near “all the features”' (Limitations)"
bears_on: [5.A2]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: "x-ai/grok-4.7 2026-10-15 (scope check) agree; notes: exclusion quotes drawn from a different feature set", council: none, adjudicated: none}
added: 2026-10-15
changed: 2026-10-15
---

The source of the word "features" in Anchor 2 claim (a). Feature identifiers as printed: self-improving AI 34M/18151534, influence and manipulation 34M/21750411, coups and treacherous turns 34M/29589962, biding time and hiding strength 34M/24580545, secrecy or discreetness 1M/268551. The authors also state, of the safety-relevant features generally, "We find that these features not only activate on these topics, but also causally influence the model’s outputs in ways consistent with our interpretations" (Safety-Relevant Features); the one deception-related causal result taken in here is c02. The secrecy-clamp scratchpad result is recorded in the source file and not taken in at summary level.

`kind: measurement`: what the dictionary learning yielded, with the labels identified as the authors'. What the claim does not say: that any of these features was shown to be active when the model was being deceptive; the paper's one test of that kind is c02. Framework sentence: none (no model report; the measurement is an SAE decomposition). Bucket `narrowing`: measured by the source, unreplicated, and unreplicable by others on this closed model. Trigger 2 (developer of studied model, none-retrieved) will mark it if compiled.
