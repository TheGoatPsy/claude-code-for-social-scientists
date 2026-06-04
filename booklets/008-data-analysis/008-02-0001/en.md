---
title_en: "Statistical Test Selection with AI Consultation Discipline"
title_tr: "Yapay Zekâ Danışma Disipliniyle İstatistiksel Test Seçimi"
booklet_id: "008-02-0001"
category: "008-data-analysis"
language: "en"
version: "0.1.0"
date_published: "2026-05-29"
date_last_revised: "2026-06-04"
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
human_review_date: "2026-06-04"
verified_citations_count: 11
fabricated_citations_count: 0
disclosure_standard: "COPE 2023 + WAME 2023 + ICMJE 2024 + STM 2025 + EU AI Act 2024/1689 Art. 50 + ENAI"
translation_notes: "Re-authored from the Turkish version (tr.md) against the same outline and the same verified citation set. The argument and the bibliographic set are identical across both languages; phrasing is native to each."
license:
  - "CC-BY-NC-SA-4.0 (prose)"
status: "release"
---

# Statistical Test Selection with AI Consultation Discipline

The previous booklet in this category built the reproducibility backbone of agentic quantitative analysis: the specification log, the fixed seed, the clean environment (booklet 008-01-0001). This booklet turns to the inferential heart of that analysis — the decision about which test to run. An Anthropic survey report (Lyttelton et al., 2026, a survey published by Anthropic, which is also the vendor of Claude Code, and not peer-reviewed) records that the social scientists it surveyed reach for a coding agent most of all to analyze quantitative data, and that those same researchers feared AI worsening selective reporting. Test selection is precisely where that fear either materializes or is disciplined away. When an agent can propose any test in an instant, which test you choose is no longer a slow deliberation. It is a decision one prompt away. This booklet is about the discipline that keeps that consultation honest and defensible.

## 1. Why Test Selection Is the Critical Decision in the Agentic Era

A statistical test is an inferential commitment. Which test you run determines what you can claim from the data. An agent compresses this commitment into a single move: it proposes a test, explains its rationale, runs it, and interprets the result — all before the researcher has finished reading the output of the previous step. The Lyttelton et al. (2026) survey report records that usage among its respondents has concentrated in exactly this direction, toward autonomous analysis.

Test selection used to be slow. The researcher would think hard about the data structure, consult a statistician down the corridor, sleep on the decision. A doctoral student running a first regression might spend an afternoon with a methods textbook before settling on a model. That slowness offered inadvertent protection: the friction of the decision forced engagement with its meaning. Now the agent is an always-available consultant who never asks to be called back tomorrow.

The speed has changed. The responsibility has not.

The constant readiness of the consultant does not lift from the researcher the burden of justifying the decision. To select a test is to accept the world it assumes — the level of measurement it requires, the distributional properties it presupposes, the sample structure it treats as given. Those acceptances carry epistemic weight. They determine what can be claimed and what cannot. It is the researcher, not the agent, who signs that acceptance and stands behind it in a methods section, a dissertation defense, or a peer-review response.

## 2. Researcher Degrees of Freedom and the Flexibility of Test Choice

The choices a researcher makes when confronting a dataset form what the methodological literature calls researcher degrees of freedom. Simmons et al. (2011) showed experimentally that these degrees of freedom, when left undisclosed, can make almost any result appear statistically significant. The demonstration is pointed: the same dataset, processed through different defensible choices, yields contradictory conclusions — and the published version shows only the one that worked. Test selection is among the largest of these degrees of freedom. The same hypothesis can come out non-significant under one parametric test and significant under a non-parametric alternative that is equally defensible by the data's characteristics.

Wicherts et al. (2016) collected the degrees of freedom spread across planning, running, analyzing, and reporting psychological studies into a comprehensive checklist, and showed how each degree of freedom opens a path toward p-hacking. The value of that checklist is not that it prohibits choices — legitimate analytical decisions require flexibility — but that it makes choices visible in advance. When an agent is asked which test to use, it can offer several options simultaneously, and the most tempting option is often the one that returns significance. A researcher who has not enumerated the decision space before consulting the agent is in a position where the agent's output can steer the decision without the researcher registering that steering as a choice at all. The Wicherts et al. checklist is the discipline that prevents this: the degrees of freedom are named before the agent is consulted, not afterward.

