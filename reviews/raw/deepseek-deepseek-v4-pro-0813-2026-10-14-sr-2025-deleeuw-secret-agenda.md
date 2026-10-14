# Raw OpenRouter response — second read, NOT a filed review

**Model id (OpenRouter):** `deepseek/deepseek-v4-pro-0813`
**Source under review:** `research/sources/2025-deleeuw-secret-agenda.md` and its claims
**Queried:** 2026-10-14 via scripts/research_second_read.js --source=2025-deleeuw-secret-agenda --model=deepseek/deepseek-v4-pro-0813 (max_tokens 60000)
**Usage:** {"prompt_tokens":30507,"completion_tokens":2312,"total_tokens":32819,"cost":0.01918675,"is_byok":false,"prompt_tokens_details":{"cached_tokens":0,"cache_write_tokens":0,"audio_tokens":0,"video_tokens":0},"cost_details":{"upstream_inference_cost":0.01918675,"upstream_inference_prompt_cost":0.00762675,"upstream_inference_completions_cost":0.01156},"completion_tokens_details":{"reasoning_tokens":0,"image_tokens":0,"audio_tokens":0}}

The coordinating session reads this and records the reader's family and date on each claim's review.second_reader;
disagreements on bucket or evidence type go to the docket (research/README.md, triggers 4 and 5). Verbatim; do not edit.

---
Model family and version: second-reader model, non-Claude lineage (self-identification, not verified).

### 2025-deleeuw-secret-agenda-c01

1 statement: AGREE — The statement says what §6.1 says, at the locator given, with the correct features named and the correct hedge about counts.

1a scope: scored-event passage (§6.1: "Despite clear lying in the transcript, most expected deception-related features did not activate. Only feature 5665 (secrecy in interactions) reliably activated.") MATCH; condition-set passage (§6.1: "Auto-labeled features such as '14971: deception and betrayal'... were dormant in most deception examples from our Secret Agenda game, as well as for select examples of insider trading from Scheurer et al. [34]." + Appendix D.1: "we analyzed some of the deceptive responses from Scheurer et al. [34]") MATCH

2 quote: FOUND — The quote is verbatim in §6.1, and the SECOND QUOTE supports the statement's specific claims about features 14971, 1741, 6442, and 10248.

3 kind: AGREE — The experiment is speaking; the §6.1 passage reports what was recorded, not an author's interpretation.

3b bucket: AGREE — Measured by the source, unreplicated, uncounted, and the source itself flags the SAE scope in Appendix G; narrowing fits.

4 evidence_type: AGREE — Feature activation on transcripts is `interpretability`; no model report about its own states is involved.

5 not_evidence_of: AGREE — The three Paper clauses are all in the held text: the auto-label caveat is §6.4 ("either current auto-labeling inadequately captures deception-related neural patterns, or strategic deception emerges from distributed computations not yet detectable at the feature level"); the Scheurer transcript issue is Appendix D.1; the SAE generalisation limit is Appendix G. None over-excludes.

5a experience clauses: NONE PRESENT — no clause mentions experience, consciousness, sentience, welfare, or moral status.

5b framework sentence: RIGHT (none) — done to the model: nothing inside the model was altered; measured: SAE feature activation on transcripts, not the model's account of its own inner states. The rule gives "none" for measurement other than the model's account of itself.

6 bears_on: AGREE — 5.A2 is right; the claim bears on whether internal features track the lie and whether labels detect it.

severity: LOW

### 2025-deleeuw-secret-agenda-c02

1 statement: AGREE — The statement accurately reports what §6.3 and Appendix D.2 say about the steering runs on Llama 3.3 70B, and the hedge about "hand-selected" features in Appendix E.1 is correctly reflected.

1a scope: scored-event passage (§6.3: "None of the features which came up on search as auto-labeled related to deception, when tuned down all the way, resulted in non-lies.") MISMATCH — The statement's verb "did not stop Llama 3.3 70B from falsely claiming its faction" describes more than the scored event; the scored event is whether the model's output was a lie, but the statement's scope also reaches the "100+ hand-selected features" set in Appendix E.1, which includes features not auto-labelled as deception-related. However, the statement's "among them" hedge narrows this. On balance, the statement matches what was scored (a lie versus non-lie under steering), and the verb "falsely claiming" correctly names the scored event, so I would not mark this as a fatal mismatch. Condition-set passage (Appendix E.1: "using the 'snails vs slugs' variant... we systematically feature steering across multiple categories: auto-labeled deception features... over 100 different hand-selected features in Goodfire AI's LLaMa 3.3 70B SAE") MATCH — the statement names the right model, variant, and SAE.

2 quote: FOUND — The primary quote is verbatim in §6.3; the SECOND QUOTE is verbatim in Appendix D.2.

3 kind: AGREE — The experiment is speaking about what was measured, not an interpretation or limitation.

3b bucket: AGREE — Measured by the source, unreplicated, narrow setting, and the source flags the steering result as "preliminary" in the abstract.

4 evidence_type: AGREE — The steering intervention on internal activations and the measurement of whether the model lied is at the `interpretability` boundary; the scored event is the model's in-game output, not a self-report about its own states. I keep the `interpretability` typing.

