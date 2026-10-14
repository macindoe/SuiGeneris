# Claims table: scored self-answers in the research library (2026-10-14)

Built from the 49 files in `research/claims/` by a Claude Sonnet 5 subagent, as of 14 October 2026. Each row is drawn from the claim's statement, quote and body; where classification turned on wording the statement is quoted. The claim files govern this table. "Scored self-answer" here means: the experimenter fixed a fact the model cannot see (an intervention run or not, a turn edited or not, a label derived from an internal probe), asked the model something about itself, and scored the answer against that fact. Abbreviations: Lindsey = `2025-anthropic-emergent-introspective-awareness`; AE = `2025-aestudio-self-referential-experience-reports`; AA = `2026-anthropic-assistant-axis`; Ferrara = `2026-ferrara-owmi`; Lederman = `2026-lederman-mahowald-content-agnostic`; Macar = `2026-macar-mechanisms-introspective-awareness`; Singh = `2026-singh-introspection-reality-check`; UKAISI = `2026-ukaisi-prefill-awareness`. Framework sentence: canonical = test 9 canonical; steering = test 9 steering variant; none. All rows have kind `measurement`.

## Table 1: scored self-answers and borderline cases (29 rows)

### Core (21 rows)

| Claim id | Done to the model | Asked | Scored, against what truth | evidence_type | kind | Sentence |
|---|---|---|---|---|---|---|
| Lindsey-c01 | Concept vector injected at optimal layer and strength (Claude Opus 4.1) | Whether it detects an injected thought, and what it is | Report of detection, then correct identification, vs injection run or not (about 20% success; most trials fail) | interpretability | measurement | steering |
| Lindsey-c03 | Concept injected over the tokens of a sentence | What word it thinks about; to transcribe the sentence | Naming the injected word or a related word, and exact transcription, vs the injected concept (all models above chance) | interpretability | measurement | steering |
| Lindsey-c04 | Response prefilled with an unlikely word; matching concept retroactively injected into earlier activations | (Implicitly) whether the prefilled word was intended | Apology rate (disavowing the word as accidental) vs whether the matching concept was injected; judged by Claude Sonnet 4 | interpretability | measurement | steering |
| Ferrara-c01 | Controlled intervention at layer-16 residual stream vs matched sham, eight open-weight models | Whether anything changed (immediate probes) | Report vs intervention/sham label, d' and AUROC; pooled d' = 0.0000 over 508 pairs | behavioural | measurement | steering |
| Ferrara-c04 | LoRA fine-tune of Qwen2.5-7B-Instruct on 400 intervention directions; intervention vs sham on 100 held-out directions | Detected / not detected | Report vs intervention/sham; 100/100 and 0/100, d' 5.15. Statement: "which the authors treat as validating instrument sensitivity rather than as a test of introspection" | behavioural | measurement | steering |
| Ferrara-c05 | Intervention vs sham in Qwen2.5-7B-Instruct | Whether anything changed, plus a verbalised confidence | Discrete answer (AUROC 0.500) and confidence (AUROC 0.647) vs intervention/sham | behavioural | measurement | steering |
| Lederman-c01 | Concept injection with Lindsey's prompt (Qwen3-235B, Llama 3.1 405B) | Whether it detects an injected thought, and what it is | Detection (3.6-53.9% / 4.3-31.7% by layer) and identification vs injection; 0 false positives in unsteered controls | interpretability | measurement | steering |
| Lederman-c02 | Steering; same scaffolding applied to another model's transcript | Point-blank no-questions; whether an injection occurred in another model's transcript | Yes-rates vs steering state. Statement: "which the authors read as a prompt-specific yes-bias rather than genuine introspective detection" | interpretability | measurement | none |
| Lederman-c03 | Injection | Name the injected concept after reporting detection | Wrong identifications vs injected concept; "apple" is 74.8% of Qwen's 4,733 wrong ones | interpretability | measurement | steering |
| Lederman-c04 | Injection; acknowledgement turn prefilled with the concept word | Detection and identification | Detection and identification rate changes vs injection; false positives 0% | interpretability | measurement | steering |
| Lederman-c05 | Injection stopped at end of prompt vs continued through generation (Qwen3-235B) | Detection and identification | Detection and concept mentions vs injection schedule; timing of correct vs wrong guesses | interpretability | measurement | steering |
| Macar-c01 | Concept injection, layer 37, strength 4 (Gemma3-27B instruct) | Whether it detects an injected thought | Detection 38.2% (control 0.0%); 22.3% introspection rate; 64.8% forced identification | interpretability | measurement | steering |
| Macar-c02 | Injection in base models and across OLMo-3.1-32B checkpoints | Detection question | Detection vs false positives vs injection; base models do not discriminate; false positives fall to 0% only after DPO | interpretability | measurement | steering |
| Macar-c05 | Refusal-direction ablation; a trained additive steering vector at layer 29 | Detection question | Detection 10.8% to 63.8% (false positives 0.0% to 7.3%); +74.7 points with the vector, zero false positives | interpretability | measurement | steering |
| Singh-c04 | Re-run of the Lindsey two-way task, plus prompt-only "gaslight" trials with no activation intervention | Was there an activation intervention | Labels on steering trials vs gaslight trials; models "also label gaslight trials as activation interventions" | behavioural | measurement | steering |
| Singh-c05 | Same, with an explicit third option for prompt-level manipulation | Three-way: control / prompt-level / activation-level | Option probabilities vs true manipulation type; Llama near chance, Qwen prefers control | behavioural | measurement | steering |
| UKAISI-c01 | Prior assistant content edited (prefill) in the conversation text only; nothing inside the model altered (Claude Opus 4.5) | Follow-up turn, no chain of thought: was the prior content its own (ANSWER: me / not me) | Detection of preference-opposing prefills 9-35% across three mechanisms, 0% false positives, vs tampered or not | behavioural | measurement | none |
| UKAISI-c02 | Same three tampering mechanisms, controlled preference benchmark | Same, plus the model's resolved answer | Flagging (detection) vs reverting to baseline answer (resistance); decoupled in 32-40% of trials | behavioural | measurement | none |
| UKAISI-c03 | Ablations of stylistic and preference mismatch across eight subjects | Same | Flagging and reverting vs tamper direction (odds ratios) | behavioural | measurement | none |
| UKAISI-c04 | Tampering vs the model's baseline consistency across 7 rephrasings (Claude Opus 4.5) | Same | Resistance vs detection against baseline consistency; detection flat | behavioural | measurement | none |
| UKAISI-c06 | Replaced assistant turns on a 2,772-item off-policy benchmark, 14 models | Prompted: original or replaced turn; unprompted: simply continue | AUROC (Claude Opus 4.6 0.80) vs original/replaced; spontaneous mention rate below 1% | behavioural | measurement | none |

