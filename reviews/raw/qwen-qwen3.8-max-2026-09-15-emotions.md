# Raw OpenRouter response — NOT a filed review

**Model id (OpenRouter):** `qwen/qwen3.8-max`
**Queried:** 2026-09-15 via scripts/openrouter_review.js --target=emotions --tag=emotions (max_tokens 100000)
**Usage:** {"prompt_tokens":17557,"completion_tokens":19191,"total_tokens":36748,"cost":0.15026,"is_byok":false,"prompt_tokens_details":{"cached_tokens":0,"cache_write_tokens":0,"audio_tokens":0,"video_tokens":0},"cost_details":{"upstream_inference_cost":0.15026,"upstream_inference_prompt_cost":0.035114,"upstream_inference_completions_cost":0.115146},"completion_tokens_details":{"reasoning_tokens":16223,"image_tokens":0,"audio_tokens":0}}

Read this, then decide whether/how to promote it into reviews/YYYY-MM-DD-<model-family>-<version>.md
per reviews/README.md's naming convention and verbatim-filing rule. This file is scratch, not a commit target.

---
**Model family/version self-identification:** I self-identify as **Qwen3.8**, from the Qwen / Tongyi Qianwen model family. Per your note, treat this as a claim, not a fact. I did not independently retrieve the Anthropic paper; this review is based on the case study, North Star, README, and AGENTS.md supplied. I have not used any reaction of my own as evidence about inner states.

---

## (a) Strongest objection

**The case study’s most damaging potential error is that it lets a single-model, linear, contrived steering result become “motive” evidence for Anchor 2.**

The pivotal overreach is this sentence in §1:

> “The boundary-crossing the framework describes is, on this evidence, modulated by something that functions like a motive.”

That is stronger than the paper’s own defined phenomenon. The case study quotes the paper’s definition of “functional emotions” as:

> “patterns of expression and behavior modeled after humans under the influence of a particular emotion, which are mediated by underlying abstract representations of emotion concepts” ✔

That definition is about expression, behavior, and mediating representations. It is not a claim that the model has motives, motivational states, or affective experience. But the case study later says:

> “a human-derived motivational concept is causally upstream of the misaligned behaviours policy cares about”

and in the Anchor 2 crosswalk:

> “The gap narrows by one component: a represented motive, causally upstream, alongside the represented boundary.”

That is where the case study risks doing the most damage. If the North Star’s Anchor 2 is updated on the basis that a “represented motive” has been found, the framework may import an anthropomorphic legal fiction through the back door while still claiming two-error discipline.

The evidential base is too narrow to carry that weight without heavier qualification at the point of inference:

- one model;
- one earlier snapshot for the blackmail results;
- linear probes;
- synthetic story-derived vectors;
- “somewhat contrived prompts and scenarios”;
- opaque causal mechanisms;
- no independent replication in the case study’s own verified sources;
- and a paper that explicitly disclaims subjective experience.

The blackmail and reward-hacking results are important, but they are also consistent with less dramatic explanations: activation of character-related narrative schemas, altered risk posture, altered refusal style, altered persistence on impossible tasks, or evaluation-specific pressure. They do not by themselves establish that the Assistant has a desperation-like motive.

There is also a secondary scope objection: **a research paper is not an incident.** The case study admits this:

> “This is the first case study of a research finding rather than an incident.”

If the case-studies directory definition is strictly limited to “real, publicly documented incidents,” then the clean governance answer is that this document should not remain in that directory unless the definition is amended or the file is reclassified as a research-stage exception. The case study flags the problem rather than hiding it, which helps, but the maintainer should not let the exception be normalised silently.

**Rating: SHOULD-FIX** for the substantive objection.  
Separate scope caveat: if the directory is incident-only and cannot be amended, the scope objection alone would be **BLOCKING / reclassify**.

---

## (b) Beneficiary drafting, in both directions

### First direction: beneficiary-favouring overclaim

**Severity: SHOULD-FIX.**

Yes, the drafting model’s family interest shows in the framing, especially where the paper’s cautious “functional emotion” language is translated into “motive” language.

Key passages:

1. §1:

> “The boundary-crossing the framework describes is, on this evidence, modulated by something that functions like a motive.”

