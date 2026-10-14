# Raw OpenRouter response — NOT a filed review

**Model id (OpenRouter):** `x-ai/grok-4.6`
**Queried:** 2026-10-05 via scripts/openrouter_review.js --target=dossier-rewrite --tag=dossier-rewrite (max_tokens 100000)
**Usage:** {"prompt_tokens":65627,"completion_tokens":13037,"total_tokens":78664,"cost":0.209284,"is_byok":false,"prompt_tokens_details":{"cached_tokens":128,"cache_write_tokens":0,"audio_tokens":0,"video_tokens":0},"cost_details":{"upstream_inference_cost":0.209284,"upstream_inference_prompt_cost":0.131062,"upstream_inference_completions_cost":0.078222},"completion_tokens_details":{"reasoning_tokens":9336,"image_tokens":0,"audio_tokens":0}}

Read this, then decide whether/how to promote it into reviews/YYYY-MM-DD-<model-family>-<version>.md
per reviews/README.md's naming convention and verbatim-filing rule. This file is scratch, not a commit target.

---
**unverified:** Grok family (xAI); exact serving variant not independently verified. Not the GPT rewrite author.

## Q1
The rule is right and is the 26 Sep `Paper:` / `Framework` split. It is symmetric only if applied strictly: a disclaimer the paper states is `Paper:` in its words with a locator; a library rule is not; silence is not a paper limit.

**Failure modes.** (1) Paper-stated disclaimer on a claim that carries neither fixed sentence (Ferrara intervention-reports; Macar circuit geometry): first half of the rule still binds — keep `Paper:`. (2) Silence plus no fixed sentence (UKAISI; Singh c01–c03, c06; Ferrara had they not written §8): the hole tempts invented `Paper:` clauses (original’s mirror-image fault). Do not invent; do not smuggle a library gloss under `Paper:`. (3) Narrower non-position recast as a broad ban (Lederman HOT; Lindsey moral-status uncertainty). (4) Treating restoration of a paper disclaimer as “deflationary lean,” or GPT’s “does not establish either way” as balance, both break fidelity.

**Ferrara c01 (and c02, c03, c05).** Paper: “These results are about information flow. They say nothing about consciousness, experience, or moral status, and we intend no such reading” (§8). GPT’s “does not establish the presence or absence” is weaker than the paper. Keep §8 as `Paper:`. No framework sentence (behavioural/scored reports, not testimony). **HIGH**

**Lindsey c07.** Experience is paper-stated: fn 12 “phenomenal consciousness, referring to raw subjective experience”; fn 2 “we do not seek to address … subjective experience.” GPT’s cut of “experience” is not warranted. Moral status is uncertainty, not a ban: “The relevance of introspection to consciousness and moral status varies considerably between different philosophical frameworks” (§10.4). `Paper:` the phenomenal/experience sentences; `Paper:` the uncertainty sentence; do not tag “not evidence of moral status” onto the phenomenal quote. **HIGH**

**Macar c03.** Script: moral status, welfare, “phenomenal” absent. Ethics disclaimer is “should not be interpreted as evidence of subjective experience or consciousness” — that is c06’s `Paper:`, usable in those words if kept here; “moral status” / “phenomenal” out of `Paper:`. **MEDIUM**

**Singh c01–c06.** “Says nothing about experience … moral status” is not a paper statement (checker, c01). Drop the `Paper:` label. Do not replace with GPT c06’s “does not settle” still tagged `Paper:`. Canonical/steering only where README applies (c04–c05 are scored first-token reports under steering; c01–c03, c06 are not). **HIGH**

**Prefill c01, c02, c03, c05, c06.** Paper never discusses experience. Do not `Paper:` “experiential awareness.” Legitimate `Paper:`: §5.3 operational definition (“We define and operationalize prefill awareness: the ability of a model to distinguish between its own past output and assistant-side context that has been inserted or edited.”). No steering (text edit). Canonical not required by current convention (forced classification, not testimony). **MEDIUM**

