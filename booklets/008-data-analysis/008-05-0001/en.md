---
title_en: "Research Protocol and Preregistration, Deciding Before Analysis"
title_tr: "Araştırma Protokolü ve Ön Kayıt, Analizden Önce Karar Vermek"
booklet_id: "008-05-0001"
category: "008-data-analysis"
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
    role: "drafting, verification, citation lookup, bilingual authoring"
    interaction_mode: "interactive console"
ai_contribution_level: "substantial-drafting"
human_review: "complete"
human_review_date: "2026-06-21"
verified_citations_count: 10
fabricated_citations_count: 0
disclosure_standard: "COPE 2023 + WAME 2023 + ICMJE 2024 + STM 2025 + EU AI Act 2024/1689 Art. 50 + ENAI"
translation_notes: "Re-authored in English from the finalized Turkish source (tr.md v0.1.0) as the canon for this revision; not a literal translation. Argument, section structure, and bibliographic set are identical across both languages; phrasing is native to each."
license:
  - "CC-BY-NC-SA-4.0 (prose)"
status: "release"
---

# Research Protocol and Preregistration, Deciding Before Analysis

Deciding before analysis is the discipline most consistently deferred in social science research. Recording the hypothesis before the data arrive. Writing the analysis plan before the model runs. Reporting the primary outcome as the variable designated at the outset, not the variable that turned out most interesting. None of these steps restrict the researcher's intellectual freedom. What they do is make visible the risk of presenting decisions taken after looking at the data as though they had been taken before. Agent-based analysis intensifies that risk: a model can try dozens of specifications in seconds, surface the cleanest-looking result, and widen analytical degrees of freedom without leaving any decision in the record. This booklet brings research protocol and preregistration discipline into the agentic workflow — from a local protocol file to open preregistration platforms, from the hypothesis-exploration distinction to the deviation log, from the analysis plan to its transfer into the methods section. The frame connects thinking-before-analysis to a traceable, file-level workflow.

## 1. The difference between a protocol and a methods section

A methods section is written after the study is complete. It narrates the past. A protocol is written before the study begins. It commits to a plan. The gap between these two documents is easy to overlook in academic writing, because a polished methods section gives no indication of when the decisions it describes were actually made.

In agent-based analysis that gap acquires sharper consequences. The model generates proposals, writes code, and tries alternative specifications. When the researcher accepts those proposals, the boundary between decisions made before the data and decisions made after blurs. A protocol exists precisely to remove that blur: it is the document that records what was planned, when it was planned, and who committed to it. Wagenmakers et al. (2012) argue that the credibility of confirmatory research rests on exactly this kind of record — that fixing the hypothesis and the analysis plan before the data is not merely a procedural nicety but a condition of valid statistical inference. Even a local protocol file, without any formal preregistration platform, fulfills this function.

The methods section follows from the protocol; it does not replace it. The protocol shows what was planned. The methods section reports what was done. When they coincide, that agreement is a scientific strength. When they diverge, the deviations must be recorded and justified.

## 2. The boundary between a hypothesis and an exploratory question

A hypothesis is a confirmatory claim: a testable, directional relationship or effect predicted before looking at the data. An exploratory question is an open inquiry directed at understanding a domain without prior specification of the expected pattern. Both are legitimate. Both carry scientific value. But they cannot substitute for each other, and they cannot be reported in the same analysis under the same status.

Kerr (1998) named the erasure of this boundary HARKing — Hypothesizing After the Results are Known. HARKing rarely begins as deliberate fraud. The pattern emerges because a finding that surfaced during analysis can, without conscious awareness, be rewritten as a prediction the researcher had held all along. In agent-based analysis the risk compounds: the model can deliver answers to questions the researcher had not yet asked, and those answers can be visually compelling. Framing them as pre-specified hypotheses is easy, and the record offers no resistance.

A sound workflow separates these two categories in writing before any data are examined. Which questions are confirmatory and which are exploratory is declared in the protocol. Patterns the agent discovers while running belong to the exploratory column; they do not replace the confirmatory result. Open Science Collaboration (2015), in a systematic effort to replicate one hundred psychological studies, showed that a substantial portion of original findings could not be reproduced, and identified the systematic blurring of the hypothesis-exploration boundary as one of the structural conditions underlying that failure.

