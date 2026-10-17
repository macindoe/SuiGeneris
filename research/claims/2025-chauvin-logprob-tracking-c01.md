---
id: 2025-chauvin-logprob-tracking-c01
statement: "On the TinyChange benchmark (290 variants of five open-weight models from 0.5B to 8B, made by fine-tuning, LoRA fine-tuning, weight pruning and parameter noise), logprob tracking, which sends one fixed prompt as short as the single letter 'x' and compares the top-k logprobs of a single output token with a permutation test, detected changes as small as one step of fine-tuning, with an overall ROC AUC of 0.915 against 0.878 and 0.670 for two baselines, at about a thousandth of their cost."
bucket: narrowing
evidence_type: behavioural
kind: measurement
report_class: none
ground_truth: none
source: 2025-chauvin-logprob-tracking
locator: "Abstract; §1; §2.3 (Two-sample test on first-token log-probabilities); §3.1; §3.2.1-3.2.2, Table 1, Figure 4"
quote: "We demonstrate through extensive in-vitro experiments that sending a single token of input and requesting a single token of output is enough to consistently detect changes that remain undetected by current monitoring methods. Our input token is chosen arbitrarily, and unrelated to the type of change applied."
verification: grep
models: [Qwen/Qwen2.5-0.5B-Instruct, google/gemma-3-1b-it, microsoft/Phi-3-mini-4k-instruct, meta-llama/Llama-3.1-8B-Instruct, allenai/OLMo-2-1124-7B-Instruct]
publisher_relation: independent
replication: none-retrieved
not_evidence_of: "Paper: LoRA fine-tuning is the 'possible exception', being 'challenging to detect for all methods' (§3.2.2); Paper: The method detects that a change occurred; it 'does not distinguish between infrastructure changes and model updates, or give information on the exact nature of the change' (§4); Paper: It needs endpoints that return logprobs ('Our approach applies to APIs that support and return log probabilities', §4)"
bears_on: [4]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: "deepseek/deepseek-v4-pro-0813 2026-10-17 agrees", council: none, adjudicated: none}
added: 2026-10-17
changed: 2026-10-17
---

Design: 10,000 samples per prompt per model and variant, generated with vLLM with the tested prompts mixed among random traffic from LMSYS-Chat-1M ("we introduce realistic noise from other requests", §3.1); each hypothesis test draws N=10 outputs per side. Prompt length matters little: "about 1% difference in AUC between the shortest (1.5 tokens) and longest prompt (33 tokens)" (§3.2.1). Baselines are Model Equality Testing (Gao et al. 2025) and an MMLU abstract-algebra subset (Table 1). Bucket `narrowing`: the authors' own method on their own benchmark, not replicated in the library.

The authors treat logprob non-determinism as something to model, not remove: "we see each logprob returned as itself sampled from a probability distribution , and use standard hypothesis testing" (§2.2). Their illustration is GPT-4.1 prompted with "x" over two weeks, whose logprobs fluctuate around their average.

Why for Q9: it is the published version of a minimal-input probe; a project probe would differ from it in measuring a trajectory rather than one token, which is where any novelty would lie (Q9 scan, entry 6.1).

Framework sentence: none (no question about the model was put; the prompt is a single letter).

SECOND QUOTE (Abstract): This is enough to detect changes as small as one step of fine-tuning, making this approach more sensitive than existing methods while being 1,000x cheaper.
