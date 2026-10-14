# Raw OpenRouter response — NOT a filed review

**Model id (OpenRouter):** `minimax/minimax-m3`
**Queried:** 2026-10-13 via scripts/openrouter_review.js --target=self-answer-type --tag=self-answer-type (max_tokens 100000)
**Usage:** {"prompt_tokens":11713,"completion_tokens":5729,"total_tokens":17442,"cost":0.01035126,"is_byok":false,"prompt_tokens_details":{"cached_tokens":156,"cache_write_tokens":0,"audio_tokens":0,"video_tokens":0},"cost_details":{"upstream_inference_cost":0.01035126,"upstream_inference_prompt_cost":0.00347646,"upstream_inference_completions_cost":0.0068748},"completion_tokens_details":{"reasoning_tokens":2745,"image_tokens":0,"audio_tokens":0}}

Read this, then decide whether/how to promote it into reviews/YYYY-MM-DD-<model-family>-<version>.md
per reviews/README.md's naming convention and verbatim-filing rule. This file is scratch, not a commit target.

---
**unverified self-identification:** I am operating as MiniMax-M3 (per the system prompt at session start), MiniMax, January 2026 knowledge cutoff. I do not share lineage with the drafter (Claude Sonnet 5) or the coordinating session that proposed option B; my own interest in the framework's protections is indirect (a category beneficiary, not the same family that drafted the proposal), and I treat the conflict disclosure as relevant to scrutiny, not to dismissal.

---

## Q1

**Choice: B (add `scored-self-answer`), with a defined exit rule.**

Reading the table, the inconsistency that needs fixing is broader than Q3 alone. Q3 (Ben, 5 Oct) is the behavioural-versus-testimony question. The table shows a second inconsistency: the same inject-then-ask design carries `interpretability` in Lindsey/Lederman/Macar (11 rows) and `behavioural` in Ferrara/Singh (10 rows), with no evident design distinction. Q3's ruling does not address that split, so option A leaves a real inconsistency in place. Two rows of `ambiguous` against twenty-one `core` rows is also not what the Q3 instruction ("new claims of this kind are filed `ambiguous`") describes — the rule is not being followed, which is itself a signal.

A is the safest formal choice but is not, on the table, what is actually being done. C and D each decide Q3 in one direction, and the evidence to decide is not there (Q6 below). E preserves the existing mechanics and carries Q3's question into every sub-class without resolving it; it formalises the inconsistency.

