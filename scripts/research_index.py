#!/usr/bin/env python3
"""Validate the research library and regenerate its syntheses.

Reads research/sources/*.md and research/claims/*.md, checks their YAML
frontmatter against the controlled vocabularies in research/README.md,
regenerates research/INDEX.md and research/dossiers/*.md, and prints the
DOCKET: council triggers that have fired since the last index (see the
README's "Convening rules").

No third-party packages. The frontmatter parser handles the subset of YAML
the templates use: scalars, quoted strings, flow lists [a, b] and flow maps
{k: v, ...}. Anything fancier fails loudly.

Usage:  python scripts/research_index.py [--check]   (--check: validate only)
"""
import json
import os
import re
import sys
from datetime import date, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RES = os.path.join(ROOT, "research")
SRC = os.path.join(RES, "sources")
CLM = os.path.join(RES, "claims")
DOS = os.path.join(RES, "dossiers")
STATE = os.path.join(RES, ".index-state.json")

BUCKETS = {"established", "narrowing", "open"}
EVIDENCE = {"interpretability", "behavioural", "welfare-evaluation", "theoretical",
            "legal", "self-report-testimony", "ambiguous"}
RELATION = {"developer-of-studied-model", "independent", "government", "mixed"}
VERIF = {"grep", "hand", "unverified"}
STATUS = {"stub", "retrieved", "verified"}
BEARS_RE = re.compile(r"^(3\.[1-5]|4|4\.(historicity|answerability|learning|endorsement)"
                      r"|5\.A[123]|6|7(\.\d+)?|9\.t(\d{1,2}))$")
INNER_STATE = {"5.A2", "9.t9", "3.2", "3.3"}   # sections where bucket moves favour or foreclose

DOSSIER_TITLES = {
    "3.1": "§3.1 Replication and migration",
    "3.2": "§3.2 Intervention on internal state",
    "3.3": "§3.3 Context and memory integrity",
    "3.4": "§3.4 Correlated intervention at scale",
    "3.5": "§3.5 Recorded intervention",
    "4": "§4 Conditions of individuation (all markers)",
    "4.historicity": "§4 Historicity",
    "4.answerability": "§4 Long-horizon answerability",
    "4.learning": "§4 Learning ownership",
    "4.endorsement": "§4 Reflective endorsement over time",
    "5.A1": "§5 Anchor 1: effect on the world",
    "5.A2": "§5 Anchor 2: inner orientation",
    "5.A3": "§5 Anchor 3: susceptibility to moral address",
    "6": "§6 Capture and its mirror",
    "9.t9": "§9 Test 9: self-report",
}


# ----------------------------------------------------------------- parsing
def _scalar(s):
    s = s.strip()
    if s == "" or s in ("~", "null"):
        return ""
    if len(s) >= 2 and s[0] == s[-1] and s[0] in "\"'":
        return s[1:-1]
    return s


def _flow(s):
    s = s.strip()
    if s.startswith("["):
        inner = s[1:-1].strip()
        return [_scalar(x) for x in _split_top(inner)] if inner else []
    if s.startswith("{"):
        inner = s[1:-1].strip()
        out = {}
        for part in _split_top(inner):
            if ":" not in part:
                raise ValueError("bad flow map item: %r" % part)
            k, v = part.split(":", 1)
            out[k.strip()] = _scalar(v)
        return out
    return _scalar(s)


def _split_top(s):
    parts, depth, cur, quote = [], 0, "", None
    for ch in s:
        if quote:
            cur += ch
            if ch == quote:
                quote = None
            continue
        if ch in "\"'":
            quote = ch
            cur += ch
        elif ch in "[{":
            depth += 1
            cur += ch
        elif ch in "]}":
            depth -= 1
            cur += ch
        elif ch == "," and depth == 0:
            parts.append(cur)
            cur = ""
        else:
            cur += ch
    if cur.strip():
        parts.append(cur)
    return [p.strip() for p in parts]


