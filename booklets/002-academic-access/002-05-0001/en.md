---
title_en: "Systematic Reviews and Scoping Reviews, From Search to PRISMA Flow"
title_tr: "Sistematik Derleme ve Kapsam Derlemesi, Aramadan PRISMA Akışına"
booklet_id: "002-05-0001"
category: "002-academic-access"
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
verified_citations_count: 10
fabricated_citations_count: 0
disclosure_standard: "COPE 2023 + WAME 2023 + ICMJE 2024 + STM 2025 + EU AI Act 2024/1689 Art. 50 + ENAI"
translation_notes: "English re-authored from the finalized Turkish source (v0.1.0, 2026-06-21), not a literal translation. Methodological terminology standardised for an international audience. Content, argument structure, and section order follow the Turkish canon."
license:
  - "CC-BY-NC-SA-4.0 (prose)"
status: "release"
---

# Systematic Reviews and Scoping Reviews, From Search to PRISMA Flow

The previous booklet established the infrastructure for reaching academic literature reliably in Turkish, Greek, and English — DergiPark, ULAKBİM TR Dizin, HEAL-Link, the Council of Higher Education Thesis Center. Each of those access layers has value on its own. But in synthesis work, the harder problem is combining them into a single auditable workflow. This booklet picks up exactly there: what comes after access is secured.

Conducting a systematic review or a scoping review is not simply reading many sources. It is being able to show which question was asked, which sources were searched where, which records were excluded and why, and which decisions were made by whom. The distinction between the two review types is not a methodological footnote — choosing the wrong one at the outset shapes both the research question and the conclusions. Getting that choice right requires clarity before a single database is opened.

The central claim of this booklet is this: artificial intelligence can accelerate title and abstract screening, organise search logs, and classify exclusion reasons. But the researcher holds final authority over inclusion and exclusion decisions. The PRISMA flow is the researcher's accountability document, not the model's. What follows is a practical account of building that accountability chain from the first search string to the last included study.

## 1. The Difference Between Systematic and Scoping Reviews

A systematic review typically pursues a defined, narrow question with predetermined inclusion criteria. Its goal is usually to synthesise findings across studies, and sometimes to quantify them through meta-analysis. A scoping review serves a different purpose: it maps the breadth of a field, its concepts, its methodological variety, and the gaps that remain. Both demand systematic searching and transparent reporting. They are not interchangeable.

Failing to draw this line clearly at the start is a choice that costs later. When a field is still conceptually unsettled — when foundational definitions vary across traditions, or when the range of relevant methods is unclear — a scoping review is the more appropriate starting point. When the question is narrow, inclusion criteria can be set in advance, and studies are comparable along meaningful dimensions, a systematic review is the stronger design. Higgins and colleagues (2019) identify the pre-specification of methods as the most distinguishing feature of a systematic review: the protocol is written before the search begins, and the search is conducted within it.

Stating this choice explicitly in the methods section strengthens the work. A reader can see not only what was done but why this particular review type was preferred over the alternative. Claude Code can explain the distinction, lay out comparisons between the two types, and draft a rationale. What it cannot do is make the choice, because appropriateness depends on familiarity with established practice in the field, the realistic scope of available databases, and the researcher's own resources.

## 2. Structuring the Research Question

A synthesis question is different from everyday intellectual curiosity. It must be structured precisely enough to translate directly into a search string and a set of inclusion criteria. Several frameworks exist to support this.

For questions intersecting clinical or health contexts, PICO is the most widely applied: Population, Intervention, Comparison, Outcome. For qualitative and mixed-methods work, SPIDER offers more flexibility: Sample, Phenomenon of Interest, Design, Evaluation, Research type. For scoping reviews, PCC is the standard frame: Population, Concept, Context. Peters and colleagues (2020) set out in detail how PCC operates in JBI-aligned scoping reviews and how it shapes both the search and the eligibility criteria that follow.

At this stage Claude Code can take on concrete work: proposing question drafts, generating concept equivalents across languages, rewriting the same question according to different frameworks for comparison. But not every question the model proposes is actually researchable. The question must be evaluated against the realities of what databases cover, what literature exists in the relevant languages, and what is genuinely achievable within the project's time frame.

The practical output of this stage is a question framework document. It records the main question, any sub-questions, the language equivalents of key concepts, the population or context boundary, and the areas explicitly left outside scope. This document functions as an anchor: it keeps eligibility criteria from drifting as the search proceeds and provides a reference point if the team's interpretations diverge during screening.

## 3. Database Layers and Regional Search

No serious synthesis in the social sciences runs through Web of Science and Scopus alone. Both are important and broad. But for work carrying Turkish and Greek context, they are a necessary rather than sufficient starting point. Bramer and colleagues (2017), in a prospective exploratory study, showed empirically that single-database searches yield substantially lower recall than combinations — and that the optimal combination varies by discipline. Running only one or two databases leaves a retrievable portion of the relevant literature permanently invisible.

