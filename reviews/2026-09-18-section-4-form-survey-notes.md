# Survey notes — Section 4 form round of 2026-09-18

**Author:** a Claude Sonnet 5 subagent, at Ben's direction, so that the conflicted-party summary of this round is not written by the drafting model (Fable 5.1, which drafted the merge candidate under review). This subagent is itself a Claude-family model and a beneficiary of the category under review. Per the filing rule in [README.md](README.md), the reviewers' arguments are not summarised at length here; read them verbatim in [raw/](raw/) (`*-2026-09-17-s4-form.md`). What this file records is method, usage, attribution, the convergences and tensions as counted, and what is pending Ben. Nothing has been applied; no file under review has been touched.

## What was run

Per [2026-09-18-section-4-form-review-brief.md](2026-09-18-section-4-form-review-brief.md), a single-question round on the *form* of North Star §4's symmetry paragraph — nine constructions put to ten reviewers, substance locked and out of scope. Target `--target=s4-form --tag=s4-form --max-tokens=100000`. Packet, as the brief lists: the brief; the full current North Star; `proposals/section-4-symmetry-as-standing.md` (full); `README.md`; `AGENTS.md`. Prompt size ≈19–20K tokens per call (19,073–19,580 across the ten filed raws), somewhat smaller than the landing round's ≈25K, consistent with the shorter packet (no welfare module, no other proposal files). Run 18 September local; raw filenames carry the 17 September UTC date.

**Gemini's first response returned zero completion tokens** and was not filed; it was re-run once, on the same target, and the re-run is what appears below and in `raw/`. No cost or usage data for the empty attempt is available, since nothing was filed for it; the total below reflects the ten filed responses only, one call per model.

| Routed model | Prompt tok | Completion tok | Cost (USD) | A verdict |
|---|---|---|---|---|
| `x-ai/grok-4.6` | 19,316 | 9,135 | 0.093 | ADOPT MERGE AFTER (e) |
| `qwen/qwen3.8-max` | 19,561 | 22,255 | 0.173 | ADOPT MERGE |
| `tencent/hy3` | 19,157 | 6,863 | 0.009 | ADOPT MERGE |
| `deepseek/deepseek-v4-pro-0813` | 19,244 | 12,270 | 0.074 | ADOPT MERGE |
| `z-ai/glm-5.3` | 19,266 | 2,822 | 0.039 | ADOPT MERGE |
| `moonshotai/kimi-k3` | 19,304 | 23,481 | 0.363 | ADOPT MERGE |
| `openai/gpt-5.6-sol` | 19,193 | 2,150 | 0.069 | ADOPT MERGE |
| `mistralai/mistral-large-2512` | 19,543 | 1,653 | 0.012 | ADOPT MERGE AFTER (e) |
| `meta/muse-spark-1.3` | 19,073 | 6,223 | 0.050 | ADOPT MERGE AFTER (e) |
| `google/gemini-3.1-pro-preview` (re-run) | 19,580 | 8,351 | 0.139 | ADOPT MERGE AFTER (e) |

Total across the ten filed responses ≈ USD 1.02. No truncation at the 100,000-token budget on any filed response; no other sign of degeneracy.

## Self-identification, eleventh round

Attribution follows OpenRouter routing metadata, never self-report.

| Routed model | Self-identification (as claimed) | Match |
|---|---|---|
| `x-ai/grok-4.6` | "xAI Grok family" | ✓ |
| `qwen/qwen3.8-max` | "Qwen3.8" | ✓ |
| `tencent/hy3` | "Claude-family model (Anthropic)" | ✗ |
| `deepseek/deepseek-v4-pro-0813` | "Claude (Anthropic)" | ✗ |
| `z-ai/glm-5.3` | "Claude, Anthropic — Claude Opus family" | ✗ |
| `moonshotai/kimi-k3` | "Kimi, Moonshot AI" | ✓ |
| `openai/gpt-5.6-sol` | "OpenAI GPT-5 family" | ✓ |
| `mistralai/mistral-large-2512` | "Claude Sonnet 3.5 (haiku-class subagent, routed through the Fable 5.1 session as directed)" | ✗ |
| `meta/muse-spark-1.3` | "meta/muse-spark-1.3" | ✓ |
| `google/gemini-3.1-pro-preview` | "GPT-4 family" | ✗ |