## 3. The Garden of Forking Paths, in Test Selection

Gelman and Loken (2014) call the situation in which data-dependent analytic choices create an invisible tree of multiple comparisons the garden of forking paths. The name captures something important: each fork looks reasonable at the moment it is taken, and yet the cumulative effect is that the reported p-value is no longer an honest probability.

Test selection is the most frequently walked path in that garden. To look at the data, notice that the distribution departs from normality, switch to a non-parametric test, and find that this test returns significance — that is a data-dependent decision even when the intent is entirely honest. The researcher did not set out to cheat. But because the decision was made after seeing the data, the reported test outcome no longer means what a prospectively chosen test would mean.

An agent, the guide's reading of the forking-paths problem suggests, does not eliminate this structure — it accelerates and conceals it. The test alternatives a researcher would spend hours deliberating, the agent tries in seconds and can present the cleanest-looking one. The forks do not disappear. They multiply and vanish from view simultaneously. For this reason the forking-paths problem in test selection demands more attention in an agentic workflow, not less.

## 4. Multiverse Analysis: Agentic Speed Turned Into a Virtue

The most powerful answer to the forking-paths problem is not to hide the chosen path but to expose every path at once. Steegen et al. (2016) proposed multiverse analysis, which systematically computes the space of results produced by all defensible analytic choices. Instead of one result from one test, the researcher reports the distribution of results across all reasonable specifications. Simonsohn et al. (2020) formalized this into specification curve analysis — a graphical and inferential technique that displays every specification alongside the outcome it produces and tests whether the pattern of results across the curve differs from what chance would predict. Silberzahn et al. (2018) supplied the empirical warrant: twenty-nine independent teams analyzing the same dataset reached markedly different conclusions through different analytic choices. The lesson is not that any one team was wrong. It is that analytic decisions are a force that shapes findings, and that force should be made visible rather than resolved by a single hidden choice.

Here agentic speed turns from a liability into a tool. Multiverse analysis was expensive by hand — building and running dozens of specifications one by one took days. The agent, precisely because it will try every reasonable test without complaint, makes that analysis tractable. Rather than leaving the agent's willingness to explore as a concealed fishing expedition, the researcher steers it into an openly reported specification curve. The condition that makes this work is fixed in advance: the full set of defensible specifications must be defined before any results are inspected. When that condition holds, the same computational convenience that would otherwise feed selective reporting becomes the instrument of transparency instead.

## 5. Separating Pre-specification From Exploration

Even multiverse reporting requires the confirmatory claim to be fixed before the data are touched. Nosek et al. (2018) argue that preregistration brings degrees of freedom under control precisely by separating confirmatory from exploratory analysis — a distinction that Munafò et al. (2017), in their manifesto for reproducible science, treat as a structural foundation of the field's robustness. In agentic test selection, the meaning of this distinction is clear. Write down the primary test and its assumptions before consulting the agent. Every alternative the agent proposes during exploration carries an explicit exploratory label. None of those alternatives replaces the confirmatory result.

This is the specification log of the previous booklet, applied to the specific decision of test choice (booklet 008-01-0001). Consultation is welcome. The commitment is made beforehand. When the agent proposes a test mid-session, the researcher asks one question: was this test chosen at the planning stage, or does it emerge from looking at the data? When that question is entered in the log alongside the answer, the richness the agent produces becomes not a threat to inference but a documented sensitivity analysis.

## 6. The Finder Is Never the Grader, Applied to a Test's Assumptions

The recurring principle of this guide is that the tool that produces a finding cannot be the authority that confirms it. In statistical test selection, that principle cuts through a specific and common failure mode: an agent that runs a test and declares the assumptions met without having genuinely examined the diagnostics.

A doctoral student testing whether two groups differ on a psychological outcome might ask the agent to choose between an independent-samples t-test and a Mann-Whitney U. The agent proposes the t-test, generates the output, and adds a sentence: "The assumption of normality was verified." The output looks complete. But the agent may have produced that sentence because sentences about verified assumptions typically follow sentences about test selection in its training data — not because it inspected a Shapiro-Wilk statistic, examined the Q-Q plots, or checked the sample size against the robustness of the central limit theorem for the particular distribution at hand.

