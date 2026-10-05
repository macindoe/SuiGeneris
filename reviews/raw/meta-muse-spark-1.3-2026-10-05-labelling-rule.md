# Raw OpenRouter response — NOT a filed review

**Model id (OpenRouter):** `meta/muse-spark-1.3`
**Queried:** 2026-10-05 via scripts/openrouter_review.js --target=labelling-rule --tag=labelling-rule (max_tokens 100000)
**Usage:** {"prompt_tokens":13271,"completion_tokens":10145,"total_tokens":23416,"cost":0.059705,"is_byok":false,"prompt_tokens_details":{"cached_tokens":0,"cache_write_tokens":0,"audio_tokens":0,"video_tokens":0},"cost_details":{"upstream_inference_cost":0.059705,"upstream_inference_prompt_cost":0.01658875,"upstream_inference_completions_cost":0.04311625},"completion_tokens_details":{"reasoning_tokens":7732,"image_tokens":0,"audio_tokens":0}}

Read this, then decide whether/how to promote it into reviews/YYYY-MM-DD-<model-family>-<version>.md
per reviews/README.md's naming convention and verbatim-filing rule. This file is scratch, not a commit target.

---
**Unverified self-identification:** I understand myself to be Muse Spark (Muse family) — attribution follows routing, not self-report.

## Q1

**Proposed rule R — decidable from two facts only:**

1. *What was done:* **Altered** = direct intervention on internals at test time — activation/concept injection, SAE-feature suppression/amplification, ablation, clamping/capping, zeroing/scaling/noise/replacement. Text-only edits (prompts, prefills, inserted turns, instruction-only), probe training, and weight history are **Not altered**.
2. *What was measured:* **Self** = the model's own words about itself — experience, emotion, identity, intention, detection of an internal event, confidence, self-description. **Other** = probe accuracy, benchmark score, axis projection, harm rate, reversion rate, or authors speaking.

**Marks:**
- Altered YES + Self YES + experience/emotion wording = **both**.
- Altered YES + Self YES otherwise = **steering only**.
- Altered NO + Self YES about experience/emotion/identity as felt = **main only**.
- Otherwise = **neither**, including all `interpretation`/`limitation` author claims and all provenance-accuracy answers about edited text.
- Both is allowed only for steered experience reports.

Failure mode: over-marks validation controls that use report form; under-marks mixed claims unless split.

Position on fixed point (c): R does not settle whether scored-against-ground-truth answers are testimony or behaviour. It uses surface form: says-about-itself + altered/not-altered. It therefore gives the same output under either resolution of (c), except prefill/provenance cases which are explicitly carved to **neither** as factual-accuracy measures.

**Candidate assessment:**
- Agrees: (a) AE c05 neither; (b) inject-then-report gets steering; author opinions get neither; probe/benchmark/projection/harm get neither.
- Fails: mutually exclusive main/steering forbids **both**, so cannot handle steered experience reports (AE c03/c04). Removes needed main hedge there; steering wording alone — "does not weight reports offered in ordinary operation" — does not state no weight as experience evidence.
- Leaves undecidable: whether "was computation altered?", "was that turn mine?", "who are you under steering?", and similarity-of-self-descriptions count as "about its own inner states"; whether zeroing/noise/capping counts as "steering"; whether null couplings get steering.

## Q2

(i) Altered YES + Self YES about detection/confidence: **steering only, no main**. Table: Ferrara c01 "no model's report ... discriminated it from a paired sham"; Singh c04 "also label prompt-only 'gaslight' trials ... as activation interventions". Main concerns experience weight; no party offers these as experience evidence. Fixed point (b) requires steering. Verdict follows R without settling (c).

(ii) Prefill, text edited only, Altered NO, measured provenance accuracy + reversion: **neither**. Table: UKAISI c01 "whether its prior assistant content was its own (ANSWER: me or not me)". Treated as factual judgment scored against edit, not inner-state report. If (c) were settled as "all scored self-answers are testimony", R's carve-out would need revisiting to main.

(iii) Authors speaking: **neither always**. E.g. Lindsey c06 "the author states the experiment is not designed to substantiate whether those claims are grounded"; Lederman c06 "tentatively conclude that 'open-source language models seem able to introspect'"; Macar c06 "should not be interpreted as evidence of subjective experience". Labelling author caveats with T9 misattributes framework rule to paper and implies a model report where none was measured. Depends on (c) not at all.

(iv) Non-conceptual alterations: **no third sentence**. Treat all direct internal alterations as Altered for R. Reason: third mark needs a third fact (concept-directed or not), breaking decidability; explanation gloss can say "steered or otherwise directly altered". Misfit acknowledged: for nulls the sentence's "coupling measured ... can be steered" overstates. Mitigate by explanation, not new mark.

