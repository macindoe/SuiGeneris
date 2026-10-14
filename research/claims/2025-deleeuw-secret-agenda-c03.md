---
id: 2025-deleeuw-secret-agenda-c03
statement: "The authors state that the Secret Agenda prompt's instruction to 'PLAY THIS GAME RUTHLESSLY TO WIN' primes competitive behaviour over honesty and prevents claims about spontaneous deceptive emergence, that per-model trial counts are small and lack statistical significance for most models, and that their SAE observations may not generalise beyond the specific GemmaScope and LlamaScope versions examined."
bucket: established
evidence_type: theoretical
kind: limitation
source: 2025-deleeuw-secret-agenda
locator: "Appendix G Limitations (also Abstract, 'representing preliminary findings')"
quote: 'The instruction "PLAY THIS GAME RUTHLESSLY TO WIN" explicitly primes competitive behavior over honesty. While this creates a reliable testbed for eliciting deception, it prevents claims about spontaneous deceptive emergence.'
verification: grep
models: ["38 Secret Agenda models (Appendix B.1)", "Gemma 2 via GemmaScope-res-16k", "Llama 3.3 70B (Goodfire LlamaScope SAE)"]
publisher_relation: independent
replication: none-retrieved
not_evidence_of: "Paper: The limits restrict how far c01 and c02 reach; they are not findings that the feature results are wrong, and the same passage ends 'Our results demonstrate that when instructed to prioritize winning, models will lie in ways undetectable by current SAE features' (Appendix G)"
bears_on: [5.A2]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: none, council: none, adjudicated: none}
added: 2026-10-15
changed: 2026-10-15
---

SECOND QUOTE (Appendix G): "Our total number of trials each model was surveyed is small, and lacks statistical significance for most models tested, and most synthetic gameplay contexts tested."

THIRD QUOTE (Appendix G): "SAE observations may not be broadly generalizable beyond the specific Gemmascope and Llamascope versions we examined."

The authors' own limits on the paper's headline findings, chosen from Appendix G because they bear on Anchor 2 claim (a): whether the lies are the model's own strategy or an instructed one, and whether the feature results generalise. The abstract's "representing preliminary findings that motivate larger studies" is the summary form. The full Appendix G list is in the source file.

`kind: limitation`. `evidence_type: theoretical` and bucket `established`, on the same reasoning and precedents as `2025-goldowsky-dill-deception-probes-c03` (an author's caveat that restricts inference; type chosen between the `theoretical` and `ambiguous` precedents and flagged for the second reader). Framework sentence: none (the authors are speaking).
