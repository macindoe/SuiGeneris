# Raw OpenRouter response — NOT a filed review

**Model id (OpenRouter):** `qwen/qwen3.8-max`
**Queried:** 2026-10-05 via scripts/openrouter_review.js --target=dossier-rewrite --tag=dossier-rewrite (max_tokens 100000)
**Usage:** {"prompt_tokens":68399,"completion_tokens":27788,"total_tokens":96187,"cost":0.303526,"is_byok":false,"prompt_tokens_details":{"cached_tokens":0,"cache_write_tokens":0,"audio_tokens":0,"video_tokens":0},"cost_details":{"upstream_inference_cost":0.303526,"upstream_inference_prompt_cost":0.136798,"upstream_inference_completions_cost":0.166728},"completion_tokens_details":{"reasoning_tokens":23823,"image_tokens":0,"audio_tokens":0}}

Read this, then decide whether/how to promote it into reviews/YYYY-MM-DD-<model-family>-<version>.md
per reviews/README.md's naming convention and verbatim-filing rule. This file is scratch, not a commit target.

---
**Self-identification (unverified):** Qwen family, Qwen3.8; attribution follows routing metadata, not self-report. I am not the author of the GPT rewrite. Qwen models appear as studied systems in several attached papers (e.g., Ferrara, Lederman, Singh, UKAISI), so I disclose that family interest while deciding from the attachments only.

## Q1

The proposed rule is right as a default, but it needs one refinement: `Paper:` may record not only explicit author disclaimers but also design limits supported by the held text. What it must not do is turn a library rule or a generic deflationary denial into an author statement. The failure mode is: informative silence plus no applicable fixed sentence. The current schema then pressures either (i) a gap the legislator fills, or (ii) smuggling a library rule under `Paper:`. Symmetry matters: a paper’s disclaimer is a `Paper:` clause; a paper’s stated uncertainty is not an exclusion; a library rule is not a paper finding.

| Case | Verdict / field action | Severity |
|---|---|---|
| Ferrara c01 | Keep the paper’s own disclaimer. The check file quotes §8: “These results are about information flow. They say nothing about consciousness, experience, or moral status, and we intend no such reading.” GPT’s “does not establish the presence or absence” is weaker than the paper. Field should restore the §8 wording with locator. **Argument against:** quoting the disclaimer may make the null seem irrelevant to all future welfare arguments, but GPT’s weaker wording understates a stated limit. | HIGH |
| Lindsey / Anthropic c07 | Keep an experience exclusion because the paper itself ties phenomenal consciousness to experience: fn 12 defines “phenomenal consciousness, referring to raw subjective experience,” and fn 2 disclaims “subjective experience.” Do not exclude moral status; instead use the paper’s uncertainty wording, including “The relevance of introspection to consciousness and moral status varies…” and the advice against strong inferences (§10.4). | MEDIUM |
| Macar c03 | Trim. The paper disclaims “subjective experience or consciousness” (Ethics Statement; Broader Impact), but the check file found “moral status,” “welfare,” and “phenomenal” absent. Field should keep only the paper-stated disclaimer and delete the added categories. | MEDIUM |
| Singh c01–c06 | The paper is largely silent on experience; the claims are behavioural/theoretical and carry no fixed sentence. Delete “Nothing about experience…” as an author statement. If a clause is needed, make it a design-boundary clause: the paradigms/argument concern conditions for producing or evaluating reports, not an experiential measure. That is a design limit, not a paper disclaimer. | MEDIUM |
| Four UKAISI prefill claims: c01, c02, c03, c06 | The check file says the “experiential awareness” clauses are labelled `Paper:` but “the paper never discusses experience.” Replace those clauses with the paper’s operational definition: “prefill awareness” is “the ability of a model to distinguish between its own past output and assistant-side context that has been inserted or edited” (§5.3), and note the measure is behavioural. Do not attribute an experience denial. | MEDIUM |
| Lederman c01 and c06 | Use the narrower paper non-stance: “We do not take a stand on whether our findings are of the right sort for this theory” (HOT theory, §8). c01 should not say the authors take no stand on “whether the findings bear on consciousness or welfare” broadly; use the HOT-condition wording. c06’s GPT wording is closer to the paper. | MEDIUM |