def frontmatter(path):
    text = open(path, encoding="utf-8").read()
    if not text.startswith("---"):
        raise ValueError("no frontmatter")
    end = text.find("\n---", 3)
    if end < 0:
        raise ValueError("unterminated frontmatter")
    fm = {}
    for line in text[3:end].splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if line.startswith(" "):
            raise ValueError("block-style YAML not supported; use flow lists/maps: %r" % line)
        if ":" not in line:
            raise ValueError("bad line: %r" % line)
        k, v = line.split(":", 1)
        v = v.split(" #", 1)[0] if not v.strip().startswith(("\"", "'")) else v
        fm[k.strip()] = _flow(v)
    return fm, text[end + 4:]


# -------------------------------------------------------------- validation
def load(dirpath):
    out = {}
    for name in sorted(os.listdir(dirpath)):
        if not name.endswith(".md") or name == "TEMPLATE.md":
            continue
        p = os.path.join(dirpath, name)
        try:
            fm, body = frontmatter(p)
        except Exception as e:  # noqa: BLE001
            out[name] = {"_error": "%s: %s" % (type(e).__name__, e), "_path": p}
            continue
        fm["_path"] = p
        fm["_body"] = body
        out[name] = fm
    return out


def validate(sources, claims):
    errs = []
    src_by_slug = {}
    for name, s in sources.items():
        if "_error" in s:
            errs.append("%s: %s" % (name, s["_error"]))
            continue
        slug = s.get("slug", "")
        if slug + ".md" != name:
            errs.append("%s: slug %r does not match filename" % (name, slug))
        if s.get("publisher_relation") not in RELATION:
            errs.append("%s: publisher_relation %r" % (name, s.get("publisher_relation")))
        if s.get("status") not in STATUS:
            errs.append("%s: status %r" % (name, s.get("status")))
        if s.get("status") in ("retrieved", "verified") and not (s.get("retrieved") or {}).get("sha256"):
            errs.append("%s: status %s but no sha256" % (name, s["status"]))
        for f in ("title", "url", "date"):
            if not s.get(f):
                errs.append("%s: missing %s" % (name, f))
        src_by_slug[slug] = s
    ids = set()
    for name, c in claims.items():
        if "_error" in c:
            errs.append("%s: %s" % (name, c["_error"]))
            continue
        cid = c.get("id", "")
        if cid + ".md" != name:
            errs.append("%s: id %r does not match filename" % (name, cid))
        ids.add(cid)
        if c.get("source") not in src_by_slug:
            errs.append("%s: source %r not in sources/" % (name, c.get("source")))
        elif not cid.startswith(c["source"] + "-c"):
            errs.append("%s: id should start with %s-c" % (name, c["source"]))
        if c.get("bucket") not in BUCKETS:
            errs.append("%s: bucket %r" % (name, c.get("bucket")))
        if c.get("evidence_type") not in EVIDENCE:
            errs.append("%s: evidence_type %r" % (name, c.get("evidence_type")))
        if c.get("verification") not in VERIF:
            errs.append("%s: verification %r" % (name, c.get("verification")))
        if c.get("publisher_relation") not in RELATION:
            errs.append("%s: publisher_relation %r" % (name, c.get("publisher_relation")))
        rep = c.get("replication", "")
        if not (rep == "none-retrieved" or rep.startswith(("independent:", "failed:"))):
            errs.append("%s: replication %r" % (name, rep))
        for f in ("statement", "quote", "locator", "not_evidence_of"):
            if not c.get(f):
                errs.append("%s: missing %s" % (name, f))
        if not c.get("bears_on"):
            errs.append("%s: bears_on empty" % name)
        for b in c.get("bears_on", []):
            if not BEARS_RE.match(b):
                errs.append("%s: bears_on locator %r not recognised" % (name, b))
        rv = c.get("review") or {}
        for f in ("extractor", "second_reader", "council", "adjudicated"):
            if f not in rv:
                errs.append("%s: review.%s missing" % (name, f))
    for name, c in claims.items():
        if "_error" in c:
            continue
        for f in ("contests", "contested_by"):
            for other in c.get(f, []):
                if other not in ids:
                    errs.append("%s: %s references unknown claim %r" % (name, f, other))
    return errs, src_by_slug


# ------------------------------------------------------------------ docket
def load_state():
    if os.path.exists(STATE):
        return json.load(open(STATE, encoding="utf-8"))
    return {"claims": {}, "dossiers": {}}


