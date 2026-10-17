---
id: 2025-wang-discrete-minds-time-c03
statement: "The authors state that their study primarily tested open-source models, excluding commercial models such as GPT-4o or Claude, that more powerful commercial models might lead to different conclusions, and that the experiments examine text-only models within controlled settings, whereas real deployments would face multimodal and variable computational environments affecting the token-time to wall-clock relationship."
bucket: established
evidence_type: theoretical
kind: limitation
report_class: none
ground_truth: none
source: 2025-wang-discrete-minds-time
locator: "Limitations (after the Conclusion)"
quote: "our study primarily tested open-source models, excluding commercial models such as GPT-4o or Claude. More powerful commercial models might lead to conclusions that differ from our current findings."
verification: grep
models: []
publisher_relation: independent
replication: none-retrieved
not_evidence_of: "Paper: An established limitation is not a finding that commercial models behave differently; the authors say only that they 'might lead to conclusions that differ' (Limitations)"
bears_on: [4, 9.t9]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: "deepseek/deepseek-v4-pro-0813 2026-10-17 agrees", council: none, adjudicated: none}
added: 2026-10-17
changed: 2026-10-17
---

`kind: limitation`, bucket `established` (the limit is a stated fact about the design), `evidence_type: theoretical` (library practice for authors' methodological limits). Framework sentence: none. Taken in for **Q8 heading 6**, so that the standby/active statement (c01) and the hypothesis (c02) are read with the scope the authors give them: six open-weight models from 7B to 72B parameters (§3), text only, controlled settings.

The authors also state that "understanding the underlying mechanisms driving these differences remains an area for future research" and that the study "does not provide specific methods to enhance this capability" (Limitations). Small models were excluded from BombRush because they "lacked the basic spatial navigation capabilities necessary for the test" (§5.1).

SECOND QUOTE (Limitations): our experiments examine text-only models within controlled settings, whereas real-world applications would face multimodal and variable computational environments affecting the Token-Time to Wall-Clock-Time relationship.
