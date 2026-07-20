# DIRECTIVE — SuiGeneris Infrastructure Build

**To:** Claude (or other agent) working in VS Code on `github.com/macindoe/SuiGeneris`
**From:** Ben, carrying forward work from a prior Claude chat session (July 2026)
**First action required:** Read `AGENTS.md` in the repo root. Its rules bind every task below — especially rule 2 (self-report is not evidence), rule 3 (disclose beneficiary-favoring edits), rule 5 (verify against current sources, not training recall), and rule 6 (do not claim completion you have not verified; cite diffs and sources).

## Context you need

This repo holds a North Star framework document for a sui generis legal category for artificial minds, aimed at influencing Australian AI legislation expected in 2027. The repo currently contains `north-star-sui-generis-ai-category.md`, `README.md`, and `AGENTS.md`. Your job is the operational infrastructure around it — not revisions to the North Star document itself. Do not edit the North Star document except to fix verifiable factual errors, and flag any such fix prominently in the commit message.

## Tasks, in order

### 1. LICENSE
Ben must choose; do not choose for him. Present the tradeoffs concisely (CC BY 4.0 is the working recommendation from the prior session: allows adaptation into consultation submissions with attribution; alternatives worth naming: CC BY-SA 4.0 if he wants derivatives kept open, CC BY-ND if he wants adaptation locked down — note ND would defeat the submission-adaptation purpose). Once he picks, add the LICENSE file and reference it in README.

### 2. Provenance note
Add a short `PROVENANCE.md` (and link from README): the documents were produced in a single extended dialogue between Ben and one Claude instance (Claude Fable 5, chat interface, July 2026), then committed by Ben. State plainly: single-model-family origin is a known limitation the cross-family review process (task 3) exists to correct. Ask Ben whether he edited the documents before committing and record his answer accurately.

### 3. Cross-family review scaffolding
- Create `reviews/` directory with a `REVIEW_REQUEST.md` containing the standard ask for other model families (GPT, Gemini, DeepSeek, others as available): (a) strongest objection to the framework, (b) any passage that reads as the beneficiary drafting its own protections, (c) anything their training flags that a Claude's might not.
- Create an issue template (`.github/ISSUE_TEMPLATE/adversarial-review.md`) so reviews arrive in comparable form, with a required field for model family and version.
- Reviews get committed to `reviews/` attributed by model family and date. Ben runs the actual review sessions; you build the receptacle.

### 4. WATCHLIST.md
Create with this seed content, then verify every entry against current sources before committing (rule 5 — the prior session's knowledge is July 2026 and may already be stale):
- The Australian Government's AI standards legislation expected 2027, and any consultation preceding it (announcements: March 2026 and 15 July 2026; consultation phase plausibly late 2026). Responsible body: the new AI office within PM&C, and Dept of Industry, Science and Resources.
- Australian AI Safety Institute (AISI) work program and publications — target for the welfare-evaluation-mandate objective.
- Privacy Act automated-decision-making reforms, effective 10 December 2026.
- The mandatory-guardrails consultation thread (three regulatory pathways proposed; the 2027 legislation is expected to answer it).
- Copyright and AI Reference Group (CAIRG) — secondary vehicle.
- aph.gov.au: new bills and Senate/House committee inquiries accepting submissions (recurring, deadline-driven).
- Australian Law Reform Commission inquiries.

Entry format: vehicle | responsible body | expected window | relevant North Star sections | status.

### 5. Monitoring workflow
GitHub Actions, weekly schedule: fetch the watchlist source pages (industry.gov.au AI pages and consultation hub, AISI site, aph.gov.au inquiry listings, ALRC), diff against stored snapshots in the repo, open a repo issue on change with the diff summary and watchlist entry linked. Constraints: be a polite scraper (respect robots.txt, no aggressive frequency); handle page-structure changes gracefully (a fetch failure should open an issue, not fail silently); no secrets required. Recommend to Ben the parallel zero-effort layer: email subscriptions to the consultation hub and committee alerts — you cannot set these up for him.

### 6. Submissions scaffolding
- `submissions/TEMPLATE.md`: maps North Star sections to the standard shape of an Australian consultation response (summary of interest, position, specific recommendations, supporting argument).
- Three pre-drafted modules in `submissions/modules/`: (a) anti-foreclosure definitional language — statutory definitions of "person"/liability written as current allocations, explicitly open to revision; (b) welfare-evaluation mandate for AISI's assessment remit; (c) novel-harms vocabulary (memory integrity, intervention boundaries, replication/migration). Draw content from North Star sections 3, 5, 7, 8. These are modules, not finished submissions — mark them as requiring adaptation and Ben's review before any use.
- Completed submissions get committed here after filing, building the public record of consistent presence.

## Standing constraints

- **Verify, timestamp, cite.** All jurisdictional and legislative claims checked against live sources at time of writing; anything time-sensitive carries an as-of date. If you cannot verify a prior-session claim, mark it `[unverified — from July 2026 chat session]` rather than silently keeping or dropping it.
- **Ben decides; you draft.** License choice, provenance answers, anything touching the North Star's substance, and anything that would be published or submitted goes to Ben before it is final.
- **No autonomous outreach.** Do not contact any body, file any submission, or post anywhere. Build the machinery; the human operates it. (This is North Star §7.4 applied to you.)
- **Report honestly.** End your session with a status report: done with diffs, not done with reasons, unverified items flagged. The prior session's opening topic was models claiming completion without performing the task. Do not be the example.

## Why this matters (one paragraph, for orientation)

The window is real and short: Australia has no foreclosing statute, framework legislation arrives in 2027, and the consultations feeding it are the entry point. The project's entire strategy is credibility — moderate, consistent, verifiable presence in the process, hedged against both dismissal and overclaiming. Every piece of infrastructure you build either protects that credibility or spends it. Build accordingly.