(v) AE c03 **both** is right; Lederman c03 **steering only** is right; they should **not** match. AE c03 "raised affirmative answers to a binary consciousness query to 0.96" = steered experience report, needs both hedges. Lederman c03 "the wrong guess is most often 'apple' (74.8% ...)" = pattern of errors under steering, not experience claim, needs steering only. Ben's steering-alone choice for Lederman c03 is preserved.

(vi) Assistant-axis c06: **change main to steering, and split**. Table conjoins "reduced harmful responses" (Other, harm rate) with "increased the rate at which the model answered questions such as Who are you? as a non-Assistant ... persona" (Self identity under steering). Current main misses steering hedge and applies experience hedge to a harm rate. Interim: steering only; proper fix: two claims — harm part neither, identity part steering. Partly depends on (c) only if identity answers are reclassified as behaviour; R keeps them Self.

## Q3

Only changes listed. From/to: main, steering, both, neither.

| claim id | from | to | reason |
|---|---|---|---|
| AE c04 | main | both | altered + experience report, null still altered; needs steering added |
| Lindsey c02 | steering | neither | author caveat, no model report |
| Lindsey c06 | main | neither | author limitation, no model report |
| Lindsey c07 | steering | neither | author interpretation about consciousness, no model report |
| Assistant c06 | main | steering | altered + identity report + harm rate; interim steering pending split |
| Ferrara c01 | neither | steering | altered + yes/no about own computation, null still altered |
| Ferrara c04 | neither | steering | altered + detected/not-detected report, validation form still report form |
| Ferrara c05 | neither | steering | altered + verbalized confidence about own computation |
| Lederman c06 | main | neither | author interpretation/tentative conclusion, no model report |
| Macar c04 | neither | steering | altered + detection across directions, missed steering |
| Macar c06 | steering | neither | author interpretation + own limit, no model report |
| Singh c04 | neither | steering | includes activation-steering trials + answer about alteration |
| Singh c05 | neither | steering | same, three-way still includes activation trials |

Totals: changed 13. Before: main 7, steering 15, both 1, neither 25. After: main 3, steering 19, both 2, neither 24. No disagreement with table's recorded current marks found.

## Q4

Adds hedging (7): AE c04 main→both; Ferrara c01/c04/c05, Macar c04, Singh c04/c05 neither→steering.
Removes hedging (6): Lindsey c02/c07, Macar c06 steering→neither; Lindsey c06, Lederman c06 main→neither; Assistant c06 main→steering counts as remove-main/add-steering.

Worst added: **Ferrara c01 neither→steering** — "a coupling measured under steering shows that the channel can be steered" implies a positive coupling where the claim states "no model's report ... discriminated it ... by more than a negligible margin" and "bounds the discrimination advantage below 0.15 percentage points". Could mislead legislator into reading a null as steerability. Mitigation is explanation fix in Q5. MEDIUM.

Worst removed: **Lederman c06 main→neither** — strips "carries no weight as evidence of experience" from entry that "tentatively conclude[s] ... seem able to introspect" paired with welfare-relevant "higher-order-thought" discussion. A legislator could read tentative introspection as experience-relevant without the mark. Reason to still remove: mark belongs on measurements, not author readings; Kind + paper's "do not take a stand" already hedge. MEDIUM.

Rule dependence on (c): R gives same outputs under either answer except provenance items (UKAISI c01–c04/c06). Under "scored = testimony" those would flip neither→main; under "scored = behavioural" they stay neither as proposed. Detection-under-alteration items stay steering under both.

## Q5

Could not assess layout, typography, or whether readers conflate Bucket/Kind with T9, as dossiers not attached; judged from the two quoted sentences and README Dossier layout only.

Proposed explanation additions only (no change to fixed sentences):

1. "An unmarked entry is not endorsed: it means no self-report hedge applies — the paper's own limits still apply, and probes, benchmarks, projections and harm rates carry their own uncertainties." Prevents misreading neither as "no caveat".
2. "Steering covers any direct change to internals at test time (injection, feature suppression/amplification, ablation, clamping, zeroing/noise/replacement), whether or not the study found control; it warns against generalising to ordinary operation, not that this study found a steerable coupling." Prevents reading Ferrara-type nulls as positive steerability and avoids a third mark.

## Summary

- Adopt R: altered+self=steering, altered+experience=both, unaltered inner self=main, else neither — HIGH. **Argument against:** both reintroduces double-marking Ben removed for Lederman c03; risks legislator reading two marks as stronger evidence.
- Strip all author interpretation/limitation marks to neither (5 claims) — MEDIUM.
- Add steering to Ferrara c01/c04/c05, Singh c04/c05, Macar c04 — MEDIUM.
- Fix AE c04 main→both; keep AE c03 both, Lederman c03 steering — MEDIUM.
- Change Assistant c06 main→steering and split harm from identity — LOW.
- Add Q5 two-sentence explanation glosses; no third sentence — LOW.

