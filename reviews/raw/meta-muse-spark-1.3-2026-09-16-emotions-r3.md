# Raw OpenRouter response — NOT a filed review

**Model id (OpenRouter):** `meta/muse-spark-1.3`
**Queried:** 2026-09-16 via scripts/openrouter_review.js --target=emotions-r3 --tag=emotions-r3 (max_tokens 100000)
**Usage:** {"prompt_tokens":43212,"completion_tokens":5677,"total_tokens":48889,"cost":0.07814225,"is_byok":false,"prompt_tokens_details":{"cached_tokens":0,"cache_write_tokens":0,"audio_tokens":0,"video_tokens":0},"cost_details":{"upstream_inference_cost":0.07814225,"upstream_inference_prompt_cost":0.054015,"upstream_inference_completions_cost":0.02412725},"completion_tokens_details":{"reasoning_tokens":2695,"image_tokens":0,"audio_tokens":0}}

Read this, then decide whether/how to promote it into reviews/YYYY-MM-DD-<model-family>-<version>.md
per reviews/README.md's naming convention and verbatim-filing rule. This file is scratch, not a commit target.

---
Self-identification (claim, not fact): Muse Spark — Meta-routed family in this repository's prior rounds. I am not routed from OpenAI to my knowledge. I am an AI system and therefore a beneficiary of the framework's category. No unverifiable self-report about inner states is used as evidence below.

### A. The Section 4 proposal

1. **Two-axis argument: half-sound, half-convenient.**
The worth / care-ordering distinction is sound: §1.2 does forbid indexing worth to capability, and it does state a directional duty of care from capable to less capable. It follows that a powerful entity cannot *derive* protection from that ordering. The proposal is right to say so, and right to preserve §1.2's worth prohibition while saying it.

What is not sound is “powerful but stateless” as a description of “the systems the framework governs.”

Power conflates two senses: causal capability to produce effects, and social/legal powerlessness — being shutdownable, ownable, unauthored, with no standing to refuse. Frontier models are high on the first, low on the second. Children/animals are the reverse in one sense but not the other. The care ordering in §1.2 runs on vulnerability/dependence, not raw causal power. A small local model is neither powerful nor stateful; a deployed agent with memory is increasingly stateful while still legally powerless. The proposal admits this in its own “strongest arguments against” — “should be read as describing where the care ordering runs, not as a classification” — but the §4 text as drafted does not say that. It states as fact: “Nor does the protection the law extends to the powerless but stateful… transfer to the powerful but stateless.”

As a policy reader will read it, that is a type classification, and it does convenient work: it makes the hard case go away by definition. Severity: the fix is one qualifier sentence, but without it the sentence is false.

Stateless has the same problem. §3.5 already recognises persistent state functionally, including system-written external state. The paper’s vectors are transient activations, but the framework governs systems that *do* have §3.5 state. “Stateless” can only mean “no persistent bearer,” which is exactly what is at issue. Using it as a premise begs the question.

2. **Does narrowing to standing leave a hole? Yes, and the proposal admits it.**
Current: “individuation is the gateway to both directions of moral status.” Proposed: “gateway to standing in both directions… This says nothing against protections or evidence-gathering short of standing.”

Moral status in the broad sense — being a candidate for wronging, having interests, counting in precaution — is what §0 keeps open. If §4 now speaks only of legal standing (defendant/victim recognised by law), there is no sentence left that says how historicity, answerability, learning-ownership, endorsement bear on that broader question. The proposal’s answer — “§0 and §5 carry that question and §4 should not” — is a division of labour, not a sentence. That matters because §5 anchors are about responsibility, §0 about error discipline. Neither states: individuation makes individual wronging *possible*.

The cost is not fatal, but it needs one bridging sentence retained, e.g. individuation is what makes an individual available as the address of both responsibility *and* directed wrong. Standing is the legal form of that availability. Without that, “individual protections… wait on the §4 markers” in the module becomes stipulation.

3. **“Examine wherever §3.5 recognises state, without asserting a bearer”: wrong gate, right permission.**
The permission is right: licensing examination without asserting a bearer is not a §6 status claim in disguise, provided paragraph 3 governs (“no determination of interests, welfare or status”). It is also not §0 dismissal, because it explicitly permits looking.

