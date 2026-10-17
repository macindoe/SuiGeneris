---
id: 2026-bruckner-one-token-c01
statement: "Across 165 models queried through OpenRouter with prompts requiring a one-word answer, sampled three times per probe cell at temperature 0, 90.4% of cells were deterministic within a serving provider and 84.5% when pooled across providers, a gap the author attributes to serving-stack variance: different upstream deployments of the same model give different, individually stable, greedy answers."
bucket: narrowing
evidence_type: behavioural
kind: measurement
report_class: none
ground_truth: none
source: 2026-bruckner-one-token
locator: "§VI-A (RQ1: Fingerprints Exist and Are Stable); §V (Sampling; Pilot and pre-registration); §IV-A"
quote: "At temperature 0, 90.4% of cells are deterministic within serving provider; pooled across providers the rate drops to 84.5%, the gap being serving-stack variance – different upstream deployments of the same model produce different, individually stable, greedy answers"
verification: grep
models: ["165 models served via OpenRouter, 53 serving providers"]
publisher_relation: independent
replication: none-retrieved
not_evidence_of: "Paper: The rates are for one-token answers to trivial prompts, three samples per cell at T=0 (§V), not for longer generations; Paper: One aggregator, short horizon: 'we quantify short-horizon stability but not multi-month drift' and 'ecosystem findings may not generalize' beyond the one aggregator (§VII-D)"
bears_on: [4]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: "x-ai/grok-4.7 2026-10-17 agrees; notes: bears_on: reader proposes [] (one-token greedy stability is not endorsement); all other fields agreed", council: none, adjudicated: none}
added: 2026-10-17
changed: 2026-10-17
---

Each cell is one task in one language (ten tasks, four languages, 40 cells per model), queried "with a fixed system prompt enforcing a one-word answer, a hard cap of 16 completion tokens, and provider-side reasoning modes disabled" (§IV-A); the temperature-0 variant is collected alongside the T=1.0 fingerprint. The pilot pre-specified "within-provider greedy determinism \geq 90\% of cells" as a criterion (§V). The paper does not define "deterministic cell" further in the text read; with three samples, the reading that all three answers matched is the natural one but is not stated. Bucket `narrowing`: one study on one aggregator, not replicated in the library.

Why for Q9: it is the measured size of temperature-0 nondeterminism on the platform the project uses, for a single token; a trajectory of many tokens can only compound it (Q9 scan, "Corrections and cautions"; that compounding is the scan's inference, not the paper's).

Framework sentence: none (no question about the model's own states is scored; the measurement is answer agreement across repeats).

SECOND QUOTE (§V): Each model \times 10 tasks \times 4 languages is sampled 30 times at T{=}1.0 and 3 times at T{=}0
