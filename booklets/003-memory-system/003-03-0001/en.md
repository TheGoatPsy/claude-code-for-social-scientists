---
title_en: "Material Passport. Tracking Sources Across Sessions"
title_tr: "Kaynak Pasaportu. Kaynakları Oturumlar Arasında İzlemek"
booklet_id: "003-03-0001"
category: "003-memory-system"
language: "en"
version: "0.2.0"
date_published: "2026-06-12"
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
verified_citations_count: 6
fabricated_citations_count: 0
disclosure_standard: "COPE 2023 + WAME 2023 + ICMJE 2024 + STM 2025 + EU AI Act 2024/1689 Art. 50 + ENAI"
translation_notes: "English re-authored from the finalized Turkish source (v0.2.0, 2026-06-21), not a literal translation. Body follows the Turkish section structure and argumentation; register adapted to fluent scholarly English throughout. The passport entry example is synthetic in its discovery details and uses a reference from this booklet's own verified list, in keeping with the vault sanitization protocol. Citation audit 2026-06-21: all DOIs verified against Crossref; the Wilkinson et al. author list follows the APA 7 twenty-plus rule with the order taken from the Crossref record. The FAIR alignment in section four is explicitly framed as the guide's own analogy, since FAIR is defined at institutional scale."
license:
  - "CC-BY-NC-SA-4.0 (prose)"
status: "release"
---

# Material Passport. Tracking Sources Across Sessions

## Introduction

The first booklet in this category established the principles of turning memory into an archive. This booklet brings an identity regime to the archive's most mobile element: the source.

In engineering, a material passport is the record documenting where every component in a structure came from, what properties it carries, and what history of use it has accumulated. Transferred to the research archive, the same idea becomes the source passport. Every article, book, report, or thesis entering the archive carries an identity line showing where it was found, with which query it arrived, whether it has been verified, and in which draft it was used.

This booklet describes the fields of the passport, the moment at which it should be written, and how Claude Code can sustain the practice reliably. The core problem in source management is not only finding a source. It is keeping a found source findable, verifiable, and usable months later.

## 1. The Passport Metaphor

A source's academic life does not end at the moment of discovery; it begins there. The article found in a catalog search today may resurface three weeks later in a draft's introduction, three months later in the discussion, and six months later in a response to reviewers.

At every reappearance the same questions arise. Where did I find this? Was the reference verified? Which query led to it? Which claim was it carrying? In which draft did I use it before? If the answers to those questions live only in the researcher's memory, source management becomes fragile.

The source passport attaches those answers to the source itself. The source then ceases to be merely a PDF, a DOI, or a reference line. It lives in the archive together with its discovery context, verification status, and use history.

The strength of the metaphor is its portability. The passport belongs to the source and travels with it. Sessions change, projects change, drafts change hands. The identity line stays put.

## 2. Why a Ledger Is Needed

The root of the problem is the difference between finding and keeping found. Jones (2007), surveying the field of personal information management, shows that the hard part is rarely finding information for the first time but keeping found information findable again. That observation applies directly to academic source management.

A researcher touches many sources every week: some are skimmed, some read in depth, some incorporated into a draft, some set aside for later. If those encounters are not recorded, the same article is searched for again, the same abstract read again, the same decision made again.

The source passport reduces that silent cost. A brief record is opened at the moment of discovery. That record becomes the foundation for every future act of re-finding, re-verifying, and deciding on use. This is the source-level expression of the principle established in the memory booklets: whatever would have to be held in mind is moved from mind to file.

## 3. The Fields of the Passport

A source passport should not contain more detail than necessary; otherwise the researcher will not sustain it. The passport line should therefore be kept short enough to answer six core questions.

What is the reference and its DOI?

Where was the source found, and with which query?

On which date was it found?

What is the access route? Open access, institutional subscription, print copy, or another path.

On which date and against which catalog was the reference verified?

In which draft, which section, and carrying which claim was the source used?

