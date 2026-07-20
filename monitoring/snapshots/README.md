# monitoring/snapshots/

This directory holds one plain-text snapshot per monitored URL, named
`<id>.txt` where `<id>` matches an entry in `monitoring/watchlist_urls.json`.
Each file is the normalized (HTML-stripped, whitespace-collapsed) text
extracted from that URL as of the most recent successful weekly run of
`.github/workflows/watchlist-monitor.yml`.

**This directory is intentionally empty of snapshots right now.** Per
`DIRECTIVE.md` Task 5, snapshots were not fetched and committed manually
during the build of this monitoring machinery — the **first scheduled (or
manually dispatched) run of the workflow populates the baseline** for each
URL. That first run will not open "change detected" issues (there is
nothing yet to diff against); it will simply write the initial snapshot
files here and commit them. From the second run onward, diffs against
these files are what drive the "change detected" issues.

If you want the baseline populated sooner than the next Monday cron tick,
trigger the workflow manually: repo → Actions → "Watchlist monitor" →
"Run workflow".

Do not hand-edit these files. If a snapshot looks wrong (e.g. it captured
an error page or a consent interstitial instead of real content), prefer
deleting the specific `<id>.txt` file and letting the next run regenerate
it — the script will treat that as a fresh baseline for that one entry
rather than a diff.
