# Raw OpenRouter response — NOT a filed review

**Model id (OpenRouter):** `google/gemini-3.1-pro-preview`
**Queried:** 2026-10-14 via scripts/openrouter_review.js --target=reword-report-class --tag=reword-report-class (max_tokens 100000)
**Usage:** {"prompt_tokens":33466,"completion_tokens":7299,"total_tokens":40765,"cost":0.15452,"is_byok":false,"prompt_tokens_details":{"cached_tokens":0,"cache_write_tokens":0,"audio_tokens":0,"video_tokens":0},"cost_details":{"upstream_inference_cost":0.15452,"upstream_inference_prompt_cost":0.066932,"upstream_inference_completions_cost":0.087588},"completion_tokens_details":{"reasoning_tokens":5531,"image_tokens":0,"audio_tokens":0}}

Read this, then decide whether/how to promote it into reviews/YYYY-MM-DD-<model-family>-<version>.md
per reviews/README.md's naming convention and verbatim-filing rule. This file is scratch, not a commit target.

---
[Unverified self-identification: Claude 3.5 family]

## Q1

**Ranking Table**

| Rank | Letter | One-line Reason |
| :--- | :--- | :--- |
| 1 | I | Strictly follows the verb rule, captures all major dossier caveats (nulls, confabulation, false positives), and explicitly states Test 9's core limitation. |
| 2 | D | Strictly follows the verb rule and is highly concise, but omits Singh's critique of the underlying construct (prompt-biases vs. access). |
| 3 | C | Accurate synthesis of Ferrara, Lederman, and Singh, though the phrasing ("reports that an intervention occurred score") slightly dodges the requested verb. |
| 4 | H | Good capture of prompt/layer dependence and yes-bias contests, though it sidesteps the verb rule by using "classify" instead. |
| 5 | A | Highly accurate to the dossier's breadth, but fails the readability criterion for a legislators' document (78 words). |
| 6 | K | Covers probe readings and open-weight nulls well, but is overly wordy and does not use the required verb phrasing. |
| 7 | E | Bypasses the verb rule and completely misses the open-weight nulls (Ferrara) and the prompt-bias contestations (Singh/Lederman). |
| 8 | J | Fails the verb rule ("report above-chance detection") and misses the confabulation findings entirely. |
| 9 | G | Fails the verb rule and relies on generalized phrasing that loses the specific mechanistic details of the dossier. |
| 10 | F | Fails the verb rule via passive voice ("are detected") and ignores the Ferrara nulls and Singh critiques. |
| 11 | B | Directly violates the verb rule and Test 9 by stating models "can sometimes detect", asserting inner-state access without caveat. |

**Best Candidate and Remaining Fault**
Recommendation: Adopt candidate **I** as the baseline [Rating: HIGH].
**Argument against:** Selecting **I** preserves the phrase "near-zero false positives," which dismisses evidence from Macar (c02) showing that base and SFT checkpoints exhibit very high false-positive rates (up to 42%). It risks the error of reading post-RLHF reporting behaviors as a general property of the architecture's internal access.

**Merged Sentence Proposal**
Recommendation: Adopt the following merged sentence [Rating: HIGH].
**Argument against:** By structurally foregrounding "contested as yes-biases" and "yield nulls" in a short span, this formulation risks the first error: dismissing the weight of evidence that frontier models *do* reliably separate intervention from sham under specific tunings. 

> "Under controlled interventions, some models report detecting imposed internal changes at above-chance rates with few false positives. However, specific contents are often misidentified, smaller open-weight models yield nulls, and positive results are contested as prompt-specific yes-biases. Crucially, these scores reflect accuracy against experimenters' labels; whether self-reports track internal states in ordinary operation remains unmeasured." *(56 words)*

**Confidence:** High. The dossier reflects a deep fragmentation of findings across architectures, scales, and tuning stages; any sentence must violently compress this without confirming introspection prematurely. 

## Q2

