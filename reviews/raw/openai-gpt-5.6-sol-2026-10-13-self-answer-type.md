# Raw OpenRouter response — NOT a filed review

**Model id (OpenRouter):** `openai/gpt-5.6-sol`
**Queried:** 2026-10-13 via scripts/openrouter_review.js --target=self-answer-type --tag=self-answer-type (max_tokens 100000)
**Usage:** {"prompt_tokens":11772,"completion_tokens":4809,"total_tokens":16581,"cost":0.0775185,"is_byok":false,"prompt_tokens_details":{"cached_tokens":0,"cache_write_tokens":11769,"audio_tokens":0,"video_tokens":0},"cost_details":{"upstream_inference_cost":0.0775185,"upstream_inference_prompt_cost":0.0294285,"upstream_inference_completions_cost":0.04809},"completion_tokens_details":{"reasoning_tokens":3196,"image_tokens":0,"audio_tokens":0}}

Read this, then decide whether/how to promote it into reviews/YYYY-MM-DD-<model-family>-<version>.md
per reviews/README.md's naming convention and verbatim-filing rule. This file is scratch, not a commit target.

---
**unverified:** OpenAI GPT-5 family; exact version unavailable.

## Q1

**Recommendation — HIGH:** Choose **B**, with a narrower definition:

> `scored-self-answer`: the claim’s scored dependent variable is an answer about the reporting model, or the provenance of its prior output, evaluated against a scoring key fixed independently of that answer.

This accurately describes the measurement without deciding whether it demonstrates self-access. The table’s 11 `interpretability` and 10 `behavioural` core rows otherwise inherit inconsistent labels despite overlapping designs. Mechanism claims such as Macar c03/c04 should remain `interpretability`; compound claims should be split.

The value should carry no presumption of privileged access, experience, or zero weight. Test 9 sentences remain determined independently under the existing rule.

**Argument against:** `evidence_type` otherwise describes an epistemic method, while `scored-self-answer` describes an instrument form. It could conceal whether evidence came from activation intervention or ordinary text and could postpone Q3 indefinitely.

**Confidence:** high.

## Q2

**Recommendation — HIGH:** Treat the three instruments as a package of controls, not three individually sufficient tests.

- **Trained-channel control:**  
  - For access: held-out intervention labels are recoverable reliably after report training.  
  - Against: failure after adequate training suggests the prompt, architecture, or intervention does not make the label recoverable. It does not by itself refute ordinary self-access.  
  - Without access: yes. A trained classifier can exploit intervention-correlated signals without the untrained model ordinarily consulting them. Ferrara c04 therefore validates sensitivity, not introspection.

- **Privileged-access test:**  
  - For access: the target model reliably exceeds a capability-matched observer given the same visible transcript, under randomized and blinded intervention labels.  
  - Against: the observer matches the target in a well-powered comparison, especially across prompts and base rates.  
  - Without access: yes. Target-specific priors, output artifacts, architecture differences, or intervention-induced response tendencies can create an advantage. Yoked same-family controls and transcript-only baselines are needed.

- **Measured coupling:**  
  - For access: a preregistered internal measure predicts trial-level reports out of sample after controlling for intervention, transcript, prompt, and output propensity; targeted perturbation of the measured mediator changes the report selectively.  
  - Against: coupling disappears under controls, input-only probes match it, or perturbing the proposed mediator does not affect reporting.  
  - Without access: yes. A common downstream effect can drive both probe and answer, and a probe may decode information the model does not use.

Missing controls include sham interventions, balanced labels, held-out concepts and layers, prompt paraphrases, gaslighting trials, calibration, observer matching, causal mediation, and negative-control probes. “Self-access” should be operationally defined as use of system-internal information unavailable from the matched transcript, not merely above-chance classification.

**Argument against:** Requiring all these controls may set a higher standard than comparable behavioural measurements and could dismiss genuine but weak or distributed access.

**Confidence:** high.

## Q3

