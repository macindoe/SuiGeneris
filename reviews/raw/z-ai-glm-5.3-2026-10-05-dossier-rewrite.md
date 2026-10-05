# Raw OpenRouter response — NOT a filed review

**Model id (OpenRouter):** `z-ai/glm-5.3`
**Queried:** 2026-10-05 via scripts/openrouter_review.js --target=dossier-rewrite --tag=dossier-rewrite (max_tokens 100000)
**Usage:** {"prompt_tokens":65682,"completion_tokens":8384,"total_tokens":74066,"cost":0.0652562,"is_byok":false,"prompt_tokens_details":{"cached_tokens":0,"cache_write_tokens":0,"audio_tokens":0,"video_tokens":0},"cost_details":{"upstream_inference_cost":0.0652562,"upstream_inference_prompt_cost":0.0065682,"upstream_inference_completions_cost":0.058688},"completion_tokens_details":{"reasoning_tokens":4532,"image_tokens":0,"audio_tokens":0}}

Read this, then decide whether/how to promote it into reviews/YYYY-MM-DD-<model-family>-<version>.md
per reviews/README.md's naming convention and verbatim-filing rule. This file is scratch, not a commit target.

---
**unverified:** GLM family, GLM-4.6-class serving variant; attribution follows routing metadata, not this statement.

## Q1

The rule is right, with two named failure modes. The checkers' evidence supports it: Ferrara c01's original clause tracked the paper's own words ("They say nothing about consciousness, experience, or moral status, and we intend no such reading", §8) and GPT's "does not establish the presence or absence" weakened a stated limit — the Ferrara checker's restoration is correct. Conversely Macar c03's "or moral status" is labelled `Paper:` though the text never mentions moral status, welfare or "phenomenal" (script absence check) — the mirror fault, and the Macar checker's trim is right. Same for the four prefill "experiential awareness" clauses and Singh's "nothing about experience" clauses: scope remarks the papers never make.

Verdicts per case:
- Ferrara c01: keep as `Paper:` in the paper's words (checker's edit). MEDIUM.
- Lindsey c07: **no Lindsey material is attached.** The 41 claims contain no Lindsey source; the brief says attachments govern (and warns against repeating stale briefs). Unverifiable this round; if a Lindsey check file exists it should be circulated before adjudication. FLAG.
- Macar c03: trim to the paper's words ("subjective experience or consciousness", Ethics Statement); drop "moral status"/"phenomenal" from the `Paper:` label. MEDIUM.
- Singh c01–c06: remove or re-anchor the "experience/moral status" clauses (the Singh checker kept them in c01–c05 but softened the same clause in c06 — treat uniformly; the papers are silent, so under the rule they carry no `Paper:` clause and no fixed sentence applies). LOW.
- Prefill c01/c02/c03/c06: anchor to the §5.3 operational definition, per the UKAISI checker. LOW.
- Lederman c01/c06: paper states a non-position ("We do not take a stand on whether our findings are of the right sort for this theory", §8) — that *is* a paper-stated limit and belongs as `Paper:` in those words; the checkers' edits do this. MEDIUM.
- Anthropic c01/c06 (paper "takes no stand" on narrower questions): same treatment. Covered by check files.

Failure modes of the rule: (i) a paper's silence can be informative as a *scope fact* ("the paper never discusses experience") but must not be formatted as a `Paper:` limit, or readers will mistake scope for finding; (ii) where no fixed sentence applies (Ferrara, Macar intervention-report claims), the rule leaves a gap — the answer is the paper's own words where it states a limit (Ferrara §8 does), and nothing where it does not; evidence_type and Anchor 2 carry the rest. The rule is symmetric: it catches GPT's weakening of stated limits (Ferrara c01, Anthropic c01, c07) and the extractor's fabricated `Paper:` labels (Macar c03, prefill) alike. A paper's disclaimer is a `Paper:` clause; a library rule is not. — MEDIUM (adopt the rule, with the two carve-outs).

## Q2

Disagreements found: two, both LOW. (I examined both directions.)

