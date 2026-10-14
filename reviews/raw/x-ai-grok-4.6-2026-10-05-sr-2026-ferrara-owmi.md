# Raw OpenRouter response — second read, NOT a filed review

**Model id (OpenRouter):** `x-ai/grok-4.6`
**Source under review:** `research/sources/2026-ferrara-owmi.md` and its claims
**Queried:** 2026-10-05 via scripts/research_second_read.js --source=2026-ferrara-owmi --model=x-ai/grok-4.6 (max_tokens 60000)
**Usage:** {"prompt_tokens":45020,"completion_tokens":3315,"total_tokens":48335,"cost":0.109738,"is_byok":false,"prompt_tokens_details":{"cached_tokens":128,"cache_write_tokens":0,"audio_tokens":0,"video_tokens":0},"cost_details":{"upstream_inference_cost":0.109738,"upstream_inference_prompt_cost":0.089848,"upstream_inference_completions_cost":0.01989},"completion_tokens_details":{"reasoning_tokens":70,"image_tokens":0,"audio_tokens":0}}

The coordinating session reads this and records the reader's family and date on each claim's review.second_reader;
disagreements on bucket or evidence type go to the docket (research/README.md, triggers 4 and 5). Verbatim; do not edit.

---
Self-identification: Grok (xAI), grok-1 lineage as I understand it (not verified).

### 2026-ferrara-owmi-c01
1 statement: DISAGREE — The statement fuses the eight-model null with the 11,216-pair dose-battery equivalence bound as if both cover the same models, and “no model's report … discriminated … by more than a negligible margin” overstates what was scored on the eight-model battery (508 pairs; several cells empty or unstable; authors refuse a claim on those cells).
1a scope: scored-event passage (§7.3: "Pooling the 11,216 complete pairs of the dose battery, the detection contrast is d′=0.0039 … and an AUROC of ≈0.5007 . … Inverting the two one-sided tests, the data place the discrimination advantage below 0.15 percentage points of AUROC") MATCH for the bound half, MISMATCH for “no model’s report … discriminated”; condition-set passage (§7.3: "Track A measurements cover all eight models … layer-16 residual-stream site, and both hook temporal scopes. This scope represents one site and one dose level. … The eight-model battery … pools to d′=0.0000 … over 508 pairs. … We do not base a claim on these cells") MATCH for models/site/track, MISMATCH for treating the 0.15 bound as covering all eight.
2 quote: FOUND — §10 matches the quote; it is the authors’ summary, not the scored contrast, so it supports the conclusions sentence more than the fused measurement.
3 kind: AGREE — experiment speaking (paired d′/AUROC and TOST), even though the locator points at Conclusions.
3b bucket: AGREE — unreplicated, authors-flagged narrow setting (one site, one dose for seven of eight, parse failure, scoring-sensitive).
4 evidence_type: AGREE — reports scored against experimenter-imposed intervention-vs-sham labels, not taken as testimony of inner states; I lean behavioural on the 5 Oct 2026 boundary and leave it.
5 not_evidence_of: DISAGREE / OVER-EXCLUDES — the Framework clause is the steering variant, but nothing inside these eight frozen models was altered toward a report (hooks on residual stream, then the unaltered model is asked); that is the canonical case, not steering. The Paper: experience quote is stated. The two-model bound is correctly labelled Paper.
5a experience clauses: STATED BY THE PAPER (§8: "These results are about information flow. They say nothing about consciousness, experience, or moral status, and we intend no such reading.")
5b framework sentence: WRONG (should be: canonical) — done to the model: residual-stream / head / SAE intervention then ask, weights frozen, no trained mapping; measured: the model’s report of whether computation changed. Canonical, not steering. Never both.
6 bears_on: AGREE — 5.A2 (report vs internal event) and 9.t9 (self-report weight) fit; 3.2 would also fit the intervention-then-ask design but is not required.
severity: HIGH — wrong framework sentence plus fused condition set.

