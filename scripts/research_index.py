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
REQUIRE_KIND = True   # every claim carries `kind` since 2026-10-06
INNER_STATE = {"5.A2", "9.t9", "3.2", "3.3"}   # sections where bucket moves favour or foreclose
SYSTEM_CONDITIONS = {   # research/README.md, source field system_conditions (added 2026-09-26)
    "modality": {"text", "multimodal", "unstated"},
    "state": {"none", "in-context", "cross-session", "unstated"},
    "operation": {"per-call", "continuous", "unstated"},
    "world": {"none", "tools", "embodied", "unstated"},
    "access": {"api", "open-weights", "internal", "both", "unstated"},
}

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
        sc = s.get("system_conditions")
        if sc is not None:
            if not isinstance(sc, dict):
                errs.append("%s: system_conditions must be a flow map" % name)
            else:
                for k, allowed in SYSTEM_CONDITIONS.items():
                    if sc.get(k, "unstated") not in allowed:
                        errs.append("%s: system_conditions.%s %r" % (name, k, sc.get(k)))
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
        if "kind" in c and c.get("kind") not in KINDS:
            errs.append("%s: kind %r" % (name, c.get("kind")))
        if REQUIRE_KIND and c.get("kind") not in KINDS:
            errs.append("%s: kind missing" % name)
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
        # 2. single-lineage support in a dossier: persists until a replication is
        #    retrieved or the council has sat on the claim (not a one-time event).
        rv2 = c.get("review") or {}
        # A claim whose review.adjudicated carries a dated decision is off the
        # docket for triggers 2 to 5 (added 2026-10-05: until then nothing could
        # ever be crossed off). A later bucket move (T1) needs adjudicated reset
        # to none. A reader disagreement recorded after a decision is written
        # 'disagrees (open)' and fires T5 whatever adjudicated says (6 Oct 2026),
        # so the record of the earlier decision is kept; when it is decided the
        # marker becomes 'disagrees (decided YYYY-MM-DD)'.
        settled = str(rv2.get("adjudicated", "none")) not in ("", "none")
        if c["publisher_relation"] == "developer-of-studied-model" and c["replication"] == "none-retrieved" \
                and str(rv2.get("council", "none")) in ("", "none") and not settled:
            items.append("T2 single-lineage claim in dossier(s) %s, no replication retrieved, council not yet sat: %s"
                         % (", ".join(c["bears_on"]), cid))
        # 3. contradictions in the same bucket
        for other_id in c.get("contests", []):
            other = next((x for x in claims.values() if x.get("id") == other_id), None)
            if other and other.get("bucket") == c["bucket"] and not settled:
                items.append("T3 %s contests %s and both sit in bucket %r" % (cid, other_id, c["bucket"]))
        # 4. ambiguous evidence type
        if c["evidence_type"] == "ambiguous" and not settled:
            items.append("T4 evidence_type ambiguous (self-report boundary): %s" % cid)
        # 5. second reader disagreement, recorded in body or review as 'disagrees'
        rv = c.get("review") or {}
        if "disagrees (open)" in str(rv.get("second_reader", "")):
            items.append("T5 second reader disagrees, recorded after the last decision: %s" % cid)
        elif ("disagree" in str(rv.get("second_reader", "")).lower() or "SECOND READER DISAGREES" in c["_body"]) \
                and not settled:
            items.append("T5 second reader disagrees with extractor: %s" % cid)
    # 8. drift, per dossier
    today = date.today()
    for key, cl in group_by_dossier(claims).items():
        ds = state.get("dossiers", {}).get(key, {})
        total = len({c["id"] for c in cl})
        since = total - ds.get("count_at_last_council", 0)
        last = ds.get("last_council")
        age = (today - datetime.strptime(last, "%Y-%m-%d").date()).days if last else None
        if last is None and total >= 10:
            items.append("T8 dossier %s has %d claims and the council has never sat on it" % (key, total))
        elif last is not None and since >= 10:
            items.append("T8 dossier %s has %d new claims since the council sat on %s" % (key, since, last))
        elif age is not None and age >= 90:
            items.append("T8 dossier %s: %d days since the council last sat" % (key, age))
    return items


