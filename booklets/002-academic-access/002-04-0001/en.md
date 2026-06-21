---
title_en: "DergiPark, ULAKBIM TR Dizin, HEAL-Link, and Regional Indexing"
title_tr: "DergiPark, ULAKBİM TR Dizin, HEAL Link ve Bölgesel İndeksleme"
booklet_id: "002-04-0001"
category: "002-academic-access"
language: "en"
version: "0.2.0"
date_published: "2026-05-24"
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
translation_notes: "English re-authored from the finalized Turkish source (v0.2.0, 2026-06-21), not a literal translation. Regional terminology (DergiPark, TR Dizin, HEAL-Link, akademik teşvik) preserved with explanatory glosses for an international reader. Content, argument structure, and section order follow the Turkish canon."
license:
  - "CC-BY-NC-SA-4.0 (prose)"
status: "release"
signature_booklet: true
---

# DergiPark, ULAKBIM TR Dizin, HEAL-Link, and Regional Indexing

This booklet opens the academic access category of the Claude Code for Social Scientists guide. The preceding category addressed what Claude Code is, its agentic logic, installation, and the discipline of persistent instructions. This booklet turns to the first serious question that arises after setup: how does a social scientist working in Turkish, Greek, and English reach the academic literature reliably — and how does that access connect responsibly to a Claude Code workflow?

The question appears technical, but it is not only technical. A literature search is shaped by which sources the researcher sees, which are left out, and which are trusted. When a search runs only through Web of Science, Scopus, or Google Scholar, a substantial portion of Turkish- and Greek-language scholarship may remain invisible. That invisibility does not merely reduce the source count; it also weakens the contextual grounding, the conceptual map, and the regional sensitivity of the research question itself.

The aim of this booklet is to treat regional academic infrastructure as a methodological layer that cannot be set aside when working with Claude Code. DergiPark, ULAKBİM TR Dizin, the Council of Higher Education Thesis Center, HEAL-Link, EZproxy, institutional VPN, and multilingual citation practice are discussed here not simply as access tools but as the infrastructure that determines the scope and integrity of scholarly output.

The booklet's central claim is this: regional indexing is not a secondary detail for the social scientist. For a researcher working in Turkish and Greek, it is one of the necessary conditions for constructing the literature fairly, completely, and in a manner open to scrutiny. Claude Code can facilitate this process, but it cannot evaluate access rights, source quality, or institutional limits on the researcher's behalf.

## 1. The Gap That International Guides Do Not See

Most international guides to AI-assisted academic work assume English-language literature and the indexing infrastructure of the English-speaking world. Web of Science, Scopus, Google Scholar, and Semantic Scholar are treated in these guides as natural starting points. These databases are important. But they do not represent the full range of academic output in the social sciences.

This representational gap is not new. Van Leeuwen and colleagues (2001) demonstrated how language bias in the Science Citation Index affects comparisons of national research performance. Mongeon and Paul-Hus (2016) compared the journal coverage of Web of Science and Scopus and showed empirically that these databases do not offer equal coverage across languages, disciplines, and publication types.

The implications are direct for the Turkish and Greek contexts. A social scientist in Türkiye or Greece who conducts a search relying only on international databases may miss a substantial portion of the regional literature in their own field. This becomes still more critical in systematic reviews, doctoral thesis scans, theoretically grounded work with local context, and research on minority communities.

Regional indexing infrastructure should therefore be seen not as an advanced optional feature but as a mandatory part of a consistent academic workflow. Claude Code does not know this infrastructure by default. The researcher must explicitly define which index does what, how each source is to be verified, and which access channel operates within which ethical limits.

## 2. DergiPark and the Crossref Bridge

DergiPark is an open-access publishing platform hosted by TÜBİTAK ULAKBİM that brings hundreds of Turkish academic journals under a single roof (TÜBİTAK ULAKBİM, 2024). One of DergiPark's most important features for the social scientist is that many of its articles can be connected to the international bibliographic infrastructure via a Digital Object Identifier — a DOI. A DOI is a robust and permanent identifier that gives reliable access to a record.

When working with Claude Code, a DOI provides an important handle for managing Turkish-language literature. If a DergiPark article carries a DOI, Claude Code can use it to retrieve bibliographic metadata, convert the record to APA 7 format, add it to a reference file, or check consistency across a bibliography. The critical point here is this: Claude Code should not invent citations. It should work with metadata verified through a DOI.

Crossref content negotiation offers a practical bridge at this point. By sending a request to a DOI address specifying a desired format, the article's record can be retrieved in structured form. BibTeX format can be requested as follows.

```bash
curl -LH "Accept: application/x-bibtex" https://doi.org/10.3390/publications7010018
```

