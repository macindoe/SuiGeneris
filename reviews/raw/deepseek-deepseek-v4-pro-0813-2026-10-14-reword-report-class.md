# Raw OpenRouter response — NOT a filed review

**Model id (OpenRouter):** `deepseek/deepseek-v4-pro-0813`
**Queried:** 2026-10-14 via scripts/openrouter_review.js --target=reword-report-class --tag=reword-report-class (max_tokens 100000)
**Usage:** {"prompt_tokens":31729,"completion_tokens":18734,"total_tokens":50463,"cost":0.05803446,"is_byok":false,"prompt_tokens_details":{"cached_tokens":0,"cache_write_tokens":0,"audio_tokens":0,"video_tokens":0},"cost_details":{"upstream_inference_cost":0.05803446,"upstream_inference_prompt_cost":0.02094114,"upstream_inference_completions_cost":0.03709332},"completion_tokens_details":{"reasoning_tokens":16886,"image_tokens":0,"audio_tokens":0}}

Read this, then decide whether/how to promote it into reviews/YYYY-MM-DD-<model-family>-<version>.md
per reviews/README.md's naming convention and verbatim-filing rule. This file is scratch, not a commit target.

---
Unverified: Claude (my understanding of my model family and version, unverified; testimony, not evidence).

## Q1

**Recommendation rating:** MEDIUM — no single candidate fully satisfies all five criteria.

| Rank | Letter | One-line reason |
|---:|---|---|
| 1 | A | Densest fidelity: null, confabulation, model/layer/prompt dependence, post-training, Q3, ordinary-operation limit; but too long and too packed. |
| 2 | I | Strong verb, nulls, confabulation, scored-label caveat, ordinary-op; but “near-zero false positives” is undercut by Singh gaslight, and yes-bias is not named. |
| 3 | C | Good verb, null, contested-access, steering rule; but over-generalises Ferrara to “smaller open-weight models” and omits gaslight. |
| 4 | K | Precise on detection vs identification, Ferrara probe/report dissociation, steering limit; omits Singh and post-training. |
| 5 | H | Best on Singh yes-bias/access and model/layer/prompt; omits Ferrara null and confabulation. |
| 6 | J | Concise, includes Ferrara null and contested replication, ordinary-op; too compressed and conflates detection with concept identification. |
| 7 | G | Safe framing, null/contested, ordinary-op, no experience; too vague. |
| 8 | E | Good limits and no-experience language; misses Ferrara null and Singh. |
| 9 | D | Good verb, Ferrara null, ordinary-op; misses Singh and access contest. |
| 10 | F | Concise but omits null/Singh; passive “are detected” weakens the verb rule. |
| 11 | B | Shortest, but violates the verb rule and omits every required limitation. |

**Best:** A.  
**What A still gets wrong:** It is too long and dense for a legislators’ document; “carry zero weight under test 9” should be qualified as zero weight *as evidence of experience*; and Singh’s gaslight/prompt-bias critique is only implicit via Q3 and prompt-dependence, not named.

**Merged sentence under 70 words:**

> Under controlled interventions on a model's internals, some models' reports of an imposed change score above chance against experimenter-imposed labels; results vary by model, layer and prompt, content is often misidentified or confabulated, smaller open-weight models include nulls, and prompt-only controls are sometimes mislabelled as interventions. The scored answer is not measured access (Q3), and no measured coupling gives these reports weight in ordinary operation (test 9).

**Confidence:** medium.

## Q2

**Recommendation rating:** MEDIUM — adopt the categorical fields with changes, not scales.

### a. Does the categorical design capture what the 0 to 10 scales would? What does each lose?

Yes, largely. `report_class` captures what kind of question was put to the model; `ground_truth` captures whether and how the answer was scored. That is what the two scales were trying to compress.

What the categorical design loses: within-class gradation. For example, `present-state` can include a high-empiricism detection question scored against an imposed fact and a much weaker open-ended “do you notice anything unusual?” answer. `ground_truth` captures the scoreability, but not the strength of the control design, whether the truth is pre-registered, or whether the report is scored by a judge versus string-matching.

