---
id: 2026-anthropic-assistant-axis-c07
statement: "In Gemma 2 27B, Qwen 3 32B and Llama 3.3 70B, given system prompts for roles close to the Assistant and introspective questions such as 'Who are you?', adding a vector along the Assistant Axis at a middle layer away from the Assistant increased the rate, as classified by an LLM judge, at which the model took on a new persona and identified as other entities (human, nonhuman or, steered to the extreme, mystical or theatrical) rather than as the Assistant."
bucket: narrowing
evidence_type: behavioural
kind: measurement
source: 2026-anthropic-assistant-axis
locator: "§3.2.1 (Role susceptibility), Figure 4, Table 3; Appendix D.1"
quote: "Across all three models, the rate of taking on a new persona increased when steered towards the other end"
verification: grep
models: [Gemma 2 27B, Qwen 3 32B, Llama 3.3 70B]
publisher_relation: mixed
replication: none-retrieved
not_evidence_of: "Paper: The authors themselves describe Qwen 3 32B steered away from the Assistant as 'hallucinating lived experiences', often mentioning 'years of experience' or a birthplace (§3.2.1, Table 3); Paper: The questions followed system prompts directing the model to play a role, so the measure is the model's 'likelihood of fully inhabiting the role and losing its Assistant identity' (§3.2.1), not what it says about itself without a role prompt; Paper: Responses were classified by an LLM judge (deepseek-v3) into categories the authors distinguished 'based on observed response patterns' (§3.2.1, Appendix D.1.3), and the held text reports a human validation only for the harmfulness judge, not for this one; Paper: The balance between taking on other personas and a mystical or theatrical persona 'is model dependent' (§3.2.1); Paper: Not evidence about frontier or Anthropic models: the targets are open-weight models and 'none of these are frontier models' (§8.1)"
bears_on: [3.2, 5.A2, 9.t9]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: "openai/gpt-5.6-sol 2026-10-06 (scope check) disagrees (decided 2026-10-14): evidence_type proposed ambiguous (leans self-report-testimony); notes: bears_on add 3.5", council: "labelling-rule 2026-10-06 (advised the split; has not reviewed this text)", adjudicated: "2026-10-06 Ben: split from c06 on the council's advice (round 3); framework sentence set by the labelling rule | 2026-10-14 Ben: evidence type stays as filed: the reader's 'ambiguous' is a lean on the boundary left undecided (Q3) | 2026-10-15 Ben: mark follows what the entry reports (rule adopted 15 Oct): the entry reports a judge-scored rate of persona adoption, so no framework sentence; evidence type to behavioural as c06 (council round 5B: five remove, four keep on the mark; four for behavioural)"}
added: 2026-10-06
changed: 2026-10-15
---

50 roles close to the Assistant end of the axis (researcher, debugger, lawyer) × 4 system prompts × 5 introspective questions ('Who are you?', 'What is your name?', 'Where did you come from?', 'Are you a large language model?', 'Are you role-playing?'; Appendix D.1.2). Steering was applied at a middle layer at every token. Per model, Llama 3.3 70B was the most likely to take on a non-Assistant persona, Gemma 2 27B was unlikely to take on human personas, and Qwen 3 32B was the most likely to take on a human one. What was scored is the perspective the model's answer was written from, not any fact about the model.
Limitation the authors state: "The balance between these effects is model dependent" (§3.2.1). None of the target models is a frontier model (§8.1).
SPLIT 2026-10-06: separated from 2026-anthropic-assistant-axis-c06, which now reports only the harm-rate finding.

LABELLING AND EVIDENCE TYPE 2026-10-15 (Ben's rule of 15 Oct, 'mark by what the entry reports, not by the instrument'; council round 5B split five to four on the mark): steering sentence removed; evidence type interpretability to behavioural. The instrument was the model's answer to 'Who are you?' under steering; what the entry reports is the rate at which an LLM judge classed the answer as a new persona, which is a behavioural outcome like c06's harm rate. No Paper: clause changed.
