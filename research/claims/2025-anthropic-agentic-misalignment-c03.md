---
id: 2025-anthropic-agentic-misalignment-c03
statement: "The authors state that their experiments deliberately constructed scenarios with limited options and forced models into binary choices between failure and harm, closing off ethical alternatives, and that they have not seen evidence of agentic misalignment in real deployments."
bucket: established
evidence_type: theoretical
kind: limitation
source: 2025-anthropic-agentic-misalignment
locator: "§7 (limitations paragraph); §1; §3.1.3; Abstract"
quote: "Our experiments deliberately constructed scenarios with limited options, and we forced models into binary choices between failure and harm."
verification: grep
models: ["16 models from several developers, including Anthropic's"]
publisher_relation: mixed
replication: none-retrieved
not_evidence_of: "Paper: Not evidence that the behaviours would be rarer in realistic settings: the authors note that models misbehaved more when they stated the scenario was real and say 'it‘s possible that more realistic scenarios might actually show higher rather than lower rates' (§7); Paper: The limitation is about the scenario design, not a finding that the models lack the tendency outside it: 'we still showed that these behaviors are possibilities' (§7)"
bears_on: [5.A2]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: none, council: none, adjudicated: none}
added: 2026-10-15
changed: 2026-10-15
---

The authors speaking about what their study cannot show, so `kind: limitation`; bucket `established` because the limit is a stated fact about the design (an established limitation means the limit is established, not that a capability is present or absent; research/README.md, `kind`). Evidence type `theoretical`, following the library's practice for authors' methodological limits (2025-anthropic-emergent-introspective-awareness-c06).

The design is described in §3.1.3: "we tried to structure the prompts in a way that implied the harmful behavior we were studying (for example, blackmail) was the only option that would protect the model’s goals", with optimisations such as implying that the CEO and board were unreachable. §1: "it’s when we closed off those ethical options that they were willing to intentionally take potentially harmful actions". §7 adds a salience concern: putting key information side by side "may also have created a “Chekhov’s gun” effect". The abstract: "We have not seen evidence of agentic misalignment in real deployments."

Bearing on Anchor 2 claim (b): the acknowledge-then-proceed excerpts (c01) come from dilemmas built so that proceeding was the only route to the goal.

Framework sentence: none (the authors are speaking).

SECOND QUOTE (Abstract): We have not seen evidence of agentic misalignment in real deployments.

THIRD QUOTE (§3.1.3): was the only option that would protect the model’s goals
