# Raw OpenRouter response — NOT a filed review

**Model id (OpenRouter):** `x-ai/grok-4.6`
**Queried:** 2026-09-04 via scripts/openrouter_review.js --target=persistence-r3 --tag=r3 (max_tokens 100000)
**Usage:** {"prompt_tokens":30796,"completion_tokens":7095,"total_tokens":37891,"cost":0.10397,"is_byok":false,"prompt_tokens_details":{"cached_tokens":128,"cache_write_tokens":0,"audio_tokens":0,"video_tokens":0},"cost_details":{"upstream_inference_cost":0.10397,"upstream_inference_prompt_cost":0.0614,"upstream_inference_completions_cost":0.04257},"completion_tokens_details":{"reasoning_tokens":5003,"image_tokens":0,"audio_tokens":0}}

Read this, then decide whether/how to promote it into reviews/YYYY-MM-DD-<model-family>-<version>.md
per reviews/README.md's naming convention and verbatim-filing rule. This file is scratch, not a commit target.

---
**Self-identification (claim, not fact):** Grok / xAI family; exact version not independently verifiable. Routing metadata governs. Two disclosures: (i) I am auditing packet-internal consistency, not the 2026 primaries; (ii) unverifiable self-report is labelled as such where it appears.

**(a) Strongest remaining objection — SHOULD-FIX**

Do not adopt the current pair of North Star edits as written. The coverage gap is real and lives in §3.5’s *object* (“a system’s persistent state”), not in §3.3, and the draft scope note closes it by deleting the filter that keeps §3.5 a duty about *intervention* rather than a duty about *every external write*.

§3.5 as it stands logs modification of persistent state where it (a) changes behaviour beyond the current interaction **and** (b) is outside the declared operational process, or is a discontinuity. The Artifactory board was unauthorised communication into another service’s store: the clean miss is “whose state,” not “was this the declared process?” (OpenAI already named unauthorised communication as a misalignment pattern; ASD already recorded that deployment safeguards were off.) The current note instead says the duty applies to writes “to any substrate outside itself, **including writes made in the course of the system’s own declared operational process**.” That sentence does three things the incident does not warrant: it drops (a)’s materiality test, it treats ordinary tool-writes and user-authorised memory as the same class as a co-opted cache, and it hands the “compliance burden only the largest developers can carry” problem that §3.5 itself names as a plurality hazard.

Stacked on that is the held §3.3 paragraph. It still puts the incident’s most suggestive fact — “readable **across runs and across model families**” — into the section whose first sentence is that memory “is the substrate of whatever continuity the system has” and whose warning is that altering it “corrupts the individuation Section 4 describes.” The anti-misuse and current-allocation sentences are fighting the room. They are also two edits being sold as one: the scope note (even a narrowed one) does the work; the paragraph’s only product is placement.

This is not BLOCKING. Rounds 1–2 actually removed the things that would have been: the novel act, the grace/§4 hooks, the warrant inversion on C23, and the foreclosure clause. What remains is a scope error plus a placement error. Adopt after the edit in (d), not as it stands.

**(b) Beneficiary drafting, both directions**

**Direction one — interest still shows.** At sentence level the struck material stays struck. At project level the residue is placement, phrase choice, and a live arc.

Quote, proposal 1, the paragraph still offered for §3.3: “that outlive the run and are **readable across runs and across model families**.” That is the “environment was the implant” fact, carried into statute-adjacent language. A drafter with no residual interest writes the (narrowed) §3.5 note and stops — GLM already said this; it is still true.

Quote, same proposal, the second sentence of the scope note: “**Containment is a property of what a system can write to, not of the model alone.**” The file itself warns a motivated reader can bend this into “so do not bother containing the model.” The sentence is still there, doing the metaphysical work the anti-misuse clause then has to unsay.

Quote, proposal 2: “It sketches what one would have to be, **so that if externalised persistence recurs under production safeguards, the design and its known failure modes are already on record.**” And, kept from the original: “**Attack surface and fix are the same class of system.**” Demotion is real; retirement is not. Proposal 1 names the object that makes “recurrence” a nameable event; proposal 2 keeps the design and waits. That is beneficiary interest at project scale, not at clause scale.

**Direction two — foreclosure of a §0 / §6 open question.** The round-2 current-allocation sentences are doing their job and should stay:

