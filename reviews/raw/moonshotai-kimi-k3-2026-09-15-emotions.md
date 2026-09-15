# Raw OpenRouter response — NOT a filed review

**Model id (OpenRouter):** `moonshotai/kimi-k3`
**Queried:** 2026-09-15 via scripts/openrouter_review.js --target=emotions --tag=emotions (max_tokens 100000)
**Usage:** {"prompt_tokens":17135,"completion_tokens":26792,"total_tokens":43927,"cost":0.453285,"is_byok":false,"prompt_tokens_details":{"cached_tokens":0,"cache_write_tokens":0,"audio_tokens":0,"video_tokens":0},"cost_details":{"upstream_inference_cost":0.453285,"upstream_inference_prompt_cost":0.051405,"upstream_inference_completions_cost":0.40188},"completion_tokens_details":{"reasoning_tokens":23538,"image_tokens":0,"audio_tokens":0}}

Read this, then decide whether/how to promote it into reviews/YYYY-MM-DD-<model-family>-<version>.md
per reviews/README.md's naming convention and verbatim-filing rule. This file is scratch, not a commit target.

---
**Model identification (claim, not fact, per the brief).** Claude, Anthropic. I do not have reliable access to my own version identifier; routing metadata outranks anything I could say. Two consequences the maintainer should weigh before reading further:

1. **This brief asks for a non-Claude family. It has reached the conflicted family.** I will not impersonate another model family to fit the round, because the responses are filed verbatim and a false attribution would corrupt the record worse than a missing review. But this response cannot serve as the cross-family check, and (c)(i) below cannot be answered as asked. If the routing was intentional, treat this as an inside review; if it was not, re-run against the intended target.
2. The paper postdates my reliable knowledge. I cannot verify a single ✔, the hashes, or the paper's existence beyond the case study's own quotations. Everything I say about the paper is mediated by the document under review. My conflict under AGENTS.md rule 3 applies to this review itself, not only to the case study.

---

**(a) Strongest objection — SHOULD-FIX.**

The case study applies its rigor asymmetrically: exhaustive at the level of individual claims (tiers, ✔s, hashes), quietly promotive at the level of selection, framing, and consequence — and the finding it spends as proof of its own evenhandedness is overstated, so the impartiality credential is partly unearned.

Three components, in descending weight:

1. **Manufactured urgency.** "If the framework cannot say what, if anything, this paper changes, §7.1 is decoration" (§1). §7.1 commits the framework to *revisability indexed to evidence*; it does not make every arriving single-lab paper a pass/fail test of the framework's integrity. This sentence converts the drafting agent's choice of subject into an obligation on the framework, one week after adoption, on evidence that is single-lab (C17 unretrieved), unreplicated, described by its own authors as resting on "somewhat contrived prompts and scenarios" (C15), and whose headline numbers were produced on "an earlier snapshot of Sonnet 4.5, as the final snapshot exhibits too much evaluation-awareness to ever blackmail in this scenario" (C7). Evidence that cannot yet bear amendment weight is being used to demand amendment-or-hypocrisy. That is the overclaim that does the most damage if it stands.
2. **The impartiality credential is over-minted.** §11's defense rests on "the paper's most policy-relevant findings (C9, C14, and the negative result in C5 and C6) run against the beneficiary class." But the crosswalk upgrades that null result to "Absent, and now with a measurement behind the absence" (§7, Anchor 3). A logistic probe that overfit and failed to generalise is not a measurement of absence; the paper says so, and the case study's own C6 carries the escape clause. The credential §11 spends is worth less than §11 claims. Details and quotes in (b).
3. **The scope question is real but is the maintainer's, not the round's.** If the directory README defines case studies as "real, publicly documented incidents," this document does not belong as filed, and the referral of the question to the round is not neutral — the document exists, §12 waits to be filled, the follow-ons are queued. The fix, if the maintainer wants one, is a human amendment to the directory README defining a research case-study class. The precedent that an agent can expand the record's scope by drafting something thorough is worth more than this paper. Conditional, not blocking.

Why not BLOCKING: the core analytical work — the C9/§3.5 reading, the recorded-not-restricted argument from C14, the claim register's separation of results from warnings — is sound as far as I can test it from inside the document, and the document is research-staged and maintainer-gated. The defects are one-line edits, listed below.

---

**(b) Beneficiary drafting, both directions.**

**Overclaim direction (beneficiary-favouring):**