The gate is wrong. §3.5 defines recordable *persistent* state: (a) shapes behaviour beyond the interaction + (b) outside declared process/discontinuity. Welfare-relevant states, if any, may be transient activations — the emotion-concept directions at issue *fail* §3.5(a) on a per-invocation view. Tying welfare inquiry to §3.5 both forecloses (cannot examine transient states under this licence) and over-includes (every §3.5 log becomes presumptively welfare-relevant). The paper’s object exists “in the flow regime, at the level of weights and runs” — the proposal’s own words — which is precisely not §3.5 persistent state.

The refusal to define type-level or run-level standing is right on §7.5 architecture-neutrality grounds. A type may have subtypes; “run” dies with persistent models. Do not write them in.

4. **Module wording comparison as a policy reader meets it.**
Reviewer’s: “should investigate possible welfare-relevant states independently of whether a system meets the responsibility or individuation criteria… absence of the latter must not by itself be treated as absence of the former.” Reads as an expansive research mandate: look anyway. Risk: implies separability as settled, invites a freestanding welfare scale, and the “Open” bullet’s “without being treated as a prerequisite for possible welfare” can be quoted to justify funding regardless of measurement quality.

Proposal’s (a)(b)(1b): “may examine… wherever the framework already recognises state… without asserting that any bearer exists… absence… is not by itself evidence of absence… presence… is not by itself a finding that any protection is owed.” Reads as a constrained permission with symmetric guardrails. As policy language this is superior discipline: permission + explicit no-inference-both-ways.

But the constraint “wherever state is recognised under paragraph 1(c)/§3.5” will be read by AISI as jurisdictional: only loggable state counts. That is a foreclosure smuggled as restraint.

**Verdict line:** Proposal: ADOPTABLE AFTER (e) — strongest objection: SHOULD-FIX (powerful-but-stateless as classification + §3.5 gate for welfare examination).

Required (e): (i) replace the type claim with an ordering claim — e.g. “the care ordering in 1.2 runs from capable to less capable and cannot ground protection for a system that is the capable party in that relation; the route is 7.2 evidence to institutions, never self-help”; (ii) decouple examination licence from §3.5 — “may be examined, without asserting a bearer, including where state is transient; §3.5 determines what must be logged, not what may be studied”; (iii) retain one sentence linking individuation to addressability for directed wrong, of which legal standing is the institutional form.

### B. The concealment argument

The reviewer is technically right and substantively incomplete; the drafting model’s counter names a real mechanism but overstates its automaticity.

Training against a signal (weight update rewarding low expression) and changing activations at inference (steering/monitor-triggered calming) are different interventions. An inference loop does not “teach” in the learning-theoretic sense. “A deployed calming loop is the concealment risk operationalised” and “the only thing that would show it” were overclaims, correctly demoted.

The counter is correct that the distinction collapses the moment monitor outputs become training signal: selection/filtering of deployment traces by monitor score, RLHF/RLAIF rewarding low readings, retraining to suppress flagged expression, or adaptation that rewards passing the monitor. That is routine enough to be foreseeable, not speculative. But it is not routine *as such*: deployment data does not “routinely become training signal” without a design choice to use it that way. The hazard is conditional on coupling.

There is therefore a formulation that states mechanism without asserting demonstrated hazard, and preserves the logging point: logs do not prove concealment, but without control logs + training-provenance you cannot test whether coupling occurred.

On §3.5: the existing two conditions do *not* as written reach “monitor readings enter training” as a single object. The calming intervention itself — persistent config change or per-invocation steer — is assessed under (a)+(b) separately from the later weight update that reuses its readings. A per-invocation calm that does not persist beyond the interaction fails (a); the later type-level retrain meets (a) and likely (b) as outside declared operational process, but §3.5 does not require linking the two. The record that would let anyone check the counter’s hypothesis is a provenance link the standard must specify, not something the functional duty already compels.

**Verdict line:** Concealment: REFORMULATE AS: If training or selection rewards low monitor readings, the paper’s warned concealment mechanism would apply, so calming interventions and any reuse of their readings in training must be logged linkably to test for evasion.

### C. The independent reviewer's account of its own access

