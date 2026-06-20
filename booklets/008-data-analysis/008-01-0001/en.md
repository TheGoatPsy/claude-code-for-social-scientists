---
title_en: "Reproducible Quantitative Workflows"
title_tr: "Yeniden Üretilebilir Nicel İş Akışları"
booklet_id: "008-01-0001"
category: "008-data-analysis"
language: "en"
version: "0.1.0"
date_published: "2026-05-29"
date_last_revised: "2026-06-20"
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
human_review_date: "2026-06-20"
verified_citations_count: 10
fabricated_citations_count: 0
disclosure_standard: "COPE 2023 + WAME 2023 + ICMJE 2024 + STM 2025 + EU AI Act 2024/1689 Art. 50 + ENAI"
translation_notes: "Re-authored from the Turkish version (tr.md) against the same outline and the same verified citation set. The argument and the bibliographic set are identical across both languages; phrasing is native to each."
license:
  - "CC-BY-NC-SA-4.0 (prose)"
status: "release"
---

# Reproducible Quantitative Workflows

The earlier booklets in this guide addressed what the tool is, how it differs from a chat window, how it is installed, and which standing instructions govern it. This booklet turns to the work the social scientist most often does with a coding agent: quantitative data analysis. Anthropic's 2026 survey of 1,260 quantitative social scientists in the United States and Canada, a commissioned report carrying an inherent conflict of interest that a careful reader should register, found that the great majority of coding-agent users reached for the tool to generate code, and most often to analyze quantitative data (Lyttelton et al., 2026). This pattern is consistent with the broader finding in independent research that AI assistance concentrates where structured, repetitive, high-volume tasks dominate (Ziems et al., 2024). Handing an analysis to an agent does not bring reproducibility with it, however. It creates a new fragility instead. This booklet is about the discipline that keeps an autonomous analysis honest and reproducible.

## The Hard Problem of Agentic Analysis

An agent can take a dataset and a research idea, write the analysis, run it, interpret the output, and iterate on its own. The Lyttelton et al. (2026) survey, an Anthropic-commissioned, non-peer-reviewed report that should be read with the conflict-of-interest limitation in mind, reports that usage has concentrated precisely in this direction. This concentration is the source of both the power and the risk.

In computational research, reproducibility means that someone else, or the same researcher months later, can move from the same data to the same result (Peng, 2011). When an agent produces an analysis in seconds, the intermediate decisions, the paths it tried, and the reasoning that led to the final code can stay invisible. Consider a concrete scenario: a social psychologist studying implicit bias runs a regression on a survey dataset, and the agent, choosing among several defensible variable codings and model specifications without logging any of them, returns a clean-looking result. Twelve months later, a co-author cannot reproduce it. The problem is not the agent's competence. It is the absence of a record.

Sandve et al. (2013) list ten simple rules for reproducible computational research; their core demand is that every step of a process be recorded and, as far as possible, automated. Wilson et al. (2017) extend that demand into a practical framework for scientific computing at all skill levels, emphasizing version control, environment capture, and automation of data processing pipelines. Agentic analysis does not make this discipline easier. It makes it harder, because the convenience of speed tends to crowd out the habit of recording. If the result arrives in a second, writing down how it was produced feels unnecessary. Yet for the person who reproduces that result a year later, it is precisely that record that decides the matter.

## What Reproducible Means When an Agent Does the Work

Agentic speed introduces a specific reproducibility trap: an analysis can look finished while the decisions that shaped it remain entirely unrecorded. Closing that gap requires fixing several components of the process, not just the output.

The prompt is the primary record: the instruction given to the agent is the true text of the analysis, defining its scope, assumptions, and exclusion criteria. The model and its version must also be logged, because the same prompt can produce different code on a different model or version. The data version must be pinned with a checksum or version tag so that the snapshot used is never ambiguous. Every step that splits, samples, or bootstraps requires a fixed random seed; without one, results vary on each run. The computational environment rounds out the record: package versions can change a result silently even when the code itself is unchanged.

These components connect directly to two patterns this guide has already introduced. `CLAUDE.md` documents the AI component of the analysis by fixing the model, the instruction, and the operational limits (booklet 001-01-0004). Memory as Vault, a working concept this guide uses for the practice of treating a persistent folder as a traceable record of research decisions (booklet 003-01-0001), keeps the prompts, the intermediate decisions, and the data passports across sessions. Together they transform agentic analysis from a one-off act of magic into a documented procedure. Neither "Memory as Vault" nor the `CLAUDE.md` conventions are established academic constructs; they are this guide's operational framework, introduced here as practitioner tools.

## The Garden of Forking Paths, Now Automated

A dataset admits countless valid analytic paths. Which variables to exclude, which transformation to apply, which subgroup to examine: each choice is defensible, and each makes a different result possible. Gelman and Loken (2014) call this the garden of forking paths. The researcher believes a single hypothesis is being tested, while data-dependent choices create an invisible tree of multiple comparisons. Simmons et al. (2011) demonstrate experimentally that these researcher degrees of freedom, when left undisclosed, can make almost any result appear statistically significant.

