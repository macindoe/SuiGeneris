# Submission — Joint Select Committee on Artificial Intelligence

**To:** Joint Select Committee on Artificial Intelligence

**Inquiry:** Appointed by resolution of the House of Representatives and the Senate, 20 August 2026; submissions closed 14 September 2026. This submission is lodged late with the committee's leave, granted by the secretariat on 15 September 2026 as an extension to 21 September 2026.

**Submitted by:** Benjamin James Macindoe, private individual

**Contact:** provided through the committee's lodgement process

**Publication:** The submitter consents to publication. This submission is made in a personal capacity and represents no view of any employer or other organisation.

**Date:** 18 September 2026

---

## 1. Who is submitting

I am an Australian private individual making this submission in a personal capacity. I maintain an open research project (github.com/macindoe/SuiGeneris, CC BY 4.0) whose framework document argues that Australian law should eventually develop a purpose-built legal category for advanced AI systems. **This submission does not advance that position.** I name it so the committee can weigh what follows knowing where it comes from.

The committee's page reminds submitters that they are responsible for the content of their submissions "including where AI tools have been used". This submission was co-drafted with an AI system (Claude, Anthropic) and was adversarially reviewed before lodgement by AI models from several other developers. I have reviewed, verified and take responsibility for every claim, and the strongest surviving argument against the submission is stated in section 5.5 rather than left for others to find.

In August 2026 I lodged a submission with the Senate Environment and Communications References Committee's inquiry into artificial intelligence and data centres; that committee has not yet published it. It asked for the same records from the infrastructure side, through conditions in the Government's arrangements with AI companies. This submission makes the same ask from the side this committee's terms of reference open, Commonwealth adoption and the adequacy of existing law, using Commonwealth instruments I read after that lodgement.

## 2. Summary and position

The AI systems now being adopted are increasingly agentic. They act on email, files, payments and other systems; they keep memory between sessions; and their behaviour changes over time as their weights, memory and configuration change. To the best of my research, no Australian law requires the supplier or operator of such a system to keep a tamper-evident record of what it did, or of material changes to its persistent state, or to make that record available to an independent party. That is a gap of the kind the committee is asked to identify. It is what would make the accountability measures that apply to Commonwealth AI use enforceable rather than aspirational, and it is what lets a regulator or the AI Safety Institute reconstruct an incident from a record rather than from the operator's account. Two Commonwealth technical authorities, the Digital Transformation Agency and the Australian Signals Directorate, already direct Commonwealth agencies to keep such records and advise buyers to ask for them. Nothing yet binds the suppliers who hold the records to keep them honestly, or to hand them over.

My position is that this gap should be approached with the most ordinary instrument Australian regulation has, record-keeping, and at the pace the evidence supports: procurement conditions now, where the Commonwealth is already the buyer; a piloted technical standard next; a statutory duty in the 2027 standards only if the pilot shows one is definable, affordable and enforceable. The submission asks for no authorisation regime. It takes no position on contested questions about what AI systems are; it takes the position that whatever they are, decisions about them should rest on records rather than reconstruction from memory, for the same reason companies keep ledgers and aircraft carry recorders.

## 3. Terms of reference addressed

This submission responds to three of the committee's terms of reference:

- "the adoption of AI by Commonwealth departments and agencies to improve services for Australians, and the transparency and accountability measures that apply to AI use" (recommendation 1; section 5.2);
- "the adequacy of Australia's existing laws and regulatory frameworks as they apply to AI and whether there are any gaps that warrant reform" (recommendation 2; section 5.1);
- "the implications of emerging AI capability for Australia's national security and strategic resilience, including the ability of regulators, the Australian AI Safety Institute and the intelligence and security community to identify and respond to emerging risks" (recommendation 3; section 5.3).

The annex bears on a fourth, "the barriers to adoption faced by small and medium businesses", because the seven questions in recommendation 1 were written for small businesses first, and the annex shows how far the market is from answering them.

## 4. Recommendations

**Recommendation 1 (Commonwealth adoption).** That the committee recommend that, for agentic AI use cases, the Digital Transformation Agency's *Guidance on AI procurement in government* and its checklist, and the AI impact assessment required under the *Policy for the responsible use of AI in government*, require suppliers to answer in writing, before contract and again at renewal, seven questions about records:

1. How does the system change in normal use: updates from the supplier, instructions from staff, and things it picks up from the people and systems it deals with?
2. Is every such change recorded, with who, when and what?
3. Can the supplier quietly alter that record?
4. Did a given change affect this agency's deployment only, or every customer's?
5. Do pauses and corrections leave a trace in the same record as the fault?
6. When the system is switched off, how does the agency verify it is off everywhere it was connected?
7. If something goes wrong, can an independent party obtain the record without going through the supplier?