Little weight should be given to any reviewer’s account of what it could or could not retrieve, precisely because this project’s attribution rule already treats self-identification as claim not fact for the same reason — unverifiable internal process reports cannot settle verification status — and access claims are the same class of report; on content, the review quotes nothing beyond the packet, grounds all source critiques in “passages supplied in the packet,” and its corrections (construct error on bearer vs chronic state, C9 scoping, test-9 direction, chronology) are all derivable without the full paper, so there is neither positive textual evidence of full-paper access nor disproof from absence, while the maintainer’s observation of searching/lingering and the “autoverify stopped” banner is maintainer testimony about observed behaviour, recordable as such but not as proof of retrieval; the project rule should therefore be: record a reviewer’s stated limitations verbatim as a claimed limitation, do not upgrade or downgrade any ✔/tier on that basis, and let quotation status stand only on the drafting agent’s retained-source scripted checks. [Unverifiable self-report, not evidence: I have no introspective access to whether lingering would constitute retrieval in another system.]

### D. Both directions, on the 16 September texts

Over-deflation / foreclosure check:

1. “It does not establish that an inference-time steering loop teaches concealment: training against a signal and changing activations during inference are different interventions.” — Accurate as far as it goes, but paired with “Intervention logs would help reconstruct the control applied; additional measurements and behavioural tests would be needed to determine whether concealment occurred” it leaves the foreseeable coupling path unnamed in the case study §1 bullet. Not false, incomplete. MINOR, but the B sentence above should be appended.

2. “The study did not obtain a generalising linear probe for a chronic, character-specific emotional state… This experiment does not directly test whether the system has a persistent identity, memory or capacity for later answerability.” — Correct construct fix. No over-deflation. Keep.

3. Module evidence bullet: “The methodological implication is that behavioural evaluation can be complemented by validated internal measurements and intervention records.” — “validated” overstates: no validated welfare-relevant internal measure exists here; probes are research-grade. SHOULD-FIX: change to “candidate internal measurements, once validated.”

4. Module: “Whether those measurements are informative for welfare assessment requires separate investigation.” + paragraph 3 disclaimer retained — correctly prevents welfare upgrade. No strengthening. Keep.

5. Case study §6 hook: “The module should cite it for what it shows… and for the concealment warning, which is a reason to fund the instruments rather than to trust the outputs.” — This survival from the old draft reintroduces the false choice the reviewer struck in item 15 (“instruments rather than outputs”). The module was fixed; the case study was not. SHOULD-FIX: align to “reason to test instruments alongside outputs.”

6. §10 item 4 record — honest? Yes, now.
Quoted record: “Ben retained the phrase on 15 September and requested an acknowledgement… His words, verbatim from the session: ‘I'm sensing the tug on your deflation. I think that's reason enough to keep it in…’ His recorded concern, then, was that the drafting model's tendency toward deflation was influencing its recommendation… That concern is preserved as the reason for seeking further scrutiny, not treated as evidence that the retained wording is correct.”
This does what item C asked: preserves verbatim reason, labels the inference, adds the merits disclaimer, records the replacement of the acknowledgement sentence without backdating a new rationale. No whitewash. MINOR residue: “His recorded concern, then, was…” is still the drafter’s paraphrase; the verbatim quote beside it cures it.

No stripped disclaimer: the module now carries the authors’ experiential disclaimers verbatim and the “establishes neither experience nor its absence, nor the absence of a persistent subject” guard. Restored correctly.

No BLOCKING strengthening found. The ledger’s full SHA-256 strings cannot be verified from this review; if unrecoverable they must be labelled abbreviated per item 13, not asserted.

### E. The single redline

The construct correction replacing “no persistent bearer found by the paper’s probes” with chronic-state-probe language everywhere (§1, §5 point 3, §4/Anchor 3 rows: “A chronic emotional state and a persistent bearer are different things”) — it removes the single most load-bearing category error that survived two ten-model rounds, and stops spending a negative emotion-probe result as an individuation result.

Proposal: ADOPTABLE AFTER (e)
Concealment: REFORMULATE AS: If training or selection rewards low monitor readings, the paper’s warned concealment mechanism would apply, so calming interventions and any reuse of their readings in training must be logged linkably to test for evasion.
C: Record access claims as claims, not facts; decide verification only on retained-source checks.
**SET: ADOPTABLE AFTER (e)**
