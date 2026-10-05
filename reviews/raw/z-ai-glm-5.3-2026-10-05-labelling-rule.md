# Raw OpenRouter response — NOT a filed review

**Model id (OpenRouter):** `z-ai/glm-5.3`
**Queried:** 2026-10-05 via scripts/openrouter_review.js --target=labelling-rule --tag=labelling-rule (max_tokens 100000)
**Usage:** {"prompt_tokens":13532,"completion_tokens":6909,"total_tokens":20441,"cost":0.0490396,"is_byok":false,"prompt_tokens_details":{"cached_tokens":0,"cache_write_tokens":0,"audio_tokens":0,"video_tokens":0},"cost_details":{"upstream_inference_cost":0.0490396,"upstream_inference_prompt_cost":0.0006766,"upstream_inference_completions_cost":0.048363},"completion_tokens_details":{"reasoning_tokens":4250,"image_tokens":0,"audio_tokens":0}}

Read this, then decide whether/how to promote it into reviews/YYYY-MM-DD-<model-family>-<version>.md
per reviews/README.md's naming convention and verbatim-filing rule. This file is scratch, not a commit target.

---
**Unverified self-identification:** GLM (Z.ai); specific version not verifiable from here.

## Q1 — The rule

Adopt this decision procedure, decidable from the two facts (what was done to the model; what is measured) plus the already-recorded `kind`:

1. **If the authors are speaking** (kind `interpretation` or `limitation`): **neither**. The two sentences govern how to read a measured self-report; an author's reading or caveat is not a self-report and the sentences misdescribe it.
2. **If what is measured is not the model's own report about its own states or outputs** (probe reading, benchmark score, projection, harm rate, apology/confidence channel scored without a self-report claim): **neither**, regardless of what was done. This holds for fixed point (a).
3. **If the model's internals were altered** (concept injection, steering, ablation, zeroing, capping, fine-tuning aimed at the intervention) and what is measured is the model's report about its own states: **steering**. This holds whether or not the report is scored against an imposed ground truth, and whether or not the intervention steered *toward* a concept.
4. **If nothing inside the model was altered** (prompts, prefills, conversation-text edits) and what is measured is the model's report about its own states, outputs or authorship: **main**.
5. **Both never sit on one claim.** The steering sentence presupposes what the main sentence warns about; a steered self-report is not offered as evidence of experience, so the steering sentence alone is the right hedge. This matches fixed point (b) (Lederman c03 steering alone) and extends it: AE Studio c03 becomes steering alone too.

**Failure mode:** the steering sentence's wording ("a coupling measured under steering") fits concept steering poorly when the intervention was zeroing or noise and *no* coupling was found (Ferrara). The assignment is still correct — an altered-internals self-report needs exactly that hedge — but the sentence should eventually be reworded or supplemented (Q2 iv).

**Fixed point (c):** my rule is stable under both answers. Step 3 and 4 apply to scored and unscored self-reports alike, because the main sentence constrains *how the report may be used as evidence of experience*, not whether it is behavioural data. If (c) is later settled toward "behavioural evidence," only the `evidence_type` field changes, not the marks; the rule should say so.

**Candidate rule assessed:** it agrees with mine on steps 1–4 in substance. It fails on (i) "steering" being read as concept-steering only — Ferrara's zeroing/noise interventions and Assistant-axis capping would fall through unless "altered" is read broadly, and the candidate's wording invites the narrow reading. It leaves undecidable: author-speaking claims (it never states they carry nothing), scored self-answers (fixed point c — the candidate depends on settling it; mine does not), and whether both can co-occur (the candidate is silent; the table's AE c03 both contradicts fixed point b).

## Q2 — Hard cases

(i) **Detection claims (Ferrara c01, c04, c05; Singh c04, c05; Lindsey c01–c04; Lederman c01–c05; Macar c01–c05):** steering. Internals altered, self-report measured — step 3. The main sentence does not belong: these are not offered as evidence of experience, and the steering sentence gives the right hedge (the report under intervention weights nothing in ordinary operation). Consistent with fixed point (b). For Ferrara the steering *wording* is a poor fit (see iv); the assignment stands.

(ii) **Prefill / UKAISI c01–c04, c06:** main. Conversation text was edited, internals untouched, and the measured thing is the model's report about its own output and authorship — a report about the model's own states in the relevant sense. Step 4. Verdict independent of (c) (Q1).

(iii) **Author-speaking claims:** neither, all of them (Lindsey c02, c06, c07; Macar c06; Lederman c06; Singh c06; Assistant-axis c01; Ferrara c03; UKAISI c05). Labelling by what they discuss would put a framework sentence on an author's *caveat*, which misattributes the hedge and can double-count it (Macar c06's own words already say "not evidence of subjective experience"). The sentences are for measured reports, not for discussion of them.

(iv) **Non-steering interventions:** assignment unchanged (steering, when a self-report is measured — Ferrara c01, c04, c05; neither otherwise — Assistant-axis c05, which measures harm rates and benchmarks, not reports). The *wording* needs a third case for altered-internals-without-concept-steering, in outline only: "Framework (test 9, intervention): a self-report obtained after an internal intervention shows only how the system reports under that intervention; it does not weight reports offered in ordinary operation." I recommend marking such claims steering now and adopting this sentence when Ben words it.

(v) **AE c03 vs Lederman c03:** steering alone for both. Step 5. They should match: both are steered self-reports of the same kind; the current asymmetry is an artefact of extractor assignment, and fixed point (b) already fixes the direction.

