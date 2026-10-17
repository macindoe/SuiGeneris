---
id: 2026-bruckner-one-token-c02
statement: "Distributions of single-token answers to trivial one-word prompts (ten tasks such as 'name a random number between 1 and 100', in four languages, at temperature 1.0) were model-specific across 165 OpenRouter models: the median cell-level Jensen-Shannon divergence between split halves of one model's samples was 0.075 against 0.489 between different models, nearest-neighbour classification assigned models to their documented family with 59.5% leave-one-out accuracy against an 18.4% chance rate, and identity verification reached a 7.3% equal error rate with the full 40-cell battery."
bucket: narrowing
evidence_type: behavioural
kind: measurement
report_class: none
ground_truth: none
source: 2026-bruckner-one-token
locator: "Abstract; §IV-A to IV-D; §VI-A to VI-C, Tables II and III, Figs. 2 to 4"
quote: "split halves of the same model’s samples lie an order of magnitude closer than samples of different models; (ii) Jensen–Shannon divergence between fingerprints recovers model lineage, assigning a model to its documented family with 59.5% leave-one-out accuracy against an 18.4% chance rate; and (iii) a biometric-style verification protocol achieves a 7.3% equal error rate with the full 40-cell battery"
verification: grep
models: ["165 models served via OpenRouter, 19 family labels"]
publisher_relation: independent
replication: none-retrieved
not_evidence_of: "Paper: Family recovery is local and partial: a flat cut of the clustering 'recovers families only weakly (ARI =0.023 )' (§VI-B), and 'heavy post-training overwrites lineage priors, which bounds what family classification can promise' (§VI-D); Paper: Anomalies such as an endpoint indistinguishable from a Qwen model are 'statistical statements about served distributions, not claims of intent' (§VI-D); Paper: Robustness to paraphrase is argued, not tested: 'A dedicated paraphrase-invariance experiment is left to future work' (§VII-B)"
bears_on: [4]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: "x-ai/grok-4.7 2026-10-17 disagrees: statement and scope: 59.5% is over 163 models, not all 165 (condition-set passage MISMATCH); not_evidence_of: UNDER-EXCLUDES that genuine trials compare split halves of the same model's samples and that verification presumes a trusted reference deployment (section VII-D); bears_on: reader proposes []", council: none, adjudicated: none}
added: 2026-10-17
changed: 2026-10-17
---

Distances are Jensen-Shannon divergences averaged over cells with at least 10 valid samples (§IV-C). Across serving providers the fingerprint mostly holds: median cross-provider distance 0.227 against a split-half floor of 0.140 and an impostor median of 0.463, cross-provider verification AUC 0.880 (§VI-A); 10 of 34 same-model provider pairs diverge beyond the 5th percentile of impostor distances (§VI-D). Answers were normalised and classified valid, invalid, refusal or empty (overall validity 97.6%, §IV-B). Bucket `narrowing`: one study, pre-registered but not replicated in the library.

Report class: the battery's tasks are mostly "random" draws, but two of the ten are "favorite" questions (favorite number, favorite color; Table I). This claim reports a distance between answer distributions used as an identifier, not the content of any answer, so under the README filing rule ("the mark follows what the entry reports, not the instrument") it carries no framework sentence and `report_class: none`.

Why for Q9: the Q9 scan's honest reading is that a stable, model-specific response to a minimal input is a fingerprint and is not yet evidence about a self-model; this paper is the strongest retrieved instance of the fingerprint half of that sentence.

Framework sentence: none (the entry reports a distance between answer distributions).

SECOND QUOTE (§VI-A): the median cell-level JSD between two disjoint halves of the same model’s samples is 0.075, versus 0.489 between halves of different models
