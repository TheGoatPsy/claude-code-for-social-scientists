---
title_en: "Research Lifecycle Map, From Idea to Publication, From Publication to Archive"
title_tr: "Araştırma Yaşam Döngüsü, Fikirden Yayına, Yayından Arşive"
booklet_id: "001-02-0001"
category: "001-foundations"
language: "en"
version: "0.1.0"
date_published: "2026-06-21"
date_last_revised: "2026-06-21"
authors:
  - name: "Onour Impram"
    orcid: "0000-0003-1076-3928"
    role: "author, principal reviewer"
ai_assisted: true
ai_tools:
  - name: "Claude Code"
    vendor: "Anthropic"
    model_alias: "claude-opus-4-8"
    model_dated: null
    role: "drafting, verification, citation lookup, bilingual re-authoring"
    interaction_mode: "interactive console"
ai_contribution_level: "co-drafting"
human_review: "complete"
human_review_date: "2026-06-21"
verified_citations_count: 9
fabricated_citations_count: 0
disclosure_standard: "COPE 2023 + WAME 2023 + ICMJE 2024 + STM 2025 + EU AI Act 2024/1689 Art. 50 + ENAI"
translation_notes: "Native re-authoring from the finalized Turkish source (tr.md, v0.1.0). Same section order, same argument line, same verified citation set. English is not a literal translation but an independent composition in academic English preserving the author's argumentative voice."
license:
  - "CC-BY-NC-SA-4.0 (prose)"
status: "release"
---

# Research Lifecycle Map, From Idea to Publication, From Publication to Archive

This booklet situates the full guide within a single organizing framework. The preceding foundations booklets addressed what Claude Code means for the social science researcher, how agent-based work differs from a chat window, what methodological checks govern a first installation, and how standing instructions through CLAUDE.md function as a methodological instrument. This booklet turns to the more immediate and harder question: where in the research process am I right now, and what protocol does that position require?

The academic life of a social scientist does not unfold in a single linear sequence. A manuscript draft is in progress; an ethics committee file is pending; a reviewer response has just arrived; a source archived a year ago needs to be found again. Across these parallel currents, AI-assisted work can carry genuine weight — but only when the right tool is matched to the right stage. A powerful tool deployed at the wrong stage does not increase productivity; it blurs the method and breaks the decision trail.

The central claim of this booklet is this: Claude Code can only be positioned responsibly within the social scientist's research lifecycle through stage diagnosis. The sequence is tool after stage, stage after responsibility, automation after accountability. When that sequence is reversed, the researcher does not use the tool — the tool uses the researcher.

## 1. Why mapping the lifecycle matters

The most common error researchers make is mislabeling the work in front of them. A researcher who believes she is conducting a literature review may in fact be trying to sharpen an unsettled research question. A researcher who believes he has moved into analysis may not yet have committed the data-preparation decisions to a record. A researcher writing a reviewer response may discover, mid-draft, that the paper's theoretical framework needs to be rebuilt from the ground up.

A lifecycle map reduces that confusion. It tells the researcher which question to ask at each point. In the idea stage, the right question is not which sources to gather but what conceptual tension the research question is meant to address. In the analysis stage, the right question is not which statistical test to run but which decisions were committed to writing before the data were examined. In the writing stage, the right question is not how much text has been produced but how consistently the text reflects the decisions made across the preceding stages.

The lifecycle map is therefore not a production schedule. It is a reasoning instrument. It shows when each type of risk arises, which document should be produced, and which form of AI-assisted work stays within defensible limits. Munafò et al. (2017) identified pre-design transparency, rigorous data management, and pre-specified analysis as the structural preconditions for reproducible science. Each precondition corresponds to a distinct node in the lifecycle. Without mapping the cycle, knowing where each condition must be satisfied is not possible.

In AI-assisted research, this need presses harder. An agent can produce a response to a question the researcher has not yet consciously formulated. It can propose alternative analysis paths while the researcher is still trying to clarify scope. Given an open-ended instruction, it may advance to an output stage the researcher did not intend. That drift is silent and rapid. A map makes it visible; without one, the drift surfaces only under peer review.