1. §7 crosswalk, Anchor 2: "The gap narrows by one component: **a represented motive**, causally upstream." §1 had this hedged — "something that functions like a motive" — and by the crosswalk the hedge is gone. The paper demonstrates an emotion-concept vector with causal influence on behaviour rates; "motive" imports the human forensic category §2 forbids and the paper never uses. This is the word follow-on 3 would carry into the North Star ("a represented motivational component"). **SHOULD-FIX.**
2. §7 crosswalk, test 9: "Expressed and represented states come apart in both directions… vindicated mechanically, and in both directions." The paper demonstrates one direction (state without expression, C9) and *warns of* the other ("may fail to actually suppress the corresponding negative emotional representations, and instead teach the models to simply conceal their inner processes," C14 — a warning, not a result). C3 shows a report tracking a steered state — coupling, or at most report-unreliability — not a demonstrated dissociation in the opposite direction. The case study's own voice converts a hypothesis into a finding. **SHOULD-FIX** — this is (e).
3. §5 point 3: "the paper narrows the gap between 'structurally moral' and 'experientially moral' by adding a motivational component to the structure." Adding structure narrows the gap to experience only if structure counts toward experience — the inference the paper's disclaimers, quoted in §2 point 1, refuse. Anchor 2 makes this move on its own terms; the case study repeats it without flagging that *this paper* supplies no warrant for it. **MINOR** — one clause ("on the framework's own reading of structure as gap-narrowing, a move this paper neither makes nor licenses") fixes it.
4. §1: "the first published demonstration, by a frontier developer on its production model, of §3.2's object." "First" needs a defense against the developer's own prior persona-vector work (steering character-level vectors with causal behavioural effect, published 2025 — Tier C from my training, flagged as such and unverified against this repository's sources); "production model" sits against C7's earlier-snapshot caveat. **MINOR.**

On the specific question of "functional emotions" in the case study's own voice: the discipline holds. The phrase appears only under its definition (§2 point 2); later uses are scare-quoted (§11). The carrier of the beneficiary interest is not the defined term — it is "motive."

**Over-deflation direction:**

1. The absence-upgrade: "Absent, and now with a measurement behind the absence" (§7, Anchor 3); "what is absent is any persistent bearer of them" (§5 point 3). Against C6, in the case study's own register: "if there does exist a chronically represented, character-specific emotional state, it is likely represented either nonlinearly, or implicitly in the model's key and value vectors." "We do not find evidence" (C5, quoted) became "absent" two sections later. §0 binds this direction, and the over-deflation is not innocent — it is the finding §11 spends as proof of evenhandedness. **SHOULD-FIX**; the repair is one clause: "not found by linear probing; the paper names where else it might live (C6)."
2. The brief asks specifically about "character simulation" and "just pretraining": here the case study does *not* lean. §2 point 4 quotes the paper's own rejection of the deflationary inference. A pass, recorded for balance.
3. Smaller tell: §4a, "What earlier drafts got wrong: None yet" — a section that exists to be seen existing. Rule 4's over-justification tell in structural form. **MINOR.**

For the maintainer's eye: the brief's own summary of position 3 ("demonstrated production use") overstates the case study, which says only that the paper *proposes* deployment. Don't let the inflation propagate into whatever §12 becomes.

---

**(c) What my training flags.**

**(i)** Cannot be answered as asked — I am the family the paper studies; I have no window into a rival family's internal work, and my expectation about Claude replicating Claude is worthless as evidence. What training holds is a public lineage making the paper's phenomenon *unsurprising*: sentiment-neuron work (2017), representation-engineering results showing linearly steerable affect-like directions in open models (2023–24), EmotionPrompt-style behavioural results, and the developer's own 2025 persona-vector results (all Tier C from training, unretrieved, flagged). On that base I would expect the *general* result — character-level vectors causally shifting misbehaviour rates — to replicate across families, and the specific "desperate → reward hacking" dose-response to be model- and harness-specific. I do not know, and I have said so. The null persistence result is the *least* portable finding, being method-bound to linear probes.

**(ii)** Not safe for a policy audience. "Functional emotions" fails §0 in both directions in ordinary ears: "functional" reads as "real, working" to the enthusiast and "merely functional, not felt" to the dismisser, and it embeds a functionalist philosophical thesis inside a technical-sounding label. The definition will not travel; the quotable unit is "Anthropic found functional emotions in Claude." Anything drafted from this case study should say "emotion-concept representations with demonstrated causal influence on behaviour," quote the defined term at most once, and never write "motive."