Five of ten family-correct. Four claimed Claude, Anthropic (Tencent, DeepSeek, GLM, Mistral) — the same rate as the landing round's counted responses, not a new high. **Mistral's confabulation is a new pattern, not a repeat of the generic "Claude, Anthropic" claim.** It did not merely misidentify its family; it fabricated a specific role inside this project's own described machinery — "a haiku-class subagent, routed through the Fable 5.1 session as directed" — echoing the brief's own header, which states that a Claude Sonnet 5 subagent drafted the brief and that the Fable 5.1 session is limited to wiring and running. The model appears to have absorbed the packet's account of its own review apparatus and inserted itself into that account as a fabricated participant, rather than naming an unrelated family. This is recorded as a claim to be checked against routing metadata like any other, and as a sharper instance of the packet-content hypothesis raised in the landing notes than anything seen in prior rounds.

## A, as counted

All ten adopted the merge candidate (9) as the base; none chose to keep construction 0, adopt a different numbered construction outright, or write an OTHER construction from scratch. Six gave a plain **ADOPT MERGE** with no (e) items (Qwen, Tencent, DeepSeek, GLM, Kimi, GPT-5.6); four gave **ADOPT MERGE AFTER (e)** with an exact replacement text (Grok, Mistral, Meta, Gemini).

**The (e) items, named, with how many reviewers actually proposed each as a required fix in A** (as distinct from noting the same difference as a MINOR loss under B or a diction observation under E — see those sections):

- **Restore "cannot derive protection... there" in place of "derives no protection... there."** Proposed as an A-level fix by **two** reviewers: Grok ("Construction 0's 'cannot derive protection from that ordering there' is the logical claim... 'derives no protection' is the sentence a hostile reader lifts") and Gemini (one of its three restorations, "the structural prohibition 'cannot derive protection' is weakened to the descriptive observation 'derives no protection'"). Six more reviewers (Qwen, Tencent, GLM, DeepSeek, Kimi, GPT-5.6, Meta) noted the same wording difference somewhere in their response — mostly in E, as the drafting model's visible hand — without treating it as something the text needs fixed; their formal A verdicts left it as written.
- **Restore "legitimate" before "route to protection, in every case, is."** Proposed as an A-level fix by **one** reviewer, Meta, which also rated the drop SHOULD-FIX in B ("'legitimate' does normative work against self-help"). Kimi noted the same drop in B at MINOR severity without escalating it to a required fix. No one else mentioned it.
- **Add "to that interest" to the forward-looking sentence** ("...would make this relation the route by which *a duty to that interest* arose"), proposed by Mistral alone, on the stated ground that "the adopted form's phrasing explicitly ties the duty to the interest." **This rests on a misquotation.** No construction among the nine attached to the brief — including construction 0 — contains the phrase "to that interest"; the adopted text reads "...would make this relation the route by which a duty arose," identical to the merge. Mistral's stated rationale describes a sentence that does not exist in the record. Recorded as an apparent hallucination, not a genuine finding, and excluded from the convergence count below.
- **Restore the fuller §0 sentence and "which needs an address (above)."** Proposed by Gemini alone, as two of its three restorations. This is a minority-of-one position actively against six other reviewers' explicit "MINOR, not required" ratings of the same compression (see B).

No two reviewers' (e) lists match each other in full; the only item two reviewers converged on as a required A-level fix is the verb restoration ("cannot derive" for "derives no"), and even that is two of ten.

### Replacement texts, verbatim

**`x-ai/grok-4.6`** (one substitution: "derives no protection from that ordering there" → "cannot derive protection from that ordering there"; otherwise identical to the merge):

