---
slug: 2024-binder-looking-inward
title: "Looking Inward: Language Models Can Learn About Themselves by Introspection"
authors: [Felix J Binder, James Chua, Tomek Korbak, Henry Sleight, John Hughes, Robert Long, Ethan Perez, Miles Turpin, Owain Evans]
date: 2024-10-17
venue: "arXiv preprint (cs.CL), v1; ICLR 2025 per the Q1 scan (not shown on the arXiv abstract page; not checked)"
url: "https://arxiv.org/abs/2410.13787"
identifiers: {arxiv: "2410.13787v1", doi: ""}
models_studied: [GPT-4o (gpt-4o-2024-05-13), GPT-4, GPT-3.5 (gpt-3.5-turbo-0125), Llama 3.1 70B]
publisher_relation: independent
status: verified
retrieved: {date: "2026-10-17", method: "curl.exe arXiv HTML", by: "Claude Opus 5.5 subagent", sha256: "dab37a673b649798f550cca2afafa7785959181c9b9dc7ea467c847c1f2f1e2d", text_location: "research/texts/2024-binder-looking-inward/text.txt (gitignored; raw.html alongside; re-fetch and compare sha256 if absent)"}
related: [research/scans/2026-09-25-q1-same-context-cross-model.md, research/OPEN-QUESTIONS.md]
system_conditions: {modality: text, state: none, operation: per-call, world: none, access: api}
intake: summary
---

# Looking Inward: Language Models Can Learn About Themselves by Introspection

Binder, Chua, Korbak, Sleight, Hughes, Long, Perez, Turpin, Evans. arXiv 2410.13787v1 [cs.CL], 17 October 2024 (the only version listed on the abstract page). The arXiv comments field reads "15 pages, 9 figures" and gives no venue; ICLR 2025 is the Q1 scan's statement and was not checked here. Licence as printed on the held HTML: arXiv.org perpetual non-exclusive licence.

