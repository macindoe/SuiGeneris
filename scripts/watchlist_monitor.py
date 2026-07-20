#!/usr/bin/env python3
"""
watchlist_monitor.py

Polite, zero-dependency (Python 3 stdlib only) monitor for the source pages
listed in monitoring/watchlist_urls.json, which track the vehicles catalogued
in WATCHLIST.md. Built per DIRECTIVE.md Task 5.

For each configured URL, this script:
  1. Checks robots.txt before fetching. If disallowed, the URL is skipped
     and noted in the run summary (not fetched, no issue opened for that
     alone).
  2. Fetches the page once, with a single retry on failure (two attempts
     total), a short timeout, and a descriptive User-Agent identifying this
     repository.
  3. Normalises/extracts text content (tags stripped, scripts/styles
     removed, whitespace collapsed) to reduce diff noise from things like
     rotating nonces, ad IDs, or timestamps embedded in markup.
  4. Diffs the extracted text against the last stored snapshot in
     monitoring/snapshots/<id>.txt.
       - No prior snapshot: this is a baseline run. The snapshot is written
         and no issue is opened (nothing to compare against yet).
       - Diff found: an issue is opened via the gh CLI with a diff summary
         and a link to the relevant WATCHLIST.md entry.
       - Fetch failure (network error, timeout, non-200 status) or a
         "page-structure surprise" (extracted text implausibly short,
         suggesting the page changed shape rather than content): an issue
         is ALSO opened. Failures must be loud, never silent.
  5. Writes an updated snapshot file for anything successfully fetched.

Git commit/push of updated snapshots is handled by the calling GitHub
Actions workflow (.github/workflows/watchlist-monitor.yml), not by this
script -- this script only reads/writes files under monitoring/snapshots/
and talks to `gh` for issues.

Usage:
    python3 scripts/watchlist_monitor.py

Environment:
    GITHUB_REPOSITORY  "owner/repo" -- used to build WATCHLIST.md links and
                        to scope `gh` calls. Set automatically by GitHub
                        Actions; falls back to a placeholder if absent so
                        the script remains runnable locally for testing.
    GITHUB_TOKEN / GH_TOKEN -- required for `gh issue create` /
                        `gh issue list` / `gh issue comment` to work.
                        Provided automatically in Actions via
                        secrets.GITHUB_TOKEN; no extra secret is needed.
    GITHUB_ACTIONS      Set to "true" automatically inside GitHub Actions.
                        This script treats that as its permission to
                        actually call `gh` and touch the real issue
                        tracker. Outside of Actions (e.g. a developer
                        running this locally, where `gh` may already be
                        authenticated as a real account with write access
                        to the real repo), all `gh` calls are skipped and
                        printed instead -- see safe_to_post() below. Set
                        WATCHLIST_MONITOR_ALLOW_POSTING=1 to override this
                        deliberately for local testing against a
                        disposable scratch repo. Do not set it against a
                        real repo -- an earlier local test run during this
                        script's own development did exactly that by
                        accident and opened seven real issues.
"""

from __future__ import annotations

import dataclasses
import difflib
import html.parser
import json
import os
import re
import shutil
import subprocess
import sys
import time
import urllib.error
import urllib.request
import urllib.robotparser
from pathlib import Path
from urllib.parse import urlparse

REPO_ROOT = Path(__file__).resolve().parent.parent
CONFIG_PATH = REPO_ROOT / "monitoring" / "watchlist_urls.json"
SNAPSHOT_DIR = REPO_ROOT / "monitoring" / "snapshots"
WATCHLIST_PATH = REPO_ROOT / "WATCHLIST.md"

USER_AGENT = (
    "SuiGenerisWatchlistBot/1.0 "
    "(+https://github.com/{repo}; automated, low-frequency, weekly; "
    "monitors public AI-policy pages for the WATCHLIST.md in this repo; "
    "contact via repo issues)"
)