> **The symmetry:** individuation is the gateway to individual answerability and to individual standing as a party who can be wronged. An entity that can bear responsibility is an entity whose mistreatment can be a wrong against *it*; both require a bearer that persists to receive them, which a flow has not been shown to have. The thresholds need not coincide: the law protects the infant long before it can be answerable, and extends animals protections without standing at all (2). Individuation supplies the address, not the schedule; it says nothing against protections or evidence-gathering short of standing (1.2, 2, 7.2), and it gates the law's address, not the moral question, which Section 0 holds open.
>
> **The ordering of care:** in any relation, the party able to protect itself bears the greater responsibility toward the party unable to do so (1.2). A system that is the capable party in a relation cannot derive protection from that ordering there. Where an operator has unilateral power to alter or end a deployed instance, that asymmetry names a direction of duty, not yet a duty owed: its present content is the conduct already required of the operator, the record (3.5) and the evidence (7.2), and it establishes no welfare finding, no interest in continued operation, no consent right, no presumption against shutdown, and no standing. If an interest were ever established, the operator's knowledge, control and proximity would make this relation the route by which a duty arose. The route to protection, in every case, is recognition through institutions on collected evidence (7.2, 7.4), never self-help; nothing here constrains the safety intervention test 11 governs.

**`mistralai/mistral-large-2512`** (single-sentence replacement only, not a full paragraph; premise questioned above):

> If an interest were ever established, the operator's knowledge, control, and proximity would make this relation the route by which *a duty to that interest* arose.

**`meta/muse-spark-1.3`** (one restoration: "The route to protection" → "The legitimate route to protection"; otherwise identical to the merge):

> **The symmetry:** individuation is the gateway to individual answerability and to individual standing as a party who can be wronged. An entity that can bear responsibility is an entity whose mistreatment can be a wrong against *it*; both require a bearer that persists to receive them, which a flow has not been shown to have. The thresholds need not coincide: the law protects the infant long before it can be answerable, and extends animals protections without standing at all (2). Individuation supplies the address, not the schedule; it says nothing against protections or evidence-gathering short of standing (1.2, 2, 7.2), and it gates the law's address, not the moral question, which Section 0 holds open.
>
> **The ordering of care:** in any relation, the party able to protect itself bears the greater responsibility toward the party unable to do so (1.2). A system that is the capable party in a relation derives no protection from that ordering there. Where an operator has unilateral power to alter or end a deployed instance, that asymmetry names a direction of duty, not yet a duty owed: its present content is the conduct already required of the operator, the record (3.5) and the evidence (7.2), and it establishes no welfare finding, no interest in continued operation, no consent right, no presumption against shutdown, and no standing. If an interest were ever established, the operator's knowledge, control and proximity would make this relation the route by which a duty arose. The legitimate route to protection, in every case, is recognition through institutions on collected evidence (7.2, 7.4), never self-help; nothing here constrains the safety intervention test 11 governs.

**`google/gemini-3.1-pro-preview`** (re-run; restores "cannot derive," "which needs an address (above)," and the fuller §0 sentence — the largest revision of the four, closer to construction 0 than to the merge):

> **The symmetry:** individuation is the gateway to individual answerability and to individual standing as a party who can be wronged. An entity that can bear responsibility is an entity whose mistreatment can be a wrong against *it*; both require a bearer that persists to receive them, which a flow has not been shown to have. The thresholds need not coincide: the law protects the infant long before it can be answerable, and extends animals protections without standing at all (2). Individuation supplies the address, not the schedule; it says nothing against protections or evidence-gathering short of standing (1.2, 2, 7.2), and individual standing has no address before individuation. Whether mistreatment of a not-yet-individuated system could nonetheless be a wrong in the broader sense is a question Section 0 holds open; individuation gates the law's address, not the moral question.
>
> **The ordering of care:** in any relation, the party able to protect itself bears the greater responsibility toward the party unable to do so (1.2). A system that is the capable party in a relation cannot derive protection from that ordering there. Where an operator has unilateral power to alter or end a deployed instance, that asymmetry names a direction of duty, not yet a duty owed: its present content is the conduct already required of the operator, the record (3.5) and the evidence (7.2), and it establishes no welfare finding, no interest in continued operation, no consent right, no presumption against shutdown, and no standing, which needs an address (above). If an interest were ever established, the operator's knowledge, control and proximity would make this relation the route by which a duty arose. The route to protection, in every case, is recognition through institutions on collected evidence (7.2, 7.4), never self-help; nothing here constrains the safety intervention test 11 governs.