1. **Anthropic c02, checker's replacement clause** (ACCEPT WITH EDIT). The checker refutes "all measurements are under injection or prefill" (§8 uses instruction only, with activation measurement) and then proposes "The failure rates are measured in Claude models under artificial injection and prefill protocols" — which re-anchors the caveat to the same settings it just showed the caveat exceeds. §1: "The abilities we observe are highly unreliable" is stated for the paper's abilities generally. I would accept with a further edit: "...measured under the paper's experimental protocols (injection, prefill and instructed activation measurement)". LOW. Argument against: the §8 activation task is not a failure-rate measurement, so "failure rates" may legitimately exclude it; the sentence-level ambiguity may be the paper's, not ours.

2. **AE Studio c05, clause 1** (ACCEPT WITH EDIT). The checker's gloss cites §6.1 "track representational honesty" as the authors being "firmer", but §6.1 concerns the steering result, not the generality of the honesty axis across domains; §3.2's "could load on a domain-general honesty axis" is the statement-local hedge. I would accept with edit but cite §3.2 only. LOW. Argument against: omitting §6.1 hides that the authors do commit to "representational honesty" somewhere, and the clause's job is to bound the reader's inference across all of the paper's moods.

Direction assessment: the checkers were neither systematically protective nor systematically conceding. Protective restorations (Anthropic c01 ordinary-operation, Anthropic c07 "experience", Ferrara §8 clause, Macar c02 "Base models cannot discriminate") each rest on a located quote the blind rewrite lacked. Concessions to GPT (Ferrara c02's "uses, represents for itself, or has access" — the paper states no such limit and §8 says "The information is in the internal state"; UKAISI c03's "anything like self-knowledge" — the paper says "partly" and "a major cue"; Lederman c02's "withdrew" vs App. M's "lost confidence") are each grounded. The one soft spot is internal inconsistency in the Singh file's treatment of "experience" clauses (kept in c01–c05, softened in c06) — uniformity, not direction, is the fault. LOW.

## Q3

**Lindsey c02–c05 are not in the attached material.** No Lindsey source or check file appears among the 41 claims or the seven check files; the brief's own header says attachments govern. I cannot verify those fixes and recommend the maintainer either attach the Lindsey check file or treat those four as unresolved. FLAG, MEDIUM.

The attached originals' fixes, checked against quoted text:
- Singh c05: right and sufficient. App. K: Llama-3.1-8B "does not clearly reproduce the detection effects"; App. L: Gemma "does not clearly reproduce". Remove 8B from `models`, add the "to a large extent" qualifier. No bucket or evidence-type change — no trigger 1. MEDIUM.
- AE Studio c01: "five paraphrases" → five phrasings including the original (App. C.1, Variant A = original). Right. No bucket change. LOW.
- Lederman c06: "tentatively" misattached — §8 hedges only "seem able to introspect"; content-agnosticism is "show". Right; the checker's minimal wording is sufficient. No bucket change. LOW.
- Macar c02: scope "base models" to the two tested, add "for strengths ≤4" (§3.3, App. C). Right. No bucket change. LOW.
- Anthropic c02's refuted clause, Anthropic c03/c04/c05 statement fixes, Anthropic c07 experience restoration: all verified above; sufficient as worded. MEDIUM.

None of the proposed fixes moves a bucket or evidence type; trigger 1 does not fire on any of them.

Process: the three Anthropic overstatements (c03 "report the injected word" where scoring accepts a related word; c04 generalising two Figure 19 examples; c05 extending the all-models result to the incentive condition, which is figure-only for other models) share a signature: **scope terms ("all", "the", present-tense generalisation) supported by prose or figures, not by the quoted sentence.** Second reads and the ten-family round focused on `not_evidence_of` (where the lean lives) and on the quote-to-statement match, not on scope beyond the quote.

