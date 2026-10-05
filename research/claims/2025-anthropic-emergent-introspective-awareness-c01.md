---
id: 2025-anthropic-emergent-introspective-awareness-c01
statement: "Under concept injection at the optimal layer and injection strength, Claude Opus 4.1 reports detecting an injected concept, before mentioning it, and correctly identifies it on about 20% of trials; on most trials it does not."
bucket: narrowing
evidence_type: interpretability
source: 2025-anthropic-emergent-introspective-awareness
locator: "§5.3 Failure Modes (rates also §2.1, §5.4, Figure 9)"
quote: "In fact, on most trials, they do not–below, we quantify this and show that at the optimal injection strength and layer, Opus 4.1 succeeds on about 20% of trials."
verification: grep
models: ["Claude Opus 4.1", "Claude Opus 4 (similar rate, §2.1)"]
publisher_relation: developer-of-studied-model
replication: independent:2026-lederman-mahowald-content-agnostic; also 2026-macar-mechanisms-introspective-awareness (SHARED AUTHOR with this paper: Lindsey is an advising author of Macar et al.)
not_evidence_of: "Paper: Not evidence of experience or of anything it is like to detect an injection; Paper: Not evidence about models outside the Claude family, or about Claude models not tested; Paper: Not evidence about ordinary operation: coupling here is measured only under an artificial injection the authors say models never meet in training or deployment; Paper: Not evidence that the rest of the model's description of the injection, beyond detection and identification, is grounded (§2.1); Paper: Success is graded by an LLM judge of the same family (Claude Sonnet 4); Framework (test 9, steering): a coupling measured under steering shows that the channel can be steered and does not weight reports offered in ordinary operation"
bears_on: [9.t9, 5.A2, 3.2]
contests: []
contested_by: [2026-singh-introspection-reality-check-c04, 2026-singh-introspection-reality-check-c05, 2026-singh-introspection-reality-check-c06]
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: "google/gemini-3.1-pro-preview 2026-09-25 agree", council: "research-docket 2026-09-26", adjudicated: "2026-10-05 Ben: stays narrowing with the contests recorded (council round 1); partial independent replication linked 2026-09-28"}
added: 2026-09-25
changed: 2026-10-05
---

The authors inject a concept vector into the residual stream (a layer about two thirds of the way through the model) while asking the model whether it detects an injected thought. Success requires affirmative detection, correct identification, detection before the word is said aloud, and coherence, judged by Claude Sonnet 4 over 50 concepts. Production models showed 0 false positives over 100 control trials (§5.1); some helpful-only variants showed high false-positive rates (§5.7). The authors state the protocol "places models in an unnatural setting unlike those they face in training or deployment" (§1).

REPLICATION 2026-09-28 (set by the coordinating session from the two intakes' reports): PARTLY replicated by 2026-lederman-mahowald-content-agnostic-c01 (Qwen3-235B-A22B, Llama 3.1 405B: detection and identification on a minority of trials with zero control false positives; partial because a third-person control attributes detection at many layers to a prompt-specific yes-bias, and the success criterion differs). Also partly reproduced by 2026-macar-mechanisms-introspective-awareness-c01 (Gemma3-27B), which shares an advising author with this paper and is therefore not recorded as independent; the council is asked whether a shared-author replication counts.

CORRECTION 2026-10-05 (council round 1, seven of ten flagged it; Ben, 5 Oct): the statement said the model "notices" the injected concept. What the experiment scores is the model's report that it detects one, so the verb is now "reports detecting". The paper's own word in the quote is unchanged.

REPLICATION 2026-10-05 (Ben): Macar et al. 2026 is to be treated as an independent replication, WITH THIS CALLOUT: it shares one author with this paper (Jack Lindsey, an advising author there, the sole author here), uses his protocol by design, and so is independent in models, judge and released artefacts but not in research group. Lederman and Mahowald 2026 shares no author; it thanks Lindsey for discussions and used a Claude model as grader.
