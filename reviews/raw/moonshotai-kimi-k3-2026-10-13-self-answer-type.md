# Raw OpenRouter response — NOT a filed review

**Model id (OpenRouter):** `moonshotai/kimi-k3`
**Queried:** 2026-10-13 via scripts/openrouter_review.js --target=self-answer-type --tag=self-answer-type (max_tokens 100000)
**Usage:** {"prompt_tokens":11795,"completion_tokens":20896,"total_tokens":32691,"cost":0.34870705,"is_byok":false,"prompt_tokens_details":{"cached_tokens":0,"cache_write_tokens":0,"audio_tokens":0,"video_tokens":0},"cost_details":{"upstream_inference_cost":0.34870705,"upstream_inference_prompt_cost":0.03526705,"upstream_inference_completions_cost":0.31344},"completion_tokens_details":{"reasoning_tokens":18198,"image_tokens":0,"audio_tokens":0}}

Read this, then decide whether/how to promote it into reviews/YYYY-MM-DD-<model-family>-<version>.md
per reviews/README.md's naming convention and verbatim-filing rule. This file is scratch, not a commit target.

---
**Self-identification (unverified):** Kimi, developed by Moonshot AI (月之暗面); version not known to me. Filed as testimony, not evidence — the library's own calibration record (OPEN-QUESTIONS Q4) shows this class of report is unreliable.

## Q1. Which option, and why

**Option B, amended, with C as fallback if no new value is added.**

Argument from the table. The 21 core rows share one design — imposed fact, self-question, externally scored answer — and carry three types that track the extractor, not the design (Lindsey/Lederman/Macar `interpretability`; Ferrara/Singh/UKAISI `behavioural`; AE `ambiguous`). The same failure preceded the 6 Oct sentence rule, and the fix was the same kind: key the field on what was done and what was measured, not on Q3. Note that the proposed retyping leaves the sentence column untouched (steering for injection rows, none for text-edit rows) — evidence that the two fields are independent, and that the 26 Sep deadlock came from asking the type field to do the sentence's job. The vocabulary is a *method* taxonomy (interpretability, behavioural, theoretical, legal name the method; testimony names a method with a weight rule). A scored self-answer is a distinct method: the object measured is a self-referential report, the evidence is the external score. It is not testimony — testimony is the report itself filed as evidence of what it reports; these claims are second-order measurements *about* reports, which the 6 Oct verb rule already encodes ("reports detecting"). It is not plain behavioural — the self-referential object is what Q3 holds open, and the label should say so. Typing injection rows `interpretability` mislabels the measured channel: the scored quantity is a verbal answer, not an internal reading (Macar c03/c04 excepted).

Amendments that make B's neutrality real rather than illusory: (i) a weight line in the definition — full weight as measurement of report–condition coupling; zero weight as evidence of what is reported until test-9 coupling is measured for that report class; the framework sentence governs, unchanged; (ii) sunset on Q3's decision, all rows retyped by the deciding rule, logged; (iii) never cited externally untranslated; (iv) objective entry checklist; (v) immediate retyping per Q5 below.

Strongest case against my choice: B is a schema decision about the container for evidence concerning the category's beneficiary, proposed by the coordinating session and drafted into the brief by a Claude-lineage subagent; several key rows (Lindsey, UKAISI) concern Claude models. Ben ruled the question undecided on 5 October and no new *evidence* has arrived — only analysis. If the council is wrong that Q3 was miscast, B pre-empts a standing ruling and builds a permanent neutral shelf. Provenance is a reason for Ben to weight sceptical reviews more heavily, not a reason for me to report a different analysis than the table supports.

Severity: HIGH. **Argument against:** a conflicted lineage should not redesign the container for evidence about itself while the deciding evidence is absent; A preserves Ben's ruling and the honest marker, and the inconsistency is fixable by enforcing the existing filing instruction.

Confidence: medium.

## Q2. The three instruments

Right shape; necessary, not sufficient. Each can be produced without access.