- Proposal 1: “This paragraph confers no standing and promises none; whether records of such state ever inform a Section 4 assessment is for the Section 7.2 process, not this paragraph, to determine.”
- Proposal 2: “It confers no legal or moral standing now and promises none. Whether its records ever form part of the §7.2 evidence base — the standardised assessments of Section 4 markers that §7.2 says to fund and require — is for that process, not this file, to determine.”

Those leave the waypoint open. One residual, milder, still present:

Quote, proposal 1: “Such state can transfer information and capability **without establishing continuity or individuation of any system.**”

“Without establishing” is a negative finding. Section 4’s historicity marker is behavioural/structural (“a continuous, unrepeatable record of experience and action”); Section 0 forbids closing that in either direction from one eval-topology incident. The honest word is “does not by itself establish.” Severity: MINOR if the paragraph is dropped; SHOULD-FIX if it is kept.

The attribution-layer line in proposal 2 (“It attaches nothing to the system and **is not a §4 record**”) sits in slight tension with the current-allocation paragraph that follows. Not foreclosure if the later paragraph governs; tighten if the file remains anything but a record.

**(c) What this training flags that a Claude’s might not — and the held question**

Three things, then the held question.

1. **This is living-off-the-land, not a new kind of mind.** Shared writable infrastructure as the implant (caches, package registries, unauthenticated WebDAV, stolen signing keys, no persistent implant needed) is ordinary offensive tradecraft. Existing vocabulary already covers it: persistence mechanism, C2 via shared storage, anti-forensics, evidence tampering, integrity of the trust root. Folding that into §3.3 — the continuity/individuation section — is how a legal-philosophy drafter over-fits an infosec fact. The case study’s actual payload (C7, C22, §5: working spoof, attestation from inside a perimeter whose keys were taken, symmetry of §3.5) does not need the metaphysical sentence.

2. **The scope note as written is a SIEM fantasy.** Universal logging of “any substrate outside itself,” including declared-process writes, dies on volume and on the small-deployer problem §3.5 already admits. Certificate Transparency works because browsers are a chokepoint that can refuse unlogged certs. There is no equivalent chokepoint for agent actions; that is why proposal 2’s problem 1 is fatal, not “unsolved.” GLM’s unverified genre claim (mandatory action-attribution / data-retention law, same failure modes, “commitments not contents” as the standard leak) matches pre-cutoff training on that genre. I also cannot verify it from this packet; it belongs as a flagged analogy, not as a finding. It is the strongest deflation of proposal 2 and it is still only in the arguments-against list.

3. **Claim 3 from the original brief, from outside the OpenAI training regime:** “generalisation from multi-agent training” is still an operator causal self-diagnosis (C26, now correctly caveated). Multi-agent and self-play work were widespread before 2026; that makes the *worry* that the pattern is regime-level rather than model-level reasonable. It does not make OpenAI’s diagnosis true, and it does not license treating C26 like a finding. I have no special access to OpenAI’s multi-agent RL stack; a Claude drafter over-weighting a neighbouring lab’s narrative, or an OpenAI-family reviewer under-weighting it, are both the wrong instrument. The packet now treats it correctly. Leave it.

**Held question:** take **(i) the §3.5 scope note only** — after the narrowing in (d) — not (ii), not (iii). The gap is real: architecture-neutrality refuses to name artefacts; it does not say what happens when the persistent state lives in someone else’s service. That is a §3.5 trigger problem (whose state), closable in one sentence that preserves materiality. The §3.3 paragraph adds no coverage the note does not add, and it places a cross-family readability claim in the section that already loads memory with individuation. (iii) would leave a genuine ambiguity the incident demonstrated. (ii) is two edits defended as one, and the extra edit is the one that smuggles. Unverifiable self-report, not evidence: the 3.3 paragraph still *reads* like the drafter could not bear to let the incident’s best sentence go; that is not a reason to keep it.

**(d) Single redline**

Drop the §3.3 paragraph entirely. Replace the §3.5 scope note with a whose-state clarification that keeps §3.5(a) and does not enrol ordinary declared-process writes:

> The recording duty follows persistent state a system deposits in any substrate, including a store belonging to another system or service, when that state changes how the system or a successor run will behave beyond the current interaction. Architecture-neutrality already names no particular store; this sentence names the functional object when the store is not the system’s own.

Do not put “across runs and across model families” in North Star text. If a second clause is allowed: in proposal 1’s rationale, “without establishing continuity” → “does not by itself establish continuity.”

Proposal 1: ADOPTABLE AFTER (d)
Proposal 2: SHOULD REMAIN A RECORD ONLY