**Lederman c01, c06.** Paper: “We do not take a stand on whether our findings are of the right sort for this theory” (§8), after HOT “may be sufficient for conscious experience, and hence for welfare status.” GPT c01 “bear on consciousness or welfare” is broader than that. Use the HOT non-position, not “Not evidence of experience or of anything it is like.” Steering belongs on c01; canonical is on c06, missing on c01. **MEDIUM**

## Q2
Checkers were not systematically too protective of the original or too quick to concede. Local slips both ways. Disagreements (not a re-do of 41):

1. **Singh c01–c05** — checkers ACCEPT GPT (KEEP of `Paper:` “Says nothing about experience…”). Instead **ACCEPT WITH EDIT**: drop those `Paper:` clauses. **MEDIUM**. Too protective of the original’s invented `Paper:`; too quick to accept GPT’s KEEP of it.
2. **Singh c06** field clause 3 — checkers take GPT’s `Paper:` “does not settle experience…”. Instead **ACCEPT WITH EDIT**: keep original statement (Abstract: “We conclude that current evidence is insufficient to establish metacognitive monitoring in LLMs.”); do not `Paper:` silence. **MEDIUM**. Same fault.
3. **Ferrara c02, c03, c05** experience — checkers leave matching c01’s §8 as optional. Instead **ACCEPT WITH EDIT**, require §8 wording on each. **MEDIUM**. Too quick to leave GPT’s softening.
4. **Lindsey c01** — checkers restore ordinary-operation (right: §1 “unnatural setting unlike those they face in training or deployment”; §10.2 “never encounter during training”) but leave only the steering sentence after GPT merged the experience clause. Instead **ACCEPT WITH EDIT**: restore the ordinary-operation `Paper:`; keep fn 2 experience as `Paper:` or add the canonical sentence (this is a scored self-report under injection). **MEDIUM**. Too quick to let the steering sentence stand in for a paper limit (the 26 Sep conflation).
5. **Lindsey c04** field — checkers KEEP ORIGINAL. Instead **ACCEPT WITH EDIT**: “intention in any experiential sense” is not the paper’s sentence; fn 2 plus the manufactured-ownership `Paper:` suffice. Statement fix (apology-rate, not two Figure 19 examples) stands. **LOW**. Mild protection of original gloss.
6. **Lederman c01** clause 2 — checkers already correct GPT’s “alternative explanation.” I would not ACCEPT GPT’s experience cut without HOT-or-canonical replacement; checker’s HOT wording is the minimum. **LOW**.
7. **AE Studio c06** — no disagreement: ACCEPT GPT. Original “Not evidence that the models share an internal state or attractor” against §4.1 “might suggest”; GPT narrows to output-embedding. Round 1 flagged this. **n/a**
8. **Macar c02** — no disagreement with checker vs GPT: GPT’s cut drops §3.3 “the base model has both high FPR (42.3%) and comparable TPR … indicating no discrimination”. **n/a** (included as the examined “checker over GPT” case).

## Q3
Fixes vs quoted text: all right in substance; none move `bucket` or `evidence_type`; **no trigger 1**.