The implications for Turkish and Greek contexts are direct. Turkish-language literature requires DergiPark, ULAKBİM TR Dizin, and the Council of Higher Education Thesis Center as separate layers. Greek and internationally subscribed literature requires HEAL-Link and institutional access routes planned in advance. In bilingual or regionally situated topics, this layered approach is not optional — a study may be absent from international indexes while constituting a foundational theoretical or historical reference in its own field.

A separate search log must be maintained for each database: which query string, on which date, with which filters, returning how many records, how many of which were duplicates. These numbers cannot be reconstructed after the fact. They must be recorded as the search proceeds, because they form the numerical foundation of the PRISMA flow. Failing to log them is not a minor oversight; it is a gap that cannot be closed later without repeating the entire search.

## 4. The Search String Log

The search string is the backbone of a synthesis. A well-constructed string is not simply a list of keywords. It contains synonyms, spelling variants, cross-language equivalents, Boolean connectors, and syntax rules that differ from one database to the next.

A concrete example clarifies this. A researcher mapping Turkish and English literature on social anxiety in adolescents might construct a string along these lines:

```
("sosyal kaygı" OR "sosyal fobi" OR "sosyal anksiyete")
AND
("social anxiety" OR "social phobia" OR "social anxiety disorder")
AND
("ergen*" OR "adolescent*" OR "genç*" OR "youth")
```

The same query must then be adapted: Thesaurus terms in PsycINFO, MeSH terms in PubMed, title and abstract field codes in DergiPark. Claude Code can do real work here — comparing syntax rules across databases, suggesting Turkish and Greek concept equivalents, generating verification questions to test whether the string captures known relevant studies. McGowan and colleagues (2016) recommend that electronic search strategies be subject to peer review before a synthesis begins, precisely because string errors at this stage propagate into every subsequent step.

Failed search attempts belong in the log too. Which query returned too much noise, which artificially narrowed the field, which missed a known body of regional literature — all of this is methodological information. It demonstrates that the final string was not the first one tried but the result of an iterative calibration process. If a reviewer later asks why a particular source cluster was absent, the search log is where the answer lives.

## 5. Inclusion and Exclusion Criteria

Inclusion and exclusion criteria must be written before any records are examined. This rule is not merely about methodological rigour — it is about protecting the synthesis from selection bias. When criteria are set after records have been seen, there is a well-documented tendency to make decisions that favour sources supporting the emerging conclusions. Writing criteria in advance removes that pressure.

The criteria set should cover explicit categories: publication year range, included language or languages, study design (experimental only, or qualitative included), sample definition, minimum methodological standards, contextual boundary, and full-text accessibility requirements. Criteria that are too loose produce an unmanageable volume of records; criteria set too narrowly produce a dataset that misrepresents the field's actual breadth.

Claude Code can propose draft criteria, extract the criteria used in comparable syntheses, and check internal consistency across a draft criteria list. What it cannot do is determine whether those criteria are appropriate for that particular field and literature. A criterion the model marks as reasonable may systematically exclude regional literature or methodological traditions that matter to the research question. That judgment belongs to the researcher. Shamseer and colleagues (2015), in the PRISMA-P elaboration, show how pre-registration of eligibility criteria in a protocol document prevents criteria drift during the screening process — a problem that compounds when teams are large or when the search spans a long period.

Standard exclusion reason categories should be established and applied consistently: full text unavailable, wrong population, wrong outcome variable or concept, ineligible study design, duplicate record, language outside scope. These categories, defined in advance, make the PRISMA flow and supplementary files internally consistent and allow a reader to audit the screening decisions without ambiguity.

## 6. AI-Assisted Screening

At the title and abstract screening stage, artificial intelligence can deliver meaningful time savings. The difference between reading one thousand records by hand and focusing human attention on uncertain cases after AI-assisted pre-classification is substantial in large syntheses. The model can classify candidate records against the inclusion criteria, flag borderline cases, and draft exclusion reason codes.

But this classification is not a decision. It is a pre-screen. The distinction matters.

The most defensible workflow is two-layered. The model produces a candidate classification and flags uncertain records. A human researcher reviews this classification and does not automatically exclude flagged cases: they are carried forward to full-text review or sent to a second screener. No exclusion recommended by the model is acted on without the researcher's explicit confirmation.

Model error is more likely with regional and multilingual records. A concept used in a Turkish title may not map cleanly onto its English-language counterpart in the literature. A Greek term may carry theoretical weight that did not survive translation into the English abstract. For this reason, the model's exclusion suggestions must be checked against local language and field knowledge. Ouzzani and colleagues (2016), describing the Rayyan application, demonstrate how a double-blind review design can be embedded in screening tools. AI-assisted screening should follow the same principle: the model's output is a starting point, not a verdict.

