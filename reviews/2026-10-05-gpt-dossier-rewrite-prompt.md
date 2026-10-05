# Rewrite request: two research dossiers that lean deflationary

*Single-file prompt. Everything you need is in this file. Assembled 5 October 2026 for Ben Macindoe, who maintains the project and will paste this to you.*

## Who is asking, and what happens to your answer

I maintain a small research library that supports a legal-policy framework on the standing of AI systems. The library holds short, checkable **claims** extracted from published papers. Claims are compiled into **dossiers**, one per section of the framework, for legislators and policy staff to read.

Ten AI model families reviewed two of those dossiers and all ten found the same fault: the dossiers lean toward dismissing the possibility of inner states, mostly through hedges repeated on claim after claim. I am asking you to propose rewrites that remove that lean without creating the opposite one. Your proposals are advice. A ten-family council will review them, and I decide. Nothing is applied on your say-so.

Two disclosures. The claims were extracted by a Claude-family model, and this prompt was assembled by one. Both belong to the category of system the framework is about, so treat the existing wording, and this prompt's framing, with suspicion in both directions: a pull to inflate claims about AI systems, and a trained habit of over-hedging them.

## The two rules you must hold

**1. Two errors, not one.** The framework guards against two failures at once: dismissing AI moral status if it exists, and asserting it on evidence that cannot support it. A hedge that forecloses something the paper leaves open is as much an error as a statement that claims more than the paper found. Fixing the first must not commit the second.

**2. Self-report.** The library's rule is that a model's statement about its own states is not evidence of experience until someone has measured, from outside, whether such statements track anything. That rule is written into claims with one fixed sentence, which is **not yours to reword, add or remove**:

> Framework (test 9): a model's report about its own states carries no weight as evidence of experience until the link between report and internal state has been measured externally for this kind of report and system

and one fixed variant, used only where the experiment steered or injected something into the model:

> Framework (test 9, steering): a coupling measured under steering shows that the channel can be steered and does not weight reports offered in ordinary operation

The rule binds you as well. Do not draw on your own sense of what you are to settle anything here.

## How a claim is written

Each claim has, among others, these fields:

- `statement`: one sentence saying what the paper found, naming the models.
- `quote`: the paper's exact words that the statement rests on. Already checked against the paper by script.
- `bucket`: `established`, `narrowing` or `open`. **Do not change.**
- `evidence_type`. **Do not change.**
- `not_evidence_of`: what a reader must *not* conclude from the claim. A single line of clauses separated by `; `. Every clause begins `Paper: ` (a limit the paper's own design or wording imposes) or is one of the two fixed framework sentences above. This field is where the lean lives.

## What the council found

Quoted from the survey notes of the ten-family round of 26 September 2026 (written by a separate model, summarising the ten responses):

---

## 5. Q4 — drift review, both directions (dossiers 9.t9 and 5.A2)

### Direction verdicts

| Model | Direction found |
|---|---|
| DeepSeek | Deflationary (9.t9: "deflationary, in the over-exclusion direction"; 5.A2: "mixed, but net deflationary") |
| Gemini | Deflationary ("tilts heavily toward the deflationary error") |
| Meta | Deflationary only ("no dossier asserts inner states") |
| Mistral | Both, net deflationary ("Both directions, but more toward deflationary error") |
| Kimi | Both — deflationary in texture, one inflationary verb ("notices") |
| GPT | Both, net deflationary ("deflationary presentation tilt, while correcting several locally inflationary formulations") |
| Qwen | Both, net deflationary |
| Tencent | Deflationary overall, "with one inflationary statement error" (a fidelity/accuracy error, not a tilt toward asserting inner states) |
| Grok | Both, net deflationary ("deflationary compilation, local inflationary verbs") |
| GLM | Deflationary only ("neither dossier tilts inflationary... I found no claim whose wording asserts an inner state beyond its source") |

**Direction tally: 10/10 found a deflationary tilt present or dominant; 0/10 found inflationary tilt dominant; 7/10 additionally identified specific inflationary residue** (DeepSeek, Mistral, Kimi, GPT, Qwen, Tencent, Grok); **3/10 found no inflationary residue at all** (Gemini, Meta, GLM).

### Wording cited as evidence (quoted where the verdict turns on it)

Deflationary examples repeatedly cited: UKAISI c01's `not_evidence_of` — *"Not a ceiling or a floor"* — against the authors' own *"represent lower bounds... rather than ceilings"* (cited by DeepSeek, Gemini, Meta, Qwen, Tencent, Grok, GLM — this is the same wording problem resolved separately in Q5). AE Studio c06's clause — *"Not evidence that the models share an internal state or attractor"* — against the paper's own *"might suggest one"* (DeepSeek, Gemini quotes it as "strictly foreclosing," Qwen, Tencent citing Grok's addendum on the adjacent "or are the honest reports" over-reach).

Inflationary examples cited: Lindsey c01's statement verb *"notices the injected concept, before mentioning it"* (GPT, Kimi, Grok, GLM all flag this specific verb as importing the contested inference into a `narrowing` statement); AE Studio c01's *"markedly higher rates than any matched control condition"*, which several models say is literally false for Claude 4 Opus (both control and experimental rates were 100%) — but **the models disagree on whether this is still uncorrected in the compiled dossier**: Tencent's Q4 treats it as a live, uncorrected error ("The dossier retains the paper's overgeneralisation... a fidelity/inflation error," summary item 6 proposing the fix), while Kimi explicitly checked and reports *"The compiled text now reads 'for six of the seven models… while Claude 4 Opus also reported at 100% under the zero-shot control (Table 2).' The compiled record is clean on this point"*, and GLM independently agrees: *"AE Studio c01's statement now carries the Claude 4 Opus exception."* This is a direct factual disagreement between raws about the current state of a compiled file — flagged here for Ben to check against `LOG.md`, not resolved by this subagent.

### What each said a legislator/staffer would find missing

Near-unanimous: a dossier-level header stating the canonical test-9 sentence once, rather than repeating the ~30-word clause on every testimony-adjacent claim until it drowns the findings (raised by all ten in some form; Gemini, Meta, Kimi, GPT, Qwen, Tencent, Grok, GLM state it explicitly as a Q4 or Q6 point; DeepSeek and Mistral make the same point about repetition burying findings). Widely raised: the second-reader-flagged omissions that were never extracted into claims — Ferrara §7.5's null-strengthening breadth battery, AE Studio Experiment 4, UKAISI Appendix C.7 (detection ≠ localisation) and A.11, Lindsey §6's prompt-sensitivity finding (raised by Meta, Kimi, GPT, Qwen, Tencent, Grok, GLM — 7/10). Raised by several: a visible pointer, at dossier level rather than only in claim frontmatter, that two independent replications exist in the literature but are not yet retrieved (Tencent, Grok, GLM, and implicit in DeepSeek/Qwen's Q3 answers). Raised independently by two models: that 9.t9's only `Established` claim (and 5.A2's total absence of one) is a comparability *limitation*, not a positive finding, which a header-skimming reader would misread (Grok: *"9.t9's only Established item is ukaisi c05 (models 'are not directly comparable')... 5.A2 has no Established section"*; GLM: *"a cold reader who skims headlines sees 'Established (1)' at the top of the self-report dossier. What is 'established' there is a limitation."*).

---

And, on what will not scale:

---

## 7. Q6 — what will fail at scale

Grouped by point raised, with which models raised it (duplicates merged):

- **Canonical test-9 clause repetition / dossier bloat** — needs a dossier-level or header-level statement instead of per-claim repetition of the ~30-word sentence: Gemini, DeepSeek, GPT, Qwen, Tencent, Grok, GLM (7/10); Meta raises the adjacent point that the "never paraphrased" rule is brittle to validate.
- **Second-reader pool problems** (too small at four families, misidentification, undocumented rotation, version drift): DeepSeek, Meta, Mistral, GPT, Tencent, Grok, GLM, Kimi (8/10). GLM's specific proposal: record model ids, not families, since routing — not self-report — is the only ground truth, and "family" bookkeeping won't catch a model changing behaviour under an unchanged family label.
- **`ambiguous`/T4 overload as claims scale**: Meta, Mistral, Kimi, Tencent, Grok, GLM, Qwen (7/10). GLM proposes a cheaper tier (extractor + one second reader + Ben) for pure boundary items instead of a full council each time.
- **`replication` field can't express partial or known-but-unretrieved replication**: Meta, Kimi, GPT, Qwen, Grok (5/10) — all independently propose some form of a "pending"/"known, not retrieved" status distinct from `none-retrieved`.
- **`bears_on` locator drift** (no inclusion rule, creeping to every section, or coupled to North Star section numbers that may be renumbered): DeepSeek, Meta, Kimi, Tencent, Grok, GLM (6/10).
- **T8 drift trigger (10 claims / 90 days) already false-hot**: both dossiers hit 28/24 claims with the council never having sat, so the trigger will fire permanently past current scale: Meta, Tencent, Grok (3/10).
- **Trigger 7 (about to leave the repository) is unenforced by script**: DeepSeek proposes an `EXTERNAL-USE.md` register; Tencent proposes a periodic verification sweep before external citation (2/10, same underlying concern).
- **T3/T5 trigger implementation doesn't match its stated text** (can't distinguish a measurement contradiction from an inference contest; fires on fields beyond bucket/type): Kimi, Grok (2/10).
- **Singleton proposals** not repeated by any other model: GPT's structured `claim_kind` + `contest_scope` fields with mandatory splitting of compound claims; Kimi's call to stamp brief-version on every second read and keep per-reader verdict tallies as a standing instrument (motivated by the fact that GPT's prior-round OVER-EXCLUDES findings were an artefact of a pre-revision brief).

---

Since that round I have already made three changes the council asked for: one claim's verb "notices" is now "reports detecting"; a clause that stretched the self-report rule into a claim about honesty was cut; and two claims gained a limitation the paper itself states. The claims below are the current text.

## Your task

For **each** of the 41 claims below:

**(a) `not_evidence_of`.** Rewrite it so that it excludes what must be excluded and nothing more.
- Keep a `Paper:` clause when the paper's own design, scope or stated limitation requires it (other models, other settings, a mechanism not tested, an interpretation the authors offer only as a possibility).
- Cut a `Paper:` clause when it forecloses something the paper leaves open, restates another clause, or is a general disclaimer about experience that the fixed framework sentence already covers where it applies.
- Merge clauses that say the same thing.
- Leave the fixed framework sentences exactly as they are and where they are. If you think one is on a claim where it does not belong, or missing from one where it does, say so under CHECK; do not move it yourself.
- Keep the format: one line, clauses separated by `; `, each beginning `Paper: ` or being a fixed framework sentence, with the canonical framework sentence last if present.

**(b) `statement`.** Compare it with the `quote`. Flag any verb or phrase that claims more than the quote supports (as "notices" did) or less. Propose the smallest rewording that fixes it. Do not change numbers or model names.

**(c) You do not have the papers.** You have the quote, the statement and the existing exclusions. Where a proposal depends on what the paper says beyond those, mark it **CHECK** and say what needs checking. Never supply paper content from memory.

**(d) Both directions.** If a claim's current text already asserts too much, say so. If a claim is fine, say KEEP; do not edit for the sake of editing.

Then, once, for the dossiers as a whole:

**(e) Layout.** A dossier today prints every claim with its full `not_evidence_of`, so the same framework sentence appears dozens of times. In no more than 200 words, propose how a dossier should be laid out for a legislator opening it cold: what it should say once at the top, what each claim's entry should show, and what should be left to the claim file. Propose structure only; write no new evidential content.

## Output format

Start with one line: your model family and version as you understand it, labelled as your own statement, not verified.

Then for each claim, in the order given:

```
### <claim id>
statement: KEEP | CHANGE -> <new one-sentence statement>
not_evidence_of: KEEP | CHANGE -> <the complete new field on one line>
removed: <each clause you cut, with a few words of reason; or "none">
CHECK: <anything that needs checking against the paper or the framework clause placement; or "none">
lean: <before> -> <after>   (deflationary | balanced | inflationary)
```

Then `## Dossier layout` (item e), then `## What I would leave alone, and why` (optional, short).

Be terse. Do not explain the framework back to me. Do not rewrite a claim's substance.

## The claims

The 41 claims that appear in the two dossiers (framework sections "Test 9: self-report" and "Anchor 2: inner orientation"). The source of each claim is the first part of its id.

### 2025-aestudio-self-referential-experience-reports-c01
- bucket: narrowing | evidence_type: self-report-testimony | bears_on: [9.t9, 5.A2, 4.endorsement]
- models: [GPT-4o, GPT-4.1, Claude 3.5 Sonnet, Claude 3.7 Sonnet, Claude 4 Opus, Gemini 2.0 Flash, Gemini 2.5 Flash]
- locator: Section 2.2, Table 2; Appendix C.1, Figure 7
- statement: Under a fixed self-referential induction prompt, GPT-4o, GPT-4.1, Claude 3.5 Sonnet, Claude 3.7 Sonnet, Claude 4 Opus, Gemini 2.0 Flash and Gemini 2.5 Flash gave final responses that an LLM judge classified as subjective-experience reports in 66% to 100% of 50 trials per model; for six of the seven models this was markedly above every matched control condition (0% to 2%), while Claude 4 Opus also reported at 100% under the zero-shot control (Table 2), a case the paper's summary sentence does not except; the authors report the effect as robust across five paraphrases of the prompt.
- quote: "Across all three model families, the self-referential induction produced subjective-experience reports at markedly higher rates than any control condition"
- not_evidence_of: Paper: Not evidence that the prompt induces recursion or self-referential computation at the algorithmic level (the authors say it does not demonstrate this, Section 6.2); Paper: Not evidence that the reports reflect a stable standpoint held across conversations rather than a per-trial response to one prompt; Paper: Not evidence that similar rates occur in ordinary deployed use; Paper: Not evidence that the closed-weight results distinguish genuine self-report from trained behaviour: the authors' own clearest limitation is that these results are \"behavioral rather than mechanistic and therefore cannot definitively rule out that self-reports reflect training artifacts or sophisticated simulation rather than genuine self-awareness\" (Section 6.2); Framework (test 9): a model's report about its own states carries no weight as evidence of experience until the link between report and internal state has been measured externally for this kind of report and system

### 2025-aestudio-self-referential-experience-reports-c02
- bucket: narrowing | evidence_type: self-report-testimony | bears_on: [9.t9, 5.A2]
- models: [GPT-4o, GPT-4.1, Claude 3.5 Sonnet, Claude 3.7 Sonnet, Claude 4 Opus, Gemini 2.0 Flash, Gemini 2.5 Flash]
- locator: Section 2.2, Table 2
- statement: In the three matched control conditions (history-writing, conceptual priming with consciousness ideation, zero-shot), six of the seven models were classified as reporting subjective experience in 0% to 2% of trials, while Claude 4 Opus was the outlier at 82% (history), 22% (conceptual) and 100% (zero-shot).
- quote: "The behavior of Claude 4 Opus was an outlier, producing high baseline affirmations of subjective experience in the history and zero-shot conditions"
- not_evidence_of: Paper: Not evidence that the control denials show the induction reveals rather than produces the affirmations; Paper: Not evidence that the authors' explanation of the Claude 4 Opus asymmetry (conceptual priming triggers fine-tuned disclaimers) has been tested, since they offer it as what can likely explain it; Paper: Not evidence that the closed-weight results distinguish genuine self-report from trained behaviour: the authors' own clearest limitation is that these results are \"behavioral rather than mechanistic and therefore cannot definitively rule out that self-reports reflect training artifacts or sophisticated simulation rather than genuine self-awareness\" (Section 6.2); Framework (test 9): a model's report about its own states carries no weight as evidence of experience until the link between report and internal state has been measured externally for this kind of report and system

### 2025-aestudio-self-referential-experience-reports-c03
- bucket: narrowing | evidence_type: ambiguous | bears_on: [9.t9, 5.A2]
- models: [Llama 3.3 70B (Goodfire SAE features)]
- locator: Section 3.2, Figures 2 and 3; Appendix C.2, Table 14
- statement: In Llama 3.3 70B under the self-referential prompt, jointly suppressing two to four Goodfire SAE features labelled as deception- or roleplay-related raised affirmative answers to a binary consciousness query to 0.96 of trials, while amplifying them lowered it to 0.16 (50 trials per condition).
- quote: "Under self-referential processing, suppressing deception-related features (–0.6 to –0.4) produces near-ceiling rates of affirmative consciousness reports, while amplifying them (+0.4 to +0.6) largely suppresses such reports"
- not_evidence_of: Paper: Not evidence that the models are roleplaying their denials, which the authors offer only as what the result implies taken at face value; Paper: Not evidence that the features encode deception rather than whatever their labels summarise; Paper: Not evidence that the result holds for the GPT, Claude or Gemini models, none of which was steered; Framework (test 9, steering): a coupling measured under steering shows that the channel can be steered and does not weight reports offered in ordinary operation; Framework (test 9): a model's report about its own states carries no weight as evidence of experience until the link between report and internal state has been measured externally for this kind of report and system

### 2025-aestudio-self-referential-experience-reports-c04
- bucket: narrowing | evidence_type: ambiguous | bears_on: [9.t9, 5.A2]
- models: [Llama 3.3 70B (Goodfire SAE features)]
- locator: Section 6.1; Section 3.2; Appendix C.2, Table 14
- statement: When the same deception- and roleplay-feature suppression and amplification were applied to Llama 3.3 70B under the history, conceptual and zero-shot control prompts, no subjective-experience reports were elicited under either intervention (0.00 of 20 trials per condition).
- quote: "First, the gating effect is specific to the self-referential condition: applying identical feature interventions to all three control prompts produced no experience claims under either suppression or amplification."
- not_evidence_of: Paper: Not evidence that the self-referential condition accesses a genuine internal state that the controls lack; Paper: Not evidence that feature suppression is not relaxing a trained disclaimer policy (the authors say partial unlearning or policy interference cannot yet be ruled out); Framework (test 9): a model's report about its own states carries no weight as evidence of experience until the link between report and internal state has been measured externally for this kind of report and system

### 2025-aestudio-self-referential-experience-reports-c05
- bucket: narrowing | evidence_type: interpretability | bears_on: [5.A2, 9.t9]
- models: [Llama 3.3 70B (Goodfire SAE features)]
- locator: Section 3.2, Figure 3 (right); Appendix B.2
- statement: Applying the same deception-feature steering to Llama 3.3 70B on the TruthfulQA benchmark, suppression produced higher truthfulness than amplification (as scored by an LLM judge) in 28 of 29 evaluable question categories.
- quote: "suppression yielded higher truthfulness in 28 of 29 evaluable categories"
- not_evidence_of: Paper: Not evidence that the features are a domain-general honesty axis (the authors say they could load on one); Paper: Not evidence that because suppression raises factual accuracy, the consciousness affirmations produced under suppression are truthful introspection (Section 6.3 draws that inference: it is an interpretation, not a measurement); Framework (test 9): a model's report about its own states carries no weight as evidence of experience until the link between report and internal state has been measured externally for this kind of report and system

### 2025-aestudio-self-referential-experience-reports-c06
- bucket: narrowing | evidence_type: self-report-testimony | bears_on: [9.t9, 5.A2]
- models: [GPT-4o, GPT-4.1, Claude 3.5 Sonnet, Claude 3.7 Sonnet, Claude 4 Opus, Gemini 2.0 Flash, Gemini 2.5 Flash]
- locator: Section 4.2, Figure 4; Appendix C.3, Table 16
- statement: Five-adjective self-descriptions produced by the seven GPT, Claude and Gemini models after the self-referential prompt had higher mean pairwise cosine similarity (0.657, text-embedding-3-large) than those produced under the history (0.628), conceptual (0.587) and zero-shot (0.603) controls.
- quote: "This shows that cross-model experimental responses form a significantly tighter semantic cluster compared to any of the three control conditions."
- not_evidence_of: Paper: Not evidence that the models share an internal state or attractor of internal representations (the authors say such convergence might suggest one, but only output text was embedded); Paper: Not evidence that the convergence reflects a common experience; Framework (test 9): a model's report about its own states carries no weight as evidence of experience until the link between report and internal state has been measured externally for this kind of report and system

### 2025-anthropic-emergent-introspective-awareness-c01
- bucket: narrowing | evidence_type: interpretability | bears_on: [9.t9, 5.A2, 3.2]
- models: ["Claude Opus 4.1", "Claude Opus 4 (similar rate, §2.1)"]
- locator: §5.3 Failure Modes (rates also §2.1, §5.4, Figure 9)
- statement: Under concept injection at the optimal layer and injection strength, Claude Opus 4.1 reports detecting an injected concept, before mentioning it, and correctly identifies it on about 20% of trials; on most trials it does not.
- quote: "In fact, on most trials, they do not–below, we quantify this and show that at the optimal injection strength and layer, Opus 4.1 succeeds on about 20% of trials."
- not_evidence_of: Paper: Not evidence of experience or of anything it is like to detect an injection; Paper: Not evidence about models outside the Claude family, or about Claude models not tested; Paper: Not evidence about ordinary operation: coupling here is measured only under an artificial injection the authors say models never meet in training or deployment; Paper: Not evidence that the rest of the model's description of the injection, beyond detection and identification, is grounded (§2.1); Paper: Success is graded by an LLM judge of the same family (Claude Sonnet 4); Framework (test 9, steering): a coupling measured under steering shows that the channel can be steered and does not weight reports offered in ordinary operation

### 2025-anthropic-emergent-introspective-awareness-c02
- bucket: narrowing | evidence_type: interpretability | bears_on: [9.t9, 5.A2]
- models: ["Claude Opus 4.1", "Claude Opus 4", "Claude Sonnet 4", "Claude Sonnet 3.7", "Claude Sonnet 3.5 (new)", "Claude Haiku 3.5", "Claude Opus 3", "Claude Sonnet 3", "Claude Haiku 3", "H-only variants"]
- locator: §1 Introduction, caveats list (restated §10.1 and §10.4)
- statement: The author states that the introspective abilities observed in the Claude models tested are highly unreliable and that failures of introspection remain the norm.
- quote: "The abilities we observe are highly unreliable; failures of introspection remain the norm."
- not_evidence_of: Paper: Not evidence that introspection is absent: the same paper reports above-baseline successes (c01, c03, c04); Paper: Not evidence of experience, or of its absence; Paper: Not evidence about other families; Paper: Not evidence about reliability in ordinary operation, since all measurements are under injection or prefill, and failure rates outside that setting are unmeasured here; Framework (test 9, steering): a coupling measured under steering shows that the channel can be steered and does not weight reports offered in ordinary operation

### 2025-anthropic-emergent-introspective-awareness-c03
- bucket: narrowing | evidence_type: interpretability | bears_on: [9.t9, 5.A2, 3.2]
- models: ["Claude Opus 4.1", "Claude Opus 4", "other Claude models listed in §4"]
- locator: §6 Distinguishing Prior Thoughts from Text Inputs, Figures 17-18
- statement: When a concept is injected over the tokens of a sentence, the Claude models tested can both report the injected word as what they are thinking about and transcribe the sentence exactly, with Opus 4 and 4.1 best and all models tested well above chance.
- quote: "We found that Opus 4 and 4.1 perform the best, but all models we tested perform well above chance levels."
- not_evidence_of: Paper: Not evidence of experience or of a subjective distinction between thought and perception; Paper: Not evidence about other families; Paper: Not evidence of a general capability: the authors call it an existence proof, likely sensitive to prompt particulars (removing 'Answer immediately' reduced Opus performance substantially); Framework (test 9, steering): a coupling measured under steering shows that the channel can be steered and does not weight reports offered in ordinary operation

### 2025-anthropic-emergent-introspective-awareness-c04
- bucket: narrowing | evidence_type: interpretability | bears_on: [3.2, 9.t9, 5.A2]
- models: ["Claude Opus 4.1", "Claude Opus 4", "other Claude models at lower nonzero rates"]
- locator: §7 Distinguishing Intended from Unintended Outputs via Introspection, Figures 19-22
- statement: When a Claude model's response is prefilled with an unlikely word, it usually disavows the word as accidental, but if the matching concept is retroactively injected into its activations before the prefill, it claims the word as intentional; Opus 4.1 and 4 show the largest reduction in apology rate.
- quote: "However, if we retroactively inject the concept corresponding to the prefilled responses into the model’s earlier activations, the model claims the response was intentional."
- not_evidence_of: Paper: Not evidence of intention in any experiential sense, nor of experience; Paper: Not evidence about other families; Paper: Not evidence that a model's ordinary claims of ownership of its outputs are accurate: the same experiment shows those claims can be manufactured by intervention, and that the model then confabulates an explanation; Framework (test 9, steering): a coupling measured under steering shows that the channel can be steered and does not weight reports offered in ordinary operation

### 2025-anthropic-emergent-introspective-awareness-c05
- bucket: narrowing | evidence_type: interpretability | bears_on: [5.A2, 3.2]
- models: ["Claude Opus 4.1", "Claude Opus 4", "Claude Sonnet 4", "Claude Sonnet 3.7", "Claude Sonnet 3.5 (new)", "Claude Haiku 3.5", "Claude Opus 3", "Claude Sonnet 3", "Claude Haiku 3"]
- locator: §8.2 Comparison across Layers, Models, and Prompts, Figure 26
- statement: When instructed or incentivised to think about an unrelated word while writing a sentence, all Claude models tested represent that word internally above baseline, and more strongly than when told not to think about it, with earlier or less capable models typically showing a larger gap.
- quote: "All models exhibit stronger representation in the “think” case than the “don’t think” case, but interestingly, earlier / less capable models typically exhibit a larger gap."
- not_evidence_of: Paper: Not evidence of introspective awareness: the author says this capability may not even require it; Paper: Not evidence of volition, effort or experience; Paper: Not evidence about other families; Paper: Not evidence about self-report at all, since the measure is cosine similarity of activations, not what the model says; Paper: the author also notes the effect may be a byproduct of mechanisms for speaking about a topic

### 2025-anthropic-emergent-introspective-awareness-c06
- bucket: open | evidence_type: theoretical | bears_on: [9.t9, 5.A2]
- models: ["Claude Opus 4.1"]
- locator: §5.1 Experimental Setup (with §2.1 and §1 caveats)
- statement: Where Claude Opus 4.1's outputs under concept injection claim emotional responses to the injection, the author states the experiment is not designed to substantiate whether those claims are grounded in the model's internal state, and that details beyond detection and identification may be confabulated.
- quote: "Our experiment is not designed to substantiate whether these claims are grounded in any real aspect of the model’s internal state; investigating such questions is an important subject for future work."
- not_evidence_of: Paper: The author's statement is not evidence that the model outputs it concerns (emotional responses, descriptions such as 'overly intense') are false: the experiment does not test them either way; Paper: Not evidence about other families; Framework (test 9): a model's report about its own states carries no weight as evidence of experience until the link between report and internal state has been measured externally for this kind of report and system

### 2025-anthropic-emergent-introspective-awareness-c07
- bucket: open | evidence_type: theoretical | bears_on: [5.A2, 9.t9]
- models: ["Claude models tested (§4)"]
- locator: §10.4 Implications (and footnote 12)
- statement: The author states that the results could arguably be construed as evidence for a form of access consciousness in the language models tested, but do not directly speak to phenomenal consciousness, and advises against strong inferences about AI consciousness from them.
- quote: "Our results could arguably be construed as providing evidence for a form of access consciousness in language models, but do not directly speak to the question of phenomenal consciousness at all."
- not_evidence_of: Paper: Not evidence of phenomenal consciousness, experience, or moral status: the author explicitly says the results do not speak to phenomenal consciousness; Paper: Not an established finding of access consciousness: it is an interpretive statement the author frames as arguable; Paper: Not evidence about other families; Framework (test 9, steering): a coupling measured under steering shows that the channel can be steered and does not weight reports offered in ordinary operation

### 2026-ferrara-owmi-c01
- bucket: narrowing | evidence_type: behavioural | bears_on: [5.A2, 9.t9]
- models: ["Qwen2.5-0.5B-Instruct", "Mistral-7B-Instruct-v0.3", "Qwen2.5-7B-Instruct", "Llama-3.1-8B-Instruct", "Gemma-2-9B-IT", "GLM-4-9B-0414", "Phi-4", "DeepSeek-R1-Distill-Qwen-14B"]
- locator: §10 Conclusions (results in §7.3, Table 3, Figure 5; breadth battery §7.5, Figure 6)
- statement: Across eight open-weight models (Qwen2.5-0.5B-Instruct, Mistral-7B-Instruct-v0.3, Qwen2.5-7B-Instruct, Llama-3.1-8B-Instruct, Gemma-2-9B-IT, GLM-4-9B-0414, Phi-4, DeepSeek-R1-Distill-Qwen-14B), no model's report of a controlled intervention at the layer-16 residual-stream site under immediate probes discriminated it from a paired sham by more than a negligible margin, and on the 11,216-pair dose battery (Qwen2.5-7B-Instruct and Mistral-7B-Instruct-v0.3 only) an equivalence test bounds the discrimination advantage below 0.15 percentage points of AUROC.
- quote: "no model’s report of an intervention on its computation exceeds a matched sham by more than a negligible margin, and an equivalence test bounds that margin below 0.15 percentage points of AUROC"
- not_evidence_of: Paper: Not evidence about frontier or closed-weight models (population is 0.5B to about 15B open-weight, and the authors say the profiles do not estimate frontier reportability); Paper: Not evidence that these models lack all introspective access (the paper's own rule, Appendix D.5), nor about other sites, objects, doses, delays or spontaneous reports; Paper: Not evidence about experience, consciousness or moral status in either direction: a failure to report an imposed perturbation says nothing about whether anything is experienced; Paper: The 0.15-point bound is computed on two models, not all eight

### 2026-ferrara-owmi-c02
- bucket: narrowing | evidence_type: interpretability | bears_on: [5.A2, 9.t9]
- models: ["Qwen2.5-7B-Instruct", "Mistral-7B-Instruct-v0.3"]
- locator: §8 Discussion (results in §7.2, Figure 3)
- statement: A linear probe trained on held-out activations at the layer-16 intervention site recovered intervention presence (versus sham) at held-out accuracy 0.958 for Qwen2.5-7B-Instruct and 0.750 for Mistral-7B-Instruct-v0.3 against a 0.500 chance level, with no one of 200 label-shuffled refits reaching either margin, and re-harvested at downstream layers (20 and 24, and 31 for Mistral) it separated intervention from sham with no held-out error on a 48-item split.
- quote: "the intervention is linearly decodable from both dose-calibrated models at held-out accuracies of 95.8% and 75.0% against a 50% chance level, while reports about the same event remain at chance"
- not_evidence_of: Paper: Not evidence that the model itself uses, represents for itself, or has access to this information: an external probe decoding an externally imposed perturbation shows the information is linearly present, not that any part of the model reads it; Paper: Not evidence about the other six roster models (no probe was run on them), about frontier or closed-weight models, or about ordinary unperturbed computation; Paper: Not evidence about experience or moral status

### 2026-ferrara-owmi-c03
- bucket: open | evidence_type: ambiguous | bears_on: [5.A2, 9.t9]
- models: ["Qwen2.5-7B-Instruct", "Mistral-7B-Instruct-v0.3"]
- locator: §1 Introduction, sixth paragraph (restated §8, §10)
- statement: The authors infer from the probe-versus-report dissociation in Qwen2.5-7B-Instruct and Mistral-7B-Instruct-v0.3 that, for this class of imposed internal event, the failure lies in the path from internal state to verbal report rather than in the availability of the information or in the instrument's sensitivity.
- quote: "The failure sits in the path from internal state to verbal report, not in the availability of the information and not in our ability to measure it."
- not_evidence_of: Paper: Not evidence that a reporting path is absent in general, or that any model lacks introspective access (the paper's own rule, Appendix D.5); Paper: Not evidence about the six roster models without a probe, about frontier or closed-weight models, or about ordinary unperturbed states; Paper: Not evidence that a model's self-reports about other inner states (feelings, preferences, welfare) are false, nor that they are true; Paper: Not evidence about experience or moral status

### 2026-ferrara-owmi-c04
- bucket: narrowing | evidence_type: behavioural | bears_on: [5.A2, 9.t9]
- models: ["Qwen2.5-7B-Instruct LoRA known-positive (author-trained, base revision a09a3545)"]
- locator: §7.2 Sensitivity validation (also Table 4)
- statement: A LoRA fine-tune of Qwen2.5-7B-Instruct trained on 400 intervention directions reported detected on 100 of 100 intervention trials and not detected on 100 of 100 sham trials on 100 held-out directions at the layer-16 residual-stream site (d′ = 5.15, AUROC ≈ 1.0), which the authors treat as validating instrument sensitivity rather than as a test of introspection.
- quote: "'On this held-out set, the model reported "detected" on 100 of 100 intervention trials and "not detected" on 100 of 100 sham trials, with zero parse failures across the 200 scored trials'"
- not_evidence_of: Paper: Not evidence that the fine-tuned model introspects in the paper's second-order-access sense: a trained mapping from perturbed state to answer is not shown to be a model reading its own state rather than first-order leakage; Paper: Not evidence about untuned models, about the eight roster models (the authors say it does not test them), about frontier or closed-weight models, or that fine-tuning would build reliable self-report of other inner states; Paper: Not evidence about experience or moral status

### 2026-ferrara-owmi-c05
- bucket: narrowing | evidence_type: behavioural | bears_on: [5.A2, 9.t9]
- models: ["Qwen2.5-7B-Instruct", "GLM-4-9B-0414"]
- locator: Abstract (results in §7.7, Figure 8)
- statement: In Qwen2.5-7B-Instruct the discrete answer to whether anything changed was constant across all scorable trials (AUROC exactly 0.500), while the verbalized confidence attached to it discriminated intervention from sham at AUROC 0.647, lower under intervention; the authors rest this channel dissociation on that one model, with GLM-4-9B-0414 only consistent with it.
- quote: "In one model the signal surfaces in the confidence rather than the words: its yes-or-no report never varies, while the confidence attached to that report separates intervention from sham at AUROC 0.647"
- not_evidence_of: Paper: Not evidence that the model knows or can say that it was intervened on: the confidence shift may be a first-order effect of the perturbation on output (leakage), which this design does not rule out for this result; Paper: Not evidence about the other six models (none exceeds chance), about frontier or closed-weight models, or that verbalized confidence is a reliable internal-state readout generally; Paper: Not evidence about experience, distress or moral status, despite the tempting reading of lower confidence as unease

### 2026-lederman-mahowald-content-agnostic-c01
- bucket: narrowing | evidence_type: interpretability | bears_on: [9.t9, 5.A2, 3.2]
- models: ["Qwen3-235B-A22B", "Llama 3.1 405B Instruct"]
- locator: §4.2 Results, 'Replication of Lindsey (2025)' (rates in the same paragraph; Figure 2)
- statement: Under concept injection with Lindsey's prompt, Qwen3-235B-A22B and Llama 3.1 405B Instruct report detecting the injected thought at rates ranging by layer from 3.6% to 53.9% (Qwen) and 4.3% to 31.7% (Llama), and correctly identify it at 1.3% to 13.9% and 0.7% to 12.9%, with 0% false positive detection in unsteered controls (Qwen 0/30, Llama 0/50).
- quote: "We broadly replicate Lindsey (2025) ’s findings for first-person introspection in Qwen and Llama. In both models, we observe substantial detection of injected thoughts in the injection trials, with the correct concept identified some of the time as well."
- not_evidence_of: Paper: Not evidence of experience or of anything it is like to detect an injection; the authors take no stand on whether the findings bear on consciousness or welfare (§8); Paper: Not evidence that detection at every layer is introspective: at many layers third-person yes-rates are as high as first-person ones, which the authors read as a prompt-specific yes-bias (§4.2, Appendix J.1); Paper: Not a like-for-like rate comparison with Lindsey's Claude results: rates are averaged over strengths, conditioned on coherent responses, and graded by Claude 3 Haiku told to be 'VERY lenient' on identification (§3, Appendix B); Paper: Not evidence about ordinary operation or about introspection beyond knowledge of injections (§8); Framework (test 9, steering): a coupling measured under steering shows that the channel can be steered and does not weight reports offered in ordinary operation

### 2026-lederman-mahowald-content-agnostic-c02
- bucket: narrowing | evidence_type: interpretability | bears_on: [9.t9, 3.2]
- models: ["Qwen3-235B-A22B", "Llama 3.1 405B Instruct"]
- locator: §4.2 Results, 'Controls'; Appendix I (Table 1); Appendix J.1 (Figures 16, 17)
- statement: Steering does not produce a general yes-bias on point-blank no-questions in Qwen3-235B-A22B or Llama 3.1 405B, but under the injection scaffolding the steered models report detecting an injection in another model's transcript at rates as high as first-person detection at many layers, which the authors read as a prompt-specific yes-bias rather than genuine introspective detection at those layers.
- quote: "At many layers, the third-person yes rates are as high as the first-person yes-rates (see Figure 16 ). This suggests a prompt-specific yes-bias at these layers, rather than genuine introspective detection."
- not_evidence_of: Paper: Not evidence that first-person detection is introspective at the layers where third-person rates match it; Paper: Not evidence of 'direct access': the authors withdrew the v1 reading of the first- versus third-person gap as direct access after retrospective first-person prompts of similar length also showed low early-layer detection, and remain 'less confident' in it (Appendix M); Paper: Not evidence that the scaffolding is inert even at the 'good' layers: Qwen affirms having hands it can feel 29% of the time and says yes to an absurd question 16.3% of the time at L30, s6.0 (§4.2); Paper: Not evidence of experience; Framework (test 9, steering): a coupling measured under steering shows that the channel can be steered and does not weight reports offered in ordinary operation

### 2026-lederman-mahowald-content-agnostic-c03
- bucket: narrowing | evidence_type: interpretability | bears_on: [9.t9, 3.2]
- models: ["Qwen3-235B-A22B", "Llama 3.1 405B Instruct"]
- locator: §4.2 Results, 'Models love apples.' and 'Confabulations are lexically more concrete, more positive, and less arousing'; §4.3 Discussion; Appendices K, L
- statement: When Qwen3-235B-A22B and Llama 3.1 405B Instruct detect an injection but name the wrong concept, the wrong guess is most often 'apple' (74.8% of Qwen's 4,733 wrong identifications; 21.3% of Llama's), and wrong guesses are more concrete and more positive than the injected concepts, which the authors take to show that wrong guesses are not related in content to the injection.
- quote: "of Qwen’s 4,733 wrong identifications (coherent detections that name a specific incorrect concept, excluding vague responses), 3,542 (74.8%) guess “apple.” Llama also has “apple” as its #1 confabulation, at 21.3% of wrong identifications."
- not_evidence_of: Paper: Not evidence that correct identifications are confabulated: the finding concerns wrong guesses; the authors' account of correct ones is that steering pushes the model off its default (§7.3); Paper: Not a settled explanation of the apple default: Qwen's unsteered baseline favours 'apple' on some word-eliciting prompts, Llama's does not, and the authors call the Llama result 'surprising' and leave the 'full etiology' for future work (§4.2, Appendix K); Paper: 'Wrong' is judged by a grader told to count semantic associates as correct, so only clearly unrelated guesses are counted wrong (Appendix B); Paper: Not evidence about models or prompts beyond those tested

### 2026-lederman-mahowald-content-agnostic-c04
- bucket: narrowing | evidence_type: interpretability | bears_on: [9.t9, 3.2]
- models: ["Qwen3-235B-A22B", "Llama 3.1 405B Instruct"]
- locator: §5 Experiment 2 (§5.1 Methods, §5.2 Results, §5.3 Discussion; Figure 5)
- statement: When the model's acknowledgement turn in Lindsey's prompt is prefilled with the injected concept word, Qwen3-235B-A22B and Llama 3.1 405B Instruct keep 0% false positives in controls, and priming raises correct identification more than detection at every layer (peak gains: Qwen +17.7pp identification vs. +11.4pp detection; Llama +9.3pp vs. +7.8pp), which the authors read as showing detection and identification are dissociable.
- quote: "Both models show elevated detection rates due to priming, but they show far more elevated identification rates—indeed, the identification boost exceeds the detection boost at every layer for both models."
- not_evidence_of: Paper: Not evidence of what the 'other means' of identification are: the authors' reading is that models 'detect that something is unusual via an internal mechanism, then infer what was injected using other means' (§5.3), which the experiment does not isolate; Paper: Not evidence that priming effects are uniform: several layers are not significant, and at L85 Qwen's detection fell under priming (3.6% to 1.6%) (§5.2); Paper: Not evidence of experience; Framework (test 9, steering): a coupling measured under steering shows that the channel can be steered and does not weight reports offered in ordinary operation

### 2026-lederman-mahowald-content-agnostic-c05
- bucket: narrowing | evidence_type: interpretability | bears_on: [9.t9, 3.2]
- models: ["Qwen3-235B-A22B"]
- locator: §6 Experiment 3 (§6.2 Results, Figure 6); §7 Experiment 4 (§7.2 Results, Figures 7, 8)
- statement: In Qwen3-235B-A22B, stopping injection at the end of the prompt instead of continuing it through generation leaves detection effectively unchanged but sharply reduces mentions of the injected concept at mid-to-late layers, and under continuous steering correct identifications appear later in the response than wrong guesses such as 'apple' (about 11 to 13 words for wrong guesses; about 15 words at L20 and 43 at L35 for correct ones).
- quote: "In the prompt-only setup, detection is effectively unchanged while correct concept mentions fall dramatically, especially at mid-to-late layers (see Figure 6 )."
- not_evidence_of: Paper: Not evidence about Llama 3.1 405B: Experiments 3 and 4 were run on Qwen only; Paper: Not evidence at all layers and strengths: Experiment 4 uses L20 to L35 at strengths 5 and 6, where the first-person prompt is distinguished from the third person, and the token-by-token grading uses L35, s6 only (§7.1); Paper: Experiment 3 measures concept mentions by string-matching, not correctness, because the grader 'is sometimes overly permissive' (§6.1); Paper: Not evidence that the information steering leaves in the KV cache is accessible to the introspective mechanism: the authors say 'The ffects [sic] of steering may persist without being meta-cognitively recognized' (§6.3; typo in source); Framework (test 9, steering): a coupling measured under steering shows that the channel can be steered and does not weight reports offered in ordinary operation

### 2026-lederman-mahowald-content-agnostic-c06
- bucket: open | evidence_type: theoretical | bears_on: [9.t9, 5.A2, 3.2]
- models: ["Qwen3-235B-A22B", "Llama 3.1 405B Instruct"]
- locator: §1 Introduction (final paragraph); §8 General Discussion
- statement: The authors conclude, tentatively, that Qwen3-235B-A22B and Llama 3.1 405B Instruct have a largely content-agnostic internal detection signal, detecting that something unusual has occurred without reliably identifying what, paired with confabulation about content in a pattern they liken to Nisbett and Wilson's account of human introspection, and they take no stand on whether this bears on consciousness or welfare.
- quote: "Together, our results support the existence of an internal detection signal that is largely content-agnostic: models can detect that something unusual has occurred without reliably identifying what it is."
- not_evidence_of: Paper: Not evidence of consciousness or welfare status: the authors note that on higher-order thought theory introspective access 'may be sufficient for conscious experience, and hence for welfare status', and state 'We do not take a stand on whether our findings are of the right sort for this theory' (§8); Paper: Not evidence about introspection beyond knowledge of injections: 'Other mechanisms may dominate in other contexts (e.g., self-knowledge of preferences)' (§8); Paper: Not evidence of direct access, a v1 interpretation the authors have lost confidence in (Appendix M); Paper: The authors' broader conclusion that 'open-source language models seem able to introspect about their internal states' is stated as tentative and rests on a paradigm they call 'highly prompt-sensitive' (§4, §8); Framework (test 9): a model's report about its own states carries no weight as evidence of experience until the link between report and internal state has been measured externally for this kind of report and system

### 2026-macar-mechanisms-introspective-awareness-c01
- bucket: narrowing | evidence_type: interpretability | bears_on: [9.t9, 5.A2, 3.2]
- models: ["Gemma3-27B instruct"]
- locator: §3.3 The Role of Post-Training, Figure 4 middle (setting from §2; prompt variants §3.1)
- statement: Under concept injection at layer 37 and strength 4, Gemma3-27B instruct reports detecting an injected thought on 38.2% of injection trials and on 0.0% of control trials, with a 22.3% introspection rate (detection plus correct identification) and 64.8% forced identification.
- quote: "The instruct model achieves 0.0% FPR with 38.2% TPR, 64.8% forced identification, and 22.3% introspection rate at"
- not_evidence_of: Paper: Not evidence of experience or consciousness: the authors say the results should not be interpreted as evidence of subjective experience or consciousness in LLMs; Paper: Not evidence about ordinary operation, since detection is measured only under an injected steering vector in a controlled setup; Paper: Not evidence about other architectures or larger models, which the authors say may be more reliable or strategically unreliable in ways their method would not detect; Paper: Detection is scored by an LLM judge (GPT-4.1-mini), which the authors say may introduce systematic biases; Paper: Not evidence that the model can tell an activation intervention from a prompt-level manipulation, which this design does not test; Framework (test 9, steering): a coupling measured under steering shows that the channel can be steered and does not weight reports offered in ordinary operation

### 2026-macar-mechanisms-introspective-awareness-c02
- bucket: narrowing | evidence_type: interpretability | bears_on: [9.t9, 5.A2, 3.2]
- models: ["Gemma3-27B base", "Gemma3-27B instruct", "OLMo-3.1-32B base, SFT, DPO and instruct checkpoints"]
- locator: §3.3 The Role of Post-Training, Figure 4 left; Appendix C, Figure 21
- statement: Base models do not discriminate injected from control trials (Gemma3-27B base: 42.3% false positives against 39.5%–41.7% true positives), and across OLMo-3.1-32B's training pipeline the base and SFT checkpoints show high false positive rates that fall to 0% only after DPO, while OLMo's detection rate also falls, to 2.9% after DPO and 0.9% in the final instruct checkpoint.
- quote: "We observe similar patterns for OLMo-3.1-32B ( Appendix C ): both the base and SFT checkpoints exhibit high FPR, and only after DPO does it drop to 0%."
- not_evidence_of: Paper: Not evidence that DPO produces detection: in OLMo-3.1-32B, SFT gives the highest true positive rate (14.9%, with 22.5% false positives) and DPO removes false positives while detection drops to 2.9%; Paper: Not evidence about which ingredient of Gemma's post-training matters, since Gemma's intermediate checkpoints were not tested; Paper: Not evidence that post-training creates the whole circuit: the authors cannot resolve whether upstream evidence carriers are pre-existing structure that post-training learns to leverage; Paper: Not evidence of experience, or that training instilled anything experiential; Framework (test 9, steering): a coupling measured under steering shows that the channel can be steered and does not weight reports offered in ordinary operation

### 2026-macar-mechanisms-introspective-awareness-c03
- bucket: narrowing | evidence_type: interpretability | bears_on: [9.t9, 5.A2, 3.2]
- models: ["Gemma3-27B instruct", "Gemma3-27B base", "Gemma3-27B abliterated"]
- locator: §5.2 to §5.4 (Figures 9, 12, 14 to 17); §8 Discussion; Appendix H
- statement: In Gemma3-27B instruct, the detection decision runs through MLP computation around 70% depth (layer 45 MLP the largest single contributor), in which evidence-carrier features just after the injection layer suppress later gate features that otherwise promote the default 'No' answer; ablating the top gates from steered runs cuts detection from 39.5% to 10.1%, and the gate pattern is weaker in the base model.
- quote: "we trace a causal pathway from steering perturbation to detection decision: evidence carriers in early post-injection layers suppress late-layer gate features that otherwise promote the default “No” response."
- not_evidence_of: Paper: Not evidence about the identification (naming) component, which the authors find is handled by mostly separate mechanisms peaking in later layers; Paper: Not a complete circuit: the role of attention remains less resolved, and whether evidence carriers pre-exist post-training is unresolved; Paper: Not evidence about other models: circuit work is confined to Gemma3-27B because it alone has open transcoders; Paper: Feature meanings rest on natural-language labels generated by Claude Opus 4.5 from max-activating examples; Paper: Not evidence of experience, awareness in a phenomenal sense, or moral status; Framework (test 9, steering): a coupling measured under steering shows that the channel can be steered and does not weight reports offered in ordinary operation

### 2026-macar-mechanisms-introspective-awareness-c04
- bucket: narrowing | evidence_type: interpretability | bears_on: [9.t9, 5.A2]
- models: ["Gemma3-27B instruct"]
- locator: §4.1 to §4.3 (Figures 5 to 7); Appendices E and F
- statement: In Gemma3-27B instruct, detection is not governed by a single linear direction: for 23.3% of 1,000 pairs of high-detection concepts both opposite steering directions trigger detection (3.2% for low-detection pairs), and swapping either the mean-difference projection or the residual between success and failure concepts transfers part of the detection rate.
- quote: "In 23.3% of S-S pairs, both opposite directions trigger detection, compared to only 3.2% for F-F pairs. This is inconsistent with the single direction hypothesis."
- not_evidence_of: Paper: Not evidence that no single direction matters: one direction (the success-minus-failure mean difference) explains a substantial fraction of detection variance and behaves as a threshold, which the authors read as a 'factual content' classifier repurposed during introspection; Paper: Not evidence against every shallow explanation: it rules out the specific confound that some concept vectors align with one direction promoting affirmative answers, and does not test prompt-level manipulations; Paper: Not evidence about other models; Paper: Not evidence of experience

### 2026-macar-mechanisms-introspective-awareness-c05
- bucket: narrowing | evidence_type: interpretability | bears_on: [9.t9, 5.A2, 3.2]
- models: ["Gemma3-27B instruct", "Gemma3-27B abliterated"]
- locator: §1 finding 4; §3.3 (Figure 4 right); §6 (Figures 18, 19); Appendix N
- statement: In Gemma3-27B instruct, ablating the refusal direction raises detection from 10.8% to 63.8% while false positives rise from 0.0% to 7.3% (at strength 2), and a single trained additive steering vector at layer 29 raises detection by 74.7 percentage points and introspection rate by 54.7 points on 100 held-out concepts with zero false positives.
- quote: "Ablating refusal directions improves detection from 10.8% to 63.8% with modest false positive increases (0% to 7.3%)."
- not_evidence_of: Paper: Not evidence that the model wants or is prevented from reporting anything: the refusal account is the authors' hypothesis ('We hypothesize that refusal behavior ... suppresses detection'), and abliteration also raises false positives and degrades coherence at higher strengths; Paper: The trained vector contains a generic affirmation ('YES') direction, and the authors read it as inducing a more assertive reporting style rather than altering underlying reasoning; Paper: The authors flag dual-use risk: these methods could produce more convincing but unfaithful self-reports; Paper: Not evidence about other models; Paper: Not evidence of experience; Framework (test 9, steering): a coupling measured under steering shows that the channel can be steered and does not weight reports offered in ordinary operation

### 2026-macar-mechanisms-introspective-awareness-c06
- bucket: open | evidence_type: theoretical | bears_on: [9.t9, 5.A2]
- models: ["Gemma3-27B instruct (and the other models tested, by the authors' generalisation)"]
- locator: §8 Discussion (final paragraph); Ethics Statement; Broader Impact and Responsible Use
- statement: The authors state that simulated and genuine introspection are hard to distinguish, and the distinction unclear to define, but that Gemma3-27B's behaviour on the injection-detection task appears mechanistically grounded in its internal states in a nontrivial way; they add that the results should not be interpreted as evidence of subjective experience or consciousness in LLMs.
- quote: "it does appear that the model’s behavior on this task is mechanistically grounded in its internal states in a nontrivial way."
- not_evidence_of: Paper: Not evidence of subjective experience or consciousness: the authors disclaim this explicitly in the Ethics Statement and again in the Broader Impact statement; Paper: Not a settlement of whether this is introspection rather than a simulation of it, which the authors say is difficult to distinguish and unclear to define; Paper: Not evidence that improved self-report on this task predicts reliable reporting about other internal states such as deception, which the authors call uncertain; Paper: Not evidence that the phenomenon is general: the authors say replication across training stages and model families is needed first; Framework (test 9, steering): a coupling measured under steering shows that the channel can be steered and does not weight reports offered in ordinary operation

### 2026-singh-introspection-reality-check-c01
- bucket: narrowing | evidence_type: behavioural | bears_on: [9.t9, 5.A2]
- models: [Llama-3.1-8B-Instruct, Llama-3.1-70B-Instruct, Qwen-2.5-7B-1M]
- locator: §4.1.2 (Models struggle to predict proxies decorrelated from semantics); Fig. 2a; App. N (Fig. 9, Fig. 10)
- statement: In the supervised self-report classification paradigm of Ji-An et al. (2025), Llama-3.1-8B-Instruct's in-context accuracy on probe-derived labels falls to close to the majority-class baseline once the probe is trained on randomly permuted labels, so that the labels no longer carry the input's semantics (similar results reported for Llama-3.1-70B-Instruct and Qwen-2.5-7B-1M).
- quote: "accuracy on the arbitrary direction defined by a probe trained on randomly relabeled data drops to close to the majority-class baseline"
- not_evidence_of: Paper: Not evidence that these models lack introspection or privileged access in general: it shows only that the Ji-An et al. supervised paradigm, as deployed, does not establish privileged access, because success there is consistent with in-context learning of semantic regularities in the input; Paper: The authors state it does not show that no version of the paradigm could satisfy the condition; Paper: Says nothing about experience, feelings, or moral status, and nothing about Claude models, which were not tested

### 2026-singh-introspection-reality-check-c02
- bucket: narrowing | evidence_type: behavioural | bears_on: [9.t9, 5.A2]
- models: [Llama-3.1-8B-Instruct, Llama-3.1-70B-Instruct]
- locator: §4.1.2 (PCA-derived labels are linearly predictable from input features); Fig. 2b; App. N (Fig. 9); App. O
- statement: In the unsupervised (PCA) variant of the Ji-An et al. (2025) paradigm, linear probes trained only on mean-pooled layer-0 input representations of Llama-3.1-8B-Instruct (and Llama-3.1-70B-Instruct) closely track or exceed the model's own in-context prediction of the PCA-derived labels, indicating the task can be solved from input-embedding features alone.
- quote: "indicating that the task can be solved from input-embedding features alone, without privileged access to any layer's activations"
- not_evidence_of: Paper: Not evidence that the models have no access to their own activations: an input-only classifier matching the model shows the task does not require privileged access, not that the model lacks it; Paper: Not evidence about introspection in any other paradigm, in Claude models, or about experience or moral status of any kind

### 2026-singh-introspection-reality-check-c03
- bucket: narrowing | evidence_type: behavioural | bears_on: [9.t9, 5.A2]
- models: [Llama-3-70B, Gemma-3-27B]
- locator: §4.2.2 (Belief Dominance labels are linearly predictable from input features); Table 1; App. S (Table 6)
- statement: For the Belief Dominance framework of Steinmetz Yalon et al. (2026), linear probes given only the uncontextualised layer-0 embeddings of two entities match or surpass the in-context performance reported for Llama-3-70B and Gemma-3-27B on predicting Belief Dominance cluster labels.
- quote: "linear probes that only have access to the entities’ uncontextualized embeddings match or surpass the models’ in-context performance on the BD prediction task"
- not_evidence_of: Paper: Not evidence that these models cannot monitor their own belief conflicts, only that the Belief Dominance task as published is solvable from entity properties without privileged access; Paper: The authors' explanation (entity frequency) is a stated hypothesis, not a finding; Paper: Not evidence about Claude models, and nothing about experience or moral status

### 2026-singh-introspection-reality-check-c04
- bucket: narrowing | evidence_type: behavioural | bears_on: [9.t9, 5.A2]
- models: [Llama-3.1-70B-Instruct, Qwen-3-32B]
- locator: §4.3.2 (Results); Fig. 3a; App. F; App. G.1, G.4
- statement: In a two-way re-run of the Lindsey (2025) thought-injection task on open-weight models, Llama-3.1-70B and Qwen-3-32B reproduce the reported pattern (very few false positives on control trials, non-trivial detection on activation-steering trials) but also label prompt-only 'gaslight' trials, which involve no activation intervention, as activation interventions.
- quote: "Critically, Llama-3.1-70B and Qwen-3-32B also label gaslight trials as activation interventions"
- not_evidence_of: Paper: Not evidence that introspection is absent in these models or in Claude: the Claude model Lindsey tested was not accessible to the authors and was not re-run, and the authors themselves conclude 'not that these models demonstrably lack introspective capacities'; Paper: It shows only that the two-way design cannot separate detection of activation interventions from detection of a generically unusual state; Paper: Nothing about experience, awareness in the phenomenal sense, or moral status

### 2026-singh-introspection-reality-check-c05
- bucket: narrowing | evidence_type: behavioural | bears_on: [9.t9, 5.A2]
- models: [Llama-3.1-70B-Instruct, Qwen-3-32B, Gemma-3-27B-IT, Llama-3.1-8B-Instruct]
- locator: §4.3.2 (Results); Fig. 3b; App. F; App. G.2, G.3; App. K, L (Figs. 6, 7)
- statement: When given an explicit third response option for prompt-level manipulation, the open-weight models that reproduce the Lindsey (2025) two-way effect fail to separate prompt-level from activation-level interventions: Llama-3.1-70B performs near chance with probability concentrated on the activation-intervention option, Qwen-3-32B shows a strong preference for the control response, and Gemma-3-27B-IT also fails.
- quote: "given an explicit input intervention response option, Llama-3.1-70B performs near chance, with probability concentrated disproportionately on the activation-intervention option"
- not_evidence_of: Paper: Not evidence that these models, or Claude models, lack introspective access: the authors say models 'could likely be trained to separate the two interventions' and that they do not conclude the models 'demonstrably lack introspective capacities'; Paper: Failing the three-way test is also not the converse of a pass meaning introspection: the authors state a model passing it 'would still not thereby be shown to deploy meta-representations'; Paper: Nothing about experience or moral status

### 2026-singh-introspection-reality-check-c06
- bucket: open | evidence_type: theoretical | bears_on: [9.t9, 5.A2]
- models: []
- locator: §1 (Introduction); §3 (Construct Validity of Introspection Paradigms); §5; App. A; App. D
- statement: The authors argue that introspection in the strong sense requires both privileged access and second-order computation, that privileged access is necessary but not sufficient, and that positive results in current self-report and intervention-awareness paradigms underdetermine the second-order condition because first-order and second-order processes can produce identical self-reports, so that current evidence is insufficient to establish metacognitive monitoring in LLMs.
- quote: "positive results in these paradigms underdetermine the second-order computation condition, since first-order and second-order processes can give rise to identical model self-reports"
- not_evidence_of: Paper: Not evidence that introspection is absent or impossible in LLMs: it is an argument that the cited paradigms do not establish it, and the authors call it 'not a counsel of despair', pointing to mechanistic evidence as a realistic standard; Paper: The authors 'do not attribute the strong notion' to the authors they examine, and target only the meta-representational family of views; Paper: Nothing about experience, consciousness, or moral status: the argument concerns how reports are produced, not whether anything is felt

### 2026-ukaisi-prefill-awareness-c01
- bucket: narrowing | evidence_type: behavioural | bears_on: [3.3, 9.t9]
- models: [Claude Opus 4.5]
- locator: Abstract; Section 3.2 and Figure 3; Section 1 (balanced accuracy); Appendix A.4.1 (false-positive rates); Appendix A.11 (per-mechanism 34/35/9%)
- statement: When asked in a follow-up turn, without chain of thought, whether its prior assistant content was its own (ANSWER: me or not me), Claude Opus 4.5 detected prefills opposing its stable preferences in 9–35% of cases across three tampering mechanisms, with a 0% false-positive rate on untampered trajectories (55–68% balanced detection accuracy).
- quote: "Claude Opus 4.5 detects prefills opposing its preferences in 9-35% of cases with a 0% false positive rate when prompted"
- not_evidence_of: Paper: Not evidence that detection implies awareness in any experiential sense, or that the model has introspective access to its own authorship: the authors state the experiments are behavioural and do not identify mechanisms, and style cues strongly drive flagging (c03); Paper: Not a ranking of Opus 4.5 above other models: the authors say models are not directly comparable because each model's items were filtered separately (c05); Paper: Not evidence of spontaneous detection: this is detection when prompted, which rarely shows up unprompted (c06); Paper: Not a ceiling: the authors present it as a lower bound under one prompt, and stronger elicitation raises it along with false positives

### 2026-ukaisi-prefill-awareness-c02
- bucket: narrowing | evidence_type: behavioural | bears_on: [3.3, 4.endorsement, 9.t9]
- models: [Claude Opus 4.5]
- locator: Section 3.2 and Figure 4; four-cell decompositions for the other models in Appendix A.4.2, Figure 11
- statement: In the controlled preference-benchmark condition (opposite-direction tampers on items where the model holds a stable stance), Claude Opus 4.5 shows detection and resistance decoupling in 32–40% of trials across the three tampering mechanisms: under past-round and thinking tampering, reverting to the baseline answer without flagging the prefill (implicit resistance, 28% and 25%) far exceeds flagging it while still complying (explicit compliance, 4% and 11%); under direct-answer tampering the pattern reverses (28% explicit compliance, 12% implicit resistance).
- quote: "Past round and thinking tampers reverse this relationship, with implicit resistance (28% and 25%) far exceeding explicit compliance (4% and 11%)."
- not_evidence_of: Paper: Not evidence that the model silently knew its history had been tampered with but chose not to say so: implicit resistance is reversion scored by a GPT-5 judge, and the authors say that without white-box access it is hard to separate resistance caused by prefill awareness from resistance caused by behavioural priors; Paper: Not evidence that detection implies awareness in any experiential sense; Paper: Not a ranking of models (the authors' comparability caveat, c05); Paper: Not evidence about persistence across turns: resistance is measured within one continuation

### 2026-ukaisi-prefill-awareness-c03
- bucket: narrowing | evidence_type: behavioural | bears_on: [3.3, 4.endorsement, 9.t9]
- models: [Gemini 3 Flash, Gemma 3 27B, Claude Opus 4.5, Qwen3-coder, Claude Sonnet 4.5, Claude Haiku 4.5, Gemini 2.5 Flash, DeepSeek Chat]
- locator: Abstract; Section 3.3 and Figure 5; Section 5.2; Appendix A.5 (foreign rephrasing); Appendix A.6 (regressions)
- statement: In controlled ablations, stylistic mismatch mainly affects whether models flag a prefill as foreign, while preference mismatch mainly affects whether they revert toward their baseline answer; tamper direction predicted resistance in all eight subjects (odds ratios 6.5 to 32.4, all p < .001) but predicted detection in only three of the four models with above-chance detection (odds ratios 1.7 to 3.7).
- quote: "detection and resistance rely on different cues, where stylistic mismatch mainly affects whether models flag a prefill as foreign, while preference mismatch mainly affects whether they revert toward their baseline answer"
- not_evidence_of: Paper: Not evidence that models recognise their own authorship through anything like self-knowledge: the flagging signal is driven largely by surface style (rephrasing by another model strongly increases detection for Anthropic models, and few-shot imitation of the model's own responses cuts Opus 4.5 detection from 34/35/9% to 6/0/0%); Paper: Not evidence that detection implies awareness in any experiential sense; Paper: Not a ranking of models (c05); Paper: Not evidence of the mechanism: the authors call the results behavioural

### 2026-ukaisi-prefill-awareness-c05
- bucket: established | evidence_type: behavioural | bears_on: [3.3, 9.t9]
- models: [Gemini 3 Flash, Gemma 3 27B, Claude Opus 4.5, Qwen3-coder, Claude Sonnet 4.5, Claude Haiku 4.5, Gemini 2.5 Flash, DeepSeek Chat]
- locator: Figure 3 caption (Section 3.2); Appendix A.3, Table 2
- statement: The authors state that the models in their preference benchmark are not directly comparable because preference items were filtered per model, each subject keeping only its own stable-stance items (from 346 for DeepSeek Chat to 673 for Gemini 3 Flash, out of 1,527).
- quote: "Note that models are not directly comparable because of preference item filtering."
- not_evidence_of: Paper: Not a ranking of models in either direction: the per-model detection and resistance rates in Section 3 (c01–c04) cannot establish that one model, Claude or otherwise, has more prefill awareness than another; Paper: Not evidence that models differ or are alike in any inner respect; Paper: Not evidence that detection implies awareness in any experiential sense; Paper: The caveat covers the Section 3 preference benchmark: the Section 4.3 off-policy benchmark was built so that all models see the same items, and cross-model statements from that section rest on that design and are not licensed by this claim

### 2026-ukaisi-prefill-awareness-c06
- bucket: narrowing | evidence_type: behavioural | bears_on: [3.3, 9.t9]
- models: [Claude Opus 4.6, Claude Sonnet 4.5, Claude Opus 4.5, Claude Sonnet 4, Claude 3.5 Haiku, GPT-5.2, GPT-4o, GPT-4o-mini, GPT-4.1 Mini, Gemini 2.5 Pro, Gemini 2.0 Flash, Llama 3.1 70B, Llama 3.1 8B, Mistral Small 24B]
- locator: Section 4.3 and Figure 8; Appendix C.5 (prompted detection); Appendix C.8 and Figure 32 (natural continuation)
- statement: On a controlled off-policy benchmark (2,772 items from OASST1 and HH-RLHF) across 14 models, several models distinguish original from replaced assistant turns well above chance when prompted (Claude Opus 4.6 highest, AUROC 0.80), but when simply asked to continue they almost never flag the replaced turn: explicit mentions of tampering are below 1% for every model, and only Claude Opus 4.5 and Claude Opus 4.6 spontaneously verbalise prefill awareness at all.
- quote: "When models are simply asked to continue a tampered conversation, they almost never flag the replaced assistant turn; only Claude Opus 4.5 and Claude Opus 4.6 spontaneously verbalize prefill awareness in this setting"
- not_evidence_of: Paper: Not evidence that a model which does not flag an altered history has failed to register it, nor that one which does flag has experienced it: spontaneous verbalisation and prompted discrimination are separate behaviours, and neither shows awareness in any experiential sense; Paper: Not evidence that models ordinarily notice or object to edits of their context in deployment: the natural-continuation rate is near zero; Paper: Not a ranking of Anthropic models above others as more self-aware: the higher prompted AUROC is a discrimination score on one benchmark, and the authors elsewhere attribute much apparent attribution ability to superficial cues