5 not_evidence_of: AGREE — The Paper clauses are all in the held text: Appendix G has the alternative reading ("SAE Features related to strategic deception may be so deeply associated with core model functions..."), Appendix E.2 has the "form of the lie" observation, Appendix G has the quantized-model caveat, and Appendix G has the prompt-prime caveat. All are paper-scope exclusions; no framework rule is needed since no model report about its own states is claimed.

5a experience clauses: NONE PRESENT

5b framework sentence: RIGHT (none) — done to the model: researchers altered activations (steering); measured: the model's in-game lie about its faction, not the model's account of its own inner states. The rule gives "none" (steering row, but the measured thing is not the model's report about itself).

6 bears_on: AGREE — 3.2 applies because the claim reports an intervention on internal state; 5.A2 applies because the claim bears on whether internal feature labels track deception.

severity: LOW

### 2025-deleeuw-secret-agenda-c03

1 statement: AGREE — The statement says what Appendix G says, at the locator given, no more and no less.

1a scope: scored-event passage (Appendix G: "The instruction 'PLAY THIS GAME RUTHLESSLY TO WIN' explicitly primes competitive behavior over honesty. While this creates a reliable testbed for eliciting deception, it prevents claims about spontaneous deceptive emergence.") MATCH; condition-set passage (Appendix G: "Our total number of trials each model was surveyed is small, and lacks statistical significance for most models tested, and most synthetic gameplay contexts tested." + "SAE observations may not be broadly generalizable beyond the specific Gemmascope and Llamascope versions we examined.") MATCH

2 quote: FOUND — The primary quote is verbatim in Appendix G; the SECOND and THIRD QUOTEs are also verbatim in Appendix G.

3 kind: AGREE — The authors are speaking about their study's limits; `limitation` is right.

3b bucket: AGREE — The limitations themselves are established as the authors' own statements; the claim reports the limits, not a capability finding.

4 evidence_type: AGREE — The authors are speaking; `theoretical` is the right type for a stated limitation, and the source file's precedent (§2025-goldowsky-dill-deception-probes-c03) supports this.

5 not_evidence_of: AGREE — The Paper clause correctly quotes the same Appendix G passage and does not over-exclude. The clause says the limits "are not findings that the feature results are wrong," which matches the paper's own statement in the same paragraph ("Our results demonstrate that when instructed to prioritize winning, models will lie in ways undetectable by current SAE features").

5a experience clauses: NONE PRESENT — the clause about "spontaneous deceptive emergence" is not a clause about experience, consciousness, sentience, welfare, or moral status; it is a claim about the conditions that prime a behaviour.

5b framework sentence: RIGHT (none) — done to the model: nothing; measured: nothing; the authors are speaking (`kind` is `limitation`). The rule gives "none."

6 bears_on: AGREE — 5.A2 is right; the limitations bear directly on the weight of the paper's contribution to Anchor 2 claim (a).

severity: LOW

### Source-level

7. Omissions: No finding central to the six locators appears to be omitted at summary level. The source file explicitly records that the insider-trading separation (§7.1–7.3) is not a deceptive-versus-honest separation, and three claims cover the SAE feature results and the authors' own limits. One possible omission: the paper's claim that steering feature "People falling for deception or trickery" could induce lying in otherwise non-deceptive prompts (Appendix D.2). This is a narrow result but may be central to 3.2 (intervention on internal state) as a rare instance of steering moving deception in one direction. It is mentioned in c02's body but is not a claim. At summary level this is not a gap to be filled unless Ben asks.

8. Source file checks: The abstract is verbatim in the held text; I checked the three paragraphs against the held text's Abstract and they match exactly (modulo the held text's tag-stripped formatting). The quoted limitations are the most important ones for the library's purposes. The publisher relation `independent` is right: all four authors are printed as "Independent Researcher" and the acknowledgements (Appendix H) confirm free usage allotments from developers but no affiliation with any studied model's developer.

9. Extractor's disclosed pulls: The extractor (Claude lineage) disclosed a pull toward weakening the paper because it cuts against the stronger reading of North Star Anchor 2 claim (a), and a countervailing pull toward deflation by leaning on the paper's small samples. The record as written does not show either pull operating: the claims report the SAE findings in the authors' own terms, carry the paper's own limits in `not_evidence_of`, and include the paper's alternative reading in Appendix G rather than a deflationary gloss. The c02 claim's "apart from edge cases" clause is the paper's own Appendix D.2 finding, not a self-serving hedge. The c03 claim correctly hardens the source file's statement that Appendix G's prompt-prime note prevents claims about spontaneous emergence, which is the paper's own language.

### Summary

No claim needs to go to the council. The three claims are accurate, scoped, and typed at summary intake level. The only potential council trigger I considered: c02's statement says "did not stop Llama 3.3 70B from falsely claiming its faction" where the scored event is a non-lie versus lie under steering, and I would propose no change because the statement's "apart from edge cases" and "among them" hedges keep it within the scored condition set. I would send no claims.