## 2. From idea to research question

An idea is not yet a research question. An idea typically begins as a broad intuition, a personal observation, or a felt gap in what the researcher knows. A research question is a bounded structure with a traceable place in the literature and a methodological path toward an answer. The distance between those two forms is where most research either gains or loses its foundation.

An agent is useful in this traversal. It can surface related concepts, organize strands of a disciplinary debate, flag where the question is too broad or too narrow, and map terminological overlaps and divergences across subfields. Brainstorming about which theoretical tradition the idea engages, exploring which method family has addressed adjacent questions, and sketching possible conceptual frameworks — these are tasks where an agent contributes without overreaching.

The intellectual responsibility for the research question, however, belongs to the researcher. The ethical weight of a question in clinical psychology, the pedagogical consequence of a question in educational science, the contextual burden of a question in sociology — none of these can be determined by probabilistic text generation. A model can clarify a question's formulation. Which question is worth asking is determined by the researcher's domain knowledge and ethical commitment. When that line is crossed, the research question becomes, in practice, the model's question wearing the researcher's name.

The document to produce at this stage is a short research idea note. It should record: the problem statement, candidate conceptual frameworks, the intended audience and disciplinary home, initial source domains, the expected data type, and apparent ethical risks. This note does not need to be polished. It needs to exist, because it will later ground the ethics application, the methods section, and the AI contribution statement. Left unwritten, it becomes impossible to demonstrate when the AI was first engaged and what prior orientation guided that engagement.

## 3. From literature search to systematic workflow

Literature searching begins as exploration. The researcher learns the field's edges, tracks how key concepts have been named and disputed over time, identifies the debates that anchor the area, and finds where the settled questions end and the open ones begin. In this exploratory mode, the agent can be used freely: concept mapping, terminological discussion, initial source identification, and field orientation are all legitimate tasks.

At a certain point, searching must become systematic. Which databases were queried, which search strings were used, which language and date boundaries were applied, which records were included, and which were excluded on what criteria — none of this can remain tacit if the search is to support a publishable claim. Reproducible research requires that the protocol for gathering evidence be documented as rigorously as the evidence itself (Wilson et al., 2017).

Claude Code is capable at this stage: extracting bibliographic metadata, verifying DOIs, maintaining a source ledger, and separating database layers. Search logs, query strings, and inclusion and exclusion decisions should be saved to dedicated files. Those records form the methodological backbone of the literature section and, in journals requiring systematic review protocol, will be requested directly by peer reviewers.

One limit applies here as it does everywhere: the final authority over inclusion and exclusion decisions belongs to the researcher. Whether a source enters the synthesis depends on domain knowledge, the precise formulation of the research question, and methodological coherence. An agent cannot make that call on the researcher's behalf; it can record decisions already made, flag inconsistencies, and help complete missing metadata.

## 4. AI boundaries before the ethics committee

An ethics committee application is not paperwork completed after research has started — not in AI-assisted research. The tools through which data will be processed, the directories in which it will be stored, the timing of anonymization, and the materials the agent will never access are all design decisions that must be made before data collection begins.

When the research involves clinical data, interview transcripts, student writing, or field notes from small communities, the lifecycle moves immediately into a sensitive data protocol. Raw data and working data are separated. No data passes into an agent session before de-identification is complete. That rule does not yield to convenience. The researcher must explain to the ethics committee not only the consent form and participant protections but also which AI tools were used at which stages and how data security was maintained throughout.

The document produced at this stage is an ethics and data security note. It will later be absorbed into the ethics application, the methods section, and the AI contribution statement. Depending on the research type, it should specify: which data will never enter an agent session without de-identification, the choice between local storage and cloud processing, and any additional protocols triggered by data types that emerge during fieldwork. For researchers working within a pre-registration framework, this protocol must exist before analysis begins — not as a formality but as a substantive commitment, consistent with what Nosek et al. (2018) identified as the core logic of the preregistration revolution.

## 5. Data collection and data preparation

