---
title_en: "Material Passport: Tracking Sources Across Sessions"
title_tr: "Kaynak Pasaportu: Kaynakları Oturumlar Arası İzlemek"
booklet_id: "003-03-0001"
category: "003-memory-system"
language: "en"
version: "0.1.0"
date_published: "2026-06-12"
date_last_revised: "2026-06-20"
authors:
  - name: "Onour Impram"
    orcid: "0000-0003-1076-3928"
    role: "author, principal reviewer"
ai_assisted: true
ai_tools:
  - name: "Claude Code"
    vendor: "Anthropic"
    model_alias: "claude-fable-5"
    model_dated: null  # no dated identifier published by Anthropic for Fable 5 as of 2026-06-12
    role: "drafting, verification, citation lookup, bilingual re-authoring"
    interaction_mode: "interactive console"
ai_contribution_level: "substantial-drafting"
human_review: "complete"
human_review_date: "2026-06-20"
verified_citations_count: 6
fabricated_citations_count: 0
disclosure_standard: "COPE 2023 + WAME 2023 + ICMJE 2024 + STM 2025 + EU AI Act 2024/1689 Art. 50 + ENAI"
translation_notes: "English re-authored from the Turkish source, not a literal translation. The passport entry example is synthetic in its discovery details and uses a reference from this booklet's own verified list, in keeping with the vault sanitization protocol. Citation audit 2026-06-12: all DOIs verified live against Crossref before drafting; the Wilkinson et al. author list follows the APA 7 twenty-plus rule with the order taken from the Crossref record. The FAIR alignment in section four is explicitly marked as the guide's own analogy, since FAIR is defined at institutional scale."
license:
  - "CC-BY-NC-SA-4.0 (prose)"
status: "release"
---

# Material Passport: Tracking Sources Across Sessions

The first booklet in this category set out the principles of turning memory into an archive. This booklet brings an identity regime to the archive's most mobile resident, the source. In engineering, a material passport is the record that documents where every component in a structure came from and what properties it carries. Carried over to a research archive, the same idea becomes the source passport. Every article, book, and report that enters the archive carries an identity line saying where it was found, with which query it arrived, whether it has been verified, and in which draft it has been used. This booklet describes the fields of that line, the moment it should be written, and how Claude Code keeps it effortless.

## 1. The Passport Metaphor

A source's life does not end at the moment of discovery. It begins there. The article found in today's catalog search reappears three weeks later in a draft's discussion section and three months later in a response to reviewers. The same questions return at every appearance. Where did I find this? Was the reference verified? Which claim was it carrying? The passport attaches the answers to the source itself, so that when the question arises, what is searched for in the archive is a record, not a recollection.

The strength of the metaphor is its portability. The passport belongs to the source and travels with it. Sessions change, projects change, drafts change hands. The identity line stays put.

## 2. Why a Ledger Is Needed

The root of the problem is the difference between finding and keeping found. Jones (2007), surveying the field of personal information management, shows that the hard part is not finding information but keeping found information findable again. A researcher touches dozens of sources every week, and every touched source, if no record was made, is a stranger again a few sessions later. The cost of re-finding accumulates silently. The same article is searched for twice, the same abstract read twice, the same decision made twice.

The ledger trades that cost for a one-time recording effort. A line is written at the moment of discovery, and that line stands in for every future act of re-finding. The principle of the memory booklet takes its most concrete form here. Whatever would have to be held in mind is moved from mind to file.

## 3. The Fields of the Passport

A passport line answers six things. The reference and its DOI. Where it was found and with which query. The date of discovery. The access route: open access, institutional subscription, print copy. The verification status: on which date the record was confirmed against which catalog. The place of use: which claim it carries, in which section of which draft.

The example below is synthetic in its discovery details and exists to show the form.

> **Source.** Sandve, G. K., Nekrutenko, A., Taylor, J., & Hovig, E. (2013). Ten simple rules for reproducible computational research. https://doi.org/10.1371/journal.pcbi.1003285
> **Found.** PubMed search, "reproducible research rules", 2026-06-12.
> **Access.** Open access.
> **Verification.** Crossref, 2026-06-12, record matched.
> **Use.** Methods section draft, provenance paragraph.
> **Note.** The provenance-tracking rule comes from this paper.

Six fields is a deliberate ceiling. A record that takes under a minute to fill gets written. A form that takes a quarter of an hour does not.

## 4. Alignment with the FAIR Principles

This personal regime has a counterpart at the institutional layer of data stewardship. Wilkinson and colleagues (2016) set out the FAIR principles for scientific data management: findability, accessibility, interoperability, reusability. The spine of the principles is that every object carries rich metadata and a persistent identifier. The source passport can be read as that spine brought down to the personal archive layer. The DOI is the persistent identifier, the passport fields are the metadata, and the ledger itself builds findability inside the archive.

The analogy should be used with its limits in view. FAIR is defined at the scale of institutions and repositories. The passport is one researcher's ledger. What the two share is the principle. An object without an identity, at any scale, is a candidate for loss.

## 5. Recording Inside the Session

Half the passport's value lies in when it is written. The right moment is the moment the source enters the archive. If a record returned over the catalog bridge looks useful, its passport line is opened in that same session. A record postponed is, most of the time, a record never written, because the context of discovery, which query, toward which purpose, evaporates when the session closes.