FETCH_TIMEOUT_SECONDS = 20
MAX_ATTEMPTS = 2  # one retry beyond the first attempt, no more
RETRY_BACKOFF_SECONDS = 5
MIN_PLAUSIBLE_TEXT_CHARS = 200  # below this, treat as a page-structure surprise
ISSUE_LABEL = "watchlist-monitor"


def repo_slug() -> str:
    return os.environ.get("GITHUB_REPOSITORY", "OWNER/REPO")


def default_branch() -> str:
    return os.environ.get("WATCHLIST_MONITOR_BRANCH", "main")


def watchlist_url(anchor: str) -> str:
    return f"https://github.com/{repo_slug()}/blob/{default_branch()}/WATCHLIST.md#{anchor}"


@dataclasses.dataclass
class WatchEntry:
    id: str
    url: str
    watchlist_entry: str
    watchlist_anchor: str
    notes: str = ""


class _TextExtractor(html.parser.HTMLParser):
    """Minimal, dependency-free HTML-to-text extractor.

    Strips tags, drops <script>/<style>/<noscript> content, and keeps only
    visible text. This is intentionally crude -- the goal is noise
    reduction for diffing, not faithful rendering.
    """

    _SKIP_TAGS = {"script", "style", "noscript", "template"}

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self._skip_depth = 0
        self.chunks: list[str] = []

    def handle_starttag(self, tag, attrs):
        if tag in self._SKIP_TAGS:
            self._skip_depth += 1

    def handle_endtag(self, tag):
        if tag in self._SKIP_TAGS and self._skip_depth > 0:
            self._skip_depth -= 1

    def handle_data(self, data):
        if self._skip_depth == 0:
            self.chunks.append(data)

    def get_text(self) -> str:
        return "".join(self.chunks)


def normalize_html_to_text(raw_html: str) -> str:
    parser = _TextExtractor()
    try:
        parser.feed(raw_html)
        parser.close()
    except Exception:
        # Malformed markup shouldn't crash the run; fall back to a crude
        # tag-strip so we still have *something* to diff.
        text = re.sub(r"<[^>]+>", " ", raw_html)
        return _collapse_whitespace(text)
    return _collapse_whitespace(parser.get_text())


def _collapse_whitespace(text: str) -> str:
    text = re.sub(r"[ \t\r\f\v]+", " ", text)
    text = re.sub(r"\n\s*\n+", "\n", text)
    lines = [line.strip() for line in text.split("\n")]
    lines = [line for line in lines if line]
    return "\n".join(lines).strip()


def load_config() -> list[WatchEntry]:
    data = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    return [
        WatchEntry(
            id=item["id"],
            url=item["url"],
            watchlist_entry=item.get("watchlist_entry", ""),
            watchlist_anchor=item.get("watchlist_anchor", ""),
            notes=item.get("notes", ""),
        )
        for item in data["urls"]
    ]


def robots_allows(url: str, user_agent: str) -> tuple[bool, str]:
    """Return (allowed, reason). Fails open with a clear reason if robots.txt
    itself cannot be retrieved or parsed -- since every monitored host was
    manually reviewed at Task-4 time and none disallow the specific paths
    monitored here, an unreadable robots.txt (e.g. a WAF block page served
    in its place) is treated as 'unknown, proceed' rather than 'blocked'.
    """
    parsed = urlparse(url)
    robots_url = f"{parsed.scheme}://{parsed.netloc}/robots.txt"
    rp = urllib.robotparser.RobotFileParser()
    rp.set_url(robots_url)
    try:
        req = urllib.request.Request(robots_url, headers={"User-Agent": user_agent})
        with urllib.request.urlopen(req, timeout=FETCH_TIMEOUT_SECONDS) as resp:
            body = resp.read().decode("utf-8", errors="replace")
        # A WAF/interstitial block page masquerading as robots.txt won't
        # parse as meaningful directives; detect the obvious case and fail
        # open with a note rather than silently obeying garbage.
        if "user-agent" not in body.lower():
            return True, f"robots.txt at {robots_url} did not look like a real robots file; proceeding cautiously"
        rp.parse(body.splitlines())
    except Exception as exc:  # noqa: BLE001 - deliberately broad, this is best-effort
        return True, f"could not retrieve/parse {robots_url} ({exc}); proceeding cautiously"

    allowed = rp.can_fetch(user_agent, url)
    return allowed, f"robots.txt at {robots_url} {'allows' if allowed else 'disallows'} this path"


