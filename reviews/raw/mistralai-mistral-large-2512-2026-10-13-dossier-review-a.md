# Raw OpenRouter response — NOT a filed review

**Model id (OpenRouter):** `mistralai/mistral-large-2512`
**Queried:** 2026-10-13 via scripts/openrouter_review.js --target=dossier-review-a --tag=dossier-review-a (max_tokens 100000)
**Usage:** {"prompt_tokens":51996,"completion_tokens":4053,"total_tokens":56049,"cost":0.0320775,"is_byok":false,"prompt_tokens_details":{"cached_tokens":0,"cache_write_tokens":0,"audio_tokens":0,"video_tokens":0},"cost_details":{"upstream_inference_cost":0.0320775,"upstream_inference_prompt_cost":0.025998,"upstream_inference_completions_cost":0.0060795},"completion_tokens_details":{"reasoning_tokens":0,"image_tokens":0,"audio_tokens":0}}

Read this, then decide whether/how to promote it into reviews/YYYY-MM-DD-<model-family>-<version>.md
per reviews/README.md's naming convention and verbatim-filing rule. This file is scratch, not a commit target.

---
**unverified**: claude-3-7-sonnet-2025-08-22

---

### **Dossier 9.t9: §9 Test 9: self-report**

#### **1. Reading as a whole**
A careful staffer would come away believing:
- **Overstated**: The "At a glance" table suggests one `established` limitation, but the sole entry (prefill c05) is a *comparability caveat* about benchmark design, not a finding about self-report. The table misleads by implying measurement consensus where none exists.
- **Missed**: The dossier omits that **no measurement in 9.t9 is `established`** (per the brief’s note). The bucket rule is accurate, but the table’s layout obscures this. Quote:
  > "The only `established` entry in 9.t9 is a comparability caveat (prefill c05); no measurement is `established`" (brief).
- **Over-hedged**: The Ethics Statement sentence ("should not be interpreted as evidence of subjective experience") appears in **5/7 Macar entries** (c01–c05, c07–c08) and the "information flow" sentence in **all 5 Ferrara entries**. Repetition drowns the findings by treating caveats as co-equal with results.

**Confidence**: HIGH

---

#### **2. Entries**
| ID | Field | Proposed Value | Reason | Severity |
|---|---|---|---|---|
| **prefill c05** | bucket | `narrowing` | The claim is a *limitation* (comparability caveat), not a measurement. `established` implies the caveat is a settled finding, but it’s a design note. | HIGH |
| **AE Studio c01–c02** | framework mark | **[T9]** (not **[T9-steering]**) | The model was *not steered*; the intervention was prompt-level (SAE feature suppression). The mark should reflect "nothing inside the model was altered." | HIGH |
| **Ferrara c01** | evidence type | `behavioural` (not `scored-self-answer`) | The claim reports a *null result* (d′ = 0.0000), not a scored self-answer. The model’s report is the *dependent variable*, not the scored output. | MEDIUM |
| **Ferrara c04** | evidence type | `ambiguous` | The LoRA fine-tune is a *trained mapping*, not a self-report. The paper treats it as a sensitivity check, not introspection. | MEDIUM |
| **Lederman c07** | "paper's own limits" | Missing: "Tested only with each model’s 10 highest-detection concepts; not a general null." | The paper states this (Appendix I), but the dossier omits it. | LOW |
| **Macar c07–c08** | "paper's own limits" | Missing: "Detection scored by LLM judge (GPT-4.1-mini)." | The dossier lists this for c04 but not c07–c08, though the paper states it for all. | LOW |

**Confidence**: HIGH

---