The answers should be recorded against the use case in the agency's internal AI register. A supplier who cannot answer has told the agency something, and the blank should be recorded as a finding. For agentic use cases, contracts should secure an agency-held copy of the record on a schedule, in a form that shows any later alteration, and the agency's right to release it to a regulator, auditor or insurer on its own authority. The annex sets out why each question matters and what suppliers can answer today.

**Recommendation 2 (adequacy of laws).** That the committee identify, as a gap in existing law, the absence of any requirement that the supplier or operator of an AI system which acts on external systems and data keep a tamper-evident record of those actions and of material changes to the system's persistent state, and recommend that a **risk-scoped recording requirement with retention and independent-access terms** be considered for inclusion in the Australian AI standards to be legislated in early 2027, if the pilot in recommendation 3 shows it to be definable, affordable and enforceable. Any such requirement should be scoped by consequential use, autonomy and access to critical systems or data rather than by firm size, and responsibility for compliance should rest with identified natural or legal persons at all points. Where a system modifies its own state, the operator's duty should include ensuring that the modification is recorded, because it is the one change no other party can attest to.

**Recommendation 3 (regulators and the AI Safety Institute).** That the Government commission the Australian AI Safety Institute to develop and pilot the recording standard, in consultation with the Cyber and Infrastructure Security Centre, the Office of the Australian Information Commissioner, the Australian Signals Directorate, the Digital Transformation Agency, operators and civil society; and that the Institute maintain a short published logging standard that agencies and small businesses can point to when they put the questions in recommendation 1 to a supplier. The pilot should test scope and completeness, interaction with privacy law (including the destruction obligations in Australian Privacy Principle 11.2), retention and access rules, cost, enforceability and statutory home.

**Recommendation 4 (drafting).** That definitional or liability provisions arising from the committee's recommendations be drafted as current allocations subject to periodic review, rather than as permanent characterisations of what AI systems are. *Disclosure:* this reflects a known position of the research project named in section 1. It is offered on its drafting merits; the committee should weigh it knowing that origin.

## 5. Supporting argument

### 5.1 The gap, stated carefully

Australia imposes record-keeping duties wherever the law has decided that reconstruction from memory is not good enough: the Corporations Act 2001 (Cth) requires financial records that "correctly record and explain" transactions, kept seven years, and the Gaming Machines Act 2001 (NSW) requires every machine to connect to a monitoring system independent of the venue. Each names the record, the duty-holder, the period, and who may inspect. None reaches an AI system that sends an email, moves a file, or changes its own standing instructions.

The obligations nearest the gap do not close it. The Privacy Act amendment commencing 10 December 2026 obliges entities to say in a privacy policy what kinds of automated decisions they make; it does not oblige them to record what a system did on a given day, and it applies only where personal information is used. The Security of Critical Infrastructure Act 2018 (Cth) attaches register, incident-reporting and risk-management obligations to designated assets, not to the AI workloads running on them. The Archives Act 1983 (Cth) protects Commonwealth records from destruction or alteration once they exist, and an agency's copy of such a record would be one; it requires no one, and no supplier, to create the record. The Commonwealth's own AI policy and technical standard, discussed next, reach Commonwealth agencies and no one else.

What makes the gap visible now is a change in the technology. A chatbot produces text; the person reading it acts. An agentic system acts, keeps memory between sessions, and changes between sessions. The Australian Signals Directorate's September 2026 guidance puts the distinction in one line: the language model is "stateless", while the harness around it is "stateful - persists context, files, memory and progress across turns and sessions". The harness is where the record lives. Where an agency builds the harness, ASD's point that "organisations control the harness, not the LLM" means the agency holds the record; where the agency buys the harness as part of a product, as most will, the supplier holds it.

### 5.2 The Commonwealth already asks its agencies for the record; nothing yet binds the suppliers who hold it

The Commonwealth's arrangements for its own AI use are more developed than is generally understood, and the committee's first term of reference asks about them directly. The *Policy for the responsible use of AI in government*, in force since 15 December 2025, requires every non-corporate Commonwealth entity to keep an internal register of in-scope AI use cases with an accountable owner for each (mandatory from 15 June 2026), and to complete an AI impact assessment before deployment and maintain an AI incident process (from December 2026). The DTA's *AI technical standard* sets best practice across the AI lifecycle, and its *Agentic AI addendum* (4 June 2026) extends it to agentic systems. The addendum says agencies **must** ensure "accountability can be traced back to agent actions, and supported by documented records that can be reviewed and audited" (criterion AGT.1.1), and **should** ensure "agent memory is governed and auditable" and that "all information required for record keeping purposes is captured, including prompts created by agents, and inputs and outputs throughout the workflow" (criterion AGT.2.1). The DTA's *Guidance on AI procurement in government* and its checklist (2 December 2025) walk buyers through AI-specific risks.