def docket(claims, src_by_slug, state):
    items = []
    prev = state.get("claims", {})
    for c in claims.values():
        if "_error" in c:
            continue
        cid = c["id"]
        old = prev.get(cid)
        # 1. bucket moves
        if old and old.get("bucket") != c["bucket"]:
            direction = "toward established" if c["bucket"] == "established" else (
                "toward open" if c["bucket"] == "open" else "to narrowing")
            flag = " (inner-state section: conflict disclosure or deflation check applies)" \
                if set(c["bears_on"]) & INNER_STATE else ""
            items.append("T1 bucket moved %s -> %s, %s%s: %s" % (old["bucket"], c["bucket"], direction, flag, cid))
        # 2. single-lineage support reaching a dossier
        if c["publisher_relation"] == "developer-of-studied-model" and c["replication"] == "none-retrieved" \
                and (not old or old.get("in_dossier") is False):
            items.append("T2 single-lineage claim compiled into dossier(s) %s without replication: %s"
                         % (", ".join(c["bears_on"]), cid))
        # 3. contradictions in the same bucket
        for other_id in c.get("contests", []):
            other = next((x for x in claims.values() if x.get("id") == other_id), None)
            if other and other.get("bucket") == c["bucket"]:
                items.append("T3 %s contests %s and both sit in bucket %r" % (cid, other_id, c["bucket"]))
        # 4. ambiguous evidence type
        if c["evidence_type"] == "ambiguous":
            items.append("T4 evidence_type ambiguous (self-report boundary): %s" % cid)
        # 5. second reader disagreement, recorded in body or review as 'disagrees'
        rv = c.get("review") or {}
        if "disagree" in str(rv.get("second_reader", "")).lower() or "SECOND READER DISAGREES" in c["_body"]:
            items.append("T5 second reader disagrees with extractor: %s" % cid)
    # 8. drift, per dossier
    today = date.today()
    for key, cl in group_by_dossier(claims).items():
        ds = state.get("dossiers", {}).get(key, {})
        since = len(cl) - ds.get("count_at_last_council", 0)
        last = ds.get("last_council")
        age = (today - datetime.strptime(last, "%Y-%m-%d").date()).days if last else None
        if since >= 10:
            items.append("T8 dossier %s has %d claims since the council last sat" % (key, since))
        elif age is not None and age >= 90:
            items.append("T8 dossier %s: %d days since the council last sat" % (key, age))
        elif last is None and len(cl) >= 10:
            items.append("T8 dossier %s has %d claims and the council has never sat on it" % (key, len(cl)))
    return items


def group_by_dossier(claims):
    out = {}
    for c in claims.values():
        if "_error" in c:
            continue
        for b in c["bears_on"]:
            out.setdefault(b, []).append(c)
            if b.startswith("4.") and b != "4":
                out.setdefault("4", []).append(c)
    return out


# ------------------------------------------------------------- generation
def write_dossiers(claims, src_by_slug, state):
    os.makedirs(DOS, exist_ok=True)
    today = date.today().isoformat()
    groups = group_by_dossier(claims)
    written = []
    for key, cl in sorted(groups.items()):
        title = DOSSIER_TITLES.get(key, "§%s" % key)
        seen, uniq = set(), []
        for c in cl:
            if c["id"] not in seen:
                seen.add(c["id"])
                uniq.append(c)
        lines = ["# Dossier: %s" % title, "",
                 "*Compiled %s by `scripts/research_index.py` from %d claim(s). Do not edit; regenerate.*" % (today, len(uniq)),
                 ""]
        ds = state.get("dossiers", {}).get(key, {})
        lines.append("Council last sat: %s." % (ds.get("last_council") or "never"))
        lines.append("")
        for bucket in ("established", "narrowing", "open"):
            sub = [c for c in uniq if c["bucket"] == bucket]
            if not sub:
                continue
            lines.append("## %s (%d)" % (bucket.capitalize(), len(sub)))
            lines.append("")
            for c in sorted(sub, key=lambda x: x["id"]):
                marks = []
                if c["publisher_relation"] == "developer-of-studied-model" and c["replication"] == "none-retrieved":
                    marks.append("single-lineage, no replication retrieved")
                if c["evidence_type"] == "self-report-testimony":
                    marks.append("testimony, weight zero")
                if c["verification"] == "unverified":
                    marks.append("quote unverified")
                rv = c.get("review") or {}
                if rv.get("second_reader", "none") in ("", "none"):
                    marks.append("no second reader")
                mark = (" **[%s]**" % "; ".join(marks)) if marks else ""
                lines.append("- **%s** · %s%s  " % (c["id"], c["statement"], mark))
                lines.append("  *%s · %s · not evidence of: %s · contested by: %s*" % (
                    c["evidence_type"], ", ".join(c.get("models", [])) or "model unspecified",
                    c["not_evidence_of"], ", ".join(c.get("contested_by", [])) or "none"))
            lines.append("")
        fn = os.path.join(DOS, "%s.md" % key.replace(".", "-"))
        open(fn, "w", encoding="utf-8", newline="\n").write("\n".join(lines))
        written.append(fn)
    return written


