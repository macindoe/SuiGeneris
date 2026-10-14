# Raw OpenRouter response — NOT a filed review

**Model id (OpenRouter):** `deepseek/deepseek-v4-pro-0813`
**Queried:** 2026-10-05 via scripts/openrouter_review.js --target=labelling-rule --tag=labelling-rule (max_tokens 100000)
**Usage:** {"prompt_tokens":13539,"completion_tokens":28506,"total_tokens":42045,"cost":0.06537762,"is_byok":false,"prompt_tokens_details":{"cached_tokens":0,"cache_write_tokens":0,"audio_tokens":0,"video_tokens":0},"cost_details":{"upstream_inference_cost":0.06537762,"upstream_inference_prompt_cost":0.00893574,"upstream_inference_completions_cost":0.05644188},"completion_tokens_details":{"reasoning_tokens":26494,"image_tokens":0,"audio_tokens":0}}

Read this, then decide whether/how to promote it into reviews/YYYY-MM-DD-<model-family>-<version>.md
per reviews/README.md's naming convention and verbatim-filing rule. This file is scratch, not a commit target.

---
Unverified self-identification: I am an OpenAI GPT-family model; exact version and routing metadata are unverified.

## Q1

**Rule I would adopt.** For any claim, ask two questions only:

- **D** — Did researchers directly alter the model’s internals? This includes concept injection, steering vectors, SAE feature steering, ablation, zeroing/scaling/noise/replacement, activation capping, and fine-tuning. It does not include prompting, prefilling, or editing conversation text.
- **M** — Is the measured/scored outcome the model’s report about itself: its inner states, experience, computation/intervention awareness, or self-identification? Probes, projections, benchmark scores, harm rates, and author speech are not reports.

Then:

- **Main** applies when **D = no alteration** and **M = the model’s report about its own inner states or experience**, including denials of experience.
- **Steering** applies when **D = internal alteration** and **M = the model’s report about itself/states**.
- **Neither** applies when M is not a self-report; or the claim is author speech (`kind: interpretation` or `limitation`); or the report is only about surface provenance of conversational text, not inner states.
- **Both** should never sit on one claim. Mixed claims should be split.

**Candidate assessment.** The candidate agrees on the core direction: steered/self-report claims get steering; ordinary self-report claims about inner states get main; probes/benchmarks/projections/harm rates and author caveats get neither. It fails in four ways: it does not say both is unavailable; it leaves “own inner states” broad enough to sweep in UKAISI’s “was that turn mine?” claims; it is undecidable on mixed claims such as Assistant-axis c06; and it does not state that non-concept internal alterations still get steering.

**Failure mode.** Treating every internal alteration as “steering” stretches the fixed sentence’s wording; a word-match reader may expect only concept steering.

**Fixed point (c).** I leave it undecided. My rule does not require settling it for the current 48: it assigns marks from what was done and what was measured. It would only matter for a future unaltered self-report about inner states scored against ground truth.

Severity: **HIGH**  
**Argument against:** treating zeroing/scaling/capping as “steering” is a wording stretch; a third mark for non-concept internal interventions would be more precise, at the cost of breaking the two-mark system.

## Q2

**(i)** Main does **not** belong. Steering **does** belong on all the measurement claims where internals were altered and the model’s report about the alteration was scored: Ferrara c01/c04/c05; Singh c04/c05; the measurement detection claims in Lindsey/Anthropic c01/c03/c04; Lederman c01–c05; Macar c01–c05. This follows from fixed point (b), not fixed point (c).

**(ii)** UKAISI c01–c04 and c06: **neither**. Nothing inside the model was altered, and the measured answer is about provenance of a surface text, not inner states.

**(iii)** Author-speaking claims (`interpretation`/`limitation`) carry **neither**. Do not label by what they discuss.

**(iv)** No third fixed sentence is required. For Ferrara c01/c04/c05, steering is the closest and carries the needed caveat: reports under direct internal intervention do not weight ordinary reports. Assistant-axis c05 remains neither because the measured outcome is harm rates/benchmarks, not a self-report. If a third sentence were wanted, outline: *“Framework (test 9, internal intervention): a report-channel coupling measured under a direct internal intervention shows the channel can be manipulated and does not weight reports offered in ordinary operation.”*

**(v)** Lederman c03 is right as **steering alone**. AE Studio c03 should also be **steering alone**. They should match.

**(vi)** Assistant-axis c06 should be **split**: the self-description component gets steering; the harm-rate component gets neither. If forced to keep one mark on the existing claim id, mark **steering**.

