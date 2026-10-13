# Raw OpenRouter response — NOT a filed review

**Model id (OpenRouter):** `deepseek/deepseek-v4-pro-0813`
**Queried:** 2026-10-13 via scripts/openrouter_review.js --target=self-answer-type --tag=self-answer-type (max_tokens 100000)
**Usage:** {"prompt_tokens":11928,"completion_tokens":11289,"total_tokens":23217,"cost":0.0439003224,"is_byok":false,"prompt_tokens_details":{"cached_tokens":0,"cache_write_tokens":0,"audio_tokens":0,"video_tokens":0},"cost_details":{"upstream_inference_cost":0.0439003224,"upstream_inference_prompt_cost":0.011415096,"upstream_inference_completions_cost":0.0324852264},"completion_tokens_details":{"reasoning_tokens":10181,"image_tokens":0,"audio_tokens":0}}

Read this, then decide whether/how to promote it into reviews/YYYY-MM-DD-<model-family>-<version>.md
per reviews/README.md's naming convention and verbatim-filing rule. This file is scratch, not a commit target.

---
**Unverified:** Claude, Anthropic lineage; version unknown to me.

**Q1.** Option C: type them `behavioural`, with a mandatory note. The field should record what is measured. Table 1’s core rows all measure a scored verbal answer against an experimenter-fixed or externally held label; that is the library’s behavioural class. The fact that an intervention altered internals should change the framework sentence to `[T9-steering]`, not the evidence type. This removes the Lindsey/Ferrara inconsistency without adding a design label that would obscure evidential weight. The note must say: *scored self-answer; the score shows response accuracy against the imposed label, not introspective access, unless report–state coupling is measured.* Test 9 still operates through the framework sentence where experience is inferred. Strongest case against C: it decides Q3 de facto, and a legislator may read correct detection as access if the note is missed. Confidence: medium.

**Q2.** Necessary but not sufficient.  
- **Trained-channel control:** For self-access, the base model should perform above sham/chance with low false positives, approaching the positive control’s ceiling. Against: base model at chance while fine-tuned is near-perfect. It can be produced without access: fine-tuning can exploit any prompt or distributional artefact; it validates the instrument, not ordinary operation.  
- **Privileged-access test:** For: first-model report outperforms a third-model observer given the same transcript after controlling yes-bias. Against: third model matches, or a prompt-specific yes-bias explains the result. It can be produced without access: models differ for non-introspective reasons.  
- **Measured coupling:** For: report accuracy covaries with probe decoding under perturbation; stronger if perturbing the decoded state changes the report. Against: probe decodes but report is uncorrelated, or report tracks only output-causing features. It can be produced without access: correlation/decoding can reflect a shared cause without introspective access.  
Missing: causal perturbation of the decoded state with prompt held constant, false-positive/yes-bias controls, same-family third-party controls, and separation of detection from compliance. Confidence: medium.

**Q3.** Likely misreadings:  
- **A:** “no usable measurement exists” or ignored.  
- **B:** “scored” read as “introspection confirmed,” though the score is external, not coupling.  
- **C:** “behavioural” read as ordinary benchmark, so detection rate becomes evidence of access.  
- **D:** “weight zero” read as discrediting the result, suppressing scored sensitivity and merging it with unscored testimony.  
- **E:** internal intervention typed `interpretability` read as “internals were measured,” when only the report was measured. Confidence: high.

**Q4.** Yes. A new value could become a parking lot. Exit rule: explicitly provisional while Q3 is open; automatic reclassification to `behavioural` or `self-report-testimony` when Q3 is decided or when a study satisfying the three-instrument test enters the library; every claim using it must record the unresolved Q3 in `not_evidence_of`; a council trigger fires after a fixed number of such claims or when one is cited for a North Star consequence. Confidence: medium.

**Q5.** Under C:  
- Ferrara c04: in; `behavioural`, with note “instrument validation, not introspection.”  
- UKAISI c02: in for the flagging/scored-answer half; split the reverting behaviour into a separate behavioural claim.  
- Singh c01: in as a probe-derived-label variant; `behavioural`; if the claim’s point is only the probe baseline, split.  
- AE c03: out; no external fact about the correct answer exists. It remains `ambiguous`/testimony.  
- Lederman c02: out as to third-model scored yes-rates; split any first-person detection comparison into `behavioural`. The third-person yes-bias should not carry self-answer status. Confidence: medium.

**Q6.** To decide Q3, the council needs one study on one system combining: intervention vs sham, self-report, internal probe decoding, third-model observer, trained positive control, and causal perturbation of the decoded state. No existing library source has all of these together. Ferrara c04 gives only the trained channel; Lederman c02 only third-person/prompt-bias; Macar c03/c04 only causal circuit/probe; Singh c01/c02 only probe-label classification. A concrete missing study: open-weights model, injection/sham, report, probe decode, third-family observer, trained control, and ablation of the decoded direction. Until then, keep Q3 open but do not file scored measurements as `ambiguous`; file them `behavioural` with the access caveat. Confidence: high.

**Severity:** A: LOW. B: MEDIUM. C: HIGH. **Argument against:** treating all scored self-answers as behavioural is itself a decision on Q3 and may over-normalise self-report unless the access caveat is printed with the entry. D: LOW. E: MEDIUM.

FINAL: option C, confidence medium