The source of this fragility lies in the nature of the model. A language model produces statistically patterned text without anything that constitutes understanding of the domain (Bender et al., 2021). The generated text can have, at the epistemic level, a character indifferent to the difference between seeming true and being true (Hicks et al., 2024). Fluency is not accuracy. A fluent rationale is not a verified rationale. The two can be identical in surface form and entirely different in epistemic standing.

For this reason the agent's test recommendation is a hypothesis to be checked, not a verdict to be accepted. The researcher reads the assumption diagnostics against the raw output independently: the actual test statistic, the actual p-value of the normality check, the actual residual plot. The agent's sentence about whether the assumptions are met is noted and then set aside while the researcher forms an independent judgment.

## 7. Take the Consultation, Do Not Delegate the Decision

In agentic analysis the line between what can and cannot be delegated is especially sharp in test selection. What can be delegated is the consultation itself: the agent lists candidate tests, explains the trade-offs between them, computes each one, and flags where assumptions are borderline. What cannot be delegated is the decision.

Which test answers the research question? Which assumption is defensible given the theory of the domain and the context of the data? Whether a borderline normality violation matters depends on the sample size, the research tradition, the claim being made, and the expectations of the audience — none of which the agent knows unless the researcher has supplied them explicitly. That judgment belongs to the researcher. The agent is treated as a knowledgeable but non-accountable consultant: taking its advice is legitimate, but the researcher must be able to defend that advice independently. The instruction file externalizes analytical procedure, not judgment (booklet 001-01-0004). The agent computes the test. The researcher selects it and stands behind the result in writing.

## 8. In Practice: A Test-Selection Consultation Protocol

This discipline reduces to a concrete, applicable protocol that can be entered in the specification log before a session begins.

First, write down the primary test and its assumptions before consulting the agent, and enter them in the log. Second, ask the agent to enumerate not a single test but the full set of defensible alternatives — framed explicitly as the multiverse of reasonable specifications. Third, define the specification set before examining any results; then run the multiverse or specification curve analysis across those pre-defined options and report the distribution of results, not one cleaned-up finding. Fourth, verify the assumption diagnostics independently against the raw numerical output — the statistic itself, not the agent's prose summary of it. Fifth, separate the confirmatory and exploratory analyses in the log: the primary pre-specified test carries the confirmatory claim; any additional tests identified during the session carry an exploratory label. Sixth, disclose the agent's consultative role in the methods section or contribution statement of the paper.

This protocol unites the researcher-degrees-of-freedom checklist of Wicherts et al. (2016), multiverse and specification curve reporting, and the preregistration mindset into a single agentic consultation workflow. Without the protocol, the agent's convenience feeds selective reporting directly: it offers the test that works, the researcher accepts it, and no record shows that alternatives existed. With the protocol, the consultation becomes part of a defensible inferential chain. The agent scans the space of tests quickly. The protocol puts that speed in the service of transparency rather than in the service of the result the researcher was hoping for.

## 9. The Next Booklet

This booklet tied test selection to a discipline of consultation. The question the protocol holds open — who carries epistemic responsibility for the inference — is the same question that runs through this entire guide. The agent proposes. The researcher decides. The log records. And the paper discloses.

That honest disclosure of the agent's analytic role fits into a broader ethical frame that the next booklet addresses directly. The decisions made at the test-selection stage are among the most consequential decisions in a quantitative study — not because statistics are the heart of social science, but because the choice of test shapes what can be claimed, and the claim shapes what accumulates in the literature. An agent that accelerates that choice without a discipline around it accelerates the accumulation of noise. An agent working within the discipline described here accelerates the accumulation of defensible evidence instead. Booklet 009-01-0001 continues from this point.

---

## References