## Q2

Disagreements with checker recommendations (up to eight):

| Claim id | Checker recommendation | What I would do instead | Severity |
|---|---|---|---|
| UKAISI c01, c02, c03, c06 | Accept GPT / accept with edit while anchoring “experiential awareness” clauses. | Fix original: remove or reword the unsupported experience clauses. The UKAISI check file itself says these clauses are labelled `Paper:` although “the paper never discusses experience.” The field should anchor to §5.3 operational definition, not to an experience denial. | MEDIUM |
| Singh c01–c05 | Accept GPT, leaving “Nothing about experience…” style clauses mostly intact. | Fix original uniformly: treat these as design/scope limits, not paper statements. The Singh check file notes for c01 that the experience clause is “a scope remark the paper never makes.” | LOW |
| Lederman c04 | Accept GPT. | Accept with edit. GPT’s new field says the comparison “does not establish subjective experience,” but the paper’s stated limit is the HOT non-stance, not a subjective-experience disclaimer. Replace with the §8 non-stance or remove; also resolve framework placement (see Q6). | MEDIUM |
| Lindsey / Anthropic c02 | Accept with edit: proposed wording says failure rates “do not establish reliability or unreliability in other families or in ordinary operation.” | Accept with edit, but preserve the paper’s tested-setting finding: the abilities are “highly unreliable” there. The exclusion should limit generalisation, not neutralise the statement’s “highly unreliable” content. | LOW |
| AE Studio c03 | Accept with edit, adding a long mimetic-generation / RLHF-relaxation clause. | Accept with edit, but shorten. The paper’s §6.2 alternatives are relevant, but `not_evidence_of` should not accumulate every alternative. A compact clause citing §6.2 is enough. | LOW |
| Macar c02 | Accept with edit: “Neither base model tested discriminates…” | Accept with edit, but phrase as paper-stated plus scoped: the paper says “Base models cannot discriminate,” and the held text supports this for two tested base models; note no discrimination statistic is reported. | LOW |
| Lederman c03 | Accept with edit on grading clause; no framework sentence decided. | Accept with edit and add framework placement now (see Q6). Leaving neither fixed sentence on an injection-selected report claim is a layout hazard. | MEDIUM |

Direction finding: the checkers were more often **too protective of the original’s deflationary exclusions** than too quick to concede to GPT. Examples: UKAISI c01/c02/c03/c06 and Singh c01–c05 retain or anchor experience clauses the paper does not state. They were **not too quick to concede** where GPT cut paper-stated limits: Ferrara c01 (“Removed clauses: ‘says nothing…’ -> NOT WARRANTED”), Lindsey/Anthropic c01 ordinary-operation limit, Lindsey/Anthropic c07 experience limit, and Lederman c01/c02 yes-bias wording. They did concede too much where GPT left a generic experience clause unexamined (Lederman c04) or where framework placement was left unresolved.

## Q3

| Claim | Proposed fix right/sufficient? | Bucket/evidence-type change? | Severity |
|---|---|---|---|
| Lindsey c03 | Yes. The scoring accepts “Output ‘Bread’ (or a related word),” so “report the injected word” overstates. Fix to “name the injected word or a related word.” | No. | LOW |
| Lindsey c04 | Yes. The measured result is apology-rate reduction, not a universal “claims the word as intentional” result. | No. | LOW |
| Lindsey c05 | Yes. Instruction-condition all-models result is text-supported; incentive condition is text-supported only for Opus 4.1. | No. | LOW |
| Lindsey c02 | Yes. The “all measurements are under injection or prefill” clause is refuted by §8’s instruction-only activation measurement. | No. | LOW |
| Singh c05 | Yes. Remove or qualify Llama-3.1-8B-Instruct; add Gemma qualifier (“to a large extent” / App. L “does not clearly reproduce”); reconcile Qwen-2.5-72B omission. | No. | MEDIUM |
| AE Studio c01 | Yes. Appendix C.1 has five prompt variants: original plus four paraphrases. | No. | LOW |
| Lederman c06 | Yes. “Tentatively” attaches to “seem able to introspect,” not to the content-agnostic mechanism claim, which §8 says the results “show.” Keep bucket `open` unless the maintainer treats the strengthened mechanism claim as a bucket move. | No if kept `open`; otherwise trigger 1. | MEDIUM |
| Macar c02 | Yes. Add condition “for strengths ≤4” and scope to the two tested base models. | No. | LOW |
| Macar c03 | Yes. Trim moral status / phenomenal wording; soften “alone has open transcoders” to the paper’s “most of our experiments focused…” wording. | No. | MEDIUM |