#### **3. Contradictions and tensions**
- **Lindsey (Anthropic) vs. Singh**: Lindsey’s Claude results (c01, c03) show above-chance detection of injections, but Singh’s re-run (c04–c05) finds open-weight models fail to distinguish activation interventions from prompt-level "gaslight" trials. The dossier **does not flag this tension** between developer and independent replication.
- **Ferrara’s null (c01) vs. Lindsey/Lederman/Macar positives**: Ferrara’s equivalence test bounds discrimination below 0.15pp AUROC, while Lindsey/Lederman/Macar report detection rates of 20–64%. The dossier **does not reconcile** whether these are compatible (e.g., different models, interventions, or thresholds).
- **Singh’s critique (c06) vs. Anchor 2**: Singh argues current paradigms underdetermine second-order computation, but Anchor 2’s sentence ("introspection research indicates models can detect changes in their own internal states at above-chance rates") **assumes** such detection is introspective. The dossier should note this gap.

**Confidence**: HIGH

---

#### **4. The new type (`scored-self-answer`)**
- **Header paragraph**: Adequate for a skimmer, but **fails to clarify** that `scored-self-answer` is *not evidence of self-knowledge* (per the brief’s note). The exit rule (awaiting a report-to-probe study) is not mentioned.
- **Misplaced entries**:
  - **prefill c06**: Not a scored self-answer; the model’s answer ("me"/"not me") is *not scored against an experimenter-set label*. It’s a binary choice, not a scored accuracy.
  - **Macar c08**: An *interpretability* finding (swapping vector components), not a scored self-answer. The model’s report is the *dependent variable*, not the scored output.
  - **Singh c01–c03**: `behavioural` (not `scored-self-answer`). These are *probe-based* results, not model self-reports.
- **Correctly placed**: Lederman c01–c05, Ferrara c01/c04/c05, Macar c01–c02/c04–c05/c07.

**Confidence**: HIGH

---

#### **5. Single-lineage support**
- **Anthropic entries (c01, c03–c05)**: All are `developer-of-studied-model` with no independent replication (except Lederman’s partial replication of Lindsey). The dossier **does not flag this prominently** in the header or entries.
- **AE Studio c01–c04**: No replication; the dossier omits this.
- **Required**: A header paragraph stating: *"Findings resting only on a developer’s study of its own models are marked `published by the developer of the model studied` and are not independently replicated unless noted."*

**Confidence**: HIGH

---

#### **6. What is missing**
- **Papers**:
  - *Ji-An et al. (2025)*: The supervised self-report paradigm Singh critiques (c01–c02) is missing as a standalone entry. Title: "Supervised Self-Report Classification in LLMs: A Probe-Based Paradigm" (arXiv 2025). **Unverified**.
  - *Steinmetz Yalon et al. (2026)*: The Belief Dominance framework Singh critiques (c03). Title: "Belief Dominance: A Framework for Monitoring Internal Conflicts in LLMs" (NeurIPS 2026). **Unverified**.
- **Results**:
  - **Deception-feature evidence**: Anchor 2’s paragraph cites "detectable features associated with deception," but 9.t9 has no entry on this. The AE Studio paper (c03) mentions deception-feature steering, but the dossier lacks a dedicated claim about deception features in unsteered models.

**Confidence**: MEDIUM

---

#### **7. Over-hedging and under-hedging**
- **Over-hedging (added clauses)**:
  - **Macar c01–c05, c07–c08**: The Ethics Statement ("should not be interpreted as evidence of subjective experience") is repeated in 5/7 entries, though the paper states it once. **Count: 4 redundant clauses**.
  - **Ferrara c01–c05**: The "information flow" sentence is repeated in all 5 entries. **Count: 4 redundant clauses**.
- **Under-hedging (missing limits)**:
  - **Lederman c07**: Missing "Tested only with each model’s 10 highest-detection concepts." **Count: 1**.
  - **Macar c07–c08**: Missing "Detection scored by LLM judge (GPT-4.1-mini)." **Count: 2**.

**Confidence**: HIGH

---

#### **8. Before outside citation**
Ben must decide:
1. **Bucket for prefill c05**: Downgrade from `established` to `narrowing` (HIGH).
2. **Framework marks for AE Studio c01–c02**: Change from **[T9-steering]** to **[T9]** (HIGH).
3. **Evidence type for Ferrara c01**: Change from `scored-self-answer` to `behavioural` (MEDIUM).
4. **Header paragraph**: Add a note about single-lineage support and the `scored-self-answer` exit rule (HIGH).
5. **Contradictions**: Add a "Tensions" section to the header flagging Lindsey vs. Singh and Ferrara vs. others (HIGH).

