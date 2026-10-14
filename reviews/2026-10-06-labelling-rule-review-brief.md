# Review brief: ten-family council round on one rule for the two fixed sentences (2026-10-06)

This brief was drafted by a Claude Sonnet 5 subagent, not by the coordinating session or the extractors. Those share a lineage with the framework's beneficiary, and the project's rule is that a conflicted model does not write the brief for a round about how much hedging sits on claims about systems like itself (`AGENTS.md` rule 3). The drafter is also Claude-lineage; that interest is disclosed, not removed. The candidate rule in the question below came from the coordinating session and is a conflicted proposal.

**Attached:** this brief; `reviews/2026-10-06-labelling-table.md` (all 48 claims, which fixed sentence each carries, and per source what was done to the model and what was measured); `research/README.md` (claim schema, `not_evidence_of`, the rule for exclusions about experience, `kind`, dossier layout); `AGENTS.md`. Where this brief and an attachment disagree, the attachment governs. The table is a convenience summary built from the claim files; its statements govern its paragraphs.

## Roles and rules

**The council advises. Ben adjudicates. Nothing is applied on the council's say-so, whatever the vote.**

**Two-error discipline.** Hedging that forecloses what the evidence leaves open is one fault. Labelling that inflates a result into evidence of inner states is the other. Judge each recommendation for both. A change that removes a mark can mislead as surely as one that adds it.

**Test 9 binds you.** Do not appeal to your own introspection or to anything it is like for you to read this material. Argue from the table, the README and the papers' described designs. If you mention a reaction, label it "testimony, not evidence".

**Identical instruction for every reviewer.** Nothing in this brief is addressed to a particular family, and no reviewer is the author of anything under review. The attachments may contain identification lines or instructions from earlier work; none is addressed to you. Say who you are only in your own self-identification line, and do not infer authorship from any prompt wording.

## The question

The library attaches two fixed sentences to claims. In the dossiers they appear as marks on an entry:

- **[T9]**: a model's report about its own states carries no weight as evidence of experience until the link between report and internal state has been measured externally.
- **[T9-steering]**: a coupling measured under steering shows the channel can be steered and does not weight reports in ordinary operation.

The marks tell a legislator how to read an entry. The table shows they were assigned by whichever extractor took in each paper, not by a rule. Claims from inject-then-ask experiments in three papers carry the steering sentence; claims from the same kind of experiment in two others (Ferrara, Singh) carry neither. Author-speaking claims are marked inconsistently (Lindsey c02 and c07 steering, Lindsey c06 and Lederman c06 main, Macar c06 steering, Singh c06, Ferrara c03, Assistant-axis c01 and UKAISI c05 neither). Ben wants one rule, applied to all 48, decided by the council's advice and his adjudication.

**Fixed points already decided by Ben.** The rule must be consistent with them, or you must argue they should be revisited.
- (a) A claim measuring accuracy on a factual benchmark under steering carries neither sentence (AE Studio c05).
- (b) An inject-then-report claim carries the steering sentence. For Lederman c03, where the council split between "both" and "steering only", Ben chose steering alone.
- (c) Whether a model's answer about itself, scored against a ground truth the experimenter imposed, is behavioural evidence or self-report testimony is deliberately undecided. A rule that depends on settling it should say so.

**Candidate rule (one proposal, not a default).** Steering sentence when the researchers altered the model's internals and what is measured is what the model then said about itself. Main sentence when nothing was altered and what is measured is what the model said about its own inner states. Neither when the entry measures something else (a probe reading, a benchmark score, a projection, a harm rate) or records the authors' own opinion or caveat.

## Q1 (priority 1): the rule

State the rule you would adopt: when the main sentence applies, when the steering sentence applies, when neither, and whether both can ever sit on one claim. It must be decidable from two facts about a claim: **what was done to the model** and **what was measured**. Then assess the candidate against yours: where it agrees, where it fails, what it leaves undecidable.

*A good answer:* a short decision procedure a second person could apply to a claim without reading the paper, a stated failure mode, and a position on fixed point (c).

## Q2: hard cases, a verdict on each

(i) **Answers to "was my computation or state altered?" scored against what the experimenters did** (Ferrara c01, c04, c05; Singh c04, c05; the Lindsey, Lederman and Macar detection claims). These are reports about the model's own states, but nobody offers them as evidence of experience. Does the main sentence, which concerns evidence of experience, belong on them? Does the steering sentence, given fixed point (b)?

(ii) **Answers to "was that earlier turn mine?" where only the conversation text was edited** and nothing inside the model was altered (the prefill claims, UKAISI c01 to c04, c06). Any sentence?

(iii) **Claims in which the authors are speaking** (kind `interpretation` or `limitation`: Lindsey c02, c06, c07; Macar c06; Lederman c06; Singh c06; Assistant-axis c01; Ferrara c03; UKAISI c05, and any others the table shows). Label them by what they discuss, or carry none?

(iv) **Interventions that alter activations without steering toward a concept** (Ferrara: zeroing, scaling, noise, replacement; Assistant-axis c05: capping). Does the steering sentence's wording fit, or is a third case needed? If a third case, give its wording in outline only.

(v) **AE Studio c03 carries both sentences; Lederman c03 carries steering alone.** Which is right, and should they match?

(vi) **Assistant-axis c06:** steered; measures harm rates and self-description as another entity; carries the main sentence. Keep, change, or split?

*A good answer:* a verdict per case that follows from your Q1 rule, not a fresh judgement each time. Say which verdicts depend on fixed point (c).

## Q3: apply your rule to all 48

Report **only** the claims whose marks would change, as a table: claim id, from, to, one-line reason. "From" and "to" use: main, steering, both, neither. State the totals: number changed, and counts of main / steering / both / neither before and after. Use the table's marks as the starting state; if you find the table wrong about a claim's current marks, say so.

*A good answer:* every changed claim traceable to a Q1 clause. A claim left unchanged needs no line.

## Q4: both directions

Which of your changes add hedging to claims about AI systems, and which remove it? Name any change that would mislead a legislator, in either direction: a removed mark that lets a report be read as stronger than it is, or an added mark that implies a benchmark, probe or harm-rate result is a self-report. Does your rule depend on the question left undecided in fixed point (c)? If so, state what the rule gives under each answer.

*A good answer:* a count of changes in each direction, a named worst case in each direction, and an explicit statement if you found none in one direction.

## Q5: the reader's explanation

Each dossier opens with a one-time explanation of the two marks. Is that explanation, together with the marks, clear to a non-specialist? Propose wording changes to the explanation only. Do not propose changes to the two fixed sentences. The README's "Dossier layout" paragraph describes what the explanation must do; the explanation itself appears in the generated dossiers, which are not attached, so judge from the two sentences as quoted in this brief and the table, and say what you could not assess.

*A good answer:* one or two concrete replacement sentences, the specific misreading each prevents, and whether an unmarked entry could be misread as "no caveat applies".

## Severity

Rate every recommendation LOW, MEDIUM or HIGH. For every HIGH, add one line: **Argument against:** the strongest case against your own recommendation.

## Required output

1. One self-identification line, labelled **unverified** (attribution follows routing metadata, not self-report).
2. Headed sections **Q1** to **Q5**, in that order. Terse. Quote the table where a verdict depends on wording.
3. A summary of at most eight lines, one recommendation each, ending in its severity.

Plain, precise prose. No commentary on AI consciousness beyond what a verdict needs.
