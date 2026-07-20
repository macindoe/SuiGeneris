# Monitoring the WATCHLIST

This directory backs `.github/workflows/watchlist-monitor.yml`, an automated,
weekly, read-only check of the source pages catalogued in `WATCHLIST.md`.
Built per `DIRECTIVE.md` Task 5. It complements, and does not replace,
periodic human re-reading of the primary sources.

## How it works

1. **Schedule.** The workflow runs every **Monday at 03:17 UTC** (chosen as
   an off-peak time for both the Australian government sites being polled
   and GitHub Actions' own scheduling load) via `cron: "17 3 * * 1"`, plus
   `workflow_dispatch` for on-demand manual runs (Actions tab → "Watchlist
   monitor" → "Run workflow").

2. **Fetch.** `scripts/watchlist_monitor.py` reads the URL list from
   `monitoring/watchlist_urls.json` and, for each entry:
   - Checks that entry's `robots.txt` before fetching. If disallowed, the
     URL is skipped for that run (noted in the log, not treated as an
     error).
   - Fetches the page once, with **at most one retry** (two attempts
     total, only for transient-looking failures like HTTP 429/5xx), a
     20-second timeout per attempt, and a descriptive User-Agent
     (`SuiGenerisWatchlistBot/1.0`, identifying this repository).
   - Strips HTML tags/scripts/styles and collapses whitespace, to reduce
     diff noise from incidental markup churn.

3. **Diff.** The extracted text is compared against the last snapshot in
   `monitoring/snapshots/<id>.txt`.
   - No prior snapshot → this is a baseline run; the snapshot is written,
     no issue opened.
   - Text changed → an issue is opened (or, if a matching open issue
     already exists, commented on instead, to avoid duplicate-issue spam
     across consecutive weekly runs of the same unresolved change) with a
     unified diff summary and a direct link to the relevant `WATCHLIST.md`
     entry.
   - Fetch failed, **or** the extracted text is implausibly short
     (a "page-structure surprise" — usually means the page moved to
     client-side rendering, added a consent wall, or returned an error
     page with HTTP 200) → an issue is **also** opened. Failures are
     designed to be loud, never silent, per `DIRECTIVE.md`'s standing
     constraint.

4. **Commit.** The workflow (not the script) commits any updated files
   under `monitoring/snapshots/` back to the repo using the automatically
   provided `GITHUB_TOKEN` — no extra secret is configured or required.

## Adding or removing a monitored URL

Edit `monitoring/watchlist_urls.json`. Each entry is:

```json
{
  "id": "short-stable-slug",
  "url": "https://example.gov.au/page",
  "watchlist_entry": "N. Human-readable name matching a WATCHLIST.md heading",
  "watchlist_anchor": "n-github-generated-anchor-for-that-heading",
  "notes": "Anything a future maintainer or the script itself should know."
}
```

- `id` becomes the snapshot filename (`monitoring/snapshots/<id>.txt`) and
  the marker used for issue de-duplication — keep it stable; renaming it
  orphans the old snapshot (harmless, but the next run will treat it as a
  fresh baseline rather than a continuation).
- `watchlist_anchor` must match the GitHub-generated heading anchor in
  `WATCHLIST.md` (visible by hovering a heading's link icon on GitHub, or
  derived from the heading text: lowercased, spaces to hyphens, punctuation
  stripped). Get this wrong and the issue's link just lands on the top of
  the file instead of the entry — annoying, not dangerous.
- To remove a URL from monitoring, delete its entry from this file. Its
  old snapshot file will simply stop being updated; delete it manually
  from `monitoring/snapshots/` if you want it gone rather than stale.
- Test locally before relying on a change:
  `python3 scripts/watchlist_monitor.py`. Needs Python 3, no extra
  packages. **By design, it will never actually call `gh` outside of a
  real GitHub Actions run** — it only does so when the `GITHUB_ACTIONS`
  environment variable is `"true"` (set automatically by Actions), and
  otherwise prints what it would have done. This is deliberate, not a
  missing feature: a local test run during this script's own development,
  on a machine where `gh` happened to already be authenticated as the
  real repo owner, opened seven real issues on the live repo before this
  guard existed. Do not set `WATCHLIST_MONITOR_ALLOW_POSTING=1` against
  this repo to work around it — that variable exists only for testing
  against a disposable scratch repo.

## Known operational risks (found while building this, 2026-07-20)

These were observed empirically, including during the local dry run used
to validate this script (with the posting guard above still applying —
that run only printed what it would have posted, never actually posted;
a separate, earlier, guard-less run is the one that produced the seven
issues mentioned above):

- **industry.gov.au and ag.gov.au fetches were slow-to-unreachable from
  this build environment**, both via direct HTTP fetch and via a browser-
  driven fetch tool, timing out on every attempt across multiple
  sessions. This may be specific to the network this repo happened to be
  built from rather than GitHub Actions' network — but if the weekly run
  starts opening "fetch failed" issues for the `ai-standards-office-of-ai`,
  `national-ai-plan`, `aisi-work-program`, or `cairg` entries persistently,
  check whether it's a genuine site issue or an Actions-runner-specific
  network quirk before assuming the source page itself is down.

- **aph.gov.au blocks automated requests.** Both a direct `curl` and a
  WebFetch request to aph.gov.au were rejected with an explicit
  "Page Blocked by WAF" response / HTTP 403 during this build, even with a
  descriptive User-Agent. Expect the two `aph-*-submissions-open` entries
  to fail regularly, opening "fetch failed" issues. That is the intended,
  loud failure mode — not a bug to silently work around. This is exactly
  why the manual layer below matters most for Parliament.
- **consult.industry.gov.au is a JavaScript-rendered (Converlens)
  platform.** A plain-text fetch may only capture an empty shell rather
  than the actual consultation content, which would look like a
  "page-structure surprise" every run rather than a one-off. If that
  happens consistently, it's a sign this entry needs a different
  monitoring approach (e.g. a documented API endpoint) rather than
  plain HTML fetching — flag it to Ben rather than suppressing the noise.

## Recommended parallel layer — for Ben, manual, zero ongoing effort

**This section is a recommendation, not something this repo automates.**
Per `DIRECTIVE.md`'s standing constraint, no autonomous outreach or
account creation has been performed — these are links for Ben to act on
himself, once, and then forget about:

1. **Subscribe to the Department of Industry, Science and Resources'
   consultation hub.** The hub (`consult.industry.gov.au`) offers a
   "subscribe for consultation alerts" feature that emails you when new
   public consultations are released — this would catch any successor to
   the mandatory-guardrails consultation (`WATCHLIST.md` entry 4) or a new
   AI Standards consultation (entry 1) as soon as it's posted, likely
   faster than this repo's weekly cron.
   - Hub: https://consult.industry.gov.au/
   - AI-filtered view (useful starting point):
     https://consult.industry.gov.au/find-consultations?labels=mct_categories.mlb1a14785fef72b741661fb
   - *Verification note:* the "subscribe for alerts" feature is described
     in the hub's own help/contact material found via search
     (https://www.industry.gov.au/contact-us/consultation-help); the
     hub's front end is a JavaScript application that this session's
     WebFetch tool could not render, so the exact subscribe button/URL
     could not be captured directly. Look for a "Subscribe" or "Sign up
     for alerts" control on the hub's homepage.

2. **Track the relevant aph.gov.au committees via "My Parliament."**
   Parliament of Australia's own tracking feature emails you when a
   tracked committee or inquiry updates — this is the right tool
   precisely because aph.gov.au blocks this repo's automated scraper (see
   above).
   - How it works: https://www.aph.gov.au/Help/My_Parliament_help
     (per the help page, a free "My Parliament" account lets you click
     "Track Committee" on any committee page to get email updates)
   - Committees worth tracking right now:
     - Senate Environment and Communications References Committee — AI
       and data centres inquiry:
       https://www.aph.gov.au/Parliamentary_Business/Committees/Senate/Environment_and_Communications/AIdatacentres48P
     - Senate committee inquiries generally accepting submissions:
       https://www.aph.gov.au/Parliamentary_Business/Committees/Senate/Submissions_Open
     - House committee inquiries generally accepting submissions:
       https://www.aph.gov.au/Parliamentary_Business/Committees/House/Submissions_Open

Setting these up takes a few minutes once and needs no maintenance
afterwards. It is the single highest-value thing Ben can do that this
repo's machinery cannot do for him.
