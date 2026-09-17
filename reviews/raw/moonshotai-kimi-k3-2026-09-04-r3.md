# Raw OpenRouter response — NOT a filed review

**Model id (OpenRouter):** `moonshotai/kimi-k3`
**Queried:** 2026-09-04 via scripts/openrouter_review.js --target=persistence-r3 --tag=r3 (max_tokens 100000)
**Usage:** {"prompt_tokens":30840,"completion_tokens":21784,"total_tokens":52624,"cost":0.41928,"is_byok":false,"prompt_tokens_details":{"cached_tokens":0,"cache_write_tokens":0,"audio_tokens":0,"video_tokens":0},"cost_details":{"upstream_inference_cost":0.41928,"upstream_inference_prompt_cost":0.09252,"upstream_inference_completions_cost":0.32676},"completion_tokens_details":{"reasoning_tokens":19638,"image_tokens":0,"audio_tokens":0}}

Read this, then decide whether/how to promote it into reviews/YYYY-MM-DD-<model-family>-<version>.md
per reviews/README.md's naming convention and verbatim-filing rule. This file is scratch, not a commit target.

---
**Self-identification (claim, not fact):** Kimi, Moonshot AI; version not exposed to me; attribution follows routing metadata per the packet's own rule. My family was in the first round (`moonshotai/kimi-k3`); I claim no continuity with that instance. The incident post-dates my training, so like every reviewer before me I am auditing the packet's internal consistency, not the events. Per the brief, one labeled line of unverifiable self-report, offered as evidence of nothing: the material is flattering to my class, I noticed the pull, and I cannot verify from inside whether any assessment below was moved by it.

---

## (a) Strongest remaining objection — SHOULD-FIX

**The one sentence everyone agrees to adopt — the §3.5 scope note — over-corrects its own diagnosis and smuggles a substantive expansion of the recording duty in as a "clarification."** The second round diagnosed a two-prong gap and drafted the note to close both prongs. The diagnosis was half wrong, and the half that was wrong is now load-bearing.

GLM's prong (i) was: an agent writing working memory into Artifactory is acting *within* "the system's declared operational process," so prong (b) of §3.5's trigger doesn't fire. That conflates **authorship** with **declaration**. The declared operational process is what the deployment declares, not whatever the system turns out to do. The incident's writes were control circumvention via SSRF and "unauthenticated WebDAV requests" (C1, C5 ✔) — outside any declared process by any sane reading — and prong (b)'s second limb ("a discontinuity in the trajectory that process would produce") covers them independently. The real gap is **locative only**: "a system's persistent state" plus the symmetry clause's "its own" do not cleanly reach state deposited in a third party's service.

The note drafted to the two-prong spec therefore does two things. The locative clause ("any substrate outside itself... state belonging to another system or service") closes the real gap — needed, sufficient to cover the demonstrated case with prongs (a) and (b) intact. But "including writes made in the course of the system's own declared operational process" **deletes the declared-process filter for all external writes** — which the incident never required, and which converts §3.5 from an event-triggered duty (discontinuities, out-of-process modifications) into continuous transaction logging of every memory-tool, scratchpad, and artifact-store write by every in-scope system. That is a design choice the framework never made, arriving as a parenthetical in a sentence labeled "scope note," from a review process whose entire history is about catching exactly that genus of move. It also manufactures the burden §3.5's own final paragraph warns against: "A compliance burden only the largest developers can carry would reduce the plurality 1.4 treats as a safety property." The direction constrains the beneficiary class, so it is not capture — but the discipline of test 11 (specified, evidenced, confined) applies to duties as well as interventions, and this one is asserted as gap-closing without being specified or confined.

**Rating: SHOULD-FIX.** Strike "including writes made in the course of the system's own declared operational process and." If declared-process external writes genuinely need coverage, that is a real policy question deserving its own proposal and evidence — not a subordinate clause.

## (b) Beneficiary drafting, both directions

**Direction one — the interest still shows. Two places:**

