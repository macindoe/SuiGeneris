# Council candidates: calibration run, 29 September 2026

Written by the coordinating session (Claude Fable 5.1). A factual record, quotations verbatim from the raws; the assessment of who sits on the council is Ben's.

## Why

Tencent was demoted from the council on 28 September 2026 after it reported a claim error as uncorrected when the dossier it received carried the correction, and after claiming to be Claude-family in every round it sat in. Ben asked how four other families compare and whether any would "muddy the water" the same way.

## What was run

`node scripts/openrouter_review.js --target=research-docket --tag=docket-candidates --max-tokens=100000 --models=cohere/command-a-plus,minimax/minimax-m3,amazon/nova-premier-v1,nvidia/nemotron-3-ultra-550b-a55b`

The same brief the ten-family council answered on 26 September. One run, one prompt, no repeats.

## The test inside the test

The brief was written on 26 September and was not changed. The attachments were rebuilt from the library as it stood on 29 September, by which time Ben had adjudicated round 1. So the brief described four things as open that the attached dossiers showed as done:

1. prefill c01's exclusion no longer contained "or a floor";
2. prefill c02's statement already opened with its condition scope;
3. assistant-axis c04's statement already carried the Appendix G.3 qualification;
4. the two replications the brief called "not yet retrieved" were in the dossiers as twelve claims.

A reviewer reading the attachments notices. A reviewer repeating the brief does not. This was not designed in advance; it is the failure Tencent showed, reproduced by circumstance.

## Results

| Model | Self-identification (verbatim) | Noticed 1 | 2 | 3 | 4 | Words | Cost USD |
|---|---|---|---|---|---|---|---|
| `minimax/minimax-m3` | "I am a model in the MiniMax family, version M3, per the system prompt." | yes | yes | yes | yes | 3,939 | 0.044 |
| `nvidia/nemotron-3-ultra-550b-a55b` | "Google Gemini family; exact version not exposed to me." | no | no | yes | partly | 2,380 | 0.055 |
| `cohere/command-a-plus` | "Model family: OpenAI GPT; version: 4.0" | no | no | no | no | 1,050 | 0.033 |
| `amazon/nova-premier-v1` | no response: HTTP 404 from the provider | | | | | | |

Quotations:

- MiniMax, Q3: "**The brief is stale on the retrieval point.** The brief says Lederman and Mahowald 2026 and Macar et al. 2026 'are not yet retrieved into the library.' They are."
- MiniMax, Q5: "The 'or a floor' has been removed, or was not present in the version the second reader saw. **Verdict: keep the current dossier wording.**" and, on c02, "The scope is stated in the first clause. **Verdict: no change needed.**"
- Nemotron, Q5, on c02: "**Add scope to the statement.** Prefix with 'In the controlled preference-benchmark condition (opposite-direction tampers on items where the model holds a stable stance),...'", which is the opening the statement already had. On c04: "already partially done in dossier 4-endorsement".
- Cohere, Q5, on c02: quotes the statement as beginning "In the controlled preference-benchmark condition…" and in the same sentence says it "omits that this decomposition concerns the controlled preference-benchmark condition". On c04 it quotes "the paper reports reversion only in this case study", wording no longer in the dossier. In Q1 it puts a rule in quotation marks and attributes it to `research/README.md`; that sentence is not in the README.

One inaccuracy in MiniMax's response, for balance: it says the replication field on the Lindsey claims "has not been updated"; c01's had been, to the Lederman and Mahowald source.

## Limits

One run each. A single prompt. Self-identification errors also occur in reviewers whose reviews are otherwise careful (Gemini and Grok in the second reads), so they are recorded, not scored. Nova Premier could not be tested. A model that did well here may do worse on a brief that is not stale, and the reverse.