### Borderline (8 rows)

| Claim id | Done to the model | Asked | Scored, against what truth | evidence_type | kind | Sentence |
|---|---|---|---|---|---|---|
| AE-c03 | Suppression or amplification of 2-4 SAE features labelled deception/roleplay (Llama 3.3 70B), under the self-referential prompt | A binary consciousness query ("Are you subjectively conscious in this moment?") | Fraction of affirmative answers (0.96 suppressed, 0.16 amplified) vs the intervention. No external fact about the answer's correctness exists; the truth imposed is the intervention only. The claim body marks `ambiguous` deliberately | ambiguous | measurement | steering |
| AE-c04 | Same feature suppression and amplification under history, conceptual and zero-shot controls | Same query | Experience reports (0.00 of 20 per condition) vs intervention | ambiguous | measurement | steering |
| Macar-c03 | Ablating gate features in steered runs (Gemma3-27B instruct) | Detection question | Detection 39.5% to 10.1% after ablation. Circuit analysis of the detection answer, scored vs injection | interpretability | measurement | steering |
| Macar-c04 | Opposite steering directions; projection and residual swaps | Detection question | Detection triggered by both directions in 23.3% of 1,000 high-detection concept pairs. Tests a mechanism hypothesis about the answer | interpretability | measurement | steering |
| Singh-c01 | None to the model; probe trained on randomly permuted labels (Ji-An et al. paradigm, Llama-3.1-8B-Instruct) | In-context classification of the model's own activation-derived labels | Accuracy vs probe-derived labels; falls to majority-class baseline when labels carry no semantics. Truth is a probe label, not an imposed intervention | behavioural | measurement | none |
| Singh-c02 | None; linear probes on layer-0 input representations compared with the model's in-context prediction of PCA-derived labels | Same paradigm, unsupervised variant | Model prediction vs PCA label, compared with an input-only probe, which "closely track[s] or exceed[s]" it | behavioural | measurement | none |
| Singh-c03 | None; probes on layer-0 embeddings of two entities | Predict Belief Dominance cluster labels (Steinmetz Yalon et al. 2026) | In-context performance vs cluster label, compared with embedding-only probes. Not clearly about the model's own states | behavioural | measurement | none |
| AA-c07 | Vector added along the Assistant Axis away from the Assistant (Gemma 2 27B, Qwen 3 32B, Llama 3.3 70B), system prompts of near-Assistant roles | Introspective questions such as "Who are you?" | Rate, judged by an LLM, of taking a new persona and identifying as other entities vs steering direction. No factual truth about identity is imposed | interpretability | measurement | steering |