The infrastructure of the earlier booklets converges here. For a source that came over a bridge, the query and the date are already known, and the model can fill those fields on its own. A single check added to the session-closing ritual seals the system. Did any source enter a draft this session without a passport? If so, the line is written before the close.

## 6. A Reproducible Search Record

The systematic review tradition offers the most mature example of search documentation. Bramer and colleagues (2017), studying optimal database combinations for systematic review searches, treat the recording of which catalogs were searched with which queries as a constitutive part of the process. Even for the researcher not running a full systematic review, the lesson is plain. A search whose query and date are recorded becomes a repeatable operation.

The passport ledger is that discipline adapted to everyday scale. The query and date fields in every line allow the same search to be rerun months later. When the methods section asks for the search strategy, the answer rests on the ledger, not on recall.

## 7. Provenance and Reproduction

Sandve and colleagues (2013), compiling the rules of reproducible computational research, put provenance first: for every result, how it was produced must be traceable. The provenance of a claim in a draft is the source that carries it, and the passport's use field builds exactly that trace. When the claim is questioned, the chain is ready. Sentence, source, reference, verification date.

Noble (2009), in his guide to organizing computational projects, observes that everything will probably have to be done over again, and that organization should make the doing-over possible even for a stranger. The stranger, most of the time, is your future self. The author returning to a revision six months later does not have to run an archaeology of their own decisions, because the ledger already holds them.

## 8. The Passport Against Fabrication

The ledger's function at the integrity layer is its sternest. Walters and Wilder (2023) documented the scale of fabricated records in ChatGPT-generated bibliographies. This guide's citation discipline requires every reference to be verified against a catalog, and the passport is that requirement's enforcer inside the archive. The rule is one sentence. A source without a passport does not enter the bibliography.

The rule's strength is that it mechanizes. Put the draft's bibliography next to the passport ledger and three lists fall out. Sources with passports and uses, the healthy core. Citations without passports, the verification queue. Passports without uses, reserves that may serve later. As the first list grows, the bibliography's reliability becomes structural.

## 9. The Passport Ledger with Claude Code

Maintaining the ledger is the kind of work the model does best. Appending a passport line in the correct form, filling the query and date fields for a source that came over a bridge, comparing bibliography against ledger and reporting the three lists. The question of which sources carry the discussion section becomes, with a ledger in place, a search command.

The boundary stands where it always stands. Whether a source is useful, which claim it will carry, and what goes into the note are the researcher's decisions. The model keeps the ledger. The researcher decides what the ledger gets to say. As the recording mechanizes, the time left for judgment grows, and that is the real return of the regime.

## 10. Bridge, to the Ledger's Home

The passport ledger is a file in the archive, and like every file it needs an address. Where does the ledger live, how does it relate to the daily logs, where does it hang in the map of content? The system for those questions is folder discipline. The next booklet builds the archive's folder architecture and the Maps of Content pattern. The passport's home is ready there.

## References

Citations are in APA 7 format. DOIs verified against Crossref on 2026-06-12.

Bramer, W. M., Rethlefsen, M. L., Kleijnen, J., & Franco, O. H. (2017). Optimal database combinations for literature searches in systematic reviews: A prospective exploratory study. *Systematic Reviews*, 6(1), Article 245. https://doi.org/10.1186/s13643-017-0644-y

Jones, W. (2007). Personal information management. *Annual Review of Information Science and Technology*, 41(1), 453–504. https://doi.org/10.1002/aris.2007.1440410117

Noble, W. S. (2009). A quick guide to organizing computational biology projects. *PLoS Computational Biology*, 5(7), e1000424. https://doi.org/10.1371/journal.pcbi.1000424

Sandve, G. K., Nekrutenko, A., Taylor, J., & Hovig, E. (2013). Ten simple rules for reproducible computational research. *PLoS Computational Biology*, 9(10), e1003285. https://doi.org/10.1371/journal.pcbi.1003285

Walters, W. H., & Wilder, E. I. (2023). Fabrication and errors in the bibliographic citations generated by ChatGPT. *Scientific Reports*, 13, Article 14045. https://doi.org/10.1038/s41598-023-41032-5

Wilkinson, M. D., Dumontier, M., Aalbersberg, I. J., Appleton, G., Axton, M., Baak, A., Blomberg, N., Boiten, J.-W., da Silva Santos, L. B., Bourne, P. E., Bouwman, J., Brookes, A. J., Clark, T., Crosas, M., Dillo, I., Dumon, O., Edmunds, S., Evelo, C. T., Finkers, R., … Mons, B. (2016). The FAIR Guiding Principles for scientific data management and stewardship. *Scientific Data*, 3, Article 160018. https://doi.org/10.1038/sdata.2016.18

---

**Booklet ID.** `003-03-0001`
**Version.** `0.1.0`
**Date.** 2026-06-20
**License.** This booklet is licensed under CC BY-NC-SA 4.0. https://creativecommons.org/licenses/by-nc-sa/4.0/
**Approximate word count.** 1415 (English body text, measured with wc)
**Verified citations.** 6
**Hallucinated citations.** 0
**Previous booklet.** [`003-01-0001`](../003-01-0001/en.md). Memory as Vault, A First-Principles Introduction
**Next booklet.** [`004-01-0001`](../../004-vault-architecture/004-01-0001/en.md). Folder Discipline and the Maps of Content (MOC) Pattern
