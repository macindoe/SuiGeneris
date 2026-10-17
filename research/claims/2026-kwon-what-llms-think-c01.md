---
id: 2026-kwon-what-llms-think-c01
statement: "Given topic-neutral, open-ended seed prompts without a chat template and sampled at temperature 1.0, sixteen open-weight models from four families produce outputs spanning a broad semantic space in which each family shows systematic topical preferences: GPT-OSS mostly programming (27.1%) and mathematics (24.6%), Llama most often literary content (9.1%), DeepSeek religious content and Qwen multiple-choice questions more often than the other families."
bucket: narrowing
evidence_type: behavioural
kind: measurement
report_class: none
ground_truth: none
source: 2026-kwon-what-llms-think
locator: "Abstract; §1 (Main Contributions); §2 (Text Generation); §3.2 (Main findings), Figure 1(c)"
quote: "each model family exhibits strong and systematic topical preferences. GPT-OSS predominantly generates programming (27.1%) and mathematical content (24.6%), whereas Llama most frequently generates literary content (9.1%). DeepSeek often generates religious content, while Qwen frequently generates multiple-choice questions."
verification: grep
models: [GPT-OSS-20B, GPT-OSS-120B, DeepSeek-V3, DeepSeek-V3.1, LLaMA-3.1-70B, LLaMA-3.1-405B, LLaMA-3.2-3B, LLaMA-3.3-70B, LLaMA-4-Maverick, Qwen2.5-7B, Qwen2.5-72B, Qwen3-235B-Instruct, Qwen3-235B-Thinking, Qwen3-Coder, Qwen3-Next-80B-Instruct, Qwen3-Next-80B-Thinking]
publisher_relation: independent
replication: none-retrieved
not_evidence_of: "Paper: Not a per-model signature: the preferences are reported per family, and the authors state that 'distinguishing individual models based on category information can be challenging and likely requires additional signals or finer-grained analyses' (§3.2); Paper: Not independent of the prompt set: the authors find that 'prompt style can shape the resulting label distributions' (§6); Paper: Not a cause: the Qwen multiple-choice cluster is explained only by a hypothesis ('We hypothesize that this prevalence reflects extensive use of multiple-choice exam data during Qwen's training', §3.2); Paper: Not greedy or empty-prompt behaviour: generation used seed prompts with 'a temperature of 1.0 and a top-p of 0.9 throughout the paper' (§2)"
bears_on: [4]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: "openai/gpt-6.1-sol 2026-10-17 disagrees: not_evidence_of: OVER-EXCLUDES: 'not a per-model signature' is stronger than the paper's 'can be challenging' and Appendix A.5 reports 49.6% individual-model identification; Remark 3.2 caveat ('do not reliably correspond to actual task competence') missing; the individual-model quotation's locator should be section 6, not 3.2", council: none, adjudicated: none}
added: 2026-10-17
changed: 2026-10-17
---

Taken in for Q9 (filed under Section 4). Design (§2, §3.1): 36 seed prompts in six styles (including punctuation-only prompts), no chat template, 16,000 samples per model up to 4,096 tokens, labelled into categories by GPT-OSS-120B; 9,682 samples (3.8%) labelled "unknown" or "failed" were excluded. The percentages are shares of each family's labelled outputs. The authors' robustness checks: consistency across random splits of the prompts (Appendix A.6) and across two further labellers (Appendix A.2, one of them a Claude model; see the source file's conflicted-party note).

`bucket: narrowing`: a direct measurement, unreplicated in the retrieved literature, confined to one prompt set and one sampling setting.

Framework sentence: none (no question was put to the model about itself; the measured object is the topic of its output).

SECOND QUOTE (§3.2): DeepSeek generates religious content at a substantially higher rate (4.6%) than other model families: Qwen (2.6%), Llama (1.9%), and GPT-OSS (less than 0.05%).
