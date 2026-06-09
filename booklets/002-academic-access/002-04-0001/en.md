---
title_en: "DergiPark, ULAKBIM TR Dizin, HEAL-Link, and Regional Indexing"
title_tr: "DergiPark, ULAKBIM TR Dizin, HEAL-Link ve Bölgesel İndeksleme"
booklet_id: "002-04-0001"
category: "002-academic-access"
language: "en"
version: "0.1.0"
date_published: "2026-05-24"
date_last_revised: "2026-06-04"
authors:
  - name: "Onour Impram"
    orcid: "0000-0003-1076-3928"
    role: "author, principal reviewer"
ai_assisted: true
ai_tools:
  - name: "Claude Code"
    vendor: "Anthropic"
    model_alias: "claude-opus-4-7"
    model_dated: null  # no dated identifier published by Anthropic for Opus 4.7 as of 2026-05-24
    role: "drafting, verification, citation lookup, bilingual re-authoring"
    interaction_mode: "interactive console"
ai_contribution_level: "co-drafting"
human_review: "complete"
human_review_date: "2026-06-04"
verified_citations_count: 10
fabricated_citations_count: 0
disclosure_standard: "COPE 2023 + WAME 2023 + ICMJE 2024 + STM 2025 + EU AI Act 2024/1689 Art. 50 + ENAI"
translation_notes: "English re-authored from the Turkish source, not a literal translation. Regional terminology (DergiPark, TR Dizin, HEAL-Link, akademik teşvik) preserved with explanatory glosses for an international reader."
license:
  - "CC-BY-NC-SA-4.0 (prose)"
status: "release"
signature_booklet: true
---

# DergiPark, ULAKBIM TR Dizin, HEAL-Link, and Regional Indexing

The previous category established the installation and first session of Claude Code. This category addresses the first real question that arises after setup: how does a scholar who publishes in Turkish or Greek reach their sources reliably? This booklet is the guide's signature contribution, because it fills a category that international AI guides structurally leave empty. The aim is not a tool walkthrough but a map of regional academic infrastructure, and a way to connect that infrastructure to a Claude Code workflow.

## 1. The Structural Silence of International Guides

Almost all international guides on AI-assisted academic workflows assume English-language literature and the indexing infrastructure of the English-speaking world: Web of Science, Scopus, Google Scholar, Semantic Scholar. This infrastructure covers a large share of the world's scientific output, but not all of it. There is a structural asymmetry here, and it is not an opinion but a measured fact. Van Leeuwen and colleagues (2001) documented the language bias of the Science Citation Index and the distortion it introduces into international comparisons of national research performance. Mongeon and Paul-Hus (2016), comparing the journal coverage of Web of Science and Scopus, demonstrated empirically that both databases cover certain languages and disciplines more weakly than others.

The practical consequence of this asymmetry is direct. A social scientist in Türkiye or Greece who builds a Claude Code workflow resting only on international databases will fail to see a substantial part of the literature in their own language. A systematic review, a theoretical framework, a doctoral thesis scan: all remain incomplete because of this blind spot. Regional indexing infrastructure is therefore not an advanced feature but a mandatory component of a consistent workflow. This booklet provides the map of that component and a protocol for filling it: the Turkish and Greek infrastructures, the technical realities of access, and a concrete workflow.

## 2. DergiPark and the Crossref Bridge

DergiPark is the platform, hosted by TÜBİTAK ULAKBİM, where hundreds of Turkish academic journals are published under a single roof (TÜBİTAK ULAKBİM, 2024). For the social scientist, DergiPark's most important feature is its integration with Crossref. That integration means the articles on the platform receive a Digital Object Identifier, a DOI. The DOI is the most reliable handle for reaching an article through Claude Code, because it is the permanent, unchanging address of a record in the international bibliographic infrastructure.

In practice this works as follows. Given the DOI of a DergiPark article, Claude Code can retrieve the bibliographic metadata through that DOI via a mechanism called DOI content negotiation: a request to a DOI address that specifies a desired format returns the article's record in that format.

