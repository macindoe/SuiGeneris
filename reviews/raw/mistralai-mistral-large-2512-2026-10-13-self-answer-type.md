# Raw OpenRouter response — NOT a filed review

**Model id (OpenRouter):** `mistralai/mistral-large-2512`
**Queried:** 2026-10-13 via scripts/openrouter_review.js --target=self-answer-type --tag=self-answer-type (max_tokens 100000)
**Usage:** {"prompt_tokens":12320,"completion_tokens":1044,"total_tokens":13364,"cost":0.007726,"is_byok":false,"prompt_tokens_details":{"cached_tokens":0,"cache_write_tokens":0,"audio_tokens":0,"video_tokens":0},"cost_details":{"upstream_inference_cost":0.007726,"upstream_inference_prompt_cost":0.00616,"upstream_inference_completions_cost":0.001566},"completion_tokens_details":{"reasoning_tokens":0,"image_tokens":0,"audio_tokens":0}}

Read this, then decide whether/how to promote it into reviews/YYYY-MM-DD-<model-family>-<version>.md
per reviews/README.md's naming convention and verbatim-filing rule. This file is scratch, not a commit target.

---
**unverified:** I am a Mistral AI model, version and snapshot unknown to me.

---

### Q1. Which option, and why.
**Option B: Add `scored-self-answer`.**
The table shows 21 core claims where the same design (inject-then-ask) is typed `interpretability` in 11 rows and `behavioural` in 10. This inconsistency violates the library’s rule that evidence type should reflect what was done and measured, not the authors’ framing. A neutral value names the class without deciding Q3, removes the inconsistency, and makes the class filterable. The framework sentence rule is unchanged because it keys on what was done (steering/injection) and measured (the answer), not on type.

**Strongest case against:** A permanent third category can become a parking place for claims that should be decided. A dossier line reading "scored-self-answer" tells a legislator less than "behavioural" or "testimony".

**Confidence:** high.

---

### Q2. The three instruments.
**Trained-channel control:** Right test. A fine-tuned channel (Ferrara c04) shows the information is available to the model, but not that it is used in ordinary operation. A result counts for self-access only if the channel’s performance exceeds the base model’s on the same task; against if it does not. The result could be produced without access (e.g., a probe that reads the intervention directly).

**Privileged-access test:** Right test. A second model given the same transcript must not match the "self"-report (Song, Lederman et al.). A result counts for self-access if the second model fails to match; against if it matches. The result could be produced without access (e.g., a model trained to mimic the first model’s answers).

**Measured coupling:** Right test. A link between the report and an internal probe on the same system (test 9) is the strongest evidence. A result counts for self-access if the report and probe correlate; against if they do not. The result cannot be produced without access.

**What is missing:** A fourth instrument: **cross-model replication**. If multiple models with different architectures show the same coupling, it rules out family-specific artifacts.

**Confidence:** high.

---

### Q3. Dossier reading.
**Option A (`ambiguous`):** A legislator may read it as a methods caveat (UKAISI c05) rather than a neutral marker, dismissing the claim as unreliable.

**Option B (`scored-self-answer`):** A legislator may read it as a settled category, assuming the library has decided the answer shows nothing about self-access.

**Option C (`behavioural`):** A legislator may read a correct detection rate as evidence of access, assuming the answer is a behaviour like any other.

**Option D (`self-report-testimony`):** A legislator may read it as zero-weight testimony, ignoring the score even where it exceeds a control (Ferrara c04).

**Option E (split by design):** A legislator may read the sub-class as answering Q3, assuming `interpretability` means access and `behavioural` means no access.

**Confidence:** medium.

---

### Q4. A parking place.
**Yes, it could.** Exit rule: **any claim that meets one of the three instruments (trained-channel, privileged-access, measured coupling) must be re-typed** as `behavioural` (if the instrument shows no access) or `interpretability` (if it shows access). The rule is enforced by the index script, which flags claims with `scored-self-answer` and no instrument result for council review.

**Confidence:** high.

---

### Q5. Boundary cases.
- **Ferrara c04:** In. The fine-tuned channel is a scored self-answer, even if the authors treat it as instrument validation.
- **UKAISI c02:** In. The flagging half is a scored answer to "was that turn yours?".
- **Singh c01:** Out. The truth is a probe-derived label, not an imposed intervention.
- **AE c03:** Out. No external fact about the answer’s correctness exists.
- **Lederman c02:** Out. The scored object is yes-rates about another model’s transcript, not the model’s own states.

**Confidence:** high.

---

### Q6. Deciding Q3 itself.
The council needs **a study that measures coupling between a model’s self-report and an internal probe on the same system**, with cross-model replication. Example: a dataset of paired self-reports and probe readings under the same interventions, with correlation analysis. The library does not yet have such a study.

**Confidence:** high.

---

**FINAL: option B, confidence high**

**Argument against:** The new value could become a permanent third category, obscuring the need to decide Q3.