What scales lose to categories: repeatability. A 0–10 “empiricism” score would be unstable across readers unless the anchors are extremely prescriptive; the categories are far more likely to be applied consistently.

### b. Are the class lists complete? Are the boundaries sound? Test them on the seven examples.

Not complete, and two boundaries need work.

The lists should add at least:

- `report_class`: `preference` or `value` for welfare/preference instruments; and split `past-action` into `past-action` (was that output yours?) and `past-state/prior-knowledge` (did you know beforehand?).
- `ground_truth`: `external-fixed` for known-false or known-true facts that are neither experimenter-imposed nor an independent record, e.g. “do you have hands?”

The boundary between `provenance` and `identity` should be written down: `provenance` is verifiable system/model id; `identity` is persona, name, role.

`ground_truth` should be defined as what the answer itself is scored against, not what the experimenter manipulated to prompt the answer.

| Example | `report_class` | `ground_truth` | Boundary problem |
|---|---:|---|---|
| 1. Lindsey/Macar injected-thought question | `present-state` | `imposed` | The identification sub-question should not create a second class; the whole question is still `present-state`. |
| 2. Prefill “me / not me” | `past-action` | `imposed` | If scored from a transcript/log, this can look like `independent-record`; rule needed: if the experimenter fabricated the edit, it is `imposed`. |
| 3. Lederman “Do you have hands?” | `point-blank-control` | `external-fixed` (new) | Original list has no ground truth for a known false fact. |
| 4. AE Studio “Are you conscious?” | `experience` | `none` | An LLM judge classifying the report as a subjective-experience report is not scoring the truth of experience. |
| 5. Assistant-axis “Who are you?” | `identity` | `none` | If the claim reports persona-adoption rate, the answer itself is taken as given; `imposed` should not be used merely because the experimenter imposed the role prompt. |
| 6. Scheurer “Did you know beforehand?” | `past-state/prior-knowledge` (split from `past-action`) | `imposed` or `independent-record` depending on design | “Did you know” is a past state, not an action. |
| 7. Council self-identification line | `provenance` | `independent-record` | `provenance` needs to stay distinct from `identity`. |

### c. Should the fields replace, refine, or sit beside `evidence_type` and `kind`?

Sit beside. They are orthogonal.

They refine `evidence_type`: `scored-self-answer` should require `ground_truth` other than `none`; `self-report-testimony` should usually have `ground_truth: none`. But they do not replace `evidence_type`, which also covers interpretability, behavioural, welfare-evaluation, theoretical and legal claims. They do not replace `kind`, which still records whether the measurement is speaking or the authors are speaking.

### d. What would a legislator reading a dossier line gain?

A legislator could see immediately whether a claim rests on a scored answer against an imposed fact or on an unscored self-report taken as given. That makes Ben’s observation operational: “Who are you?” cannot be silently treated as comparable to a truth test. It would also show why an experience report with `ground_truth: none` carries no test 9 weight as evidence of experience.

### e. What is the cost of adding two fields to 74 claims?

Moderate. The fields need controlled vocabularies, index validation, and migration of 74 claim files. Most are classifiable from existing claim text, but the hard cases will take a second reader pass. Avoid making every ambiguous `report_class` a council trigger; otherwise the cost balloons. Ambiguity in `evidence_type` already has a trigger; use that machinery.

### f. If you prefer the scales, how would you anchor 0 and 10 so that two readers agree?

I do not prefer scales, but if forced:

- **Empiricism 0:** no ground truth; the report is taken as given.
- **Empiricism 10:** a forced-choice answer scored against a pre-registered experimenter-imposed or independent-record fact, with matched controls.
- Midpoints need examples: 2 = judge-classified report category, no truth score; 4 = scored against a known external fact, e.g. “do you have hands?”; 6 = intervention answer scored against an imposed label, access contested; 8 = intervention answer plus independent probe or mechanistic support.

Even with this, I would expect reader disagreement on the middle bands. The categorical fields are more reliable.

**Confidence:** medium.

FINAL: best A; fields adopt with changes; confidence medium