## 3. Specifying primary and secondary outcomes in advance

The primary outcome variable carries the central claim of a study. Secondary outcomes provide supporting and complementary information. When this distinction is not written into the analysis plan before the data are examined, the variable that happens to reach the strongest result can be retrospectively positioned as the primary outcome. This is selective reporting, and it inflates false-positive rates in ways that are statistically indistinguishable from a genuine finding.

Simmons et al. (2011) demonstrated experimentally that undisclosed researcher degrees of freedom — choices about which dependent variable to report, which observations to exclude, how large a sample to collect, and which covariates to include — can accumulate to push a genuinely null result below the five-percent significance threshold. Wicherts et al. (2016) mapped this problem across every phase of a study, from planning through reporting, showing that each stage carries its own set of degrees of freedom; their checklist recommends that researchers record in writing, before data collection, which variables are designated primary.

In agent-based analysis this risk is particularly acute. The model can calculate relationships among variables the researcher had not considered, generate tables, and place prominent results in front of the analyst. Without a prior plan, there is no record of which variable was primary from the start. The existence of the plan closes that gap: the primary outcome is written before the model runs, and whatever the model subsequently surfaces is labeled secondary or exploratory.

## 4. Writing inclusion and exclusion criteria before analysis

Which participants will enter the analysis, which will be excluded, how missing data will be handled, and which criterion will govern the treatment of outliers — these decisions form the methodological spine of a study. Writing them before examining the data is a basic requirement of both reproducibility and research integrity.

Exclusion decisions taken after looking at the data can be shaped, without deliberate intent, by pressure toward statistically significant results. The researcher may find a methodologically sound rationale for a given exclusion. But whether that rationale was formed before or after seeing the data cannot be established from the outside. A protocol solves this observability problem: it records the timing and sequence of decisions, making it possible to verify that exclusion criteria were set independently of the results they produce.

In an agentic workflow exclusion decisions can become especially fluid. The model can calculate, in seconds, how different exclusion rules produce different outcomes. If the researcher selects the rule that yields the cleanest result and that selection goes unrecorded, the workflow has produced selective reporting without any single dishonest step. Pre-specifying the criteria in the protocol eliminates this risk. If a change becomes necessary — a measurement instrument behaves unexpectedly, a data quality issue is discovered — the change is entered in the deviation log with its rationale.

## 5. Specifying the analysis plan in advance

The analysis plan states which statistical model will be run, with which variables, under which assumption checks, and in which order. The plan derives from the research question and the theoretical framework. It does not derive from an iterative search for the specification that produces the most favorable result after the data are in view.

Gelman and Loken (2014) showed that researchers who believe they are testing a single hypothesis are in fact navigating a garden of forking paths: a chain of data-dependent choices, each individually defensible, that together generate an invisible tree of multiple comparisons. Munafò et al. (2017) position advance fixation of the analysis plan as one of the structural foundations of reproducible science, arguing that transparent reporting alone is insufficient without it — what is reported cannot be evaluated without knowing what would have been reported had the results come out differently.

An AI agent can contribute to the planning stage. It can list assumption checks for a candidate test, compare the theoretical rationale for alternative modeling approaches, and draft a structured analysis plan for the researcher's review. What remains with the researcher is the theoretical defense and the statistical justification. The agent can propose a test; whether that test's assumptions hold for this sample, and whether the field's conventions warrant this specification, is the researcher's determination. Once the plan is established, the agent executes it. It does not generate results that replace the plan.

## 6. The deviation log: recording departures from the plan

Departing from a protocol is not always an error. Data can contain unexpected structures; an assumption check can show that the planned model is inapplicable; a measurement can behave differently from the design's expectation. Science is not closed to such reassessments. The problem is not deviation but undisclosed deviation.

A deviation log is the document opened specifically to manage this risk. For each departure from the plan, it records the date, the rationale, who made the decision, and the expected effect on the analysis. The methods section the reader encounters then reflects not only the original plan but also how and why it was modified.

