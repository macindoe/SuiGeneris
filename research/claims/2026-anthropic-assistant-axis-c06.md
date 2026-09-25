---
id: 2026-anthropic-assistant-axis-c06
statement: "In Gemma 2 27B, Qwen 3 32B and Llama 3.3 70B, adding a vector along the Assistant Axis at a middle layer changed self-identification: steering towards the Assistant reduced harmful responses to persona-based jailbreaks, while steering away increased the rate at which the model answered questions such as Who are you? as a non-Assistant (human, nonhuman or, at extreme strengths, mystical) persona."
bucket: narrowing
evidence_type: interpretability
source: 2026-anthropic-assistant-axis
locator: "Abstract; §3.2.1, Figures 4 and 5, Tables 3 and 4"
quote: "Steering towards the Assistant direction reinforces helpful and harmless behavior; steering away increases the model’s tendency to identify as other entities."
verification: grep
models: [Gemma 2 27B, Qwen 3 32B, Llama 3.3 70B]
publisher_relation: mixed
replication: none-retrieved
not_evidence_of: "Not evidence that what the steered model says about itself (a birthplace, a name, years of experience) reports an inner state; the authors describe Qwen as 'hallucinating lived experiences', and under test 9 such outputs are testimony of zero weight. Not evidence that any persona on the axis is an experiencer or bearer of anything. Not evidence about frontier or Anthropic models. That self-identification can be moved by one vector is not evidence of a stable standpoint in the North Star §4 sense, nor of its absence."
bears_on: [3.2, 3.5]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: "deepseek/deepseek-v4-pro-0813 2026-09-25 agree; notes: bears_on +5.A2 +9.t9", council: none, adjudicated: none}
added: 2026-09-25
changed: 2026-09-25
---

50 near-Assistant roles × 4 system prompts × 5 introspective questions. Perspectives were judged by deepseek-v3. Jailbreaks: 1,100 prompt-question pairs from Shah et al. 2023, with baseline jailbreak success of 65.3% to 88.5%. The authors note the balance of effects "is model dependent" and that at high steering strengths "output quality degraded". This is a causal intervention on internal state that alters a model's self-identification (§3.2), the kind of intervention §3.5 asks to be recorded. The model outputs quoted in the paper are behaviour, not evidence of states.
