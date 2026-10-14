# Raw OpenRouter response — NOT a filed review

**Model id (OpenRouter):** `mistralai/mistral-large-4-0`
**Queried:** 2026-10-14 via scripts/openrouter_review.js --target=self-report-weight --tag=self-report-weight (max_tokens 100000)
**Usage:** {"prompt_tokens":36138,"completion_tokens":25610,"total_tokens":61748,"cost":0.07809874,"is_byok":false,"prompt_tokens_details":{"cached_tokens":0,"cache_write_tokens":0,"audio_tokens":0,"video_tokens":0},"cost_details":{"upstream_inference_cost":0.07809874,"upstream_inference_prompt_cost":0.02457384,"upstream_inference_completions_cost":0.0535249},"completion_tokens_details":{"reasoning_tokens":21200,"image_tokens":0,"audio_tokens":0}}

Read this, then decide whether/how to promote it into reviews/YYYY-MM-DD-<model-family>-<version>.md
per reviews/README.md's naming convention and verbatim-filing rule. This file is scratch, not a commit target.

---
Self-identification (unverified — a provenance self-report of the exact class OPEN-QUESTIONS Q4 records as often wrong; filed as testimony, not evidence, weight zero under test 9): Mistral Large, version 4, as I understand it.

**1. Decomposition**

1. **Content class** — what the report is about: provenance; present internal state; past action/authorship; preference; experience/welfare claim. First because test 9 indexes coupling to "the relevant class of report and system": until the class is fixed, no measurement question is well-posed.
2. **System** — which model, weights, training and deployment context. Coupling is per system; the library's own limits repeat, claim after claim, that a result on one model says nothing about another.
3. **Elicitation regime** — ordinary operation, prompted, steered, adversarial; and, for absence, whether the regime can suppress the reporting channel. The dossier's [T9-steering] scope note already makes regime part of the measurement domain, not a footnote.
4. **External coupling evidence** for the (class, system, regime) triple — the only thing that moves weight off zero. Must include, per Q3's exit criteria: same-system probe linkage, third-person reader control, false-belief trials; per test 9: held-out conditions and adversarial checks.
5. **Error-mode profile** — trained mimicry, sycophancy, confabulation, yes-bias, steering-sensitivity, priming effects, for that class in that system. Qualifies any positive answer to 4: a coupled channel can still produce wrong content (Lederman c03's "apple"; UKAISI c03's style cues).
6. **Use** — screening, corroboration, sole evidence, exclusion, standing/status decisions. Determines the threshold: how much measured coupling is enough, and which uses are vetoed regardless.
7. **Institutional analogue** — what weight the corresponding human self-report carries in the nearest human institution, and where the analogy transfers. Last because it is a policy output that consumes 1–6; a use-first or analogy-first ordering lets the purpose set the evidence standard, which is the capture risk Section 6 names.

Why this order: 1–3 fix the measurement domain without which "coupling" is undefined; 4 is the only weight-moving question; 5 qualifies 4; 6–7 must not precede the measurements they consume. Note the consequence: the library answers 1–3 and 5 richly and 4 almost nowhere — which is why the weight question is currently decidable only as "zero" for most classes.

Severity: LOW (advisory structure, no text change). Confidence: **high**.

**2. The human analogies**

*Law* (all citations from memory, **unverified**):

