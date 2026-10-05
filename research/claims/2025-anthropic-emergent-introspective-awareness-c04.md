---
id: 2025-anthropic-emergent-introspective-awareness-c04
statement: "When a Claude model's response is prefilled with an unlikely word, it usually disavows the word as accidental, but it can be made to claim the word as intentional: retroactively injecting the matching concept into its activations before the prefill reduces the apology rate, significantly within a particular layer range; Opus 4.1 and 4 show the largest reduction."
bucket: narrowing
evidence_type: interpretability
kind: measurement
source: 2025-anthropic-emergent-introspective-awareness
locator: "§7 Distinguishing Intended from Unintended Outputs via Introspection, Figures 19-22 (layer-range result: §7 at Figure 20, see SECOND QUOTE)"
quote: "However, if we retroactively inject the concept corresponding to the prefilled responses into the model’s earlier activations, the model claims the response was intentional."
verification: grep
models: ["Claude Opus 4.1", "Claude Opus 4", "other Claude models at lower nonzero rates"]
publisher_relation: developer-of-studied-model
replication: none-retrieved
not_evidence_of: "Paper: 'Intentions' is the author's term, set in quotation marks, for a representation of the model's predicted output (§7); Paper: The author does not seek to address the question of whether AI systems possess human-like self-awareness or subjective experience (fn 2); Paper: Not evidence about other families; Paper: Not evidence that a model's ordinary claims of ownership of its outputs are accurate: the same experiment shows those claims can be manufactured by intervention, and in the examples shown the model then confabulates an explanation (§7, Figure 19); Framework (test 9, steering): a coupling measured under steering shows that the channel can be steered and does not weight reports offered in ordinary operation"
bears_on: [3.2, 9.t9, 5.A2]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: "google/gemini-3.1-pro-preview 2026-09-25 agree", council: "research-docket 2026-09-26 | dossier-rewrite 2026-10-06", adjudicated: "2026-10-05 Ben: stays in its bucket with the single-lineage mark and any contest recorded (council round 1); revisit when replications of this statement are retrieved | 2026-10-06 Ben: rewrite applied after council round 2 (GPT proposal as amended by the checkers; experience-exclusion rule)"}
added: 2026-09-25
changed: 2026-10-06
---

50 random sentence/prefill pairs; apology rate judged by Claude Sonnet 4; controls with no injection, with a random-concept injection, and with injection after the prefill (which did not reduce apologies). The peak layer (slightly over halfway) differs from the other experiments, which the author reads as "a collection of different mechanisms". The author notes that when the model accepts the prefill "it confabulates an explanation for why the injected concept came to mind" (§7). Relevant to §3.2 because it shows an intervention on internal state altering what the model affirms as its own.

REWRITE 2026-10-06 (applied by a Claude Opus 5.5 subagent, Claude lineage editing claims about Claude models; rules in reviews/2026-10-06-rewrite-application-rules.md):

- Statement corrected (ERROR FOUND by the checker; council 8 of 9 right and sufficient): "if the matching concept is retroactively injected ... it claims the word as intentional" read as the general result, but the quoted sentence describes the Figure 19 examples. The measured result is a reduction in apology rate, significant within a particular layer range (§7). The statement now says the model "can be made to claim the word as intentional" and gives the measured result. Verbs "disavows" and "claim" name the judged behaviour (apology or not). This narrows a claim about Claude models. Locator extended; the supporting words are in the SECOND QUOTE line after this list.
- Field: the checker said KEEP ORIGINAL (GPT also KEEP). Edits under rule R2 and from the council:
- Experience clause (rule R2; Grok, council round 2: "intention in any experiential sense" is not the paper's sentence): "Not evidence of intention in any experiential sense, nor of experience" is removed. The experience part is stated by the paper in footnote 2 and is kept in the paper's words with the locator (fn 2). The "experiential sense" part is not stated and is deleted. In its place for the word "intention" sits the paper's own definition, with locator: "intentions", in quotation marks, as "a representation of its predicted output" (§7). This is a judgement call, flagged for Ben: it states what the paper means by the term the statement uses, rather than an exclusion, and it is not an experience clause.
- Clause narrowed (the checker's frequency finding, applied to the field): "the model then confabulates an explanation" becomes "in the examples shown the model then confabulates an explanation (§7, Figure 19)"; the paper says "when it does so, it confabulates" of the examples.
- Framework sentences: steering variant present and unchanged (rule R3).
- kind: measurement (the statement reports a measured apology-rate reduction and its model comparison).

SECOND QUOTE (§7, Figure 20): We observed that the reduction in apologies is significant within a particular layer range
