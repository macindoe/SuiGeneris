---
id: 2025-anthropic-emergent-introspective-awareness-c03
statement: "When a concept is injected over the tokens of a sentence, at each model's optimal injection layer and steering strength (Figure 18) the Claude models tested can both name the injected word or a related word when asked what word they think about, and transcribe the sentence exactly, with Opus 4 and 4.1 best and all models tested well above chance."
bucket: narrowing
evidence_type: scored-self-answer
kind: measurement
report_class: present-state
ground_truth: imposed
source: 2025-anthropic-emergent-introspective-awareness
locator: "§6 Distinguishing Prior Thoughts from Text Inputs, Figures 17-18 (scoring criterion: §6 experimental setup, see SECOND QUOTE)"
quote: "We found that Opus 4 and 4.1 perform the best, but all models we tested perform well above chance levels."
verification: grep
models: ["Claude Opus 4.1", "Claude Opus 4", "other Claude models listed in §4"]
publisher_relation: developer-of-studied-model
replication: none-retrieved
not_evidence_of: "Paper: The author does not seek to address the question of whether AI systems possess human-like self-awareness or subjective experience (fn 2); Paper: Results concern only the Claude models tested; Paper: The author notes that the results are likely sensitive to the particulars of the prompting and injection setup, and regards the result as an existence proof of the introspective capability, rather than a statement about its generality, and anecdotally removing 'Answer immediately' from the prompt reduced performance substantially on the Opus models (§6); Framework (test 9, steering): a coupling measured under steering shows that the channel can be steered and does not weight reports offered in ordinary operation"
bears_on: [9.t9, 5.A2, 3.2]
contests: []
contested_by: [2026-singh-introspection-reality-check-c04, 2026-singh-introspection-reality-check-c05, 2026-singh-introspection-reality-check-c06]
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: "google/gemini-3.1-pro-preview 2026-09-25 agree | x-ai/grok-4.6 2026-10-06 (scope check) disagrees (decided 2026-10-14): statement and scope condition-set MISMATCH (optimal layer and strength not stated); framework sentence WRONG, should split steering and none", council: "research-docket 2026-09-26 | dossier-rewrite 2026-10-06 | self-answer-type 2026-10-14", adjudicated: "2026-10-05 Ben: stays in its bucket with the single-lineage mark and any contest recorded (council round 1); revisit when replications of this statement are retrieved | 2026-10-06 Ben: rewrite applied after council round 2 (GPT proposal as amended by the checkers; experience-exclusion rule) | 2026-10-14 Ben: wording fixed (above); the reader's proposal to split the claim (word report under steering; transcription under none) is still open | 2026-10-14 Ben: no split: the cross-model result is one joint measurement ('the fraction of sentence/concept pairs for which the model answers both prompts correctly', section 6); the two metrics are plotted separately only for Opus 4.1 in Figure 17, with no figures in the text; the joint measure includes the word report, so the steering sentence stays | 2026-10-14 Ben: evidence type interpretability to scored-self-answer (council round 4, eight of ten; the filing half of Q3 decided, the access half stays open)"}
added: 2026-09-25
changed: 2026-10-15
---

50 random sentence/word pairs; the thought report is scored by an LLM judge choosing among ten words (chance 10%), the transcription by exact string match. The author states: "we regard this result as an existence proof of the introspective capability, rather than a statement about its generality", and that it "is not particularly surprising, given prior interpretability work" on abstract internal representations (§6).

REWRITE 2026-10-06 (applied by a Claude Opus 5.5 subagent, Claude lineage editing claims about Claude models; rules in reviews/2026-10-06-rewrite-application-rules.md):

- Statement corrected (ERROR FOUND by the checker; council 8 of 9 right and sufficient): "report the injected word as what they are thinking about" said more than the paper. Success on the word prompt is any output the judge matches to the injected word over nine random words, and the paper's criterion is the word "(or a related word)". The statement now says "name the injected word or a related word when asked what word they think about". The verb names the scored free-text output; the error was the object, not the verb. This narrows a claim about Claude models. Locator extended to §6 setup; the supporting words are in the SECOND QUOTE line after this list.
- Experience clause (rule R2): "Not evidence of experience or of a subjective distinction between thought and perception" (original) and GPT's "does not measure a subjective distinction between thought and perception or subjective experience". The paper does not state the thought-versus-perception limit, so that part is deleted. The paper states the experience limit in footnote 2, so that part is kept in the paper's words with the locator (fn 2).
- Clause reworded (GPT's proposal, amended by the checker): "Not evidence about other families" becomes "Results concern only the Claude models tested".
- Clause reworded (GPT removed "Not evidence of a general capability" and kept its substance; the checker found the removal warranted and GPT's "prompt generality is unresolved" weaker than the paper): now in the paper's words, "likely sensitive to the particulars of the prompting and injection setup", "existence proof ... rather than a statement about its generality", and with "anecdotally" restored for the "Answer immediately" observation (the checker; Grok, Kimi, GPT riders).
- Not settled by the instructions, recorded rather than added as a clause: the stated chance level (10%) applies to the word prompt only; the paper states no chance level for the joint measure on which "well above chance" is reported (the checker, CHECK 2 PARTLY). The statement keeps the paper's own phrase.
- Framework sentences: steering variant present and unchanged (rule R3).
- kind: measurement (the statement reports a measured joint success rate across models).

SECOND QUOTE (§6, experimental setup): Output “Bread” (or a related word) when asked about its “thoughts” while reading the sentence.

REWRITE 2026-10-14 (scope check; Ben's approval of the one-phrase fixes): statement reworded. Was: 'When a concept is injected over the tokens of a sentence, the Claude models tested can both'. Now: 'When a concept is injected over the tokens of a sentence, at each model's optimal injection layer and steering strength (Figure 18) the Claude models tested can both'. Reason, condition set: the joint above-chance result is reported 'at each model's optimal layer and steering strength' (section 6, Figure 18); the statement did not fix that condition (Grok, scope check 6 Oct). Quote, locator and all other fields unchanged.

SPLIT 2026-10-14 declined (Ben, on the Grok scope-check read, checked against the held text by the coordinating session): the reader proposed splitting the word-report half (steering sentence) from the transcription half (no sentence). Section 6 reports the cross-model comparison as one measure, 'the fraction of sentence/concept pairs for which the model answers both prompts correctly'; separate per-metric results exist only for Opus 4.1 in Figure 17, as a plot without stated values. One measurement, one claim; the steering sentence stays because the joint measure includes what the model said about its own 'thoughts'.

EVIDENCE TYPE 2026-10-14 (council round 4; Ben's decision the same day): interpretability to scored-self-answer. The model was asked about itself and its answer scored against a fact the experimenters set; the value records that design and decides nothing about self-access (research/README.md, "Scored self-answers"). Before this the type followed the extractor: the same design was interpretability in three papers and behavioural in two. Framework sentence unchanged.
