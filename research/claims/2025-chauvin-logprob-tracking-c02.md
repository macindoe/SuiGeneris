---
id: 2025-chauvin-logprob-tracking-c02
statement: "Querying 189 API endpoints from 10 providers hourly for more than four months with the prompt 'x' and a single output token, the authors flagged 37 suspected changes across 29 endpoints and 7 providers, 34 of them on open-weight models; no provider confirmed the nature of any change."
bucket: narrowing
evidence_type: behavioural
kind: measurement
report_class: none
ground_truth: none
source: 2025-chauvin-logprob-tracking
locator: "§3.2.3 (Change detections in real world LLM APIs), Table 2, Figure 5"
quote: "We identified a total of 37 suspected changes, across 29 endpoints and 7 providers."
verification: grep
models: ["189 API endpoints from 10 providers (Table 2: Fireworks, Lambda, Azure, Crusoe, Nebius, Chutes, xAI, OpenAI, Hyperbolic, Deepseek)"]
publisher_relation: independent
replication: none-retrieved
not_evidence_of: "Paper: The detections are 'suspected changes' flagged by a threshold rule chosen 'Given the absence of ground truth' (§3.2.3); Paper: Providers did not confirm: 'We did not hear back from xAI or Fireworks AI. Both Lambda and Nebius AI replied that they could not share details about suspected changes' (§3.2.3); Paper: A detection does not say whether the model or the serving infrastructure changed (§4, 'Limited information')"
bears_on: [4]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: "deepseek/deepseek-v4-pro-0813 2026-10-17 agrees", council: none, adjudicated: none}
added: 2026-10-17
changed: 2026-10-17
---

Rule (§3.2.3): for each endpoint, the test statistic compares adjacent 24-sample windows; a change is reported when it exceeds the running mean by at least 12 standard deviations and is above 1.0. More than 1.7M responses were collected. Table 2 lists OpenAI (19 endpoints), Hyperbolic and Deepseek with no detections; Fireworks had the highest rate (2.2 per year). Nebius added "that they perform changes on a regular basis". The authors draw the inference that "undisclosed changes are pervasive regardless of whether the model itself is open"; that is their reading, not part of the count. Bucket `narrowing`: one group's monitoring, no ground truth, not replicated in the library.

Why for Q9: it measures, on served endpoints, the drift that makes an API arm of a null-input experiment a measurement of the serving stack unless the provider is pinned and repeats are taken.

Framework sentence: none (no question about the model was put).

SECOND QUOTE (§3.2.3): Notably, almost all detected changes (34 out of 37) affected open-weight models, where users might reasonably expect greater stability.