The example below is synthetic and exists only to show the form.

> **Source.** Sandve, G. K., Nekrutenko, A., Taylor, J., & Hovig, E. (2013). Ten simple rules for reproducible computational research. https://doi.org/10.1371/journal.pcbi.1003285
>
> **Found.** PubMed search, "reproducible research rules", 2026-06-12.
>
> **Access.** Open access.
>
> **Verification.** Crossref, 2026-06-12, record matched.
>
> **Use.** Methods section draft, provenance paragraph.
>
> **Note.** The provenance-tracking rule comes from this paper.

Keeping the fields few is a deliberate choice. A record that cannot be completed in under a minute will eventually be abandoned. The sustainability of the passport ledger depends on its remaining short and functional.

## 4. Alignment with the FAIR Principles

The source passport is a personal archival practice, but it aligns with the broader literature on data stewardship. Wilkinson and colleagues (2016) set out the FAIR principles for scientific data management: findability, accessibility, interoperability, and reusability. Those principles were developed for institutions, data repositories, and scientific data infrastructure. The source passport operates at the scale of a single researcher's archive. The scale differs. The underlying logic is similar.

An object without an identity, without metadata, and without a persistent identifier is a candidate for loss, whether it sits in an institutional repository or in a personal archive. The DOI is the source's persistent identifier. The passport fields are its metadata. The ledger itself builds findability within the archive. The source passport can therefore be understood as a simplified adaptation of the FAIR logic to the level of the personal research archive.

## 5. Recording Inside the Session

The passport's value depends not only on which fields it contains but also on when it is written. The right moment is the moment a source enters the archive.

If a record returned from a catalog search appears useful, the passport line should be opened in that same session. A record postponed is, most of the time, a record never written. The query by which the source was found, the purpose toward which it was sought, and the context in which it appeared all blur quickly once the session closes.

The infrastructure established in earlier booklets converges here. For a source that came over the bibliographic bridge, the query, the date, and the access route are often already known. Claude Code can fill those fields as a draft. The researcher then determines whether the source is genuinely usable, which claim it will carry, and what note should accompany it.

Adding one question to the session-closing routine is usually sufficient. Did any source enter a draft in this session without a passport? If so, the passport line should be written before the session closes.

## 6. A Reproducible Search Record

The systematic review tradition offers the most developed example of search documentation. Bramer and colleagues (2017), examining optimal database combinations for systematic review searches, treat the recording of which catalogs were searched with which queries as a constitutive part of the process — not supplementary documentation but core method.

Even for a researcher not conducting a full systematic review, the principle is valuable. A search is only a repeatable operation when its query, date, database, and selection rationale have been recorded.

The source passport brings that discipline to everyday academic work. The query and date fields in every line allow the same search to be rerun months later. When the methods section asks for the search strategy, the answer rests on the ledger, not on recall.

## 7. Provenance and Reproduction

Sandve and colleagues (2013) emphasize the importance of provenance tracking in reproducible computational research: for every result, how it was produced must be traceable. In academic writing, the origin of a claim is the source that carries it. The use field of the source passport builds exactly that trace.

When a sentence is challenged, the chain should be visible. Which claim does the sentence assert? Which source supports it? Has the reference been verified? On which date and against which catalog? The answers to all of these questions should be present in the passport ledger.

Noble (2009), in his guide to organizing computational projects, observes that everything may one day have to be redone, and the most likely person to undertake that redoing is the researcher's own future self. An author returning to a revision six months later need not run an archaeology of their own decisions, because the ledger already holds them.

## 8. The Passport Against Fabrication

The ledger's most critical function is protecting source integrity. Walters and Wilder (2023) demonstrate that fabricated and erroneous references constitute a serious problem in bibliographic records generated by ChatGPT. This risk makes the passport ledger more important still in AI-assisted academic writing.

This guide's rule is clear. A source without a passport does not enter the bibliography. The rule is strong because it is mechanizable. When a draft's bibliography is placed alongside the passport ledger, three lists emerge.

