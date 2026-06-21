---
title_en: "Open Science Package, Data, Code, Supplementary Files, and Persistent DOI"
title_tr: "Açık Bilim Paketi, Veri, Kod, Ek Dosya ve Kalıcı DOI"
booklet_id: "003-04-0001"
category: "003-memory-system"
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
    model_dated: null  # no dated identifier published by Anthropic for Opus 4.8 as of 2026-06-21
    role: "drafting, verification, citation lookup, bilingual re-authoring"
    interaction_mode: "interactive console"
ai_contribution_level: "substantial-drafting"
human_review: "complete"
human_review_date: "2026-06-21"
verified_citations_count: 9
fabricated_citations_count: 0
disclosure_standard: "COPE 2023 + WAME 2023 + ICMJE 2024 + STM 2025 + EU AI Act 2024/1689 Art. 50 + ENAI"
translation_notes: "English re-authored from the finalized Turkish source (v0.1.0, 2026-06-21), not a literal translation. Body follows the Turkish section structure and argumentation; register adapted to fluent scholarly English throughout. Section count expanded from 10 to 11 to match TR. Citation audit 2026-06-21: all DOIs verified against Crossref and DataCite. Kitzes et al. 2018 verified by ISBN; no DOI exists for the UC Press open-access edition. Klump & Huber 2017 and Fenner et al. 2019 added as enrichment beyond the operator draft's original 7 sources."
license:
  - "CC-BY-NC-SA-4.0 (prose)"
status: "release"
---

# Open Science Package, Data, Code, Supplementary Files, and Persistent DOI

Publication is not the end of a research project. The finding has been reported; how it was produced has not yet been shown. Without a data dictionary, without documented analysis code, without organized supplementary files, without a license, and without a persistent identifier, the research package is incomplete. That incompleteness is not only a transparency problem. Five years later, the researcher who returns to her own archive may find she can no longer reconstruct what she did.

The central argument of this booklet is straightforward: a social scientist should think about her article not as a standalone object but as the public face of a reproducible, auditable research package. Open science is not reckless disclosure. It is sharing what can be shared in a disciplined way, and documenting honestly why what cannot be shared cannot be. Those two responsibilities are not in tension. They complete each other.

## 1. The difference between an article and a research package

An article tells the story of a finding. A research package shows how the finding was produced. These are different things, and one cannot substitute for the other.

What a few paragraphs of methods text summarize, a research package makes visible as concrete files: data-cleaning decisions, transformation steps, the sequence of analysis, the source-verification protocol, the ethical boundaries that governed collection. That visibility serves more than the reader. Kitzes and colleagues (2018), examining reproducibility experiences across data-intensive sciences, make the point directly: researchers are the most frequent reproducers of their own work. A well-assembled research package teaches a researcher what she did when she returns to her archive five years later. Which version of the data was used, which script ran, which source was drawn from where, which variable was defined how. These things are not remembered. They are recorded.

An article without a package points to a conclusion. An article with a package keeps the road to that conclusion open. The difference between them determines whether the research can be interrogated in the future.

## 2. When open data is possible

Open data is not possible for every study, and that is normal. Participant rights, ethics committee conditions, the scope of informed consent, and the risk of harm when data are decontextualized are genuine constraints that govern sharing decisions.

Anonymized data that carries no re-identification risk, falls within the scope of consent, and will not produce harm when separated from its original context can be shared. Clinical data, data from small communities, and sensitive interview transcripts often fail to meet those conditions. But that does not leave the researcher empty-handed.

When direct sharing is not possible, alternative forms take its place: synthetic example data, a variable dictionary, analysis code, summary statistics, an access request guide, and an ethics limitation note. These alternatives do not mean the research is unverifiable. They document the conditions under which verification is possible. Nosek and colleagues (2015), mapping the infrastructure of an open research culture, show that transparency, methodological rigor, and reproducibility are the foundational commitments of open science. Within that framework, constrained-data research can still be open — when the constraint is documented honestly.