During data collection, the role of the AI should be actively circumscribed. Drafting survey items, organizing interview protocols, building a data dictionary, and setting up the project file structure are legitimate preparation tasks. Passing participant responses or raw field data directly to an agent session is a different matter — it becomes possible only after consent has been obtained, de-identification has been completed, and secure processing conditions have been confirmed.

Data preparation is the stage that receives the least attention and does the most damage when done carelessly. The reliability of analysis results is largely determined here. Decisions about missing data, exclusion criteria, variable transformations, codebook construction, and data dictionary finalization are the decisions hardest to revisit after the fact. Each one should be recorded at the moment it is made, with its rationale. Sandve et al. (2013) included the explicit documentation of every data transformation step among the ten rules for reproducible computational research — a standard that applies to qualitative coding schemes and scale transformations as equally as to numerical pipelines.

Open science planning enters here, not at the submission stage. The data-sharing plan, repository address, and file format choices are made while data are being collected, not after publication. The FAIR principles formulated by Wilkinson et al. (2016) — findable, accessible, interoperable, and reusable — provide the reference framework for these decisions. An agent can help build a FAIR-compliant file structure, populate metadata templates, and audit whether the documentation is complete. Which data will be shared, which will remain restricted, and under what conditions access will be granted are decisions that belong to the researcher and the institutional ethics protocol.

## 6. Analysis, pre-registration, and the decision log

Moving into analysis is not the act of running code. It is the act of committing in writing to which claim will be tested by which method. Without that commitment, confirmatory analysis and exploratory analysis merge — and the practice of generating hypotheses by looking at the data while presenting them as hypotheses tested independently of the data becomes possible without anyone noticing.

In agent-based analysis, the problem is sharper. An agent can rapidly propose alternative tests, produce visualizations, and draft interpretive text. Speed obscures exactly when and why each decision was taken. The discipline required here is either a formal pre-registration document or, at minimum, a local analysis plan written before the data are opened. The plan should record: the primary outcome variable, exclusion criteria, planned tests, accepted statistical threshold, and the boundary between confirmatory and exploratory analyses. Nosek et al. (2015) identified prior commitment as one of the structural prerequisites for an open research culture — not a bureaucratic requirement but the mechanism through which a finding can be distinguished from an artifact of search.

Every unplanned decision made during analysis enters a deviation log. If the agent proposes a test not in the plan and the researcher adopts it, the log records the test, the reason, and the label: exploratory. If a variable is dropped or a sub-sample is redefined, the same entry is made. Each undocumented change silently erodes the reproducibility of the manuscript. The agent can maintain this log, generate a deviation summary when analysis is complete, and format the summary for incorporation into the discussion section. The contextual justification for each change — why it was methodologically defensible — is written by the researcher.

## 7. Writing, submission, and peer review

The writing stage is where AI-assisted support becomes most visible. Building the IMRAD structure, producing a bilingual re-authoring, verifying DOIs, assessing journal fit, drafting the cover letter, and generating the AI contribution statement are all standard tasks at this stage. What the writing stage is not, however, is mere text production. It is the process of bringing to a readable and defensible form all the decisions, frameworks, and findings accumulated across the preceding stages.

This distinction matters. A model can produce fluent prose, but it cannot determine which finding the researcher chooses to foreground, which limitation is named with intellectual honesty, or which inference comes from the data rather than from interpretive desire. Those are the researcher's intellectual prerogative and must be fully represented in the AI disclosure. Publication processes are converging on requirements for greater transparency, with the role of generative AI in each component of a manuscript becoming a standard question (Nosek et al., 2015).

Peer review is not the end of the lifecycle; it is a new production round. When reviewer comments arrive, a traceability matrix is opened. Each comment is linked to a row. Each accepted or rejected revision is recorded with its location and rationale. The revised section is archived in a form comparable with the original. If the agent assisted in drafting any portion of the revision, the disclosure is updated to reflect current journal policy. As Belcher (2019) showed through systematic analysis of successful publication trajectories, academic publishing is a system, not a talent — and the reviewer response round is the most methodologically consequential node in that system. Traceability is what makes it navigable rather than arbitrary.