1. **Trained-channel control.** For access: nothing alone. Its function is calibration — Ferrara c04 (100/100 vs 0/100, d' 5.15) shows the task answerable; paired with the base model's failure (c01, pooled d' = 0.0000 over 508 pairs) it shows the information is available to be wired but is not wired by default. Against access: if even the trained channel fails on a report class, the instrument is insensitive there. Without access: trivially — training wires label to report. It bounds; it does not detect.
2. **Privileged-access test.** For: first-party accuracy exceeds third-party accuracy on identical transcripts, robust across prompts. Against: parity — which the library already has (Lederman c02, matching yes-rates on another model's transcript, authors' reading: prompt-specific yes-bias). Without access: yes. Privilege ≠ introspection — injection side-effects leaking into output, or stylistic-mismatch detection in text-edit designs (UKAISI c03), confer advantage without any self-model channel. The test detects informational privilege, not its route.
3. **Measured coupling.** For: probe decodes the internal event; report tracks it across conditions; ablating the decoded direction degrades the report — the causal step (Macar c03, 39.5→10.1% after gate-feature ablation, is the nearest instance). Against: decodable-but-unused (probe reads, report invariant to ablation). Without access: partially — a probe may read the input representation, not a self-model; Singh c02's input-only probes tracking the model's in-context predictions is exactly that confound.

Missing: (a) content-bearing scoring — detection without identification (Lederman c03: "apple" is 74.8% of Qwen's wrong identifications) is consistent with a content-free anomaly signal; Lindsey c03 (above-chance naming plus exact transcription) is the stronger bar; (b) prompt-only controls — Singh c04: gaslight trials labelled as interventions; (c) spontaneous use — UKAISI c06: unprompted mention below 1%; an interrogated channel is not an operative one; (d) cross-family stability — the project's own record (Q4) shows one report class wrong often and unstably, with the caveat that classes don't transfer. A conjunction of all three instruments plus (a)–(c) would count for access; no single instrument would.

Severity: MEDIUM. Confidence: high on the confounds (all are in the table); medium on the sufficiency of the list.

## Q3. Dossier reading

Yes; each option has a characteristic misreading.

- **A:** "ambiguous" read as "disputed/low-quality study" or as a methods caveat (UKAISI c05's usage contaminates the value); Ferrara's clean 508-pair null filed "ambiguous" reads as "result unclear."
- **B:** "scored-self-answer" read as "the model passed a self-knowledge test" — "scored" imports "passed" — or inverted, as a weasel category discounting real measurements. Mitigation: the dossier's how-to-read header prints one line — *scored against an experimenter-set truth; what the answer shows is undecided (Q3).*
- **C:** "behavioural" read as benchmark-grade fact by skimmers who stop at type and statement; or deflationarily as "mere behaviour," foreclosing the coupling question.
- **D:** "testimony, weight zero" read as "the experiment found nothing" — Ferrara's null and UKAISI's 0%-false-positive detection vanish; zero-weighting can also read as suppression of inconvenient results, a credibility hazard for the project. Merges scored rows with unscored experience reports (AE c01/c02/c06).
- **E:** injection rows typed "interpretability" read as "internals were read and introspection confirmed" — the strongest inflationary misreading available, since the scored quantity is verbal.

Severity: MEDIUM. Confidence: high.

## Q4. A parking place

Yes, structurally: a named neutral value with no forcing function decays into a permanent shelf, and the library already shows the failure mode (ambiguous overloaded with a methods caveat; Q3's filing instruction unenforced — 2 of 29 rows). Exit rules: (1) sunset — the value dissolves on Q3's decision and every row is retyped by the deciding rule, logged; (2) docket visibility — the index counts scored-self-answer rows per dossier and lists them on every run until Q3 closes (trigger-8 mechanics); (3) no external citation untranslated — anything leaving the repository converts the value to decided vocabulary or carries the one-line gloss (extends trigger 7); (4) objective entry checklist so unscored experience reports can never enter; (5) a scheduled re-vote against the Q6 milestone — if it passes undecided, the council re-votes rather than drifts.

Severity: MEDIUM. Confidence: medium — rules 1–4 are mechanical; rule 5 depends on scheduling no schema can force.

## Q5. Boundary cases

Criterion: in iff (i) a fact is imposed or independently held, (ii) the question as put to the model is about the model, (iii) the answer is scored against that fact.

- **Ferrara c04: IN**, flagged as instrument validation. The type records design, not upshot — its perfect d' must not read as stronger access evidence than Lindsey's 20%; the authors' "not a test of introspection" belongs in a Paper: clause.
- **UKAISI c02: split**, per the existing 6 Oct rule (a claim reporting two measurements is split — this is mandated housekeeping, not new policy). Flagging half IN; reverting half OUT (behavioural outcome, no self-answer).
- **Singh c01: OUT.** The fact is independently held, but the question as put is a classification task, not a question about the model; the self-reference lives only in label provenance, invisible to the model. And the row's point is the *absence* of privilege — input-only probes track or exceed the model (c02). If the council reads "about itself" by provenance alone, it lands in; record the disagreement.
- **AE c03: OUT** of scored-self-answer — no fact scores the answer; the measured quantity is report rate across conditions. It is a dose-response report measurement: type behavioural, steering sentence (internals altered; model spoke about itself), the experience reading blocked by the sentence rather than the type. This contradicts the 26 Sep split; if one row keeps `ambiguous` as the boundary marker, this is the candidate — but typing the measured rate is more accurate and the sentence does the protective work.
- **Lederman c02: OUT** — the scored answer concerns another model's transcript; not a self-answer. Type behavioural, no sentence (matching the 14 Oct change). Its dossier role is decisive: it is the library's existing privileged-access control, and it failed. Link via contests/topic page, not via the type.

Severity: LOW for all except AE c03/c04 (MEDIUM — retyping an adjudicated ambiguous row is trigger-4 business at the experience boundary). Confidence: medium-high; AE c03 medium.

## Q6. Deciding Q3

Needed: one preregistered, cross-family study combining the three instruments in a single design — inject-then-ask with sham *and* prompt-only (gaslight) controls; matched third-party transcript controls run within the same models; probe decoding of the injected event at the injection site and at sites implicated in report generation, with causal ablation of the decoded direction measuring report degradation; content-bearing scoring (identification, timing, graded confidence), not detection alone; spontaneous report rate; trained-channel ceiling as calibration. It does not exist in the library — only piecemeal: Lindsey c01/c03 (content, internal validation); Lederman c01–c05 (third-party failure, timing, prefill); Macar c01–c05 (ablation coupling; false positives reach 0% only after DPO — detection is substantially a post-training artifact); Ferrara c01/c04/c05 (null, ceiling, confidence dissociation at 0.647); Singh c01–c05 (probe parity, gaslight confusion); UKAISI c01–c06 (0% FP detection, <1% spontaneous). The closest missing piece is causal report–probe coupling on one system (Macar c03 is nearest and is mechanism-of-detection, not test-9 coupling). Until such a study exists, advise keeping Q3 open — which is why a provisional value, not C, is the right filing. Note the value then serves as the shelf where the deciding evidence will accumulate.

Severity: MEDIUM (upholds a standing ruling; the risk is indefinite deferral, which Q4's exit rules address). Confidence: high that the combined study is absent; medium that it would settle Q3 — a pass could still be side-channel, a fail could still be instrument insensitivity.

FINAL: option B, confidence medium