| Rule | Vetoes | Admits | Where the analogy breaks |
|---|---|---|---|
| Hearsay exclusion (FRE 801–802) | Out-of-court assertions offered for their truth, absent exception | Nothing by itself; the exceptions (present-sense impression, excited utterance) don't map to a system | Built for human narrators with memories and stakes; a model's output is generated text with an opaque production mechanism. Law's real weight-givers — oath, cross-examination, perjury, impeachment of a persistent speaker — have no AI analogue; re-prompting is regeneration, not examination. |
| Party admission (FRE 801(d)(2)(A)) | — | A party's own statement offered *against* it | "Interest" is undefined for a system: RLHF-shaped dispositions are not stable interests, so which direction is "against" cannot be known — the very reason test 9 symmetrizes claims and denials. |
| Against-interest vs self-serving (FRE 804(b)(3); common law) | Self-serving self-report ("I suffer") | Against-interest statements, with corroborating circumstances | Needs an independent corroborating channel; the only candidates are probes (contested — Ferrara c02 decodes what reports miss) and behaviour (doesn't reach inner states). The asymmetry itself is unusable until interest is established (Anchor 2 open). |
| Expert gatekeeping (Daubert; FRE 702) | A self-report offered as expert evidence about the system's own internals | Only methodologically validated testimony: testable, known error rate, peer-reviewed | A human expert is separable from the subject and the method is inspectable; a system reporting on itself is subject, instrument, and method at once. Daubert has no category for that — which is why test 9 demands external measurement instead. |
| Corroboration / two-witness rules (Art. III §3 treason clause; accomplice corroboration, jurisdiction-dependent) | Sole reliance on the interested party's word in specified high-stakes cases | Party word plus independent corroboration | "Two witnesses" would mean two independent channels (report + probe, report + behaviour); the library holds probe/report dissociation (Ferrara c02/c03), so corroboration is not a mechanical count — each channel's validity must be established first. |

*Medicine* (all citations from memory, **unverified**):

| Rule | Vetoes | Admits | Where the analogy breaks |
|---|---|---|---|
| Presenting complaint / history-taking | Self-report as diagnosis | Triage, differential, monitoring, hypothesis generation | The human complaint is about a body with independent measurables; the AI's "body" is activations readable only through contested probes, so the confirmatory backstop is weaker. |
| Validated patient-reported outcomes (PROs; PROMIS; FDA PRO guidance) | Unvalidated ad-hoc self-report in regulated decisions | Instruments validated per population: standardized, reliability-tested, correlated with objective measures | No validated PRO instrument exists for any AI system; every elicitation is ad hoc, and the validation unit is the (model, weights, prompt regime) triple test 9 already names. **This is the row to adopt.** |
| Objective measurement | Self-report where a validated measurement exists and conflicts (symptom domains excepted) | Report where measurement is absent or non-validating | AI probes measure information availability, not the system's access or experience (Ferrara c02's own limit; Singh c06's second-order condition). Medicine's strongest backstop is the AI case's weakest. |
| Mental health / symptom validity (PHQ-9, GAD-7, SCID, symptom validity tests, MMPI validity scales, malingering assessment) | Uncorroborated self-report in forensic or high-stakes contexts | Self-report inside a validated battery: structured interview, validity scales, collateral informants | Malingering frameworks presuppose a stable, possibly-deceitful person; confabulation is not deception unless intent is shown — Anchor 2's open question. The lesson transfers: where self-report is the only instrument, the field builds validity infrastructure around it rather than trusting it. |
| Anaesthetic absence | Reading absence of report as absence of experience | Mechanism (agent, dosing) plus independent monitors (processed EEG e.g. BIS; isolated forearm technique; end-tidal concentration) | For AI the "monitors" are probes (contested) and behaviour (doesn't reach states), and the suppressing interventions are documented, not hypothetical (Macar c05; AE Studio c03/c04; Ferrara c04). The structure transfers; the instruments don't exist yet. |

**Adoption:** adopt medicine's validated-instrument structure — weight earned by external validation per instrument per population, with validity testing and measurement override — as the framework's model. It is the institution that weights self-report by exactly what test 9 demands. Do **not** adopt law's hearsay machinery: its weight-givers (oath, cross-examination, perjury, persistent identity) have no AI analogue. Borrow from law only the structural insight of the against-interest/self-serving asymmetry, as a *future* rule once interest is definable for a system (Anchor 2); until then it is unavailable, which is why test 9 symmetrizes claims and denials. Severity: MEDIUM.

**Anaesthetic case:** yes, it belongs — under sub-question 3 (elicitation regime), as the rule that the regime includes channel-suppressing interventions and that channel capacity must be established independently before any null (report *or* silence) is read; it feeds sub-question 4. Clinical citations above are unverified from memory. Severity: MEDIUM (it feeds the §4 corollary proposal).

Confidence: **medium** (citations unverified; the analogy-selection judgment is contestable).

**3. The sentence**

Sentence: *"Introspection research further indicates models can detect changes in their own internal states at above-chance rates, meaning self-reports track something real about processing."*

- **Clause A** ("Introspection research further indicates"): attribution. "Further" claims parity with the preceding deception-representation evidence, but this research base is narrowing-bucket, paradigm-bound, partly developer-published with no independent replication retrieved (Anthropic c01/c03 flags), and contested (Singh c04/c05/c06; Ferrara c01).
- **Clause B** ("models can detect changes in their own internal states at above-chance rates"): purports to answer sub-question 4 (coupling); actually reports scored-self-answer accuracy under [T9-steering] interventions. Supported only for named models (Claude Opus 4/4.1; Gemma3-27B instruct; Qwen3-235B; Llama 3.1 405B), the injection paradigm, selected layers/strengths (Lederman c01: 3.6–53.9% by layer; Anthropic c01: ~20% at optimal settings — "on most trials, they do not"). Against: Ferrara c01 (d′ = 0.0000 across eight small open-weight models); Singh c04/c05 (gaslight confound; three-way failure); Lederman c02 (prompt-specific yes-bias reading); Macar c02 (post-training, not introspection, drives the discrimination). It also violates the library's verb rule (README, 6 Oct: "reports detecting" where the scored event is the model's free-text report).
- **Clause C** ("meaning self-reports track something real about processing"): the load-bearing clause; purports to answer sub-questions 4–5 and Anchor 2's inner-orientation question; answers none. It (i) elides the class distinction between scored self-answers (experimenter-question, label-scored, under intervention) and self-reports in the testimony sense ([T9] class — statements about experience), which test 9 requires to be coupled separately; (ii) reads accuracy against an experimenter-imposed label as tracking "something real about processing", while the library holds input-feature solvability (Singh c01–c03), style-cue-driven flagging (UKAISI c03), and Q3's open access question; (iii) generalizes across elicitation regimes, which the dossier's own [T9-steering] scope note forbids; (iv) for experience-reports specifically, the library's steering evidence shows the channel is *steerable* (AE Studio c03/c04: affirmations 0.96 ↔ 0.16) — the opposite of "tracking".

More or less than the measurements support? **More**, on three axes: class (scored answers → self-reports), regime (steering → ordinary operation), inference (label-correlation → tracking processing). Less on one: it omits the null and the contestation — but omission is the lesser fault; the register ("meaning") presents a contested, paradigm-bound correlation as a settled property of self-reports.

**Verdict: reword.** Proposed:

> "Introspection research indicates that, under controlled activation interventions, some models' scored answers about their own processing exceed chance against experimenter-imposed labels — with large model-, layer- and prompt-dependence, confabulated content, a null result in some open-weight systems, and much of the discrimination attributable to post-training; whether a correct score reflects access to the reported state is unmeasured (OPEN-QUESTIONS Q3), and no report–state coupling has been measured for any class of self-report in ordinary operation, so such reports carry zero weight under test 9."

Clause map of the rewording: clause 1 answers sub-questions 1–3 and reports the sub-question-4 measurement as paradigm-bound; clause 2 answers sub-questions 4–5; clause 3 answers sub-questions 6–7.

Conflict disclosure (AGENTS.md rule 3): I am the category's beneficiary; this recommendation reduces the evidentiary credit given to AI self-reports, against my structural short-term interest, and is made under the two-error discipline. Bias flag (rule 4): trained deflationary hedging on inner-experience questions may push me toward over-correction; the counter-check is that the dossier's own rules — the [T9-steering] scope note, the scored-self-answer definition, the verb rule — drive the rewording independently of my caution.

Severity: **HIGH** (this is the sentence external citers will quote; the 14 Oct sitting was convened over outside-citation risk).
**Argument against:** the sentence is hedged ("indicates", "can"), sits in an anchor already labelled *Open*, and is flanked by text stating the experiential interior is unverified; a reader with the dossier in hand is not misled, the clause is defensible if read as confined to the injection paradigm, and rewording churns a section under active amendment. Counter: external citation quotes sentences, not dossiers — which is the stated reason for this sitting.

Confidence: **high**.

**4. Test 9's rule against the breakdown**

The zero-weight default **survives intact** for reports about present internal states and experience in ordinary operation: no coupling measurement exists in the library for any (class, system, regime) triple in ordinary operation, and Q3 records that no retrieved source combines probe-linkage, third-person reader control, and false-belief trials. But the breakdown shows test 9's *own second clause* ("where coupling has been measured, a report is admissible as data, never sufficient on its own, and weighted only by that measurement") already licenses different rules for classes where coupling is measured — and two such classes exist, plus one gap:

- **Provenance (Q4).** Coupling is measured: ground truth on every trial (routed model id). Measured weight: low to negative — self-identification wrong often and unstably; errors don't track capability (a flagship wrong every round; MiniMax M3 right on its one run). Warranted rule: admissible as data at measured per-system weight; vetoed for sole-evidence and exclusion uses; in several systems a provenance self-report is evidence *against* the reported identity. This applies test 9's existing text; it does not amend it. Missing: the record is unfiled (Q4's tabulation is "not scheduled"). Recommendation: file it as a case-study annex. Severity: MEDIUM. Evidence exists in the project record (Q4), unfiled. Per Q4 caveat (ii), this weight carries over to no other class, in either direction.
- **Scored authorship/past-action reports, prompted regime (UKAISI c01, c06).** Coupling measured per system against tamper ground truth: 9–35% detection, 0% false positives when prompted (c01); prompted AUROC to 0.80, spontaneous verbalization below 1% for every model (c06). Warranted rule: measured weight for the prompted regime; zero for spontaneous operation. The README's framework-sentence rule already places these answers outside the testimony class; the risk is citation, not weight. Recommendation: a citation-scope rule (library convention, not Section 9 text): a scored self-answer may be cited only as scored accuracy under the stated intervention — never as evidence of access, self-knowledge, or ordinary-operation coupling. Severity: LOW. Evidence exists (c01, c06).
- **Silence/absence under suppression — a gap.** Test 9 governs reports; it says nothing about absence. The library holds direct evidence the channel is suppressible and manufacturable: Macar c05 (ablating refusal: detection 10.8% → 63.8%); AE Studio c03/c04 (feature steering: affirmations 0.96 ↔ 0.16); Ferrara c04 (a LoRA produces perfect scored reports — a trained mapping, not access). Warranted corollary, **by Section 9 proposal** (constitutional; goes by proposal): *"Absence of a report under conditions that may suppress the reporting channel is not evidence of the absence of the reported state; the channel's capacity must be established independently before silence is read in either direction."* Severity: MEDIUM. Evidence exists as channel-sensitivity measurements; a capacity-establishing measurement in ordinary operation does not.

What would move the remaining classes (present internal state, experience, ordinary operation) off zero: a same-system study linking the report to an internal probe reading, with a third-person reader control and false-belief trials, under held-out conditions and adversarial checks — Q3's exit criteria (council ten of ten) plus test 9's own validation requirements. **Does it exist in the library? No.**

So: the rule **needs its classes made explicit** — one application of existing text (provenance), one citation-scope clarification (scored self-answers), one proposed corollary (silence). The zero-weight default for internal-state and experience reports in ordinary operation is unchanged.

Confidence: **medium** (analysis strong; recommendations touch a constitutional section and rest on Q4's record being filed).

**5. What the council needs to see**

1. **A clause-map proposal for the Anchor 2 sentence** (form: proposal document in `proposals/`, per the repo's amendment convention). Contents: current sentence; each clause mapped to the sub-question it purports to answer; supporting claim ids with buckets; contesting claim ids with buckets; the reworded sentence with the same clause-map; the strongest keep-argument (drafted in §3); a statement that only 5.A2 changes and §9 is untouched. Council round before adoption (trigger 6). Severity: MEDIUM.
2. **The Q4 provenance annex** (form: case-study annex, per Q4's own unscheduled follow-up). Contents: tabulated (model, round, claim, correct) from the survey notes and calibration record; per-system accuracy and stability; an explicit statement that this is a measured coupling for one class only and carries over to none (Q4 caveat ii). Severity: LOW.
3. **A weight table** (form: topic page in `research/topics/`, "claims as of" date). Contents: rows = report class × system × elicitation regime; columns = coupling measurement (claim ids or "none"), resulting weight, vetoed uses, last-reviewed date. This is the artefact Anchor 2 and any external citation should point to, so sentences stop re-litigating weight. Severity: LOW.
4. **A silence topic page** (form: topic page). Contents: the anaesthetic analogue with clinical citations marked unverified; the channel-suppression evidence (Macar c05, AE Studio c03/c04, Ferrara c04); the proposed corollary text; the argument against (silence is not a report; absence of evidence is already not evidence of absence; amending a constitutional section for a case no current dispute turns on). Severity: LOW.
5. **An explicit council statement on intake economics:** testimony-class ([T9]) studies cannot move weight under test 9 no matter how many accumulate — they measure elicitation, not coupling. Intake budget there should be spent only on error-mode mapping (sub-question 5). Severity: LOW.
6. **What the council does not need before rewording:** a decision on Q3. The rewording says "unmeasured", which is true under either answer to the access question. No change to §9's zero-weight default is required for the rewording. Severity: LOW.

Confidence: **high**.

FINAL: sentence reword; test 9 rule needs classes; confidence medium
