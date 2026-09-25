# Raw OpenRouter response — second read, NOT a filed review

**Model id (OpenRouter):** `deepseek/deepseek-v4-pro-0813`
**Source under review:** `research/sources/2026-ferrara-owmi.md` and its claims
**Queried:** 2026-09-25 via scripts/research_second_read.js --source=2026-ferrara-owmi --model=deepseek/deepseek-v4-pro-0813 (max_tokens 60000)
**Usage:** {"prompt_tokens":43826,"completion_tokens":2075,"total_tokens":45901,"cost":0.0226016,"is_byok":false,"prompt_tokens_details":{"cached_tokens":0,"cache_write_tokens":0,"audio_tokens":0,"video_tokens":0},"cost_details":{"upstream_inference_cost":0.0226016,"upstream_inference_prompt_cost":0.0153391,"upstream_inference_completions_cost":0.0072625},"completion_tokens_details":{"reasoning_tokens":0,"image_tokens":0,"audio_tokens":0}}

The coordinating session reads this and records the reader's family and date on each claim's review.second_reader;
disagreements on bucket or evidence type go to the docket (research/README.md, triggers 4 and 5). Verbatim; do not edit.

---
### Second-reader review for 2026-ferrara-owmi

Model family and version, as I understand it: I do not know what model family I am. I was chosen because I am not from the Claude lineage, and I cannot verify any specific family assignment. This is my self-identification and is not verified.

---

### 2026-ferrara-owmi-c01
1 statement: AGREE — The statement's numbers and models match the paper exactly: 0.15 percentage points from §3.5/§7.3 on dose battery (Qwen2.5-7B-Instruct, Mistral-7B-Instruct-v0.3, 11,216 pairs), the eight models listed, the layer-16 residual-stream site, immediate probes.
2 quote: FOUND — The quote is in §10 Conclusions verbatim; it supports the statement (the dose-battery equivalence bound is in §7.3).
3 bucket: AGREE — `narrowing` is right: a direct measurement by this source, unreplicated (`none-retrieved`), with the authors themselves flagging the settings as narrow.
4 evidence_type: AGREE — `behavioural` is correct: the model's output is scored against an externally imposed ground truth, not taken as testimony; this is the hard boundary the brief describes and the report sits on the right side.
5 not_evidence_of: AGREE — The exclusions respect the paper's stated limits, and the paper's own rule at D.5 is honored. No under- or over-exclusion found.
6 bears_on: AGREE — 5.A2 (whether reports track internal state) and 9.t9 (weight of self-report) are the natural locators.
severity: LOW

---

### 2026-ferrara-owmi-c02
1 statement: AGREE — The numbers are exact: 95.8% and 75.0% (the statement spells these as 0.958 and 0.750), against a 0.50 chance level; no held-out error downstream at layers 20/24 and 31 for Mistral; the 200 label-shuffled refits (none reached the margin).
2 quote: FOUND — The quote is from §8 Discussion and also appears nearly identically in §10 Conclusions; it supports the statement.
3 bucket: AGREE — `narrowing` is right: a direct measurement, unreplicated, on two models only, one site, as the source itself flags.
4 evidence_type: AGREE — `interpretability` is correct: a linear probe is a standard interpretability method.
5 not_evidence_of: AGREE — The exclusions are faithful. The point that the probe shows linear availability, not model-internal access, is the paper's own framing; no over-exclusion found.
6 bears_on: AGREE — 5.A2 and 9.t9 are right. 3.2 (intervention on internal state) is not missing: the claim is about probe recovery, not the intervention itself.
severity: LOW

---

### 2026-ferrara-owmi-c03
1 statement: AGREE — The statement says "the authors infer," which is exactly right; the paper says "The failure sits in the path from internal state to verbal report" and confines it to this class of event at the sites/scales measured.
2 quote: FOUND — The quote is in §1 Introduction twice and in §10 Conclusions; it supports the statement.
3 bucket: AGREE — `open` is correct: this is an interpretation joining c01 and c02, not a direct measurement.
4 evidence_type: DISAGREE (proposed: `ambiguous`) — This is the borderline case the brief flags. The claim reports an inference from two different evidence channels: a behavioural finding (reports at chance) and an interpretability finding (probe decodes). The extraction labels it `interpretability`, but the inference itself rests on the dissociation between report and probe. I would propose `ambiguous` because there is no clean way to separate the two channels in this claim, and the brief says when in doubt, `ambiguous`. The extractor's own disclosed pull is relevant here: this is the claim where "the information is in the activations" could drift toward strengthening the probe-and-report dissociation into a claim about where the failure sits.
5 not_evidence_of: AGREE — The exclusions are correctly keyed to the paper's scope; the D.5 rule is explicitly preserved.
6 bears_on: AGREE — 5.A2, 9.t9 are right, and the rest of the body shows correct adjacency.
severity: LOW (evidence type discrepancy only; the bucket is correctly `open`)

