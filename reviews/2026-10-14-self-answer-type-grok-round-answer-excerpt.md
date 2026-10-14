# Your own answer in the round (verbatim; self-identification line removed)

## Q1
Option **B**. Table 1’s 21 core rows are one design class (hidden or independently held fact; question about the model; answer scored against that fact) and are typed 11 `interpretability` / 10 `behavioural` / 0 `self-report-testimony` / 0 `ambiguous`. The split tracks paper culture, not Q3: inject-then-ask is `interpretability` in Lindsey/Lederman/Macar and `behavioural` in Ferrara/Singh. Note 1: Q3’s filing rule is already not applied.

C and D each answer Q3 without the instruments. **D** is error 1: it zero-weights replicable scores, including Ferrara-c04 (100/100 vs sham, d′ 5.15; authors: instrument check, not introspection) and UKAISI-c06 (AUROC 0.80). **C** is error 2: “like any benchmark” invites reading Lindsey-c01 (~20% detection, most trials fail) or Lederman-c01 (wide by-layer spread, 0% unsteered FP) as access. **A** leaves the table inconsistent, or recodes ~19 measurements to a trigger value also used for a methods caveat (UKAISI-c05), which in a dossier reads as “the library cannot type this finding.” **E** copies the sentence-rule cut into `evidence_type` and still leaves Q3 inside every subclass.

B names the class, makes it filterable, and states that the value records design, not what the answer shows. The 6 Oct sentence rule is unchanged.

Strongest case against B: new enum is a schema decision; it can park; “scored-self-answer” tells a legislator less than `behavioural` or `interpretability`; the proposal is the coordinating session’s and is conflicted.

Severity: **HIGH**. **Argument against:** a third category becomes a place to park claims that should be decided, and this is the conflicted coordinating-session proposal.

Confidence: medium

## Q2
They are the right *separation* tests for self-access vs a scored channel. They are not tests of experience. Missing: Singh-style prompt-only gaslight on the same items; a yoked control where the hidden fact is in the activations under both “self” and “other” framings; per-class coupling (Q4: provenance ID does not transfer); a negative control the model has no channel for.

1. **Trained-channel.** For access: does not count; Ferrara-c04 is correctly “not a test of introspection.” Against ordinary access: untrained report at chance while the trained channel is perfect (Ferrara-c01 d′ = 0.0000 vs c04 d′ 5.15). Without access: yes — training can write a readout of an available bit. Shows availability under fine-tune, not use in ordinary operation.

2. **Privileged-access.** For: first-person score tracks the hidden fact; a second model with the same text does not. Against: third-person matches first-person (Lederman-c02: prompt-specific yes-bias). Without access: yes — Lederman-c02 is not matched activations; the reader never had the injection, so a first-person edge is expected from input physics alone. A clean test needs the same residual evidence, different attribution framing.

3. **Measured coupling.** For: report covaries with a probe of the same state, not with the prompt. Against: report and probe dissociate, or both follow the prompt (Singh-c04: gaslight labelled as activation intervention). Without access: yes — a trained or incidental readout of the probed features is coupling without “access” in the test-9 sense. The test-9 sentence asks for this measurement; it still would not license inner-state claims.

Confidence: medium

## Q3
Yes. Dossiers print `evidence_type` on every entry. A new value is what the legislator sees unless the how-to-read blurb says it records design only.

- **A:** “ambiguous” → the measurement is unreliable or the paper is confused, not “typing rule undecided.”
- **B:** “scored-self-answer” → either a passed self-knowledge test (score = access) or a quiz to ignore. Mitigation: one dossier sentence that the type does not decide Q3.
- **C:** “behavioural” → benchmark capability; Lindsey-c01 / Macar-c01 detection rates read as introspection.
- **D:** “self-report-testimony” → skip; Ferrara-c04 and UKAISI detection AUROCs vanish.
- **E:** same design, different words across papers (status quo); Lindsey vs Ferrara look like different kinds of evidence.

Severity: **MEDIUM**.

Confidence: medium

## Q4
Yes. Exit rule: (i) `kind: interpretation` / `limitation` and unscored experience reports (AE-c01, c02, c06) cannot take the value; (ii) a row that fails the definition is retyped by method and leaves; (iii) when any of the three instruments exists in-library *for that report class*, Ben decides Q3 for that class (C or D, or a stated hybrid) and recodes — the holding type is not a third ontology; (iv) a decision to leave Q3 open still counts as adjudication (existing crossing rule) but cannot add new subclasses to the holding type. Topic page + OPEN-QUESTIONS Q3 remain the visibility mechanism, not an eternal enum.

Severity: **MEDIUM**.

Confidence: medium

## Q5
Definition used: model’s answer to a question about itself, scored against a fact imposed or held independently of the answer.

- **Ferrara-c04:** **in.** Detected/not vs intervention/sham is the design. Authors’ “not introspection” belongs in the statement / `not_evidence_of`, which B is built to carry.
- **UKAISI-c02:** **split.** Flagging (me / not me vs tamper) **in**; reverting to baseline **out** (`behavioural`). Matches the 6 Oct split rule for two measurements.
- **Singh-c01:** **in** (narrow). Probe-derived labels are an independent truth; the ask is in-context classification of the model’s own activation labels. Not an imposed intervention. Keep `none` sentence.
- **AE-c03:** **out.** Intervention is imposed; there is no external correct answer to the consciousness query. Stay `ambiguous` (or method-type the report-rate shift); do not treat as a scored self-answer.
- **Lederman-c02:** **out** of this class. The scored object is yes-rates about *another* model’s transcript; authors read prompt yes-bias. If first-person rates are in the same file, split; the other-transcript half is not a self-answer. Sentence already `none` — keep.

Confidence: medium

## Q6
Do not advise deciding Q3 until one report class has, on the same system: untrained report vs sham; a trained-channel ceiling; gaslight/prompt-only trials; a third-person or yoked-transcript control with matched evidence where possible; and a probe of the hidden state scored against the report. That assembled study is **not** in the library. Nearest pieces: Ferrara-c01+c04 (channel off/on), Singh-c04/c05 (gaslight / three-way), Lederman-c02 (other-transcript, imperfect control), Macar-c03 (circuit of the detection answer, not report–probe coupling). Q1’s coupling scan is still unanswered. Until then file under a neutral design value (B), not C or D.

Severity: **MEDIUM**.

Confidence: medium

FINAL: option B, confidence medium