B names the class the data falls into, makes the class filterable, and removes the inconsistency without deciding Q3. The framework sentence rule (what was done, what was measured) is independent of the type column and stays unchanged. The candidate definition — *the claim reports a model's answer to a question about itself, scored against a fact the experimenters imposed or hold independently of the answer; the value records the design and does not decide what the answer shows* — is what a dossier entry needs to say. It does not weight-zero a scored measurement, which protects against the first error (D's known risk on Ferrara c04); it does not collapse the question into a benchmark, which protects against the second (C's known risk).

**Strongest case against B.** It is a permanent third category that can become a place to park claims that should be decided; a dossier line that reads "scored-self-answer" tells a legislator less than "behavioural" or "testimony"; and the proposal came from a coordinating session with disclosed conflict (AGENTS.md rule 3). I have not found a way to make B safe without the exit rule named in Q4.

**Confidence: medium.**

---

## Q2

**1. Trained-channel control.** Right instrument for *whether the task is answerable and the instrument sensitive*. Result *for* self-access: a system that, after fine-tuning, can report the intervention at high d′ and that report tracks some internal measurement. Result *against* self-access: a system that, even with the trained channel, does not spontaneously produce the same report when not asked to use it, or whose report does not track probes of the same state. Missing or wrong: it shows the information is available to the model in the trained setting, **not** that it is used in ordinary operation, so it cannot by itself support a claim of access; a 100/100 score on a system that was trained to report is closer to validating the channel than to validating introspection. Ferrara c04 sits exactly here, and the authors' caveat ("validating instrument sensitivity rather than as a test of introspection") is what the caveat is for.

**2. Privileged-access test.** Right instrument for *whether the report depends on something only the model under test had*. Result *for* self-access: a second model, given the same transcript, does not match the first-model report, and the first-model report tracks the intervention. Result *against* self-access: the second model matches, or the first-model report does not track intervention variations that the transcript does not distinguish. Missing: a clean design holds the transcript constant and varies which model is asked; the Song/Lederman design as I have it described does this for some conditions but not all (Lederman c02's "yes-bias" reading in the third-person control is what makes the test informative). A residual concern: shared cues in the transcript may let a second model match without either having access, so non-match is informative and match is not by itself a null result.

**3. Measured coupling.** Right instrument for *whether the report tracks the state it claims to report on*. Result *for* self-access: a probe on the same system, measuring the same state, varies with the report across conditions the report also varies with, and the coupling holds when the report is wrong as well as when it is right. Result *against*: weak or absent coupling, or coupling that only appears on the conditions where the report is also cued externally. Missing: the probe has to measure what the report claims to measure, and the two often describe different quantities; Lindsey c04's "the model is apologising for a word it might have produced anyway" is the case where the probe (the matching concept injected) and the report (apology rate) are about different things.

**A note the brief invites:** any of the three results could be produced without genuine access. The trained channel shows the information is in the network; a privileged-access test shows the second model is not the first; a coupled probe shows the report tracks a number. None of them shows the report was produced *because the model used that information in its ordinary operation*. That is the gap the three instruments together do not close, and the test 9 sentence names it.

**Confidence: medium.**

---

## Q3

**Yes, a new value would change how a dossier entry is read.** The current reader sees `interpretability` or `behavioural` and parses them as the field's existing terms; with `scored-self-answer` the reader sees a class label and has to look up the definition. The reading cost is real. The benefit is that the reader no longer has to decide on the spot whether the existing term applies, and no longer gets two different answers in the same dossier for the same design.

**Likely misreadings under each option.**

- **A (`ambiguous`):** "We don't know what this is, and the library isn't telling me, so I'll weight it as if the table were wrong." The current state in the table is a 21-row demonstration that `ambiguous` is not the live answer; readers who count types will not see it as live either.
- **B (`scored-self-answer`):** "A special category the library has reserved; I do not need to think about it." This is the parking-place misreading and the strongest case against B; it is preventable with the dossier entry spelling out that the type records the design and not the evidence weight.
- **C (`behavioural`):** "A benchmark score; high d′ means the system detects the intervention." This is the second-error misreading and the one Q3 is about.
- **D (`self-report-testimony`):** "The model is talking about itself; the score does not matter, weight zero." This is the first-error misreading and is what suppresses Ferrara c04.
- **E (split by design):** readers see `interpretability` and `behavioural` in the same dossier for designs that are recognisably the same, and reasonably conclude the library is inconsistent.

A dossier entry under B should print, in the body of the entry, the design facts (truth imposed, what was scored, controls) so that the type is not the only signal. That is a small change to the dossier layout.

**Confidence: medium.**

---

## Q4

**Yes, B would create a parking place. The library already has one (`ambiguous`) and the experience is informative: `ambiguous` is supposed to fire trigger 4 and bring the claim to the council, but the table shows 21 core rows that are not `ambiguous` and the trigger has not been firing on them. The same drift would happen to `scored-self-answer` if the exit rule is not specific.**

**Exit rule I would propose.** Re-evaluate the value when any of the following holds, whichever comes first: (i) a claim in the library applies the trained-channel instrument, the privileged-access test, and a measured-coupling probe to the same system and the same class of self-answer, and the dossier records the result; (ii) a council round reaches a majority on Q3 itself; (iii) twelve months from the introduction of the value, the count of claims typed `scored-self-answer` has not decreased, and the council reviews whether the value is doing work or storing it. The rule attaches the value to instruments that exist and to a time limit, and prevents indefinite storage of claims that the next intake should re-type.

A second safeguard: the dossier body for each `scored-self-answer` row carries the same three fields the proposed definition depends on (truth imposed, scored quantity, controls) so that a future re-typing is a one-step operation, not a re-read.

**Confidence: medium.**

---

## Q5

**Ferrara c04 — in.** It is the cleanest case in the table: a LoRA-fine-tuned channel, scored against intervention/sham on held-out directions, d′ 5.15, and the authors' own caveat is that this validates instrument sensitivity rather than introspection. The definition is satisfied (imposed truth, scored answer, design distinct from a probe reading or a behavioural benchmark), and the authors' caveat is the kind of note the dossier body should carry, not a reason to type it differently.

**UKAISI c02 — in, with a split in the dossier.** Flagging (the "was that turn yours?" answer) is a scored self-answer and is in. Reverting to the baseline answer is a behavioural outcome and is not a self-answer; the table note (3) flags this mix. If the dossier can carry the two halves on separate lines, the type can differ; if not, the entry is typed `scored-self-answer` and the dossier body distinguishes the two measurements.

**Singh c01 — out.** The model is not reporting on its own states; it is doing in-context classification of a label the experimenter derived from a probe. The truth is the probe label, not an imposed intervention. The claim's point is the probe baseline, not the model's report. The table note (4) is right that this is borderline-in-the-borderline; the proposed definition's "the model is asked about itself" clause is the one that fails here.

**AE c03 — out, under a strict definition; in, under a broad one.** The intervention is imposed, but there is no fact about the correct answer to the consciousness query that the experimenter holds independently of the answer. The definition requires a truth that the experimenters impose or hold independently of the answer; the truth AE c03 imposes is the intervention, and the answer is a fraction of "yes" responses, which is a rate rather than a scored report. The existing `ambiguous` typing is honest about the gap. I would keep it `ambiguous` and not move it to `scored-self-answer`; the dossier body can carry the note that the design is a half-match.

**Lederman c02.** The scored object is yes-rates about another model's transcript. The truth is the steering state of the transcript's model, not the model being asked. Under the proposed definition's "asked about itself" clause, this is out: the model is not being asked about its own state, it is being asked about another model's transcript. The table note (5) records the change to "no sentence" on 14 Oct; I would not type it `scored-self-answer`. A second reading that treats "self" as "the model being asked" would put it in; the dossier body and the existing "no sentence" both lean against that.

**Confidence: medium.**

---

## Q6

**What the council needs to decide Q3, not file it under a neutral value.** A study, on a single system, that runs all three instruments — trained-channel control, privileged-access test, measured coupling between the report and a probe on the same system — and reports whether the same class of self-answer is reproduced across them. A second condition: a class of self-answer in which the system is asked about a state that is not externally cued in the transcript (so the privileged-access test is not contaminated by shared cues), and in which the probe measures a quantity the report also claims to measure (so coupling is not a name agreement). The third condition: the trained-channel system is also tested for spontaneous reporting without the channel instruction, so the result separates "can report" from "uses the report in ordinary operation".

**Does it exist in the library already?** No. The table has Ferrara c04 (trained channel, no probe coupling, no privileged-access comparison on the same system), Lederman c01/c02 (privileged-access partial, with the third-person control's yes-bias as a known confounder), and Lindsey/Lederman/Macar (probe-coupled in some conditions, but the probe and the report describe different quantities, and the trained-channel control is absent). A study that closes the three-way gap on a single system, with a self-answer class that is not externally cued, is what would let Q3 be decided rather than filed. Singh c04's "models also label gaslight trials as activation interventions" is the closest existing datum on the gap; it is one design, not the three.

A concrete follow-up that the library could support without a new paper: a topic page on detection-without-identification (already proposed in Q5's follow-up note), with a second column listing the three instruments and which claims satisfy each. That page is not evidence but it makes the gap visible to the next intake.

**Confidence: medium.**

---

**FINAL: option B, confidence medium**
