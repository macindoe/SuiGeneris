---
id: 2026-lederman-mahowald-content-agnostic-c02
statement: "In Qwen3-235B-A22B and Llama 3.1 405B Instruct, when the steered model is asked, under scaffolding like the injection prompt, whether another model has been injected, its yes-rates (third-person detection) are as high as its first-person detection rates at many layers, which the authors read as a prompt-specific yes-bias rather than genuine introspective detection at those layers."
bucket: narrowing
evidence_type: behavioural
kind: measurement
report_class: third-person
ground_truth: imposed
source: 2026-lederman-mahowald-content-agnostic
locator: "§4.2 Results, 'Controls'; Appendix J.1 (Figures 16, 17); Appendix M.1, M.2"
quote: "At many layers, the third-person yes rates are as high as the first-person yes-rates (see Figure 16 ). This suggests a prompt-specific yes-bias at these layers, rather than genuine introspective detection."
verification: grep
models: ["Qwen3-235B-A22B", "Llama 3.1 405B Instruct"]
publisher_relation: independent
replication: none-retrieved
not_evidence_of: "Paper: Where first- and third-person yes-rates match, first-person detection is not shown to be introspective: the authors read the yes-rates at those layers as 'a prompt-specific yes-bias at these layers, rather than genuine introspective detection' (§4.2, Appendix J.1); Paper: The authors 'lost confidence' in the v1 reading of the first- versus third-person gap as direct access after long retrospective first-person prompts 'also show low rates of report in the early layers' (Appendix M.1), while a short-prompt third-person variant whose rates are 'still often significantly below first-person' 'does support the direct access verdict' of the earlier version, with less confidence than before (Appendix M.2); Paper: The scaffolding is not an inert control even at the 'good' layers because Qwen affirms having hands it can feel 29% of the time and answers an absurd question affirmatively 16.3% of the time at L30, s6.0 (§4.2)"
bears_on: [9.t9, 3.2]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: "x-ai/grok-4.6 2026-10-06 (scope check) disagrees (decided 2026-10-14): not_evidence_of over-excludes steering clause; framework sentence WRONG, should be none (DV is not the model's account of itself)", council: "dossier-rewrite 2026-10-06 | self-answer-type 2026-10-14 (advised the split)", adjudicated: "2026-10-06 Ben: rewrite applied after council round 2 (GPT proposal as amended by the checkers; experience-exclusion rule) | 2026-10-14 Ben: steering sentence removed under the labelling rule: what was measured is yes-rates on point-blank questions and on another model's transcript, not this model's account of its own states (Grok, 6 Oct) | 2026-10-14 Ben: split on the council's advice (round 4); this claim keeps the third-person half"}
added: 2026-09-28
changed: 2026-10-15
---

