---
id: 2024-gu-attention-sink-emerges-c03
statement: "The authors find that the attention sink acts more like key biases, storing extra attention scores that may be non-informative and do not contribute to the value computation, and that it stems at least partly from the softmax normalisation, since in their own pre-trained models up to 1B parameters replacing softmax with sigmoid attention without normalisation removes the sink."
bucket: open
evidence_type: interpretability
kind: interpretation
report_class: none
ground_truth: none
source: 2024-gu-attention-sink-emerges
locator: "Abstract; §1 (conclusions list); §3.1 (first token acts as biases, LLaMA3-8B Base); §7 (Learnable biases in attention, Table 4; Inner dependence on attention scores; Scale up to 1B parameters)"
quote: "Most importantly, we find that attention sink acts more like key biases, storing extra attention scores, which could be non-informative and not contribute to the value computation."
verification: grep
models: [LLaMA3-8B Base, "authors' own LLaMA-style models trained from scratch (about 60M, up to 1B parameters)"]
publisher_relation: mixed
replication: none-retrieved
not_evidence_of: "Paper: The architecture interventions were run only on the authors' small from-scratch models ('Due to the intractability of replicating LLaMA pre-training, we design small-sized models', §4), with the sigmoid result stated for 'LMs up to 1B parameters' (abstract); Paper: The authors leave open whether the sink helps the model: 'it remains unclear whether attention sink benefits LM downstream performance' (§8)"
bears_on: [4]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: "x-ai/grok-4.7 2026-10-17 disagrees: statement, scope and quote: 'removes' and unhedged 'do not contribute' go past the 2.46% proxy 'near zero' and the abstract's 'could' (scored-event passage MISMATCH; quote FOUND BUT MISLEADING); not_evidence_of: UNDER-EXCLUDES the proxy-score caveat; bears_on: reader proposes []", council: none, adjudicated: none}
added: 2026-10-17
changed: 2026-10-17
---

Taken in for Q9 (filed under Section 4). The bias reading rests on two kinds of evidence: on a public model, "the first token acts as a bias: its key ... is distributed in a different manifold and its value ... has small \ell_{2} norm" (§7, summarising §3.1 on LLaMA3-8B Base); and on the authors' own models, adding learnable key biases moves the sink from the first token onto the biases ("as long as there are key biases ..., attention sink disappears on the first token but on the biases", §7), while sigmoid attention without normalisation at 1B gives a sink metric "near zero" (2.46%, against 45.11% with softmax; §7). Hence `publisher_relation: mixed`: the decisive interventions are on models the authors trained.

`kind: interpretation` (the authors' reading, "acts more like"), `bucket: open`. For Q9 the relevance is that the first position's large attention share is a learned, input-agnostic feature, so it appears whatever the first token is.

Framework sentence: none (the authors are speaking).

SECOND QUOTE (§7, Scale up to 1B parameters): However, the attention sink metric significantly drops from 45.11% to near zero
