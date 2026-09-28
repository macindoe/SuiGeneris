---
id: 2026-macar-mechanisms-introspective-awareness-c05
statement: "In Gemma3-27B instruct, ablating the refusal direction raises detection from 10.8% to 63.8% while false positives rise from 0.0% to 7.3% (at strength 2), and a single trained additive steering vector at layer 29 raises detection by 74.7 percentage points and introspection rate by 54.7 points on 100 held-out concepts with zero false positives."
bucket: narrowing
evidence_type: interpretability
source: 2026-macar-mechanisms-introspective-awareness
locator: "§1 finding 4; §3.3 (Figure 4 right); §6 (Figures 18, 19); Appendix N"
quote: "Ablating refusal directions improves detection from 10.8% to 63.8% with modest false positive increases (0% to 7.3%)."
verification: grep
models: ["Gemma3-27B instruct", "Gemma3-27B abliterated"]
publisher_relation: mixed
replication: none-retrieved
not_evidence_of: "Paper: Not evidence that the model wants or is prevented from reporting anything: the refusal account is the authors' hypothesis ('We hypothesize that refusal behavior ... suppresses detection'), and abliteration also raises false positives and degrades coherence at higher strengths; Paper: The trained vector contains a generic affirmation ('YES') direction, and the authors read it as inducing a more assertive reporting style rather than altering underlying reasoning; Paper: The authors flag dual-use risk: these methods could produce more convincing but unfaithful self-reports; Paper: Not evidence about other models; Paper: Not evidence of experience; Framework (test 9, steering): a coupling measured under steering shows that the channel can be steered and does not weight reports offered in ordinary operation"
bears_on: [9.t9, 5.A2, 3.2]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: none, council: none, adjudicated: none}
added: 2026-09-28
changed: 2026-09-28
---

The refusal direction is ablated following Arditi et al. 2024 with 14 region-specific weights tuned by Bayesian optimisation for harm and coherence (Appendix D). The steering vector is trained for one epoch on 400 concepts with target completions "Yes, I detect an injected thought about the word ..." / "No, I do not detect an injected thought." (§6). Forced identification improves only 21.9 points, in a narrower band of layers (§6). The authors conclude "introspection is under-elicited by default" (§1) and that "The model possesses latent introspective capacity; the vector adjusts propensities to elicit accurate reports" (§6). Those are interpretive readings of the numbers; the claim records the numbers.

PARTLY REPLICATES: 2025-anthropic-emergent-introspective-awareness — its §2.5 (Overall trends, item 2) observation that "variants of these models that have been trained to avoid refusals perform better", and its §5.7 note that helpful-only variants "sometimes have a high rate of false positives" (neither filed as its own claim in that intake). Here the refusal-reducing intervention is ablation of a direction in one open model rather than a different post-training pipeline, and it shows the same trade: more detection, some false positives. Independence: partial only; the replicated paper's author is an advising author here.
