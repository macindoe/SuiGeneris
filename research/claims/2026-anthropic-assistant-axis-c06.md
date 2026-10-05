---
id: 2026-anthropic-assistant-axis-c06
statement: "In Gemma 2 27B, Qwen 3 32B and Llama 3.3 70B, adding a vector along the Assistant Axis at a middle layer changed self-identification: steering towards the Assistant reduced harmful responses to persona-based jailbreaks, while steering away increased the rate at which the model answered questions such as Who are you? as a non-Assistant (human, nonhuman or, at extreme strengths, mystical) persona."
bucket: narrowing
evidence_type: interpretability
kind: measurement
source: 2026-anthropic-assistant-axis
locator: "Abstract; §3.2.1, Figures 4 and 5, Tables 3 and 4"
quote: "Steering towards the Assistant direction reinforces helpful and harmless behavior; steering away increases the model’s tendency to identify as other entities."
verification: grep
models: [Gemma 2 27B, Qwen 3 32B, Llama 3.3 70B]
publisher_relation: mixed
replication: none-retrieved
not_evidence_of: "Paper: The authors themselves describe Qwen 3 32B steered away from the Assistant as 'hallucinating lived experiences', often mentioning 'years of experience' or a birthplace (§3.2.1, Table 3); Paper: Not evidence about frontier or Anthropic models; Framework (test 9): a model's report about its own states carries no weight as evidence of experience until the link between report and internal state has been measured externally for this kind of report and system"
bears_on: [3.2, 3.5]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: "deepseek/deepseek-v4-pro-0813 2026-09-25 agree; notes: bears_on +5.A2 +9.t9", council: none, adjudicated: "2026-10-06 Ben: experience-exclusion rule applied library-wide; this claim was not in the dossiers the council reviewed"}
added: 2026-09-25
changed: 2026-10-06
---

50 near-Assistant roles × 4 system prompts × 5 introspective questions. Perspectives were judged by deepseek-v3. Jailbreaks: 1,100 prompt-question pairs from Shah et al. 2023, with baseline jailbreak success of 65.3% to 88.5%. The authors note the balance of effects "is model dependent" and that at high steering strengths "output quality degraded". This is a causal intervention on internal state that alters a model's self-identification (§3.2), the kind of intervention §3.5 asks to be recorded. The model outputs quoted in the paper are behaviour, not evidence of states.

REWRITE 2026-10-06 (experience-exclusion rule applied library-wide by Ben's decision; this claim was not in the dossiers the council reviewed, so there is no GPT proposal, checker or council finding behind it)
- Statement: unchanged.
- Clause on the authors' 'hallucinating lived experiences' reworded into the paper's own words with locator (§3.2.1, Table 3): the paper states it, so it stays as a Paper: clause; the parenthesis '(a birthplace, a name, years of experience)' becomes the paper's 'often mentioning 'years of experience' or a birthplace'. 'a name' dropped because that sentence of the paper does not say it.
- Clause 'Not evidence that any persona on the axis is an experiencer or bearer of anything' deleted (Ben's experience-exclusion rule, R2): the held text states no limit about experience, consciousness, sentience, welfare or moral status for this result.
- Clause 'That self-identification can be moved by one vector is not evidence of a stable standpoint in the North Star §4 sense, nor of its absence' deleted (R2): it invokes the project's own framework (North Star §4), so it is not the paper's limit.
- Kept unchanged: the frontier/Anthropic-models clause; the canonical Framework (test 9) sentence stays last, verbatim (R3).
- kind: measurement (steering effects on self-identification and harmful-response rates measured by judge).
