# Scan: forward citations on five dated Q8 anchors (Raichle 2010, Morcom and Fletcher 2007, Schurger 2012, Sussillo and Abbott 2009, Maye 2007)

**Status: scan, not intake.** Candidate papers found by a Claude Opus 5.5 subagent (coordinated by Claude Fable 5.1) on 17 October 2026, briefed with `scans/briefs/2026-10-17-q8-forward-citations-scan-brief.md`, `research/README.md`, the Q8 scan `scans/2026-10-15-q8-endogeneity.md` (Short answer, headings 1, 2, 3 and 5, Recommendation), Q8 in `research/OPEN-QUESTIONS.md`, and `AGENTS.md`. Nothing here has been stubbed, hashed, extracted or second-read. Use this file to choose what enters `sources/`; do not cite it.

**Question (Ben, 17 Oct 2026):** "they're all a little dated — should we run a scan for papers that cite them? Check if our understanding of the cutting edge has changed?"

**Method.** For each anchor the OpenAlex id was found by DOI, and the works citing it from 1 January 2020 were listed from OpenAlex sorted by citation count (50 per anchor, abstracts rebuilt from the inverted index). PubMed's cited-in links (`elink`, `pubmed_pubmed_citedin`) were pulled as a cross-check. Abstracts missing from OpenAlex came from PubMed `efetch`. Full texts came from PMC (`efetch db=pmc`) and arXiv (abs pages, and one PDF through `pdftotext`). Plain web searches looked for reviews and critics that do not cite the anchors. Every page was downloaded with `curl` into a fresh scratchpad directory, stripped by a local script kept in a separate directory and run with `python -I`, and searched by hand. No summarising fetch tool stands between any paper and any quotation. Web-search summaries were used only to find papers and are never quoted. The three paywalled anchors were read from the PDFs Ben supplied in `research/texts/` (text extracted with `pdftotext`; the folders were not modified). The texts sat in the session scratchpad and were not kept. Treat every quotation as unverified until the paper is taken in and the quote checked against a held text. Publisher relation is inferred from printed affiliations, and each entry says so.

**Conflict disclosure (AGENTS.md rule 3; carried from the brief).** The question is whether current artificial systems lack a property the brain has, and the scanning model is such a system. The scan reads the newer literature in both directions: work that strengthens the intrinsic-activity reading and work that weakens it, and for the fly, work that reduces "spontaneous" to noise as readily as work that shows structure in it. The subagent adds (rule 4): it is a per-call model, and its training leans toward the deflationary reading ("brains initiate, models do not"). Two findings below cut against the simple form of that reading, in opposite ways, and both are reported at full strength. First, the human self-initiation paradigm runs on a drive that comes from the task instruction (F3.1), which narrows the human/model contrast. Second, much "spontaneous" brain activity tracks the body's own ongoing movement (F1.3, F5.1), which makes "intrinsic" less clean in biology than the Q8 short answer implies.

---

## Corrections and cautions found during the scan (17 Oct 2026)

