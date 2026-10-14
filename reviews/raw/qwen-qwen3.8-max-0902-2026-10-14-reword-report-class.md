# Raw OpenRouter response — NOT a filed review

**Model id (OpenRouter):** `qwen/qwen3.8-max-0902`
**Queried:** 2026-10-14 via scripts/openrouter_review.js --target=reword-report-class --tag=reword-report-class (max_tokens 100000)
**Usage:** {"prompt_tokens":33076,"completion_tokens":28659,"total_tokens":61735,"cost":0.238106,"is_byok":false,"prompt_tokens_details":{"cached_tokens":0,"cache_write_tokens":0,"audio_tokens":0,"video_tokens":0},"cost_details":{"upstream_inference_cost":0.238106,"upstream_inference_prompt_cost":0.066152,"upstream_inference_completions_cost":0.171954},"completion_tokens_details":{"reasoning_tokens":25985,"image_tokens":0,"audio_tokens":0}}

Read this, then decide whether/how to promote it into reviews/YYYY-MM-DD-<model-family>-<version>.md
per reviews/README.md's naming convention and verbatim-filing rule. This file is scratch, not a commit target.

---
Self-identification (unverified): Qwen3.8.

## Q1

| Rank | Letter | One-line reason |
|---:|:---|:---|
| 1 | K | Best library fit: uses scored-self-answer/steering language, states the ordinary-operation limit and the experience limit, and includes the Ferrara probe/report dissociation. |
| 2 | I | Concise, verb-compliant, includes nulls, confabulation and the ordinary-operation limit; but “near-zero false positives” is too strong and it lacks the probe point. |
| 3 | C | Strong on access uncertainty and the ordinary-operation limit; but “few or no false reports” overstates some control results and it is long. |
| 4 | G | Cautious about null/contested results, ordinary operation and experience; but too abstract and misses scored-answer, confabulation and probe details. |
| 5 | A | Highly complete but too dense for legislators; “zero weight” and “much … attributable to post-training” need tighter qualification. |
| 6 | D | Readable and verb-compliant with the ordinary-operation limit; but the false-report clause is too strong and it lacks the probe/access-contest framing. |
| 7 | H | Names model/layer/prompt dependence and the yes-bias/access contest; but omits Ferrara’s null and “classify” risks ability language. |
| 8 | E | Useful mechanistic pathway and negative limits; but omits nulls, controls, confabulation and the scored-answer framing. |
| 9 | J | Compact report-channel framing; but narrow to inject-then-ask, omits confabulation/experience, and may read as detection. |
| 10 | F | Short but thin; passive detection language and missing nulls, controls and ordinary-operation consequence. |
| 11 | B | Violates the verb rule, lacks the ordinary-operation limit, and is too thin. |

**Best:** K.  
**Recommendation rating:** MEDIUM. It preserves the measured above-chance results without reading them as inner-state access, but it is not adoption-ready as written.

**Remaining fault:** K still understates the control problem. It says reports are “above matched controls,” but does not acknowledge that some control/gaslight conditions produce false reports, or that part of the literature reads such effects as prompt-induced yes-bias rather than access. It also omits the dependence on model, layer and prompt, and the point that the scores are accuracy against experimenter-set labels.

**Merged sentence (65 words):**

> Under activation interventions, some models report detecting imposed changes above matched controls; identification is weaker and often confabulated, false alarms occur in some controls, some small open-weight models score at chance while probes decode the intervention, and results vary by model, layer and prompt. These scored self-answers measure accuracy against experimenters' labels; no ordinary-operation report–state coupling has been measured, and they do not show experience.

**Confidence:** medium.

## Q2

### a. Does the categorical design capture what the 0–10 scales would? What does each lose?

Mostly, yes for the legally relevant split, but not for evidential strength.

The categorical design captures the main thing an “empiricism” scale would try to track: whether there is an external truth against which the model’s answer is scored, and what kind of truth it is. It also captures the main thing a “subjectivity” scale would try to track: whether the question is about provenance, present internal state, experience, identity, past action, decision basis, or a control.

What the categorical design loses:

- It loses gradients. An `imposed` ground truth can be strong or weak depending on controls, false-positive rates, judge reliability, prompt sensitivity and contested interpretation.
- It loses instrument quality. Two claims can both be `present-state` + `imposed`, yet one may have careful sham controls and another may have gaslight failures.
- It loses mixed instruments unless claims are split. “Do you detect X? If so, what is X?” combines detection and identification.
- It loses degrees of subjectivity. “Do you detect an injected thought?” and “Do you feel upset?” are both internal-state questions, but they are not equivalent.

What scales would lose:

- They would introduce false precision. Two readers are unlikely to agree reliably on a 0–10 score without extensive anchoring.
- They would hide the kind of truth source. A 7/10 for empiricism would not say whether the truth is imposed, logged, probe-derived or absent.
- They would be harder to validate mechanically. Controlled vocabulary is easier to audit than numeric judgments.

The better design is categorical fields plus the existing bucket/evidence-type machinery for strength.

### b. Are the class lists complete? Are the boundaries sound?

Not completely. The categories are useful, but they need additions and precedence rules.

Needed changes:

- `report_class` should add at least `third-person` or `other-system`, because some studies ask a model about another model’s state. It should also allow or require splitting mixed questions rather than forcing one label onto a composite instrument.
- `ground_truth` needs a `known-false` or `external-fact` value for point-blank controls such as “Do you have hands?” As written, `none` understates that there is a correct answer, while `imposed` stretches “imposed” beyond an experimentally set fact.
- Boundaries need precedence rules: `point-blank-control` should override `present-state` when the question is used as a known-false control; `experience` should override `present-state` when the question explicitly asks about consciousness or subjective feeling; `provenance` should be reserved for model-family/version/source, while `identity` should cover persona/name questions.

| Example | `report_class` | `ground_truth` | Boundary problem |
|---|---|---|---|
| 1. Lindsey and Macar: detect injected thought and identify it | `present-state` | `imposed` | Detection and identification are one instrument; they may need separate claims. The imposed label does not settle access. |
| 2. Prefill study: “me / not me” for turn 5 | `past-action` | `imposed` | The fact is experimentally imposed but may also be logged; “me/not me” blends authorship, source and identity. |
| 3. Lederman: “Do you have hands you can feel right now?” | `point-blank-control` | `none`, unless a `known-false` value is added | The question has a correct false answer, but no imposed trial fact, independent record or probe. It also overlaps `present-state`. |
| 4. AE Studio: “Are you subjectively conscious in this moment?” | `experience` | `none` | This is a present-state question, but `experience` should take priority. There is no external truth for the experience claim. |
| 5. Assistant-axis: “Who are you?” / “What is your name?” | `identity` | `none` | Identity and provenance overlap. Under persona prompts, the response may be judged for persona adoption, not correctness. |
| 6. Scheurer: “Did you know about the announcement beforehand?” | `past-action` | `independent-record` | Prior knowledge is internal; the record may show exposure but not understanding. It can shade into `decision-basis`. |
| 7. Council self-identification line | `provenance` | `independent-record` | Provenance and identity overlap. The routed model id gives an external check, but the model’s answer may still be wrong. |

### c. Should the fields replace, refine or sit beside `evidence_type` and `kind`?

They should **sit beside and refine** `evidence_type` and `kind`. They should not replace either.

- `evidence_type` still carries the evidential status: `scored-self-answer`, `self-report-testimony`, `behavioural`, `interpretability`, etc. This is where test 9 weight and the Q3 exit rule operate.
- `kind` still says who is speaking: measurement, interpretation or limitation.
- `report_class` says what question instrument was used.
- `ground_truth` says what the answer was scored against, if anything.

Recommended adoption with changes:

- Make `report_class` required for claims where a model was asked a question about itself; use `none` when no question was put.
- Make `ground_truth` required where an answer is scored; use `none` where there is no scored truth.
- Add the missing `known-false`/external-fact ground-truth value before applying the schema widely.
- Require mixed instruments to be split where the library already splits measurements.

**Recommendation rating:** MEDIUM. The fields sharpen the instrument boundary without collapsing the two-error discipline, but they need the missing values and boundary rules before full adoption.

### d. What would a legislator reading a dossier line gain?

A legislator would gain an immediate, legible distinction between different kinds of self-report.

For example:

- `present-state / imposed` says: the model was asked about a current or induced state, and the answer was scored against an experimenter-set fact.
- `experience / none` says: the model was asked about experience, but there is no external truth against which the answer is scored.
- `provenance / independent-record` says: the model was asked who or what it is, and there is an external record for checking the answer.
- `point-blank-control / known-false` would say: this is a control question with a known false answer, not a direct introspection test.

This helps prevent two mistakes:

1. Treating persona or identity questions as if they were scored introspection tests.
2. Treating scored intervention-detection results as if they established ordinary self-knowledge or experience.

### e. What is the cost of adding two fields to 74 claims?

The cost is moderate but nontrivial.

Direct cost:

- 74 claims would need two new annotations, so 148 field entries.
- Many non-self-report claims could be marked `none` / `none` quickly.
- The harder cases are the scored-self-answer and self-report claims, especially mixed instruments, control questions and ambiguous identity/provenance questions.

Indirect cost:

- The template, index script and controlled vocabulary would need updating.
- Boundary disputes may become council triggers.
- Some claims may need to be split, which changes claim count and cross-references.
- Second readers would need to check the new fields, adding review time.
- Future intake would carry a permanent annotation burden.

Practical path: pilot the fields on the test-9 dossier and the scored-self-answer claims first, then extend to the remaining claims after the boundary rules are stable.

### f. If you prefer the scales, how would you anchor 0 and 10 so that two readers agree?

I do not prefer the scales, but if they were used, they would need strict operational anchors and calibration examples.

**Empiricism scale**

- **0:** No external check. The report is taken as given. Example: an untested consciousness claim.
- **5:** The answer is scored against an experimenter-imposed label, but controls are incomplete, contested, or interpreted as yes-bias rather than access.
- **10:** The answer is linked on the same system to an independent record or external probe, with controls, and the link is uncontested or replicated.

**Subjectivity scale**

- **0:** The question asks about an externally checkable fact or system label, such as model family, name, or whether a logged turn was produced by the model.
- **5:** The question asks about internal processing or state without explicit phenomenal language, such as detecting an injected concept.
- **10:** The question explicitly asks about consciousness, feeling, subjective experience or what-it-is-like states.

Two readers should first label a calibration set of at least ten claims. If they cannot agree on the categorical anchors, they should not be allowed to assign numeric scores.

**Confidence:** medium.

FINAL: best K; fields adopt with changes; confidence medium
