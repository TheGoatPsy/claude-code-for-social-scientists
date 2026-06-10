---
name: statistical-consultation-protocol
description: Use when selecting a statistical test with AI consultation, when assumptions need checking against the actual data, when an analysis plan or decision log must be written before running anything, or when results need APA-style reporting with effect sizes.
---

# Statistical Consultation Protocol

## When to use

Use this skill when a statistical decision is about to be made with an AI tool in the loop: test selection, assumption checking, analysis planning, or results reporting. It is the operating protocol behind booklet 008-02. The tool consults, the researcher decides, and for confirmatory or high-stakes designs a statistician outranks both.

## Inputs

- The design: groups, repeated measures, observational or experimental, nesting.
- Each variable with its measurement level and its role.
- Sample size, and the missing data situation.
- The inferential question, stated in words.
- The analysis software in use.

## Workflow

1. Write the inferential question in plain words before any test is named. A test chosen before the question is stated is a test chosen by habit.
2. Ask the tool for candidate tests, each with its assumptions listed next to it. A candidate without its assumptions is not a candidate.
3. Check every assumption against the actual data properties: distribution as observed, variance structure as observed, independence as designed. Textbook defaults are not evidence.
4. Record the decision log: the chosen test, the rejected alternatives, and the reason each was rejected.
5. Timestamp the analysis plan before running it, through preregistration where the study allows it, or at minimum a dated plan file in the project.
6. Run the analysis as a reproducible script rather than menu clicks, when the software allows.
7. Report in APA style: the test statistic, exact p value, effect size with its confidence interval, and the assumption check results.
8. Apply the judgment gate. Statistical significance is not substantive importance, and the written interpretation must separate the two.

## Output

Return:

- The inferential question in words.
- The candidate table, tests with assumptions.
- Assumption check results on the real data.
- The decision log.
- A reproducible analysis script or its skeleton.
- APA-formatted results sentences.

## Verification

- Every candidate test in the log carries its assumptions, and every assumption has a check result from the actual data.
- The decision log explains rejections, and no test was chosen solely because the tool named it first.
- Effect sizes and confidence intervals appear wherever a p value appears.
- The interpretation separates statistical significance from substantive importance in explicit sentences.
- The plan's timestamp precedes the analysis run.

## Safety

AI consultation does not replace a statistician for confirmatory trials, clinical decisions, or any analysis with regulatory weight. Data leave the machine only within the consent scope, and aggregated or simulated data stand in when the scope is unclear. Hypotheses stay as written once results exist, and a tool that proposes revising them afterward is proposing HARKing.

## Example prompt

"Üç gruplu, ön test son test tasarımım var, hangi analizle test edeceğime karar vermeden önce varsayımları ve alternatifleri benimle kur."

Expected smoke output:

- The inferential question restated in words.
- A candidate table with assumptions per test.
- An assumption check plan against the real data and a decision log skeleton.

## Türkçe kullanım notu

Bu beceri, istatistiksel test seçimini alışkanlıktan çıkarıp karar günlüğüne bağlar. Önce çıkarım sorusu sözle yazılır, aday testler varsayımlarıyla birlikte listelenir, varsayımlar ders kitabı varsayılanına göre değil eldeki verinin gerçek özelliklerine göre denetlenir ve reddedilen her alternatifin gerekçesi kaydedilir. Etki büyüklüğü ve güven aralığı olmadan p değeri raporlanmaz. Doğrulayıcı ya da klinik ağırlıklı işlerde son söz istatistikçinindir.
