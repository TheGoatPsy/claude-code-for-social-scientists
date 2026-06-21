---
title_en: "Reproducible Quantitative Workflows"
title_tr: "Yeniden Üretilebilir Nicel İş Akışları"
booklet_id: "008-01-0001"
category: "008-data-analysis"
language: "en"
version: "0.2.0"
date_published: "2026-05-29"
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
    model_dated: null  # no dated identifier published by Anthropic for Opus 4.8 as of 2026-05-29
    role: "drafting, verification, citation lookup, bilingual authoring"
    interaction_mode: "interactive console"
ai_contribution_level: "substantial-drafting"
human_review: "complete"
human_review_date: "2026-06-21"
verified_citations_count: 11
fabricated_citations_count: 0
disclosure_standard: "COPE 2023 + WAME 2023 + ICMJE 2024 + STM 2025 + EU AI Act 2024/1689 Art. 50 + ENAI"
translation_notes: "Re-authored in English from the finalized Turkish source (tr.md v0.2.0) as the canon for this revision; not a literal translation. Argument, section structure, and bibliographic set are identical across both languages; phrasing is native to each."
license:
  - "CC-BY-NC-SA-4.0 (prose)"
status: "release"
---

# Reproducible Quantitative Workflows

This booklet focuses on one of the tasks the social scientist most often performs with a coding agent: quantitative data analysis. Earlier booklets addressed what the tool is, how it is installed, which standing instructions govern it, and how it is used in academic writing. The question here is the analytic workflow itself. When a dataset, a research question, and an agent share the same working directory, the researcher's first obligation is not speed but reproducibility.

Anthropic's 2026 survey of 1,260 quantitative social scientists in the United States and Canada found that the majority of coding-agent users reached for the tool to generate code, and most often to analyze quantitative data (Lyttelton et al., 2026). This report is not a peer-reviewed publication; it was commissioned by Anthropic. The publisher of the report is therefore also the developer of the technology under study — a conflict of interest that must be noted explicitly. Even so, the finding is consistent with independent research showing that AI assistance concentrates precisely where tasks are structured, repetitive, and high in volume (Ziems et al., 2024).

The central claim of this booklet is as follows. Agent-based analysis can deliver real efficiency gains in quantitative social science research. Those gains carry academic value only when they are accompanied by a specification log, a fixed random seed, versioned data, a captured computational environment, human oversight, and honest disclosure. Without those elements, speed erodes rather than strengthens reproducibility.

## 1. The Hard Problem of Agentic Analysis

An agent can take a dataset and a research idea, write the analysis code, run it, interpret the output, and iterate on its own proposals. This capacity can reduce the time a researcher spends on execution. It can also make the intermediate decisions that shaped the analysis invisible. In quantitative work the problem is rarely just incorrect code. The deeper problem is that the path to a result that looks correct remains unrecorded.

In computational research, reproducibility means that the same data yields the same result when the process is repeated (Peng, 2011). That definition becomes more pressing under agentic analysis. An agent can try dozens of variable codings, model specifications, exclusion criteria, and table-formatting steps in seconds. If the researcher does not record which steps were tried, which one was selected, and why, the scientific standing of the result weakens.

Consider a concrete scenario. A social psychologist studying implicit bias runs a regression on a survey dataset. The agent makes several choices: a variable coding here, an exclusion criterion there, a selection between two model specifications. The result looks clean — a tidy table, plausible p-values, fluent prose. Twelve months later a co-author cannot reproduce it. The problem is not the agent's competence. It is the absence of a decision record.

Sandve et al. (2013) establish that reproducible computational research requires every step of a process to be recorded and, where possible, automated. Wilson et al. (2017) carry that principle into practical scientific computing, emphasizing version control, environment capture, and automated data processing pipelines. Agentic analysis does not reduce the need for this discipline. It makes it more visible, because the convenience of arriving at a result in seconds crowds out the habit of recording how one arrived there.

## 2. What Reproducible Means When an Agent Does the Work

Preserving only the output of an analysis is not sufficient for reproducibility. The path that produced the output must also be fixed. In an agentic workflow that path consists of several components, each of which must be recorded.

The instruction given to the agent is the methodological text of the analysis. It specifies which variables are used, which exclusion criteria are applied, which model is preferred, and what output is expected. The model and version must also be logged, because the same prompt can produce different code on a different model or version. The data version must be pinned — with a checksum or tag — so that the exact snapshot used is never ambiguous. A random seed must be written down at every step that involves splitting, sampling, or bootstrapping; without one, those steps return different results on each run. Package versions must be frozen so that the computational environment remains reproducible even when code is unchanged.

These components connect to two patterns this guide has already introduced. `CLAUDE.md` is the standing instruction file that documents the model, its operational limits, and the instruction set governing the AI component of the analysis. The memory-as-archive pattern — the practice this guide uses for treating a persistent project folder as a traceable record of research decisions — keeps prompts, data passports, intermediate choices, and output logs organized across sessions. These two patterns are not established academic standards; they are the practitioner frameworks this guide has developed for working researchers. Together they convert agentic analysis from a one-off operation into a traceable workflow.

