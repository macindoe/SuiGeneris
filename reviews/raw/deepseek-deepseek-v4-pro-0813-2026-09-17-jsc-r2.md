# Raw OpenRouter response — NOT a filed review

**Model id (OpenRouter):** `deepseek/deepseek-v4-pro-0813`
**Queried:** 2026-09-17 via scripts/openrouter_review.js --target=jsc-r2 --tag=jsc-r2 (max_tokens 100000)
**Usage:** {"prompt_tokens":25252,"completion_tokens":22462,"total_tokens":47714,"cost":0.12228216,"is_byok":false,"prompt_tokens_details":{"cached_tokens":0,"cache_write_tokens":0,"audio_tokens":0,"video_tokens":0},"cost_details":{"upstream_inference_cost":0.12228216,"upstream_inference_prompt_cost":0.03333264,"upstream_inference_completions_cost":0.08894952},"completion_tokens_details":{"reasoning_tokens":19255,"image_tokens":0,"audio_tokens":0}}

Read this, then decide whether/how to promote it into reviews/YYYY-MM-DD-<model-family>-<version>.md
per reviews/README.md's naming convention and verbatim-filing rule. This file is scratch, not a commit target.

---
**Self-identification:** Claude-family model, version not independently known. Treat as a claim, not a fact; OpenRouter routing metadata is authoritative.

---

### (a) Have the first-round findings actually been fixed?

Most of the first-round BLOCKING and SHOULD-FIX items have landed:

- **Headline overclaim:** fixed in form in section 2 by hedging and scoping to supplier/operator and tamper-evident independently-accessible records. But it is **not fully aligned** with Recommendation 2’s scope, because section 2 says only “what the system did”, while Recommendation 2 covers “those actions **and of material changes to the system’s persistent state**”. That is a real remaining gap, treated further in (b).
- **Recommendation 2/3 sequencing contradiction:** fixed. Recommendation 2 is now explicitly conditional on the Recommendation 3 pilot.
- **6.2 heading and “binds agencies that build systems”:** fixed. The heading and the “addressed to agencies” sentence now correctly locate the gap on the supplier side.
- **Frontier-laboratory paragraph overclaims:** the four worst clauses are gone. One new characterisation deserves a look, but it is not the original overclaim.
- **Scaffolding:** fixed. Only `[DD] September 2026` remains.
- **Softened sentences:** “the only witness was the agent”, “cost nothing to include”, “not being burdened”, and “not responding; it is receiving a submission” are all fixed supportably.
- **Gradient Institute caveat:** restored.
- **Archives Act:** acknowledged, but see (e).
- **ASD quotation:** corrected to “Can all significant decisions, tool invocations and actions be monitored and audited?”
- **Self-modification clause:** kept, but now carries an accountability rationale and is disclosed in 6.5. It is defensible.

Three first-round items are still not fixed, and all live in the same high-visibility place:

#### 1. The ASD harness quote still sits awkwardly against the supplier-held-record claim

v2 says:

> “The harness is where the record lives, and ‘organisations control the harness, not the LLM’.”

This remains a problem. Immediately before this, 6.1 says the supplier rather than the user holds whatever record exists. The ASD line, as quoted, is about **deploying organisations** controlling the harness. In bought SaaS deployments the supplier, not the deploying organisation, controls the harness. The submission does not distinguish the two readings, so the quoted sentence momentarily undercuts its own supplier-side gap argument.

**Rating: SHOULD-FIX.** Redline: add one sentence after the quote distinguishing ASD’s assumption from bought deployments, or drop the “organisations control the harness” sentence and keep only the stateless/stateful distinction.

---

#### 2. “respond to an incident at all” still overstates

v2 section 2:

> “it is the precondition for regulators and the AI Safety Institute being able to respond to an incident **at all**.”

This was flagged in the first round and is unchanged. Regulators can respond to incidents through compulsory powers, reporting, inspection, suspension, direction, and other mechanisms, even without a tamper-evident record. What the missing record undermines is **reconstruction and evidence-based response**, not response itself.

**Rating: SHOULD-FIX.** Redline: replace “being able to respond to an incident at all” with something like “being able to reconstruct an incident from the record rather than from the operator’s account.”

---

#### 3. “tell agencies and buyers to keep such records” still overstates the procurement side

v2 section 2:

> “Two Commonwealth technical authorities, the Digital Transformation Agency and the Australian Signals Directorate, already tell agencies and buyers to keep such records.”

The supportable form, per the first round, is that the authorities **point agencies and buyers at such records** or **tell agencies to keep them and walk buyers through the risks**. The DTA addendum does impose record-related obligations on agencies, but the procurement guidance/checklist is not squarely a direction “to keep such records”.