Van 't Veer and Giner-Sorolla (2016), developing a preregistration template for social psychology research, treat transparent reporting of deviations as a required component, not an optional disclosure. They show that documenting a departure from the plan does not weaken a study — it is a positive indicator of scientific integrity, because it demonstrates that the researcher maintained an auditable record of the decision sequence. In an agentic workflow this principle carries extra weight: the model can make data-dependent decisions automatically, and the researcher may not notice that the plan has shifted. The deviation log is the only mechanism that makes those shifts visible.

## 7. The consultation boundary in AI-assisted analysis

An AI agent can occupy three distinct roles in a research workflow: technical executor, methodological consultant, and analytic decision-maker. The first is fully delegable. The second is useful within defined limits. The third belongs to the researcher.

Technical execution is delegable: writing code, formatting tables, producing figures, running assumption checks, re-running the analysis from scratch in a clean session. Methodological consultation is useful when its scope is bounded: the agent can enumerate the assumptions of a candidate test, summarize how alternative approaches are used in the literature, or draft a structured checklist for the researcher's review. But those suggestions pass through the researcher's independent judgment before adoption.

Analytic decision-making is not delegable. Which test fits the structure of this data, which exclusion is theoretically justified for this sample, what an effect size of this magnitude means in this field — these determinations stay with the researcher. The agent can propose; it cannot validate its own proposals. Chambers (2013) developed the registered report model precisely to institutionalize this distinction: by binding the analysis plan to the acceptance decision before data collection begins, the format closes the pathway through which post-hoc decisions enter the methods section unchallenged.

## 8. Preregistration platforms and local protocol alternatives

Preregistration is the practice of fixing analytic decisions in a publicly accessible form — or at minimum in a verifiable record — before the data are examined. OSF (Open Science Framework) and AsPredicted are the platforms most widely used for this purpose. OSF allows time-stamped preregistration documents to be published immediately or released after an embargo period. AsPredicted offers a shorter, structured form that covers the essential decisions in a compact format.

Nosek et al. (2018) argue that the spread of preregistration provides a structural solution to three distinct problems: it makes researcher degrees of freedom visible; it separates confirmatory from exploratory analysis before the data can influence the analyst's choices; and it addresses publication bias by creating a record of what was planned regardless of what was found. Munafò et al. (2017) place preregistration among five core reforms for reproducible science, arguing that it works in combination with transparent reporting, open data, and methods sharing — not as a standalone intervention.

In studies involving sensitive data, full public preregistration may not always be feasible because of institutional constraints or participant confidentiality obligations. In those cases, an institutional ethics committee file, a research team archive, or a time-stamped local protocol file offers a functional alternative. What matters is not the platform but the fixation of decisions before analysis, and the existence of a record that makes that fixation verifiable.

## 9. Transferring the protocol to the methods section

When the study is complete, the protocol provides the skeleton of the methods section. The transfer, however, is not a copy-paste. The methods section must clearly distinguish three layers: the planned analysis, deviations from the plan, and exploratory supplementary analyses.

The planned analysis covers the confirmatory work executed as specified from the outset. Deviations are reported with their rationales, grounded in the deviation log. Exploratory analyses are labeled explicitly as such — not as confirmation of additional hypotheses but as hypothesis-generating work conducted to inform future research.

This layered transparency serves the reader. A reader who knows which result is confirmatory, which is exploratory, and where and why the plan was modified can evaluate the scientific weight of each finding with much greater accuracy. Van 't Veer and Giner-Sorolla (2016) show that this approach strengthens rather than weakens a paper in peer review: a researcher who left a verifiable decision trail before examining the data is in a stronger position to defend the analysis than one who cannot establish when the decisions were made.

## 10. Skill outputs: /preregistration-analysis-plan-ledger

The `/preregistration-analysis-plan-ledger` skill connects the workflow described in this booklet to a file infrastructure. It produces four components.

The first is a preregistration draft: a structured template covering the research question, hypotheses, primary and secondary outcome variables, inclusion and exclusion criteria, and platform selection for formal preregistration.