- **The Q8 scan's unverified energy figure can now be checked against a held text.** The Q8 scan (C1.2, Gaps) said the commonly cited percentages "were not found in any fetched text". Raichle 2010, read from the PDF Ben supplied: the brain "represents about 2% of the total body weight yet it accounts for 20% of all the energy consumed", and "the additional energy consumption associated with changes in brain activity is remarkably small, often less than 5%". Pezzulo, Zorzi and Corbetta 2021 (F1.1) give the same 20% and 2%. Caution in the other direction: Morcom and Fletcher 2007 (also now read in full) dispute what these numbers show: "We also find no specific link between the brain's energy consumption and the notion of rest as a default mode." The figures are established. What they show about intrinsic function is contested.
- **The Q8 scan's reading of Schurger 2012 needs a qualification, and the qualification comes from inside the model.** The Q8 scan's short answer says the accumulator account "makes spontaneous fluctuation, possibly noise, the proximate timer of self-initiated movement". Its C2.2 note reframes the human/model contrast as "a noise-driven accumulator that never stops running versus none running". Bogler, Grujičić and Haynes 2023 (F3.1, full text read) rerun the published model. They find that its constant "imperative" term, not the noise, supplies most of the drive to threshold: "the imperative dominates the net input. It has a mean accumulated input of 0.7 ... In contrast, the net contribution of the noise is on average 0 across all trials." Schurger 2012 describes the paradigm as one with "no specific temporal cue, but only a general imperative to produce a movement" (read in Ben's PDF). Within the model, noise still explains the trial-to-trial timing. The drive comes from the task. So in this paradigm the human is an instructed system whose timing is set internally, not an uninstructed system that starts itself. This narrows the contrast Q8(2) draws, in the direction against the subagent's trained lean.
- **The noise reading covers arbitrary decisions only.** Maoz et al. 2019 (F3.4, abstract read; it cites the anchor; published before 2020) found readiness potentials "for arbitrary decisions", but they "were strikingly absent for deliberate ones". The Q8 scan does not mention this limit.
- **OpenAlex citation lists contain citing works that are wrong.** Among the "citing" works OpenAlex lists for Raichle 2010 are chapters of *The Oxford Handbook of Negation*. For Maye et al. 2007 the top-cited "citing" works include papers on osteoblast Runx2, shark extinction risk, T-cell therapy and protein evolution models. These are almost certainly reference-matching errors, so the OpenAlex counts below overstate the real citing literature. Coverage also differs by tool: since 2020 OpenAlex lists 76 works citing Morcom and Fletcher 2007, while PubMed's cited-in link returns 10 in all years, 1 of them from 2020 onward.
- **A DOI recalled from training was wrong.** The subagent guessed a DOI for Steymans et al. 2021 (10.1371/journal.pone.0254138). It belongs to an unrelated mitochondrial paper (PMC8315533), which was downloaded, recognised and discarded. PubMed gives 10.1371/journal.pone.0256560. Three identifiers recalled from training were confirmed by fetching the records: PMID 26668390 (Schultze-Kraft et al. 2016), and the DOIs for Aimon et al. 2023 and Stringer et al. 2019.
- **Search-summary errors, corrected against fetched records.** One web-search summary dated the "point of no return" paper to 2015. PubMed gives *PNAS* 2016 Jan 26;113(4):1080–5 (epub 14 Dec 2015). Another listed the 2025 *Neuron* review as "Dimakou, Zangrossi & Corbetta". PubMed lists four authors, with Pezzulo second.
- **Date fields differ between tools.** OpenAlex dates Morcom and Fletcher to 2006 (online October 2006). The PDF header and PubMed give *NeuroImage* 37 (2007) 1073–1082. The anchor's DOI, which the brief does not give, is 10.1016/j.neuroimage.2006.09.013 (from the PDF). OpenAlex dates Brembs's BBRC review to 2020 (epub). PubMed gives 2021;564:55–69.
- **An editorial link between two anchors.** The Schurger 2012 PDF prints "Edited by Marcus E. Raichle". This is recorded as a fact, and nothing more is inferred from it.
- **The word "experience".** Several fetched abstracts use it of humans, and it is quoted only, never used in this file's own voice: Li et al. 2022, "Ongoing experiences in the resting state vary in unobserved and uncontrolled ways"; Siegel et al. 2024, "the subjective psychedelic experience"; Mitelut et al. 2022, volition as "the basis of both human subjective experience and natural behavior"; Windt 2020 and Fernandino and Binder 2024 use it in their titles or abstracts (also-read lists). No paper here measures anything in an artificial system that it calls experience.
- **Test 9.** No AI self-report appears in this scan. Li et al. 2022 (think-aloud fMRI) is human self-report and is labelled as such where it appears.

---

## Subagent report

Scan date: 17 October 2026. Counts: 5 OpenAlex anchor lookups; 5 OpenAlex citing-work listings (50 records each, 250 in total); 11 OpenAlex single-work lookups for open-access locations; 5 PubMed `elink` cited-in lookups (all years: Raichle 422, Morcom 10, Schurger 155, Sussillo 393, Maye 70); 2 `esummary` batches; 5 `esearch` lookups; about 9 PubMed `efetch` abstract batches; 3 PMC ID-converter calls; 16 PMC full texts fetched (one the wrong paper, discarded); 3 arXiv abs pages and 1 arXiv PDF; 13 web searches.

Citing-work abstracts read: 58 (Raichle 12, Morcom 11, Schurger 14, Sussillo 11, Maye 10), plus non-citing works found by search. Full texts read and searched: 13 (Pezzulo 2021, Stringer 2019, Finn 2021, Bogler 2023, Gavenas 2025, Mitelut 2022, Gavenas 2024 in part, Vyas 2020, Sauerbrei 2020, Krishnamurthy 2022, Aimon 2023, Ahamed 2019 preprint, Maesani 2015), plus the three anchors from Ben's PDFs. Polite fetching: about 1.2 s between NCBI requests, 1 s between OpenAlex requests, 3 s between arXiv requests.

Verification legend, as in the Q8 scan: **abstract read** = abstract downloaded and read (from the OpenAlex inverted index, PubMed `efetch` or an arXiv abs page, as named). **Full text read (searched: ...)** = text downloaded and stripped, and the quoted passages found by search and read in context; sections not named were not read. **Cites anchor** records whether the work appears in the OpenAlex or PubMed citing list, or, for works found by search, whether the anchor's title appears in its reference list.

---

## Anchor 1. Raichle 2010, "Two views of brain function"

Read in full from Ben's PDF. The anchor's thesis, verbatim: brain functions "are mainly intrinsic, involving information processing for interpreting, responding to and predicting environmental demands", "a position that accords well with the allocation of the brain's energy resources". OpenAlex: 1,110 citing works in all years, 430 from 2020 (some wrong, see cautions).

### F1.1 The secret life of predictive brains: what's spontaneous activity for? — **recommended to add beside the anchor**
- Giovanni Pezzulo, Marco Zorzi, Maurizio Corbetta. *Trends Cogn Sci* 25(9):730–743, September 2021. doi 10.1016/j.tics.2021.05.007. PMID 34144895; PMC8363551. https://pmc.ncbi.nlm.nih.gov/articles/PMC8363551/
- Retrievability: open (PMC author manuscript, 80 KB stripped).
- Systems: review across species; humans and mice in the figures.
- Bears on: anchor 1; Q8 heading 1; North Star §4 (candidate axis), §7.5.
- Cites anchor: no (title not in the reference list; it cites Raichle and Mintun 2006 and Raichle 2011). Found by web search.
- Findings, authors' words: "Brains are constantly active, even when they receive no sensory stimuli or are not task-engaged"; "The functional significance of spontaneous brain activity (also called intrinsic or endogenous) is largely unknown"; "When the brain is at rest and stimuli are weak or absent, top-down dynamics optimize the generative models for future interactions"; "Even at rest, brains are proactive and predictive." On energy: "the brain consumes about 20% of the body energy ... vis-à-vis only 2% of the body weight"; "If most of the energy budget goes to resting potentials and infra-slow signaling, this activity must play a fundamental, yet unknown, role in function."
- Rival explanations the authors name: correlated spontaneous patterns may "represent emergent properties of anatomical circuitries driven by noise", or "homeostatic mechanisms related to the history of task activation".
- Limits stated: the framework is a proposal ("We suggest"); "fundamental, yet unknown, role"; an Outstanding Questions box.
- Publisher relation: independent academic (inferred: CNR Rome, Padova).
- Why add beside: it restates Raichle's thesis in predictive-processing terms, it is open, and it says plainly what Raichle 2010 does not: that intrinsic activity is known to exist and its function is not known. It also names noise as a live rival explanation, which keeps the two-error discipline in the anchor pair.
- Verification: full text read (searched: introduction, the four lines of evidence, "Generative models can be optimized even without novel data", Outstanding Questions, the rival-explanations paragraph).

### F1.2 The predictive nature of spontaneous brain activity across scales and species
- Anastasia Dimakou, Giovanni Pezzulo, Andrea Zangrossi, Maurizio Corbetta. *Neuron* 113(9):1310–1332, 7 May 2025. doi 10.1016/j.neuron.2025.02.009. PMID 40101720.
- Retrievability: OpenAlex says hybrid open access, but the cell.com and doi.org pages could not be fetched from this machine (see URLs). Abstract only.
- Systems: review, *C. elegans* to humans.
- Bears on: anchor 1; Q8 heading 1.
- Cites anchor: yes (OpenAlex; it also cites Morcom and Fletcher).
- Finding, authors' words: "the brain's spontaneous activity-ongoing internal processes independent of external stimuli. Neuroimaging and computational studies support that this activity is integral to maintaining and refining mental models"; the review highlights "the similarity between spontaneous and task-related activity, the encoding of behavioral and interoceptive priors, and the high metabolic cost of this activity, underscoring prediction as a fundamental function of brains across species."
- Limits stated: none in the abstract.
- Publisher relation: independent academic (inferred).
- Note: the later, cross-species version of F1.1 by the same group. Prefer it to F1.1 once a text is held.
- Verification: abstract read (PubMed).

### F1.3 Spontaneous behaviors drive multidimensional, brainwide activity — **the weakening direction**
- Carsen Stringer, Marius Pachitariu, Nicholas Steinmetz, Charu Bai Reddy, Matteo Carandini, Kenneth D. Harris. *Science* 364(6437):255, 19 April 2019. doi 10.1126/science.aav7893. PMID 31000656; PMC6525101.
- Retrievability: open (PMC author manuscript, 39 KB stripped). Published before 2020 and found by web search. Included because no post-2020 work found makes the same point as directly.
- Organisms: mice (two-photon imaging of about 10,000 neurons in visual cortex; eight Neuropixels probes across the brain).
- Bears on: anchors 1 and 5; Q8 heading 1 (what "spontaneous" means).
- Cites anchor: no (title not in the reference list).
- Findings, authors' words: "Cortical variability and spontaneous activity have been variously proposed to represent random noise, recall of prior experience, or encoding of ongoing behavioral and cognitive variables"; "spontaneous activity reliably encoded a high-dimensional latent state, which was partially related to the mouse's ongoing behavior and was represented not just in visual cortex but across the forebrain"; "16 dimensions of facial motor activity can predict 31% of the reliable spontaneous variance. The remaining dimensions and variance might in part reflect motor activity not visible on the face or only decodable by more advanced methods ... or they might reflect internal cognitive variables such as motivational drives."
- Limits stated: the remainder is unexplained, as quoted.
- Publisher relation: independent academic (inferred: UCL, Janelia).
- Note for Q8: "spontaneous" here means without sensory stimulation, not without input of any kind. A third of the reliable activity tracks the animal's own ongoing movement, so part of what counts as intrinsic is the body feeding back to the brain. That weakens "the brain runs without input" as stated. It does not support "it is noise": the authors reject that reading ("Despite its noisy appearance, spontaneous population activity reliably encoded a high-dimensional latent signal").
- Verification: full text read (searched: abstract, "Spontaneous cortical activity reliably encodes a high-dimensional latent signal", the facial-motion section, Discussion).

### F1.4 Ongoing brain activity and its role in cognition: dual versus baseline models
- Georg Northoff, Deniz Vatansever, Andrea Scalabrini, Emmanuel A. Stamatakis. *The Neuroscientist*, 2022 (online). doi 10.1177/10738584221081752. PMID 35611670.
- Retrievability: green open access at the Cambridge repository (not fetched). Abstract only.
- Bears on: anchors 1 and 2 (it argues the opposite of Morcom and Fletcher).
- Cites anchor: yes, both Raichle 2010 and Morcom and Fletcher 2007 (OpenAlex).
- Finding, authors' words: "we propose that ongoing brain activity serves as a neuronal baseline; this builds upon Raichle's original search for the default mode of brain function"; "Akin to an internal biological clock for the rest of the organism, the ongoing brain activity may serve as an internal point of reference"; "recent empirical evidence supports a baseline model over the dual model".
- Publisher relation: independent academic (inferred).
- Note: this is the live defence of a baseline, the thing Morcom and Fletcher attacked. Its "internal biological clock" wording is the authors' analogy, not a timing measurement. It touches Ben's heartbeat question only as a metaphor.
- Verification: abstract read (OpenAlex).

### F1.5 The metabolic costs of cognition
- Sharna D. Jamadar, Anna Behler, Hamish Deery, Michael Breakspear. *Trends Cogn Sci* 29(6):541–555, June 2025. doi 10.1016/j.tics.2024.11.010. PMID 39809687.
- Retrievability: closed (OpenAlex). Abstract only.
- Bears on: anchor 1 (the energy framing).
- Cites anchor: yes (OpenAlex).
- Finding, authors' words: "Cognition and behavior are emergent properties of brain systems that seek to maximize complex and adaptive behaviors while minimizing energy utilization"; "We review how this balance manifests in both homeostatic processes and task-associated cognition."
- Publisher relation: independent academic (inferred: Monash, Newcastle).
- Note: the current energy-budget review. Whether it repeats or revises the "often less than 5%" figure was not checked.
- Verification: abstract read (PubMed).

### F1.6 May the 4C's be with you: an overview of complexity-inspired frameworks for analysing resting-state neuroimaging data
- Fran Hancock, Fernando E. Rosas, Pedro A. M. Mediano, Andrea I. Luppi and others. *J R Soc Interface*, 2022. doi 10.1098/rsif.2022.0214.
- Bears on: anchor 1 (the large-scale dynamics framing).
- Cites anchor: yes (OpenAlex).
- Finding, authors' words: the review covers "connectivity, computation, criticality and coherence-the 4C's" and outlines "a potential role for metastability as a common denominator"; "complexity science offers a principled and integrated approach to describe, and potentially understand, macroscale spontaneous brain functioning."
- Verification: abstract read (OpenAlex).

**Also read (abstract, from the OpenAlex citing list; not recommended):**
- Siegel et al. 2024, *Nature*: psilocybin desynchronises functional connectivity, most strongly in the default mode network.
- Theriault et al. 2023, *Neurosci Biobehav Rev*: proposes that BOLD increases "approximate prediction error metabolism".
- Deco et al. 2022, *Netw Neurosci*: nonreversibility ("arrow of time") of brain signals, with the default mode network orchestrating the hierarchy.
- Camacho et al. 2020, *NeuroImage*: "the child brain does not rest in a manner consistent with the adult brain".
- Northoff, Wainio-Theberge and Evers 2020, *Phys Life Rev*.
- Faria-Pereira and Morais 2022, *Int J Mol Sci*: synaptic energy use.
- Wang et al. 2023, *Artif Intell Rev*: a "neural energy" theory; not relevant.

**Has the reading changed?** The existence of intrinsic activity is now treated as settled, by its critics too. Morcom and Fletcher 2007: "we do not dispute the active nature of the 'resting' state". Finn 2021 (F2.1): "most researchers now recognize" rest as "a highly active state in its own right rather than a passive baseline". The dominant framing since 2020 is predictive processing (F1.1, F1.2), with energy (F1.5) and large-scale dynamics (F1.4, F1.6) beside it. Function is still open (F1.1: "largely unknown"). The new complication is F1.3: in awake animals, "spontaneous" activity partly encodes the body's own movement.

---

## Anchor 2. Morcom and Fletcher 2007, "Does the brain have a baseline? Why we should be resisting a rest"

Read in full from Ben's PDF. Their claim, verbatim: "observations made under resting conditions have no privileged status as a fundamental metric of brain functioning". Their concession: "we do not dispute the active nature of the 'resting' state, nor dismiss all its potential applications, but we do challenge its claim to a special status".

### F2.1 Is it time to put rest to rest? — **recommended to add beside the anchor**
- Emily S. Finn. *Trends Cogn Sci* 25(12):1021–1032, December 2021. doi 10.1016/j.tics.2021.09.005. PMID 34625348; PMC8585722.
- Retrievability: open (PMC author manuscript, 70 KB stripped).
- Systems: humans (fMRI; review and opinion).
- Bears on: anchor 2; Q8 heading 1.
- Cites anchor: yes (reference 9; OpenAlex's second most-cited citing work since 2020).
- Findings, author's words: "Our foray into rest was fruitful from both a scientific and methodological perspective, but at this point, how much more can we learn from rest on its own?"; "Though it took some time for 'rest' to be widely accepted as a highly active state in its own right rather than a passive baseline, most researchers now recognize that resting-state signals reflect a mix of intrinsic functional organization and the mentation people do when left to their own devices"; "default-mode regions are only less active during a task if you are not using the right task(s)"; "rest may be best for studying states rather than traits". Her recommendation is integrated designs "that respect the prominence of self-generated activity while offering enhanced control and interpretability".
- Limits stated: "rest likely still has a place"; an Outstanding Questions box.
- Publisher relation: independent academic (inferred: Dartmouth).
- Why add beside: it shows the objection was absorbed rather than answered or ignored. The same sentence concedes that intrinsic activity exists and denies rest a privileged status. That is the position Morcom and Fletcher took in 2007, now argued with fourteen more years of data (tasks and naturalistic paradigms predict behaviour better than rest). Morcom and Fletcher should stay, because they also contest the energy argument, which Finn does not address.
- Verification: full text read (searched: abstract, "From task, to rest, to a 'third wave'", the default-mode section, "The third wave: Integrated designs", Concluding remarks, Outstanding Questions).

### F2.2 Act natural: functional connectivity from naturalistic stimuli fMRI outperforms resting-state in predicting brain activity
- Shachar Gal, Yael Coldham, Niv Tik, Michal Bernstein-Eliav and others. *NeuroImage*, 2022. doi 10.1016/j.neuroimage.2022.119359.
- Bears on: anchor 2 (the empirical side of Finn's case).
- Cites anchor: yes (OpenAlex).
- Finding, authors' words: "naturalistic-stimulus-derived functional connectivity predicts task-induced brain activation maps more accurately than resting-state-derived functional connectivity"; "activation maps predicted using naturalistic stimuli are better predictors of individual intelligence scores".
- Verification: abstract read (OpenAlex).

### F2.3 Brain-wide dynamic coactivation states code for hand movements in the resting state
- Lu Zhang, Lorenzo Pini, Gordon L. Shulman, Maurizio Corbetta. *PNAS*, 2025. doi 10.1073/pnas.2415508122.
- Bears on: anchors 1 and 2 (the strengthening direction: rest carries task structure).
- Cites anchor: yes, Morcom and Fletcher (OpenAlex).
- Finding, authors' words: motor activation states "appeared both at rest and during task execution but underwent temporal reorganization from rest to task"; "resting-state patterns more closely resembled those associated with frequent ecological hand movements than with an unfamiliar movement, indicating a structured repertoire of movement patterns that is replayed at rest".
- Verification: abstract read (OpenAlex).

### F2.4 Neural representations of self-generated thought during think-aloud fMRI
- Tao Li, Bin Lu, Yuwei Wang, Xueying Li and others. *NeuroImage*, 2022. doi 10.1016/j.neuroimage.2022.119775.
- Bears on: anchor 2 (what "rest" contains). This is human self-report, not evidence about any artificial system.
- Cites anchor: yes (OpenAlex).
- Finding, authors' words: "Is the brain at rest during the so-called resting state? Ongoing experiences in the resting state vary in unobserved and uncontrolled ways"; "'resting-state' self-generated thoughts were distributed across a wide range of brain regions involving all seven Yeo networks."
- Verification: abstract read (OpenAlex).

**Also read (abstract; not recommended):**
- Mooraj et al. 2025, *Neuron*: argues task-based imaging "must move center stage" in research on cognitive ageing.
- Fernandino and Binder 2024, *Brain Lang*: a semantic-cognition account of the default mode network.
- Doss, Barrett and Corlett 2022, *ACS Chem Neurosci*: an editorial criticising "the ambiguity and overinterpretation of 'resting state' data".
- Windt 2020, *Phil Trans R Soc B*: spontaneous thought across sleep and waking.
- Rodriguez et al. 2024, bioRxiv: "caricatured connectomes" that remove task-like co-activations from rest.
- Zhang et al. 2021, *NeuroImage*: the resting brain moves between "sensory, somatomotor, and internal mentation networks".
- Northoff et al. 2022 (F1.4): the opposite case.
- Koculak and Wierzchoń 2022, *Front Neurosci* (opinion): OpenAlex's abstract field held only the article header.
- PubMed's cited-in list for the anchor adds Shain et al. 2026, *Nat Commun* (title only).

**Was the objection absorbed, answered or ignored?** Mostly absorbed. Its narrow claim, that rest has no privileged status as a baseline for drawing inferences about cognition, is now a mainstream position on methods (F2.1, F2.2). Its concession, that rest is active, is the consensus. The live counterweight is Finn 2021. The live defence of a baseline is Northoff et al. 2022 (F1.4). Neither side disputes that the brain is active without a task.

---

## Anchor 3. Schurger, Sitt and Dehaene 2012, the accumulator model

Read in full from Ben's PDF (doi 10.1073/pnas.1210467109; *PNAS* 109(42):E2904–E2913, as PubMed gives it). OpenAlex: 506 citing works in all years, 287 from 2020. The Q8 scan already holds Schurger et al. 2021 (C2.2).

### F3.1 Clarifying the nature of stochastic fluctuations and accumulation processes in spontaneous movements — **recommended to add beside the anchor (the critic)**
- Carsten Bogler, Bojana Grujičić, John-Dylan Haynes. *Front Psychol* 14:1271180, 12 October 2023. doi 10.3389/fpsyg.2023.1271180. PMID 37901069; PMC10602783.
- Retrievability: open (CC BY; PMC, 79 KB stripped).
- Systems: humans; the paper reanalyses the published model by simulation and reports no new data.
- Bears on: anchor 3; Q8 headings 2 and 5; North Star §4 (if an initiation axis is drafted), §7.5.
- Cites anchor: yes.
- Findings, authors' words: the points they say need clarification include "(a) the empirical evidence for the role of stochastic fluctuations is so far only indirect"; "(c) a model that is deterministic during the accumulation stage can explain the data in a similar way"; and "(e) contrary to the original interpretation, the deterministic component of the model is quantitatively the dominant input into the accumulator". Within the model: "For the first SDM version (Schurger et al., 2012) the imperative dominates the net input. It has a mean accumulated input of 0.7 ... In contrast, the net contribution of the noise is on average 0 across all trials"; "within this model the trial-wise differences in decision times are a separate matter. They are explained by the noise and not by the imperative"; "both factors are necessary, but quantitatively the constant factor makes the larger contribution".
- Limits stated: "Our aim is not to rehabilitate the role of the RP in the free will debate"; the analysis uses the published parameters.
- Publisher relation: independent academic (inferred: Charité / Bernstein Center Berlin). Haynes is senior author of the "point of no return" study (F3.8).
- Why add beside: it is the most specific critic, it works from inside the anchor's own model, and it changes what the anchor can be cited for in Q8 (see cautions). Gavenas, Schurger and Maoz 2025 (F3.3) treat it as the challenge to answer.
- Verification: full text read (searched: abstract, "the original version of the SDM", the imperative section, "What are the relative contributions of 'noise' and 'imperative'?", Figures 2, 3, 6 and 7 with their text, the linear ballistic accumulator section).

### F3.2 Slow ramping emerges from spontaneous fluctuations in spiking neural networks
- Jake Gavenas, Ueli Rutishauser, Aaron Schurger, Uri Maoz. *Nat Commun* 15(1):7285, 24 August 2024. doi 10.1038/s41467-024-51401-x. PMID 39179554; PMC11344096.
- Retrievability: open (PMC full text downloaded, 140 KB; searched in part).
- Systems: a spiking network model; human single neurons in medial frontal cortex.
- Bears on: anchor 3 (the strengthening direction); Q8 headings 2 and 3 (a network model whose activity ramps without a triggering input).
- Cites anchor: yes (title in references). Schurger is a co-author, so this is the anchor's own research programme, not independent support.
- Findings, authors' words: "we developed a spiking neural-network model that produces spontaneous slow ramping activity in single neurons and population activity with onsets ~2 s before threshold crossings. A key prediction of our model is that neurons that ramp together have correlated firing patterns before ramping onset. We confirmed this model-derived hypothesis in a dataset of human single neuron recordings"; "all simulated slow-ramping signals emerged spontaneously from ongoing activity, without necessitating any external input at ramping onset to drive changes in activity."
- Limits stated: no labelled limitations section was found by search.
- Publisher relation: independent academic (inferred: Chapman, Cedars-Sinai, Caltech, INSERM).
- Note: "without ... external input at ramping onset" is narrower than "without input". Whether the network's background drive plays the role of Bogler's imperative was not checked.
- Verification: abstract read (PubMed); full text searched for "external input", "imperative", "Bogler" and limitations.

### F3.3 Probing for intentions: the early readiness potential does not reflect awareness of motor preparation
- Jake Gavenas, Aaron Schurger, Uri Maoz. *Imaging Neuroscience* 3, 2025. doi 10.1162/imag_a_00465. PMID 40800863; PMC12319783.
- Retrievability: open (CC BY; 105 KB stripped).
- Systems: humans (EEG, probe paradigm); four simulated models.
- Bears on: anchor 3.
- Cites anchor: yes; Schurger is a co-author.
- Findings, authors' words: "pre-probe RP buildups were not related to reported awareness of motor preparation. Computational modeling suggested that the best explanation for these results is via metacognitive access to stochastic accumulation". On the critic: "Bogler et al. (2023) suggested that evidence specific for stochastic accumulation is still lacking, because other models can account for many of the same phenomena"; "Distinguishing between them is, therefore, of paramount importance". Of the models they tested, "stochastic accumulation with dual-stage reporting was the closest to recreating our ERP results".
- Limits stated: they test an alternative in which "reports of preparation are made based on a neural feature unrelated to the RP".
- Publisher relation: independent academic (inferred).
- Verification: full text read (searched: abstract, introduction, model sections 2.7.1–2.7.4, results 3.2.2, the opening of the discussion).

### F3.4 Neural precursors of decisions that matter: an ERP study of deliberate and arbitrary choice
- Uri Maoz, Gideon Yaffe, Christof Koch, Liad Mudrik. *eLife* 8:e39787, 23 October 2019. PMID 31642807; PMC6809608 (full text downloaded, not read).
- Bears on: anchor 3 (arbitrary against deliberate decisions).
- Cites anchor: yes. Published before 2020; included because it is the arbitrary/deliberate test the brief asks for.
- Finding, authors' words: "While we found the expected RPs for arbitrary decisions, they were strikingly absent for deliberate ones. Our results and drift-diffusion model are congruent with the RP representing accumulation of noisy, random fluctuations that drive arbitrary-but not deliberate-decisions."
- Publisher relation: independent academic (inferred).
- Note: one search found no replication since 2020.
- Verification: abstract read (PubMed).

### F3.5 Travers and Haggard: the readiness potential as planning, or as the internal source of action
- Eoin Travers, Maja Friedemann, Patrick Haggard. *Cogn Neurosci*, 2020. doi 10.1080/17588928.2020.1824176. And Eoin Travers, Patrick Haggard. *Eur J Neurosci*, 2020. doi 10.1111/ejn.15063.
- Bears on: anchor 3 (alternative readings).
- Cites anchor: yes, both (OpenAlex).
- Findings, authors' words: "We found that RP amplitudes grew with learning, suggesting that this neural activity reflects planning and anticipation for the forthcoming action, rather than freedom from external constraint" (2020a); "the same RP-like component showed higher amplitudes prior to actions performed without any external evidence (guesses) than for actions performed in response to equivocal, conflicting evidence. This supports the view that the RP reflects the internal source of action, rather than decision uncertainty" (2020b).
- Note: the two papers pull in different directions on whether the signal marks endogeneity. Both contest the pure-noise reading.
- Verification: abstract read (OpenAlex), both.

### F3.6 Mesoscale cortex-wide neural dynamics predict self-initiated actions in mice several seconds prior to movement — **outside humans**
- Catalin Mitelut, Yongxu Zhang, Yuki Sekino, Jamie D. Boyd and others, Timothy H. Murphy. *eLife* 11:e76506, 3 November 2022. PMID 36326239; PMC9671502.
- Retrievability: open (CC BY; 273 KB stripped, including the review record).
- Organisms: mice (widefield calcium imaging, self-initiated lever pulls).
- Bears on: anchor 3 (the weakening direction for the noise reading); Q8 heading 2.
- Cites anchor: yes.
- Findings, authors' words: "we seek to address these issues by evaluating whether pre-movement neural activity in mice contains structure beyond that present in random neural activity"; "upcoming lever pulls could be predicted between 3 and 5 s (or more in some cases) prior to movement"; "These findings support the presence of structured multi-second neural dynamics preceding self-initiated action beyond that expected from random processes."
- Limits stated: "we do not directly address the role of subjective 'intent'"; "our decoding times showed a strong dependence on the number of trials"; micro-movements could not be ruled out because there was no suitable video (acknowledged in the review record).
- Publisher relation: independent academic (inferred: UBC).
- Note: the lever pulls are rewarded with water, so "self-initiated" means uncued, not undriven.
- Verification: full text read (searched: abstract, introduction, the Schurger discussion paragraph, Limitations, Conclusion, response to reviewers).

### F3.7 Ramp-to-threshold dynamics in a hindbrain population controls the timing of spontaneous saccades — **outside humans**
- Alexandro D. Ramirez, Emre R. F. Aksay. *Nat Commun* 12(1):4145, 6 July 2021. PMID 34230474; PMC8260785 (downloaded, not read).
- Organisms: larval zebrafish.
- Cites anchor: yes (OpenAlex).
- Finding, authors' words: "Organisms have the capacity to make decisions based solely on internal drives"; "ablation of neurons with pre-saccadic rise delays saccade initiation"; "ramping of neuronal activity to a bound is a critical component of self-initiated saccadic movements."
- Note: the only causal test (ablation) of a ramp-to-bound account of self-initiated timing that this scan found.
- Verification: abstract read (PubMed).

### F3.8 The point of no return, and whether the readiness potential can be suppressed
- Matthias Schultze-Kraft and others, John-Dylan Haynes. *PNAS* 113(4):1080–1085, 26 January 2016. PMID 26668390. And Schultze-Kraft et al., "Suppress me if you can: neurofeedback of the readiness potential", *eNeuro*, 2021. doi 10.1523/eneuro.0425-20.2020.
- Bears on: anchor 3 (the "point of no return").
- Cites anchor: the 2021 paper does (OpenAlex); the 2016 paper was not checked.
- Findings, authors' words: "subjects can still veto a movement even after the onset of the RP. Cancellation of movements was possible if stop signals occurred earlier than 200 ms before movement onset, thus constituting a point of no return" (2016); "We found no evidence that participants were able to to willfully modulate or suppress their RPs while still eliciting voluntary movements" (2021; the doubled "to" is in the original).
- Note: one search found no study since 2016 that measures the point of no return again.
- Verification: abstract read (PubMed for 2016; OpenAlex for 2021).

### F3.9 Reviews: Libet's legacy (2024) and a meta-analysis of Libet-style experiments (2021)
- Tomáš Dominik, Alfred Mele, Aaron Schurger, Uri Maoz. *Neurosci Biobehav Rev* 157:105503, February 2024. PMID 38072144. Accepted version on PsyArXiv (the download returned HTTP 503).
- Moritz Nicolai Braun, Janet Wessler, Malte Friese. *Neurosci Biobehav Rev* 128:182–198, September 2021. PMID 34119525.
- Findings, authors' words: Dominik et al. "systematically reviewed a set of 2220 publications, with detailed consideration of almost 500". Braun et al.: "there were only k = 6 studies for the time difference between unconscious brain activity and the conscious intention to move"; "some of Libet et al.'s findings appear more fragile than anticipated".
- Note: Dominik et al. is the field's current map. A careful reviewer would read it, but Schurger is an author, so it is not independent of the anchor.
- Verification: abstract read (PubMed), both.

**Also read (abstract; not recommended):**
- Neafsey 2021, *Conscious Cogn*: reviews findings that the RP "may only be an 'artifact of averaging'".
- Mudrik et al. 2022, *Trends Cogn Sci*: unconscious influences on decisions.
- Schurger et al. 2021: already C2.2 in the Q8 scan.

**Artificial agents.** None found. One web search for a readiness-potential analogue in an artificial or reinforcement-learning agent returned only human studies and models of human data. A 2023 conference abstract by Ušacka, Schurger and Garagnani ("a brain-constrained deep neural-network model that can account for the readiness potential") appeared in a search result and was not fetched. Its title suggests it models the human signal rather than treating an artificial system as the subject.

---

## Anchor 4. Sussillo and Abbott 2009, chaotic networks and FORCE learning

OpenAlex id W2099231026, doi 10.1016/j.neuron.2009.07.018 (OpenAlex resolves it to the title). OpenAlex: 1,077 citing works in all years, 614 from 2020. The Q8 scan read it in full (C3.1).

### F4.1 Computation through neural population dynamics — **recommended to add beside the anchor**
- Saurabh Vyas, Matthew D. Golub, David Sussillo, Krishna V. Shenoy. *Annu Rev Neurosci* 43:249–275, July 2020. doi 10.1146/annurev-neuro-092619-094115. PMID 32640928; PMC7402639.
- Retrievability: open (PMC author manuscript, 104 KB stripped).
- Systems: review; monkey and rodent cortex; trained recurrent networks.
- Bears on: anchor 4; Q8 heading 3; North Star §4, §7.5.
- Cites anchor: yes (the most-cited citing work since 2020).
- Findings, authors' words: the framework's central question is "how a neural circuit (captured by f) and its input (captured by u) create the population dynamics". Using a pendulum as the example: "When the dynamics are perturbed by pushing the pendulum, the autonomous dynamics are modified ... Thus, an input can modify the dynamics in a time-dependent way. This can be used in two ways in neural circuits: to add, for example, sensory input to a computation, or to contextualize a computation by changing the dynamical regime". Its summary for arm movements: "preparatory activity sets an initial condition to a neural dynamical system", and "presumably a well-timed input from other brain regions gives rise to a CIS [condition-independent signal], which transitions the preparatory state" before rotational dynamics unfold.
- Limits stated: rotations are "only an approximation to the true nonlinear dynamics"; the framework is presented as still emerging ("If successful").
- Publisher relation: one author is printed as affiliated with Google AI (Sussillo); the rest are independent academics (inferred from printed affiliations). As far as the printed text shows, none developed a language model studied in the library.
- Why add beside: it is the current, open statement of the field that grew from the anchor, and its vocabulary (autonomous dynamics, input u, initial condition) is what Q8's heading 3 needs. Read against the anchor, it shows what changed. The field's working model is no longer "spontaneous activity reorganised into output" but "inputs set the initial state and the timing, and local dynamics run in between". Even here, movement onset is put down to "a well-timed input".
- Verification: full text read (searched: abstract, the pendulum primer, the motor-control summary, the paragraphs on RNNs as hypothesis generators, references for the anchor).

### F4.2 Cortical pattern generation during dexterous movement is input-driven — **the weakening direction for the biological reading**
- Britton A. Sauerbrei, Jian-Zhong Guo, Jeremy D. Cohen and others, Adam W. Hantman. *Nature* 577:386–391, 2020. doi 10.1038/s41586-019-1869-9. PMID 31875851; PMC6962553.
- Retrievability: open (PMC author manuscript, 78 KB stripped).
- Organisms: mice (optogenetics, and silencing and stimulating the thalamus during reach-to-grasp).
- Bears on: anchor 4 (what autonomous network models are taken to show about cortex); Q8 headings 1 and 3.
- Cites anchor: no (title not found in the reference list). Found by search.
- Findings, authors' words: the possibility they tested was that "the motor cortical dynamical system is largely autonomous from its inputs during movement"; "Contrary to the predictions of the autonomous model ..., silencing or stimulating thalamus severely disrupted cortical pattern generation and arm movement. Thus, temporally-patterned inputs are critical for producing the cortical output pattern during movement execution."
- Limits stated: the finding covers execution of one skilled movement in mice.
- Publisher relation: independent academic (inferred: Janelia/HHMI).
- Note: this does not touch the anchor's result about artificial networks. It weakens the step from "a trained chaotic network can generate output with no input" to "cortex does the same".
- Verification: full text read (searched: the two hypotheses in the introduction, the perturbation results, Discussion, the derivative method).

### F4.3 Lyapunov spectra of chaotic recurrent neural networks
- Rainer Engelken, Fred Wolf, L. F. Abbott. *Phys Rev Research* 5:043044, 2023. doi 10.1103/physrevresearch.5.043044. arXiv 2006.02427.
- Retrievability: open (gold; arXiv). Abstract only.
- Systems: random and trained firing-rate recurrent networks.
- Bears on: anchor 4 (the strengthening direction for the artificial claim); Q8 heading 3.
- Cites anchor: yes (OpenAlex).
- Findings, authors' words: "chaos in these networks is extensive with a size-invariant Lyapunov spectrum and characterized by attractor dimensions much smaller than the number of phase space dimensions"; "Fluctuating input reduces both the entropy rate and the attractor dimension"; "For trained recurrent networks, we find that Lyapunov spectrum analysis provides a quantification of error propagation and stability achieved."
- Publisher relation: independent academic (inferred).
- Note: it measures the input-free chaos the anchor starts from, and confirms that input suppresses it. Rajan, Abbott and Sompolinsky 2010, seen in search results, made the same point earlier.
- Verification: abstract read (arXiv abs page).

### F4.4 Theory of gating in recurrent neural networks
- Kamesh Krishnamurthy, Tankut Can, David J. Schwab. *Phys Rev X* 12:011011, 2022. doi 10.1103/physrevx.12.011011. PMID 36545030; PMC9762509.
- Retrievability: open (CC BY; 160 KB stripped).
- Systems: gated recurrent networks of the kind used in machine learning (analysis, mean-field theory and simulation).
- Bears on: anchor 4; Q8 heading 3 (whether machine-learning recurrent architectures have dynamics without input).
- Cites anchor: yes (title in references).
- Findings, authors' words: "Gates also provide a flexible, context-dependent mechanism to reset the memory trace"; "The gate modulating the dimensionality can induce a novel, discontinuous chaotic transition, where inputs push a stable system to strong chaotic activity, in contrast to the typically stabilizing effect of inputs". In the phase diagram, one region "is chaotic in the absence of input and flows to a stable fixed point in the presence of input. However, this behavior is reversed for [parameter range elided: the stripped text lost the mathematical symbols; check against the held text] ... Here, we see a significant swath of phase space which is stable in the absence of input but which becomes chaotic when input is present."
- Publisher relation: independent academic (inferred: Princeton is printed for the corresponding author).
- Note: whether a recurrent network evolves without input depends on its parameters, not its class. The same architecture can be quiet or chaotic when nothing drives it. This supports the Q8 scan's warning that "no forward pass between calls" is a design fact, not a law.
- Verification: full text read (searched: abstract, the sections on spontaneous fixed points and the discontinuous transition, the phase-diagram passage on static input).

### F4.5 Reconstructing computational system dynamics from neural data with recurrent neural networks
- Daniel Durstewitz, Georgia Koppe, Max Ingo Thurm. *Nat Rev Neurosci* 24(11):693–710, November 2023. PMID 37794121.
- Retrievability: paywalled; abstract only.
- Cites anchor: yes (OpenAlex).
- Finding, authors' words: RNNs "can also be trained on the measured physiological and behavioural data, thereby directly inheriting their temporal and geometrical properties. In this way they become a formal surrogate for the experimentally probed system that can be further analysed, perturbed and simulated. This powerful approach is called dynamical system reconstruction."
- Note: this is how a trained network can be run freely, with no input, as a stand-in for a measured system. Not read beyond the abstract.
- Verification: abstract read (PubMed).

### F4.6 Preparatory activity and the expansive null-space
- Mark M. Churchland, Krishna V. Shenoy. *Nat Rev Neurosci* 25(4):213–236, April 2024. PMID 38443626.
- Cites anchor: yes (OpenAlex).
- Finding, authors' words: "Central to such hypotheses are 'output-null' factors that do not directly drive motor outputs yet are essential to the overall computation"; "the range of computational roles hypothesized to be subserved by output-null factors continues to expand."
- Publisher relation: competing interests are printed (neurotechnology companies, including Neuralink and Blackrock Neurotech). No relation to an AI developer is printed.
- Verification: abstract read (PubMed).

**Also read (abstract; not recommended):**
- Recanatesi et al. 2021, *Neuron*: in rats, the variable timing of self-initiated action sequences is modelled by "metastable attractors", with transitions "generated by correlated variability arising from the feedback loop between the two networks" (bears on anchors 3 and 5 as well).
- Logiaco, Abbott and Escola 2021, *Cell Rep*: thalamic units control a recurrent cortical network to string motor motifs together.
- Schuessler et al. 2020, *Phys Rev Research*: random plus low-rank connectivity.
- Perich, Narain and Gallego 2025, *Nat Neurosci*: neural manifolds shaped by "intrinsic (for example, connectivity) and extrinsic (for example, behavior)" constraints.
- Yang and Wang 2020, *Neuron*: a primer on artificial networks for neuroscientists.
- Not read: Kim et al. 2021, *Nat Mach Intell* (reservoirs that run autonomously after training), O'Byrne and Jerbi 2022 and Finkelstein et al. 2021 (no abstract in OpenAlex).

**Has the reading changed?** For the narrow claim about artificial networks, no. A random recurrent network with gain above 1 is chaotic without input. Later theory measures that chaos (F4.3), and shows that in gated machine-learning architectures the same can hold, or reverse, depending on parameters (F4.4). For the biological reading built on the anchor, yes. The field now models cortex as autonomous dynamics that inputs set going and time (F4.1), and the clearest test found shows motor cortex needs patterned thalamic input during movement (F4.2). No better anchor was found for "an artificial system whose state evolves with no input and is coupled to output". The anchor still says it in one paper.

---

## Anchor 5. Maye, Hsieh, Sugihara and Brembs 2007, "Order in spontaneous behavior"

OpenAlex: 276 citing works in all years, 61 from 2020, with many errors (see cautions). PubMed cited-in: 70 in all years, 12 from 2020. The Q8 scan read it in full (C5.2).

### F5.1 Global change in brain state during spontaneous and forced walk in *Drosophila* is composed of combined activity patterns of different neuron classes — **whole-brain imaging; points both ways**
- Sophie Aimon, Karen Y. Cheng, Julijana Gjorgjieva, Ilona C. Grunwald Kadow. *eLife* 12:e85202, 17 April 2023. PMID 37067152; PMC10168698.
- Retrievability: open (CC BY; 160 KB stripped).
- Organisms: adult *Drosophila*, head-fixed, walking on a ball or a treadmill; GCaMP expressed in all neurons and in specific cell classes; light-field whole-brain imaging.
- Bears on: anchor 5; Q8 headings 1, 2 and 5.
- Cites anchor: no (title not found in the reference list). The DOI was recalled from training and confirmed by the PMC ID converter.
- Findings, authors' words: "We observed a global change in activity that tightly correlated with spontaneous bouts of walk"; "While activity onset in some areas preceded walk onset exclusively in spontaneously walking animals, spontaneous and forced walk elicited similar activity in most brain regions. These data suggest a major contribution of walk and walk-related sensory or proprioceptive information to global activity of all major neuronal classes"; "walk itself and not top-down motor control is responsible for the majority of activity observed in actively moving animals' brains"; "we identified several brain components and small subregions, for instance in the posterior slope, that were activated hundreds of milliseconds before the fly started to walk ... This activity was delayed in forced walk and started only when the fly had started to move. This suggests a potential role of these areas in initiating walk."
- Limits stated: activity before onset "could also be due to preparatory movements that were not detected as walk ... or represent the activity of neurons downstream of neurons responsible for triggering walk"; PCA/ICA "would not detect signals strongly corrupted by noise".
- Publisher relation: independent academic (inferred: TU Munich, Bonn).
- Note: the spontaneous-versus-forced comparison is the fly version of the yoked self-initiated/externally-triggered design that the Q8 scan found only in humans (C2.4). Its result cuts both ways: most brain-wide activity during walking is feedback from the walking, and a small set of regions becomes active ahead of spontaneous walking only. It studies walking, not the tethered-flight turning that Maye et al. analysed.
- Verification: full text read (searched: abstract, introduction, "Whole brain imaging reveals broad activation during walk", the walk-onset analysis, "Forced walk recapitulates most activity", Discussion, "Advantages and limitations of the method", Methods for walking substrates).

### F5.2 Capturing the continuous complexity of behaviour in *Caenorhabditis elegans* — **recommended to add beside the anchor**
- Tosif Ahamed, Antonio Carlos Costa, Greg J. Stephens. *Nature Physics* 17:275–283, 2021 (OpenAlex dates it 2020, online). doi 10.1038/s41567-020-01036-8. arXiv 1911.10559.
- Retrievability: the journal version was not fetched; the arXiv preprint (v1, 24 November 2019) was read from its PDF.
- Organisms: *C. elegans*, moving freely (posture taken from video).
- Bears on: anchor 5 (telling deterministic from stochastic variability apart with better instruments); Q8 heading 5.
- Cites anchor: yes (reference 6 in the preprint; OpenAlex).
- Findings, authors' words (preprint): "we find variability in the presence of locally-unstable dynamics, and this unpredictability shows signatures of deterministic chaos: a collection of unstable periodic orbits together with a positive maximal Lyapunov exponent"; "One hypothesis for this variability is that worm behavior is stochastic and results from noise induced transitions between a finite number of elements such as stable limit cycles ... However, the exponential divergence of nearby state-space trajectories ... and the consistency of this divergence with the spectrum of unstable periodic orbits ... as well as the symmetric Lyapunov spectrum ... provide evidence for important, deterministic variation"; "even within a 'single' behavior such as forward crawling, each cycle is deterministically different."
- Limits stated: "the quantitative dynamics of worm posture defy a straightforward interpretation or even, as yet, a model". The analysis covers short-time posture dynamics, which include body mechanics and the environment.
- Publisher relation: independent academic (inferred: OIST, VU Amsterdam).
- Why add beside: it is the cleanest case since 2007 of the move Maye et al. made, telling unstable deterministic dynamics from noise using behaviour alone. It uses stronger tools (state-space reconstruction, the Lyapunov spectrum), and it cites the anchor. Caution: the worms were not in a featureless, stimulus-free setting, so it shows deterministic structure in variability, not endogeneity in Q8's sense. The published version may differ from the preprint.
- Verification: abstract read (arXiv); full text read from the preprint PDF (searched: abstract, "Unstable periodic orbits and deterministic behavioral variability", "Symmetric Lyapunov spectrum", the stochastic-hypothesis paragraph, methods for Lyapunov exponents, references).

### F5.3 Fluctuation-driven neural dynamics reproduce *Drosophila* locomotor patterns — **the noise side**
- Andrea Maesani, Pavan Ramdya, Steeve Cruchet, Kyle Gustafson, Richard Benton, Dario Floreano. *PLoS Comput Biol* 11(11):e1004577, 23 November 2015. PMID 26600381; PMC4657918.
- Retrievability: open (CC BY; 90 KB stripped). Published before 2020; found by web search.
- Organisms: freely walking *Drosophila* (sensory-deprived and odour-evoked), compared against evolved continuous-time recurrent network models.
- Bears on: anchor 5; reconciling it with London et al. 2010; Q8 headings 3 and 5.
- Cites anchor: no (title not found in the reference list).
- Findings, authors' words: the fluctuations neurons receive "are both deterministic, reflecting a neuron's embedding within complex dynamical networks, and random, arising from stochastic noise sources"; "we found that fluctuations and network dynamics were both required by models to match these in vivo data. Neither network dynamics alone ... nor a threshold applied to fluctuations in the absence of a network ... performed as well"; "in the absence of fluctuations or sensory input, network activity remained trapped within stable equilibria below the threshold for walking."
- Limits stated: the models are "not intended to inform the topology of Drosophila AS circuits".
- Publisher relation: independent academic (inferred: EPFL, Lausanne).
- Note: the nearest thing found to a reconciliation of the noise reading with Maye's. Neither pure noise nor pure deterministic dynamics fits fly walking; noise amplified by multistable recurrent dynamics does. It does not address Maye's flight data or cite London et al.
- Verification: full text read (searched: abstract, author summary, introduction, "fluctuations were required", the Class 1 model dynamics, the opening of the Discussion).

### F5.4 Collective action or individual choice: spontaneity and individuality contribute to decision-making in *Drosophila*
- Isabelle Steymans, Luciana M. Pujol-Lereis, Björn Brembs, Ezequiel A. Gorostiza. *PLoS ONE* 16(8):e0256560, 26 August 2021. doi 10.1371/journal.pone.0256560. PMID 34437617; PMC8389364.
- Organisms: *Drosophila* in a light/dark T-maze.
- Bears on: anchor 5 (what the same lab has done since).
- Cites anchor: yes (PubMed).
- Finding, authors' words: "approximately 70% of a group of Drosophila fruit flies choose the bright arm ... Taking the photopositive and the photonegative subgroups and re-testing them reveals the spontaneous component: a similar 70-30 distribution emerges in each of the two subgroups"; "The interaction of individuality and spontaneity together explains why group averages ... are poor predictors of individual choices."
- Note: "spontaneity" here means variability not predicted by the individual's history. The design does not separate intrinsic from stochastic sources.
- Verification: abstract read (PubMed).

### F5.5 The brain as a dynamically active organ
- Björn Brembs. *Biochem Biophys Res Commun* 564:55–69, 2021 (epub December 2020). PMID 33317833.
- Retrievability: an accepted version is listed at epub.uni-regensburg.de, but the download failed (see URLs). Abstract only.
- Cites anchor: yes (OpenAlex).
- Finding, author's words: "Nervous systems are typically described as static networks passively responding to external stimuli (i.e., the 'sensorimotor hypothesis'). However, for more than a century now, evidence has been accumulating that this passive-static perspective is wrong"; the review "details some select modern examples falsifying the sensorimotor hypothesis."
- Publisher relation: independent academic. The author is an author of the anchor, so this is a self-citation.
- Verification: abstract read (PubMed).

### F5.6 Approximations of algorithmic and structural complexity validate cognitive-behavioral experimental results
- Hector Zenil, James A. R. Marshall, Jesper Tegnér. *Front Comput Neurosci*, 2023 (OpenAlex; PubMed lists 2022). doi 10.3389/fncom.2022.956074. PMID 36761393.
- Cites anchor: yes (PubMed, OpenAlex).
- Finding, authors' words: "Our analysis of flight (fruit flies) invalidated the common hypothesis that animals navigating in an environment devoid of stimuli adopt a random strategy. Fruit flies exposed to a featureless environment deviated the most from Levy flight, suggesting an algorithmic bias".
- Note: an independent reanalysis that agrees with Maye et al. that the behaviour is not random. It also departs from their description of it as Lévy-like.
- Verification: abstract read (OpenAlex).

### F5.7 Functional advantages of Lévy walks emerging near a critical point
- Masato S. Abe. *PNAS* 117(39):24336–24344, 29 September 2020. PMID 32929032.
- Cites anchor: yes.
- Finding, author's words: "some findings suggest that Lévy walks might also be epiphenomena that arise from interactions with the environment"; "Based on some evidence that Lévy walks are spontaneously generated in the brain and the fact that power-law distributions in Lévy walks can emerge at a critical point, we hypothesized that the advantages of Lévy walks might be enhanced by criticality". The author's analysis of larval trajectories suggests "the Lévy walks may emerge near a critical point".
- Publisher relation: independent (inferred: RIKEN AIP).
- Verification: abstract read (PubMed).

**Also read (abstract; not recommended):**
- Minasandra et al. 2025, *PNAS*: behavioural sequences in wild meerkats, coatis and hyenas show "decreasing hazard functions", and predictability decays "as a truncated power-law".
- Fenk, Kim and Maimon 2021, *Curr Biol*: motor-related signals in fly visual neurons appear "during spontaneous turns" but are weak during optomotor turns.
- Ghosh and Rihel 2020, *eNeuro*: structure at many timescales in larval zebrafish behaviour.
- Cocconi et al. 2021, *Bull Math Biol*: corrections for boundary effects in intermittent locomotion.
- Koul et al. 2023, *iScience*: interpersonal synchrony of spontaneous movements.

**Has the reading changed, and has the noise reading been reconciled?** The claim that spontaneous fly behaviour is not random has held, and an independent reanalysis supports it (F5.6). The method has moved on: deterministic chaos in behaviour has been shown with stronger tools in the worm (F5.2). Whole-brain imaging has reached the fly (F5.1). Its main message is that much brain-wide activity during spontaneous behaviour is feedback from the behaviour itself, with a small set of regions active ahead of spontaneous action only. No paper was found that explicitly reconciles London et al. 2010's "pure noise" with Maye et al. The nearest are Brembs 2011 (in the Q8 scan: the source of the seed does not matter if the amplifier is nonlinear) and Maesani et al. 2015 (noise plus multistable network dynamics, neither enough alone). No one was found to have applied Maye's procedure to an artificial agent.

---

## Not verified

- **Full texts not retrieved:** Dimakou et al. 2025 (cell.com and doi.org gave no response from this machine); Brembs 2021 BBRC (the repository PDF download failed); Dominik et al. 2024 (OSF/PsyArXiv returned 503); Jamadar et al. 2025 (closed); Durstewitz et al. 2023 (paywalled); Northoff et al. 2022 (repository copy not fetched); the journal version of Ahamed et al. (the preprint was read instead).
- **Downloaded but not read:** Maoz et al. 2019 (PMC6809608), Ramirez and Aksay 2021 (PMC8260785), Schurger et al. 2021 (PMC8192467, already in the Q8 scan), Gavenas et al. 2024 beyond the passages searched.
- **Seen in search results, not fetched:** Rajan, Abbott and Sompolinsky 2010, *Phys Rev E* 82 (input suppresses chaos; arXiv 0912.3513); the Ušacka, Schurger and Garagnani 2023 conference abstract; Callard, Smallwood and Margulies 2012 (a historical critique of the "default"); Kim et al. 2021, *Nat Mach Intell* (no abstract in OpenAlex); the 2016 PNAS commentaries on the point of no return.
- **Whether Gavenas et al. 2024's network has a constant background drive** that does the job of the imperative Bogler et al. analyse.
- **Whether Jamadar et al. 2025 restates or revises** the "often less than 5%" figure for task-evoked energy.
- **Author affiliations and licences** beyond those printed in the fetched texts.

## Gaps

- **No measure in the style of the readiness potential or of Maye et al. has been applied to an artificial agent.** One targeted search was run for each, and none was found. The Q8 scan's gap stands.
- **No explicit reconciliation of London et al. 2010 with Maye et al. 2007.**
- **No whole-brain imaging of the behaviour Maye et al. measured** (tethered flight turning in a featureless surround). F5.1 studies walking.
- **No restatement since 2020 of Morcom and Fletcher's objection to the energy argument.** Finn 2021 addresses rest as a baseline, not energy.
- **No replication found of Maoz et al. 2019's result for deliberate decisions**, and no new measurement of the point of no return since 2016 (one search each).
- **The yoked spontaneous/forced design now exists in the fly (F5.1)** as well as in humans (Q8 scan C2.4). No artificial counterpart was found.

---

## Recommendation

**Per anchor:**

1. **Raichle 2010: keep, and add Pezzulo, Zorzi and Corbetta 2021 (F1.1) beside it.** Raichle is still the statement of the thesis and is now held in full. Pezzulo et al. is open and was read in full. It frames the thesis in today's dominant vocabulary (predictive processing), and it says the function of intrinsic activity is "largely unknown". Swap in Dimakou et al. 2025 (F1.2) if a text is obtained. Reserve: Stringer et al. 2019 (F1.3), for the weakening direction.
   *Does the Q8 short answer still stand for heading 1?* Yes, with one addition. "The brain is intrinsically active" is consensus, conceded by the critics (Morcom and Fletcher 2007; Finn 2021), and the energy figures behind it are now in a held text. "Contested below it" is still right. Rest as a privileged baseline is contested, now with Finn 2021 as the live counterweight and Northoff et al. 2022 as the defence, and function remains open. The addition: in awake animals much "spontaneous" activity tracks the animal's own ongoing movement (Stringer et al. 2019; Aimon et al. 2023 in the fly). So "without input" means "without sensory stimulation or a task", not "without any input". A brain in a body is never fully cut off from input. That makes the brain a less clean example of a system that runs with nothing coming in, and leaves the core finding in place.

2. **Morcom and Fletcher 2007: keep, and add Finn 2021 (F2.1) beside it.** The objection was absorbed. Rest's privileged status is now widely doubted, and both sides concede it is active. Finn is the live, open counterweight. Morcom and Fletcher stay because no paper found since restates their argument against the energy inference.
   *Does the short answer still stand?* Yes. "Whether rest is a privileged baseline (Morcom and Fletcher 2007, against)" is still an accurate summary. The citation should carry Finn 2021 beside it.

3. **Schurger, Sitt and Dehaene 2012: keep, and add Bogler, Grujičić and Haynes 2023 (F3.1) beside it.** The accumulator account is still the leading model. It has been extended (Gavenas et al. 2024, with a test in human single neurons) and defended (Gavenas et al. 2025), but by the anchor's own group. Bogler et al. is the independent critic, and it works from inside the model. Reserve: Maoz et al. 2019 (F3.4) for the arbitrary/deliberate limit; Mitelut et al. 2022 (F3.6) and Ramirez and Aksay 2021 (F3.7) for work outside humans.
   *Does the short answer still stand?* Only in part, and the Q8 scan's wording should not go into intake unchanged. "Spontaneous fluctuation, possibly noise, the proximate timer of self-initiated movement" is still a fair reading of how the model accounts for trial-to-trial timing. But with the model's own published parameters, most of the drive to threshold is a constant "imperative" that reflects the task demand (Bogler et al. 2023; Schurger 2012's "general imperative to produce a movement"). The noise reading holds for arbitrary decisions; readiness potentials are absent before deliberate ones (Maoz et al. 2019). Evidence for the fluctuations themselves is "so far only indirect", and a deterministic model fits the same data. In mice, activity before movement shows "structure beyond that expected from random processes" (Mitelut et al. 2022). The C2.2 note ("a noise-driven accumulator that never stops running versus none running") should become something like: an instructed accumulator, timed by internal fluctuation, that keeps running between cues. That narrows Q8(2)'s contrast between humans and models. The contrast survives, since nothing in a per-call model runs between calls. But the human paradigm is not a case of action with no instruction at all.

4. **Sussillo and Abbott 2009: keep, and add Vyas, Golub, Sussillo and Shenoy 2020 (F4.1) beside it.** No better anchor was found for the claim about artificial networks. Vyas et al. is the open, current review of the framework the anchor started, and it makes the distinction between autonomous and input-driven dynamics explicit. Reserve: Sauerbrei et al. 2020 (F4.2) as the biological counterweight, and Krishnamurthy, Can and Schwab 2022 (F4.4) if the library needs a statement about machine-learning recurrent architectures.
   *Does the short answer still stand?* Yes, for what it claims: "In non-language artificial systems the property exists and is old". Later work adds two things. First, whether a recurrent network evolves without input depends on its parameters, not its class (Krishnamurthy et al. 2022). Second, the biological analogy has weakened. Motor cortex during movement is input-driven (Sauerbrei et al. 2020), and in the field's working model, inputs set the initial state and the timing (Vyas et al. 2020). Using the anchor to say "brains do this too" now needs that caveat.

5. **Maye, Hsieh, Sugihara and Brembs 2007: keep, and add Ahamed, Costa and Stephens 2020 (F5.2) beside it.** Maye et al. is still the only operational procedure found for telling intrinsic from stochastic variability under featureless conditions. Ahamed et al. cite it and make the same separation with stronger tools, finding deterministic chaos in worm behaviour. Reserve: Aimon et al. 2023 (F5.1) for whole-brain imaging and the spontaneous/forced comparison; Maesani et al. 2015 (F5.3) for the noise side.
   *Does the short answer still stand?* Yes. "The one method found that separates intrinsic from stochastic variability is Maye et al. 2007 ... applied to flies, never to an artificial agent" is still true of that method. Two qualifications. Stronger methods for the same separation now exist (Ahamed et al.), though not in a stimulus-free setting. And no published paper reconciles the noise reading with Maye; the nearest is noise plus nonlinear network dynamics, neither enough alone (Maesani et al. 2015; Brembs 2011).

**Net effect on the Q8 intake list:** the anchors stay. Five papers are proposed beside them (Pezzulo 2021, Finn 2021, Bogler 2023, Vyas 2020, Ahamed 2020), all open. Four were read in full here, and Ahamed from its preprint. The heading 2 short answer needs rewording before intake, as above. Ben's PDFs mean Raichle 2010, Morcom and Fletcher 2007 and Schurger 2012 no longer need to stay at `stub` for lack of a text.

**Conflict disclosure, restated for the recommendation (AGENTS.md rule 3).** The drafter is a per-call model. On heading 2, the scan's main finding (the human paradigm runs on a drive from the instruction) narrows the gap between humans and models. That favours the drafter's class and cuts against its deflationary lean. The strongest argument against giving it weight: the "imperative" is a model parameter fitted to data, not a measured signal; Bogler et al. analyse the model, not the brain; and a human under an instruction still produces its own timing from internal state between cues, which no per-call model does. On headings 1 and 5, the finding that "spontaneous" brain activity is partly feedback from the body makes the brain a less clean example of activity without input. The argument against over-reading it: both studies (F1.3, F5.1) also find activity that movement does not explain, and in F5.1 some regions become active ahead of spontaneous action only. Neither finding is used here to recommend an edit to the North Star.

---

## Search and API queries run

**Web searches (13):** (1) review spontaneous brain activity intrinsic predictive processing 2023 2024 "spontaneous activity" Pezzulo Corbetta; (2) Stringer 2019 spontaneous behaviors drive multidimensional brainwide activity "spontaneous" cortical activity explained by movements; (3) critique resting state default mode "baseline" 2022 2023 rest is not a baseline task-free naturalistic paradigm review; (4) Drosophila spontaneous behavior variability intrinsic deterministic versus stochastic noise nonlinear dynamics 2022 2023 2024 study; (5) Ahamed Costa Stephens "Capturing the continuous complexity of behaviour" C. elegans chaotic Lyapunov arXiv; (6) Brembs 2024 OR 2025 spontaneous behavior Drosophila flight variability endogenous initiation paper; (7) Gavenas Rutishauser Schurger Maoz slow ramping spontaneous fluctuations spiking readiness potential Nature Communications; (8) test of stochastic accumulator model readiness potential critique evidence against Schurger 2012 2022 2023 2024; (9) readiness potential arbitrary versus deliberate decisions Maoz eLife 2019 replication 2023 2024; (10) readiness potential analogue artificial agent OR neural network "self-initiated" action timing stochastic accumulator reinforcement learning agent arXiv; (11) "point of no return" vetoing self-initiated movements readiness potential brain-computer interface follow-up 2021 2022; (12) recurrent neural network spontaneous activity without input trained networks review 2022 2023 "spontaneous activity" chaos suppression by input Rajan Abbott Sompolinsky; (13) Sauerbrei 2020 Nature "Cortical pattern generation during dexterous movement is input-driven" thalamus abstract.

**OpenAlex (all with `mailto=anonymous@example.org`):**
- Anchor lookups, `works/https://doi.org/<doi>`: 10.1016/j.tics.2010.01.008 (W2022616811), 10.1016/j.neuroimage.2006.09.013 (W2128129825), 10.1073/pnas.1210467109 (W2012598170), 10.1016/j.neuron.2009.07.018 (W2099231026), 10.1371/journal.pone.0000443 (W2137348639).
- Citing lists, `works?filter=cites:<id>,from_publication_date:2020-01-01&sort=cited_by_count:desc&per-page=50`, for each of the five (counts since 2020: 430, 76, 287, 614, 61).
- Single-work lookups for open-access locations: 10.1016/j.neuron.2025.02.009, 10.1016/j.tics.2024.11.010, 10.1016/j.neubiorev.2023.105503, 10.1016/j.bbrc.2020.12.011, 10.1177/10738584221081752, 10.1016/j.neubiorev.2021.06.018, 10.1038/s41567-020-01036-8, 10.1103/physrevresearch.5.043044, 10.1038/s42256-021-00321-2, 10.1103/physrevx.12.011011, 10.1038/s41583-023-00740-7.

**NCBI E-utilities:**
- `elink` cited-in for PMIDs 17505542, 22869750, 20206576, 17052921, 19709635.
- `esummary` for the cited-in sets of 17505542 and 17052921 (filtered to 2020 onward).
- `esearch`: Bogler[au] AND readiness potential, plus three title searches (Preparatory activity and the expansive null-space; A neural manifold view of the brain; Artificial Neural Networks for Neuroscientists: A Primer).
- `efetch db=pubmed` abstracts: 40101720, 34437617, 32929032, 40372439, 36852275, 33317833, 37901069, 31642807, 39179554, 38072144, 34119525, 36326239, 34230474, 39809687, 37794121, 36545030, 38443626, 40721675, 32970997, 26668390.
- `efetch db=pmc`: PMC8585722, 8363551, 7402639, 9671502, 8260785, 8192467, 6525101, 8315533 (wrong paper, discarded), 10168698, 4657918, 12319783, 11344096, 6809608, 10602783, 6962553, 9762509.
- PMC ID converter: three batches of DOIs. The first request went to the old endpoint, returned HTTP 301, and was repeated at the new address.

**arXiv:** abs pages 1911.10559 and 2006.02427; PDF 1911.10559.

## URLs that could not be fetched or returned incomplete content

- `https://www.cell.com/neuron/fulltext/S0896-6273(25)00127-8` (Dimakou et al. 2025): no response (curl status 000).
- `https://doi.org/10.1016/j.neuron.2025.02.009`: no response (curl status 000).
- `https://epub.uni-regensburg.de/43962/1/responses_01.pdf` (Brembs 2021, accepted version): no response on two attempts (status 000; on the second, curl reported error 43).
- `https://osf.io/a8mqf/download` (Dominik et al., PsyArXiv): HTTP 503.
- `https://www.ncbi.nlm.nih.gov/pmc/utils/idconv/v1.0/`: HTTP 301 to `https://pmc.ncbi.nlm.nih.gov/tools/idconv/api/v1/articles/`; the request was repeated there and succeeded.
- PMC8315533: fetched in full, but it was the wrong paper (from a DOI recalled wrongly); discarded and not quoted.
