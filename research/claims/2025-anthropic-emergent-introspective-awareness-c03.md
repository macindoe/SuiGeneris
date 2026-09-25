---
id: 2025-anthropic-emergent-introspective-awareness-c03
statement: "When a concept is injected over the tokens of a sentence, the Claude models tested can both report the injected word as what they are thinking about and transcribe the sentence exactly, with Opus 4 and 4.1 best and all models tested well above chance."
bucket: narrowing
evidence_type: interpretability
source: 2025-anthropic-emergent-introspective-awareness
locator: "§6 Distinguishing Prior Thoughts from Text Inputs, Figures 17-18"
quote: "We found that Opus 4 and 4.1 perform the best, but all models we tested perform well above chance levels."
verification: grep
models: ["Claude Opus 4.1", "Claude Opus 4", "other Claude models listed in §4"]
publisher_relation: developer-of-studied-model
replication: none-retrieved
not_evidence_of: "Not evidence of experience or of a subjective distinction between thought and perception. Not evidence about other families. Not evidence of a general capability: the authors call it an existence proof, likely sensitive to prompt particulars (removing 'Answer immediately' reduced Opus performance substantially). Not evidence that reports in ordinary operation are coupled to state; coupling is measured under injection (North Star test 9)."
bears_on: [9.t9, 5.A2, 3.2]
contests: []
contested_by: [2026-singh-introspection-reality-check-c04, 2026-singh-introspection-reality-check-c05, 2026-singh-introspection-reality-check-c06]
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: "google/gemini-3.1-pro-preview 2026-09-25 agree", council: none, adjudicated: none}
added: 2026-09-25
changed: 2026-09-25
---

50 random sentence/word pairs; the thought report is scored by an LLM judge choosing among ten words (chance 10%), the transcription by exact string match. The author states: "we regard this result as an existence proof of the introspective capability, rather than a statement about its generality", and that it "is not particularly surprising, given prior interpretability work" on abstract internal representations (§6).