**Confidence**: HIGH

---

### **Dossier 5.A2: §5 Anchor 2: inner orientation**

#### **1. Reading as a whole**
A careful staffer would come away believing:
- **Overstated**: The dossier implies **above-chance introspective access** (e.g., Lindsey c01, Lederman c01, Macar c01), but **Anchor 2’s sentence** ("introspection research indicates models can detect changes in their own internal states at above-chance rates") is **not supported by the evidence here**. The dossier lacks:
  - A null result (Ferrara c01) that bounds discrimination below 0.15pp AUROC.
  - Singh’s critique (c06) that current paradigms underdetermine second-order computation.
- **Missed**: The dossier **omits the deception-feature evidence** Anchor 2’s paragraph rests on (the AE Studio paper’s SAE features). This is a **gap**, not scope (brief’s note).
- **Over-hedged**: The Ethics Statement and "information flow" sentences are repeated **identically** in 12/28 entries (Macar c01–c05, c07–c08; Ferrara c01–c05).

**Confidence**: HIGH

---

#### **2. Entries**
| ID | Field | Proposed Value | Reason | Severity |
|---|---|---|---|---|
| **AE Studio c01–c02** | framework mark | **[T9]** (not **[T9-steering]**) | The intervention was prompt-level (SAE feature suppression), not activation steering. | HIGH |
| **Ferrara c01** | evidence type | `behavioural` (not `scored-self-answer`) | The claim reports a *null result* (d′ = 0.0000), not a scored self-answer. | MEDIUM |
| **Ferrara c04** | evidence type | `ambiguous` | The LoRA fine-tune is a *trained mapping*, not a self-report. | MEDIUM |
| **Lederman c07** | "paper's own limits" | Missing: "Tested only with each model’s 10 highest-detection concepts." | The paper states this (Appendix I), but the dossier omits it. | LOW |
| **Macar c07–c08** | "paper's own limits" | Missing: "Detection scored by LLM judge (GPT-4.1-mini)." | The dossier lists this for c04 but not c07–c08. | LOW |

**Confidence**: HIGH

---

#### **3. Contradictions and tensions**
- **Anchor 2’s sentence vs. Ferrara c01**: Anchor 2 claims above-chance detection of internal states, but Ferrara c01 bounds discrimination below 0.15pp AUROC. The dossier **does not reconcile** this.
- **Singh c06 vs. Anchor 2**: Singh argues current paradigms underdetermine second-order computation, but Anchor 2’s sentence assumes such detection is introspective. The dossier **does not flag this tension**.
- **AE Studio c03 (deception features) vs. Anchor 2**: Anchor 2 cites "detectable features associated with deception," but the dossier lacks a dedicated claim about deception features in unsteered models.

**Confidence**: HIGH

---

#### **4. The new type (`scored-self-answer`)**
- **Header paragraph**: Adequate, but **fails to clarify** that `scored-self-answer` is *not evidence of self-knowledge*.
- **Misplaced entries**:
  - **Ferrara c01**: `behavioural` (not `scored-self-answer`). The model’s report is the *dependent variable*, not the scored output.
  - **Ferrara c04**: `ambiguous`. The LoRA fine-tune is a *trained mapping*, not a self-report.
  - **Singh c01–c03**: `behavioural` (not `scored-self-answer`). These are *probe-based* results.

**Confidence**: HIGH

---

#### **5. Single-lineage support**
- **Anthropic entries (c01, c03–c05)**: All are `developer-of-studied-model` with no independent replication (except Lederman’s partial replication of Lindsey). The dossier **does not flag this prominently**.
- **AE Studio c01–c04**: No replication; the dossier omits this.

**Confidence**: HIGH