The DOI in this example belongs to a Crossref-registered article; DergiPark DOIs use the same bibliographic logic. This means Turkish-language literature is no longer confined to a manually entered local reference list — it becomes connected to the international reference infrastructure.

This bridge is valuable on two counts. First, it reduces bibliographic errors. Second, it enables Turkish sources to be cited in international texts in a structured and verifiable way. That said, a DOI does not guarantee the methodological quality of an article. A DOI is an access and identification tool. Scholarly evaluation remains the researcher's responsibility.

## 3. ULAKBİM TR Dizin and the National Quality Filter

ULAKBİM TR Dizin serves a different function from DergiPark. DergiPark is a publishing platform; TR Dizin is Türkiye's national citation index, covering journals that meet defined evaluation criteria (TÜBİTAK ULAKBİM, 2026). The distinction matters. A journal's presence on DergiPark is not equivalent to its inclusion in TR Dizin.

TR Dizin evaluates journals against criteria covering publication ethics, peer review process, editorial structure, regularity, and formal standards. For this reason it carries particular weight in Türkiye's academic incentive schemes, appointment procedures, promotion reviews, doctoral qualification processes, and institutional evaluations. For the social scientist, TR Dizin is not simply a bibliographic register — it is an indicator with concrete consequences for national academic visibility and institutional assessment.

The coverage gap identified by Mongeon and Paul-Hus (2016) has a direct practical correlate here. In the social sciences, many journals indexed in TR Dizin do not appear in Web of Science or Scopus. Their absence does not mean the journals lack scholarly merit; most often it reflects the coverage policies, language preferences, and disciplinary priorities of the international commercial databases.

When conducting a literature scan with Claude Code, TR Dizin status should be tracked as a distinct field. For example, a source table might record, alongside the journal name, DOI, publication year, and sample type, whether the journal falls within TR Dizin coverage. This keeps the distinction between international visibility and national academic evaluation explicit and visible throughout the search.

## 4. The Council of Higher Education Thesis Center and Institutionally Scrutinised Knowledge

The Council of Higher Education National Thesis Center is the central archive of master's and doctoral theses completed at Turkish universities (YÖK, 2026). For the social science researcher, this archive offers a distinctive type of source. Theses typically contain more detailed methods sections, broader literature discussions, and more extensive contextual explanation than corresponding journal articles.

The scholarly value of theses derives not from placing them in the same category as published articles but from their passage through institutional scrutiny. A doctoral thesis is not a peer-reviewed journal article. However, because it has been subject to supervisory oversight, jury evaluation, and university approval, it can offer important grounding for tracking the development of a field.

When working with Claude Code, it is worth maintaining a consistent record template for Council of Higher Education Thesis Center entries. Most theses carry no DOI, so fields such as author name, thesis title, year, university, institute, thesis type, and access address must be recorded in a standard format. Claude Code can assist in converting this information to APA 7 format. However, the accuracy of the citation data must be verified by the researcher against the Thesis Center record.

This archive provides a layer of sources invisible to international databases, particularly for work situated in the Turkish context. When building a regional literature map, theses should be treated not only as supplementary material but as institutional traces showing the historical development of the field.

## 5. HEAL-Link and Greece's Consortium Infrastructure

On the Greek side, one of the foundational academic access infrastructures is HEAL-Link, the Hellenic Academic Libraries Link consortium (HEAL-Link, 2026). HEAL-Link operates as a shared subscription consortium of Greek academic libraries, providing member institutions with access to major publisher packages. This structure plays an important role in connecting university researchers in Greece to international literature.

The context of Democritus University of Thrace in Komotini offers a concrete example. When a researcher wishes to access an article through HEAL-Link, the process typically runs through institutional authentication. Off campus, systems such as EZproxy or similar proxies come into play. These systems connect the user's institutional membership to the publisher's access control.

```text
User -> Institutional login (EZproxy or VPN) -> Publisher access control -> Full text
```

Claude Code's role here must be kept carefully bounded. Claude Code should not be used as a tool that automatically bulk-downloads subscription content using the researcher's institutional identity. Instead it should serve as a working assistant organizing article records, DOI information, access addresses, and source tables. Full-text access must remain within the limits of the researcher's own institutional account and the library's licensing terms.

This distinction is important both practically and ethically. Claude Code can facilitate access; it does not hold access rights. Institutional subscriptions are personal, non-transferable, and bounded by publisher agreements.

## 6. EZproxy and Institutional VPN Realities

Off-campus access is one of the practical thresholds of academic work in both Türkiye and Greece. EZproxy and institutional VPN systems carry the researcher's institutional identity to publisher systems, making subscription content reachable from outside campus. But this access has firm limits.