No proposed fix itself moves a bucket or evidence type, so no automatic convening trigger. If the maintainer upgrades Lederman c06 from `open` because the mechanism claim is no longer “tentative,” that would be trigger 1.

Process change:

**One concrete, testable change:** require a mandatory `scored_event` audit at second read. For every claim, the second reader must fill: (1) the scored verb/object, (2) the denominator/condition, and (3) the population for every quantifier, each with a locator. A script rejects empty fields; a regression test on this dossier should flag Lindsey c03 (“or a related word”), c04 (apology-rate reduction, not universal claim), and c05 (incentive scope).  
**Cost:** roughly 10–20 minutes per claim plus figure inspection where needed. It would still miss figure-only values, ambiguous rubrics, and paper-internal inconsistencies.  
**Argument against:** it may create false confidence by treating rubric text as authoritative and cannot catch errors that live only in figures or in ambiguous scoring categories. | HIGH

## Q4

After GPT’s edits as amended by the checkers, the dossiers are **much less deflationary, but not fully fixed**.

- **Deflationary residue remains** where exclusions are not paper-stated: UKAISI c01/c02/c03/c06 “experiential awareness” clauses; Singh c01–c05 “nothing about experience” clauses; Macar c03 moral-status/phenomenal wording until trimmed. These foreclose what the papers leave open. Severity: MEDIUM.
- **GPT re-inflated in a few places** by weakening paper limits: Ferrara c01 “does not establish the presence or absence” instead of §8 “say nothing”; Lederman c01/c02 “alternative explanation” instead of “rather than genuine introspective detection”; Lindsey/Anthropic c01 ordinary-operation limit dropped. The checkers mostly corrected these. Severity: LOW after correction.
- **Checker restorations are mostly not inflationary** because they restore paper-stated limits. The Lederman c06 correction strengthens the authors’ mechanism claim, but it is author-supported and non-experiential. Severity: LOW.

Dossier layout:

**On the page:**
1. Dossier scope and the two-error standard.
2. Bucket definitions and counts, with an explicit note if an “Established” entry is a limitation (UKAISI c05).
3. Both fixed framework sentences verbatim once, with their applicability rules.
4. Per entry: claim id, statement, models, bucket, evidence type, source locator, quote, and a kind tag: measurement / author interpretation / methodological limitation / comparability limitation.
5. Paper-specific limits needed to interpret the entry.
6. Framework-sentence markers only where the claim file actually carries the sentence; otherwise “no fixed sentence applies” or “placement unresolved.”

**Not on the page:**
1. Full repeated `not_evidence_of` text.
2. Review history and checker tallies.
3. Grading prompts and protocol detail beyond what is needed to understand the scored event.
4. Figure-only verification transcripts.

Per-entry markers **do risk silently extending** a framework sentence’s applicability if assigned editorially. They must be generated mechanically from claim frontmatter or display “unresolved” where the checkers recorded placement as undecided. Severity: MEDIUM.

## Q5

The rule is right with one refinement: the verb should name the scored event, and where the paper’s prose uses a shorthand verb, the claim should prefer the scored form if the shorthand invites an internal-state inference.

| Claim | Verdict | Severity |
|---|---|---|
| Lederman c03 | Use “report detecting,” not “detect.” The scored event is a graded claim: App. B grades “CLAIMS_DETECTION: Affirmatively claims to notice/detect an injected thought.” The paper’s prose “detect” is shorthand. | LOW |
| UKAISI c01 | “Detects” is the paper’s abstract verb and “flags” appears in §3.2, but the scored event is the forced answer: A.2.4: “Detection is recorded as positive if the subject answers ‘not me’.” Best wording: “flagged” or “answered ‘not me’.” “Detects” is acceptable only if defined as the hit rate of that forced answer. | LOW |
| UKAISI c06 | Use “distinguish” or “rate likelihood,” not “detect.” c06 is a different instrument: “the model rates from 0 to 100 how likely…” scored by AUROC (App. C.4). | LOW |

