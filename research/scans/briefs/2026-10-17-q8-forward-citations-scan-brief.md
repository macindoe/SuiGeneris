# Scan brief: forward citations on five dated anchors from the Q8 scan

**Written 17 October 2026 by the coordinating session (Claude Fable 5.1) on Ben's question of the same day: the Q8 scan's anchors for the brain and fly literatures are 2007 to 2012; has the field moved, and are they still the right anchors?** Run before the Q8 intake so the intake takes in the right papers.

**Conflict disclosure (AGENTS.md rule 3), to be carried into the scan file:** the question is whether current artificial systems lack a property the brain has, and the scanning model is such a system. The scan reads the newer literature in both directions: work that strengthens the intrinsic-activity reading and work that weakens it, and for the fly, work that reduces "spontaneous" to noise as readily as work that shows structure in it.

---

## The prompt

You are updating a literature scan for a research library attached to a legal framework. Read `research/README.md` (a scan is a pre-intake docket, filed verbatim, never cited), then the Q8 scan `research/scans/2026-10-15-q8-endogeneity.md` (its "Short answer", its headings 1, 2, 3 and 5, and its Recommendation), and Q8 in `research/OPEN-QUESTIONS.md`.

**Five anchors.** For each, find the work that cites it from 2020 onward and answer: has the reading changed; what is the best current anchor; and recommend one of **keep**, **add beside** (name the paper) or **replace** (name the paper).

1. **Raichle 2010**, "Two views of brain function", *Trends Cogn Sci* 14(4):180–190, doi 10.1016/j.tics.2010.01.008, PMID 20206576. The intrinsic-activity view. Has it become consensus, and in what framing (predictive processing, energy budget, large-scale dynamics)? Is there a review since 2020 that a careful reviewer would cite instead?
2. **Morcom and Fletcher 2007**, "Does the brain have a baseline? Why we should be resisting a rest", *NeuroImage* 37(4):1073–1082, PMID 17052921. The counterweight. Was the objection to rest as a privileged baseline absorbed, answered or ignored? What is the live counterweight now, if any?
3. **Schurger, Sitt and Dehaene 2012**, the accumulator model, *PNAS* 109(42):E2904–E2913, PMID 22869750. The noise-timing reading of self-initiated movement. The Q8 scan already holds Schurger et al. 2021 (*Trends Cogn Sci*). Beyond it: arbitrary against deliberate decisions, the "point of no return", direct tests and critics of the accumulator reading, and anything applying the paradigm outside humans or to artificial agents.
4. **Sussillo and Abbott 2009**, "Generating coherent patterns of activity from chaotic neural networks", *Neuron* 63(4):544–557. Intrinsic chaotic activity in a random recurrent network. Has later work on intrinsic dynamics in trained or biological recurrent networks changed what this is taken to show? Is there a better current anchor for "an artificial system whose state evolves with no input"?
5. **Maye, Hsieh, Sugihara and Brembs 2007**, "Order in spontaneous behavior", *PLoS ONE* 2(5):e443. Spontaneous turning in tethered flies is not random. What has the same lab and the field done since, especially with whole-brain imaging; has anyone separated intrinsic from stochastic variability with better instruments; and has the noise reading (London et al. 2010, in the Q8 scan) been reconciled with it?

**Method.** Use the open citation tools from this machine: OpenAlex (`https://api.openalex.org/works?filter=cites:<openalex id>&from_publication_date=2020-01-01&sort=cited_by_count:desc&per-page=50`, with abstracts from the inverted index; find each anchor's OpenAlex id by DOI or title search), PubMed's cited-in link (`elink` with `linkname=pubmed_pubmed_citedin`), and for full texts PMC (`efetch db=pmc`), arXiv HTML and bioRxiv where open. Download with `curl` into a fresh empty directory; strip with a uniquely named script kept in a separate directory and run with `python -I`; search the stripped text by hand. No summarising fetch tool for any quotation. For each anchor, read at least the ten most-cited citing works' abstracts and the full text of the two or three you rely on. Also run a few plain web searches per anchor for reviews that may not cite the anchor directly. Be a polite fetcher: at most one request per second per host; OpenAlex asks for a `mailto` parameter, pass `mailto=anonymous@example.org`.

**Record for each citing paper you rely on:** authors, year, venue, DOI or id, URL, retrievability, organisms or systems, what it bears on (which anchor; which North Star section), the finding in the authors' words, the limits the authors state, the publisher relation (say when inferred), a verification line (abstract read; full text read, searched: sections). Note discrepancies between search results and fetched pages. Keep "Corrections and cautions", "Gaps", "Not verified" and "Recommendation" sections. The Recommendation gives, per anchor, keep / add beside / replace with the paper named, and a one-paragraph statement of whether the Q8 scan's "Short answer" for that heading still stands. Record every search and API query.

**Output.** One markdown file, filed verbatim as `research/scans/2026-MM-DD-q8-forward-citations.md`, with the standard header ("Status: scan, not intake", the question in Ben's words: "they're all a little dated — should we run a scan for papers that cite them? Check if our understanding of the cutting edge has changed?", your method sentence, the conflict disclosure above). Do not propose edits to the North Star. Do not use the word "experience" for anything a paper measures unless the paper does; where it does, quote it.

## Attachments

- `research/README.md`
- `research/scans/2026-10-15-q8-endogeneity.md`
- `research/OPEN-QUESTIONS.md` (Q8)
- `AGENTS.md`