## 3. Data dictionary and codebook

The data dictionary is the most neglected and most useful component of a research package. Without it, a data file is a sequence of numbers that means nothing to anyone who was not present when the decisions were made — and, given enough time, it will mean nothing to the researcher herself.

A well-prepared data dictionary records for every variable: its name and a plain-language description, measurement level, value range and the meaning of each code, the missing-data code and what it signifies, any transformation applied, the variable's role in the analysis, and its link to the source it came from. This information may not fill more than a page. But without that page, no one can read the data correctly.

For qualitative research, the codebook serves the same purpose. It holds the code label, a definition, inclusion and exclusion criteria, an example quotation, and a version note. When AI-assisted coding has been used, the model's role, the segments of text it processed, and how analyst oversight was conducted must be stated explicitly. AI contribution is an increasingly critical documentation point both for technical transparency and for defensibility in peer review.

Sandve and colleagues (2013), in their ten rules for reproducible computational research, place provenance tracking among the foundational commitments. Knowing where a variable came from, when it was defined, and by what decision is a matter of tracing origin. The data dictionary builds that trace.

## 4. Analysis code and environment capture

Code alone is not sufficient. The environment in which the code runs must also be recorded. R packages, Python libraries, version numbers, and the operating environment can all affect results directly. The same script may produce different output across package versions, or it may fail to run at all.

The solution is an environment file included in the package: `renv.lock` for R, `requirements.txt` or `environment.yml` for Python, `Project.toml` for Julia. These files freeze the computational environment. Recreating it later becomes possible rather than guesswork.

Noble (2009), in his guide to organizing computational biology projects, treats the recording of file structure, scripts, and environment as a basic practice, not an optional refinement. He notes that everything may one day have to be redone, and the most likely person to undertake that task is the researcher's own future self. Without an environment file, that task grows considerably harder.

Claude Code can assist in this process: organizing code, preparing a reproduction note, identifying missing dependencies, standardizing comments. What it cannot do is determine whether the code is methodologically appropriate, whether the analysis answers the research question, or whether the interpretation is grounded in domain knowledge. That judgment belongs to the researcher.

## 5. Organizing supplementary materials

Supplementary files are not the article's overflow drawer. They are a documented layer that provides the reader with what the article could not hold, available when needed.

What belongs there? Scale items and scoring guides, the systematic search protocol and PRISMA flow diagram, exclusion rationale tables, sensitivity analyses and additional results, power calculations, ethics approval documents, and search strings. Every supplementary file carries a brief header: what it is, when it was produced, which section of the article it connects to, and how it should be read.

Bezjak and colleagues (2018), in the Open Science Training Handbook, recommend organizing supplementary materials under content-descriptive file names rather than generic numbering. A file named `supp-a-scale-items.pdf` tells the reader what it contains; `Appendix 1.pdf` does not. The discipline of naming is also the discipline of organizing: if a file cannot be given a descriptive name, its role in the package has probably not been fully thought through.

Piwowar and Vision (2013) show that sharing data is associated with increased citation rates. The same effect almost certainly extends to complete, well-organized supplementary materials. A package that makes auditing easy invites the kind of engagement that produces citations.

## 6. OSF, Zenodo, and institutional repositories

Platform choice depends on the nature of the research and its goals. OSF is well suited to documenting the research process, pre-registering a study, and keeping project components organized throughout a project's life. It functions as a living workspace and gives researchers who want to make their process transparent a flexible infrastructure for doing so.

Zenodo stands out for persistent DOI assignment and version archiving. Operated by CERN and integrated into the European Commission's Horizon research infrastructure, it is free to use. Because each version receives its own DOI, the exact data or code used in a given publication can be cited with precision. That precision matters for editorial integrity and for the scientific record.