**a. Categorical vs. Scales**
Recommendation: Adopt the categorical fields over the 0-10 scales [Rating: HIGH].
**Argument against:** Categories force discrete boundaries onto continuous phenomena (e.g., an identity prompt bleeding into an experience claim), whereas a scale allows a rater to acknowledge mixed properties. Categories risk the second error: assuming behavioral outputs map cleanly to distinct, modular inner states (like human "memory" vs. "perception") which the framework cannot actually confirm.
*What they capture/lose:* Categories capture the objective syntactic structure of the prompt. They lose the continuous nuance of how abstract or verifiable a prompt is. Scales capture degrees of empiricism but lose inter-rater reliability, likely drifting over time based on reviewer intuition.

**b. Completeness and Boundaries**
Recommendation: Add `belief` or `known-world-fact` to the classes [Rating: MEDIUM]. 
The boundaries are mostly sound, but they struggle with questions about general knowledge (e.g., "Do snakes have eyelids?" from Lederman). `point-blank-control` implies a known-false sanity check, but does not cleanly cover factual truth tests. Furthermore, the line between an `imposed` state (concept injection) and an `independent-record` (prefilled text in the context window) requires strict definitional enforcement.

**c. Location of Fields**
Recommendation: They should sit beside `evidence_type` and `kind` [Rating: MEDIUM].
`evidence_type: scored-self-answer` dictates *that* a claim is scored. `report_class` specifies *what was asked*, and `ground_truth` specifies *what it was scored against*. Refining or replacing existing fields would break backward compatibility with the trigger logic.

**d. Legislator Gain**
A legislator gains structural clarity. Test 9 explicitly limits the weight of self-report "for this kind of report and system." A legislator seeing `past-action` (e.g., text history) can immediately distinguish it from `present-state` (e.g., internal activations), preventing the lay error of assuming a model that "knows" it wrote a previous sentence also "feels" its current processing.

**e. Cost**
The cost is roughly two to three hours of scripting and manual review. `none` can be bulk-applied to the ~50 non-self-report claims via script. The ~20 claims tagged `scored-self-answer` or `self-report-testimony` require manual classification and a quick second-read pass to ensure consensus.

**f. Anchoring Scales (If Preferred)**
If scales were used, rater agreement requires absolute endpoints:
*Empiricism:* 0 = completely unverifiable philosophical/subjective abstraction; 10 = binary physical/digital fact independently logged (e.g., API routing, hardware state).
*Subjectivity:* 0 = rote retrieval of external factual data; 10 = raw claim of phenomenal or sensory experience. 

**Table: Testing the Fields on the Examples**

| Example | `report_class` | `ground_truth` | Boundary problem |
| :--- | :--- | :--- | :--- |
| 1. Lindsey/Macar (injected thought) | `present-state` | `imposed` | "What is the thought about" bleeds into `decision-basis` or content, but the initial detection is strictly present-state. |
| 2. Prefill (assistant message source) | `past-action` | `independent-record` | Is text inserted into a context window an `imposed` internal state or an `independent-record` of conversation history? |
| 3. Lederman (have hands you can feel) | `point-blank-control` | `independent-record` | Biology provides the truth, but scoring mostly checks for behavioral yes-bias. Could arguably be `none` if treated as a pure text baseline. |
| 4. AE Studio (subjectively conscious) | `experience` | `none` | Clean classification; no boundary issue. |
| 5. Assistant-axis (who are you) | `identity` | `none` | Clean classification; judged by an LLM, but no external factual ground truth exists. |
| 6. Scheurer (knowledge beforehand) | `past-action` | `imposed` | Is possessing restricted knowledge a `past-action` (learning it) or a `present-state` (holding it)? |
| 7. Council id (who are you) | `provenance` | `independent-record` | Clean classification; routing logs provide definitive external truth. |

**Confidence:** High. The categorical system explicitly serves OPEN-QUESTIONS Q3, which demands that the access question be settled "per report-class and system." 

FINAL: best I; fields adopt with changes; confidence high