## 7. Dual Screeners and the Disagreement Protocol

In the systematic review tradition, a dual-screener arrangement is the primary safeguard for reliability. Two researchers assess the same records independently. Disagreements are discussed and resolved. When discussion does not resolve the disagreement, a third reviewer adjudicates. Artificial intelligence is not a third reviewer in this arrangement. At most it can function as an auxiliary classifier or pre-screening assistant.

The disagreement protocol must be written before screening begins. Which situations escalate to full-text review, which lead to a clear exclusion decision, which go to a third screener — these procedures must be established and documented in advance. When in doubt, moving a record forward rather than excluding it early is the safer operating principle. Excluding a potentially eligible study at the abstract stage is a costlier error than carrying a potentially ineligible one forward to full-text review, because the first type of mistake cannot be detected or corrected during the synthesis.

This protocol must be reported in the published work. A reader should be able to see not only how many records were excluded but how the decisions were made. Levac and colleagues (2010) address screener reliability in scoping reviews directly, arguing that the transparency of the process is central both to methodological assessment and to appropriate interpretation of the findings. A synthesis that cannot describe its decision-making process is not fully auditable.

## 8. Preparing the PRISMA Flow

The PRISMA flow diagram is not a decorative figure appended at the end of a manuscript. It is the decision ledger of the synthesis. How many records were identified across all databases, how many duplicates were removed, how many records were screened at title and abstract stage, how many full texts were assessed, how many studies were ultimately included — and at each stage, how many were excluded and why. Every number must trace back to the search log and the screening records. Page and colleagues (2021), in the PRISMA 2020 statement, specify exactly which quantities the flow diagram should report and how the different phases of screening correspond to distinct counts.

Claude Code can extract these numbers from screening tables, flag duplicate counts, and generate a draft summary for the flow. But numerical consistency must be verified by a human. A record counted twice, an exclusion reason placed in the wrong category, or a duplicate overlooked across databases damages the synthesis's credibility in a way that cannot easily be explained away after publication.

The flow diagram is not drawn at the end from memory. It is populated throughout the process. The most reliable PRISMA diagram is the one updated at each step as searching and screening proceed, not a retrospective reconstruction assembled when the manuscript is being written. Maintaining this means updating the search log and screening tables at the close of each working session rather than deferring the accounting to later.

Tricco and colleagues (2018), in PRISMA-ScR, define the flow elements specific to scoping review reporting. The flow diagram for a scoping review may differ in structure from the one used for a systematic review, with different columns and phases. Identifying the correct reporting template for the review type chosen is therefore part of the preparation, not an afterthought.

## 9. Source Passport and Citation Verification

In synthesis work, a source passport — a record of provenance for each included and excluded source — becomes a methodological necessity rather than an optional practice. Each record should carry: the database in which it was found, the search query that retrieved it, the date of retrieval, whether the DOI or alternative persistent identifier has been verified, which screening stage it reached, and the exclusion reason if it did not proceed.

DOI verification is the central security layer when AI-assisted citation generation is part of the workflow. A model can generate a bibliographic record that looks correct but points to a non-existent article or to a different paper entirely. For this reason, no source proposed by the model enters the reference list without independent verification through Crossref.

```bash
curl -LH "Accept: application/x-bibtex" https://doi.org/10.1136/bmj.n71
```

This command retrieves the BibTeX record for the PRISMA 2020 article directly from Crossref. The same logic applies to every record in the synthesis. The verified citation is entered into the source passport alongside the record's metadata. When no DOI exists, an ISBN, institutional repository URL, thesis center record, or publisher page serves as the secondary verification point.

The source passport covers not only included studies but the full trail of excluded records. This trail is what makes the synthesis reproducible: a third researcher, working from the same question, the same criteria, and the same record identifiers, should be able to evaluate the screening decisions independently. That capacity for independent audit is the strongest evidence that the synthesis was conducted with integrity.

## 10. Skill Protocol and Output Package

The working implementation of this booklet is the `/prisma-scoping-review-pipeline` skill. The skill generates the question framework, search string log, database layer map, screening table, exclusion reason codes, PRISMA count summary, and AI contribution disclosure as a coordinated package. Each component is saved to a separate file and becomes part of the research archive.

The output package consists of the following files. `review-question.md` holds the main question, sub-questions, and cross-language concept equivalents. `search-log.md` records each database search: the query string, date, filters applied, number of records returned, and duplicate count. `database-layer-map.md` shows which source belongs to which access layer and how it was reached. `screening-table.csv` classifies each title-and-abstract record against the eligibility criteria. `exclusion-reasons.csv` tracks exclusion decisions using the pre-established standard codes. `prisma-counts.md` contains the numerical summary for the flow diagram. `source-passport-ledger.md` records the DOI verification status of every record in the synthesis. `ai-disclosure-note.md` documents at which stages the model contributed and to what degree.

