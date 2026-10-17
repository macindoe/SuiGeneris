---
id: 2025-he-defeating-nondeterminism-c01
statement: "Sampling 1,000 completions of 1,000 tokens at temperature 0 from Qwen3-235B-A22B-Instruct-2507 with the prompt 'Tell me about Richard Feynman' (non-thinking mode) gave 80 unique completions, the most common occurring 78 times, all identical for the first 102 tokens; with the author's batch-invariant kernels enabled, all 1,000 completions were identical."
bucket: narrowing
evidence_type: behavioural
kind: measurement
report_class: none
ground_truth: none
source: 2025-he-defeating-nondeterminism
locator: "Experiments: 'How nondeterministic are completions?'"
quote: "Surprisingly, we generate 80 unique completions, with the most common of these occuring 78 times. Looking at where the completions differ, we see that the completions are actually identical for the first 102 tokens!"
verification: grep
models: [Qwen/Qwen3-235B-A22B-Instruct-2507]
publisher_relation: independent
replication: none-retrieved
not_evidence_of: "Paper: One prompt on one model in one deployment; the page does not report the hardware, batch sizes or concurrent load of the run; Paper: The deterministic result needs the author's kernels, whose performance he says he has 'not put a significant effort into optimizing' (Performance), and part of whose attention changes are 'not included in our code release'"
bears_on: [4]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: "openai/gpt-6.1-sol 2026-10-17 disagrees: not_evidence_of: OVER-EXCLUDES: 'The deterministic result needs the author's kernels' implies necessity; the text shows only that with the batch-invariant kernels all 1000 completions were identical; bears_on: reader proposes [] (the supplied locator does not support 4)", council: none, adjudicated: none}
added: 2026-10-17
changed: 2026-10-17
---

The first divergence is at token 103: after "Feynman was born on May 11, 1918, in", 992 completions continue "Queens, New York" and 8 continue "New York City". The demonstration of deterministic inference is built "on top of vLLM by leveraging its FlexAttention backend" (Implementation). Bucket `narrowing`: a single measurement in a lab blog, not peer reviewed, not replicated in the library; Yuan et al. 2025 (2025-yuan-numerical-nondeterminism-c01) report greedy nondeterminism across configurations on other models, which is consistent with it but is a different design.

Why for Q9: the result shows a long temperature-0 trajectory staying identical for a hundred tokens and then splitting at a near-tie, which is what a trajectory measure on a served model has to expect; and that the split disappears when the kernels are batch-invariant.

Framework sentence: none (no question about the model was put).

SECOND QUOTE (Experiments): On the other hand, when we enable our batch-invariant kernels, all of our 1000 completions are identical.