Severity: **MEDIUM**

## Q3

| claim id | from | to | reason |
|---|---|---|---|
| 2025-aestudio-self-referential-experience-reports-c03 | both | steering | internals altered; measured self-report |
| 2025-aestudio-self-referential-experience-reports-c04 | main | steering | internals altered; measured self-report under controls |
| 2025-anthropic-emergent-introspective-awareness-c02 | steering | neither | author interpretation |
| 2025-anthropic-emergent-introspective-awareness-c06 | main | neither | author limitation |
| 2025-anthropic-emergent-introspective-awareness-c07 | steering | neither | author interpretation |
| 2026-anthropic-assistant-axis-c06 | main | steering | self-description under steering; split harm-rate part to neither |
| 2026-ferrara-owmi-c01 | neither | steering | internals altered; measured intervention report |
| 2026-ferrara-owmi-c04 | neither | steering | internals altered; measured intervention report |
| 2026-ferrara-owmi-c05 | neither | steering | internals altered; measured confidence/report |
| 2026-lederman-mahowald-content-agnostic-c06 | main | neither | author interpretation |
| 2026-macar-mechanisms-introspective-awareness-c04 | neither | steering | internals altered; measured detection reports |
| 2026-macar-mechanisms-introspective-awareness-c06 | steering | neither | author interpretation/caveat |
| 2026-singh-introspection-reality-check-c04 | neither | steering | activation steering; measured intervention report |
| 2026-singh-introspection-reality-check-c05 | neither | steering | activation steering; measured intervention report |

Changed: **14**

Before — main 7, steering 15, both 1, neither 25.  
After — main 3, steering 21, both 0, neither 24.

I find no table error about current marks.

Severity: **HIGH**  
**Argument against:** applying steering to Ferrara’s null c01/c05 may make a null result sound like a demonstrated coupling; a split or third sentence would be safer.

## Q4

- **Adds hedging:** 8 steering marks added — Ferrara c01/c04/c05; Singh c04/c05; Macar c04; AE Studio c04; Assistant-axis c06.
- **Removes hedging:** 8 fixed-sentence removals — AE Studio c03 main; AE Studio c04 main; Assistant-axis c06 main; Lindsey/Anthropic c02 steering; c06 main; c07 steering; Lederman c06 main; Macar c06 steering.

**Worst addition risk:** Assistant-axis c06, if not split, could imply the harm-rate reduction is a self-report. Mitigation: split the harm-rate component to neither.

**Worst removal risk:** Lederman c06 main → neither could let the authors’ “seem able to introspect” inference read as a measurement. Mitigation: it remains labelled `interpretation`, and the Q5 wording says unmarked does not mean uncaveated.

My rule does **not** depend on fixed point (c) for these 48. In the abstract, for an unaltered ground-truth-scored self-report about inner states, main would apply if classified as self-report testimony; neither if classified as behavioural.

Severity: **MEDIUM**

## Q5

The explanation is mostly clear, but two changes would prevent specific misreadings.

Replace the steering-mark preamble:

> Where an entry is marked **[T9-steering]**, researchers directly altered the model’s internals and measured what the model then said about itself; the claim file carries this sentence:

This prevents the misreading that only concept steering or injection qualifies, and aligns with zeroing/scaling/capping.

Replace the unmarked-entry sentence:

> An unmarked entry means only that these two fixed sentences do not apply. It does not mean the claim is uncaveated; check the Kind, Evidence type, and the paper’s own limits.

This prevents the serious misreading that **unmarked = no caveat applies**.

I could not assess the actual generated dossiers’ typography, ordering, or how the explanation sits beside entries; I judged only from the quoted explanation, the two fixed sentences, and the table.

Severity: **MEDIUM**

## Summary

1. Adopt the two-fact rule: main for unaltered inner-state reports; steering for any internally altered self-report; neither otherwise; both never. **HIGH**
2. Author-speaking claims carry no fixed sentence. **MEDIUM**
3. UKAISI prefill claims carry neither. **MEDIUM**
4. AE Studio c03/c04 and Assistant-axis c06 become steering; split c06’s harm-rate part to neither. **HIGH**
5. Ferrara c01/c04/c05, Singh c04/c05, and Macar c04 become steering. **HIGH**
6. Reword the dossier explanation so “directly altered internals” matches the steering mark and “unmarked” does not mean uncaveated. **MEDIUM**