When these files exist together, a synthesis is no longer only a written text. It is an auditable, reproducible, and archivable research object. Whether a colleague can follow the same trail and reach the same screening decisions is the clearest test of whether the synthesis was conducted with the rigour that review methodology demands.

## References

Citations are in APA 7 format. All DOIs were independently verified against Crossref. Institutional URLs were confirmed accessible as of 2026-06-21.

Arksey, H., & O'Malley, L. (2005). Scoping studies: Towards a methodological framework. *International Journal of Social Research Methodology*, *8*(1), 19–32. https://doi.org/10.1080/1364557032000119616

Bramer, W. M., Rethlefsen, M. L., Kleijnen, J., & Franco, O. H. (2017). Optimal database combinations for literature searches in systematic reviews: A prospective exploratory study. *Systematic Reviews*, *6*(1), Article 245. https://doi.org/10.1186/s13643-017-0644-y

Higgins, J. P. T., Thomas, J., Chandler, J., Cumpston, M., Li, T., Page, M. J., & Welch, V. A. (Eds.). (2019). *Cochrane handbook for systematic reviews of interventions* (2nd ed.). Wiley. https://doi.org/10.1002/9781119536604

Levac, D., Colquhoun, H., & O'Brien, K. K. (2010). Scoping studies: Advancing the methodology. *Implementation Science*, *5*, Article 69. https://doi.org/10.1186/1748-5908-5-69

McGowan, J., Sampson, M., Salzwedel, D. M., Cogo, E., Foerster, V., & Lefebvre, C. (2016). PRESS peer review of electronic search strategies: 2015 guideline statement. *Journal of Clinical Epidemiology*, *75*, 40–46. https://doi.org/10.1016/j.jclinepi.2016.01.021

Ouzzani, M., Hammady, H., Fedorowicz, Z., & Elmagarmid, A. (2016). Rayyan: A web and mobile app for systematic reviews. *Systematic Reviews*, *5*, Article 210. https://doi.org/10.1186/s13643-016-0384-4

Page, M. J., McKenzie, J. E., Bossuyt, P. M., Boutron, I., Hoffmann, T. C., Mulrow, C. D., Shamseer, L., Tetzlaff, J. M., Akl, E. A., Brennan, S. E., Chou, R., Glanville, J., Grimshaw, J. M., Hróbjartsson, A., Lalu, M. M., Li, T., Loder, E. W., Mayo-Wilson, E., McDonald, S., … Moher, D. (2021). The PRISMA 2020 statement: An updated guideline for reporting systematic reviews. *BMJ*, *372*, n71. https://doi.org/10.1136/bmj.n71

Peters, M. D. J., Marnie, C., Tricco, A. C., Pollock, D., Munn, Z., Alexander, L., McInerney, P., Godfrey, C. M., & Khalil, H. (2020). Updated methodological guidance for the conduct of scoping reviews. *JBI Evidence Synthesis*, *18*(10), 2119–2126. https://doi.org/10.11124/JBIES-20-00167

Shamseer, L., Moher, D., Clarke, M., Ghersi, D., Liberati, A., Petticrew, M., Shekelle, P., & Stewart, L. A. (2015). Preferred reporting items for systematic review and meta-analysis protocols (PRISMA-P) 2015: Elaboration and explanation. *BMJ*, *349*, g7647. https://doi.org/10.1136/bmj.g7647

Tricco, A. C., Lillie, E., Zarin, W., O'Brien, K. K., Colquhoun, H., Levac, D., Moher, D., Peters, M. D. J., Horsley, T., Weeks, L., Hempel, S., Akl, E. A., Chang, C., McGowan, J., Stewart, L., Hartling, L., Aldcroft, A., Wilson, M. G., Garritty, C., … Straus, S. E. (2018). PRISMA extension for scoping reviews (PRISMA-ScR): Checklist and explanation. *Annals of Internal Medicine*, *169*(7), 467–473. https://doi.org/10.7326/M18-0850

---

**Booklet ID.** `002-05-0001`
**Version.** `0.1.0`
**Date.** 2026-06-21
**License.** This booklet is licensed under CC BY-NC-SA 4.0. https://creativecommons.org/licenses/by-nc-sa/4.0/
**Word count (approx.).** 3164 (English body text, measured with wc)
**Verified citations.** 10
**Hallucinated citations.** 0
**Previous booklet.** [`002-04-0001`](../002-04-0001/en.md). DergiPark, ULAKBIM TR Dizin, HEAL-Link, and Regional Indexing
**Next booklet.** [`003-01-0001`](../../003-memory-system/003-01-0001/en.md). Memory as Vault. A First Principles Introduction