The pre-submission checklist includes: journal fit and scope, formatting and word count compliance, ethics approval number consistency, presence of the AI contribution statement, DOI-verified references, and working links to any open science components (data repository, analysis code, pre-registration record). This checklist can be managed through an agent. The final signature belongs to the researcher.

## 8. Presentation, public communication, and teaching

A piece of work does not end when the article is published. It is presented at conferences, discussed in courses, communicated to public audiences, and cited as a reference in student work. At this stage, the text type changes and ethical accountability changes form with it. A slide deck, a poster, a course reading, a blog post, and a social media thread all emerge from the same academic core; each addresses a different audience and a different interpretive frame.

The agent is capable in format conversion: adapting a long article for a teaching context, organizing key findings for a poster, restructuring a presentation sequence for a general audience. Those are tasks where the agent contributes without misrepresenting. Simplification, however, does not reduce epistemic responsibility. The obligation to discuss mental health topics without diagnosing, to include appropriate referrals in crisis-adjacent content, to avoid presenting an individual observation as a universal finding, and to preserve source fidelity applies regardless of the format.

Teaching introduces an additional layer of responsibility. Institutional policies on student AI use differ across universities and continue to evolve. The practices a researcher models for students should align with those policies and should help students understand what is permitted in their own context, what requires disclosure, and what remains their own intellectual work. Modeling careful, attributed, and documented AI use is itself a pedagogical act.

## 9. Archive, open science, and closure

The final stage of the lifecycle is the archive. The archive is not where a piece of work ends — it is where the next one begins. Source ledgers, analysis code, the data dictionary, supplementary materials, decision logs, deviation records, AI contribution statements, and the open science package are brought together here. Kitzes et al. (2018) demonstrated through detailed case studies that the reproducibility value of an archive in data-intensive research depends not only on the files stored but on the documentation of when and how those files were produced.

At this stage the researcher asks one question: if this study were opened five years from now, could anyone — including the researcher herself — understand what was done and why? If the answer is uncertain, then even a published article constitutes an incomplete archive. A well-constructed archive does not merely store files; it preserves the decision trail, the provenance of every source, and the record of where and how human oversight operated.

The FAIR principles take their most concrete form here: are the data deposited at a findable repository address, organized according to a metadata standard, stored in formats that can be opened without proprietary software, and accompanied by clearly stated reuse conditions? Wilson et al. (2014) formulated these requirements as foundational practical standards for scientific computing — standards that apply to the social scientist running qualitative content analysis as directly as to one running a Monte Carlo simulation.

Archive closure is also a project opening. The archival decisions of one project feed the design decisions of the next. Conceptual frameworks are reused and refined. Measurement instruments are updated in light of what worked. Data dictionaries are extended. Methodological explanations become more precise. This continuity is what builds a research program rather than a sequence of isolated outputs.

## 10. Skill routing and output standards

The practical counterpart to this booklet is the `/research-lifecycle-pipeline` skill. The skill determines the researcher's current stage, extracts the risk level specific to that stage, proposes the relevant skill list, and identifies which artifacts should be written to the archive at the session's close.

Every stage should produce a document. An idea note, a search log, an ethics and data security note, an analysis plan, a source ledger, an open science package, a reviewer response matrix, a presentation disclosure, or an archive closure record — which of these applies depends on the stage and research type. An undocumented stage is a stage that cannot later be reproduced or defended.

The scope of agent assistance also shifts across the cycle. In the idea stage, the agent is a thinking partner. In the literature stage, it is a source manager. In the ethics stage, it is a warning and documentation instrument. In the analysis stage, it is a computational collaborator — but not the decision-maker. In the writing stage, it is a language and format support — but it does not absorb intellectual responsibility. In the archive stage, it is an organization and verification tool.

This distribution is not arbitrary. At every stage, the boundary of what the agent can take on is as legible as the responsibility the human researcher must retain. Lifecycle discipline keeps that boundary visible by resurfacing it at each transition. It moves research away from heroic memory and individual vigilance as the primary safeguards, and toward a working order that is visible, auditable, and transferable.