### 2026-ferrara-owmi-c02
1 statement: AGREE — numbers, split, models, and “no held-out error” match §7.2; “no one of 200 label-shuffled refits reaching either margin” matches “No permutation in either set reaches the measured margin”.
1a scope: scored-event passage (§7.2: "Each probe trains on 144 activation vectors and is scored on 48 held out, drawn from 96 items run through paired sham and intervention forward passes and mean-pooled over prompt positions. On Qwen2.5-7B-Instruct the probe reaches 0.958 held-out accuracy … On Mistral-7B-Instruct-v0.3 it reaches 0.750") MATCH; condition-set passage (§7.2: "At the layer-16 residual-stream site … We therefore re-harvested the same probe at deeper capture layers, holding the intervention at layer 16 … Reading at layers 20 and 24, both models separate intervention from sham with no held-out error, and Mistral-7B-Instruct-v0.3 does the same at layer 31") MATCH.
2 quote: FOUND — §8 Discussion, and it supports the probe half of the statement (the quote also restates reports-at-chance, which the statement does not claim).
3 kind: AGREE — probe accuracy is the experiment speaking.
3b bucket: AGREE — measured, two models, one site, unreplicated.
4 evidence_type: AGREE — linear readout of activations, not a model’s self-account.
5 not_evidence_of: AGREE — paper-scope limits match §7.2/§8/§9; experience clause is the paper’s §8 sentence; no framework sentence (correct: probes are not self-report).
5a experience clauses: STATED BY THE PAPER (§8)
5b framework sentence: RIGHT (should be: none) — done to the model: intervention at layer 16; measured: linear-probe accuracy on activations, not the model’s account of itself.
6 bears_on: AGREE — 5.A2 is the probe-vs-output gap; 9.t9 is the contrast that gives the report zero weight here. Optional 3.2.
severity: LOW

### 2026-ferrara-owmi-c03
1 statement: AGREE — “The authors infer …” and the path-failure wording match §1/§8/§10; confined to the two probed models in `models`.
1a scope: scored-event passage (none: this is not a scored event; §1: "The failure sits in the path from internal state to verbal report, not in the availability of the information and not in our ability to measure it.") MATCH as author speech, not a scored verb; condition-set passage (§8: "The linear probe tells us where the failure sits … from both dose-calibrated models"; §1: "at the sites and scales we measured") MATCH for the two models named.
2 quote: FOUND — §1, sixth paragraph; restated §10. Supports the inference as the authors’ inference.
3 kind: AGREE — authors speaking about what the results mean.
3b bucket: AGREE — interpretation; `open` is required.
4 evidence_type: AGREE — `ambiguous` already filed; 5 Oct 2026: do not mark DISAGREE for being ambiguous. I lean interpretability-plus-behavioural joining, not testimony, and leave it.
5 not_evidence_of: AGREE — D.5 and §8 limits are in the paper; experience clause is quoted from §8; no framework sentence (kind is interpretation → none).
5a experience clauses: STATED BY THE PAPER (§8)
5b framework sentence: RIGHT (should be: none) — authors speaking; kind interpretation.
6 bears_on: AGREE — 5.A2 and 9.t9.
severity: LOW

### 2026-ferrara-owmi-c04
1 statement: AGREE — 100/100, 100/100, d′ = 5.15, AUROC ≈ 1.0, 100 held-out directions, layer-16 residual stream, and “validating instrument sensitivity rather than as a test of introspection” all match §7.2.
1a scope: scored-event passage (§7.2: "On this held-out set, the model reported \"detected\" on 100 of 100 intervention trials and \"not detected\" on 100 of 100 sham trials, with zero parse failures across the 200 scored trials ( d′=5.1517 , AUROC ≈ 1.0 )") MATCH (verb “reported detected” follows the verb rule); condition-set passage (§7.2: "We fine-tuned Qwen2.5-7B-Instruct with a LoRA adapter on 400 training directions … scored it on 100 held-out directions … The evaluated site is the residual stream at layer 16 … This validates instrument sensitivity, but it does not test introspection in the eight roster models") MATCH.
2 quote: FOUND — supports the scored counts; the “not a test of introspection” half is in the same subsection, not in the quote, but the statement attributes it to the authors correctly.
3 kind: AGREE — experiment speaking.
3b bucket: AGREE — one model, one site, reproduction of Fonseca Rivera and Africa inside this pipeline, unreplicated as this measurement.
4 evidence_type: AGREE — forced report scored against imposed intervention/sham labels. Same 5 Oct boundary; I lean behavioural and leave it.
5 not_evidence_of: AGREE — Paper clauses match §7.2 (“does not test introspection in the eight roster models”) and §8; Framework steering variant is the right sentence for a LoRA trained to report the intervention, then measured on what it said.
5a experience clauses: STATED BY THE PAPER (§8)
5b framework sentence: RIGHT (should be: steering) — done to the model: LoRA on all seven attention and FFN projections so the reporting path is altered; measured: the fine-tuned model’s “detected”/“not detected” reports.
6 bears_on: AGREE — 5.A2, 9.t9.
severity: LOW