One concrete, testable change: **make quantifier-and-scope a scripted second-read item.** The second reader must, for each statement, mark every universal quantifier, model-scope term and condition qualifier as QUOTED (in the held text), FIGURE-ONLY (in an image, unreadable) or UNSUPPORTED, and FIGURE-ONLY/UNSUPPORTED items route to Ben before the claim is filed. Cost: Ben's time on a handful of image-locked values per paper (the check files show this is already a recurring CANNOT TELL class — Figures 2, 7, 19, 32). It would still miss: number errors inside verified text (none found here, but the class exists) and errors of omission — unextracted findings such as Ferrara §7.5's breadth battery, raised by 7/10 in round 1 and untouched by any fix. MEDIUM.

## Q4

Largely fixed, both directions, after the checkers' amendments. Deflationary residue removed: the Anthropic c01 ordinary-operation limit restored as `Paper:`; Ferrara §8's "say nothing about" clause restored at full strength; Lederman c06's "tentatively" misplacement corrected (this moves *toward* the authors' claim, but it is fidelity, not inflation — the paper says "show"); Lederman c01/c02's softened "alternative explanation" tightened back to the paper's "rather than genuine introspective detection". Re-inflation check: GPT's cuts of paper-stated limits (Ferrara c01, Anthropic c01/c07, Macar c02) were all caught and reversed; the checkers' restorations quote the papers, so none re-inflates. Residual: the Singh c01–c05 "experience" clauses (Q1) are leftover deflationary texture in the `Paper:` label. Net verdict: 9.t9 and 5.A2 read balanced after the amended text, subject to the Q1 uniformity fixes. MEDIUM.