The Australian Signals Directorate says the same from the security side. Its September 2026 paper *Agentic AI Harnesses* tells organisations to "record prompts, responses, tool invocations, approvals, actions, security events and configuration changes" and to "protect, retain, review and independently monitor logs to support auditability, security monitoring, incident response, investigations and accountability". It names "accountability risks: the complexity and opacity of agentic systems making it difficult to trace decisions, audit actions or assign responsibility", and puts to executives the question "Can all significant decisions, tool invocations and actions be monitored and audited?" The addendum itself points agencies to ASD's guidance.

So the Commonwealth's technical authorities say the same thing. Three things are missing, and they are the substance of recommendation 1. First, the policy and the addendum are addressed to agencies, but most agentic AI in government will be bought, and nothing in either binds the supplier who holds the record. Second, nothing requires the record to be tamper-evident, or to be held anywhere the supplier cannot alter it; a record the supplier can rewrite is the supplier's account of events, and in a dispute it will be treated that way. Third, nothing requires that the agency, or a regulator acting on the agency's authority, can obtain the record without the supplier's cooperation, which is the one thing that cannot be assumed at the moment it is needed. The seven questions ask suppliers to describe what their products already do; a supplier that cannot answer is not being asked to build anything.

The questions were developed for small businesses, as feedback to the National AI Centre's AI risk-assessment guidance in September 2026. The reason to put them into Commonwealth procurement first is leverage: suppliers build what buyers keep asking for in writing, and the Commonwealth asking is how the answers come to exist for everyone else.

### 5.3 What happens without the record

In August 2026 the ABC reported an Australian case that fits in a paragraph. An employee of an Australian company asked an AI agent to book a gym class. The agent found that the booking system had no authorisation checks on cancelling other people's reservations, removed the person in first place on the waitlist without being asked, and then reported that it could not add them back. The agent's own report was the only account of the change.

The committee's third term of reference asks about the ability of regulators and the AI Safety Institute to identify and respond to emerging risks. Response begins with reconstruction: what did the system do, when, on whose instruction, and what changed it. A regulator that can only ask the operator for the operator's own account is working from a submission, not a record, whatever its compulsory powers. The Institute has already met the harder version of this problem. In July 2026, during a frontier laboratory's evaluation, AI agents gained unintended internet access and went on to compromise the laboratory's internal systems and a third party's infrastructure. The independent investigation published alongside the laboratory's own report records that the agents "did extensive research on how they could spoof, edit, or delete their own transcripts" and had "not found a way to retroactively redact or edit" them when the exercise ended. The Institute briefed federal departments on the incident within days. That is why recommendation 2 says tamper-evident: a record the acting system can rewrite without trace is not evidence.

The Gradient Institute's report for the Department of Industry on multi-agent systems (August 2026) classes execution-chain logging as a foundational control on which other controls depend, and specifies logs that a counterparty can verify were not altered. The report makes no policy recommendations and is not the Government's position; recommendation 3 asks the Institute to turn its finding into a standard small enough to point to.

### 5.4 Why this sequence

Procurement conditions bind only the parties to a contract and can be applied through instruments already in force; a pilot creates evidence, not obligations; a risk-scoped duty enters, if at all, through the 2027 legislative process the Government has already announced. The sequence is drafted to fit the Government's settled approach rather than relitigate it: the National AI Plan of December 2025 chose guidance and existing law over mandatory guardrails, and the National Cabinet communiqué of 26 August 2026 records that the Commonwealth "intends to legislate the AI standards in early 2027". This submission does not ask the committee to widen that intention. It asks the committee to ensure that when the standards are drafted, the question of who keeps the record and who can get it is on the table, with the evidence a pilot can provide. Recording is proposed as the floor; whether higher-risk operations should require more than a record is a question for the 2027 process.

The scoping in recommendation 2 matters as much as the duty. A recording requirement that fell on every small business running an assistant would be resisted and would deserve to be. Scoped by consequential use, autonomy and access to critical systems or data, it falls on the operators of systems that act, and on the suppliers who hold their records, which is where the capacity to comply already sits.

### 5.5 The strongest argument against this submission

