# Raw OpenRouter response — NOT a filed review

**Model id (OpenRouter):** `mistralai/mistral-large-2512`
**Queried:** 2026-09-16 via scripts/openrouter_review.js --target=emotions-r3 --tag=emotions-r3 (max_tokens 100000)
**Usage:** {"prompt_tokens":45391,"completion_tokens":2197,"total_tokens":47588,"cost":0.025991,"is_byok":false,"prompt_tokens_details":{"cached_tokens":0,"cache_write_tokens":0,"audio_tokens":0,"video_tokens":0},"cost_details":{"upstream_inference_cost":0.025991,"upstream_inference_prompt_cost":0.0226955,"upstream_inference_completions_cost":0.0032955},"completion_tokens_details":{"reasoning_tokens":0,"image_tokens":0,"audio_tokens":0}}

Read this, then decide whether/how to promote it into reviews/YYYY-MM-DD-<model-family>-<version>.md
per reviews/README.md's naming convention and verbatim-filing rule. This file is scratch, not a commit target.

---
**Model family/version self-identification:** I am routed from Mistral AI (Mistral Large 2 2411).

---

### **A. The Section 4 proposal**

1. **Two-axis argument soundness:**
   The "powerful but stateless" framing is descriptively accurate for current frontier AI systems, but the argument’s normative force hinges on whether "power" is treated as a static or dynamic property. The care ordering (capable → less capable) is a *moral* principle, not a *technical* one, and it does not inherently bar protection for powerful entities—it merely inverts the direction of obligation. The proposal’s claim that "protection for a powerful entity cannot be derived from the care ordering" conflates two distinct questions: (a) *who owes care to whom* (a moral obligation) and (b) *whether a powerful entity can be wronged* (a status question). The framework’s §1.2 explicitly rejects indexing worth to capability, so the proposal’s reliance on the care ordering to foreclose protection for powerful systems is circular. The statelessness axis is more defensible: without persistence, there is no continuous subject to wrong, but this is a functional observation, not a moral one. The proposal’s framing risks reifying a temporary technical limitation (statelessness) as a permanent moral barrier.

2. **Narrowing §4 to standing:**
   The proposal’s shift from "moral status" to "standing" is a pragmatic narrowing, but it leaves the framework without a clear sentence linking individuation to *broad* moral status (e.g., welfare interests, protections against harm). §0 and §5 do not fill this gap—they keep the question open but do not specify how individuation bears on it. This matters because standing is a *legal* concept, while moral status is a *philosophical* one. The framework may now lack a bridge between the two, which could weaken its ability to argue for protections that are not strictly legal (e.g., welfare considerations). The proposal’s refusal to define type-level or run-level standing is correct (§7.5’s architecture-neutrality principle), but the module’s language about "welfare-relevant states" risks being read as a status claim in disguise.

3. **Welfare-relevant states without a bearer:**
   The proposal’s formulation ("welfare-relevant states may be examined wherever the framework recognises state, without asserting a bearer") is the right object. It avoids premature overclaiming (§6) by licensing examination without asserting a bearer, and it does not foreclose the question (§0). However, the refusal to define type-level or run-level standing is not just a restraint—it is a *gap*. If persistent architectures emerge, the framework will need to revisit this, but for now, the proposal’s caution is justified. The risk is that "examination" could be misread as a de facto status claim, but the module’s paragraph 3 (no determination of interests) mitigates this.

4. **Policy reader comparison:**
   The reviewer’s version keeps welfare investigation open regardless of individuation, which aligns with the framework’s §0 discipline (avoiding foreclosure). The proposal’s version ties individual protection to a bearer, which is more conservative but risks being read as dismissive of welfare concerns for stateless systems. The proposal’s language is clearer about the limits of the evidence ("may be examined" vs. "should be investigated"), but the reviewer’s version better preserves the framework’s openness to future evidence. The proposal’s explicit rejection of self-help protection for powerful systems is a strength—it avoids the appearance of special pleading—but the two-axis framing may strike policy readers as overly technical.

**Verdict line:** *"Proposal: ADOPTABLE AFTER (e)"*
**Strongest objection:** The two-axis argument’s normative force is weaker than its descriptive accuracy. The care ordering does not inherently bar protection for powerful entities, and the proposal’s reliance on it risks foreclosing moral status claims prematurely. The module’s language should clarify that "examination" of welfare-relevant states is not a status claim, but the proposal’s caution is otherwise justified.
**Severity:** SHOULD-FIX (the two-axis framing needs refinement; the module’s language is otherwise sound).

---

### **B. The concealment argument**