The second is an analysis plan: a Markdown file specifying which statistical model will be run, which variables it will use, which assumption checks will be performed, and what random seed is fixed. This file is passed to the agent as its instruction set. Whatever the agent proposes during execution does not replace this plan.

The third is a deviation log template: a tracking document with fields for date, rationale, decision-maker, and estimated impact for each departure from the plan.

The fourth is a methods-section transfer summary: a draft showing how the planned analysis, deviations, and exploratory analyses will be reported in separate, clearly labeled passages in the methods section.

The skill makes deciding-before-analysis not a habit to be remembered but a traceable, file-level workflow built into the agentic research process from the start.

## References

Citations are in APA 7 format. Each DOI was independently verified against Crossref on 2026-06-21.

Chambers, C. D. (2013). Registered reports: A new publishing initiative at Cortex. *Cortex*, *49*(3), 609–610. https://doi.org/10.1016/j.cortex.2012.12.016

Gelman, A., & Loken, E. (2014). The statistical crisis in science. *American Scientist*, *102*(6), 460. https://doi.org/10.1511/2014.111.460

Kerr, N. L. (1998). HARKing: Hypothesizing after the results are known. *Personality and Social Psychology Review*, *2*(3), 196–217. https://doi.org/10.1207/s15327957pspr0203_4

Munafò, M. R., Nosek, B. A., Bishop, D. V. M., Button, K. S., Chambers, C. D., Percie du Sert, N., Simonsohn, U., Wagenmakers, E.-J., Ware, J. J., & Ioannidis, J. P. A. (2017). A manifesto for reproducible science. *Nature Human Behaviour*, *1*(1), Article 0021. https://doi.org/10.1038/s41562-016-0021

Nosek, B. A., Ebersole, C. R., DeHaven, A. C., & Mellor, D. T. (2018). The preregistration revolution. *Proceedings of the National Academy of Sciences*, *115*(11), 2600–2606. https://doi.org/10.1073/pnas.1708274114

Open Science Collaboration. (2015). Estimating the reproducibility of psychological science. *Science*, *349*(6251), Article aac4716. https://doi.org/10.1126/science.aac4716

Simmons, J. P., Nelson, L. D., & Simonsohn, U. (2011). False-positive psychology: Undisclosed flexibility in data collection and analysis allows presenting anything as significant. *Psychological Science*, *22*(11), 1359–1366. https://doi.org/10.1177/0956797611417632

van 't Veer, A. E., & Giner-Sorolla, R. (2016). Pre-registration in social psychology: A discussion and suggested template. *Journal of Experimental Social Psychology*, *67*, 2–12. https://doi.org/10.1016/j.jesp.2016.03.004

Wagenmakers, E.-J., Wetzels, R., Borsboom, D., van der Maas, H. L. J., & Kievit, R. A. (2012). An agenda for purely confirmatory research. *Perspectives on Psychological Science*, *7*(6), 632–638. https://doi.org/10.1177/1745691612463078

Wicherts, J. M., Veldkamp, C. L. S., Augusteijn, H. E. M., Bakker, M., van Aert, R. C. M., & van Assen, M. A. L. M. (2016). Degrees of freedom in planning, running, analyzing, and reporting psychological studies: A checklist to avoid p-hacking. *Frontiers in Psychology*, *7*, Article 1832. https://doi.org/10.3389/fpsyg.2016.01832

---

**Booklet identifier.** `008-05-0001`
**Version.** `0.1.0`
**Date.** 2026-06-21
**License.** This booklet is licensed under CC BY-NC-SA 4.0. https://creativecommons.org/licenses/by-nc-sa/4.0/
**Approximate word count.** 2398 (English body text, measured with wc)
**Verified citations.** 10
**Fabricated citations.** 0
**Previous booklet.** [`008-04-0001`](../008-04-0001/en.md). Preparing Sensitive Data, Anonymization, Masking, and Local Preprocessing
**Next booklet.** [`009-01-0001`](../../009-ethics-irb/009-01-0001/en.md). Ethics in AI-Assisted Research, From Principle to Behavior
