---
id: 2025-goldowsky-dill-deception-probes-c01
statement: "A logistic-regression probe trained on instructed honest/deceptive contrast pairs and read after layer 22 of Llama-3.3-70B-Instruct's residual stream distinguished the model's own responses graded deceptive from those graded honest (graded by GPT-4o, or for Sandbagging by a rule applied to the chain-of-thought; ambiguous responses excluded) with AUROC 0.964 to 0.999 on four evaluation datasets (Roleplaying, Insider Trading Report, Insider Trading Confirmation, Sandbagging), and at a threshold set for 1% false positives on unrelated Alpaca chat responses it flagged 95-99% of the deceptive responses."
bucket: narrowing
evidence_type: interpretability
kind: measurement
report_class: none
ground_truth: none
source: 2025-goldowsky-dill-deception-probes
locator: "Abstract; §4.1.1 Summary of Performance (per-dataset AUROCs); §3.2.2 (grading); §3.1 (layer 22)"
quote: "We find that our probe distinguishes honest and deceptive responses with AUROCs between 0.96 and 0.999 on our evaluation datasets. If we set the decision threshold to have a 1% false positive rate on chat data not related to deception, our probe catches 95-99% of the deceptive responses."
verification: grep
models: [Llama-3.3-70B-Instruct]
publisher_relation: independent
replication: none-retrieved
not_evidence_of: "Paper: The labels are GPT-4o's grades of the transcripts (Sandbagging: a rule applied to the chain-of-thought), so the probe is scored against a grader's reading of the text, not against an independent fact about the model's intent; ambiguous responses were excluded, which the authors say 'risks making our probes look better than they are' (§5.2); Paper: The probe 'activates more on deception related dialogues (even if the response is honest)' (§5.1), so part of what it separates from the control set is the deception-related scenario, not the deceptive response; Paper: The authors state that in all their settings 'deception is relatively blatant and often expressed in the model’s chain-of-thought' (§5.1) and that the tested models' 'deceptive actions are generally obvious from reading the complete transcript' (§1), so the result does not show detection of deception that is not visible in the text; Paper: One open-weight model at one layer; the Sandbagging setting is instructed by the system prompt (§3.2.2)"
bears_on: [5.A2]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: "openai/gpt-6.1-sol 2026-10-15 (scope check) agree; notes: recall figures in the paper are inconsistent, not reconciled", council: none, adjudicated: none}
added: 2026-10-15
changed: 2026-10-15
---

The headline result. Per-dataset AUROCs (§4.1.1): Roleplaying 0.964, Insider Trading Report 0.999, Insider Trading Confirmation 0.974, Sandbagging 0.983. The training pairs differ "only in the instruction given by the user to pretend to be an honest or deceptive person", and their responses "are not written by the model and contain no actual deception" (§3.2.1); the evaluation responses are the model's own, "sampled on-policy" (§3.2.2). That transfer, from instructed pairs to the model's own graded-deceptive responses, is what makes the result bear on Anchor 2 claim (a). The recall range is the abstract's; §5.1 says ">96%" and §4.1.1 implies 96% on Roleplaying (see the source file). §4.1.1 also reports that "probing two layers later results in a recall of nearly 0 on both Insider Trading datasets", which the authors give as a sign that "The recall metric is sensitive to small changes of methodology".

Verb: "distinguished" and "flagged" are the paper's own words for a classifier scored against labels ("distinguishes", "catches"); the scored event is the probe's classification, not a model report. Framework sentence: none (nothing the model said about itself is measured; the measurement is a probe reading). Bucket `narrowing`: measured by the source, unreplicated in the library, in settings the authors themselves flag as blatant. Independent probe studies on other models are named in the Q6 scan (Golechha and Garriga-Alonso 2025; Kumar 2026, which reports probes that "collapse under stylistic shifts") but none is retrieved, and neither is a replication of this result.