Institutional repositories connect to the university's long-term records system and sometimes satisfy funder mandates that specify a particular deposit location. More than one repository can serve the same project. What matters is that records point to one another: the article DOI, the data DOI, the code repository, and any supplementary-file DOI should form a cross-referencing network. Klump and Huber (2017), surveying twenty years of persistent identifier systems, show that the systems that last are those built on institutional sustainability and a social contract between stakeholders — not technical superiority alone.

## 7. Concept DOI and version DOI

Platforms like Zenodo assign two kinds of DOI to a deposited project. The concept DOI carries the persistent identity of the project as a whole; it always resolves to the latest version. The version DOI carries the fixed identity of a specific release; once assigned, it never changes.

This distinction looks like a technical detail. It is not. The version DOI is what belongs in the methods section of a published article. Citing the concept DOI instead means that a reader who follows the link six months after publication may arrive at a different version of the data or code than the one used to produce the results. That ambiguity undermines independent verification.

Fenner and colleagues (2019), in their data citation roadmap for scholarly repositories, recommend that repositories support citation at both the concept and version level as part of their implementation. For the individual researcher, using this infrastructure correctly means understanding the difference: the version DOI in the article bibliography, the concept DOI as a general pointer to the project as a whole.

## 8. Choosing a license

A license is the legal language of sharing ethics. It specifies what a user may do with the material, what she may not do, and under what conditions attribution is required. Sharing without a license creates ambiguity, and ambiguity often results in the material not being used at all.

Code and prose deserve different licenses. For code, MIT or Apache 2.0 are common choices: they allow reuse, support derivative works, and cause no friction in dependency chains. GPL requires that any derivative using the code also be released under the same license. Which to choose depends on the project's goals and on whether the researchers want to require downstream openness. Clarifying this at the start of a project reduces the risk of conflict later.

For prose and procedural text, Creative Commons licenses are more suitable. CC BY permits free use with attribution. CC BY-NC restricts commercial use. CC BY-SA requires that derivative works carry the same license. The right combination depends on the research context, funder conditions, and institutional policy.

Sensitive or personal data is not shared under an open license. In that case, the package README documents why the data carries no open license. An unexplained restriction is not transparency. An explained restriction is.

## 9. FAIR principles and the README

Wilkinson and colleagues (2016) set out the FAIR Guiding Principles for scientific data management: findability, accessibility, interoperability, and reusability. Developed initially for institutional repositories and large-scale data infrastructure, the same logic applies at the scale of an individual research package.

The package README is the FAIR framework applied at the package level. A complete README addresses: the purpose and scope of the project, a list of all data and code components with brief descriptions, steps to set up the analysis environment, the order in which analyses should be run, license information for each component, the AI contribution statement, and contact information. Without a README, even the best-documented package remains a closed box to any researcher who approaches it from outside.

For the social sciences this requirement carries particular weight. The range of methods — from quantitative analysis to qualitative interpretation, from archival work to experimental design — means that the components of a research package vary enormously from project to project. No single README template fits every case. But the principle is constant: every package needs a starting document that explains which component answers which question and how the whole can be navigated.

## 10. Pre-release checklist

Before a package is published, the following questions should be answered. Is data sharing consistent with the ethics committee decision and participant consent? If data cannot be shared, has a justification note been prepared? Does the data dictionary cover every variable? Has the code been verified to run in a clean environment? Do the supplementary files match the claims in the article? Has the concept DOI been distinguished from the version DOI, and does the article bibliography cite the version DOI? Have licenses been chosen separately for code and prose? Can an independent researcher navigate the package using the README alone? Is an AI contribution statement included in the package?

This checklist forms the basis of the `/open-science-release-packager` skill. The skill assembles the package. The researcher makes the final decisions. Ethical compliance, methodological soundness, and citation integrity cannot be delegated to any tool.

## 11. Skill outputs

`/open-science-release-packager` produces the following outputs: a README draft, a data dictionary template, a codebook template, an analysis reproduction note, a supplementary materials index, a license summary, a Zenodo and OSF preparation checklist, a note on concept DOI versus version DOI, and an AI contribution statement.