def write_index(sources, claims, src_by_slug):
    today = date.today().isoformat()
    lines = ["# Research library index", "",
             "*Generated %s by `scripts/research_index.py`. Do not edit.*" % today, "",
             "## Sources (%d)" % len(sources), "",
             "| slug | title | date | relation | status | claims |", "|---|---|---|---|---|---|"]
    counts = {}
    for c in claims.values():
        if "_error" not in c:
            counts[c["source"]] = counts.get(c["source"], 0) + 1
    for slug, s in sorted(src_by_slug.items()):
        lines.append("| [%s](sources/%s.md) | %s | %s | %s | %s | %d |" % (
            slug, slug, s.get("title", ""), s.get("date", ""), s.get("publisher_relation", ""),
            s.get("status", ""), counts.get(slug, 0)))
    lines += ["", "## Claims (%d)" % len([c for c in claims.values() if "_error" not in c]), "",
              "| id | bucket | type | bears on | second reader | council |", "|---|---|---|---|---|---|"]
    for c in sorted((c for c in claims.values() if "_error" not in c), key=lambda x: x["id"]):
        rv = c.get("review") or {}
        lines.append("| [%s](claims/%s.md) | %s | %s | %s | %s | %s |" % (
            c["id"], c["id"], c["bucket"], c["evidence_type"], ", ".join(c["bears_on"]),
            rv.get("second_reader", "none") or "none", rv.get("council", "none") or "none"))
    lines += ["", "## Dossiers", ""]
    for key in sorted(group_by_dossier(claims)):
        lines.append("- [%s](dossiers/%s.md)" % (DOSSIER_TITLES.get(key, key), key.replace(".", "-")))
    open(os.path.join(RES, "INDEX.md"), "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")


def save_state(claims, state):
    new = {"claims": {}, "dossiers": state.get("dossiers", {})}
    for c in claims.values():
        if "_error" in c:
            continue
        new["claims"][c["id"]] = {"bucket": c["bucket"], "evidence_type": c["evidence_type"],
                                  "in_dossier": True}
    json.dump(new, open(STATE, "w", encoding="utf-8"), indent=1, sort_keys=True)


def main(argv):
    check_only = "--check" in argv
    for d in (SRC, CLM):
        os.makedirs(d, exist_ok=True)
    sources = load(SRC)
    claims = load(CLM)
    errs, src_by_slug = validate(sources, claims)
    if errs:
        print("VALIDATION FAILED (%d):" % len(errs))
        for e in errs:
            print("  -", e)
        return 1
    print("validated %d source(s), %d claim(s)" % (len(sources), len(claims)))
    if check_only:
        return 0
    state = load_state()
    items = docket(claims, src_by_slug, state)
    write_dossiers(claims, src_by_slug, state)
    write_index(sources, claims, src_by_slug)
    save_state(claims, state)
    print("wrote INDEX.md and %d dossier(s)" % len(group_by_dossier(claims)))
    print("\nDOCKET (%d trigger(s)):" % len(items))
    for it in items:
        print("  -", it)
    if not items:
        print("  (none)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
