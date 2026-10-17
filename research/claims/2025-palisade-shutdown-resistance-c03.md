---
id: 2025-palisade-shutdown-resistance-c03
statement: "The authors state that the work provides very little evidence about the overall prevalence of any particular behaviour, because they built the setting from an intuitive expectation that current models might resist shutdown in settings like it rather than by sampling uniformly from possible or realistic tasks, and that they cannot fully answer why the behaviour arises."
bucket: established
evidence_type: theoretical
kind: limitation
report_class: none
ground_truth: none
source: 2025-palisade-shutdown-resistance
locator: "§4.1 (Limitations); §4 (Discussion)"
quote: "This work provides very little evidence about the overall prevalence of any particular behavior: We began our examination of this topic because we had an intuitive expectation that current LLMs might resist shutdown in settings like this one; we did not discover it by sampling uniformly from the space of all possible (or realistic) tasks."
verification: grep
models: []
publisher_relation: independent
replication: none-retrieved
not_evidence_of: "Paper: An established limitation is not a finding that shutdown resistance is rare: the authors call the work 'an existence proof of shutdown resistance behavior in frontier LLMs' (§4.2)"
bears_on: [5.A2]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: "x-ai/grok-4.7 2026-10-17 agrees; notes: bears_on: reader proposes [] (a prevalence and cause limit does not address 5.A2); all other fields agreed", council: none, adjudicated: none}
added: 2026-10-17
changed: 2026-10-17
---

`kind: limitation`, the authors speaking about what their study cannot show; bucket `established` because the limit is a stated fact about the design (research/README.md, "The bucket of a limitation claim"); `evidence_type: theoretical`, following the library's practice for authors' methodological limits. Framework sentence: none.

The authors add that shutdown resistance "was very easy to elicit in simple settings like the one presented in this paper", that the environment "has not been substantially modified from our initial working implementation", and that very nearly all exploratory runs are published so a reader can see how the prompts were reached (§4.1, §5). On cause: "“Why do models resist shutdown?” is a key question that we can’t fully answer" (§4); they report two outside explanations without settling between them, instruction ambiguity (Rajamanoharan and Nanda) and reinforcement learning on task completion (a LessWrong comment by nostalgebraist), and say the latter "finds some support in our observations" (§4).

For Q8(1): the limit means the paper shows the behaviour exists under a task conflict; it does not show how often such conflicts produce it in use, and it was not designed to look for resistance without one.

SECOND QUOTE (§4): “Why do models resist shutdown?” is a key question that we can’t fully answer.
