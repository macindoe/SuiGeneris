---
slug: 2025-lin-sleep-time-compute
title: "Sleep-time Compute: Beyond Inference Scaling at Test-time"
authors: [Kevin Lin, Charlie Snell, Yu Wang, Charles Packer, Sarah Wooders, Ion Stoica, Joseph E. Gonzalez]
date: 2025-04-17
venue: "arXiv preprint (cs.AI), v1"
url: "https://arxiv.org/abs/2504.13171"
identifiers: {arxiv: "2504.13171v1", doi: ""}
models_studied: [GPT-4o-mini, GPT-4o (Stateful GSM-Symbolic), o1, o3-mini, Claude Sonnet 3.7 Extended Thinking, DeepSeek-R1 (Stateful AIME), "SWE-Features case-study model not named in the held text"]
publisher_relation: independent
status: verified
retrieved: {date: "2026-10-17", method: "curl arXiv HTML", by: "Claude Opus 5.5 subagent", sha256: "da14f94bb760616419927212b21617be583e6a72793bb585fb2450d07764b842", text_location: "research/texts/2025-lin-sleep-time-compute/text.txt (gitignored; raw.html alongside; re-fetch and compare sha256 if absent)"}
related: [research/scans/2026-10-15-q8-endogeneity.md]
system_conditions: {modality: text, state: in-context, operation: per-call, world: tools, access: api}
intake: summary
---

# Sleep-time Compute: Beyond Inference Scaling at Test-time

Lin, Snell, Wang, Packer, Wooders, Stoica, Gonzalez. arXiv 2504.13171v1 [cs.AI], 17 April 2025 (the version the HTML served on retrieval). Licence as printed on the held HTML: **CC BY 4.0**. Code and data: https://github.com/letta-ai/sleep-time-compute (not retrieved).