Sources with passports and uses: the healthy core.

Citations without passports: the verification queue.

Passports without uses: reserves that may serve later.

As the first list grows, the bibliography's reliability ceases to depend on personal vigilance alone and becomes a structural guarantee.

## 9. The Passport Ledger with Claude Code

Maintaining the ledger is among the kinds of work Claude Code can support well. Appending a passport line in the specified form, filling query and date fields for a source that arrived via the bibliographic bridge, comparing a bibliography against the ledger, and reporting the three lists are structured tasks with clear inputs and outputs.

For example, a researcher may ask for a comparison of sources used in the discussion section against the passport ledger. The model can report passported sources, sources requiring verification, and records not yet used in any draft. Source auditing then ceases to be an exhausting cleanup performed only at the end and becomes a natural part of the writing process.

The boundary is the same as always. Whether a source is genuinely useful, what claim it will carry, and what evaluation the note field should record — those are the researcher's decisions. The model helps maintain the ledger. Scientific judgment remains with the researcher.

## 10. Bridge, to the Ledger's Home

The source passport is a file in the archive, and like every file it needs a home. Where does the passport ledger live? How does it relate to daily session logs? Under which heading in the map of content does it hang? These questions require folder discipline.

The next booklet addresses the archive's folder architecture and the Maps of Content pattern. The passport's home will take on its full meaning within that architecture.

## References

Citations are in APA 7 format. DOIs verified against Crossref on 2026-06-21.

Bramer, W. M., Rethlefsen, M. L., Kleijnen, J., & Franco, O. H. (2017). Optimal database combinations for literature searches in systematic reviews: A prospective exploratory study. *Systematic Reviews*, 6(1), Article 245. https://doi.org/10.1186/s13643-017-0644-y

Jones, W. (2007). Personal information management. *Annual Review of Information Science and Technology*, 41(1), 453–504. https://doi.org/10.1002/aris.2007.1440410117

Noble, W. S. (2009). A quick guide to organizing computational biology projects. *PLoS Computational Biology*, 5(7), e1000424. https://doi.org/10.1371/journal.pcbi.1000424

Sandve, G. K., Nekrutenko, A., Taylor, J., & Hovig, E. (2013). Ten simple rules for reproducible computational research. *PLoS Computational Biology*, 9(10), e1003285. https://doi.org/10.1371/journal.pcbi.1003285

Walters, W. H., & Wilder, E. I. (2023). Fabrication and errors in the bibliographic citations generated by ChatGPT. *Scientific Reports*, 13, Article 14045. https://doi.org/10.1038/s41598-023-41032-5

Wilkinson, M. D., Dumontier, M., Aalbersberg, I. J., Appleton, G., Axton, M., Baak, A., Blomberg, N., Boiten, J.-W., da Silva Santos, L. B., Bourne, P. E., Bouwman, J., Brookes, A. J., Clark, T., Crosas, M., Dillo, I., Dumon, O., Edmunds, S., Evelo, C. T., Finkers, R., … Mons, B. (2016). The FAIR Guiding Principles for scientific data management and stewardship. *Scientific Data*, 3, Article 160018. https://doi.org/10.1038/sdata.2016.18

---

**Booklet ID.** `003-03-0001`
**Version.** `0.2.0`
**Date.** 2026-06-21
**License.** This booklet is licensed under CC BY-NC-SA 4.0. https://creativecommons.org/licenses/by-nc-sa/4.0/
**Approximate word count.** 1703 (English body text, measured with wc)
**Verified citations.** 6
**Fabricated citations.** 0
**Previous booklet.** [`003-01-0001`](../003-01-0001/en.md). Memory as Vault. A First Principles Introduction
**Next booklet.** [`004-01-0001`](../../004-vault-architecture/004-01-0001/en.md). Folder Discipline and the Maps of Content (MOC) Pattern