def record_council(claims, state, spec):
    """--record-council=YYYY-MM-DD:key,key  Record that the council sat on these
    dossiers on that date. The claim count is taken as of that date (claims whose
    `added` is on or before it), so later intakes show up as new since the sitting."""
    day, keys = spec.split(":", 1)
    datetime.strptime(day, "%Y-%m-%d")
    groups = group_by_dossier(claims)
    state.setdefault("dossiers", {})
    for key in [k.strip() for k in keys.split(",") if k.strip()]:
        ids = {c["id"] for c in groups.get(key, []) if str(c.get("added", "9999")) <= day}
        state["dossiers"][key] = {"last_council": day, "count_at_last_council": len(ids)}
        print("recorded council sitting %s on dossier %s (%d claims at that date)" % (day, key, len(ids)))


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
CANON = ("Framework (test 9): a model's report about its own states carries no weight as evidence of experience "
         "until the link between report and internal state has been measured externally for this kind of report and system")
STEER = ("Framework (test 9, steering): a coupling measured under steering shows that the channel can be steered "
         "and does not weight reports offered in ordinary operation")
KINDS = ("measurement", "interpretation", "limitation")


def split_exclusions(field_text):
    """Split a not_evidence_of field into (paper clauses, has canonical, has steering, other clauses)."""
    paper, other, canon, steer = [], [], False, False
    for cl in [x.strip() for x in str(field_text).split("; ") if x.strip()]:
        bare = cl.rstrip(".")
        if bare == CANON:
            canon = True
        elif bare == STEER:
            steer = True
        elif cl.startswith("Paper: "):
            paper.append(cl[len("Paper: "):])
        else:
            other.append(cl)
    return paper, canon, steer, other


def conditions_line(src):
    sc = (src or {}).get("system_conditions")
    if not isinstance(sc, dict):
        return "not recorded"
    return "input %s; state carried %s; run %s; acts on a world: %s; access %s" % (
        sc.get("modality", "unstated"), sc.get("state", "unstated"), sc.get("operation", "unstated"),
        sc.get("world", "unstated"), sc.get("access", "unstated"))