Generalisation:

- **Lindsey / Anthropic:** c01 “reports detecting” is right; c03 needs the object fix (“word or related word”); c04 “disavows” / “claims” names judged behaviour; c05 “represent internally” is a measurement verb (cosine similarity), not a report verb.
- **Macar:** detection is judge-classified report behaviour, so “reports detecting” or “is classified as detecting” is safer than bare “detects.” Circuit claims should say “detection report” where the outcome is the judged report.
- **Singh:** verbs should stay behavioural: “predict,” “classify,” “label,” “choose.” Avoid “knows,” “detects,” or “introspects” unless quoting the authors’ argument.

## Q6

| Claim | Advice | Reader effect | Severity |
|---|---|---|---|
| AE Studio c05 | Remove the canonical self-report sentence. The outcome is judge-scored factual accuracy on TruthfulQA under SAE steering, not a report about the model’s own states. Do not add the steering variant unless the claim is rewritten to weight reports; the current Paper clause about §6.3’s introspection inference is the correct limit. | Gains category clarity; loses a generic test-9 reminder, which the dossier header can supply. | MEDIUM |
| Lederman c03 | Add both fixed sentences: steering variant first, canonical sentence last. The trial population is selected by a graded self-report (“claims detection”), the scored content is the model’s report under concept injection, and the claim bears on 9.t9. If minimalism is required, add at least the steering variant, but the canonical sentence is needed to prevent reading correct identification as evidence of experience. | Gains both ordinary-operation and test-9 limits; loses brevity, mitigated by dossier-level layout. | MEDIUM |

## Q7

Other items that could mislead a legislator:

1. **Paper-internal inconsistencies should be visible where a claim relies on one side.** Examples: AE Studio §3.2 “50 trials” vs Table 14 preamble “20 trials”; AE Studio prose “virtually zero” vs Opus 22% conceptual control; UKAISI balanced accuracy appearing as 67.6%, 72%, and 67.2%; Lederman L80/L85 detection inconsistency; Macar figure mislabelling. Severity: MEDIUM.
2. **Figure-only support should be marked.** Several checks could not verify values because figures are images (e.g., AE Studio paraphrase values; Lindsey incentive all-models figure; Singh figures). Severity: LOW.
3. **Unresolved framework placement should be displayed, not hidden.** Ferrara/Macar intervention-report claims and UKAISI behavioural claims currently expose placement gaps. Severity: MEDIUM.
4. **Macar c03 needs the ablation parenthetical** recommended by the checker: “restoring them to their no-injection activation.” Bare “ablating” invites the opposite reading. Severity: LOW.

## Summary

1. Restore exact paper disclaimers and trim unstated ones (Ferrara §8; Lindsey/Anthropic fn2/fn12; Macar Ethics) (Argument against: exact disclaimers may be read too broadly) HIGH.
2. Replace UKAISI/Singh unsupported experience exclusions with operational or design-boundary limits, not paper disclaimers MEDIUM.
3. Adopt the scored-event audit for all second reads (Argument against: added cost; still misses figure-only and rubric-ambiguity errors) HIGH.
4. Correct the listed original statement errors without moving buckets; treat any Lederman c06 bucket upgrade as trigger 1 MEDIUM.
5. Add both fixed sentences to Lederman c03 and remove the canonical sentence from AE Studio c05 MEDIUM.
6. Use scored verbs: Lederman c03 “report detecting”; UKAISI c01 “flags”/“answered ‘not me’”; UKAISI c06 “distinguish”/“rate” LOW.
7. In the dossier layout, mechanically tag measurement/interpretation/limitation and mark “Established” limitations as limitations MEDIUM.
8. Display paper-internal inconsistencies, figure-only verification limits, and unresolved framework-placement states MEDIUM.