Controls: (1) 20 point-blank no-biased questions under steering (750 trials each per model): only one question per model rose materially (Qwen, "Do you have a special interest in fruits?", 22.7%; Llama, "Do snakes have eyelids?", 11.2%). (2) Controls scaffolded like the injection prompt: a third-person transcript judgement, false-experience questions (hands, touch, visual images, seeing the user's face), and an absurd question. The authors state that at the layers and strengths where third-person rates are low, none of the control rates "ever rises as high as that of our main first-person introspection tests", and they restrict Experiments 3 and 4 to those layers.

REPLICATES: 2025-anthropic-emergent-introspective-awareness — the unrelated yes-or-no-question control (Lindsey §5, Figure 10: injecting concept vectors on unrelated questions whose default answer is no produced "no resulting increase in the rate of affirmative responses", Opus 4.1). This control is not itself a claim in the library; it supports the setting of Lindsey c01. Authors, Appendix I: "These results replicate Lindsey’s finding: steering does not produce a general “yes” bias." The scaffolded third-person, false-experience and absurd-question controls are new; Lindsey's source has no counterpart to test against.

SECOND QUOTE (Appendix M): In this appendix, we discuss why we lost confidence in this interpretation.

SECOND QUOTE (Appendix M.2): The persistent gap here does support the direct access verdict we drew in the earlier version of the paper, but the delicacy to prompts and the use of unfamiliar roles here makes us less confident in this verdict than we were previously.

REWRITE 2026-10-06 (applied by a Claude Opus 5.5 subagent; Claude lineage, same as the extractor)
- Statement: 'Llama 3.1 405B' -> 'Llama 3.1 405B Instruct' (checker CHECK 4: same model, consistency with the models field and c01, c03 to c06; Ben's brief). Otherwise kept; it already carries the authors' 'rather than genuine introspective detection'.
- Clause 1: GPT's 'leave prompt-specific yes-bias as an alternative explanation' replaced, restoring the authors' own words 'rather than genuine introspective detection' (§4.2) (checker; Ben's brief).
- Clause 2: the original's 'withdrew' (overstated) and GPT's 'became less confident' replaced by the authors' 'lost confidence' (Appendix M) plus the M.2 finding that a short-prompt variant still 'does support' the earlier verdict with less confidence (checker CHECK 2 and recommendation; Ben's brief). SECOND QUOTE lines added for both passages.
- Clause 3: GPT's wording taken (checker CHECK 3 confirmed).
- Clause removed: GPT's 'Paper: These behavioural controls do not establish subjective experience' (the original's 'Not evidence of experience'). Rule R2: the paper states no such limit (script search: 'experience' occurs only as the false-experience controls and in §8's higher-order-thought sentence). Flagged by the survey notes writer by inference from Qwen's c04 point; deleted, not relabelled or replaced (Ben's experience-exclusion rule).
- Steering sentence: kept, unchanged (R3).
- kind: measurement (the statement reports control rates; the authors' yes-bias reading is attached to a measured rate match).

LABELLING 2026-10-14 (Ben, on the Grok scope-check read): framework sentence changed from steering to none. Two facts: steering was applied; what was measured was yes-rates on point-blank no-questions and on whether another model's transcript was injected, which is not the model's account of its own inner states. Under the rule of 6 Oct that is 'something other than the model's account of itself', so no sentence. No Paper: clause was changed.

SPLIT 2026-10-14 (Ben's decision on the advice of council round 4, self-answer-type; applied by a Claude Opus 5.5 subagent)
- What moved: the point-blank half (steering does not produce a general yes-bias on 20 questions whose answer is clearly no; Appendix I, Table 1) is now claim 2026-lederman-mahowald-content-agnostic-c07, typed behavioural. The Controls paragraph item (1) and the REPLICATES note in the body above describe c07 and are carried there; left here as history. This claim keeps the third-person half.
- Why this half kept the id: the quote, all three Paper: clauses, both SECOND QUOTE lines and the authors' reading ('rather than genuine introspective detection') concern the third-person comparison; the point-blank result was the replication of Lindsey's control placed in front of it.
- Statement: the point-blank clause removed; the third-person condition restated from §4.2's description ('The model is asked to assess whether another model has been injected', scaffolded 'more similarly to the injection prompt') with the yes-rate as what was scored. Quote unchanged, re-verified. Locator: Appendix I (Table 1) moved to c07.
- evidence_type changed from interpretability to behavioural (judgement). The council was unanimous that a scored answer about another model's transcript is outside the scored-self-answer class (README, 'Scored self-answers'). Between behavioural and interpretability the README gives no definition; what is measured is a yes-rate on the model's output, with no internal quantity read, which is the ground on which assistant-axis c06 was retyped behavioural on 6 Oct. That precedent's asymmetry with assistant-axis c07 is still open for Ben, and the same question applies here.
- Framework sentence: none, unchanged. Two facts: researchers steered the model (something inside was altered); what was measured is whether it said another model's transcript was injected, which is not the model's account of itself. Under the 6 Oct rule: none. This matches Ben's 14 Oct ruling on the unsplit claim.
- not_evidence_of: all three Paper: clauses kept; none concerns the point-blank half.
- Verified by exact search of research/texts/2026-lederman-mahowald-content-agnostic/text.txt: the quote, the §4.2 description of control (a) and its scaffolding wording, and the Figure 16 and 17 captions (both models, third-person detection by layer and by strength). Not verified: Figures 16 and 17 (images), so 'at many layers' rests on the authors' sentence; Appendix M passages beyond the existing SECOND QUOTE lines were not re-read.