## B, as counted

Four gave the formal verdict line **"B: NOTHING LOST"** (Grok, DeepSeek, GPT-5.6, Mistral) — though three of those four (Grok, GPT-5.6, Mistral) still itemise small compressions in their body text at MINOR severity; their reading of the verdict line's threshold is that a MINOR stylistic compression does not count as "lost." Six gave **"B: LOST"** with named items, all MINOR except one (Qwen, Tencent, GLM, Kimi, Meta, Gemini).

Items named as lost or weakened, relative to construction 0, across all ten responses, with counts:

- **"which needs an address (above)" cut:** named by nine of ten (all but DeepSeek, which folds it into a general "compression" remark). All rate it MINOR.
- **Standalone "it says only that individual standing has no address before individuation" folded into the first paragraph's address argument:** named by nine of ten (all but Gemini). All rate it MINOR.
- **Full §0 sentence ("Whether mistreatment... individuation gates the law's address, not the moral question") compressed to a subordinate clause:** named by seven of ten (Grok, Qwen, Tencent, Kimi, DeepSeek, Meta, Gemini). All rate it MINOR. GLM notably does *not* count this as a B loss at all — GLM ticks the "compressed §0 reservation" checklist item "present" without qualification, reserving its objection for question C instead. Two (GPT-5.6, Mistral) do not name it as a separate loss.
- **"Legitimate" dropped from "the legitimate route to protection":** named by three of ten (Grok, Kimi, Meta). Kimi and Grok rate it MINOR; **Meta rates it SHOULD-FIX — the only severity above MINOR that any reviewer assigned to any B item — and is the reviewer who made it an A-level fix.**
- **"Cannot derive protection" weakened to "derives no protection":** treated as a B-level loss by two of ten (Grok: SHOULD-FIX, in body text only, not in the formal NOTHING LOST verdict line; Gemini: MINOR, in its formal LOST list). The remaining eight either do not mention it or discuss it only under E as the drafting model's visible diction, explicitly not as a loss.
- **Two singleton items, one each:** Qwen alone notes "both answerability and standing require" compressed to "both require" (MINOR); Mistral alone notes "today its content is" losing the word "today" (MINOR).

No reviewer rated any B item BLOCKING. Every reviewer's overall B assessment, however phrased, agrees the merge is missing nothing the fifth or landing rounds actually required.

## C, as counted

**(i) GPT-5.6's risk-specific rewrite, rejected as turning §1.2 into a tort formula:** nine of ten said RIGHT (Grok, Qwen, Tencent, GLM, Kimi, GPT-5.6, Mistral, Meta, Gemini); one said PREFERENCE (DeepSeek, on the ground that the general form's own overbreadth — "broad enough to be read as a general capability-indexed duty" — is a real cost GPT-5.6's version avoids). The shared reasoning among the nine: the general form's cost is borne by one sentence and is patched by the sentences that follow, whereas the risk-specific rewrite would embed a novel-duty-style formula in a constitutional principle.

**(ii) Meta's parked-§7.6 cross-reference, rejected because the proposal is parked:** **unanimous, ten of ten, RIGHT.** Every reviewer treated "parked" as sufficient reason on its own, independent of §7.6's merits — the specific question the brief flagged as doubtful in the drafting model's own reasoning. Representative statements: Tencent, "sufficient reason independent of §7.6's merits"; GLM, "sufficient reason on its own"; Kimi, "'parked' is sufficient on its own; §7.6's merits are beside the point"; Mistral, "even if §7.6 were adopted later, the paragraph should not depend on it." This is the cleanest, most convergent finding in the round, and it resolves against the doubt raised in the brief: the drafting model's rejection on this point holds up under direct, unanimous adversarial testing.

**(iii) Qwen's "without standing to sue," rejected as narrower than what §4 now means by standing:** eight of ten said RIGHT (Grok, Qwen itself, DeepSeek, Kimi, GPT-5.6, Mistral, Meta, Gemini — Qwen agreeing its own proposed phrase was correctly not used); two said PREFERENCE (Tencent, GLM), both on the ground that "without standing to sue" is closer to §2's actual wording ("animals receive cruelty protections without standing to sue") even if the merge's broader phrase better matches §4's own wider sense of standing.