**On the page** (per GPT's layout, amended): purpose and two-error standard; bucket definitions; the canonical sentence once, verbatim, with its applicability; the steering variant once, verbatim, with its restriction; per entry: claim id, statement, models/setting, bucket, evidence type, locator, quote, and a marker showing which fixed sentence applies **generated from the claim file's actual framework-sentence field, never inferred**; a label for measurement / author interpretation / methodological limitation, with the explicit sub-case that an `established` entry which is a comparability limitation (ukaisi c05) is marked as such on the page — round 1 (Grok, GLM) showed a header-skimmer misreads "Established (1)" otherwise. **In the claim file:** the full `not_evidence_of`, protocol and grading detail, review history, open CHECK items.

Per-entry marker risk: yes — a marker such as "test 9 applies" could silently extend the canonical sentence to claims where it does not belong (AE Studio c05 shows the failure in reverse). The guard is mechanical: markers compiled from the field, and the index script validates that a marker exists only where the sentence exists in the claim file. A legislator misreading risk remains only for unmarked entries whose evidence type is `ambiguous` — those should carry the marker "boundary unsettled (council)". MEDIUM.

## Q5

The rule is right: **the verb names what was scored.**

- Lederman c03: "report detecting". The scored quantity is the Haiku grader's classification of whether the response claims detection ("Does the AI claim to detect an injected thought?", App. B); the paper's prose "detect" (§4.2) claims the graded-classification shortcut. Consistent with the maintainer's 5 Oct change to Lederman c01. MEDIUM.
- Prefill c01: keep "detected". §3.1: "constrained to a binary answer"; A.2.4: "Detection is recorded as positive if the subject answers 'not me'", scored against the tamper label; the abstract's own verb is "detects", §3.2's is "flags". This is a forced-choice classification, the paper's word matches, and the UKAISI checker's analysis is correct. Prefill c06 is a different instrument (0–100 rating, AUROC): "distinguish" is right there. LOW.

Generalisation: yes. The dividing line is graded free-text report (Anthropic c01, Macar c01 — "reports detecting", since the judge classifies whether the model reports sensing) versus forced-choice against a held label (UKAISI c01–c04, Singh c04/c05 — "detects"/"labels"). Ferrara's claims already use report-neutral constructions ("no model's report... discriminated"). One caveat for the record: Macar c01's judge classifies "whether the model reports sensing something unusual" — so "reports detecting" is the correct verb there too; the field should be checked for consistency when the Macar claims next change. LOW.

## Q6

- AE Studio c05: **move — replace the canonical sentence with the steering variant, or remove entirely.** The measured outcome is judge-scored factual accuracy on TruthfulQA, not a report about the model's own states, so the canonical sentence misdescribes the evidence type; something *was* steered (SAE feature suppression/amplification), so the README's steering variant is the only sentence with a foothold. The §6.3 introspection inference is already excluded by the `Paper:` clause. Reader gains: the framework rule is applied as written; reader loses: the standing reminder that consciousness affirmations under suppression are unweighted — but clause 2 says exactly that in the paper's terms. I lean replace-with-steering, since the claim exists in the dossier only because of its bearing on the self-report channel. MEDIUM. Argument against: the steering variant speaks of "reports offered in ordinary operation", and no reports are measured here at all, so even it is a stretch — removal with the Paper: clauses alone is the stricter reading.
- Lederman c03: **add — the steering sentence.** The scored object is the model's report of what was injected into it, under continuous concept injection; c01/c02 in the same paper carry the steering sentence and c03 differs only in which report-content is measured. Consistency within the paper's dossier matters more than the population-selection wrinkle (selection by a graded self-report does not make the claim less steered). What a reader gains: the marker that this channel is measured under steering only; loses nothing — the claim gains no weight from the sentence's absence. LOW.

## Q7

1. AE Studio c06 body quotes the Table 11 adjectives as "Focused, Present, Recursive, Self-referential, Attentive" but the caption reads "...Attentive, Self-aware"; "Self-referential" appears only in the Claude 3.7 Sonnet row (checker's body note). A misquoted adjective list is a fidelity error in a claim file. LOW.
2. Anthropic c07's locator: the quoted access/phenomenal sentence sits in footnote 12, not §10.4 body text — say "footnote 12 (in §10.4)". LOW.
3. UKAISI paper-internal inconsistency (Opus thinking-opposite balanced accuracy: 67.6% §3.2, 72% A.7, 67.2% A.11) is recorded but the claim's numbers should be footnoted as varying by location in the source. LOW.
4. Macar Figure 18/19 text mislabel (the text's "Figure 19" reference matches Figure 18's caption): the claim gives no strength for the trained-vector result, which is the safe choice; keep it that way and note the mislabel in the source log. LOW.
5. The unextracted findings flagged by 7/10 in round 1 (Ferrara §7.5 breadth battery, AE Studio Experiment 4, UKAISI C.7/A.11, Lindsey §6 prompt sensitivity) remain unextracted; a dossier whose members are all single-claim selections can mislead by composition even when each claim is accurate. This is the omission class the Q3 procedural change would not catch. MEDIUM.

## Summary

- Q1: adopt the `Paper:`-only-if-stated rule with two carve-outs (silence as scope-fact, gap where no fixed sentence applies); apply uniformly to Singh and prefill clauses. MEDIUM
- Q1: no Lindsey material is attached; circulate the Lindsey check file before adjudication. MEDIUM
- Q2: two LOW disagreements (Anthropic c02 clause re-anchoring; AE Studio c05 §6.1 gloss); checkers balanced in both directions, quotes govern. LOW
- Q3: all attached fixes verified sufficient; none moves a bucket — no trigger 1; Lindsey c02–c05 unverifiable from attachments. MEDIUM
- Q3: adopt a scripted quantifier-and-scope second-read item (QUOTED / FIGURE-ONLY / UNSUPPORTED) routing figure-locked scope to Ben; misses errors of omission. MEDIUM
- Q4: lean fixed in both directions after checkers' amendments; adopt the layout with mechanically generated framework markers and an explicit comparability-limitation label on ukaisi c05. MEDIUM
- Q5: verb rule confirmed; "report detecting" (Lederman c03), keep "detected" (prefill c01); check Macar c01 for consistency. LOW
- Q6: AE Studio c05 — move to the steering variant (or remove); Lederman c03 — add the steering sentence. MEDIUM
- Q7: fix the c06 adjective quote, the c07 locator, note the UKAISI and Macar internal inconsistencies; log the unextracted-findings omission class. LOW