First, access is personal. It is tied to the researcher's institutional account and cannot be shared with others. Second, when a researcher leaves the institution or authorization expires, the right of access expires with it. Third, many publisher agreements explicitly prohibit automated bulk downloading. A workflow in which Claude Code downloads hundreds of full texts in a single session therefore carries both ethical and institutional risk.

From these constraints the basic rule of the regional workflow follows. Claude Code should operate at the level of records, DOIs, access addresses, abstracts, source tables, and index information. Full-text access must be conducted through the researcher's own browser, the researcher's own institutional identity, and within the applicable licensing conditions.

This rule may appear to constrain the researcher's pace to some degree. In the long run, however, it keeps access sustainable. It prevents institutional subscriptions from being suspended, publisher agreements from being violated, and the research team's access rights from being put at risk.

## 7. Where Indexing Sits in the Academic Incentive System

In Türkiye, academic incentive schemes and similar institutional evaluation processes produce concrete outcomes based on which indexes a journal is covered by. Indexing information is therefore not merely a bibliographic detail — it is a criterion that shapes the researcher's journal selection, publication strategy, and institutional profile.

This booklet does not assign specific incentive scores, because incentive regulations and their institutional applications change over time. The durable principle is this: the database in which a publication is indexed affects how the academic is positioned in the context of institutional evaluation. For this reason, when working with Claude Code on journal selection, literature scanning, or publication strategy, indexing status should be kept as a distinct field.

For instance, when preparing a journal list, the journal's status across Web of Science, Scopus, TR Dizin, DergiPark, DOAJ, and other relevant indexes can be shown in separate columns. This allows the researcher to examine not only subject alignment but also visibility and evaluation conditions. It makes publication strategy more transparent and open to scrutiny.

## 8. A Literature Scan Across Language Boundaries

Consider a social anxiety researcher who wants to assess Turkish, Greek, and English literature within a single study. The conventional approach requires running searches across separate interfaces for three languages and three access layers, merging results manually, and working through deduplication. This is manageable, but it is open to error and time loss.

With Claude Code a more structured approach is possible. The source layers are defined at the outset: international databases for English-language literature, DergiPark, ULAKBİM TR Dizin, and the Council of Higher Education Thesis Center for Turkish literature, and HEAL-Link together with institutional access routes for Greek and internationally subscribed literature.

Each record's language, the index through which it was found, and the access route by which it was retrieved are then kept in distinct fields. This matters not only for collecting sources but for monitoring the scope of the scan itself. The researcher can track explicitly how many sources were identified in each language, which source types remain underrepresented, and which access obstacles were encountered.

The Model Context Protocol — MCP — can provide structured access to bibliographic tools in workflows of this kind. MCP connections must, however, be configured and bounded by the user. It must be clear which source Claude Code is accessing and with what authorization. The structure below is given only as a skeleton to illustrate the architecture; the actual server name and arguments will vary according to the bibliographic MCP the researcher uses.

```json
{
  "mcpServers": {
    "bibliographic-search": {
      "command": "<bibliographic MCP server>",
      "args": ["--source", "crossref"],
      "env": {}
    }
  }
}
```

The purpose of this structure is not to bulk-download full texts automatically. The purpose is to run record-level operations through a structured and auditable tool. Full-text access remains within the researcher's institutional identity and licensing conditions.

Tenopir and colleagues (2019), in an international study examining how researchers discover, read, and use scholarly articles, found that access obstacles push researchers toward developing alternative strategies. This booklet draws the following conclusion from that finding: workflows that reduce access friction while preserving licensing and ethical boundaries carry high practical value for the social scientist. That conclusion extends beyond the finding Tenopir and colleagues directly established; it represents this guide's own methodological inference applied to multilingual Claude Code workflows.

## 9. Cross-Language Citation Considerations

Using a Turkish or Greek source in an English article is not merely a matter of formal citation. It is also a question of visibility, translation, and conceptual representation. APA 7 permits preserving titles in their original language and, where needed, providing an English translation in square brackets. This practice preserves the original identity of the source while providing accessibility for English-language readers.

Claude Code can assist in formatting a citation of this kind. However, title translation is the researcher's responsibility. The field-specific meaning of concepts is too sensitive to be delegated to the model without verification. Particularly in psychology, educational sciences, political science, and minority studies, an incorrect translation produces not merely a language error but a conceptual distortion.

Larivière and colleagues (2015), in their analysis of the oligopolistic structure of academic publishing in the digital era, showed that which output is visible is to a large extent determined by commercial infrastructure. The conclusion this booklet draws from that finding is as follows: citing a Turkish or Greek source accurately in an English article is a small but meaningful way of carrying regional scholarly output into international debate.