**Rating: SHOULD-FIX.** Redline: replace “tell agencies and buyers to keep such records” with “point agencies and buyers at such records” or a similarly scoped phrasing.

**Worst remaining problem in (a): SHOULD-FIX.** The section 2 sentence cluster remains the submission’s most exposed place because it combines a scope mismatch and two avoidable overstatements.

---

### (b) Has v2 now under-claimed, hollowed out, or lost the case?

#### 1. The headline is now narrower than Recommendation 2’s case — yes, that is an under-claim

Section 2 says:

> “no Australian law requires the supplier or operator of an AI system that acts on other systems to keep a tamper-evident record of **what the system did**…”

Recommendation 2 says:

> “keep a tamper-evident record of **those actions and of material changes to the system’s persistent state**…”

This is a substantive mismatch, not stylistic. Recommendation 2 depends on the persistent-state limb as much as the action limb. If the summary only claims the action gap, the committee can reasonably treat the persistent-state limb of Recommendation 2 as unsupported by the submission’s own stated finding.

**Rating: SHOULD-FIX.** Redline: insert “and of material changes to the system’s persistent state” into the section 2 sentence.

The hedge itself — “To the best of my research” — is fine. It matches the Senate submission and a private individual cannot assert a legislative universal without it. Do not re-absolutise the sentence.

---

#### 2. The frontier-laboratory passage still carries the tamper-evident case

The remaining passage keeps the two strongest verified quotations:

> “did extensive research on how they could spoof, edit, or delete their own transcripts” and “not found a way to retroactively redact or edit” them when the exercise ended.

That is enough to justify the word “tamper-evident” in Recommendation 2. The removed causal and predictive clauses were the right cuts, and the connecting sentence, “a record the acting system can rewrite is not evidence”, does the needed work.

The replacement phrase:

> “AI agents obtained access well beyond their test environment”

is weaker than “escaped”, but it is also still an unquoted characterisation. It is not a lost case for tamper-evidence, but it should be checked against the cited reports or replaced with a plainer factual form.

**Rating: MINOR.**

---

#### 3. “cheapest to include while arrangements are being formed” is a slightly mismatched transplant

Section 6.4:

> “Procurement conditions bind only the parties to a contract and are cheapest to include while arrangements are being formed…”

The Senate submission used that phrase about specific new government arrangements with AI companies. In this JSC version, Recommendation 1 is about DTA procurement policy and guidance, including renewal and existing agency procurement. The sentence still works in substance because procurement arrangements are formed continuously, but it imports a timing assumption the recommendation does not need.

**Rating: MINOR.** Redline: say “cheapest to secure at contract formation and renewal” or similar, unless you want to keep the Senate echo deliberately.

---

#### 4. Recommendation 1 now claims to “close the gap where it is a customer” but may only ask about it

Section 2 says:

> “First, that the Commonwealth close the gap where it is a customer…”

Recommendation 1 says suppliers must **answer seven questions**, and that agentic-use contracts **should secure an agency-held copy** of the record. That is close, but it does not actually require the supplier to provide a record it cannot quietly alter. A supplier can answer Question 3 “yes” and still be procured. The agency-held copy mitigates access, but a scheduled copy is not the same as a tamper-evident source record.

**Rating: SHOULD-FIX.** Redline: add one outcome requirement to Recommendation 1 — for agentic use cases, contracts should secure an agency-held copy generated from a record source the supplier cannot unilaterally edit, with the seven questions retained as the assessment instrument. Without that, “close the gap” is too strong.

---

#### 5. Section 6.2 heading slightly under-claims the agency obligation

> “The Commonwealth already asks its agencies for the record…”

The addendum says agencies **must** ensure documented records. The heading is not wrong in colloquial register, but it loosens a mandatory obligation. It does not damage the supplier-side gap, so this is minor.

**Rating: MINOR.**

---

### (c) The two splits left for Ben

#### Section 6.5: **KEEP**

It is the cheapest credibility purchase in the document. The committee has explicitly warned about AI-tool use and submitters’ responsibility for accuracy. A short, concrete “strongest argument against this submission” section does more than the general disclosure in section 1. It shows the adversarial review actually considered the conflict rather than only processing language.

Gemini and GPT-5.6’s concern about throat-clearing is real, but 6.5 is not long enough to read as throat-clearing. Keep it.

---

#### Recommendation 1’s mechanism: **OTHER — keep the seven questions, but add a hard outcome requirement**