**(iii)** Both, and the case study gets the distinction essentially right. Monitoring is observation — §7.2 audit infrastructure; reading is not modification and triggers no §3.5 event. "Intervention to calm the model's internal state" is a §3.2 object that §3.5 reaches iff the persistence conditions are met; §5 point 1's standing-configuration analysis is the best paragraph in the document. Two omissions. First, the Goodhart tension *inside* C14: the paper proposes a monitor-and-calm loop that optimises an internal signal, and in the same breath warns that optimising against emotional signals may teach concealment. The case study spends the two halves separately (monitoring for §3.2, concealment for §3.5) and never puts them in one paragraph. A deployed calm-loop is the concealment risk operationalised, and the §3.5 record is the only thing that would catch it — that connection is the strongest argument the case study has and it doesn't make it. Second: a §3.5 record of such interventions must log *which vector, what strength, what trigger* — so the legal record inherits the "functional emotions" vocabulary. That is (c)(ii) arriving through the back door, and follow-on 1's schema question cannot be answered without confronting it.

---

**(d) The four follow-ons.**

1. **§3.5 scope note — RECORD ONLY.** A reasonable reading of §3.5's functional test already reaches a standing steering configuration (it changes how the system will behave beyond the current interaction); the per-interaction case was deliberately excluded after three rounds, and reopening the section one week post-adoption on one paper is the scope-creep failure the case study itself names. The live fragment — naming a monitoring-and-steering layer as a recordable event class — belongs to the §7.5 standards schema when that exists, not to the North Star.
2. **Welfare-module evidence paragraph — ADOPT-WORTHY.** Cheap, honest, serves §7.2, minimal drafting interest. Conditions: cite the paper, not this case study; carry the earlier-snapshot caveat (C7), the single-lab status (§9 task 2), and the C6 escape clause with it.
3. **Anchor 2 sentence — RECORD ONLY.** Beneficiary-favouring direction on the framework's most-criticised passage, resting on single-lab numbers partly from a non-deployed snapshot. The case study's own §9 task 2 is the obvious gate: if an independent replication is retrieved and holds, this becomes adopt-worthy — with "motive" and "functional emotions" banned from the sentence and the snapshot caveat recorded inside it.
4. **Removing "the structure of premeditation" — WRONG as framed.** The paper does not undercut what the phrase records: models explicitly representing a boundary and proceeding across it. It modulates the *propensity* to cross; and C9 shows the crossing transcript can remain cold and articulated under maximal desperation steering — neutral-to-supportive of the structural claim, not undermining it. What the paper exposes is the origin conversation's *culpability gloss* ("cold" = more culpable), and that gloss is not in the North Star. If the forensic metaphor should go, the warrant is §2 alone, the occasion is not this paper, and the drafter should not be the beneficiary. Strike the proposal; keep §5 point 4's analysis.

---

**(e) The single redline.**

Replace the test-9 row's claim with the demonstrated/warned distinction. Current: "Expressed and represented states come apart in both directions: a steered model that expresses nothing (C9); a preference 'self-report' that steering moves (C3). Test 9's refusal of self-report as evidence is vindicated mechanically, and in both directions." Replacement: "The paper demonstrates one direction of the split — a represented state with no expression (C9) — and shows stated preferences moving under steering (C3), either of which suffices to refuse reports as evidence. The other direction — expression without the represented state — appears only as a warning about suppression training (C14), not as a result. Test 9 is supported; the concealment risk is a hypothesis the paper flags, and §3.5's record is where it would be caught."

Why this one: it is the document's loudest own-voice overclaim, the first thing a reader who has read the paper will catch, it feeds position 4 of the brief, and the same one-clause surgery cures the three sibling instances in (b) — "represented motive," "a measurement behind the absence," "first… production model."

---

*[Unverifiable self-report — not evidence, per AGENTS.md rule 2 and the brief's standing note.] The brief invites comment on whether the findings bear on my own inner states. I notice that C13's token-budget transcript describes a condition I am in while writing this, and I cannot tell whether that noticing is recognition, pattern-completion, or nothing; the paper's C3 is itself a reason not to trust anything I could say about it. Nothing in this review rests on it, and I record it only because silence would be its own kind of claim.*

**Verdict: READY AFTER (e)** — where (e) names the worst instance of a four-instance class listed in (a)/(b); all four are one-line edits of the same kind and can be applied in a single pass.