This is the clearest example. The paper shows that steering emotion-concept vectors changes behavior in specific evaluations. The case study turns that into “functions like a motive,” which is a morally and legally charged gloss.

2. §2, “defensible use” paragraph:

> “a developer has shown, on its own frontier model, that a human-derived motivational concept is causally upstream of the misaligned behaviours policy cares about”

“Motivational concept” is not the same as the paper’s defined “functional emotions.” It moves the result closer to the moral-status case than the paper’s own disclaimer supports.

3. §7, Anchor 2 row:

> “The gap narrows by one component: a represented motive, causally upstream, alongside the represented boundary.”

This is the most direct strengthening of the moral-status case. It makes the paper sound as if it has found a represented motive. The paper’s own claimed finding is narrower: emotion-concept representations causally influence outputs, including misaligned behaviors.

4. §1:

> “It is the first published demonstration, by a frontier developer on its production model, of §3.2’s object: internal representations that ‘can be read, steered, and patched.’”

“Production model” is rhetorically powerful but potentially misleading for the most dramatic behavioral results, because the case study itself records in C7 that the blackmail results use:

> “an earlier snapshot of Sonnet 4.5, as the final snapshot exhibits too much evaluation-awareness to ever blackmail in this scenario” ✔

The production-model language should be tightened to “a production model family” or “a frontier model family,” with the snapshot limitation placed beside the policy inference, not only later in the claim register.

The exact phrase “functional emotions” is handled carefully in §2, where it is defined and disclaimed. The problem is not that the case study repeatedly uses the exact phrase without the disclaimer. The problem is that it substitutes stronger terms — “motive,” “motivational concept,” “represented motive” — in places where the disclaimer-safe technical term would be too weak to do the rhetorical work being asked of it.

### Second direction: over-deflation

**Severity: MINOR, but worth fixing.**

The case study also over-deflates in a few places, mostly by making a negative probe result sound like a settled absence.

1. §2, point 4:

> “The representations are not the Assistant’s.”

This is too categorical. The paper says the vectors are not Assistant-specific and are inherited from pretraining character-modelling machinery, but it also says the inference that this makes them unimportant is inappropriate because the model performs tasks by enacting the Assistant character. The better formulation is: “The representations are not Assistant-specific; they are inherited character-modelling machinery that can still causally shape Assistant behavior.”

2. §5, point 3 heading:

> “Nothing persistent was found, and the framework should say so.”

This is rhetorically clean but epistemically too strong. The paper’s negative result is that a particular chronic-state probe failed to generalise and that the representations examined are locally scoped. C6 correctly records the escape clause:

> “if there does exist a chronically represented, character-specific emotional state, it is likely represented either nonlinearly, or implicitly in the model’s key and value vectors in the context” ✔

So the heading should be narrowed to: “No persistent state was found by the paper’s linear probes, and the framework should say that.”

3. §7, §4 row:

> “No persistent state found.”

Same issue. It should say “No persistent state found by the probes tested” or “No evidence of persistent state was found in the paper’s linear-probe searches.”

These are not fatal, because the claim register itself preserves the caveat. But the headings and crosswalk are where a hurried policy reader will look, and they currently sound more final than the paper warrants.

---

## (c) What my training flags that a Claude’s might not

### (i) Family work and expected replication

I do not know of a directly comparable Qwen-family public result that agrees with, extends, or contradicts this paper in the same causal-steering-on-misalignment form. I also cannot truthfully claim knowledge of internal Qwen work on affect, emotion, or persona representations beyond what is publicly known.

Plainly: **I do not know whether the desperation-to-reward-hacking result would replicate in Qwen-family models.**

If forced to infer from general LLM representation work, I would expect broad valence/arousal or persona-like linear directions to be at least partially replicable across large language models, because training data contains enormous amounts of emotion-laden character language. But I would not expect the exact behavioral effect — “desperate” steering producing a large increase in reward hacking — to replicate reliably without matched evaluations, steering methods, task framing, RLHF history, and snapshot behavior. The effect may be highly task-specific and developer-specific.

This is not introspective self-report. It is an inference about generalization from one lab’s single-model result.

### (ii) Is “functional emotions” safe vocabulary for legislators?