Citations are in APA 7 format. Each DOI and identifier was independently verified against Crossref, doi.org, or the publisher page. Verification dates: original citations on 2026-05-29; Simonsohn et al. (2020) and Munafò et al. (2017) on 2026-06-04. Lyttelton et al. (2026) is an Anthropic survey report (grey literature, not peer-reviewed) verified at the publisher URL on 2026-05-29. Anthropic is also the vendor of Claude Code, the product this booklet teaches, which constitutes a vendor conflict of interest.

Bender, E. M., Gebru, T., McMillan-Major, A., & Shmitchell, S. (2021). On the dangers of stochastic parrots: Can language models be too big? In *Proceedings of the 2021 ACM Conference on Fairness, Accountability, and Transparency (FAccT '21)* (pp. 610-623). Association for Computing Machinery. https://doi.org/10.1145/3442188.3445922

Gelman, A., & Loken, E. (2014). The statistical crisis in science. *American Scientist*, 102(6), 460. https://doi.org/10.1511/2014.111.460

Hicks, M. T., Humphries, J., & Slater, J. (2024). ChatGPT is bullshit. *Ethics and Information Technology*, 26(2), Article 38. https://doi.org/10.1007/s10676-024-09775-5

Lyttelton, T., Massenkoff, M., & Wilmers, N. (2026). *Coding agents in the social sciences*. Anthropic. https://www.anthropic.com/research/coding-agents-social-sciences

Munafò, M. R., Nosek, B. A., Bishop, D. V. M., Button, K. S., Chambers, C. D., Percie du Sert, N., Simonsohn, U., Wagenmakers, E.-J., Ware, J. J., & Ioannidis, J. P. A. (2017). A manifesto for reproducible science. *Nature Human Behaviour*, 1, 0021. https://doi.org/10.1038/s41562-016-0021

Nosek, B. A., Ebersole, C. R., DeHaven, A. C., & Mellor, D. T. (2018). The preregistration revolution. *Proceedings of the National Academy of Sciences*, 115(11), 2600-2606. https://doi.org/10.1073/pnas.1708274114

Silberzahn, R., Uhlmann, E. L., Martin, D. P., Anselmi, P., Aust, F., Awtrey, E., Bahník, Š., Bai, F., Bannard, C., Bonnier, E., Carlsson, R., Cheung, F., Christensen, G., Clay, R., Craig, M. A., Dalla Rosa, A., Dam, L., Evans, M. H., Flores Cervantes, I., ... Nosek, B. A. (2018). Many analysts, one data set: Making transparent how variations in analytic choices affect results. *Advances in Methods and Practices in Psychological Science*, 1(3), 337-356. https://doi.org/10.1177/2515245917747646

Simmons, J. P., Nelson, L. D., & Simonsohn, U. (2011). False-positive psychology: Undisclosed flexibility in data collection and analysis allows presenting anything as significant. *Psychological Science*, 22(11), 1359-1366. https://doi.org/10.1177/0956797611417632

Simonsohn, U., Simmons, J. P., & Nelson, L. D. (2020). Specification curve analysis. *Nature Human Behaviour*, 4(11), 1208-1214. https://doi.org/10.1038/s41562-020-0912-z

Steegen, S., Tuerlinckx, F., Gelman, A., & Vanpaemel, W. (2016). Increasing transparency through a multiverse analysis. *Perspectives on Psychological Science*, 11(5), 702-712. https://doi.org/10.1177/1745691616658637

Wicherts, J. M., Veldkamp, C. L. S., Augusteijn, H. E. M., Bakker, M., van Aert, R. C. M., & van Assen, M. A. L. M. (2016). Degrees of freedom in planning, running, analyzing, and reporting psychological studies: A checklist to avoid p-hacking. *Frontiers in Psychology*, 7, 1832. https://doi.org/10.3389/fpsyg.2016.01832

---

**Booklet identifier.** `008-02-0001`
**Version.** `0.1.0`
**Date.** 2026-06-04
**Approximate word count.** 2698 (English body text, measured with wc)
**Verified citations.** 11
**Fabricated citations.** 0
**Previous booklet.** [`008-01-0001`](../008-01-0001/en.md). Reproducible Quantitative Workflows
**Next booklet.** [`009-01-0001`](../../009-ethics-irb/009-01-0001/en.md). Ethics in AI-Assisted Research, From Principle to Behavior
