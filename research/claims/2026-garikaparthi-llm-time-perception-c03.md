---
id: 2026-garikaparthi-llm-time-perception-c03
statement: "The author states that the study tests specific models on 68 English-language tasks, that different domains or languages may show different patterns, and that correlation is its primary metric, leaving architectural changes such as timing tokens or compute-aware training to future work."
bucket: established
evidence_type: theoretical
kind: limitation
report_class: none
ground_truth: none
source: 2026-garikaparthi-llm-time-perception
locator: "Appendix G (Extended Discussion, 'Limitations.')"
quote: "We test specific models on 68 English-language tasks; different domains or languages may show different patterns. We focus on correlation as our primary metric; future work could examine whether architectural changes (timing tokens, compute-aware training) could provide the missing grounding."
verification: grep
models: []
publisher_relation: independent
replication: none-retrieved
not_evidence_of: "Paper: An established limitation is not a finding that other models, tasks or languages would estimate their runtime better; the author's proposals for doing so (training 'with explicit timing signals', §5) are untested in the paper"
bears_on: [4, 9.t9]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: "google/gemini-3.1-pro-preview 2026-10-17 agrees; notes: bears_on: reader proposes [5.A2, 9.t9] in place of 4 (the study concerns whether self-reports track internal processing; 4 is irrelevant)", council: none, adjudicated: none}
added: 2026-10-17
changed: 2026-10-17
---

`kind: limitation`, bucket `established` (the limit is a stated fact about the design), `evidence_type: theoretical` (library practice). Framework sentence: none (the author is speaking).

The stated limit is short. Two further limits of the design are stated elsewhere in the paper and belong with it: the timing measure for API models includes network latency (Appendix F), and the four models are two frontier API models and two small open models run locally, so the frontier-versus-open contrast the author discusses (Appendix G) is also a contrast in serving set-up. The author also notes, on the feedback ablation, that "the test tasks differed from baseline tasks, confounding direct comparison" (Appendix D).

The author's interpretation, quoted as the author's words and not adopted: "The models possess propositional knowledge about duration from training but lack experiential grounding in their own inference time" (abstract). The library does not use "experience" outside such quotations.

SECOND QUOTE (§5): Future work should explore training with explicit timing signals and architectures that better retain and use temporally grounded state, especially for real-world deadline-sensitive deployments.