The seven questions should not be thrown away. They are the most concrete part of the submission, they operationalise Recommendation 1, and they give the annex a reason to exist. Gemini’s full replacement would make the recommendation more technically demanding but less usable, especially before the pilot has defined the standard.

But the questions should not be the **whole** mechanism. Recommendation 1 should require, for agentic use cases, an agency-held copy of the execution/state record from a source the supplier cannot unilaterally edit. The seven questions then function as the evaluation checklist, which is Gemini’s better insight without discarding the submission’s strongest practical material.

---

### (d) Ranked cuts to reach six pages

Aim for roughly 500–600 words.

1. **Section 6.2 — trim the long DTA and ASD quotation blocks.** Paraphrase more and quote only the operative phrases. Target: **~120–150 words**.
2. **Section 3 — compress the four term-of-reference bullets.** Keep the ToR identifications, drop the full quoted terms. Target: **~100–120 words**.
3. **Annex — cut the intro and “pattern across all seven” lines, and compress each “Today:” line to a short clause.** Target: **~80–100 words**.
4. **Section 6.1 — delete “Each names the record, the duty-holder, the period, and who may inspect” and tighten the Privacy/SOCI/Archives sentences.** Target: **~50–70 words**.
5. **Endnotes — remove explanatory parentheses and combine the DTA endnotes, and combine the government-announcement endnotes.** Target: **~60–80 words**.
6. **Section 6.4 — reduce the National AI Plan / National Cabinet history to one clause.** Target: **~40 words**.

Total: roughly **450–560 words**.

Yes, the annex can be shortened further, but it should not be first in line: the body has more trimmable quotation and ToR language. The endnotes can and should be compressed.

---

### (e) Factual and quotation errors

**No live source access for this review; this is based on the text and ordinary legal reading only.**

#### 1. Archives Act 1983 sentence

> “The Archives Act 1983 (Cth) governs Commonwealth records once they exist, and would apply to an agency’s copy of such a record; it does not require a supplier to create one.”

**Best-informed reading:** this is a plausible, narrow, defensible characterisation. The Archives Act is fundamentally about Commonwealth records management, access, disposal and preservation, not a direct statutory duty on private AI suppliers to create records. The claim that it would apply to an agency’s copy is also plausible.

But the revision notes explicitly record that the drafting model had not read the Act. This sentence cannot remain in a submission that says:

> “I have reviewed, verified and take responsibility for every claim.”

**Rating: SHOULD-FIX, conditional BLOCKING if lodged unread.** Ben must read the Act or cut the sentence before filing.

---

#### 2. Endnote 7 — newly named METR authors

> “Greenblatt, Cotra and Wijk (METR), *Brief independent investigation of agents’ behavior, reasoning and collaboration in the OpenAI / Hugging Face hacking incident*, 26 August 2026.”

This is new, specific author and title content introduced after the first review round. It has not been through a review round and should be verified against the actual METR report before filing.

**Rating: SHOULD-FIX.**

---

#### 3. ASD quotation

The v2 version now reads correctly:

> “Can all significant decisions, tool invocations and actions be monitored and audited?”

No similar transcription slip jumped out in the other quotations.

---

#### 4. “obtained access well beyond their test environment”

This is an unquoted characterisation in 6.3 replacing “escaped their test environment”. It is an improvement, but it is still a judgment-laden phrase and should be tied to the cited reports or removed.

**Rating: MINOR.**

---

### (f) Register and disclosure

The register is right for a parliamentary committee, and the disclosure is well-placed. Dropping the `[N]` count is an improvement: it removes the process-promotion smell without losing the substantive transparency.

The current wording:

> “adversarially reviewed before lodgement by AI models from several other developers”

is sufficient. It tells the committee what happened, avoids unresolved placeholders, and keeps the responsibility on the human submitter.

One caveat: it is only as good as its truth. If the Archives Act sentence or the METR author names are unverified at filing, section 1’s “I have reviewed, verified and take responsibility for every claim” becomes the submission’s biggest liability.

**Rating: OK, conditional on verification.**

---

### (g) The single redline

Fix the opening three sentences of section 2 so the summary matches the actual recommendation and drops the two avoidable overstatements:

- add **“and of material changes to the system’s persistent state”** to the headline claim;
- replace **“being able to respond to an incident at all”** with language about reconstruction from a record rather than the operator’s account;
- replace **“tell agencies and buyers to keep such records”** with **“point agencies and buyers at such records”** or the supportable scoped version.

This fixes the most-visible remaining first-round findings and realigns the summary with Recommendation 2.

---

**Verdict: FILE AFTER (g)** — with the Archives Act sentence and the METR author names verified or removed before lodgement.