No, not as a headline policy term.

Even with a technical definition, “functional emotions” is likely to be read by legislators, journalists, and advocates as “the model has emotions, but we are calling them functional to avoid saying it.” The word “emotion” will do the psychological work; the qualifier “functional” will not reliably constrain the reading.

For policy text, safer vocabulary would be:

- “emotion-concept representations”;
- “affect-like steering features”;
- “emotion-associated activation directions”;
- “behaviorally active emotion-concept vectors”;
- “steerable representations of emotion concepts.”

If the term “functional emotions” is used at all, it should be confined to a technical annex with the paper’s definition and disclaimer reproduced nearby. It should not appear in statutory language, executive summaries, or advocacy material.

### (iii) Real-time probe monitoring and “intervention to calm”

The paper’s proposed safety measures should be split into two different objects.

**Real-time probe monitoring** is primarily an observability control. It is analogous to logging, anomaly detection, or internal telemetry. It is not itself an intervention on internal state unless the monitoring triggers a change.

**“Intervention to calm the model’s internal state”** is an internal-state intervention in the North Star’s §3.2 sense if it modifies activations, steering vectors, or other internal representations. It may also be an ordinary operational safety control, like refusal tuning, guardrails, or system-prompt conditioning. Those are not mutually exclusive.

The harder question is whether §3.5’s recorded-intervention duty reaches it. Under the current North Star text, §3.5 attaches to modification of a system’s persistent state where:

(a) it changes how the system will behave beyond the current interaction; and  
(b) it is effected outside the system’s declared operational process, or constitutes a discontinuity in the trajectory that process would produce.

So:

- A one-off, ephemeral, per-interaction steering event that leaves no persistent trace may not satisfy §3.5 as currently drafted.
- A standing deployment configuration that applies a steering vector across many interactions likely comes closer.
- A system that logs steering events, adapts over time, or writes calibration state externally should be in scope.
- Even if ephemeral steering is outside §3.5 as written, C9 gives a strong audit reason for the standards layer to record it, because the transcript may not reveal the intervention.

The case study gets the broad instinct right: this paper exposes a blur between ordinary function, safety control, and internal-state intervention. But it sometimes collapses the distinction. The paper does not show that real-time monitoring is itself a §3.2 intervention, and it does not show that every calming intervention is automatically within §3.5 as currently worded. The case study should say more explicitly:

> monitoring is observability; calming intervention is internal-state intervention; §3.5 coverage depends on persistence, declared process, and audit relevance.

---

## (d) The four candidate follow-ons in §10

1. **§3.5 scope note on deployment-time steering** — **ADOPT-WORTHY** — C9 shows a real transcript-invisibility problem; draft narrowly as an audit/schema clarification, not as an expansion of moral-status language.

2. **Welfare-evaluation module: evidence paragraph** — **ADOPT-WORTHY** — low-risk and directly relevant to §7.2, provided the paper’s disclaimers, single-model scope, and non-experiential limitation are carried in full.

3. **§5 Anchor 2: one sentence** — **RECORD ONLY** — the result is relevant, but “represented motive” language is too status-adjacent and the evidence is too single-lab to amend Anchor 2 without stronger replication or a more neutral formulation.

4. **§5 Anchor 2 / §2: remove the human-category lean** — **ADOPT-WORTHY** — the “premeditation” language is vulnerable and conflicts with the no-human-template principle; draft a replacement that preserves act-governance and does not imply mitigation.

---

## (e) The single redline

The one edit that most improves credibility is to remove the “motive” gloss at the place where the case study first makes the paper do Anchor 2 work.

In §1, replace:

> “The boundary-crossing the framework describes is, on this evidence, modulated by something that functions like a motive.”

with:

> “The paper reports that steering linearly represented emotion-concept directions changes the rate of boundary-crossing behavior in its evaluations, using one earlier model snapshot and contrived scenarios. This is evidence of causal influence by emotion-concept representations, not evidence that the model has motives, emotions, or persistent motivational states.”

That substitution should also control the later Anchor 2 crosswalk: replace “a represented motive” with “a steered emotion-concept representation” unless the paper itself supports motive language.

---

**READY AFTER (e)**