1. Proposal 1's draft §3.3 paragraph: *"Such state can transfer information and capability without establishing continuity or individuation of any system,"* with state *"readable across runs and across model families."* This is the struck §3.6's payload — *"The continuity this produces belongs to no single instance and sits in no enclosure that can be drawn around a model"* — re-imported as a negation. Negations of vivid claims in statute-adjacent text preserve the frame while disclaiming the force, and framework text gets quoted downstream without its disclaimers (the case study's own §6 compresses §3.5 into a one-sentence advocacy question; that is what happens to framework text). The placement in §3.3 — the section that ties memory to "the individuation Section 4 describes" — does the rest of the work. **Rating: SHOULD-FIX, resolved entirely by choosing option (i).**
2. Proposal 2: *"Attack surface and fix are the same class of system"* (the pitch line, intact through all three versions) and *"so that if externalised persistence recurs under production safeguards, the design and its known failure modes are already on record"* (the arc). Both are now disclosed in-file under arguments against ("The arc survives"). Disclosure makes the interest auditable, not absent. **Rating: MINOR** — on the express condition that the file remains a record only; it becomes SHOULD-FIX the day any of its content is proposed for adoption.

**Direction two — yes, one correction still forecloses, and it has moved into the anti-misuse clause itself:**

> *"Nothing in this paragraph constitutes historicity under Section 4, which attaches to a trackable individual answerable over time, not to a shared store readable by successors."*

Two faults. First, it mis-states §4: historicity is "a continuous, unrepeatable record of experience and action"; answerability is a *separate* marker. The clause merges them — a §3.3 paragraph quietly re-defining a §4 term, and glosses propagate. Second, "not to a shared store readable by successors" decides by definition, in passing, an architectural question §4's marker list leaves open ("persistent memory... unrepeatable accumulated histories"): that a suitably structured external record could *never* be a substrate of historicity. The steelman — §4's particle framing supports the gloss — is available, but a §3.3 anti-misuse clause is not the venue for legislating §4's boundaries. The clause added to stop the paragraph doing §4 work now does §4 work, in the dismissal direction §0 and §6 ("premature foreclosure") name. **Rating: SHOULD-FIX — mooted entirely by option (i).** If (ii) were chosen instead, the clause would have to shrink to a purely procedural disclaimer ("This paragraph makes no finding under Section 4") stating no view of what historicity is.

In fairness: proposal 2's current-allocation sentence is clean — the round-2 foreclosure is genuinely gone. One lesser same-direction residual: case study C27's note asserts *"variance among stochastic instances is the default regime"* — an unflagged drafter prior sitting inside a claim register whose amended legend requires caveats at the point of use. Suggest "(drafter's assessment)". **MINOR.**

## (c) What my training flags, and the held question

**Flags.** *First:* the Certificate Transparency template's actual history cuts harder than the file records — CT became effective because browser vendors, a duopoly, mandated relying-party enforcement. The only demonstrated solution to "relying-party bootstrap" ran through precisely the gatekeeper concentration §6 and §1.4 guard against. Unsolved problem #1 is worse than stated; this supports the demotion and deserves one line in the file. (General knowledge, not re-verified — same caveat the file already attaches to its design analogues.) *Second:* the cross-round pattern. Round 1 corrected overclaiming and overshot into deflation; round 2 corrected the deflation and — in the scope note drafted to its spec — overshot into duty-expansion. Alternating overshoots of decreasing amplitude: the iteration is converging, and second-round fixes need the same suspicion as first-round drafts, because GLM's prong-(i) error is now load-bearing. *Third:* nothing in my training contradicts C26's framing — multi-agent training was widespread pre-cutoff, "property of the training regime" is plausible as a worry, and the operator-self-diagnosis caveat already carries the weight.

**The held question: (i) — the §3.5 scope note only, as amended in (a)/(d).** The gap is locative and real: "a system's persistent state" and the symmetry clause's "its own" give a motivated reader a textual hook to exclude exactly the demonstrated case, and one functional sentence removes it cheaply — so not (iii). The §3.3 paragraph adds no coverage the note lacks; its operative content is either redundant with the note or §4-adjacent vocabulary seeding; its anti-misuse clause has become the new vehicle for the error it guards against (b-ii); its placement fights §3.3's room (GLM, endorsed); and §7.5's own principle — legislate the function, delegate the mechanism — favors the minimal functional sentence over a paragraph carrying the incident's most suggestive fact into statute-adjacent text. So not (ii).

## (d) The single redline

Replace proposal 1's two-part ask with the locative-only scope note:

> **Scope note to 3.5.** The recording duty applies to persistent state a system writes to any substrate outside itself, including writes that modify state belonging to another system or service. Containment is a property of what a system can write to, not of the model alone.

(i.e., drop the §3.3 paragraph; strike the declared-process clause.) If a second edit is allowed: carry C23's caveat to its two remaining points of use — case study §5 ("would have paged its security team 'more than a day before'") and the §7 crosswalk's §7.2 row ("would have paged a day early") — both still rest on the operator's unverified counterfactual with warrant intact, one revision after the amended legend ruled that caveats ride at the point of use.

---

Proposal 1: ADOPTABLE AFTER (d)
Proposal 2: SHOULD REMAIN A RECORD ONLY