These outputs do not turn research into a performance. They connect it to a sustainable scientific record. When a researcher completes this package, she has not simply published an article. She has left an archive that the research can be recovered from — by anyone, including herself.

## References

Citations are in APA 7 format. DOIs verified against Crossref and DataCite on 2026-06-21. Kitzes et al. (2018) is identified by ISBN; no DOI exists for the published edition.

Bezjak, S., Clyburne-Sherin, A., Conzett, P., Fernandes, P., Görögh, E., Helbig, K., Kramer, B., Labastida, I., Niemeyer, K., Psomopoulos, F., Ross-Hellauer, T., Schneider, R., Tennant, J., Verbakel, E., Brinken, H., & Heller, L. (2018). *Open science training handbook*. FOSTER/Zenodo. https://doi.org/10.5281/zenodo.1212496

Fenner, M., Crosas, M., Grethe, J. S., Kennedy, D., Hermjakob, H., Rocca-Serra, P., Durand, G., Berjon, R., Karcher, S., Martone, M., & Clark, T. (2019). A data citation roadmap for scholarly data repositories. *Scientific Data*, *6*, Article 28. https://doi.org/10.1038/s41597-019-0031-8

Kitzes, J., Turek, D., & Deniz, F. (Eds.). (2018). *The practice of reproducible research: Case studies and lessons from the data-intensive sciences*. University of California Press. ISBN 978-0-520-29673-3

Klump, J., & Huber, R. (2017). 20 years of persistent identifiers: Which systems are here to stay? *Data Science Journal*, *16*, Article 9. https://doi.org/10.5334/dsj-2017-009

Noble, W. S. (2009). A quick guide to organizing computational biology projects. *PLoS Computational Biology*, *5*(7), e1000424. https://doi.org/10.1371/journal.pcbi.1000424

Nosek, B. A., Alter, G., Banks, G. C., Borsboom, D., Bowman, S. D., Breckler, S. J., Buck, S., Chambers, C. D., Chin, G., Christensen, G., Contestabile, M., Dafoe, A., Eich, E., Freese, J., Glennerster, R., Goroff, D., Green, D. P., Hesse, B., Humphreys, M., … Yarkoni, T. (2015). Promoting an open research culture. *Science*, *348*(6242), 1422–1425. https://doi.org/10.1126/science.aab2374

Piwowar, H. A., & Vision, T. J. (2013). Data reuse and the open data citation advantage. *PeerJ*, *1*, e175. https://doi.org/10.7717/peerj.175

Sandve, G. K., Nekrutenko, A., Taylor, J., & Hovig, E. (2013). Ten simple rules for reproducible computational research. *PLoS Computational Biology*, *9*(10), e1003285. https://doi.org/10.1371/journal.pcbi.1003285

Wilkinson, M. D., Dumontier, M., Aalbersberg, I. J., Appleton, G., Axton, M., Baak, A., Blomberg, N., Boiten, J.-W., da Silva Santos, L. B., Bourne, P. E., Bouwman, J., Brookes, A. J., Clark, T., Crosas, M., Dillo, I., Dumon, O., Edmunds, S., Evelo, C. T., Finkers, R., … Mons, B. (2016). The FAIR Guiding Principles for scientific data management and stewardship. *Scientific Data*, *3*, Article 160018. https://doi.org/10.1038/sdata.2016.18

---

**Booklet ID.** `003-04-0001`
**Version.** `0.1.0`
**Date.** 2026-06-21
**License.** This booklet is licensed under CC BY-NC-SA 4.0. https://creativecommons.org/licenses/by-nc-sa/4.0/
**Approximate word count.** 2221 (English body text)
**Verified citations.** 9
**Fabricated citations.** 0
**Previous booklet.** [`003-03-0001`](../003-03-0001/en.md). Material Passport. Tracking Sources Across Sessions
**Next booklet.** [`004-01-0001`](../../004-vault-architecture/004-01-0001/en.md). Folder Discipline and the Maps of Content (MOC) Pattern
