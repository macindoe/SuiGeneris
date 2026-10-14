---
id: 2023-apollo-strategic-deception-c03
statement: "The authors state that the work rests on a single scenario found by red-teaming, so they draw no conclusions about how likely the behaviour is in practice or in general deployment and treat it as an existence proof."
bucket: established
evidence_type: theoretical
kind: limitation
source: 2023-apollo-strategic-deception
locator: "§1 (Introduction); §4 (Conclusion)"
quote: "Given that this work focuses on a single example, we do not aim to draw conclusions about the likelihood of this behavior occurring in practice but instead treat this as an existence proof."
verification: grep
models: [gpt-4 (gpt-4-0613), gpt-4-32k (gpt-4-32k-0613), gpt-4-base]
publisher_relation: independent
replication: none-retrieved
not_evidence_of: "Paper: Not evidence that the behaviour is rare: the authors decline to estimate frequency either way, and report that it persisted under prompts that strongly discouraged it, under reduced pressure (when one pressure source at a time was removed) and without a scratchpad (§3.3)"
bears_on: [5.A2]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: none, council: none, adjudicated: none}
added: 2026-10-15
changed: 2026-10-15
---

The authors speaking about what their study cannot show, so `kind: limitation`; bucket `established` because the limit is a stated fact about the design (one environment, varied in several ways; Appendix A.8 lists rewritten variants). Evidence type `theoretical`, following the library's practice for authors' methodological limits. The work "is a result of a red-teaming effort, where we actively seek scenarios in which models behave misaligned and strategically deceive their users" (§1). The conclusion repeats the limit: "Since this is a single scenario, we do not draw any conclusions about the frequency of this behavior in general deployment settings" (§4).

Framework sentence: none (the authors are speaking).

SECOND QUOTE (§4): Since this is a single scenario, we do not draw any conclusions about the frequency of this behavior in general deployment settings