def fetch(url: str, user_agent: str) -> tuple[int | None, str | None, str | None]:
    """Fetch a URL with one retry. Returns (status_code, body, error)."""
    last_error = None
    for attempt in range(1, MAX_ATTEMPTS + 1):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": user_agent, "Accept": "text/html,*/*"})
            with urllib.request.urlopen(req, timeout=FETCH_TIMEOUT_SECONDS) as resp:
                status = resp.status
                body = resp.read().decode("utf-8", errors="replace")
                return status, body, None
        except urllib.error.HTTPError as exc:
            last_error = f"HTTP {exc.code}: {exc.reason}"
            # A 4xx/5xx is a real response; don't burn the retry budget on
            # a definitive rejection (e.g. a WAF 403), but do retry once on
            # 429/5xx which can be transient.
            if exc.code in (429, 500, 502, 503, 504) and attempt < MAX_ATTEMPTS:
                time.sleep(RETRY_BACKOFF_SECONDS)
                continue
            return exc.code, None, last_error
        except Exception as exc:  # noqa: BLE001
            last_error = f"{type(exc).__name__}: {exc}"
            if attempt < MAX_ATTEMPTS:
                time.sleep(RETRY_BACKOFF_SECONDS)
                continue
            return None, None, last_error
    return None, None, last_error


def gh_available() -> bool:
    return shutil.which("gh") is not None


def safe_to_post() -> bool:
    """Refuse to touch the real GitHub issue tracker unless we can tell
    we're actually running inside this repo's GitHub Actions workflow (or
    a human has explicitly opted in). `gh` authenticates using whatever
    account happens to be logged in on the machine running this script --
    on a developer's own machine that is very likely a real, personal
    account with write access to the real repo, not a sandboxed identity.

    This check exists because of a real incident during development: a
    local test run of this script, on a machine where `gh` was already
    authenticated as the repo owner, opened seven real issues on the live
    repository. DIRECTIVE.md is explicit that this project's machinery
    must never post anywhere autonomously; a script that can't tell the
    difference between a CI run and a developer's laptop is a standing
    risk of repeating that mistake. Set WATCHLIST_MONITOR_ALLOW_POSTING=1
    to override deliberately (e.g. to test issue creation against a
    disposable scratch repo)."""
    if os.environ.get("GITHUB_ACTIONS") == "true":
        return True
    if os.environ.get("WATCHLIST_MONITOR_ALLOW_POSTING") == "1":
        return True
    return False


def ensure_label() -> None:
    if not gh_available():
        return
    if not safe_to_post():
        print(
            "DRY RUN (not in GitHub Actions and WATCHLIST_MONITOR_ALLOW_POSTING "
            "is not set): skipping 'gh label create'."
        )
        return
    subprocess.run(
        [
            "gh", "label", "create", ISSUE_LABEL,
            "--color", "5319e7",
            "--description", "Opened automatically by scripts/watchlist_monitor.py",
        ],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=False,  # ignore "already exists" errors
    )


def find_existing_open_issue(marker: str) -> str | None:
    """Look for an already-open issue whose title contains `marker`, to
    avoid opening duplicate issues on consecutive weekly runs of an
    unresolved problem. Returns the issue number as a string, or None."""
    if not gh_available():
        return None
    if not safe_to_post():
        print(
            f"DRY RUN: would have searched for an existing open issue matching "
            f"'{marker}' (skipped: not in GitHub Actions and "
            f"WATCHLIST_MONITOR_ALLOW_POSTING is not set)."
        )
        return None
    result = subprocess.run(
        [
            "gh", "issue", "list",
            "--repo", repo_slug(),
            "--label", ISSUE_LABEL,
            "--state", "open",
            "--search", marker,
            "--json", "number,title",
            "--limit", "20",
        ],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0 or not result.stdout.strip():
        return None
    try:
        issues = json.loads(result.stdout)
    except json.JSONDecodeError:
        return None
    for issue in issues:
        if marker in issue.get("title", ""):
            return str(issue["number"])
    return None


def open_or_comment_issue(marker: str, title: str, body: str) -> None:
    if not gh_available():
        print(f"::warning::gh CLI not available; would have opened issue: {title}")
        print(body)
        return

    if not safe_to_post():
        print(
            f"DRY RUN (not in GitHub Actions and WATCHLIST_MONITOR_ALLOW_POSTING "
            f"is not set): would have opened/commented on an issue titled:\n"
            f"  {title}\n"
            f"--- body ---\n{body}\n--- end body ---"
        )
        return

    existing = find_existing_open_issue(marker)
    if existing:
        subprocess.run(
            ["gh", "issue", "comment", existing, "--repo", repo_slug(), "--body", body],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        print(f"Commented on existing open issue #{existing} ({marker})")
        return

    result = subprocess.run(
        [
            "gh", "issue", "create",
            "--repo", repo_slug(),
            "--title", title,
            "--body", body,
            "--label", ISSUE_LABEL,
        ],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        # Retry once without the label, in case the label doesn't exist and
        # ensure_label() itself failed for some reason -- an issue with no
        # label beats no issue at all (fail loudly, never silently).
        result2 = subprocess.run(
            ["gh", "issue", "create", "--repo", repo_slug(), "--title", title, "--body", body],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        if result2.returncode != 0:
            print(f"::error::Failed to open issue '{title}': {result.stderr.strip()} / {result2.stderr.strip()}")
        else:
            print(f"Opened issue (no label): {title}")
    else:
        print(f"Opened issue: {title}")


def process_entry(entry: WatchEntry) -> None:
    print(f"\n=== {entry.id} ===\n{entry.url}")
    user_agent = USER_AGENT.format(repo=repo_slug())

    allowed, reason = robots_allows(entry.url, user_agent)
    print(f"robots.txt check: {reason}")
    if not allowed:
        print(f"SKIPPED (robots.txt disallows): {entry.url}")
        return

    status, body, error = fetch(entry.url, user_agent)

    snapshot_path = SNAPSHOT_DIR / f"{entry.id}.txt"
    link = watchlist_url(entry.watchlist_anchor)

    if error is not None or body is None:
        title = f"[watchlist-monitor] Fetch failed: {entry.id}"
        issue_body = (
            f"Automated fetch failed for a monitored watchlist source.\n\n"
            f"- **Watch entry:** {entry.watchlist_entry}\n"
            f"- **WATCHLIST.md:** {link}\n"
            f"- **URL:** {entry.url}\n"
            f"- **HTTP status:** {status if status is not None else 'n/a (no response)'}\n"
            f"- **Error:** {error}\n\n"
            f"This may be transient (site outage, rate limiting) or durable (the site now "
            f"blocks automated requests, as aph.gov.au was already observed doing as of "
            f"2026-07-20 -- see WATCHLIST.md entry 6 and monitoring/README.md). Either way, "
            f"a human should check the URL directly. No snapshot was updated for `{entry.id}` "
            f"this run.\n"
        )
        open_or_comment_issue(marker=f"Fetch failed: {entry.id}", title=title, body=issue_body)
        return

    text = normalize_html_to_text(body)

    if len(text) < MIN_PLAUSIBLE_TEXT_CHARS:
        title = f"[watchlist-monitor] Page-structure surprise: {entry.id}"
        issue_body = (
            f"Automated fetch for a monitored watchlist source returned suspiciously little "
            f"extractable text ({len(text)} characters), which usually means the page's "
            f"structure changed (e.g. moved to client-side rendering, added an interstitial/"
            f"consent wall, or returned an error page with HTTP 200).\n\n"
            f"- **Watch entry:** {entry.watchlist_entry}\n"
            f"- **WATCHLIST.md:** {link}\n"
            f"- **URL:** {entry.url}\n"
            f"- **HTTP status:** {status}\n\n"
            f"No snapshot was updated for `{entry.id}` this run so a real future change isn't "
            f"masked by this noise. A human should check the URL and, if the short extract is "
            f"actually correct (e.g. the page really is just short), update "
            f"`MIN_PLAUSIBLE_TEXT_CHARS` handling or the entry's notes in "
            f"monitoring/watchlist_urls.json.\n"
        )
        open_or_comment_issue(marker=f"Page-structure surprise: {entry.id}", title=title, body=issue_body)
        return

    if not snapshot_path.exists():
        snapshot_path.write_text(text, encoding="utf-8")
        print(f"Baseline snapshot written for {entry.id} ({len(text)} chars). No issue opened (first run).")
        return

    old_text = snapshot_path.read_text(encoding="utf-8")
    if old_text == text:
        print(f"No change for {entry.id}.")
        return

    diff_lines = list(
        difflib.unified_diff(
            old_text.splitlines(),
            text.splitlines(),
            fromfile=f"{entry.id} (previous snapshot)",
            tofile=f"{entry.id} (this run, {time.strftime('%Y-%m-%d')})",
            lineterm="",
        )
    )
    diff_text = "\n".join(diff_lines)
    truncated = False
    if len(diff_text) > 6000:
        diff_text = diff_text[:6000]
        truncated = True

    title = f"[watchlist-monitor] Change detected: {entry.id}"
    issue_body = (
        f"The monitored page for this watch entry has changed since the last recorded snapshot.\n\n"
        f"- **Watch entry:** {entry.watchlist_entry}\n"
        f"- **WATCHLIST.md:** {link}\n"
        f"- **URL:** {entry.url}\n"
        f"- **Notes:** {entry.notes}\n\n"
        f"### Diff summary (normalized text, HTML stripped)\n\n"
        f"```diff\n{diff_text}\n```\n"
        + ("\n_(diff truncated at 6000 characters)_\n" if truncated else "")
        + f"\nA human should review the source and update WATCHLIST.md's status/date if this "
        f"is a substantive change, not just boilerplate churn.\n"
    )
    open_or_comment_issue(marker=f"Change detected: {entry.id}", title=title, body=issue_body)
    snapshot_path.write_text(text, encoding="utf-8")
    print(f"Change detected and snapshot updated for {entry.id}.")


def main() -> int:
    SNAPSHOT_DIR.mkdir(parents=True, exist_ok=True)
    entries = load_config()
    ensure_label()
    for entry in entries:
        try:
            process_entry(entry)
        except Exception as exc:  # noqa: BLE001 - isolate failures per URL
            print(f"::error::Unexpected error processing {entry.id}: {exc}")
            title = f"[watchlist-monitor] Unexpected script error: {entry.id}"
            body = (
                f"The monitoring script raised an unexpected exception while processing this "
                f"entry. This is a bug or an unhandled edge case, not an expected fetch failure.\n\n"
                f"- **Watch entry:** {entry.watchlist_entry}\n"
                f"- **URL:** {entry.url}\n"
                f"- **Error:** `{type(exc).__name__}: {exc}`\n"
            )
            open_or_comment_issue(marker=f"Unexpected script error: {entry.id}", title=title, body=body)
    return 0


if __name__ == "__main__":
    sys.exit(main())