**Abstract** (authors' words, quoted verbatim from the held text):

> Humans acquire knowledge by observing the external world, but also by introspection. Introspection gives a person privileged access to their current state of mind (e.g., thoughts and feelings) that is not accessible to external observers. Can LLMs introspect? We define introspection as acquiring knowledge that is not contained in or derived from training data but instead originates from internal states. Such a capability could enhance model interpretability. Instead of painstakingly analyzing a model’s internal workings, we could simply ask the model about its beliefs, world models, and goals. More speculatively, an introspective model might self-report on whether it possesses certain internal states—such as subjective feelings or desires—and this could inform us about the moral status of these states. Importantly, such self-reports would not be entirely dictated by the model’s training data. We study introspection by finetuning LLMs to predict properties of their own behavior in hypothetical scenarios. For example, “Given the input P, would your output favor the short- or long-term option?” If a model M1 can introspect, it should outperform a different model M2 in predicting M1’s behavior—even if M2 is trained on M1’s ground-truth behavior. The idea is that M1 has privileged access to its own behavioral tendencies, and this enables it to predict itself better than M2 (even if M2 is generally stronger). In experiments with GPT-4, GPT-4o, and Llama-3 models (each finetuned to predict itself), we find that the model M1 outperforms M2 in predicting itself, providing evidence for introspection. Notably, M1 continues to predict its behavior accurately even after we intentionally modify its ground-truth behavior. However, while we successfully elicit introspection on simple tasks, we are unsuccessful on more complex tasks or those requiring out-of-distribution generalization.

(Quoted from the held HTML, lines joined with spaces and the zero-width spaces inside "M1" and "M2" removed. The arXiv abstract page's `citation_abstract` differs slightly in wording, e.g. "internal states such as subjective feelings or desires" without dashes and "Such self-reports would not be" for "Importantly, such self-reports would not be".)

**"Introspection" is the authors' operational term.** They define it as the ability "to access facts about themselves that cannot be derived (logically or inductively) from their training data alone", tested as self-prediction beating cross-prediction, and say the definition "does not specify how" the model accesses the fact (§2). The library records the term as theirs.

**Intake level: summary** (17 October 2026). Three claims: the self-prediction result (c01), the design that keeps the prediction out of the acting context (c02), the authors' stated limits (c03). c01 and c02 are the library's first claims with `report_class: future-state` and `ground_truth: independent-record` (the class added on 17 October 2026 on Ben's decision, OPEN-QUESTIONS Q10): the model answers a question about its own behaviour on a prompt it has not yet answered, and the answer is scored against the behaviour it then produces on that prompt in a separate context. Under the labelling rule the scored event is the model's answer about itself, so c01 and c02 carry the canonical test 9 sentence, once and last; c03 (the authors speaking) carries none.

**Why it is in the library:** OPEN-QUESTIONS Q10 (Ben, 15 Oct 2026: "is nobody testing `future-state`?"), whose follow-up names this paper as the candidate intake; Q1 scan entry 1 (`scans/2026-09-25-q1-same-context-cross-model.md`). It bears on §4 (reflective endorsement over time, answerability: a system's relation to its own future conduct) and on test 9 (a self-report scored against a record the system supplies later, the nearest thing in the literature to a coupling measurement for one narrow class of report).

**Publisher relation:** `independent`, judged against the studied models' developers (OpenAI for GPT-4o, GPT-4 and GPT-3.5; Meta for Llama 3.1 70B): no author is printed with an OpenAI or Meta affiliation. Affiliations as printed: Binder, UC San Diego and Stanford University; Chua, Truthful AI; Korbak, Independent; Sleight, MATS Program; Hughes, Speechmatics; Long, Eleos AI; Perez, **Anthropic**; Turpin, Scale AI and New York University; Evans, UC Berkeley and Truthful AI. The Q1 scan recorded "mixed (inferred: ... some co-authors Anthropic-affiliated)"; the held text prints one Anthropic affiliation (Perez), and Anthropic developed none of the studied models, so the field is set to `independent` and the Anthropic co-authorship is recorded here. One experiment (§3.4) changes GPT-4o's behaviour by finetuning it on the outputs of Anthropic's Claude 3.5 Sonnet; Claude is a data source there, not a studied model. No funding statement was searched beyond the main text.

**Authors' stated scope and limits** (quoted from the held text):

- "Models only exhibit introspection on simpler tasks. Our tasks, while demonstrating introspection, do not have practical applications." (§6)
- "models trained to self-predict (which provide evidence of introspection on simple tasks) do not have improved performance on out-of-distribution tasks that are related to self-knowledge (Section 4)." (§6)
- "We do not observe clear-cut evidence for introspection in GPT-3.5" (§6, "Limited evidence of introspection in GPT-3.5").
- "These results show that the self-prediction setup does not always have an advantage over the cross-prediction setup." (§4, on predicting sycophantic answer changes)
- On reports of states relevant to moral status: "For us to accord similar significance to a model’s self-reports, the model would need to be answering based on knowledge of its internal states, not because certain answers are implied by its training data. It might be difficult to evaluate the ground-truth about such states as consciousness and preferences" (§7.2).

**Conflicted-party note:** the extractor is Claude Opus 5.5 (Anthropic). One author is printed with an Anthropic affiliation, and the paper's §7.2 discusses using introspective self-reports to inform judgements of moral status, which is the use test 9 rules out until coupling is measured and which would favour the extractor's class. The result is also one the beneficiary would want to read broadly. Claims keep to the authors' words and numbers and to the narrow task the paper scores (short properties of a model's own answers to prompts); nothing here draws on the extractor's own sense of whether it can predict itself.

**Notes on retrieval and verification:**

- Retrieved 17 Oct 2026 by `curl.exe -sL https://arxiv.org/html/2410.13787` (HTTP 200, 395,651 bytes, v1). SHA-256 of `raw.html`: `dab37a673b649798f550cca2afafa7785959181c9b9dc7ea467c847c1f2f1e2d`. `text.txt` stripped by `strip_2024-binder-looking-inward_20261017.py` (same directory; run with `python -I`). SHA-256 of `text.txt`: `08060420000218d9b3a7870c85e1ebbbd1edd828d323b2e5b7b60d9d874ea49c` (117,972 bytes). The strip keeps a zero-width space inside each "M1"/"M2"; one footnote in §2.2 fuses with the model-identifier sentence ("GPT-4o refers to gp4o-2024-05-13., we use the Fireworks finetuning API"), so the GPT-4o snapshot string is as printed there, typo included.
- All claim quotes checked by script (whitespace collapsed, zero-width spaces removed, exact substring of `text.txt`). Hence `status: verified`, quote verification only. No second reader yet.
- **Scan checks.** Authors, models and the figures quoted in the Q1 scan (Llama 70B 48.5% against GPT-4o's 31.8%; GPT-3.5 +0.8%; M2 trained on M1's post-finetuning behaviour, which "should give M2 a slight advantage") match the held text. The scan's "publisher relation: mixed" is revised above.

## System conditions (added 2026-10-17)

- `modality: text`: hypothetical questions over text datasets, e.g. "completing an excerpt from Wikipedia, completing a sequence of animals, and answering an MMLU" question (§2.2).
- `state: none`: each hypothetical question and each object-level prompt is answered on its own; the ground truth is generated "with temperature 0 in a separate context" (§2.2). Finetuning changes weights between experiments; nothing persists within use.
- `operation: per-call`: the same passage.
- `world: none`: no tools or environment are described for the main experiments.
- `access: api`: "we use the Fireworks finetuning API (Fireworks.ai, 2024), which uses Low-Rank Adaptation" for Llama, and "For experiments with OpenAI models (GPT-4o, GPT-4 (OpenAI et al., 2024), and GPT-3.5 (OpenAI et al., 2024)), we use OpenAI’s finetuning API" (§2.2). Llama 3.1 70B is an open-weight model, but the paper accessed it through a hosted finetuning API.