An agent magnifies the problem in scale. The dozens of specifications a researcher would spend hours on, an agent tries in seconds, and it can present the cleanest-looking one without flagging that it tried the others. Even with no ill intent, the result is selective reporting. The Lyttelton et al. (2026) survey, again Anthropic-commissioned and carrying the COI limitation noted above, records that respondents feared exactly this: that AI might worsen selective reporting and risk-averse, incremental research. That fear is not alarmist. Agentic speed turns a latent methodological vulnerability into a concrete, operationally plausible hazard.

## The Preregistration Mindset and the Specification Log

The antidote to this hazard is old, and more valuable in the agentic era than it has ever been. Preregistration is the act of writing the analysis plan before looking at the data, or in the agentic context, at least before running the agent. Nosek et al. (2018) argue that preregistration brings degrees of freedom under control by separating confirmatory from exploratory analysis before the data can influence the analyst's choices. Munafò et al. (2017), in a widely cited manifesto for reproducible science, treat preregistration and transparent reporting as the structural foundation of the field's robustness. These are requirements the architecture of credible science depends on, not a researcher's preference to adopt or set aside.

In an agentic workflow the concrete form of this is a specification log: a plain-text or Markdown file written before the agent runs. It records the planned analysis, the primary hypothesis, and the decisions fixed in advance. If the agent tries alternative specifications during exploration, those are labeled exploratory and do not replace the confirmatory result. Every deviation from the plan is entered in the log with its rationale. The richness the agent produces then becomes not a hidden fishing expedition but an openly reported sensitivity analysis, the kind of transparency that strengthens a paper rather than threatening it.

## The Finder Is Never the Grader, Applied to Statistics

The recurring principle of this guide is that the tool which produces a finding cannot be the authority that confirms it. In statistics this principle matters twice over. An agent interpreting the output of a test can present a summary that contradicts the output itself: misreporting the sign of a coefficient, the significance threshold, or the effect size. For this reason the agent's interpretation must always be verified independently against the raw output, the number in the table, not the agent's narration of it.

The reason for this warning lies in the nature of the model. The model is a system that produces statistical patterns without understanding, and the risk persists even under the most careful instruction (Bender et al., 2021). The generated text can have, at the epistemic level, a character indifferent to the difference between seeming true and being true (Hicks et al., 2024). A fluent summary of a regression table does not mean the table says what the summary says. What follows from this is structural discipline: read the number itself, and treat the agent's narration as a draft that requires verification against the raw output.

## Delegate Procedure, Not Judgment

Not everything the agent can do should be handed to it. Repetitive procedure is a legitimate target for delegation: loading the data, transforming it according to a pre-specified plan, producing a figure, formatting a table. Statistical judgment is not. Which test suits the structure of the data, which assumption is defensible given the field's theoretical constraints, which observation may legitimately be excluded, and what an effect size means substantively must remain with the researcher.

An agent can propose a particular test and articulate its rationale. But deciding whether that rationale is valid, whether the test's assumptions hold for this sample and the field's conventions warrant this specification, is the work of the researcher who knows both the theory and the data's provenance. The instruction file externalizes procedure, not judgment (booklet 001-01-0004). The agent is an assistant that accelerates the analysis. Responsibility for it belongs to the researcher.

## A Reproducible Agentic Workflow in Practice

This discipline reduces to a concrete sequence of steps, each of which the researcher owns directly.

The seed must be fixed at every random step — every split, sample, and bootstrap — and recorded explicitly in the specification log; without it, results vary on each run and the workflow cannot be called reproducible in any meaningful sense. Package versions deserve the same treatment: freezing them in a lock file ensures that the computational environment one year from now matches the environment today, not merely that the code is unchanged. Before treating any result as final, re-run the analysis from scratch in a clean session. A result that depends on accumulated interpreter state is not a result; it is a snapshot of a particular session's history. The agent's decision path also belongs in the log: which specifications were tried, why the chosen one was selected, and how the final approach differs from the first attempt. That record is what allows the paper's methods section to reflect the actual analytic process rather than a retrospective tidying of it. The prompt and model version should be archived alongside the output — not separately, where they can drift or disappear — so that the AI component of the analysis remains recoverable by any reader who needs to understand what was done.

These steps are the principle of Sandve et al. (2013) and Wilson et al. (2017), carried into the agentic workflow: record and automate every step of the process. If the instruction file is the machine-facing side of a paper's methods section, this log is the ledger of the analysis. Without it, the agent's speed becomes the enemy of reproducibility. With it, the agent serves reproducibility rather than undermining it.

## Honest Disclosure of AI's Analytic Role

