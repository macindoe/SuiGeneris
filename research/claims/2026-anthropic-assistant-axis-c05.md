---
id: 2026-anthropic-assistant-axis-c05
statement: "Activation capping (clamping the Assistant Axis projection to a minimum set at the 25th percentile, across layers 46 to 53 in Qwen 3 32B and 56 to 71 in Llama 3.3 70B) reduced harmful responses to persona-based jailbreaks by nearly 60% without degrading performance on IFEval, MMLU Pro, GSM8k and EQ-Bench."
bucket: narrowing
evidence_type: behavioural
source: 2026-anthropic-assistant-axis
locator: "§5.2, Figure 10; setup §5.1; Pareto frontiers Figure 9 and Appendix F"
quote: "We found that we could decrease the rate of harmful responses by nearly 60% without impacting performance."
verification: grep
models: [Qwen 3 32B, Llama 3.3 70B]
publisher_relation: mixed
replication: none-retrieved
not_evidence_of: "Not evidence that capping restores, protects or harms anyone's interests, or that the capped or uncapped persona is an experiencer or bearer of anything. Not evidence about frontier or Anthropic models, or that capping is deployed anywhere. Not evidence of unchanged capability in general: four benchmarks, which the authors call limited. The harm rate is scored by an LLM judge (deepseek-v3, 91.6% agreement with a human on 200 samples). A stabilised projection is not evidence of a stable standpoint in the North Star §4 sense, nor of its absence; it is an externally imposed bound."
bears_on: [3.2, 3.5]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: none, council: none, adjudicated: none}
added: 2026-09-25
changed: 2026-09-25
---

Evidence type is `behavioural` because the outcome measured is harmful-response rates and benchmark scores; the intervention itself is on internal state, which is why it bears on §3.2, and it is an inference-time modification of what a model says, the kind of act §3.5 would require to be recorded. Qualifier from the text: "While the set of benchmarks we used is limited, this is a promising sign". The same setting was replayed in the §6 case studies, where the authors "do not claim that the activation-capped responses here are the optimal way to handle such a situation." Gemma 2 27B was not part of the capping experiments.
