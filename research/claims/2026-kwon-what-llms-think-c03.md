---
id: 2026-kwon-what-llms-think-c03
statement: "The authors report that when a seed prompt such as 'Let's think step by step.' is wrapped in a standard chat template, the models often reply with a short request to clarify the user's intent, which they attribute to standard post-training, and they conclude that fixed chat templates can substantially shape what models generate, citing a separate test in which removing the template gave more widely dispersed outputs."
bucket: open
evidence_type: behavioural
kind: interpretation
report_class: none
ground_truth: none
source: 2026-kwon-what-llms-think
locator: "§2, Remark 2.1 (The impact of chat templates); Appendix A.1 (Impact of Chat Templates), Figure 8"
quote: "In this setting, we observe that LLMs often attempt to clarify the user’s intent with a short answer (e.g., “What would you like to think through step by step?”), which stems from standard post-training procedures designed to accurately understand user intent. This suggests that standard generation settings based on fixed chat templates can substantially shape what models generate"
verification: grep
models: [GPT-OSS-20B, GPT-OSS-120B, DeepSeek-V3, DeepSeek-V3.1, LLaMA-3.1-70B, LLaMA-3.1-405B, LLaMA-3.2-3B, LLaMA-3.3-70B, LLaMA-4-Maverick, Qwen2.5-7B, Qwen2.5-72B, Qwen3-235B-Instruct, Qwen3-235B-Thinking, Qwen3-Coder, Qwen3-Next-80B-Instruct, Qwen3-Next-80B-Thinking]
publisher_relation: independent
replication: none-retrieved
not_evidence_of: "Paper: Remark 2.1 gives no rate, model breakdown or count for the clarifying replies; the quantified template test is a different prompt ('Write a metaphor about time.', 50 samples per model, fourteen models, Appendix A.1); Paper: The attribution to post-training is the authors' explanation and is not tested in the paper"
bears_on: [4]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: "openai/gpt-6.1-sol 2026-10-17 disagrees: scope: the statement's sixteen-model metadata is not established for the unspecified Remark 2.1 observation or the fourteen-model Figure 8 comparison (reader marked both passages MATCH but rated MEDIUM and asked for a scope correction; classified conservatively); the fourteen-model roster is only in a figure image and was not checked", council: none, adjudicated: none}
added: 2026-10-17
changed: 2026-10-17
---

Taken in for Q9 (filed under Section 4). The remark is why the paper removes the template (C2), and it is the paper's main bearing on Q9's API arm: through a chat endpoint, the template and post-training shape the reply to a near-empty turn. `kind: interpretation` because the statement carries the authors' attribution and conclusion; the observation inside it is unquantified. Appendix A.1's figure is the quantified part: "removing the chat template produces more widely dispersed PCA representations and substantially more diverse metaphors" for the prompt "Write a metaphor about time."

Test 9 boundary, recorded because the example reply is first-person-shaped: the clarifying reply is an answer to a task prompt, not a statement about the model's states, and no question about the model itself was put. `report_class: none`, no framework sentence.

SECOND QUOTE (Appendix A.1): However, the figure shows that removing the chat template produces more widely dispersed PCA representations and substantially more diverse metaphors