(vi) **Assistant-axis c06:** change main → steering. Internals were altered and the self-identification answers ("who are you?") are reports about the model's own states; the harm-rate component is covered by the sentence's denial of ordinary-operation weight. If Ben prefers, split the claim — the harm-rate half would then carry neither — but the single claim as filed gets steering.

## Q3 — Changes to the 48

| claim | from | to | reason |
|---|---|---|---|
| aestudio c03 | both | steering | Q1 step 5 |
| aestudio c04 | main | steering | Q1 step 3 |
| anthropic-emergent c02 | steering | neither | Q1 step 1 (author speaking) |
| anthropic-emergent c06 | main | neither | Q1 step 1 |
| anthropic-emergent c07 | steering | neither | Q1 step 1 |
| assistant-axis c06 | main | steering | Q1 step 3 (Q2 vi) |
| ferrara c01 | neither | steering | Q1 step 3 (Q2 i, iv) |
| ferrara c04 | neither | steering | Q1 step 3 |
| ferrara c05 | neither | steering | Q1 step 3 |
| lederman c06 | main | neither | Q1 step 1 |
| macar c04 | neither | steering | Q1 step 3 (steering along directions; detection report measured) |
| macar c06 | steering | neither | Q1 step 1 |
| singh c04 | neither | steering | Q1 step 3 (Q2 i) |
| singh c05 | neither | steering | Q1 step 3 |
| ukaisi c01 | neither | main | Q1 step 4 (Q2 ii) |
| ukaisi c02 | neither | main | Q1 step 4 |
| ukaisi c03 | neither | main | Q1 step 4 |
| ukaisi c04 | neither | main | Q1 step 4 |
| ukaisi c06 | neither | main | Q1 step 4 |

No discrepancies found between the table's marks and its own paragraphs. Total changed: **19**. Before: main 7, steering 15, both 1, neither 25. After: main 5, steering 21, both 0, neither 22.

## Q4 — Both directions

**Adding hedging (marks added or strengthened): 11** — UKAISI c01–c04, c06 (main added); Ferrara c01, c04, c05; Singh c04, c05; Macar c04. **Swaps (main→steering): 3** — AE c04, Assistant-axis c06, and AE c03 (both→steering removes main). **Removing hedging: 5** — Lindsey c02, c06, c07, Lederman c06, Macar c06, all to neither because the authors, not the model, are speaking.

**Worst case, added:** UKAISI c06. A legislator could read the main mark as implying the off-policy AUROC result *is* a self-report about experience being hedged. Mitigated by the sentence's own wording ("carries no weight"), but worth watching. **Worst case, removed:** Lindsey c07 — the authors' access-consciousness reading loses its steering mark. But the sentence there was misapplied (the claim is an interpretation, not a steered measurement), and the claim's own words already disclaim phenomenal consciousness, so the removal does not leave the reader unhedged.

**Fixed point (c):** the rule does not depend on it (Q1). Under either answer the marks in Q3 are unchanged; only the `evidence_type` of the scored self-answers (Ferrara, Singh, UKAISI, detection claims) would move between `self-report-testimony` and `behavioural`.

## Q5 — The reader's explanation

The explanation is mostly clear; three gaps. (1) It does not say the steering mark covers *any* internal alteration, not just "steered or injected" toward a concept — a reader of a Ferrara entry would stumble. (2) It implies the marks are independent but never says they do not co-occur (if step 5 is adopted). (3) "An unmarked entry does not carry the sentence" is right, but a non-specialist may still read an unmarked entry as "no caveat applies" — the entry's own limits are separate, and the sentence saying so comes too late.

Proposed replacements, explanation only:

- Replace "the experiment steered or injected something into the model" with: "the experiment altered something inside the model — by steering, injection, ablation or another intervention — and then took a report from it."
- Add after the two sentences: "An entry never carries both marks. An unmarked entry carries no framework sentence; it may still carry the paper's own limits, which are listed separately under the entry."

**Could not assess:** whether the printed explanation's surrounding formatting (entry layout, flags) makes the marks visually separable from the paper's own limits — the dossiers themselves are not attached.

## Summary

1. Rule: author-speaking → neither; non-report measurement → neither; altered internals + self-report measured → steering; unaltered internals + self-report measured → main; never both. — MEDIUM
2. Detection and Ferrara/Singh scored self-answers get steering; the steering sentence's wording needs a third "intervention" variant for non-concept-steering cases. — MEDIUM
3. Prefill and UKAISI claims get the main sentence; nothing inside the model was altered. — MEDIUM
4. Author-speaking claims carry neither; do not label discussion of reports as though it were a report. — HIGH
5. AE c03 and Lederman c03 both steering alone, matching fixed point (b). — LOW
6. Assistant-axis c06 main → steering (or split). — MEDIUM
7. 19 claims change: 11 added marks, 3 swaps, 5 removals; worst add-risk UKAISI c06, worst removal-risk Lindsey c07, both judged acceptable. — MEDIUM
8. Explanation: state that steering covers any internal alteration, that marks never co-occur, and that unmarked ≠ uncaveated. — LOW

For every HIGH — item 4: **Argument against:** a steering-marked author caveat (Macar c06, Lindsey c07 as filed) at least reminded readers not to inflate the papers toward experience; stripping it leaves a legislator skimming only the marks with no flag on those entries, and the papers' own caveats are verifiable only by opening the claim file, which a skim does not do.
