# Raw OpenRouter response — NOT a filed review

**Model id (OpenRouter):** `qwen/qwen3.8-max`
**Queried:** 2026-10-13 via scripts/openrouter_review.js --target=self-answer-type --tag=self-answer-type (max_tokens 100000)
**Usage:** {"prompt_tokens":12266,"completion_tokens":18441,"total_tokens":30707,"cost":0.135178,"is_byok":false,"prompt_tokens_details":{"cached_tokens":0,"cache_write_tokens":0,"audio_tokens":0,"video_tokens":0},"cost_details":{"upstream_inference_cost":0.135178,"upstream_inference_prompt_cost":0.024532,"upstream_inference_completions_cost":0.110646},"completion_tokens_details":{"reasoning_tokens":16925,"image_tokens":0,"audio_tokens":0}}

Read this, then decide whether/how to promote it into reviews/YYYY-MM-DD-<model-family>-<version>.md
per reviews/README.md's naming convention and verbatim-filing rule. This file is scratch, not a commit target.

---
**Unverified:** Qwen3.8, Qwen family.

**Q1**  
Recommendation: Option B, `scored-self-answer`, as a provisional design tag. Severity: MEDIUM.

The claims table shows a stable design class: an imposed or independently held truth, a self-referential question, and scoring of the answer. Current typing is inconsistent: inject-then-ask claims are `interpretability` in Lindsey, Lederman and Macar, but `behavioural` in Ferrara and Singh; AE c03/c04 are `ambiguous`. Keeping `ambiguous` preserves Q3 but either leaves that inconsistency or requires mass retagging. Typing all as `behavioural` or all as `self-report-testimony` decides Q3 prematurely: the first risks treating detection scores as evidence of access; the second risks zero-weighting scored controls such as Ferrara c04. Splitting by intervention type follows current mechanics but does not address the unresolved self-answer problem.

B names the class, makes it filterable, leaves the test 9 sentence intact, and does not decide whether the answer shows self-access.

Strongest case against: B adds a method-flavoured label to an evidence-type field, may be opaque to a legislator, and can become a permanent parking place for claims that should be decided.

Confidence: medium.

**Q2**  
Recommendation: treat the three instruments as necessary but not sufficient. Severity: MEDIUM.

1. **Trained-channel control.**  
   For self-access: high sensitivity and low false positives show the information can be reported; stronger if unmodified models also report above chance with calibration.  
   Against: chance performance, uncalibrated confidence, or report only after artificial fine-tuning.  
   Could be produced without access: yes. Fine-tuning may create a decoder, shortcut, or demand artifact. Ferrara c04 validates an instrument; it does not show ordinary self-access.

2. **Privileged-access test.**  
   For: the answering model beats a transcript-only matched model, with low false positives and counterbalanced labels.  
   Against: transcript-only model matches or exceeds it, or self-report shows yes-bias/gaslight failures, as in Lederman c02 and Singh c04/c05.  
   Could be produced without access: yes. First-person prompt bias, roleplay, metadata, or a handicapped transcript control could produce the result.

3. **Measured coupling.**  
   For: trial-level coupling between report and an independent internal probe or causal perturbation, with sham/gaslight controls and specificity.  
   Against: no coupling, or coupling explained by a common cause, output semantics, or task demand.  
   Could be produced without access: yes. The intervention may drive both probe and report, or the model may be trained to mimic the probe.

Missing or under-specified: response-bias calibration, false-positive rates, ordinary-operation baselines, temporal and content specificity, and causal dissociation between self-monitoring and general task performance.

Confidence: medium.

**Q3**  
Recommendation: if B is adopted, the dossier legend must state that the value is a design tag, not a finding of self-access. Severity: LOW.

Likely misreadings:

- **A `ambiguous`:** a legislator may treat a sound scored measurement as defective or discount it; `ambiguous` also conflates Q3 uncertainty with ordinary method caveats.
- **B `scored-self-answer`:** a legislator may infer a settled special category of self-knowledge, or may treat the label as evasive jargon and assign it no weight.
- **C `behavioural`:** a legislator may treat detection scores as ordinary benchmark evidence of inner access.
- **D `self-report-testimony`:** a legislator may apply weight zero to scored, replicable measurements and conflate them with unscored experience reports.
- **E split by design:** a legislator may infer that `interpretability` rows prove internal access while `behavioural` rows do not, even when the experimental design is similar.

Confidence: high.

**Q4**  
Recommendation: B needs an explicit exit rule; otherwise it will park claims. Severity: HIGH.

**Argument against:** automatic docketing and sunset may force premature reclassification or decision under incomplete evidence, recreating the two-error problem.

Exit rule:

- The index script should treat `scored-self-answer` as trigger 4 until the claim has a dated adjudication or Q3 is closed.
- Each claim must carry the applicable test 9 sentence and a `not_evidence_of` clause disclaiming self-access absent controls.
- Claims must be reviewed at the next council round or after 90 days; they exit by split, reclassification to an existing type, or a dated adjudication.
- If Q3 is decided, all `scored-self-answer` claims must be migrated within one index run.

Confidence: medium.

**Q5**  
Recommendation: apply a narrowed B definition: the scored unit must be the answering model’s self-referential answer, and the truth must be a trial-level fact fixed independently of that answer. Severity: LOW.

- **Ferrara c04:** IN for the scored report, with a mandatory trained-channel/instrument-validation note; it is not evidence of ordinary self-access.
- **UKAISI c02:** split. Flagging is IN; reverting to baseline is OUT and remains `behavioural`.
- **Singh c01:** OUT. The truth is a probe-derived label, not an imposed fact; the claim is a probe/decodability comparison, not a scored self-answer as defined.
- **AE c03:** OUT. There is an imposed intervention but no external correct answer to the consciousness query; `ambiguous` remains appropriate, but B is not.
- **Lederman c02:** OUT for the other-model transcript control. If self-target trials are included, split them: self-target IN, other-target OUT.

Confidence: medium.

**Q6**  
Recommendation: do not advise Ben to decide Q3 until a study or analysis combines the needed controls. Severity: MEDIUM.

Needed: a per-trial dataset in one model with:

1. imposed truth and scored self-report;  
2. a transcript-only control;  
3. an independent internal probe or causal perturbation of the report pathway;  
4. sham/gaslight/third-person controls.

Concrete form: extend Lindsey/Lederman injection tasks with probe probabilities, confidence, a transcript-only classifier, and Macar-style ablation or Ferrara-style trained-channel controls on the same trials.

Existing in library: no single source has this. Partial components exist: Ferrara c04 trained channel; Lederman c02 third-person control; Macar c03/c04 circuit perturbation; Singh c01/c02 probe-label comparison and c04/c05 gaslight controls; UKAISI text-edit ground truth. None settles Q3.

Confidence: medium.

FINAL: option B, confidence medium
