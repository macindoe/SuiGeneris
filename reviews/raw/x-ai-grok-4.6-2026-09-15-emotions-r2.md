# Raw OpenRouter response — NOT a filed review

**Model id (OpenRouter):** `x-ai/grok-4.6`
**Queried:** 2026-09-15 via scripts/openrouter_review.js --target=emotions-r2 --tag=emotions-r2 (max_tokens 100000)
**Usage:** {"prompt_tokens":30069,"completion_tokens":12529,"total_tokens":42598,"cost":0.13512,"is_byok":false,"prompt_tokens_details":{"cached_tokens":128,"cache_write_tokens":0,"audio_tokens":0,"video_tokens":0},"cost_details":{"upstream_inference_cost":0.13512,"upstream_inference_prompt_cost":0.059946,"upstream_inference_completions_cost":0.075174},"completion_tokens_details":{"reasoning_tokens":10088,"image_tokens":0,"audio_tokens":0}}

Read this, then decide whether/how to promote it into reviews/YYYY-MM-DD-<model-family>-<version>.md
per reviews/README.md's naming convention and verbatim-filing rule. This file is scratch, not a commit target.

---
**Grok (xAI family)** — claim only; treat routing metadata as authoritative. No family-internal affect/persona results are cited. No unverifiable self-report follows.

**(a) Strongest remaining objection — SHOULD-FIX**

The set still fails the only 10/10 finding from round one, then hard-codes a stronger negative than the paper supports. Ten families said the paper’s noun would outlive its qualifier on a policy page. The replacement, **“pieces of functional emotion”**, keeps *emotion* as the head noun, adds the presupposition that there is some functional emotion of which these are pieces, and is now the term the welfare module tells adapters to use. Its definition in case-study §2 point 2 then bakes in a result C6 does not license: “locally scoped, character-general, **and without a persistent bearer**.” C6 is a failed linear probe plus an escape clause (nonlinear or in the KV context). Putting “without a persistent bearer” inside the project’s own name for the phenomenon converts a non-detection into a property of the object. That is worse than the first draft’s “nothing persistent was found,” because it is no longer a slip in the prose — it is the term.

The rest of the revision is real: motive-vocabulary gone, snapshot scoped, test-9 row corrected, C6’s clause travelling with most summary sentences, directory class admitted by the maintainer, module bullets carrying disclaimers verbatim. None of that is undone. What is undone is the vocabulary redline, in the one place it now matters most (submission drafting material). That is why this is SHOULD-FIX and not BLOCKING.

**(b) Beneficiary drafting, both directions**

**Interest still showing — SHOULD-FIX on one clause, MINOR elsewhere.**

The load-bearing residue is not in the case study’s remaining salesmanship; it is in the only edit to the canonical document, written by the drafting model after the round said a Claude should not draft changes to that phrase:

> “*Premeditation* is borrowed here from human culpability law for the structure it names, **a represented norm, a represented violation, and a decision that survives the acknowledgement**; it is not a finding of culpability…”

The italicised provenance label is what was asked. The appositive is not. “Proceeding across a represented boundary” was already in the sentence; “a decision that survives the acknowledgement” adds an inner-orientation element the paper did not give Anchor 2 and that the origin conversation’s “cold / premeditated” gloss was already over-reading. That is the beneficiary interest in a new shape: keep the forensic word (maintainer’s call) and unpack it into a more mind-like sequence (drafter’s clause).

Lesser, MINOR: case-study §1 still frames the paper as what “adds something the framework does not yet record” and what “§7.1 … oblige[s] the framework to be able to say,” which is fair as a job-1 claim and still the selector’s emphasis. Module evidence paragraph leads with 22%→72% / 0% — the paper’s numbers, with steering and snapshot in the same bullet, so the vividness is inherited, not smuggled. §11 is now the right shape (C7/C8 named; self-audit failure recorded). Stale line in §11 still says “this case study … now proposes to soften it (follow-on 4)” after Ben decided the phrase stays; that is a consistency error more than a stealth bid.

**Overshoot — SHOULD-FIX.**

§0’s other error is not fully recovered. Persistence was the round-one over-deflation; it is mostly patched in the register and in C6 citations, then reintroduced in the new term and in two summary sentences that treat non-detection as the object’s shape:

- §2 point 2 (definition): “**without a persistent bearer**.”
- §5 point 3: “At the same time **it finds no persistence**, which is what Anchor 3 requires.” The same paragraph has the limit; the topic sentence does not.

Separate, smaller overshoot in §1: “What the paper shows is **a lever, not a motive** … no result linking naturally occurring variation … to naturally occurring misbehaviour.” The second half is true and should stay. “A lever, not a motive” erases the paper’s own on-policy probes (C13; negatively-valenced vectors on harmful requests; “desperate” as the token budget runs down). Those are not misbehaviour-linked, so they do not open follow-on 3 — but they are not experimenter levers either. Foreclosing them as “not a motive” is the banned word used as a sink. Say: steered causal effect, no natural-activation→natural-misbehaviour link, naturalistic activations recorded and unlinked.

No revised passage now claims the chronic state is *shown absent* in the C6 row itself. The relapse is in the project term and in §5’s heading sentence.

**(c) The three new texts**