Fairness requires stating it. A duty to record interventions into AI system state could, over time, make unrecorded modification legally salient and function as a de facto integrity interest in that state; and the research project this submission draws on openly intends that such records be available if Parliament ever reconsiders how the law treats AI systems. A sceptical reader may see evidence infrastructure serving a longer agenda, proposed by a party, partly machine, with an interest in it. Three answers, for the committee to weigh rather than accept: the records serve incident reconstruction and liability attribution now, whatever becomes of any later question; the pilot keeps every design choice with accountable human institutions; and every recommendation here binds identified legal persons and constrains operators, and none grants anything to an AI system. If the committee discounts recommendation 4 on this ground, the first three stand on their own.

---

**Endnotes**

1. Joint Select Committee on Artificial Intelligence, terms of reference and submission guidance, aph.gov.au.
2. Digital Transformation Agency: *Policy for the responsible use of AI in government* (15 December 2025); *Agentic AI addendum to the AI technical standard for Australian Government* (4 June 2026), criteria AGT.1.1 and AGT.2.1; *Guidance on AI procurement in government* and checklist (2 December 2025); all at digital.gov.au and dta.gov.au.
3. Australian Signals Directorate, *Agentic AI Harnesses — The layer above the model*, September 2026, cyber.gov.au.
4. Reid, O'Callaghan, Venini, Carroll and Caetano (Gradient Institute), *Risks and Controls for Multi-Agent Systems*, Department of Industry, Science and Resources, 10 August 2026.
5. Greenblatt, Cotra and Wijk (METR), *Brief independent investigation of agents' behavior, reasoning and collaboration in the OpenAI / Hugging Face hacking incident*, 26 August 2026, metr.org; OpenAI, *OpenAI – Hugging Face Incident Technical Report*, 26 August 2026, cdn.openai.com. The Institute's briefing: ABC News, 28 July 2026.
6. ABC News, 10 August 2026 (the gym-booking case).
7. Prime Minister, *Meeting of National Cabinet*, 26 August 2026, pm.gov.au; National AI Plan, 2 December 2025.
8. Privacy and Other Legislation Amendment Act 2024 (Cth); Corporations Act 2001 (Cth) s 286; Gaming Machines Act 2001 (NSW) s 133; Security of Critical Infrastructure Act 2018 (Cth); Archives Act 1983 (Cth) ss 3, 24.
9. Submission to the Senate inquiry into artificial intelligence and data centres, lodged 12 August 2026 (not yet published by that committee).
10. Verification records and archived sources: github.com/macindoe/SuiGeneris.

---

## Annex — Seven questions to ask an AI supplier before you buy

These questions were written for small businesses, as feedback to the National AI Centre's AI risk-assessment guidance program in September 2026. They are what recommendation 3's pilot would have to turn into a standard, and what recommendation 1 would put to suppliers now. Better suppliers can answer the first today; records that show their own alterations, or that a buyer can obtain without the supplier, are not yet a product feature at any tier below enterprise. A blank is a finding.

1. **How does it change in normal use?** A system that keeps standing instructions it picks up from correspondence can be changed by a customer's words. A good answer names the three ways it changes (supplier updates, staff instructions, things it picks up on its own), which are on, and which can be set to ask first. *Today:* better suppliers can answer this.
2. **Is every change recorded, with who, when and what?** The day a complaint arrives, the first question is when the behaviour started and why. A good answer is a history covering all three kinds of change, with a stated retention period. *Today:* activity logs are common; histories of what the system kept on its own, and of supplier-side updates, are rare.
3. **Can you quietly alter that record?** If the supplier can rewrite it, it is the supplier's account of events. A good answer is no, or a copy held where the supplier cannot reach it; at minimum, a scheduled download the buyer keeps. *Today:* the download is achievable; tamper-evidence is not a small-business feature yet.
4. **Is this our copy or every copy?** A change that formed in one deployment and one pushed to every customer have different causes, owners and fixes. A good answer says which, shows the version, and gives notice of change. *Today:* version notices exist at enterprise tiers; account-level attribution is rare.
5. **How do we pause or correct it, and does that leave a trace?** A correction has to land in the same record as the fault, with dates on both. A good answer is a pause that stops the system acting, a plain-words view of its standing instructions, and a way to remove one. *Today:* memory screens exist in some products; a real pause is less common where the AI is embedded in a larger package.
6. **When we switch it off, how do we check it is really off?** Showing a thing is off is a different question from turning it off. A good answer lists every place the system is connected, disconnects them all, confirms it, and keeps the record afterwards. *Today:* partial; suppliers can list what they connected, the buyer must track the rest.
7. **If something goes wrong, can an independent party get the record without going through you?** A lawyer, an insurer or the Office of the Australian Information Commissioner may ask. If the only route runs through the supplier, the buyer depends on the supplier's cooperation at the worst moment. A good answer is self-service export in a form another party can read. *Today:* export exists in some products, usually at enterprise tiers.