## 3. The Garden of Forking Paths, Now Automated

A dataset usually admits more than one defensible analytic path. Which variables to exclude, which transformation to apply, which subgroup to analyze, which model specification to use — each choice is arguable, and each makes a different result possible. Gelman and Loken (2014) call this the garden of forking paths. The researcher believes a single hypothesis is being tested while data-dependent decisions generate an invisible tree of multiple comparisons.

Simmons et al. (2011) demonstrate experimentally that researcher degrees of freedom, when left undisclosed, can make virtually any result appear statistically significant. Agentic analysis amplifies that risk in scale. An agent does not tire, does not pause, does not object. It can try, in seconds, the alternatives a researcher would need hours to explore, and it can present the cleanest-looking result without flagging that others were tried. Even without any ill intent, the result — when undocumented — is selective reporting.

The Lyttelton et al. (2026) survey records that respondents feared exactly this: that AI might worsen selective reporting and encourage risk-averse, incremental research. That the report is grey literature and Anthropic-commissioned should be kept in mind. Nevertheless, the concern itself is methodologically serious. Agentic speed can take a vulnerability that already existed in quantitative research and amplify it invisibly.

## 4. The Preregistration Mindset and the Specification Log

One of the strongest antidotes to this risk is the preregistration mindset. Preregistration is the act of writing analytic decisions on paper before looking at the data — or, in the agentic context, at least before running the agent. Nosek et al. (2018) argue that preregistration brings researcher degrees of freedom under visibility by separating confirmatory analysis from exploratory analysis before the data can influence the analyst's choices. Munafò et al. (2017) position preregistration and transparent reporting among the structural foundations of a robust scientific enterprise.

This booklet's practical recommendation is the specification log: a plain-text or Markdown file written before the agent runs. It records the planned analysis, the primary hypothesis, the variables to be used, the exclusion criteria, the model specification, and the random seed. If the agent tries alternative specifications during exploration, those are labeled as exploratory; they do not replace the confirmatory result. Every deviation from the plan is entered in the log with its rationale.

The analytic richness the agent produces then becomes not a hidden fishing expedition but an openly documented sensitivity analysis. That transparency does not weaken the paper. It makes the paper defensible in front of reviewers.

## 5. The Finder Is Never the Grader, Applied to Statistics

The recurring principle of this guide is that the tool that produces a finding cannot be the authority that confirms it. In statistics this principle matters twice over. An agent interpreting the output of a test can misdescribe the sign of a coefficient, the significance threshold, a confidence interval, or an effect size. For this reason the agent's interpretation must always be verified independently against the raw output. The authoritative record is the number in the table, not the agent's narration of it.

The reason for this warning lies in the structure of the model. Large language models can generate statistically plausible text without genuine understanding (Bender et al., 2021). The text they produce may, at the epistemic level, be indifferent to the distinction between seeming true and being true (Hicks et al., 2024). A fluent summary of a regression table does not entail that the table says what the summary says.

The researcher must therefore read the number directly. The agent's interpretation should be treated as a draft awaiting verification against the raw output. Without structural discipline, agentic analysis cannot be trusted. With it, the agent can become a reliable component of a reproducible workflow.

## 6. Delegate Procedure, Not Judgment

The line between what can be delegated to an agent and what cannot must be kept clear. Delegable tasks are those that are repetitive and procedural: loading the data, transforming it according to a pre-specified plan, producing a figure, formatting a table, executing code.

What cannot be delegated is statistical judgment. Which test suits the structure of the data, which assumption is defensible given the field's theoretical constraints, which observation may legitimately be excluded, and what an effect size means substantively — these remain with the researcher. An agent can propose a particular test and articulate a rationale. Whether that rationale is valid, whether the test's assumptions hold for this sample, and whether the field's conventions warrant this specification is the work of the researcher who knows both the theory and the data's provenance.

The instruction file externalizes procedure to the tool. It cannot externalize judgment. The agent accelerates the analysis. Scientific responsibility belongs to the researcher.

## 7. A Reproducible Agentic Workflow in Practice

This discipline reduces to a concrete set of steps, each of which the researcher owns directly. A random seed must be fixed at every step that involves splitting, sampling, or bootstrapping, and recorded explicitly in the specification log; without it the workflow is not reproducible in any meaningful sense. The computational environment must be captured: package versions should be held in a lock file so that the environment a year from now matches the environment today. Before treating any result as final, the analysis should be re-run from scratch in a clean session; a result that depends on accumulated session state is not a verified result.

The agent's decision path must be recorded: which specifications were tried, which was selected, and why it was chosen. The prompt and model version must be archived alongside the output, so that the AI component of the analysis remains recoverable by any reader who needs to understand what was done.

These steps carry the principles of Sandve et al. (2013) and Wilson et al. (2017) into the agentic workflow: record every step; automate the repetitive ones; leave the final decision with the researcher. Without that record, the agent's speed is the enemy of reproducibility. With it, the agent serves reproducibility rather than undermining it.

## 8. Honest Disclosure of AI's Analytic Role

