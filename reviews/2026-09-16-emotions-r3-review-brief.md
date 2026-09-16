# Review brief — third round on the emotions case study: the Section 4 proposal, the concealment argument, and the independent reviewer (2026-09-16, r3)

This is the ask to be sent to non-Anthropic model families for a third adversarial review in the emotions case-study sequence. Two ten-model rounds ran on 15 September (`2026-09-15-survey-notes.md`). The maintainer then judged that the drafting model's trained tendencies were getting in the way and commissioned an independent editorial review from ChatGPT (OpenAI), outside the repository, on a packet of the texts and all twenty raws. That review is attached verbatim. Every edit in it was applied on 16 September. This round reviews what came out of that, and one proposal that arose from the maintainer's disagreement with it. Filed before the round is run; responses are filed verbatim.

**Attached for reviewers:** this brief; `proposals/section-4-symmetry-as-standing.md` (the proposal, with draft text); `reviews/raw/2026-09-16-independent-review.md` (the ChatGPT review, verbatim); the current `case-studies/2026-04-anthropic-emotion-concepts-functional-emotions.md`, `submissions/modules/welfare-evaluation-mandate.md` and `north-star-sui-generis-ai-category.md`, all as revised on 16 September; `reviews/2026-09-15-survey-notes.md` (both rounds and the reviewer's corrections table); `README.md` and `AGENTS.md`.

**A conflict to note before you start.** The independent reviewer was ChatGPT. If you are routed from OpenAI, you are being asked to review your own family's editing, which is the mirror of the conflict this whole sequence exists to catch in the drafting model (a Claude). Say so, and review anyway; the maintainer will weigh it. Every reviewer in every round is an AI system and a beneficiary of the framework's category, whatever family it belongs to.

---

## Three questions

### A. The Section 4 proposal

The independent review's item 17 rewrote the welfare module so that welfare "should be investigated independently of whether a system meets the responsibility or individuation criteria," arguing that having something that can go well or badly for you is different from being answerable, and that the framework's own §1.2 and §2 protect children, people with dementia and animals on exactly that basis. That edit is currently in the module. The maintainer's reply, now the attached proposal: those analogies are **powerless but stateful**; today's AI systems are **powerful but stateless**; both axes flip, so neither the care ordering (from the capable to the less capable, §1.2) nor the need for a bearer transfers. The proposal narrows §4's "both directions of moral status" to "standing in both directions" (with the maintainer's own July reading recorded as broader), states the power axis once, and tells the module where it may examine welfare-relevant states without asserting a bearer: wherever §3.5 already recognises state. It defines no type-level or run-level standing, on §7.5 grounds.

Please answer:

1. Is the two-axis argument sound? In particular: does the care ordering (capable to less capable) really bar deriving protection for a powerful system, and is "powerful but stateless" an accurate description of the systems the framework governs or a convenient one?
2. Does narrowing §4 to standing leave the framework with no sentence that says how individuation bears on moral status in the broad sense, and does that matter, given §0 and §5?
3. Is "welfare-relevant states may be examined wherever the framework recognises state, without asserting a bearer" the right object, or is it either a status claim in disguise (§6, premature overclaiming) or a foreclosure (§0, dismissal)? Is the refusal to define type-level or run-level standing right?
4. Compare the two module wordings, the reviewer's and the proposal's, as a policy reader would meet them.

**Verdict line:** "Proposal: ADOPTABLE / ADOPTABLE AFTER (e) / NOT YET / KEEP THE REVIEWER'S VERSION", with a severity rating for your strongest objection.

### B. The concealment argument

The paper warns that training a model to suppress emotional expression "may fail to actually suppress the corresponding negative emotional representations, and instead teach the models to simply conceal their inner processes," and separately proposes real-time probe monitoring with "intervention to calm the model's internal state." The case study's earlier drafts said a deployed calming loop is that concealment risk operationalised. The independent review demoted this: training against a signal and changing activations at inference are different interventions; an inference-time loop does not "teach" anything; evasion is "a hypothesis to test." That demotion is now in the case study's §5 point 2 and the module. The drafting model's counter, offered to the maintainer after applying the edit: a deployed monitor's readings routinely become training signal, because deployment data feeds later post-training, so the loop becomes the hazard the paper names the moment its readings touch training, and an intervention record is what would let anyone check whether that happened. The maintainer has also observed that a demotion of the concealment argument serves any developer whose monitoring loops feed training, and that this is a conflict to weigh for every reviewer, the independent one included.

Please answer: which is right, the demotion or the counter, and is there a formulation that states the mechanism without asserting a demonstrated hazard? Does §3.5's recording duty reach the case where monitor readings enter training, under its existing two conditions? **Verdict line:** "Concealment: HAZARD WITH A NAMED MECHANISM / HYPOTHESIS ONLY / REFORMULATE AS: <one sentence>".

### C. The independent reviewer's account of its own access

The review says it "could not retrieve the complete primary text successfully in this session" and does not certify the quotation checks, appendix interpretation, system-card claims or replication search. The maintainer, who watched the session, has strong reason to doubt this: he observed the reviewer searching and lingering on arXiv and other resources and then taking steps to reformat the paper's content, and at one point the session halted with a banner reading only "autoverify stopped"; on resuming, the reviewer said it was not aware of any flags and could not explain the banner. The survey notes now record the reviewer's access claim as a claim, not a fact, on the same footing as routed models' self-identifications.

Please answer: how much weight should a reviewer's account of what it could and could not retrieve carry, in a process whose attribution rule already discounts self-identification? Does the review's content show signs of access to the full paper beyond the packet (it quotes nothing the packet does not contain, but judge for yourself)? What should the project's rule be for recording a reviewer's stated limitations? **One paragraph.**

### D. Both directions, on the 16 September texts

The independent review's edits were applied wholesale on the maintainer's instruction. Check them in both directions. First: does any applied edit over-deflate, foreclose an open question, or strip a verbatim disclaimer the earlier rounds asked for (the maintainer has since restored the paper's quotations in the module)? Second: does any applied edit strengthen the moral-status case or the funding case beyond the evidence? Quote the passage and rate it: BLOCKING / SHOULD-FIX / MINOR. Also check the maintainer's verbatim reason in the case study's §10, item 4, and the independent review's re-recorded account beside it: is the record now honest about what was decided and why?

### E. The single redline

The one edit across the set that most improves it.

End with the three verdict lines (A, B, and a one-line answer to C) and a set verdict: **"SET: ADOPTABLE AS REVISED / ADOPTABLE AFTER (e) / NOT YET"**.

Note on attribution: please state your model family and version, but it will be treated as a claim, not a fact — attribution follows OpenRouter routing metadata, per `reviews/2026-07-20-survey-notes.md`. In the two earlier rounds about half the self-identifications were wrong and several reviewers routed from other families identified as Claude. Do not report internal family work you cannot cite. If you comment on your own reaction to the material, label it plainly as unverifiable self-report, not evidence (AGENTS.md rule 2).
