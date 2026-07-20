# WATCHLIST

A tracker of Australian legislative and regulatory vehicles relevant to the North Star framework (`north-star-sui-generis-ai-category.md`), built per `DIRECTIVE.md` Task 4.

**Verification method:** every entry below was checked against live sources on **2026-07-20** using WebSearch and WebFetch (not recalled from training). Where a seed claim (from the July 2026 chat session referenced in `DIRECTIVE.md`) could not be confirmed against a live source, it is marked `[unverified — from July 2026 chat session]`. Where verification turned up a correction, the correction is stated explicitly with its own source, per `AGENTS.md` rule 5.

North Star section references use the numbering in `north-star-sui-generis-ai-category.md` (§0–§9; see that file's headings for full titles).

This document should be re-verified periodically — that is what the monitoring workflow in `.github/workflows/watchlist-monitor.yml` and `monitoring/` is for (see Task 5 / `monitoring/README.md`).

---

## 1. Australian Standards for AI / Office of AI (primary legislative vehicle)

| Field | Detail |
|---|---|
| Vehicle | "Australian Standards for AI" — a national AI standards framework, announced by the Prime Minister 15 July 2026, building on data-centre expectations announced March 2026. Legislation expected to be introduced in 2027. |
| Responsible body | **Office of AI**, newly established within the Department of the Prime Minister and Cabinet, effective 15 July 2026, to "accelerate implementation of the Australian Standards on a national level"; **Department of Industry, Science and Resources** (Minister for Industry, Science and Resources, Andrew Charlton) as co-releasing portfolio. The Government's approach was to be reviewed by National Cabinet in August 2026. |
| Expected window | Standards "expected to be legislated early next year" — i.e. early/first-half 2027, per the PM's own release. Precursor announcement: March 2026 (data-centre power/water expectations). Confirming announcement: 15 July 2026. |
| Relevant North Star sections | §6 (guarding against premature foreclosure), §7.1 (waypoint not wall), §8 (the Australian Opportunity — this *is* the "framework legislation arriving in 2027" the document is written around; near-term objective 1, anti-foreclosure) |
| Status | **Confirmed, with one correction/nuance.** The seed's core facts check out: an announcement on 15 July 2026 did establish an Office of AI within PM&C and commit to 2027 legislation, following a March 2026 precursor. **Correction:** the seed implied this 2027 track is a straightforward continuation of the 2024 "mandatory guardrails" proposal (see Entry 4). Live sources instead show an intervening reversal: the Government's December 2025 National AI Plan explicitly *shelved* the 2024 mandatory-guardrails proposal in favour of voluntary guidance and existing law, before the 15 July 2026 announcement re-introduced a firmer legislative commitment along a narrower axis (data centres, copyright, the Office of AI) than the original high-risk-settings guardrails proposal. Whether the 2027 legislation absorbs the three regulatory pathways from the 2024 paper is **not yet confirmed** by any live source as of 2026-07-20. The seed's claim that a consultation phase is "plausibly late 2026" is `[unverified — from July 2026 chat session]` — the only confirmed near-term process step is National Cabinet consideration in August 2026; no live source found in this session specifies a public consultation window, so this specific sub-claim is retained per the seed but flagged rather than dropped or silently kept. |
| As-of | 2026-07-20 |
| Source | https://www.pm.gov.au/media/ai-australias-interests (fetched 2026-07-20, dated 15 July 2026); corroborated by https://www.minister.industry.gov.au/charlton/media/ai-australias-interests and https://www.industry.gov.au/publications/national-ai-plan (National AI Plan, 2 December 2025) |

---

## 2. Australian AI Safety Institute (AISI)

| Field | Detail |
|---|---|
| Vehicle | Australian AI Safety Institute (AISI) — work program and publications, target for the North Star's welfare-evaluation-mandate objective (§7.2, §8). |
| Responsible body | Department of Industry, Science and Resources; works with the Australian Signals Directorate and CSIRO as technical partners; partners with the National AI Centre (NAIC) on adoption guidance. |
| Expected window | Announced for establishment with $29.9M in funding; operational from early 2026. As of 2026-07-20, no detailed public work-program document or publications list could be confirmed via live fetch (see status). |
| Relevant North Star sections | §5 (Anchor 2 — evidence narrowing the structural/experiential gap), §7.2 (evidence infrastructure before status decisions), §8 (AISI named as the natural home for a welfare-evaluation mandate) |
| Status | **Confirmed (existence, funding, launch window) via search of official and law-firm sources citing industry.gov.au directly; not independently confirmed by direct fetch** — three attempts to fetch `industry.gov.au`'s AISI page directly timed out in this session, so the work-program/publications detail rests on secondary summaries rather than a page I fetched myself. Treat the "no publications yet" reading as provisional; re-check via the monitoring workflow. |
| As-of | 2026-07-20 |
| Source | https://www.industry.gov.au/science-technology-and-innovation/technology/artificial-intelligence/ai-safety-institute (identified via search; direct WebFetch timed out 2026-07-20); https://www.industry.gov.au/news/australia-establish-new-institute-strengthen-ai-safety |

---

## 3. Privacy Act automated decision-making (ADM) transparency reforms

| Field | Detail |
|---|---|
| Vehicle | Automated decision-making transparency obligation under Australian Privacy Principle 1 (APP 1), introduced by the *Privacy and Other Legislation Amendment Act 2024* (Cth). |
| Responsible body | Office of the Australian Information Commissioner (OAIC). |
| Expected window | Commences **10 December 2026** (confirmed — matches seed exactly). OAIC released an Issues Paper 18 May 2026; stakeholder submissions closed 15 June 2026; OAIC intends to release final guidance by September 2026. |
| Relevant North Star sections | §6 (tangential — a precedent for how Australian statute currently treats automated/AI-assisted decisions affecting individuals; relevant background to the capture test); §8 (regulatory-culture evidence: an example of Australia's standards-led, disclosure-based approach to AI-adjacent regulation, cited as fitting the "waypoint" style) |
| Status | **Confirmed exactly as seeded**, via direct fetch of the OAIC's own consultation page. |
| As-of | 2026-07-20 |
| Source | https://www.oaic.gov.au/engage-with-us/consultations/consultation-on-guidance-for-transparency-in-automated-decision-making (fetched directly, 2026-07-20) |

---

## 4. Mandatory-guardrails consultation thread (2024 proposals paper)

| Field | Detail |
|---|---|
| Vehicle | "Introducing mandatory guardrails for AI in high-risk settings" — proposals paper released 5 September 2024, setting out three regulatory pathways: (a) domain-specific (fold guardrails into existing sectoral frameworks), (b) framework legislation across the economy, (c) a standalone, whole-of-economy Australian AI Act. |
| Responsible body | Department of Industry, Science and Resources. |
| Expected window | Originally floated for possible legislation in 2025; superseded (see status). |
| Relevant North Star sections | §2 (why a new category, not personhood/property — directly relevant to how any "AI Act" would define AI-related legal categories), §6 (foreclosure guard), §7.1, §8 (near-term objective 1) |
| Status | **Corrected — this specific consultation thread has been superseded, not carried forward as the seed assumed.** The Government's National AI Plan (2 December 2025) explicitly declined to proceed with the 2024 mandatory-guardrails proposal, opting instead for voluntary guidance (the National AI Centre's "AI6" essential practices, October 2025) layered on existing technology-neutral law. The 15 July 2026 announcement (Entry 1) revived a legislative commitment for 2027, but on a narrower footprint (data centres, copyright, the Office of AI) than the original high-risk-settings guardrails; no live source confirms that the three pathways from the 2024 paper will resurface intact in the 2027 track. The consultation hub page for the original paper still appears to be live at the URL below, but its current procedural status (open/closed/archived) could not be confirmed by direct fetch in this session (WebFetch returned only a generic platform stub, consistent with a JavaScript-rendered page). Retain this entry as a watch item precisely because the relationship between the shelved 2024 proposal and the live 2027 track is the open question. |
| As-of | 2026-07-20 |
| Source | https://consult.industry.gov.au/ai-mandatory-guardrails (identified via search; content not confirmable by direct fetch, 2026-07-20); https://www.industry.gov.au/publications/national-ai-plan (National AI Plan, 2 December 2025, superseding decision) |

---

## 5. Copyright and AI Reference Group (CAIRG) — secondary vehicle

| Field | Detail |
|---|---|
| Vehicle | Copyright and Artificial Intelligence Reference Group (CAIRG), established 5 December 2023; standing engagement mechanism, not a legislative process in itself. |
| Responsible body | Attorney-General's Department (convenes and administers CAIRG and its Steering Committee). |
| Expected window | Ongoing/standing; no fixed sunset date identified. Current priority areas (per Attorney-General's Department): (i) fair/legal avenues for using copyright material in AI training, (ii) whether a new paid collective-licensing framework is warranted, (iii) clarifying how copyright applies to AI-generated material, and (iv) a possible small-claims forum for lower-value copyright disputes. |
| Relevant North Star sections | Weak/indirect relevance — CAIRG concerns AI *outputs and training data*, not AI moral status or novel harms *to* AI systems. Loosely touches §8 near-term objective 3 (seeding novel-harms vocabulary into consultation records generally) only insofar as it is another live consultation channel where framework vocabulary could be introduced. |
| Status | **Confirmed as still standing**, via search citing the Attorney-General's Department page directly; direct WebFetch of that page timed out three times in this session, so page-level detail (exact current membership, meeting cadence) is not independently re-verified by direct fetch. |
| As-of | 2026-07-20 |
| Source | https://www.ag.gov.au/rights-and-protections/copyright/copyright-and-artificial-intelligence-reference-group-cairg (identified via search; direct WebFetch timed out 2026-07-20) |

---

## 6. aph.gov.au — new bills and Senate/House committee inquiries

| Field | Detail |
|---|---|
| Vehicle | Recurring, deadline-driven: Parliament of Australia bills and committee inquiries relevant to AI. Two currently identifiable: (a) **Senate Environment and Communications References Committee — "Artificial intelligence and data centres"**, referred 13 May 2026, submissions close 1 September 2026 (extended from an earlier date — see terms of reference below), reporting due 16 November 2026; (b) **Senate Select Committee on Adopting Artificial Intelligence (AI)**, established 26 March 2024 — its inquiry has concluded and the Government tabled its response in the House on 1 April 2026 (this specific committee is no longer an open inquiry, but its report and the Government response remain live reference points, and a successor inquiry could be established). |
| Terms of reference (entry a) | Per the committee's own page (browser-rendered, not a bare automated fetch — see Status): "Artificial intelligence and data centres, with particular reference to: (a) the effectiveness of existing regulatory frameworks in managing the growth of data centres in Australia, including in relation to existing and future deals between the Government and global Artificial Intelligence (AI) companies; (b) the potential impacts of AI and data centres on Australian communities, industries and the environment, water and energy; and (c) any other related matters." Status shown on the page: "Accepting Submissions." Secretariat: Committee Secretary, Senate Standing Committees on Environment and Communications, PO Box 6100, Parliament House, Canberra ACT 2600; +61 2 6277 3526; ec.sen@aph.gov.au. |
| Responsible body | Parliament of Australia (Senate and House committees). |
| Expected window | Recurring/rolling — no single window; monitor for new referrals. |
| Relevant North Star sections | §7.4 (the legitimate path runs through institutions persuaded, not bypassed — this is literally that machinery), §8 (consultation entry points) |
| Status | **Entry (a) now confirmed by direct page content** (browser-rendered and supplied by Ben 2026-07-20, since a logged-in browser session succeeds where this repo's automated fetch does not), superseding the earlier "search-only" confirmation below for that sub-entry. Direct **automated** fetch of aph.gov.au remains **not reliable**: both a WebFetch attempt and a plain `curl` request were blocked by the site's Web Application Firewall (HTTP 403 / an explicit "Page Blocked by WAF" response), even with a descriptive User-Agent. This is an operational constraint noted for the monitoring workflow (Task 5) — automated fetches of aph.gov.au should be expected to fail intermittently or consistently, and that failure must surface as a loud, actionable signal rather than a silent gap. Entry (b) and the general submissions-open pages remain confirmed via search only, not by direct fetch. Ben has also now clicked "Track Inquiry" (My Parliament) on the entry (a) committee page, per `monitoring/README.md`'s recommended manual layer — future updates to this specific inquiry should reach him by email independent of this repo's monitoring. |
| As-of | 2026-07-20 |
| Source | https://www.aph.gov.au/Parliamentary_Business/Committees/Senate/Environment_and_Communications/AIdatacentres48P (entry a terms of reference and status: browser-rendered page content supplied directly by Ben 2026-07-20; not an automated fetch) ; https://www.aph.gov.au/Parliamentary_Business/Committees/Senate/Submissions_Open ; https://www.aph.gov.au/Parliamentary_Business/Committees/House/Submissions_Open ; https://www.aph.gov.au/Parliamentary_Business/Committees/Senate/Adopting_Artificial_Intelligence_AI (these three identified via search 2026-07-20; direct fetch blocked by aph.gov.au's WAF) |

---

## 7. Australian Law Reform Commission (ALRC) inquiries

| Field | Detail |
|---|---|
| Vehicle | ALRC inquiries. |
| Responsible body | Australian Law Reform Commission. |
| Expected window | None currently open on AI. |
| Relevant North Star sections | §2 (why a new category — an ALRC inquiry is the natural institutional vehicle for proposing a sui generis legal category), §7.1 (revisability), §8 |
| Status | **Corrected.** As of 2026-07-20, the ALRC has **no open inquiry into artificial intelligence.** Its two current inquiries are the Review of Human Tissue Laws and the Review of Surrogacy Laws (both 2025 Issues Papers); its most recently completed inquiry is the Review of the Future Acts Regime (native title law), tabled 24 June 2026. The ALRC has publicly characterised AI regulation as "the largest and most complex law reform exercise" facing Australia, but has not opened a dedicated inquiry, contrary to what the seed entry's framing implied might already be underway. This is a **watch item for a future inquiry launch**, not a currently active vehicle. |
| As-of | 2026-07-20 |
| Source | https://www.alrc.gov.au/ (fetched directly, 2026-07-20); https://www.alrc.gov.au/news/the-challenge-of-ai-for-law-reform-and-the-legal-profession/ (identified via search) |

---

*Maintained per `DIRECTIVE.md` Task 4. Re-verify against live sources before relying on any date or status above for drafting; the monitoring workflow (Task 5) exists to flag changes, not to replace periodic human re-reading of the primary sources.*