---

## References

Citations are in APA 7 format. All DOI links were verified against Crossref on 2026-06-21. ISBNs for Belcher (2019) and Kitzes et al. (2018) are confirmed from publisher catalog records.

Belcher, W. L. (2019). *Writing your journal article in twelve weeks: A guide to academic publishing success* (2nd ed.). University of Chicago Press. ISBN 978-0-226-49991-8

Kitzes, J., Turek, D., & Deniz, F. (Eds.). (2018). *The practice of reproducible research: Case studies and lessons from the data-intensive sciences*. University of California Press. ISBN 978-0-520-29673-3

Munafò, M. R., Nosek, B. A., Bishop, D. V. M., Button, K. S., Chambers, C. D., Percie du Sert, N., Simonsohn, U., Wagenmakers, E.-J., Ware, J. J., & Ioannidis, J. P. A. (2017). A manifesto for reproducible science. *Nature Human Behaviour*, *1*(1), Article 0021. https://doi.org/10.1038/s41562-016-0021

Nosek, B. A., Alter, G., Banks, G. C., Borsboom, D., Bowman, S. D., Breckler, S. J., Buck, S., Chambers, C. D., Chin, G., Christensen, G., Contestabile, M., Dafoe, A., Eich, E., Freese, J., Glennerster, R., Goroff, D., Green, D. P., Hesse, B., Humphreys, M., … Yarkoni, T. (2015). Promoting an open research culture. *Science*, *348*(6242), 1422–1425. https://doi.org/10.1126/science.aab2374

Nosek, B. A., Ebersole, C. R., DeHaven, A. C., & Mellor, D. T. (2018). The preregistration revolution. *Proceedings of the National Academy of Sciences*, *115*(11), 2600–2606. https://doi.org/10.1073/pnas.1708274114

Sandve, G. K., Nekrutenko, A., Taylor, J., & Hovig, E. (2013). Ten simple rules for reproducible computational research. *PLoS Computational Biology*, *9*(10), e1003285. https://doi.org/10.1371/journal.pcbi.1003285

Wilkinson, M. D., Dumontier, M., Aalbersberg, I. J., Appleton, G., Axton, M., Baak, A., Blomberg, N., Boiten, J.-W., Bonino da Silva Santos, L., Bourne, P. E., Bouwman, J., Brookes, A. J., Clark, T., Crosas, M., Dillo, I., Dumon, O., Edmunds, S., Evelo, C. T., Finkers, R., … Mons, B. (2016). The FAIR guiding principles for scientific data management and stewardship. *Scientific Data*, *3*, Article 160018. https://doi.org/10.1038/sdata.2016.18

Wilson, G., Aruliah, D. A., Brown, C. T., Chue Hong, N. P., Davis, M., Guy, R. T., Haddock, S. H. D., Huff, K. D., Mitchell, I. M., Plumbley, M. D., Waugh, B., White, E. P., & Wilson, P. (2014). Best practices for scientific computing. *PLoS Biology*, *12*(1), e1001745. https://doi.org/10.1371/journal.pbio.1001745

Wilson, G., Bryan, J., Cranston, K., Kitzes, J., Nederbragt, L., & Teal, T. K. (2017). Good enough practices in scientific computing. *PLoS Computational Biology*, *13*(6), e1005510. https://doi.org/10.1371/journal.pcbi.1005510

---

**Booklet identifier.** `001-02-0001`
**Version.** `0.1.0`
**Date.** 2026-06-21
**License.** This booklet is licensed under CC BY-NC-SA 4.0. https://creativecommons.org/licenses/by-nc-sa/4.0/
**Approximate word count.** 3112 (English body text, measured with wc)
**Verified citations.** 9
**Fabricated citations.** 0
**Previous booklet.** [`001-01-0004`](../001-01-0004/en.md). CLAUDE.md and the Discipline of Standing Instructions
**Next booklet.** [`002-04-0001`](../../002-academic-access/002-04-0001/en.md). DergiPark, ULAKBIM TR Dizin, HEAL-Link, and Regional Indexing