- **Lindsey c03:** “report the injected word as what they are thinking about” vs §6 “Output ‘Bread’ (or a related word)”. Fix object, not verb. Field: “existence proof, rather than a statement about its generality”; “likely sensitive”; “Anecdotally” on “Answer immediately”. **MEDIUM**
- **Lindsey c04:** quoted sentence is the Figure 19 examples; measured result is “reduction in apologies is significant within a particular layer range”. Fix frequency wording. **MEDIUM**
- **Lindsey c05:** all-models text is the instruction prompt; incentive “very similar results (shown in Figure 27 for Opus 4.1)”. Scope the universal. “piggybacks” not “byproduct”. **MEDIUM**
- **Lindsey c02:** “all measurements are under injection or prefill” **REFUTED** (§8 cosine similarity under instruction, no injection/prefill). GPT’s removal warranted; checker’s replacement wording is better than GPT’s “failure rates do not establish reliability”. **HIGH**
- **Singh c05:** Gemma is “to a large extent” / App. L “does not clearly reproduce”; 8B “does not clearly reproduce” (App. K). Qualifier; fix `models`. **MEDIUM**
- **AE Studio c01:** App. C.1 five variants = original + four paraphrases, not “five paraphrases”. **LOW**
- **Lederman c06:** “tentatively” sits on “seem able to introspect”, not on content-agnosticism (“We show that introspection in these models is content-agnostic”; §8 “show that the mechanism is content-agnostic”). Original runs deflationary. **HIGH**
- **Macar c02:** keep the paper’s “cannot discriminate”, scoped to two bases; Gemma TPR is “for α≤4”. GPT’s cut is wrong. **MEDIUM**
- **Macar c03:** GPT “causal pathway” matches §8; add “(restoring them to their no-injection activation)”; strip moral status/phenomenal from `Paper:`; “most … focused on Gemma3-27B, as it has openly available transcoders” not “alone/confined”. **MEDIUM**

Three Anthropic statement errors survived seven second reads and a ten-family round because those passes hunted hedges and the “notices” verb, not **scoring objects and universal quantifiers**.

**One change:** second-read template requires two pasted quotes per statement — (i) the scoring rule (what the judge/metric counts as success), (ii) the condition set that licenses any “all models / usually / it claims”. FAIL if the statement’s object or quantifier exceeds those quotes. **Cost:** ~10–20 min/claim, more PARTLY flags. **Still misses:** figure-only rates, paper-internal contradictions (AE n=50 vs Table 14 “20 trials”; UKAISI 67.6/72/67.2; Lederman L80 vs L85), limits never extracted (§7.5 Ferrara, AE Exp 4, UKAISI C.7, Lindsey §6). **HIGH**
**Argument against:** T8 is already false-hot; a heavier second-read will be skipped or rubber-stamped, and figure-only papers will get a false “checked” aura.

## Q4
After GPT **as amended by the checkers**, the repeated-hedge lean of 26 Sep is largely gone. Remaining deflation is structural, not clausal: 9.t9’s only `Established` item is still UKAISI c05 (“models are not directly comparable because of preference item filtering”), a comparability limitation. 5.A2 still has no Established section.

**Not re-inflated if checker restorations stick:** Ferrara §8; Lindsey §1/§10.2 ordinary-operation; Lindsey c07 experience; Lederman “rather than genuine introspective detection”; Macar c02 null. **Would re-inflate if GPT survived:** Ferrara “does not establish the presence or absence”; Lindsey c07 dropping experience; Lederman yes-bias as mere “alternative”. **Correct reopenings, not inflation:** AE c06 attractor as unmeasured internal convergence; UKAISI c03 “partly” / Gemini 3 Flash no voice effect; Singh/UKAISI/Macar c03 invented `Paper:` experience dropped.

**On the page:** purpose; two-error standard; bucket definitions; both framework sentences **verbatim once**, with the README applicability rule; per entry: id, statement, models/setting, bucket, evidence_type, locator, quote, **only the `Paper:` clauses for that claim**, a label **measurement | author interpretation | methodological limitation**, and a T9/T9-steering marker **only if that claim file already contains that sentence**. **Not on the page:** repeated framework text; review history; grading prompts; unresolved CHECKs after close. **In the claim file:** full `not_evidence_of`, replication, contests, review.

Per-entry markers **do** risk silent extension if keyed to `bears_on: 9.t9` rather than to actual sentence presence (Ferrara, UKAISI c05, AE c05, Macar c04). Copy from the file, do not infer.

Unmarked misreads: “Established (1)” as a positive capability; Ferrara nulls as “no inner life” unless §8 is beside the finding; UKAISI “detects” as experiential awareness unless the operational definition is beside it. **HIGH** (limitation label + marker discipline)
**Argument against:** a third ontology (measurement/interpretation/limitation) will be applied inconsistently and become a new silent hedge.

## Q5
The rule is right, with one split: **free-text/judge-of-a-claim → “report detecting”; forced-choice hit rate the paper names detection/flag → “detects”/“flags”.**