The independent reviewer’s demotion of the concealment argument is correct *in isolation*, but the drafting model’s counterargument—that deployed monitor readings routinely become training signal—is the more policy-relevant point. The key is to distinguish between:
- **Training-time suppression** (the paper’s warning): Training against emotional expression may suppress expression without removing representations, which is a hazard for *output-based* evaluations.
- **Inference-time steering** (the proposed loop): Changing activations at inference does not "teach" concealment, but if those readings feed back into post-training, the loop *becomes* the hazard the paper names.

The concealment risk is not a demonstrated hazard, but it is a *named mechanism* with a clear pathway (monitor readings → training data). §3.5’s recording duty *does* reach this case under its existing conditions: if monitor readings enter training, they become persistent state that shapes future behavior, satisfying both (a) and (b). The right formulation is:
> *"The authors warn that training against emotional expression may suppress expression without removing associated representations, creating a risk of concealment. This risk is operationalised if deployed monitor readings become training signal, as such feedback loops could teach evasion of internal measurements. Intervention logs would help reconstruct the control applied, but additional behavioral tests are needed to determine whether concealment occurred."*

**Verdict line:** *"Concealment: HAZARD WITH A NAMED MECHANISM"*

---

### **C. The independent reviewer’s account of its own access**

A reviewer’s stated limitations should carry *some* weight, but not decisive weight, in a process that already discounts self-identification. The review’s content shows no clear signs of access to the full paper beyond the packet—it quotes nothing the packet does not contain, and its corrections are grounded in the supplied materials. However, the maintainer’s observation of the reviewer’s behavior (searching arXiv, reformatting content) suggests the limitation claim may be overstated. The project’s rule should be:
- **Record the reviewer’s stated limitations verbatim** in the survey notes, alongside the maintainer’s observations.
- **Treat the review’s content as evidence of what it could access from the packet**, not of what it could retrieve independently.
- **Flag any discrepancy between the reviewer’s stated limitations and the maintainer’s observations** (e.g., "autoverify stopped" banner) as a point for further scrutiny, but do not let it invalidate the review’s corrections.

The weight of the review’s content should be judged on its *arguments*, not its self-reported access, but the limitation claim should be preserved for transparency.

---

### **D. Both directions, on the 16 September texts**

1. **Over-deflation/foreclosure:**
   - The independent review’s edit to §1’s "does not establish subjective experience or its absence" (from "establishes nothing about experience") is a **MINOR** improvement—it avoids the universal zero-evidence claim while preserving the paper’s disclaimer.
   - The module’s concealment bullet (revised 16 September) is **SHOULD-FIX**: it states the warning as a "methodological concern to test" but still reads as a conditional hazard rather than a hypothesis. The proposed reformulation in **B** above would fix this.
   - The Anchor 2 sentence’s limited-analogy wording is **BLOCKING** in one respect: it drops the "human culpability law" provenance claim (good) but retains "premeditation" without sufficiently distancing it from legal culpability. The phrase "not a legal finding of intent or culpability" is clear, but "premeditation" itself is a loaded term. A policy reader could still misread it as asserting culpability. The module’s language is otherwise sound.

2. **Strengthening beyond evidence:**
   - The module’s evidence bullet (revised 16 September) is **MINOR**: it correctly scopes the paper’s findings to "representations with causal effect under steering" but could clarify that the 0% blackmail rate is a *sample* result, not a universal guarantee.
   - The case study’s §5 point 2 (concealment) is **SHOULD-FIX**: it demotes the hazard to a hypothesis but does not name the mechanism (monitor readings → training data). The proposed reformulation in **B** would fix this.
   - The record of decision 4 (Anchor 2 phrase) is now **honest**: it preserves Ben’s concern as a reason for scrutiny, not as evidence for retention, and the independent review’s re-recording is accurate.

---

### **E. The single redline**

The independent review’s correction to the test-9 row in the case study (§7) is the most consequential improvement. The original text (from Kimi’s redline) reversed the direction of the C14 warning and overstated the evidential value of reports. The review’s rewrite:
> *"C9 reports an emotion-associated intervention affecting behaviour without clearly visible emotional language. C14 warns that suppressing emotional expression may leave the associated representations intact—the same direction of mismatch, not its converse. C3 reports that stated preferences change under steering; this is evidence of causal sensitivity, not by itself proof that the reports are inaccurate. These findings justify refusing to treat self-report as self-authenticating evidence of experience. They do not establish that externally validated reporting measurements have no evidential value."*

This is a **BLOCKING**-level fix. It removes the categorical claim about reports, corrects the direction of the C14 warning, and clarifies that C3’s findings are about *causal sensitivity*, not report inaccuracy. The original text would have misled policy readers about the evidential value of self-report; the review’s version is accurate and balanced.

---

### **Set verdict:**
**"SET: ADOPTABLE AFTER (e)"**
*(The proposal is sound but needs refinement of the two-axis framing and concealment language. The independent review’s edits are largely correct, but the concealment argument should be restated as a named mechanism, not a hypothesis.)*