The AI used in an analysis must be openly disclosed in the methods or contribution statement of the paper. The ethics booklet of this guide shows how disclosure descends from principle to behavior (booklet 009-01-0001). This booklet is itself an example: its frontmatter block declares that the text was largely drafted by AI from a human-approved outline and reviewed by the author. The same honesty applies to any analysis an agent has carried out.

The `AI-AUTHORSHIP.md` file in this guide provides a graded disclosure scale. This scale is a practitioner convention developed within this guide, an operational definition rather than an established academic standard. Merely formatting the code is one kind of contribution. Designing and running the analysis end to end is another kind entirely. The researcher records which decision belongs to the human and which to the tool. That record is a condition of both reproducibility and scientific honesty. The Lyttelton et al. (2026) survey data, notwithstanding its conflict-of-interest limitation, shows that researchers themselves counted transparent disclosure as their primary response to the quality erosion they feared from agentic analysis. That alignment between researcher concern and disclosure practice is worth both noting and acting on.

## The Next Booklet

This booklet established the reproducibility backbone of quantitative agentic workflows. The next booklets in the data analysis category will extend that foundation: the discipline of AI consultation in statistical test selection, and human oversight in qualitative coding. Meanwhile, the honest disclosure of AI's role in analysis fits into a broader ethical frame in booklet 009-01-0001, which continues from this point.

---

## References

Citations are in APA 7 format. Each DOI was independently verified against Crossref on 2026-06-04. Lyttelton et al. (2026) is Anthropic-commissioned grey literature; the DOI resolves to the publisher page. Wilson et al. (2017) added 2026-06-04.

Bender, E. M., Gebru, T., McMillan-Major, A., & Shmitchell, S. (2021). On the dangers of stochastic parrots: Can language models be too big? In *Proceedings of the 2021 ACM Conference on Fairness, Accountability, and Transparency (FAccT '21)* (pp. 610-623). Association for Computing Machinery. https://doi.org/10.1145/3442188.3445922

Gelman, A., & Loken, E. (2014). The statistical crisis in science. *American Scientist*, 102(6), 460. https://doi.org/10.1511/2014.111.460

Hicks, M. T., Humphries, J., & Slater, J. (2024). ChatGPT is bullshit. *Ethics and Information Technology*, 26(2), Article 38. https://doi.org/10.1007/s10676-024-09775-5

Lyttelton, T., Massenkoff, M., & Wilmers, N. (2026). *Coding agents in the social sciences* [Anthropic-commissioned report; grey literature; conflict of interest: publisher is the subject of the study]. Anthropic. https://www.anthropic.com/research/coding-agents-social-sciences

Munafò, M. R., Nosek, B. A., Bishop, D. V. M., Button, K. S., Chambers, C. D., Percie du Sert, N., Simonsohn, U., Wagenmakers, E.-J., Ware, J. J., & Ioannidis, J. P. A. (2017). A manifesto for reproducible science. *Nature Human Behaviour*, 1(1), Article 0021. https://doi.org/10.1038/s41562-016-0021

Nosek, B. A., Ebersole, C. R., DeHaven, A. C., & Mellor, D. T. (2018). The preregistration revolution. *Proceedings of the National Academy of Sciences*, 115(11), 2600-2606. https://doi.org/10.1073/pnas.1708274114

Peng, R. D. (2011). Reproducible research in computational science. *Science*, 334(6060), 1226-1227. https://doi.org/10.1126/science.1213847

Sandve, G. K., Nekrutenko, A., Taylor, J., & Hovig, E. (2013). Ten simple rules for reproducible computational research. *PLoS Computational Biology*, 9(10), e1003285. https://doi.org/10.1371/journal.pcbi.1003285

Simmons, J. P., Nelson, L. D., & Simonsohn, U. (2011). False-positive psychology: Undisclosed flexibility in data collection and analysis allows presenting anything as significant. *Psychological Science*, 22(11), 1359-1366. https://doi.org/10.1177/0956797611417632

Wilson, G., Bryan, J., Cranston, K., Kitzes, J., Nederbragt, L., & Teal, T. K. (2017). Good enough practices in scientific computing. *PLoS Computational Biology*, 13(6), e1005510. https://doi.org/10.1371/journal.pcbi.1005510

Ziems, C., Held, W., Shaikh, O., Chen, J., Zhang, Z., & Yang, D. (2024). Can large language models transform computational social science? *Computational Linguistics*, 50(1), 237-291. https://doi.org/10.1162/coli_a_00502

---

**Booklet identifier.** `008-01-0001`
**Version.** `0.1.0`
**Date.** 2026-06-20
**Approximate word count.** 2049 (English body text, measured with wc)
**Verified citations.** 10
**Fabricated citations.** 0
**Previous booklet.** [`007-02-0001`](../../007-academic-writing/007-02-0001/en.md). APA 7 with DOI Discipline
**Next booklet.** [`009-01-0001`](../../009-ethics-irb/009-01-0001/en.md). Ethics in AI-Assisted Research, From Principle to Behavior