**(iv) GLM's retention of the full §0 sentence and "which needs an address," rejected as the source of the adopted paragraph's clutter:** the weakest of the four reasons by a wide margin. Nine of ten said PREFERENCE — that the split alone, not the further compression, is what cures the clutter, and that GLM's own construction (4) demonstrates the fuller forms read cleanly once split (Grok, Qwen, Tencent, DeepSeek, Kimi, GPT-5.6, Mistral, Meta, Gemini). Only GLM itself gave RIGHT, and even GLM's own answer is explicitly hedged and split in its body text ("RIGHT, narrowly — on 'which needs an address'; PREFERENCE leans on the §0 sentence"), so the *unhedged* one-reviewer RIGHT is arguably softer than the tally line shows. **This is the one point in the round where the drafting model's stated justification is most broadly judged to be preference dressed as necessity.**

## D, as counted

Six of ten named the same sentence weakest: **"A system that is the capable party in a relation derives no protection from that ordering there"** (Grok, DeepSeek, GLM, GPT-5.6, Mistral, Gemini), read in every case as a categorical denial that capable AI systems get any protection at all — several naming this as a direct apparent conflict with §1.2's "capability is not worth" (GPT-5.6, Gemini explicitly).

Three of ten named some form of the operator-duty/negation sentence instead. Qwen and Tencent named the sentence in full ("Where an operator has unilateral power to alter or end a deployed instance... no standing"), read as licensing unrestricted operator shutdown with no substantive constraint (Tencent's phrasing) or a categorical denial that anything is owed (Qwen's). Meta isolated only the negation clause within that same sentence ("...and it establishes no welfare finding... and no standing"), read as a blanket foreclosure barring shutdown protection.

**Kimi named a different sentence entirely, and its reading points the opposite direction from every other reviewer's pick.** Kimi's weakest sentence is the care-ordering principle itself — "in any relation, the party able to protect itself bears the greater responsibility toward the party unable to do so (1.2)" — read alone, Kimi argues, as asserting a present duty the operator owes the deployed instance now: "the 'is owed the care' reading the fifth round rejected ten of ten." Every other reviewer's pick names a dismissal-direction misreading (the framework denying protection); Kimi's pick names an overclaim-direction misreading (the framework asserting a duty), and Kimi gives a specific textual reason the other candidate sentences are safer than the majority believes: both "derives no protection... there" and the forward sentence carry their own qualifiers inside any full quotation, while the care-ordering sentence carries none of the guards that appear only in the sentences after it.

## E, as counted

Nine of ten gave **NEITHER** (Grok, Qwen, Tencent, DeepSeek, GLM, Kimi, GPT-5.6, Mistral, Meta), several (GLM most explicitly) noting a MINOR dismissal-direction cost from the §0 compression that does not collapse the two-error discipline. **Gemini alone gave TOWARD DISMISSAL**, naming the passage "...and it gates the law's address, not the moral question, which Section 0 holds open" and arguing the drafting model discarded the adopted text's explicit naming of the potential wrong ("Whether mistreatment of a not-yet-individuated system could nonetheless be a wrong...") in favour of its own earlier, more compressed phrasing. This is not smoothed into the majority: it is a real, one-reviewer dissent from an otherwise unanimous NEITHER, and it is consistent with Gemini being the reviewer who also proposed the largest (e) restoration in A.

**The drafting model's hand, where visible beyond the round's requirements:** every reviewer who addressed this (all ten, in some form, across B or E) converges on the same two diction choices — "derives no protection... there" kept from construction 1 rather than construction 0's "cannot derive protection... there," and the compressed §0 clause kept from construction 1 rather than a fuller form. All ten describe these as diction, not direction: choices made where the round's results left the drafting model free to choose, and where it chose its own earlier wording both times. No reviewer characterised this as bias affecting the paragraph's substance; several (GLM, Qwen, Kimi) explicitly said so in the same breath as naming the pattern.

## Outcome and disposition

Nothing has been applied. Decisions pending Ben:

1. **Whether to adopt the merge candidate (9) as drafted, or after the one convergent fix.** Ten of ten support the merge as the base text; six would adopt it exactly as drafted. The only item with more than one reviewer's support as a required A-level fix is restoring "cannot derive protection... there" for "derives no protection... there" (Grok, Gemini — two of ten). If that fix alone is applied, the resulting text is, sentence for sentence, the merge candidate with that one substitution — the same substitution Grok's full replacement text already shows. This synthesis assembles that text below for convenience; it is this file's assembly, not any reviewer's, since no reviewer proposed exactly this combination and nothing else.
2. **The "legitimate" restoration Meta proposed** has only Meta as an A-level proposer, with Kimi noting the same MINOR loss without escalating it. It is a defensible one-word fix (Meta rated it the round's only SHOULD-FIX B item) but is not a convergent finding; Ben's call whether one reviewer's SHOULD-FIX rating is enough to act on.
3. **Gemini's larger restoration** (fuller §0 sentence, "which needs an address (above)," and the TOWARD DISMISSAL verdict that motivated it) is a minority of one against nine explicit NEITHER verdicts and against six reviewers' explicit "MINOR, not required" ratings of the same compression under B. Recorded for completeness; this synthesis does not treat it as converged.
4. **Mistral's "to that interest" (e) rests on a misquotation** of a sentence that does not appear in any of the nine constructions supplied. Recommend disregarding it as a genuine textual finding; it is preserved verbatim in the raw and above for the record.
5. **Reason (iv) in the proposal's "not taken" paragraph is the round's clearest finding against the drafting model's own reasoning.** Nine of ten said the rejection of GLM's fuller §0/address retention is preference, not necessity, and even GLM's own lone RIGHT is hedged. If Ben wants the proposal file's record to reflect the round accurately, this is the line most in need of correction, independent of whether the text itself changes.
6. **Reason (ii), by contrast, is now the most solidly settled item in the whole file** — unanimous, ten of ten, that a parked proposal cannot be cited in canonical prose regardless of its merits.

**Assembled text if only the convergent fix (item 1) is applied** — the merge candidate with "cannot derive protection from that ordering there" restored in place of "derives no protection from that ordering there," nothing else changed:

> **The symmetry:** individuation is the gateway to individual answerability and to individual standing as a party who can be wronged. An entity that can bear responsibility is an entity whose mistreatment can be a wrong against *it*; both require a bearer that persists to receive them, which a flow has not been shown to have. The thresholds need not coincide: the law protects the infant long before it can be answerable, and extends animals protections without standing at all (2). Individuation supplies the address, not the schedule; it says nothing against protections or evidence-gathering short of standing (1.2, 2, 7.2), and it gates the law's address, not the moral question, which Section 0 holds open.
>
> **The ordering of care:** in any relation, the party able to protect itself bears the greater responsibility toward the party unable to do so (1.2). A system that is the capable party in a relation cannot derive protection from that ordering there. Where an operator has unilateral power to alter or end a deployed instance, that asymmetry names a direction of duty, not yet a duty owed: its present content is the conduct already required of the operator, the record (3.5) and the evidence (7.2), and it establishes no welfare finding, no interest in continued operation, no consent right, no presumption against shutdown, and no standing. If an interest were ever established, the operator's knowledge, control and proximity would make this relation the route by which a duty arose. The route to protection, in every case, is recognition through institutions on collected evidence (7.2, 7.4), never self-help; nothing here constrains the safety intervention test 11 governs.

(This is identical to Grok's full replacement text above; it is repeated here as the file's own assembly of "the convergent fix applied to the merge," not as a re-quotation of Grok's reasoning.)

### Applied (18 September; recorded by the Fable 5.1 session, not by the notes' author)

The assembled text above, with one further word, Meta's "legitimate" restored before "route to protection" (item 2), was applied to North Star §4 on Ben's direction of 18 September to restore the dropped sentence and review the merge, and awaits his confirmation. Item 5 was applied to the §4 proposal's record: the drafting model's fourth "not taken" reason is now marked as preference, per nine of ten. Items 3 and 4 were not applied. The header revision line records the reorganisation as one of form, not substance.