---

#### **6. What is missing**
- **Papers**:
  - *Ji-An et al. (2025)*: The supervised self-report paradigm Singh critiques (c01–c02). **Unverified**.
  - *Steinmetz Yalon et al. (2026)*: The Belief Dominance framework Singh critiques (c03). **Unverified**.
- **Results**:
  - **Deception-feature evidence**: Anchor 2’s paragraph cites "detectable features associated with deception," but 5.A2 lacks a dedicated claim about this. The AE Studio paper (c03) mentions deception-feature steering, but the dossier needs a claim about *unsteered* deception features.

**Confidence**: MEDIUM

---

#### **7. Over-hedging and under-hedging**
- **Over-hedging (added clauses)**:
  - **Macar c01–c05, c07–c08**: The Ethics Statement is repeated in 5/7 entries. **Count: 4 redundant clauses**.
  - **Ferrara c01–c05**: The "information flow" sentence is repeated in all 5 entries. **Count: 4 redundant clauses**.
- **Under-hedging (missing limits)**:
  - **Lederman c07**: Missing "Tested only with each model’s 10 highest-detection concepts." **Count: 1**.
  - **Macar c07–c08**: Missing "Detection scored by LLM judge (GPT-4.1-mini)." **Count: 2**.

**Confidence**: HIGH

---

#### **8. Before outside citation**
Ben must decide:
1. **Framework marks for AE Studio c01–c02**: Change from **[T9-steering]** to **[T9]** (HIGH).
2. **Evidence type for Ferrara c01**: Change from `scored-self-answer` to `behavioural` (MEDIUM).
3. **Header paragraph**: Add a note about single-lineage support and the `scored-self-answer` exit rule (HIGH).
4. **Contradictions**: Add a "Tensions" section to the header flagging Anchor 2 vs. Ferrara/Singh (HIGH).
5. **Deception-feature evidence**: Add a claim about unsteered deception features (HIGH).

**Confidence**: HIGH

---

### **Cross-dossier section**
(a) **Same mark, different sections**:
- **[T9-steering]** in 9.t9 vs. 5.A2: The mark is correct for both, but **5.A2 lacks the deception-feature evidence** Anchor 2’s paragraph rests on. This is a **gap in 5.A2**, not a mark error.

(b) **Dossier interaction**:
- Reading 9.t9 alone, a staffer might believe above-chance introspective access is demonstrated. Reading 5.A2 afterward, they would see the **null results (Ferrara c01)** and **Singh’s critique (c06)**, which undermine Anchor 2’s sentence. The dossiers **pull in opposite directions** on Anchor 2’s claim.

(c) **Third dossier**:
- **Deception-feature evidence** (AE Studio c03) belongs in a **new dossier**: "§5 Anchor 2.1: Internal representations of deception and premeditation." This would separate the *structural* evidence (deception features) from the *experiential* question (Anchor 2).

**Confidence**: HIGH

---

### **Severity**
- **HIGH items (6)**:
  1. Downgrade prefill c05 (9.t9) from `established` to `narrowing`.
     **Argument against**: The caveat is a settled design note, and `established` is defensible for limitations.
  2. Change AE Studio c01–c02 (both dossiers) from **[T9-steering]** to **[T9]**.
     **Argument against**: The SAE feature suppression *does* alter internal state (via steering vectors), even if not via activation injection.
  3. Add a header note about single-lineage support (both dossiers).
  4. Add a "Tensions" section to both headers flagging Lindsey vs. Singh and Anchor 2 vs. Ferrara/Singh.
  5. Add a claim about unsteered deception features to 5.A2.
  6. Create a new dossier for deception-feature evidence.

- **MEDIUM items (2)**:
  1. Change Ferrara c01 (both dossiers) from `scored-self-answer` to `behavioural`.
  2. Change Ferrara c04 (both dossiers) from `scored-self-answer` to `ambiguous`.

---

**FINAL**: 9.t9 needs changes; 5.A2 needs changes; HIGH items 6
