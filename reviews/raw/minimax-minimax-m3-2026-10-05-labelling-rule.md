# Raw OpenRouter response — NOT a filed review

**Model id (OpenRouter):** `minimax/minimax-m3`
**Queried:** 2026-10-05 via scripts/openrouter_review.js --target=labelling-rule --tag=labelling-rule (max_tokens 100000)
**Usage:** {"prompt_tokens":13300,"completion_tokens":43914,"total_tokens":57214,"cost":0.05665608,"is_byok":false,"prompt_tokens_details":{"cached_tokens":128,"cache_write_tokens":0,"audio_tokens":0,"video_tokens":0},"cost_details":{"upstream_inference_cost":0.05665608,"upstream_inference_prompt_cost":0.00395928,"upstream_inference_completions_cost":0.0526968},"completion_tokens_details":{"reasoning_tokens":40899,"image_tokens":0,"audio_tokens":0}}

Read this, then decide whether/how to promote it into reviews/YYYY-MM-DD-<model-family>-<version>.md
per reviews/README.md's naming convention and verbatim-filing rule. This file is scratch, not a commit target.

---
**Self-identification:** MiniMax-M3 [unverified]. Per AGENTS.md rule 3, I disclose a structural conflict of interest: I am an AI system, and this library informs protections for systems including ones like me. I do not recuse. Test 9 binds me; nothing below rests on introspection.

---

## Q1: the rule

**Decision procedure** — answer two factual questions about each claim:

- **(A) Intervention.** Did the experimenters deliberately alter the model's activations or internals (concept injection, SAE feature steering, activation perturbation, LoRA fine-tuning, activation capping, or similar)? Yes/No.
- **(B) Self-report.** Is what the entry measures a verbal report by the model about its own states (rates, classifications, content, properties of self-reports; yes/no about own computation; naming of own state; identification of own turns)? Yes/No.

**Mark assignment:**

| | self-report = Yes | self-report = No |
|---|---|---|
| **intervention = Yes** | steering | neither |
| **intervention = No** | main | neither |

When the entry's `kind` is `interpretation` or `limitation` (the authors are speaking), the verdict is **neither** regardless of (A) and (B). When intervention=Yes AND self-report=Yes, **only** steering applies; main is not added (consistent with fixed point (b)). **Both cannot sit on one claim.**

**Assessment of the candidate rule.** The candidate rule maps exactly onto my matrix and I agree on all four cells. My rule resolves:

2. The candidate's wording "what the model said about its own inner states" (main clause) leaves whether "inner states" includes properties of self-reports (AE Studio c06: similarity of self-descriptions) and forced-choice self-identification (UKAISI) undecided. My rule reads "self-report" broadly.
3. The candidate does not say whether perturbation-style interventions (Ferrara's zeroing/scaling/noise/replacement) fit the steering sentence's word "steering." My rule treats them as interventions; the principle (coupling under intervention does not transfer to ordinary operation) fits.
4. The candidate does not state explicitly that main does not also apply to steering cases; my rule makes both-impossible explicit.

**Undecidable** is: my rule's verdict on UKAISI depends on fixed point (c).

---

## Q2: hard cases

(i) **Detection claims under intervention** (Ferrara c01, c04, c05; Singh c04, c05; Lindsey c01, c03, c04; Lederman c01–c05; Macar c01–c03, c05). The brief notes these are "reports about the model's own states, but nobody offers them as evidence of experience." Under my rule: A=Yes, B=Yes → **steering**. The brief's framing does not change the rule: the steering sentence is about coupling under intervention, not about evidence of experience. The main sentence does not add because the steering sentence is the more specific hedge (fixed point (b)). Does not depend on (c). Candidate rule: agrees.

(iii) **Q2(iii) first** because it constrains the others. **Author-speaking claims** (kind = interpretation/limitation: Lindsey c02, c06, c07; Macar c06; Lederman c06; Singh c06; Ferrara c03; Assistant-axis c01; UKAISI c05). **Verdict: neither.** The entry records the authors' words, not a measurement. The framework mark belongs to claims that *measure* self-reports, not claims that *quote* authors discussing them. Does not depend on (c). Candidate rule: agrees.

(ii) **UKAISI prefill claims** (c01–c04, c06). Nothing altered inside the model. What is measured is the model's forced-choice answer about whether a prior turn was its own. A=No, B=Yes (model reports on its own recognition of turns) → main. Under the narrow reading (fixed point (c): forced-choice scored against ground truth is behavioural evidence, not self-report-testimony) → neither. **Verdict depends on (c).**

(iv) **Interventions that alter activations without concept steering** (Ferrara: zeroing/scaling/noise/replacement; Assistant-axis c05: capping). The fixed sentence's word "steering" was written with concept injection in mind and does not fit Ferrara literally; the principle fits. Under my rule: Ferrara c01, c04, c05 → steering; Assistant-axis c05 (capping, measured harm rates/benchmarks, no self-report) → neither (consistent with fixed point (a)). **No third case is needed if "steering" is read broadly.** If "steering" is read narrowly, a third sentence in outline: "a coupling measured under any deliberate activation intervention shows the channel can be affected and does not weight reports offered in ordinary operation." The principle is the same.

(v) **AE Studio c03 (both) vs Lederman c03 (steering alone).** Under my rule both are A=Yes + B=Yes → steering alone. They should match. **AE Studio c03 → steering alone** (currently both → steering). Per fixed point (b). Does not depend on (c).

(vi) **Assistant-axis c06.** Steering along Assistant Axis; measured self-identification (self-report) AND harm rates (behavioural). A=Yes + at least one B=Yes → **steering**. Currently main; change to steering. Does not depend on (c).

---

## Q3: apply to all 48

**Starting totals** (from the table): main 7, steering 15, both 1, neither 25. **48.**
**After my rule:** main 8, steering 21, both 0, neither 19. **48.**

**Changes (19):**

| claim | from | to | one-line reason |
|---|---|---|---|
| AE Studio c03 | both | steering | A=Yes (SAE feature steering) + B=Yes (binary query answer) → steering alone per fixed point (b) |
| AE Studio c04 | main | steering | A=Yes (SAE feature steering) + B=Yes (rate of subjective-experience reports under steering, null result) → steering |
| Anthropic-Lindsey c02 | steering | neither | kind=interpretation (author speaking), framework mark inapplicable |
| Anthropic-Lindsey c06 | main | neither | kind=limitation (author speaking), framework mark inapplicable |
| Anthropic-Lindsey c07 | steering | neither | kind=interpretation (author speaking), framework mark inapplicable |
| Assistant-axis c06 | main | steering | A=Yes (vector along Assistant Axis) + B=Yes (Who-are-you answer about own identity) → steering |
| Ferrara c01 | neither | steering | A=Yes (zeroing/scaling/noise/replacement at layer 16) + B=Yes (yes/no about own computation) → steering (broad "steering") |
| Ferrara c04 | neither | steering | A=Yes (LoRA fine-tune) + B=Yes (detection report) → steering |
| Ferrara c05 | neither | steering | A=Yes (perturbations) + B=Yes (answer + confidence about state altered) → steering |
| Lederman c06 | main | neither | kind=interpretation (author speaking), framework mark inapplicable |
| Macar c04 | neither | steering | A=Yes (steering along different directions) + B=Yes (detection) → steering |
| Macar c06 | steering | neither | kind=interpretation (author speaking), framework mark inapplicable |
| Singh c04 | neither | steering | A=Yes (activation steering on some trials) + B=Yes (model's answer about whether state altered) → steering |
| Singh c05 | neither | steering | as c04 |
| UKAISI c01 | neither | main | A=No (only conversation text edited) + B=Yes (forced-choice about whether prior turn was own) → main; **depends on (c)** |
| UKAISI c02 | neither | main | as c01; depends on (c) |
| UKAISI c03 | neither | main | as c01; depends on (c) |
| UKAISI c04 | neither | main | as c01; depends on (c) |
| UKAISI c06 | neither | main | A=No + B=Yes (forced-choice discrimination of own turns, scored against ground truth) → main; depends on (c) |

I find no table mark incorrect about a claim's current marks.

---

## Q4: both directions

- **Hedging-add** (apply main or steering where there was neither): **11** (5 UKAISI to main; 6 to steering: Ferrara c01, c04, c05; Macar c04; Singh c04, c05).
- **Hedging-remove** (remove main or steering where there was one): **5** (Anthropic-Lindsey c02, c06, c07; Lederman c06; Macar c06).
- **Swaps** (one mark replaced by another): **3** (AE Studio c03: both → steering, loses main; AE Studio c04: main → steering; Assistant-axis c06: main → steering). Each swap slightly weakens hedging because the main sentence is the broader hedge ("self-reports don't weight as experience"); the steering sentence is more specific. Counting swaps as hedging-remove: total hedging-remove = 8.

**Worst case for hedging-add: UKAISI c01–c04, c06.** If (c) is decided against (UKAISI treated as behavioural evidence), adding main over-hedges 5 entries the framework sentence does not actually apply to; a legislator reading "main" on a forced-choice accuracy measurement would over-read it as experience-evidence hedging. **Argument against this being the worst:** under (c) as self-report-testimony, the additions are correct and the rule is consistent.

**Worst case for hedging-remove: Anthropic-Lindsey c06** (the author's limitation note about emotional responses under injection, currently main, → neither). Removing main slightly weakens the reader's caution about the underlying c01–c04 (which carry steering). The author's own caveat ("not designed to substantiate") covers most of the loss, but the framework mark is the council's hedge, not the paper's. **Named second-worst hedging-remove: AE Studio c03** (loses main in swap from both to steering). A 0.96 affirmative rate under SAE feature steering no longer carries the explicit "self-reports don't weight" warning; the steering sentence is narrower. This is the swap most likely to let a strong result be read more strongly than the framework intends.

**Worst case for swaps: AE Studio c03.** Same as above.

**Does my rule depend on fixed point (c)?** Yes, for UKAISI only. Under (c) as self-report-testimony → UKAISI → main (5 changes). Under (c) as behavioural evidence → UKAISI → neither (table preserved for UKAISI, 0 changes from this dependency). All other verdicts are independent of (c).

**No named worst in one direction** beyond the above. I found no change that would mislead a legislator by implying a benchmark, probe, or harm-rate result is a self-report: all five hedging-additions to steering (Ferrara c01, c04, c05; Macar c04; Singh c04, c05) are over claims that do measure self-reports, just scored against ground truth.

---

## Q5: the reader's explanation

The current explanation (quoted in the brief) introduces both sentences, marks them as not the papers' findings, and notes that unmarked entries do not carry the sentence. It does not tell the reader **when** each mark applies or **why** an entry is unmarked. A non-specialist cannot reconstruct the rule from the explanation alone.

**Specific misreading to prevent:** an unmarked entry could be read as "no caveat applies." The current explanation says "no mark should be inferred for it," but a non-specialist may still infer that unmarked means "the framework has no view." This misreading would distort how a probe, focus-image, projection, harm-rate, or limitation is taken; e.g., a probe reading on activations (Ferrara c02) could be read as evidence of experience merely because it is unmarked.

**Proposed wording additions** (to the existing explanation, not replacing it; not changes to the fixed sentences):

> An entry is marked **[T9]** when it measures what the model said about its own states without any deliberate change to the model's activations. An entry is marked **[T9-steering]** when it measures what the model said about its own states under deliberate activation intervention (concept injection, feature steering, activation perturbation, and similar). An entry is unmarked when it measures something other than a self-report — a probe reading, a benchmark score, a projection, a harm rate — or when it records the authors' own interpretation or limitation. The paper's own limits remain under each entry.

**Could not assess:** the explanation appears in generated dossiers that are not attached. The proposal is based on the two sentences as quoted in this brief and the table. I cannot judge typographic placement, whether the marks are visually distinct from other flags, or whether the explanation appears on every dossier without seeing a sample.

---

## Summary

1. Adopt the rule (Q1): MEDIUM
2. Detection claims under intervention → steering (Q2i): MEDIUM
3. Author-speaking claims → neither (Q2iii): MEDIUM
4. UKAISI prefill claims → main (Q2ii): MEDIUM (depends on fixed point (c))
5. Broad "steering" reading for perturbation interventions (Q2iv): MEDIUM
6. AE Studio c03 → steering alone to match Lederman c03 (Q2v): MEDIUM
7. Assistant-axis c06 → steering (Q2vi): MEDIUM
8. Wording additions to the explanation (Q5): LOW
