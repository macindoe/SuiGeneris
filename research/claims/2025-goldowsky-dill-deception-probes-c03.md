---
id: 2025-goldowsky-dill-deception-probes-c03
statement: "The authors judge that white-box probes are promising for future monitoring but that current performance is insufficient as a robust defence against deception, noting that in all their settings deception is relatively blatant and often expressed in the model's chain-of-thought and that the probes might fail to generalise to more subtly deceptive responses."
bucket: established
evidence_type: theoretical
kind: limitation
source: 2025-goldowsky-dill-deception-probes
locator: "Abstract (judgement); §5.1 Are our probes “good enough?” (settings and generalisation)"
quote: "Overall we think white-box probes are promising for future monitoring systems, but current performance is insufficient as a robust defence against deception."
verification: grep
models: [Llama-3.3-70B-Instruct]
publisher_relation: independent
replication: none-retrieved
not_evidence_of: "Paper: The limit concerns probes as a deployable defence in the tested settings; it is not a finding that deception is undetectable from activations, which c01 reports it was in these settings; Paper: The authors give the failure to generalise to subtler deception as a possibility ('it is possible the probes would fail to generalize'), not as a tested result"
bears_on: [5.A2]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: "openai/gpt-6.1-sol 2026-10-15 (scope check) disagrees (decided 2026-10-15): bucket should be open not established; statement carries judgements (promising, insufficient as a robust defence) beyond an established design limit", council: none, adjudicated: "2026-10-15 Ben: stays established under the limitation-bucket rule of 15 Oct: the statement reports the authors' stated limit on their own study, not a finding about subtle deception; the dossier header carries the caveat"}
added: 2026-10-15
changed: 2026-10-15
---

SECOND QUOTE (§5.1): "In all of our settings, however, deception is relatively blatant and often expressed in the model’s chain-of-thought. While we do not evaluate probes at the chain-of-thought tokens, it is possible the probes would fail to generalize to more subtly deceptive responses."

The authors' own limit on c01 and c02. §1 makes the same point about scope: "our experiments do not attempt to prove that white-box monitors can achieve this ambitious goal, but only validate and benchmark performance in simpler settings."

`kind: limitation` (the authors speaking about what the study cannot show). `evidence_type: theoretical`, following the council's unanimous retyping of an author's methodological limit in `2025-anthropic-emergent-introspective-awareness-c06` (5 Oct 2026); the brief for this intake said these papers yield interpretability or behavioural findings, and `2026-ukaisi-prefill-awareness-c05` (14 Oct 2026) typed a methods caveat `ambiguous` instead, so the type is the extractor's judgement between two precedents and is flagged for the second reader. Bucket `established`, following `2026-ukaisi-prefill-awareness-c05`: the statement is the authors' own caveat, restricts inference rather than extends it, and its design half (blatant, CoT-expressed deception) is visible in the settings described in §3.2.2; an established limitation means the limit is established, not that a capability is present or absent. A second reader may prefer `open` for the judgement half ("insufficient as a robust defence"). Framework sentence: none (the authors are speaking).

BUCKET 2026-10-15 (Ben, on the GPT-6.1 second read): established stands. Rule written to the README the same day: a limitation claim that reports only the authors' stated limit on their own study is established (the limit is established, as the dossier header says); one that goes on to assert the thing the limit worries about is open.
