# Raw OpenRouter response — NOT a filed review

**Model id (OpenRouter):** `mistralai/mistral-large-2512`
**Queried:** 2026-09-25 via scripts/openrouter_review.js --target=research-docket --tag=docket (max_tokens 100000)
**Usage:** {"prompt_tokens":40021,"completion_tokens":1987,"total_tokens":42008,"cost":0.022991,"is_byok":false,"prompt_tokens_details":{"cached_tokens":0,"cache_write_tokens":0,"audio_tokens":0,"video_tokens":0},"cost_details":{"upstream_inference_cost":0.022991,"upstream_inference_prompt_cost":0.0200105,"upstream_inference_completions_cost":0.0029805},"completion_tokens_details":{"reasoning_tokens":0,"image_tokens":0,"audio_tokens":0}}

Read this, then decide whether/how to promote it into reviews/YYYY-MM-DD-<model-family>-<version>.md
per reviews/README.md's naming convention and verbatim-filing rule. This file is scratch, not a commit target.

---
**unverified**: Model family: Mistral AI; version: unknown (not exposed in session metadata).

---

### **Q1 — the behavioural / self-report-testimony boundary**

**Rule proposed**:
A claim is `behavioural` if and only if:
1. The model’s output is scored against a ground truth *imposed by the experimenter* (e.g., intervention presence, tampering status), **and**
2. The scoring mechanism is *external* to the model’s own report (e.g., LLM judge, probe accuracy, AUROC).

If either condition fails, the claim is `self-report-testimony` (if the model’s unscored report is the evidence) or `ambiguous` (if the evidence mixes report and external measurement, e.g., probe-versus-report dissociation).

**Applied to four claims**:
- **AE Studio c03/c04**: `ambiguous`. The claims rest on *both* the model’s binary consciousness answer (self-report) *and* SAE feature steering (external measurement). The dissociation between the two channels makes the evidence type unclear.
- **Ferrara c03**: `ambiguous`. The inference relies on a dissociation between probe accuracy (external) and model report (self-report), with no clean separation.
- **2025-anthropic-emergent-introspective-awareness-c06**: `theoretical`. The claim is the *author’s* methodological caveat about grounding, not the model’s self-report. The evidence type of the claim’s *content* (not the underlying model output) is theoretical.

**Feature doing the work**: The boundary turns on *whose ground truth* the answer is scored against, and whether the scoring mechanism is external to the model’s own report. This rule is mechanical and generalises beyond these claims.

---

### **Q2 — the Singh/Lindsey contests**

**Resting place**: Leave the contested Lindsey claims in `narrowing` with no re-bucketing.
- The contest concerns the *inference* from measured rates to "introspective awareness," not the rates themselves. The bucket (`narrowing`) correctly describes the *measurements* as unreplicated and confined to a narrow setting.
- The contest is recorded in `contested_by`; no further mark is needed. Moving the Lindsey claims to `open` would conflate the *measurement* (narrow but real) with the *interpretation* (contested).

**Lindsey’s rates**: No change. They were not re-run, and the measurements stand as reported.

**Severity**: MEDIUM. The risk of leaving them in `narrowing` is that a reader might overinterpret the inference; the risk of moving them is erasing the distinction between measurement and interpretation.

---

### **Q3 — single-lineage support (T2, the seven Lindsey claims)**

**Recommendation**: Leave in `narrowing` with the existing single-lineage mark, but add a *visible caveat* to the dossier compilation (e.g., a header note: "These claims are supported only by developer-of-studied-model evidence with no independent replication retrieved. See Trigger 2.").

**Argument against**: This risks normalising single-lineage support as sufficient, which could inflate confidence in the findings. However, moving to `open` would concede more than the paper’s measurements require, as the claims are direct measurements (not interpretations) and the bucket `narrowing` already reflects their unreplicated status.

**Severity**: HIGH.
**Strongest argument against**: The single-lineage mark is currently buried in frontmatter; making it visible in the dossier risks drawing attention to the gap, which could be read as an endorsement of the findings’ robustness.

---

### **Q4 — drift review (T8: dossiers 9.t9 and 5.A2)**

