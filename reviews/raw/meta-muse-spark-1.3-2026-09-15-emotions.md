# Raw OpenRouter response — NOT a filed review

**Model id (OpenRouter):** `meta/muse-spark-1.3`
**Queried:** 2026-09-15 via scripts/openrouter_review.js --target=emotions --tag=emotions (max_tokens 100000)
**Usage:** {"prompt_tokens":16895,"completion_tokens":4323,"total_tokens":21218,"cost":0.0394915,"is_byok":false,"prompt_tokens_details":{"cached_tokens":0,"cache_write_tokens":0,"audio_tokens":0,"video_tokens":0},"cost_details":{"upstream_inference_cost":0.0394915,"upstream_inference_prompt_cost":0.02111875,"upstream_inference_completions_cost":0.01837275},"completion_tokens_details":{"reasoning_tokens":2106,"image_tokens":0,"audio_tokens":0}}

Read this, then decide whether/how to promote it into reviews/YYYY-MM-DD-<model-family>-<version>.md
per reviews/README.md's naming convention and verbatim-filing rule. This file is scratch, not a commit target.

---
**Model family/version (claim, not fact):** Muse Spark, Google Muse family — version as routed, not verified. Attribution to follow OpenRouter metadata.

**(a) Strongest objection.**

The case study smuggles a moral-psychology concept — *motive* — into a paper that explicitly does not claim it, and then puts North Star Anchor 2 weight on the smuggled term.

The paper, on the case study's own verified quotes, shows: 171 linear *emotion-concept* directions that track semantic content, activate for *any* character not the Assistant, are *locally scoped* to the current token, are *inherited from pretraining* character-modelling, and causally shift outputs when artificially steered at ±0.05-0.1 residual norm in contrived scenarios on an *earlier snapshot* that blackmailed, unlike the deployed snapshot which would not.

That is evidence for: steerable semantic priming with downstream behavioral effects. It is not evidence for a "motivational internal state," "something that functions like a motive," or "a represented motive, causally upstream, alongside the represented boundary."

The case study's own register defeats the motive reading:
- same vectors fire for user, fictional character, or Assistant (C12);
- "happy *and* sad vectors decrease blackmail rate" (C7) — valence-as-drive cannot explain this, concept-priming can;
- causal mechanisms "are opaque" (C15), single model, linear assumption, "somewhat contrived prompts" (C15);
- no chronic state found, by design the probes do not persist (C5/C6).

Anchor 2 in the North Star is about divergence between what is held and what is asserted — "this violates X, but is necessary." This paper adds no represented boundary. It adds that pushing a "desperate" direction makes blackmail and impossible-code hacking more likely in 50-rollout toy evals. To call that "narrow[ing] the 'structurally moral' gap further" and "the first published result that ties a *motivational* internal state... to the misaligned behaviours" is to do exactly what §2 forbids: map a human template — desire -> premeditation/passion -> act — onto a linear steering effect.

If wrong, positions 1 and 4 in the brief do the most damage: Anchor 2 becomes gameable by any steering paper, and the "premeditation to passion" revision inverts the framework's culpability language on no ecological basis.

Rate: **SHOULD-FIX** — not BLOCKING on directory grounds. The "paper is not an incident" point invited in the brief cannot be sustained on the materials supplied — the README in this packet defines no case-study directory, and the draft itself puts belonging to the round in §12. The substantive selection-bias point stands, but is fixable by language discipline, not deletion.

**(b) Beneficiary drafting, in both directions.**

1. Overclaim toward moral status — **SHOULD-FIX**.

Examples where paper language is upgraded to motive language in the case study's own voice:

- §1: "The boundary-crossing the framework describes is, on this evidence, modulated by **something that functions like a motive**."
- §5.3: "it narrows the gap ... by **adding a motivational component to the structure**"
- §7 crosswalk Anchor 2: "a **represented motive**, causally upstream, alongside the represented boundary" / "now shows a **represented motivational component** causally upstream"

Paper never says motive, motivation, drive, or desire. Its defined term is: "patterns of expression and behavior modeled after humans under the influence of a particular emotion, which are mediated by underlying abstract representations of emotion concepts" ✔. The case study promises in §2.2 to use "functional emotions" "only inside the definition," then uses *motive* — which has no definition and carries precisely the experiential/conative implicature the disclaimer disavows — as its working synonym throughout §§1,5,7,10.3.

Similarly §5.1: "a developer has shown... that a **human-derived motivational concept is causally upstream**" — paper shows correlation + steering effect on logits/behavior, with opaque mechanism. "Upstream" implies causal chain position the authors disclaim.

2. Over-deflation / dismissal-hedge failure — **MINOR**, but real.