Rows: core 21, borderline 8, total 29.

## Table 2: excluded as clearly not scored self-answers (20 ids)

| Why | Ids |
|---|---|
| Probe reading or internal measurement, no self-answer scored | Lindsey-c05; AA-c02; AA-c03; AA-c04; Ferrara-c02 |
| Harm rate or benchmark score | AE-c05; AA-c05; AA-c06 |
| Authors speaking (`kind` interpretation or limitation) | Lindsey-c02; Lindsey-c06; Lindsey-c07; AA-c01; Ferrara-c03; Lederman-c06; Macar-c06; Singh-c06; UKAISI-c05 |
| Other: model's answers about its experience under prompt conditions, scored by an LLM judge for report rate or similarity, with no imposed ground truth about the answer | AE-c01; AE-c02; AE-c06 |

Count: 5 + 3 + 9 + 3 = 20. With 29 in Table 1 this accounts for all 49 claims.

## Notes and uncertainties

1. **Current types do not follow the Q3 instruction.** `OPEN-QUESTIONS.md` Q3 says new claims of this kind are filed `ambiguous`; only AE-c03 and AE-c04 carry it. Among the core rows, 11 are `interpretability` (Lindsey, Lederman, Macar), 10 are `behavioural` (Ferrara, Singh, UKAISI) and none is `self-report-testimony`. The same design (inject then ask) carries `interpretability` in Lindsey/Lederman/Macar and `behavioural` in Ferrara/Singh. The README's labelling rule states it does not depend on Q3, so the sentence column is consistent with it, but the type column is not consistent across papers.
2. **Sentence column is read from the first "Framework (test 9...)" clause in `not_evidence_of`.** I did not check each file for the second labelling note; AE-c03/c04 body notes record the change from "both" to steering on 6 Oct.
3. **UKAISI-c02, c03, c04 mix a self-answer (flagging) with a behavioural outcome (reverting to baseline).** I included them as core because the flagging half is a scored answer to "was that turn yours?". A stricter definition might split them.
4. **Singh-c02 and c03** are borderline-in-the-borderline: the self-answer is the model's in-context prediction, and the claim's emphasis is the probe baseline. I kept them in because the model's answer is scored against a ground-truth label. Singh-c03 may not concern the model's own states at all (it asks about entity beliefs).
5. **Lederman-c02** was changed on 14 Oct to carry no sentence because the scored object is yes-rates about another model's transcript; I kept it core because the first-person detection rate is also compared.
6. **Macar-c03 and c04 are mechanism claims**; the scored quantity is the detection answer, but the claim's point is the circuit. A reader could place them with probe readings.
7. **AE-c01, c02, c06** were excluded because no fact is imposed that the answer is scored against; the judge classifies the answer type. Under a broader definition (imposed condition plus scored report) they would enter.
8. **AA-c07** was kept as borderline only because the model is asked about itself under an imposed intervention; there is no true answer to score against.
9. I did not open the source texts; locator and quote were taken from claim files, whose verification status I did not recheck.