```bash
# Retrieve a DOI's metadata as BibTeX — the same Crossref content negotiation a DergiPark DOI uses
curl -LH "Accept: application/x-bibtex" https://doi.org/10.3390/publications7010018
```

This command routes through doi.org to Crossref and returns the article's record as BibTeX. (The DOI in this example is any Crossref-registered article; DergiPark DOIs use the same mechanism.) Once the record arrives, Claude Code can convert it to APA 7, add it to a reference file in your vault, or check its consistency against your bibliography. DergiPark's Crossref integration is the bridge that connects Turkish literature to the international bibliographic infrastructure. Without this bridge, Turkish sources would have to be entered manually each time.

## 3. ULAKBİM TR Dizin and the National Quality Filter

ULAKBİM TR Dizin is Turkey's national citation index, and it serves a function distinct from DergiPark (TÜBİTAK ULAKBİM, 2026). Where DergiPark is a publishing platform, TR Dizin is a quality filter. A journal's inclusion in TR Dizin means it meets evaluation criteria covering publication ethics, peer review process, and formal standards. This distinction matters for the social scientist: according to TÜBİTAK ULAKBİM's published guidance, journals indexed in TR Dizin carry weight in doctoral qualification, academic incentive, and appointment and promotion procedures in Türkiye.

The structural coverage gap demonstrated by Mongeon and Paul-Hus (2016) has a direct practical consequence here. In the social sciences, a substantial share of the journals in TR Dizin do not appear in Web of Science or Scopus. Their absence reflects the coverage policies of international commercial databases and says nothing about their scholarly merit. A Turkish social scientist therefore often has to track TR Dizin manually. Claude Code can take on a filtering role here: while conducting a literature scan, you can instruct the model to collect only the journals within TR Dizin coverage under a separate heading. This organizes the scan output according to the requirements of national evaluation processes, making the distinction between international and national visibility explicit in every search run.

## 4. YÖK Thesis Center and Institutionally Scrutinised Knowledge

The Council of Higher Education Thesis Center is the central archive of theses completed at Turkish universities since 1987 (YÖK, 2026). This archive occupies a distinctive place in the social scientist's toolkit. A doctoral thesis, unpublished yet subject to institutional scrutiny, typically offers a more detailed methods section and a broader literature review than the corresponding journal article. Theses are also accessible chronologically, making the Center the best instrument for tracing the historical development of a field in Türkiye.

Because theses carry no DOI, the metadata must be entered manually. Keeping a standard thesis record template in your vault preserves consistency across subsequent scans. When you give the model a thesis record, you can ask it to convert the entry to APA 7 unpublished doctoral dissertation format and add it to your reference file. The Thesis Center is a source type that international databases cover almost not at all, and it is therefore a distinguishing part of the regional workflow.

## 5. HEAL-Link and Greece's Consortium Infrastructure

On the Greek side the fundamental infrastructure is HEAL-Link, the Hellenic Academic Libraries Link consortium (HEAL-Link, 2026). HEAL-Link brings together Greek academic institutions under a shared subscription umbrella, providing member institutions with access to the packages of large publishers such as Springer Nature, Wiley, and Elsevier. Because Greece is a member of the European Union, the consortium's operations are shaped, at least in part, by Union-level open access policies, though the precise alignment of any given publisher agreement with those policies depends on the specific contract and is not automatic.

Democritus University in Komotini offers a concrete example. When a psychology researcher at Democritus wishes to access a journal article through HEAL-Link, the access proceeds through institutional authentication, typically via an intermediary system called EZproxy. EZproxy connects the user's institutional account to the publisher's access control, so that subscription content can be reached from off campus as well.

```text
# The basic logic of access through EZproxy
User -> Institutional login (EZproxy) -> Publisher access control -> Full text
```

Claude Code does not download full text directly in this chain: full-text access is tied to the user's institutional identity and must remain within the limits of the user agreement. Instead, Claude Code organizes the article's record, its DOI, and its access address, making it easier for the user to reach the full text through their own browser.