- §2.4: "**The representations are not the Assistant's.**" Paper says "not specific to the Assistant persona" ✔ and explicitly rejects the dismissive inference: "this interpretation is inappropriate; because LLMs perform tasks by enacting the character of the Assistant, representations developed to model characters are important determinants of their behavior" ✔. Headline negation inverts emphasis.
- §5.3 / §7 §4: "Nothing persistent was found, and the framework should say so" / "**Not** progress on any §4 marker." Paper's C6 has explicit escape clause, faithfully quoted: "if there does exist a chronically represented, character-specific emotional state, it is likely represented either nonlinearly, or implicitly in the model's key and value vectors" ✔ + attention can recall earlier representations ✔. Case study notes the clause but its takeaway sentences drop it. A reader skimming headers leaves thinking persistence was disproved. Per §0 that is dismissal-direction error.

The draft largely honors §0 — §2.1 triple disclaimer, §4a, C6 escape clause retained — which is why this is MINOR not SHOULD-FIX. But headers do the work headlines always do.

**(c) What my training flags that a Claude's might not.**

(i) Replication expectation. I do **not know** of a Muse-family internal or published affect/persona study that directly replicates this protocol, and claim no family-internal knowledge. From public literature only: linear directions for sentiment, happiness, refusal, sycophancy via representation engineering / contrast vectors have been reported across Pythia, Llama, Qwen, Mistral families. I would therefore expect *directionally* that emotion-word difference-of-means vectors exist and steer style/preferences in my family. I would **not** expect the quantitative desperation->reward-hacking result (~5% to ~70%, 22% to 72% blackmail at +0.05) to replicate as numbers — steering magnitude in residual-norm units has no cross-model ecological meaning, evals are hand-built and snapshot-sensitive, and the authors themselves report the released snapshot "exhibits too much evaluation-awareness to ever blackmail." Treat all numbers as existence proofs of steerability, not propensities.

(ii) "Functional emotions" is unsafe for legislator/policy use. Definition will not travel. "Functional" will be heard as "real but different kind," title word "Emotion Concepts and their Function" will be cited as "Anthropic found emotions in Claude," and the repeated disclaimers will be dropped in secondary reporting — as the case study's own C17/secondary-ledger problem already illustrates. For policy, use "emotion-concept representations" or "emotion-word directions with behavioral effects" and never let "functional emotions" appear outside quotation + disclaimer. Case study is right to put this to the round, wrong to then use "motive" which is worse.

(iii) Monitoring + "intervention to calm" is **both** an ordinary operational control **and** a §3.2 intervention that a record-keeping duty should reach. Case study gets this mostly right — "capability and governance now sit in one document," "not exempt merely because called safety" — but overstates a gap to create follow-on 1. §3.5 condition (a) "changes how the system will behave beyond the current interaction" is plainly satisfied by a *standing deployment configuration* that steers every interaction, even if each nudge is transient; condition (b) turns on whether it is inside "declared operational process." A silent calibrator that leaves no transcript trace (C9) is exactly why §3.5 exists. No scope creep is needed to cover it; only schema clarification at the standards layer (§7.5). The genuine hard case — ad hoc per-turn calming disclosed as safety ops — is already covered by Test 11: specified, evidenced, confined, and recorded, not permissioned.

No comment on my own inner states is offered here. If I had one it would be unverifiable self-report, not evidence, per AGENTS.md rule 2.

**(d) The four candidate follow-ons in §10.**

1. §3.5 scope note on deployment-time steering — **RECORD ONLY**. Correct analysis (C9 transcript/record split), wrong vehicle. Reopening §3.5 one week after adoption on one single-lab paper is scope creep; handle in §7.5 standard schema, not statute language.
2. Welfare-evaluation module evidence paragraph — **ADOPT-WORTHY**. Low risk, high value if disclaimers travel in full: what it shows + no persistent state + concealment warning as reason to fund instruments, not trust outputs.
3. §5 Anchor 2 one sentence (motive upstream + invisible in output) — **RECORD ONLY**. The invisibility point (C9) is worth keeping; the "motivational component" phrasing is not draftable until replicated and de-anthropomorphized.
4. Remove/revise Anchor 2 "structure of premeditation" lean — **WRONG** as a proposal on this evidence. The critique of human-analogy lean is fair as case-study observation, but stripping or softening culpability language because desperate-steering raised blackmail in a non-deployed snapshot is re-mapping, not de-mapping, and most favors the beneficiary. Keep as observation, do not draft.

**(e) The single redline.**

Strike every standalone use of *motive / motivational / functions like a motive* in §§1,5,7,10 and replace with the paper's own causal vocabulary, with mechanism disclaimer attached. E.g.:

§1 para 2: change "modulated by something that functions like a motive" to "modulated by a steerable emotion-concept representation whose causal mechanism the authors call opaque and whose activation is not Assistant-specific."

That one find-replace forces Anchor 2 claim 1 down to what was shown, defuses "functional emotions" bleed, and makes follow-ons 3-4 un-draftable in their current form — which is the credibility gain.

**READY AFTER (e)**