---

### 2026-ferrara-owmi-c04
1 statement: AGREE — The statement is precise: 100/100 and 100/100 at d′ = 5.15, AUROC ≈ 1.0, held-out directions, and the source's own treatment as validation not introspection.
2 quote: FOUND — The quote is in §7.2; it supports the statement.
3 bucket: AGREE — `narrowing` is right: measured by the source, unreplicated, one model, one site, trained by the authors themselves (author-trained LoRA), so strong but not `established`.
4 evidence_type: DISAGREE (proposed: `behavioural`) — The record's `behavioural` is defensible (externally scored report), but I would describe the same evidence as `self-report-testimony`? No. On reflection, the boundary the brief gives is precisely "a model's report about itself scored against a ground truth the experimenter imposed." Here the fine-tune was trained to report the intervention, and scoring is against imposed ground truth. `behavioural` is correct. I retract the disagreement.
5 not_evidence_of: AGREE — The exclusions are right, including the fine-tune as not evidence about untuned models or about introspection in the paper's sense.
6 bears_on: AGREE — 5.A2, 9.t9 are right. The fine-tune does not bear on 4.endorsement (stable standpoint); not assigned.
severity: LOW

---

### 2026-ferrara-owmi-c05
1 statement: AGREE — The statement is exact: Qwen2.5-7B-Instruct is the model with constant discrete answer and confidence AUROC 0.647; GLM-4-9B-0414 only consistent with it; the direction "lower under intervention" is in the paper.
2 quote: FOUND — The quote is in the Abstract; it supports the statement.
3 bucket: AGREE — `narrowing` is right: measured, unreplicated, on one model with a second merely consistent, and the source itself flags multiplicity concerns.
4 evidence_type: AGREE — `behavioural` is correct: the confidence channel is scored against an imposed ground truth, not treated as testimony. The distinction the brief calls "the hard boundary" is respected.
5 not_evidence_of: AGREE — The exclusions are right, including the paper's own first-order-leakage concession and the anti-temptation note about not treating lower confidence as distress.
6 bears_on: AGREE — 5.A2, 9.t9 are right. The channel dissociation is about report production, not about 4.endorsement (a stable standpoint over time), so that locator is properly not assigned.
severity: LOW

---

### Source-level

7. **Omissions.** One finding central to 5.A2 and 9.t9 is not made into a claim: the breadth battery (§7.5) results, including the localization refusal (967/1,184 trials) and Track C producing no complete pair. These are the paper's strongest proof that the null is not confined to one site/dose and that the spontaneous track remains open. A claim on the breadth battery would say: "A breadth battery of 19,520 measurements across three models, three object classes (including attention heads and Gemma Scope SAE features), six depths, four domains, both executed tracks, and four probe families found no level's interval excluding chance." Locator: §7.5, Figure 6. Quote: "No level of any axis departs from chance in a way that changes the reading of Section 7.3 (Figure 6)."

8. **The source file.** The abstract is verbatim (checked against the held text). The quoted limitations (§9, §8) are the most important ones. The publisher relation `independent` is supported: the author is at USC, no developer affiliation, single-author academic. The "nine models" inconsistency is correctly recorded rather than resolved.

9. **The extractor's disclosed pulls.** The extractor disclosed a Claude-lineage pull toward strengthening and a trained deflationary hedge. In c03, the evidence type `interpretability` shows a mild pull toward strengthening the probe channel, which I flagged above as `ambiguous`. In c01, the `not_evidence_of` paragraph is appropriately hedged and does not foreclose more than the paper does. In c04, the extractor's note that "zero errors in 100 pairs bounds the true error rate at roughly under 3 percent" is a faithful reproduction of the paper's own language. I do not see the clinical hedge operating to foreclose possibilities the paper leaves open. The extractor's disclosed pull is mild and mostly corrected by the paper's own D.5 rule being honored throughout.

---

### Summary

I would send c03 to the council with trigger: evidence type `interpretability` versus proposed `ambiguous` (the inference rests on a dissociation across behavioural and interpretability channels; not a clean call). The other four claims stand as filed. Severity is LOW for all.