## 6. EZproxy and Institutional VPN Realities

Off-campus access can be a practical obstacle in both Türkiye and Greece. EZproxy and institutional VPNs make subscription resources reachable by carrying the user's institutional identity, but this access has firm limits. Access is personal and non-transferable: when a researcher leaves the institution, it ends. Automated bulk downloading is explicitly prohibited in most publisher agreements, and a Claude Code workflow that attempts to retrieve hundreds of articles in a single session may cause the institution's access to be suspended by the publisher.

The basic rule of the regional workflow follows from these constraints: Claude Code operates at the level of records, DOIs, and access addresses, while full-text downloading is done through the user's own browser and institutional identity, within the limits of the agreement. This rule is both ethical and practical: it keeps access sustainable and protects the institutional subscription.

## 7. Where Indexing Sits in the Academic Incentive System

In Türkiye, the academic incentive regulation scores a scholar's annual output and provides additional payment accordingly. In this system, a publication's score varies by the database in which its journal is indexed: a journal in certain Web of Science indexes is scored differently from a journal in TR Dizin alone. This scoring directly shapes journal selection decisions.

This booklet does not give specific figures from the incentive rules, because the regulation changes frequently and any figure tied to a specific year would quickly date the text. What matters is the principle: indexing choice produces, for a scholar in Türkiye, a concrete institutional evaluation result that extends well beyond mere visibility. When conducting a literature scan or a journal selection with Claude Code, having the model track indexing information as a separate field lets the scholar bring this institutional reality into the workflow. The database in which a journal is indexed should always remain visible in the scan output: it is a concrete trace of institutional positioning.

## 8. A Literature Scan Across Language Boundaries

A social anxiety researcher wants to collect Turkish, Greek, and English literature within a single scan. The conventional approach requires running searches across separate interfaces, merging the results manually, and working through two or more rounds of deduplication. The structured approach with Claude Code organizes these layers into a single workflow.

The source layers are defined at the outset: international databases for the English layer, DergiPark and TR Dizin for the Turkish layer, publisher packages reached through HEAL-Link for the Greek layer. Connecting Claude Code to external tools is done through the Model Context Protocol (MCP). When a bibliographic MCP server is configured, the model performs searching and record retrieval through that server.

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

This configuration is a skeleton; the real server name varies by the bibliographic MCP the user prefers. What matters is the architecture: the model performs record-level operations through a structured tool, while full-text access remains within the user's institutional identity. When the scan is complete, the model merges the three layers into a single bibliography, preserving for each record which layer and which index it came from. The result is a holistic map of the social anxiety literature that crosses language boundaries. Tenopir and colleagues (2019), in an international study of how researchers discover, read, and use scholarly articles, found that researchers actively change strategies to overcome access obstacles, a finding this guide treats as evidence that reducing access friction has practical value, though extending that finding specifically to multilingual Claude Code workflows is this guide's own inference.

## 9. Cross-Language Citation Considerations

Citing a Turkish or Greek source in an English article raises both formal and ethical considerations. Formally, APA 7 preserves the title in its original language and adds an English translation in square brackets. This rule preserves the original identity of the source while providing accessibility for the English reader. Claude Code can convert a Turkish source record into this format, but the accuracy of the translation is the author's responsibility: title translation is sensitive to field-specific terminology and cannot be delegated to the model without verification.

At the ethical level, language asymmetry carries a visibility dimension. Larivière and colleagues (2015), demonstrating the oligopolistic structure of academic publishing in the digital era, showed that which output is visible is to a large extent determined by commercial infrastructure. This guide infers, on that basis rather than as a finding of that paper itself, that citing a Turkish or Greek source in an English article is not merely a formal operation but a choice that gives a measure of visibility to output the commercial infrastructure systematically under-represents. Carrying regional literature into international debate aligns with the infrastructural aim of this booklet.

## 10. The Ethical Layer Framed by User Agreements

