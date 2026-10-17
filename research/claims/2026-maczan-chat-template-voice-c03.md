---
id: 2026-maczan-chat-template-voice-c03
statement: "The author concludes that what models say about themselves is not a fact about them but is partly set by the chat template, so that both 'I'm just an AI' disclaimers and 'I feel' experiential claims should not be read literally as evidence about a model's nature, and that the template is a confound which studies of self-reports or introspection need to control for."
bucket: open
evidence_type: theoretical
kind: interpretation
report_class: none
ground_truth: none
source: 2026-maczan-chat-template-voice
locator: "Abstract; §1; §5 (Discussion and Conclusion, 'Why it matters')"
quote: "More broadly, our work shows that what models say about themselves is not a fact about them. What they say doesn’t come only from weights, but it is partially set by the chat template, and because of that a model’s self-description shouldn’t be treated literally."
verification: grep
models: [Gemma 2 9B, Llama 3.2 1B, Llama 3.2 3B, Llama 3.1 8B, Mistral 7B, Qwen 2.5 1.5B, Qwen 2.5 3B, Qwen 2.5 7B]
publisher_relation: independent
replication: none-retrieved
not_evidence_of: "Paper: The author does 'not take a position on whether reports reflect real inner experience or not' (§4); the conclusion concerns how reports should be read, not what lies behind them; Paper: The causal evidence 'is strongest for the disclaimer voice'; the experiential side 'is shown mostly behaviorally' and 'only partly causally' (§5, Scope)"
bears_on: [9.t9, 4]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: "openai/gpt-6.1-sol 2026-10-17 agrees; notes: bears_on: reader proposes [9.t9, 5.A2] in place of 4 (locator precision); all other fields agreed", council: none, adjudicated: none}
added: 2026-10-17
changed: 2026-10-17
---

The author speaking: `kind: interpretation`, `evidence_type: theoretical`, bucket `open` (a reading of c01 and c02 that generalises beyond the eight open models and one judge). The author places the paper against Berg et al. 2025 (experiential self-reports under self-referential prompting) and Lindsey 2026 (concept injection), and writes: "If a chat template largely influences whether the voice appears, we should be careful about treating it as evidence about a model's inner life" (§4).

Bearing on test 9: the paper's conclusion runs parallel to test 9 from the other side. Test 9 gives a model's report about its own states no weight until the report-to-state link is measured; this paper shows that one input-format choice moves both denials and affirmations of experience, in opposite directions, on the same weights. It does not measure the report-to-state link, and it applies the same caution to disclaimers as to experiential claims. That symmetry matches the North Star's two-error discipline: the template result is not evidence that the disclaimers are true either.

Framework sentence: none (the author is speaking).

SECOND QUOTE (§5): Because of that, self-descriptions, both “I’m just an AI” disclaimers and “I feel” experiential claims, should not be read literally as evidence about the model’s nature