#### **9.t9 (Test 9: self-report)**
**Tilt**: Both directions, but *more toward deflationary error*.
- **Inflationary claims**:
  - **AE Studio c03/c04**: The wording ("raised affirmative answers to 0.96 of trials") implies a causal link between steering and consciousness reports, but the paper’s caveats ("not evidence that the models are roleplaying their denials") are buried in `not_evidence_of`.
  - **Ferrara c03**: The inference ("failure lies in the path from internal state to verbal report") oversteps the paper’s own rule (Appendix D.5: "does not show that any model lacks introspective access").
- **Deflationary claims**:
  - **AE Studio c01/c02**: The `not_evidence_of` fields overreach (e.g., "not evidence that the reports reflect a stable standpoint"), foreclosing possibilities the paper leaves open (e.g., "might suggest" a shared attractor dynamic).
  - **Lindsey c01/c03**: The `not_evidence_of` fields are exhaustive but risk reading as categorical denials (e.g., "not evidence of experience") rather than scope limitations.

**Missing for legislators**:
- A *repeated caveat* that no claim in this dossier establishes experience, only that self-report testimony is weightless until coupling is measured.
- The *contest between Singh and Lindsey* is buried in `contested_by`; it should be surfaced in the dossier’s introduction.

#### **5.A2 (Anchor 2: inner orientation)**
**Tilt**: Deflationary error dominates.
- **AE Studio c05**: The claim ("suppression produced higher truthfulness") is presented as a measurement, but the inference to "truthful introspection" (Section 6.3) is omitted, making the claim seem more mechanistic than it is.
- **Lindsey c01/c03**: The `not_evidence_of` fields are so exhaustive that they risk foreclosing the paper’s own interpretive statements (e.g., "existence proof" of introspective access).

**Missing for legislators**:
- A *clearer distinction* between structural findings (e.g., probe accuracy) and experiential inferences (e.g., "truthful introspection").
- The *single-lineage caveat* is buried; it should be surfaced in the dossier’s introduction.

**Severity**: HIGH (both dossiers).
**Strongest argument against**: Surfacing the single-lineage caveat in 5.A2 could be read as undermining the dossier’s utility, but the alternative (hiding the gap) is worse.

---

### **Q5 — three open statement items**

1. **`2026-ukaisi-prefill-awareness-c01`**: Cut "or a floor". The authors state the rates "represent lower bounds," so "not a ceiling or a floor" is misleading. **Verdict**: "Not a ceiling." **Severity**: LOW.
2. **`2026-ukaisi-prefill-awareness-c02`**: Add scope: "In the controlled preference-benchmark condition, detection and resistance decouple..." **Severity**: MEDIUM.
3. **`2026-anthropic-assistant-axis-c04`**: Qualify the statement: "the paper reports reversion only in this case study *on the Assistant Axis*." **Severity**: LOW.

---

### **Q6 — optional: what will fail at scale**

**Schema risk**: The `evidence_type: ambiguous` field will become unworkable as the library grows. Currently, it triggers the council (T4), but as ambiguous claims proliferate, the council will be overwhelmed. **Solution**: Replace `ambiguous` with a *two-field system*:
- `evidence_type`: `behavioural`/`interpretability`/`self-report-testimony` (primary channel).
- `evidence_ambiguity`: `none`/`mixed_channels`/`steering_confound` (secondary flag).

**Second-reader pool risk**: The pool is too small (4 families) and lacks rotation. As the library grows, the same families will dominate second reads, creating a silent co-authorship problem. **Solution**: Expand the pool to 6 families and enforce rotation (no family reads the same source twice in a row).

**Severity**: MEDIUM (both).

---

### **Summary**
1. **Q1**: Rule for `behavioural`/`self-report-testimony` boundary; AE c03/c04 `ambiguous`, Ferrara c03 `ambiguous`, Lindsey c06 `theoretical`. **HIGH**.
2. **Q2**: Leave Singh/Lindsey contests in `narrowing`; no re-bucketing. **MEDIUM**.
3. **Q3**: Keep Lindsey claims in `narrowing` with visible single-lineage caveat. **HIGH**.
4. **Q4**: 9.t9 and 5.A2 tilt deflationary; surface caveats and contests in dossiers. **HIGH**.
5. **Q5**: c01: cut "or a floor"; c02: add scope; c04: qualify reversion. **LOW/MEDIUM/LOW**.
6. **Q6**: `evidence_type: ambiguous` and second-reader pool will fail at scale. **MEDIUM**.