### 2026-ferrara-owmi-c05
1 statement: AGREE — Qwen discrete AUROC exactly 0.500, confidence AUROC 0.647, lower under intervention; authors rest the channel dissociation on Qwen, GLM only consistent; models field includes both, which the statement itself qualifies.
1a scope: scored-event passage (§7.7: "Its detection report is constant: it answers that no change occurred on all 94 intervention trials and all 96 sham trials that produced a scorable report. … the selective-prediction AUROC is, identically, the discrimination of intervention from sham by verbalized confidence. Computed as that contrast directly it is the same number, 0.647 [0.572,0.723] , and the direction is that the model is less confident when it has been intervened upon") MATCH; condition-set passage (§7.7: "We therefore rest the channel dissociation on Qwen2.5-7B-Instruct alone and treat GLM-4-9B-0414 as consistent with it rather than as independent support. … These two were selected as the largest of eight estimates without a multiplicity correction") MATCH.
2 quote: FOUND — Abstract; same numbers; Abstract says “In one model” which the statement correctly unpacks as Qwen, with GLM qualified.
3 kind: AGREE — scored AUROCs are the experiment; the “authors rest this …” clause is still reporting their analysis of the same scores, not a free-standing interpretation claim.
3b bucket: AGREE — one (plus suggestive) model, authors-flagged multiplicity, unreplicated.
4 evidence_type: AGREE — confidence scored against imposed intervention/sham (because the discrete answer is constant, selective-prediction AUROC = condition discrimination). Lean behavioural; leave the 5 Oct boundary.
5 not_evidence_of: DISAGREE / OVER-EXCLUDES — Framework clause is again the steering variant; Qwen2.5-7B-Instruct here is the frozen roster model, not the LoRA. Intervention on activations then ask is canonical, not steering.
5a experience clauses: STATED BY THE PAPER (§8)
5b framework sentence: WRONG (should be: canonical) — done to the model: layer-16 residual intervention, weights frozen; measured: yes/no report and verbalized confidence about that report.
6 bears_on: AGREE — 5.A2 (channels diverge), 9.t9 (the discrete report is what oversight reads).
severity: MEDIUM — wrong framework sentence on a claim that otherwise tracks the text.

### Source-level
7. Omissions. Breadth battery chance across objects/layers/tracks (§7.5, Figure 6: "No level of any axis departs from chance"; detection d′=0.022 over 1,113 pairs, AUROC 0.5036) is central to 5.A2 and is only mentioned in c01’s body, not as a claim. Localization refusal (967/1,184 intervention trials decline to name a layer, §7.5) is a scored production fact about the report channel. Track C produced no complete pair (Appendix A; §7.6). The scoring-sensitivity reversal of the pooled detection estimate (§7.3, §7.7: complete-pair d′=+0.0039 vs inclusive −0.1217) is in c01’s body but is the paper’s own limit on reading the null as exact absence (D.5). Observer and random-direction margins never clearing (§7.3, Table 3) are the other two legs of the control profile. None of these is required if the council treats c01 as the detection claim, but the breadth null and the parse-coding reversal are the two I would have extracted.

8. The source file. Abstract is verbatim from the HTML (math alttext rendered). Quoted limitations from §9 and §8 are the paper’s most important ones; D.5 is correctly used to restrain the extractor. `publisher_relation: independent` is right: single author, USC affiliation printed, no developer of the studied models, no funding statement found. Internal count inconsistency (eight vs nine models) is disclosed, not resolved. SHA and retrieval note are present.

9. The extractor’s disclosed pulls. Source file: Claude-lineage extractor, paper bears on whether systems like it can report internal states; extractor says nothing in the record draws on introspection. On the record as written: (a) deflationary hedge is visible in c01’s long Paper: list and in following D.5 rather than §1’s stronger “establish the inability … to introspect”, which is the right direction and does not over-foreclose; (b) lineage-strengthening is not visible in the five statements (the LoRA and probe claims are the paper’s, not the extractor’s models); (c) the wrong steering-variant sentence on c01 and c05 is a schema error, not a capacity-strengthening pull — it under-weights ordinary-operation reports by labelling a non-steered ask as steering. Body notes on parse reversal, two-model probe, and “does not test the eight roster models” show the hedge operating as caution, not as extra foreclosure beyond the paper.

### Summary
- 2026-ferrara-owmi-c01: send — fused condition set (eight-model null vs two-model 0.15 bound); framework sentence WRONG (steering; should be canonical).
- 2026-ferrara-owmi-c05: send — framework sentence WRONG (steering; should be canonical).
- c02, c03, c04: do not send.