The user agreements of Turkish and Greek libraries and publisher packages define what may and may not be done. These limits must be observed in any Claude Code workflow. Automated bulk downloading is prohibited; access is personal, non-transferable, and bound to the consortium. These rules preserve the sustainability of access. They are the condition under which access exists at all.

A further ethical layer is source quality. Demir (2018), in a mixed-methods study of where predatory journals are founded and why researchers publish in them, found that the majority of such journals are located in developing countries and that institutional pressures are among the factors that lead researchers toward them. While that study is global in scope rather than specific to Türkiye, its findings about the structural pressures that drive researchers toward low-quality outlets are directly relevant to any regional context where incentive systems shape publication choices. This booklet names no specific journals, because such lists change quickly and a false accusation carries serious consequences. Instead, it proposes a principle-level safeguard: TR Dizin coverage, consortium membership, and institutional library approval together form a multi-layered filter for source trustworthiness. The open science framework completes this filter. UNESCO's (2021) recommendation on open science offers an international policy foundation that treats access, quality, and equity as a coherent whole, each dimension reinforcing the others.

## 11. Bridge to the Memory System

The infrastructure established in this booklet (DOI retrieval, TR Dizin filtering, HEAL-Link authentication, thesis records, three-language scans) produces documents and records. The second critical question is what happens to those records after the session ends. A literature scan, records collected in three languages, a doctoral thesis scan: all of these must be findable again in a later session. That is an engineering-pattern problem. The next category establishes the Memory as Vault pattern from first principles and shows how every incoming document is held in a persistent, retrievable structure, so that infrastructure built here does not vanish at session close.

## References

Citations are in APA 7 format. DOIs were independently verified against Crossref; institutional URLs were confirmed live as of 2026-06-04.

Demir, S. B. (2018). Predatory journals: Who publishes in them and why? *Journal of Informetrics*, 12(4), 1296-1311. https://doi.org/10.1016/j.joi.2018.10.008

HEAL-Link. (2026). *Hellenic Academic Libraries Link consortium*. https://www.heal-link.gr

Larivière, V., Haustein, S., & Mongeon, P. (2015). The oligopoly of academic publishers in the digital era. *PLOS ONE*, 10(6), e0127502. https://doi.org/10.1371/journal.pone.0127502

Mongeon, P., & Paul-Hus, A. (2016). The journal coverage of Web of Science and Scopus: A comparative analysis. *Scientometrics*, 106(1), 213-228. https://doi.org/10.1007/s11192-015-1765-5

Tenopir, C., Christian, L., & Kaufman, J. (2019). Seeking, reading, and use of scholarly articles: An international study of perceptions and behavior of researchers. *Publications*, 7(1), 18. https://doi.org/10.3390/publications7010018

TÜBİTAK ULAKBİM. (2024). *DergiPark Akademik platform*. https://dergipark.org.tr

TÜBİTAK ULAKBİM. (2026). *TR Dizin journal evaluation criteria*. https://trdizin.gov.tr

UNESCO. (2021). *UNESCO recommendation on open science* (SC-PCB-SPP/2021/OS/UROS). https://unesdoc.unesco.org/ark:/48223/pf0000379949

van Leeuwen, T. N., Moed, H. F., Tijssen, R. J. W., Visser, M. S., & van Raan, A. F. J. (2001). Language biases in the coverage of the Science Citation Index and its consequences for international comparisons of national research performance. *Scientometrics*, 51(1), 335-346. https://doi.org/10.1023/A:1010549719484

YÖK. (2026). *Council of Higher Education National Thesis Center*. https://tez.yok.gov.tr

---

**Booklet ID.** `002-04-0001`
**Version.** `0.1.0`
**Date.** 2026-06-04
**Word count (approx.).** 2493 (English body text, measured with wc)
**Verified citations.** 10
**Hallucinated citations.** 0
**Previous booklet.** [`001-01-0003`](../../001-foundations/001-01-0003/en.md). Installation, First Session, and Sanity Checks
**Next booklet.** [`003-01-0001`](../../003-memory-system/003-01-0001/en.md). Memory as Vault, A First-Principles Introduction