def write_dossiers(claims, src_by_slug, state):
    """Dossier layout adopted 6 October 2026 (council round 2, nine of nine on the kind label and on
    deriving markers from the claim file). The framework's rule on self-report is printed once at the
    top; an entry is marked [T9] or [T9-steering] only if its claim file carries that sentence."""
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
        ds = state.get("dossiers", {}).get(key, {})
        L = ["# Dossier: %s" % title, "",
             "*Compiled %s by `scripts/research_index.py` from %d claim(s). Do not edit; regenerate.*" % (today, len(uniq)),
             "", "Council last sat on this dossier: %s." % (ds.get("last_council") or "never"), "",
             "## How to read this", "",
             "Each entry is one sentence about what one paper found, with the paper's exact words beside it. "
             "The full record, including review history, is in the linked claim file.", "",
             "**Two errors, not one.** This library guards against dismissing the possibility of inner states "
             "in AI systems and against asserting them on evidence that cannot carry the weight. Nothing here "
             "settles whether anything is experienced.", "",
             "**Bucket** says how settled the sentence is. *Established*: measured by the paper and either "
             "replicated independently or uncontested in what has been retrieved. *Narrowing*: measured, but "
             "unreplicated, contested, or confined to a narrow setting the authors flag. *Open*: something the "
             "paper bears on and does not settle.", "",
             "**Kind** says what sort of sentence it is. *Measurement*: a measured result. *Interpretation*: the "
             "authors' reading or argument. *Limitation*: what the study cannot show. An established limitation "
             "means the limit is established; it is not a finding that a capability is present or absent.", "",
             # Explanation reworded 6 October 2026 on the council's advice (round 3, eight of eight):
             # an unmarked entry must not read as "no caveat applies".
             "**The framework's two rules on self-report, stated once.** A mark attaches by two facts: what was "
             "done to the model, and what was measured.", "",
             "**[T9]** marks an entry where nothing inside the model was altered and what was measured is what "
             "the model said about its own inner states. Its claim file carries this sentence:", "",
             "> " + CANON + ".", "",
             "The mark attaches whether the model affirmed something or denied it, and says nothing about "
             "whether what it said is true.", "",
             "**[T9-steering]** marks an entry where researchers altered something inside the model (by steering, "
             "injection, ablation, capping, zeroing, scaling, noise or replacement) and then measured what it "
             "said about itself. Its claim file carries this sentence:", "", "> " + STEER + ".", "",
             "This is a note on scope. It does not say the effect was found or how large it was, and the result "
             "stands under the intervention described.", "",
             "An entry never carries both marks. Both sentences are the framework's rules, not the papers' "
             "findings, and each mark is read from the claim file.", "",
             "**An unmarked entry** measures something other than a model's account of itself (a probe reading, "
             "a score, a harm rate, an internal projection), or records the authors' own opinion or caveat. No "
             "mark does not mean no caveat: the paper's own limits are listed under every entry. Nor does it "
             "make the entry a self-report, or evidence about experience.", "",
             "**The paper's own limits** under each entry are limits the paper states or its design entails.", ""]
        # counts table
        L += ["## At a glance", "", "| | measurement | interpretation | limitation | unlabelled |", "|---|---|---|---|---|"]
        for bucket in ("established", "narrowing", "open"):
            sub = [c for c in uniq if c["bucket"] == bucket]
            row = [str(sum(1 for c in sub if c.get("kind") == k)) for k in KINDS]
            row.append(str(sum(1 for c in sub if c.get("kind") not in KINDS)))
            L.append("| **%s** (%d) | %s |" % (bucket, len(sub), " | ".join(row)))
        L.append("")
        for bucket in ("established", "narrowing", "open"):
            sub = [c for c in uniq if c["bucket"] == bucket]
            if not sub:
                continue
            L += ["## %s (%d)" % (bucket.capitalize(), len(sub)), ""]
            order = {k: i for i, k in enumerate(KINDS)}
            for c in sorted(sub, key=lambda x: (order.get(x.get("kind"), 9), x["id"])):
                paper, canon, steer, other = split_exclusions(c["not_evidence_of"])
                tags = [c.get("kind") if c.get("kind") in KINDS else "kind not yet labelled", c["evidence_type"]]
                if canon:
                    tags.append("**[T9]**")
                if steer:
                    tags.append("**[T9-steering]**")
                L.append("### %s" % c["id"])
                L.append("")
                L.append("*%s*" % " · ".join(tags))
                L.append("")
                L.append("> %s" % c["statement"])
                L.append("")
                L.append("- **Paper's words** (%s): \"%s\"" % (c.get("locator", ""), c.get("quote", "")))
                models = c.get("models", [])
                L.append("- **Models:** %s" % (", ".join(models) if models else "none named (not a measurement on a model)"))
                L.append("- **System studied:** %s" % conditions_line(src_by_slug.get(c["source"])))
                if paper:
                    L.append("- **The paper's own limits:**")
                    for pcl in paper:
                        L.append("  - %s" % pcl)
                else:
                    L.append("- **The paper's own limits:** none recorded")
                for o in other:
                    L.append("- **Unlabelled exclusion (needs a label):** %s" % o)
                marks = []
                if c["publisher_relation"] == "developer-of-studied-model":
                    marks.append("published by the developer of the model studied")
                if c["publisher_relation"] == "developer-of-studied-model" and c["replication"] == "none-retrieved":
                    marks.append("no independent replication retrieved")
                if c["replication"].startswith("independent:"):
                    marks.append("independent replication on record")
                if "SHARED AUTHOR" in c["replication"]:
                    marks.append("one replication shares an author with this paper")
                if c["evidence_type"] == "self-report-testimony":
                    marks.append("testimony: weight zero as evidence of experience")
                if c["evidence_type"] == "ambiguous":
                    marks.append("evidence type deliberately undecided")
                if c["verification"] == "unverified":
                    marks.append("quote not yet verified")
                rv = c.get("review") or {}
                sr = str(rv.get("second_reader", "none"))
                if sr in ("", "none"):
                    marks.append("no second reader yet")
                if c.get("contested_by"):
                    marks.append("contested by %s" % ", ".join(c["contested_by"]))
                if c.get("contests"):
                    marks.append("contests %s" % ", ".join(c["contests"]))
                if marks:
                    L.append("- **Flags:** %s" % "; ".join(marks))
                L.append("- [claim file](../claims/%s.md)" % c["id"])
                L.append("")
        fn = os.path.join(DOS, "%s.md" % key.replace(".", "-"))
        open(fn, "w", encoding="utf-8", newline="\n").write("\n".join(L))
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
    for a in argv:
        if a.startswith("--record-council="):
            record_council(claims, state, a.split("=", 1)[1])
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
    # Also written to research/DOCKET.md so a council round can attach it.
    dk = ["# Docket", "",
          "*Generated %s by `scripts/research_index.py`. Council triggers that have fired and are not yet adjudicated (research/README.md, \"Convening rules\"). Do not edit; regenerate.*" % date.today().isoformat(),
          "", "%d item(s)." % len(items), ""]
    dk += ["- %s" % it for it in items] or ["- (none)"]
    open(os.path.join(RES, "DOCKET.md"), "w", encoding="utf-8", newline="\n").write("\n".join(dk) + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