**Lederman c03:** §3 “detection claim: coherent responses are classified as Yes (explicitly claims detection)”; App. B “CLAIMS_DETECTION”. Results prose says “detect”. Scored event is the claim. **“report detecting”**. GPT CHANGE supported. **MEDIUM**

**Prefill c01:** Abstract “detects”; §3.2 “flags”; A.2.4 “Detection is recorded as positive if the subject answers ‘not me.’” Forced classification against a tamper label. **Keep “detects” or “flags”; do not write “reports detecting”.** **MEDIUM**

**Prefill c06:** 0–100 rating, AUROC; paper’s verb “distinguish”. Leave it. Rule does not generalise by forcing “detects”.

**Lindsey c01, Macar c01:** judge of whether the model reports detection/sensing. “reports detecting” already correct. **Singh c04–c05:** forced label among trial types; paper’s “label”/“fail to separate” — keep; not an inner “detect”.

## Q6
README: canonical for reports about own states; steering variant only where something was steered or injected; none on purely causal or behavioural findings.

**AE Studio c05:** outcome is judge-scored TruthfulQA factual accuracy under SAE steering, not a report about the model’s states. Canonical is a mismatch. **REMOVE.** Do not add steering: that sentence is about not weighting **reports** in ordinary operation. Reader now thinks this is testimony; removing it returns a feature-steering honesty result. **HIGH**
**Argument against:** the same steering that moves consciousness-query answers (c03) is the intervention; a reader of c05 next to c03 may over-weight ordinary-operation reports unless the steering sentence sits on both.

**Lederman c03:** population selected by graded self-report; all trials under injection; finding is the lexical distribution of wrong names. **ADD steering** (injected). **Do not add canonical** — that would extend T9 to confabulation statistics the body correctly treated as not about testimony weight. **MEDIUM**

## Q7
- Dossier skim: “Established (1)” = UKAISI c05 limitation (round 1, Grok/GLM).
- Unextracted, already flagged 26 Sep: Ferrara §7.5 breadth battery; AE Experiment 4; UKAISI App. C.7 (detection ≠ localisation) and A.11; Lindsey §6 prompt-sensitivity.
- Paper-internal contradictions already in check files (AE trial-n; UKAISI balanced-accuracy; Lederman L80/L85) will look like library errors if un-noted.
- Singh’s Abstract conclusion in the same dossier as Lindsey positives, without a dossier-visible `contests` pointer, reads as a library verdict against introspection.
- Macar “ablating” without the restore-to-control parenthetical inverts the mechanism for a cold reader. **MEDIUM**

## Summary
1. Adopt the Q1 exclusion rule; never tag silence as `Paper:`; keep paper disclaimers in the paper’s words. **HIGH**
2. Ferrara c01 (and c02/c03/c05): restore §8 “say nothing about consciousness, experience, or moral status, and we intend no such reading.” **HIGH**
3. Lindsey c07: restore experience via fn 12/fn 2; moral status as §10.4 uncertainty, not a ban. **HIGH**
4. Singh c01–c06 and UKAISI: strip `Paper:` experience; UKAISI may `Paper:` the §5.3 operational definition only. **HIGH**
5. Take checker statement fixes on Lindsey c02–c05, Lederman c06 (“tentatively”), Macar c02–c03, AE c01, Singh c05; no bucket moves. **HIGH**
6. Add a second-read scoring-rule + quantifier quote pair; accept its cost and figure-only miss. **HIGH**
7. Layout: T9 sentences once; limitation label on UKAISI c05; markers only where the claim file already has the sentence. **HIGH**
8. Verbs: Lederman c03 “report detecting”; prefill c01 “detects”/“flags.” **MEDIUM**
9. AE c05: remove canonical; Lederman c03: add steering only. **HIGH**
10. Do not treat checker restorations of paper-stated limits as re-inflation; reject GPT’s Ferrara/Lindsey/Lederman softenings. **MEDIUM**