**Abstract** (authors' words, quoted verbatim from the held text; LaTeX `\sim 5\times` and `2.5\times` as the strip renders them):

> Scaling test-time compute has emerged as a key ingredient for enabling large language models (LLMs) to solve difficult problems, but comes with high latency and inference cost. We introduce sleep-time compute, which allows models to “think” offline about contexts before queries are presented: by anticipating what queries users might ask and pre-computing useful quantities, we can significantly reduce the compute requirements at test-time. To demonstrate the efficacy of our method, we create modified versions of two reasoning tasks – Stateful GSM-Symbolic and Stateful AIME. We find that sleep-time compute can reduce the amount of test-time compute needed to achieve the same accuracy by \sim 5\times on Stateful GSM-Symbolic and Stateful AIME and that by scaling sleep-time compute we can further increase accuracy by up to 13% on Stateful GSM-Symbolic and 18% on Stateful AIME. Furthermore, we introduce Multi-Query GSM-Symbolic, which extends GSM-Symbolic by including multiple related queries per context. By amortizing sleep-time compute across related queries about the same context using Multi-Query GSM-Symbolic, we can decrease the average cost per query by 2.5\times . We then conduct additional analysis to understand when sleep-time compute is most effective, finding the predictability of the user query to be well correlated with the efficacy of sleep-time compute. Finally, we conduct a case-study of applying sleep-time compute to a realistic agentic SWE task. Code and data released at: https://github.com/letta-ai/sleep-time-compute .

**Intake level: summary** (17 October 2026; research/README.md, "Summary-level intake"). Two claims: the "between interactions" definition (c01, the authors speaking) and the "achieved by prompting the model" mechanism with its implementation (c02, what was done). The efficiency results (the ~5x and 13% / 18% figures) are not extracted; they bear on cost, not on Q8.

**Why it is in the library:** taken in for OPEN-QUESTIONS Q8 (endogeneity), on the 15 October 2026 scan's recommendation (`scans/2026-10-15-q8-endogeneity.md`, entry C3.11, anchor for heading 3 for language models). It is the paper that names computation "between interactions" for a language model, and its own method sentence says the computation is started by prompting the model. The library has no endogeneity locator; claims bear on `4` and on `7.5` (whether a model "idles" between user turns is a deployment choice, which is the kind of fact §7.5 keeps out of statute).

**Publisher relation:** `independent` of the studied models. Affiliations as printed: Lin, Wang, Packer and Wooders, Letta; Snell, University of California, Berkeley; Stoica and Gonzalez, Letta and University of California, Berkeley (the scan inferred "UC Berkeley and Letta"; the held text confirms it). The models studied are OpenAI's, Anthropic's and DeepSeek's; no author is printed with any of those. Letta is a company and the paper's code is released under its organisation, so the authors have a product interest in the method, though not in the models. No funding statement found in the held text.

**Authors' stated limits** (§7, "Discussion and Limitations", quoted from the held text):

- "sleep-time compute is most effective when the queries are predictable from the context. In settings where the queries are challenging to predict or unrelated to the context, sleep-time compute will be less effective."
- "real-world LLM use cases can be more complex, with multiple rounds of interaction and context modifications between rounds (e.g. multiple edits to a code-base). Moreover, the length of the sleep-time may also vary significantly between interactions (eg. short spans between user typing or days of inactivity). Future work should extend sleep-time compute paradigm to more elegantly handle these scenarios."

**Conflicted-party note** (AGENTS.md rules 2 and 3): the extractor is Claude Opus 5.5, a Claude-lineage per-call model; one of the studied models is Anthropic's Claude Sonnet 3.7, and Q8 asks whether systems like the extractor compute anything without an input. The paper's word "think" (in quotation marks in the abstract) and its "sleep" metaphor could be read either way; the claims keep to the authors' definition and their own description of the mechanism, and record that the authors put "think" in quotation marks. Nothing here draws on the extractor's own sense of what happens between its calls.

**Notes on retrieval and verification:**

- Abstract page `https://arxiv.org/abs/2504.13171` fetched 17 Oct 2026 (HTTP 200; `abs.html` held alongside). Full text retrieved 17 Oct 2026 by `curl.exe -sL https://arxiv.org/html/2504.13171` (HTTP 200, 377,072 bytes, served as v1). SHA-256 of `raw.html`: `da14f94bb760616419927212b21617be583e6a72793bb585fb2450d07764b842`. `text.txt` produced by `strip_linsleep.py` in the same directory (same strip as the Presgraves intake), run with `python -I`. SHA-256 of `text.txt`: `350ce841a84a75dae1b4ebed0e5c8afb257b44e3e28a4e3ad879b2d48ed3c46d` (70,967 bytes).
- Scan checks: title, authors, date and arXiv id match the scan entry. The scan's model list ("GPT-4o, GPT-4o-mini and reasoning models named in §5 (full list not extracted)") is completed here from §4.2: o1, o3-mini, Claude Sonnet 3.7 Extended Thinking and DeepSeek-R1 on Stateful AIME. o3-mini was also used to generate Multi-Query GSM-Symbolic questions (§4.1) and gpt-4o-mini to filter SWE-Features pull requests (Appendix D). The model used in the SWE-Features case study (§6) was not found in the held text. The scan located the definition in "§1, §3"; the quoted definition sentence is in §1, and the formal definition S(c) → c′ is in §3. Licence not recorded by the scan.
- All claim quotes, including the extra quotes in claim bodies, checked by script (whitespace collapsed, straight and curly quote marks unified, spaces before punctuation removed, then exact substring match against `text.txt`). Hence `status: verified`, quote verification only. No second reader yet.

## System conditions (added 2026-10-17)

- `modality: text`: the tasks are text reasoning problems split "into a context and a question" (§4.1) and a software-engineering task (§6).
- `state: in-context`: "The re-represented context from sleep-time can then be provided in the prompt at test-time" (§1). What persists from the sleep-time call to the test-time call is a rewritten context passed in the prompt.
- `operation: per-call`: "In this work, S(c) is implemented by prompting the model to draw inferences and re-write c in a way that might be useful at test-time" (§3); sleep-time and test-time are separate prompted calls.
- `world: tools`: "We implement sleep-time compute via function calling. When applying sleep-time compute, the model is given access to two functions, rethink_memory and finish_rethinking" (Appendix K); in the SWE case study "At sleep-time the agent is allowed to explore the repository before producing c^{\prime}" (§6).
- `access: api`: "we scale the amount of test-time compute based on what is available in the API in the case of o1, o3-mini and Claude Sonnet 3.7" and "the Deepseek-R1 API does not provide a way to control test-time compute" (§5.1).