## 10. User Agreements and the Ethical Layer

Academic access is not only technical access. Every library, consortium, and publisher package operates under specific user agreements. These agreements define what material may be downloaded, how it may be stored, with whom it may not be shared, and which forms of automation are prohibited.

These limits must be explicitly observed in any Claude Code workflow. Automated bulk downloading must not be performed. Subscription full texts must not be transferred outside the consortium. Institutional access must not be used as if it were a non-personal data reservoir. These rules are important not only legally but also in terms of academic ethics: institutional access rights are a shared resource affecting the entire research community.

Source quality is also part of this ethical layer. Demir (2018), examining the patterns of publishing in predatory journals, found that institutional pressures and academic incentive mechanisms can direct researchers toward low-quality journals. This finding should not be confined to a single country, but it deserves careful attention in regional academic contexts where publication pressure is strong.

This booklet names no specific journals, because journal lists change and a mistaken classification can carry serious consequences. Instead it proposes a multi-layered assurance: TR Dizin coverage, institutional library approval, publisher transparency, peer review information, open science principles, and source verification should be evaluated together. UNESCO's open science recommendation provides an international policy foundation that treats access, quality, and equity as a coherent whole (UNESCO, 2021).

## 11. Bridge to the Memory System

All the access layers discussed in this booklet generate records. DOI records, TR Dizin status, DergiPark links, Council of Higher Education Thesis Center citations, publisher pages reached through HEAL-Link, scan tables, three-language source lists, and access notes. Their value lies not only in their use within the session but in their being findable again later.

Academic access is therefore directly connected to memory and archive architecture. Once a source is found, it should not disappear in the next session. The language, index, access route, and usage constraints of each source must be recorded.

The next category addresses this question. How is academic memory turned into an archive? How are source records, decisions, notes, and scan outputs preserved over years? How does a social scientist working with Claude Code move from temporary session outputs to a persistent, retrievable research archive?

Booklet 003-01-0001, Memory as Vault: A First-Principles Introduction, continues from this point.

## References

Citations are in APA 7 format. All DOIs were independently verified against Crossref. Institutional URLs were confirmed accessible as of 2026-06-21.

Demir, S. B. (2018). Predatory journals: Who publishes in them and why? *Journal of Informetrics*, 12(4), 1296–1311. https://doi.org/10.1016/j.joi.2018.10.008

HEAL-Link. (2026). *Hellenic Academic Libraries Link consortium*. https://www.heal-link.gr

Larivière, V., Haustein, S., & Mongeon, P. (2015). The oligopoly of academic publishers in the digital era. *PLOS ONE*, 10(6), e0127502. https://doi.org/10.1371/journal.pone.0127502

Mongeon, P., & Paul-Hus, A. (2016). The journal coverage of Web of Science and Scopus: A comparative analysis. *Scientometrics*, 106(1), 213–228. https://doi.org/10.1007/s11192-015-1765-5

Tenopir, C., Christian, L., & Kaufman, J. (2019). Seeking, reading, and use of scholarly articles: An international study of perceptions and behavior of researchers. *Publications*, 7(1), 18. https://doi.org/10.3390/publications7010018

TÜBİTAK ULAKBİM. (2024). *DergiPark Akademik platform*. https://dergipark.org.tr

TÜBİTAK ULAKBİM. (2026). *TR Dizin journal evaluation criteria*. https://trdizin.gov.tr

UNESCO. (2021). *UNESCO recommendation on open science* (SC-PCB-SPP/2021/OS/UROS). https://unesdoc.unesco.org/ark:/48223/pf0000379949

van Leeuwen, T. N., Moed, H. F., Tijssen, R. J. W., Visser, M. S., & van Raan, A. F. J. (2001). Language biases in the coverage of the Science Citation Index and its consequences for international comparisons of national research performance. *Scientometrics*, 51(1), 335–346. https://doi.org/10.1023/A:1010549719484

YÖK. (2026). *Council of Higher Education National Thesis Center*. https://tez.yok.gov.tr

---

**Booklet ID.** `002-04-0001`
**Version.** `0.2.0`
**Date.** 2026-06-21
**License.** This booklet is licensed under CC BY-NC-SA 4.0. https://creativecommons.org/licenses/by-nc-sa/4.0/
**Word count (approx.).** 2246 (English body text, measured with wc)
**Verified citations.** 10
**Hallucinated citations.** 0
**Previous booklet.** [`001-02-0001`](../../001-foundations/001-02-0001/en.md). Research Lifecycle Map, From Idea to Publication, From Publication to Archive
**Next booklet.** [`002-05-0001`](../002-05-0001/en.md). Systematic Reviews and Scoping Reviews, From Search to PRISMA Flow