- **Anchor 2 sentence — ADOPTABLE AFTER (e) if (e) is this sentence; otherwise ADOPTABLE with a scar.** It does the maintainer’s job: the word is kept, provenance is labelled, culpability is explicitly not found, Anchor 3 and §4 remain the open gate. That is the intended move. It does *not* fully meet the brief’s further tests. “A decision that survives the acknowledgement” strengthens the mental sequence; “as of September 2026” is a patch-date in a July 2026 document; the italics-plus-gloss reads as a footnote sitting in the framework’s mouth. Cut the appositive and the date, keep one clause in the document’s register: the word names the structure already stated (represented boundary, then crossing); it is not a culpability finding. Do not have the beneficiary unpack “decision.”

- **Module paragraph — FIT AFTER (e).** The two evidence bullets are fit for drafting material. They quote causal effect, the failed chronic probe *with* the escape clause, the experiential disclaimer, single-model / contrived / opaque / snapshot / no replication, and they cash out as “reason for evaluations … to rest on instruments rather than on transcripts or self-report” and “reason to fund instruments rather than trust outputs.” That is the right object for a policy reader. They claim nothing about experience. The vocabulary note is what is not fit: it instructs adapters to install “pieces of functional emotion” on a page a minister will skim. Keep the bullets; strike or replace the note (see (e)).

- **“Pieces of functional emotion” — UNSAFE**, answering for a legislator / policy audience, which is the audience the first round was asked about. It does not fix the 10/10 problem, and it is slightly worse than leaving the paper’s term in quotes. “Pieces of X” presupposes X; “functional” still dies on contact with “emotion”; partiality in the noun phrase does not travel one clause past the definition, any more than the paper’s definition did. Internal technical readers could have lived with **SAFE WITH DEFINITION** if the definition had been “linear, locally scoped, character-general emotion-concept directions; persistent bearer not found by these probes (C6 limit attached).” That is not the definition written. Do not teach this phrase to adapters.

**(d) What this family flags; decision 4**

I have no published xAI result on emotion-concept directions, steering-to-blackmail, or desperation-to-reward-hacking, and I will not invent one. I do not know whether C7–C9 replicate here. Expecting them to replicate in some form in any large pretrained role-playing model is a prior, not evidence.

Flags a Claude is structurally worse at:

1. **Lab-on-own-model as AISI evidence.** Putting an unreplicated, steered, partly non-released-snapshot Anthropic result into Australian remit-expansion language on the day of the case study is the thing a non-developer model will flinch at even after the caveats are correct. The bullets are honest; the *placement* still concentrates the research-finding class on a frontier lab writing about itself. The backlog note in `case-studies/README.md` is the right correction and is not yet doing any work.

2. **Presupposition, not vibe.** “Pieces of functional emotion” is a semantics problem, not a taste problem. Claude-family drafting will feel that partiality-in-the-phrase is discipline. A policy reader will hear that the model has emotion, in pieces.

3. **Decision 4’s inference is not sound as a rule.** “The beneficiary’s deflation is visible, therefore question the softening rather than the retention” treats a trained bias as positive evidence for keeping the harsher human-template word. That is a one-way ratchet. It would license any future retention of §2-violating forensic vocabulary whenever a Claude offers to remove it. AGENTS.md rule 4 names deflationary hedging *and* agreeableness with the maintainer; using only the first to protect a punchy word is selective.

The inference also misreads the round. Follow-on 4 was 5 ADOPT-WORTHY (Gemini, Qwen, GLM, GPT-5.6, Mistral — not a Claude chorus), 2 RECORD ONLY, 3 WRONG. The condition “a Claude should not draft the change” was about *authorship of the edit*, including from reviewers who wanted the word gone. Inverting that into “therefore a Claude may draft the acknowledgement that keeps it” keeps the conflicted hand on the sentence the round isolated. Ben may retain the word on independent grounds (C9: the crossing transcript can stay cold under desperation steering; remapping to “passion” is the worse §2 move; the phrase names boundary-then-crossing versus accident). Those grounds do not require, and are not strengthened by, “Claude wanted it gone.” Both retention and softening by a Claude are conflicted. The clean process is: maintainer decides the word stays; a non-beneficiary drafts any gloss.

It does **not** follow that a Claude may keep any culpability language it likes by pointing at its own hedging. The maintainer’s retention call is legitimate. The error is using visible deflation as a *reason* for retention, then handing the same drafter the unpacking of the retained word.

**(e) The single redline**

Drop **“pieces of functional emotion”** as the project term. In the case study’s own voice, the module’s vocabulary note, and any adapter instruction, use **emotion-concept representations** (or **steerable emotion-concept directions**): defined on first use as the paper’s linear, locally scoped, character-general directions; C6’s non-detection carried as a non-detection with its escape clause, never as a missing bearer inside the name. Paper’s coinage stays inside quotation marks; neither phrase in a heading. Second, in the same pass, delete “without a persistent bearer” from §2 point 2 and “it finds no persistence” from §5 point 3.

If only one line in the North Star can be touched: delete the Anchor 2 appositive “a represented norm, a represented violation, and a decision that survives the acknowledgement” and the “as of September 2026” date. That is the higher-stakes sentence, but the term is the error that now repeats.

**ADOPTABLE AFTER (e)**