If AI was used in an analysis, that use must be stated explicitly in the methods section or an AI contribution statement. A bare statement is not sufficient on its own. The reader must be able to understand how the AI was used and at which stages of the analysis.

The `AI-AUTHORSHIP.md` file in this guide offers a graded classification of AI contribution. This classification is not an established academic standard; it is a practitioner framework developed within this guide to help researchers account for their workflow. There is a meaningful difference between an agent that only formatted the code and one that designed and ran the analysis end to end.

The researcher should record which decisions were human and which were delegated to the tool. That record is a condition of both reproducibility and scientific integrity. The Lyttelton et al. (2026) survey — notwithstanding its conflict-of-interest limitation — shows that researchers themselves identified transparent disclosure as an important response to the quality erosion they feared from agentic analysis.

## 9. The Next Booklet

This booklet established the reproducibility backbone of quantitative agentic workflows. Subsequent booklets in the data analysis category will build on this foundation: the discipline of AI consultation in statistical test selection, and the role of human oversight in qualitative coding.

Honest disclosure of AI's role in analysis connects to a broader ethical frame. Booklet 009-01-0001 — Ethics in AI-Assisted Research, From Principle to Behavior — continues from this point.

---

## References

Citations are in APA 7 format. Each DOI was independently verified against Crossref on 2026-06-21. Lyttelton et al. (2026) is Anthropic-commissioned grey literature; the DOI resolves to the publisher page. Wilson et al. (2017) added 2026-06-04.

Bender, E. M., Gebru, T., McMillan-Major, A., & Shmitchell, S. (2021). On the dangers of stochastic parrots: Can language models be too big? In *Proceedings of the 2021 ACM Conference on Fairness, Accountability, and Transparency (FAccT '21)* (pp. 610–623). Association for Computing Machinery. https://doi.org/10.1145/3442188.3445922

Gelman, A., & Loken, E. (2014). The statistical crisis in science. *American Scientist*, *102*(6), 460. https://doi.org/10.1511/2014.111.460

Hicks, M. T., Humphries, J., & Slater, J. (2024). ChatGPT is bullshit. *Ethics and Information Technology*, *26*(2), Article 38. https://doi.org/10.1007/s10676-024-09775-5

Lyttelton, T., Massenkoff, M., & Wilmers, N. (2026). *Coding agents in the social sciences* [Anthropic-commissioned report; grey literature; conflict of interest: publisher is the subject of the study]. Anthropic. https://www.anthropic.com/research/coding-agents-social-sciences

Munafò, M. R., Nosek, B. A., Bishop, D. V. M., Button, K. S., Chambers, C. D., Percie du Sert, N., Simonsohn, U., Wagenmakers, E.-J., Ware, J. J., & Ioannidis, J. P. A. (2017). A manifesto for reproducible science. *Nature Human Behaviour*, *1*(1), Article 0021. https://doi.org/10.1038/s41562-016-0021

Nosek, B. A., Ebersole, C. R., DeHaven, A. C., & Mellor, D. T. (2018). The preregistration revolution. *Proceedings of the National Academy of Sciences*, *115*(11), 2600–2606. https://doi.org/10.1073/pnas.1708274114

Peng, R. D. (2011). Reproducible research in computational science. *Science*, *334*(6060), 1226–1227. https://doi.org/10.1126/science.1213847

Sandve, G. K., Nekrutenko, A., Taylor, J., & Hovig, E. (2013). Ten simple rules for reproducible computational research. *PLoS Computational Biology*, *9*(10), e1003285. https://doi.org/10.1371/journal.pcbi.1003285

Simmons, J. P., Nelson, L. D., & Simonsohn, U. (2011). False-positive psychology: Undisclosed flexibility in data collection and analysis allows presenting anything as significant. *Psychological Science*, *22*(11), 1359–1366. https://doi.org/10.1177/0956797611417632

Wilson, G., Bryan, J., Cranston, K., Kitzes, J., Nederbragt, L., & Teal, T. K. (2017). Good enough practices in scientific computing. *PLoS Computational Biology*, *13*(6), e1005510. https://doi.org/10.1371/journal.pcbi.1005510

Ziems, C., Held, W., Shaikh, O., Chen, J., Zhang, Z., & Yang, D. (2024). Can large language models transform computational social science? *Computational Linguistics*, *50*(1), 237–291. https://doi.org/10.1162/coli_a_00502

---

**Booklet identifier.** `008-01-0001`
**Version.** `0.2.0`
**Date.** 2026-06-21
**License.** This booklet is licensed under CC BY-NC-SA 4.0. https://creativecommons.org/licenses/by-nc-sa/4.0/
**Approximate word count.** 2075 (English body text, measured with wc)
**Verified citations.** 11
**Fabricated citations.** 0
**Previous booklet.** [`007-06-0001`](../../007-academic-writing/007-06-0001/en.md). Grant Proposals and Project Texts, From Idea to Work Package
**Next booklet.** [`009-01-0001`](../../009-ethics-irb/009-01-0001/en.md). Ethics in AI-Assisted Research, From Principle to Behavior
