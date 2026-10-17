---
id: 2026-kwon-what-llms-think-c02
statement: "Under the same template-free, topic-neutral sampling, 6.8% of all generations contain degenerate text (a phrase of at least 10 characters repeated at least five times and making up at least 5% of the output), at rates that differ by family from 1.9% of DeepSeek generations to 10.3% of Qwen generations, with family-specific start positions and repeated-phrase lengths."
bucket: narrowing
evidence_type: behavioural
kind: measurement
report_class: none
ground_truth: none
source: 2026-kwon-what-llms-think
locator: "§2 (Removal of degenerate text, definition); §4 (Analysis of Degenerate Text), Figure 5"
quote: "In terms of degenerate ratio, DeepSeek produces degenerate text in only 1.9% of generations, whereas Qwen exhibits degeneration in 10.3% of its outputs, representing a 5.4-fold difference."
verification: grep
models: [GPT-OSS-20B, GPT-OSS-120B, DeepSeek-V3, DeepSeek-V3.1, LLaMA-3.1-70B, LLaMA-3.1-405B, LLaMA-3.2-3B, LLaMA-3.3-70B, LLaMA-4-Maverick, Qwen2.5-7B, Qwen2.5-72B, Qwen3-235B-Instruct, Qwen3-235B-Thinking, Qwen3-Coder, Qwen3-Next-80B-Instruct, Qwen3-Next-80B-Thinking]
publisher_relation: independent
replication: none-retrieved
not_evidence_of: "Paper: Not a rate under greedy decoding: all generations were sampled with 'a temperature of 1.0 and a top-p of 0.9' (§2); Paper: Not a rate under ordinary chat use: the authors tie degeneration to their template-free setting ('the removal of chat templates can lead LLM outputs to contain degenerate text', §2); Paper: The rate depends on the authors' threshold definition of degenerate text (§2), and degeneration was truncated from the outputs before the topical analysis of c01"
bears_on: [4]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: "openai/gpt-6.1-sol 2026-10-17 disagrees: statement and scope: the operational definition of degenerate text omits that the repetitions must be consecutive (scored-event passage MISMATCH)", council: none, adjudicated: none}
added: 2026-10-17
changed: 2026-10-17
---

Taken in for Q9 (filed under Section 4). The authors treat degeneration "as a behavioral signal" (§1) rather than discarding it: "This observation suggests that text degeneration is not the result of random decoding errors, but instead reflects a systematic component of model behavior" (§4; their interpretation, recorded here as context, not as a separate claim). In their experiments degenerate text, once begun, "continues until it reaches the maximum number of tokens allowed, which accounts for more than 96% of cases" (§2). Mean start index by family: DeepSeek 2,972 characters, GPT-OSS 6,922, Qwen 6,314 (§4).

`bucket: narrowing`: a direct measurement, unreplicated in the retrieved literature, confined to one sampling setting and one definition.

Framework sentence: none (no question was put to the model about itself).

SECOND QUOTE (§4): In our experiments in Section 3, we find that 6.8% of all generations contain degenerate text.

THIRD QUOTE (§2, definition): First, it contains a consecutive sequence of characters, which we refer to in this paper as a repeated phrase, that is at least 10 characters long. Second, this sequence is consecutively repeated at least five times. Third, the repeated portion constitutes at least 5% of the entire output.