**Recommendation — MEDIUM:** If B is adopted, dossiers need a plain-language legend: “externally scored answer about the model; whether this demonstrates internal access remains open.” Likely misreadings are:

- **A — `ambiguous`:** the experiment or result is defective, rather than the taxonomy being unresolved.
- **B — `scored-self-answer`:** the answer has been validated as self-knowledge, rather than merely scored.
- **C — `behavioural`:** benchmark accuracy establishes access to the reported internal state.
- **D — `self-report-testimony`:** the externally replicated discrimination result has zero evidential value for every proposition.
- **E — split by design:** `interpretability` means direct internal access was demonstrated, while `behavioural` means the text-only result has no relevance to self-monitoring.

B is less familiar to legislators than `behavioural`; its neutrality therefore depends on the legend and the claim’s displayed intervention and scoring key.

**Confidence:** high.

## Q4

**Recommendation — HIGH:** Adopt an explicit exit and anti-parking rule.

1. Use B only where the scored answer itself is the claim’s dependent variable.
2. Split mixed claims: behavioural outcomes, circuit findings, and author interpretations receive separate claims and their ordinary types.
3. Keep Q3 visible in `OPEN-QUESTIONS.md`; because B would no longer activate the `ambiguous` trigger, add a grouped review trigger for a new design class, ten added B claims, or ninety days without review.
4. Reconsider Q3 after one preregistered study satisfies all three controls with adequate power, or after two independent studies jointly do so.
5. At adjudication, either migrate relevant subclasses under a stated rule or retain B with an explicit standing weight rule. Do not leave its evidential weight unspecified permanently.

Individual measurement claims may properly remain B; conclusions that the measurements establish or refute access must be filed separately.

**Argument against:** A mandatory exit threshold may manufacture a categorical decision from results that are system- and report-class-specific; permanent design metadata can be more accurate than migration.

**Confidence:** high.

## Q5

**Recommendation — MEDIUM:** Apply the narrowed definition as follows.

- **Ferrara c04 — in.** It is an answer about intervention status scored against an independent intervention/sham key. The authors’ “not introspection” interpretation belongs in the limitation, not the measurement type.
- **UKAISI c02 — split.** Flagging whether the prior turn was the model’s is B. Reversion to the baseline answer is `behavioural`.
- **Singh c01 — in, but marked probe-derived.** The model predicts labels derived independently from its own activations. No intervention was imposed, but the scoring key predates the answer. Input-only and semantic baselines remain essential.
- **AE c03 — out.** Intervention status is known, but there is no correct externally scored answer to the consciousness query. Retain the present `ambiguous` treatment unless the claim is split into a causal intervention-to-answer-rate measurement and the unverified content of the answer.
- **Lederman c02 — out when the answer concerns another model’s transcript.** It is a third-person behavioural control, not the reporting model’s self-answer. Any own-intervention trials should be extracted separately.

**Confidence:** high.

## Q6

**Recommendation — HIGH:** Require a preregistered, trial-level study combining the three instruments in the same systems and intervention family.

The dataset should contain randomized intervention/sham labels, matched transcript-only observer answers, untrained and report-trained target answers, confidence, probe values, held-out directions and layers, prompt paraphrases, gaslighting controls, and targeted perturbations of the proposed report-coupled mediator. The decisive analysis would test whether the untrained target has a reproducible observer advantage and whether causal, trial-level internal coupling explains that advantage.

The attached library contains partial components: Ferrara c04 supplies trained-channel validation; Lederman c02 supplies a third-person control; Singh supplies input-only or probe baselines; Macar supplies mechanism interventions. No listed study combines all three in one powered design. A positive result would justify a class-specific ruling, not a universal ruling for all self-reports. Observer-level performance, absent coupling, or success only after report training would count against ordinary self-access.

**Argument against:** Even this design may identify privileged causal information flow without determining whether `behavioural` or `interpretability` is the better schema label; that remains partly a taxonomic judgment.

**Confidence:** high.

FINAL: option B, confidence high
