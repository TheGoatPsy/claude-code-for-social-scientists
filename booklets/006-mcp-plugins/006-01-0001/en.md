---
title_en: "MCP for the Researcher: What, Why, When"
title_tr: "Araştırmacı İçin MCP: Ne, Neden, Ne Zaman"
booklet_id: "006-01-0001"
category: "006-mcp-plugins"
language: "en"
version: "0.1.0"
date_published: "2026-06-12"
date_last_revised: "2026-06-12"
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
human_review_date: "2026-06-12"
verified_citations_count: 6
fabricated_citations_count: 0
disclosure_standard: "COPE 2023 + WAME 2023 + ICMJE 2024 + STM 2025 + EU AI Act 2024/1689 Art. 50 + ENAI"
translation_notes: "English re-authored from the Turkish source, not a literal translation. Server and search examples are generic and tied to no real participant data or credentials, in keeping with the vault sanitization protocol. Citation audit 2026-06-12: all DOIs verified live against Crossref before drafting. Tenopir et al. (2011) restricted to the willing-in-principle, guarded-in-practice survey findings; Walters and Wilder cited for the fabrication baseline that grounded retrieval changes; the two Anthropic documentation references follow the non-DOI citation precedent set in booklet 001-01-0003."
license:
  - "CC-BY-NC-SA-4.0 (prose)"
status: "release"
---

# MCP for the Researcher: What, Why, When

The previous booklet put the inside of the session in order: opening, closing, and the guard checks between, all tied to infrastructure. This booklet turns to the session's relationship with the outside. Claude Code, left to itself, is an island. It reads your archive, writes to your files, and speaks from what its training carried. Research life, though, is not lived on an island. The source catalog is outside, the database is outside, the reference manager is outside. The bridge between them is called the Model Context Protocol, MCP for short, and this booklet describes the bridge through a researcher's eyes: what it is, why it earns its keep, and, just as important, when it is not needed at all.

## 1. The Boundary of the Session

Every tool has an access boundary, and this one is a deliberate safety decision. In its default installation, Claude Code confines itself to the files in your working directory and the commands you approve. It does not connect to an outside service on its own. The boundary protects the researcher, and it has a price. A session running a literature search, if it cannot look at the catalog, has to make do with what the model remembers.

MCP is the standard that opens this boundary in a controlled way (Anthropic, 2024). The protocol fixes uniform rules for how the tool talks to an external service. A small server stands on the service side, the capabilities that server offers become visible on the tool side, and every call between them passes through a defined contract. What the researcher builds is a bridge, and both ends of the bridge stay in view.

## 2. What, the Plain Description

The technical vocabulary reduces to two ideas. A server is a door that opens onto a specific service. A PubMed server opens onto the source catalog, a Zotero server onto your reference library, a file server onto one designated folder. A tool declares which operations may pass through that door: search, fetch, list. When Claude Code connects to an MCP server, that server's tools join the list of capabilities the session can use (Anthropic, 2026).

The concrete difference shows in one example. In a session without MCP, when you ask for sources on social anxiety scales, the model assembles a list from what it saw in training. In a session connected to a PubMed server, the same request becomes a search call, and the list that returns holds the catalog's actual records at that moment. In the first case the model remembers. In the second, it looks.

## 3. Why, Looking Instead of Remembering

The difference between remembering and looking is precisely the integrity problem this guide keeps returning to. Walters and Wilder (2023) documented how common fabricated and erroneous records are in bibliographies the model produces from memory. Generation can output records that resemble the real thing and do not exist. A record returned from a real catalog arrives with the existence question already settled. The reference is there because the record is there.

This is why MCP, in a research context, is more than a convenience. It changes the failure mode. The risk of invention gives way to checkable work: reading the found record correctly and carrying it over correctly. The burden of verification does not disappear, and the citation discipline described elsewhere in this guide continues unchanged. But the most dangerous component of the burden, creation from nothing, largely leaves the circuit.

## 4. When It Is Not Needed

An honest guide does not skip this section. Every outward connection is a maintenance load, a trust question, and a breaking point. Wilson and colleagues (2017) recommend, as good-enough practice in scientific computing, not the most impressive tool but the simplest one that does the job. The principle applies to the MCP decision directly. You do not stand up a server for an operation you run once a week in one minute. If a single page in the browser is enough, no bridge is required.

The deciding question is this. Does the connection carry work that repeats often within sessions and accumulates errors when done by hand? If yes, the bridge is a candidate. If no, every added server remains an unused door and a forgotten permission. A house with few doors is both safer and easier to inspect.

## 5. Trust Triage

If a bridge is to be built, the first question is social rather than technical. Who wrote this server? A server published by the official provider and a server downloaded from a repository of unknown identity are not in the same trust class. The second question is scope of access. What can the server touch? A catalog server that only searches and a server that can write to the file system sit at different risk levels. The third question is data flow. Which machine do your queries travel to, and how long are they kept there?

This guarded posture has roots in academic culture. Tenopir and colleagues (2011) showed in a large survey that scientists are open to data sharing in principle and guarded in practice, with worries about misuse and credit measurably limiting what they share. The same protective instinct should operate at the tool layer. Refusing to open a bridge before you know where your data flows is not paranoia. It is professional ethics.

## 6. Data Flow and Data Protection

The hardest rule in the triage concerns participant data. Raw interview transcripts, tables carrying identities, and consent forms do not pass through any third-party MCP server. Every transfer the consent form did not foresee is, before any KVKK or GDPR obligation, a breach of the promise made to the participant. The ordering from the qualitative coding booklet holds here too. Anonymization first, tool second. Even with anonymized data, ask where the server runs, because a server running locally and a server relaying queries to a remote service are not the same thing.

The same care extends down to everyday queries. Even a search string sent to a catalog server is a data trace. When your research topic is sensitive, you want to know where that trace accumulates. The rule is plain. Everything that crosses a bridge has a recipient, and no package is sent to a recipient you have not identified.

## 7. Least-Privilege Setup

The installation principle is least privilege. If read-only is enough, write permission is not granted. If the server needs one folder, it opens onto that folder and not the whole disk. If a credential is required, it lives in an environment variable, not embedded in a configuration file, and it never enters the archive repository. The guard hook from the previous booklet does its second job here: because every commit passes a secret scan, a key accidentally written into a file is caught at the gate.

Each of these rules is small on its own. Together they set a ceiling on the damage a bridge can do on its worst day. The old principle of security engineering holds in a research archive too. Give a component enough authority to do its job, and no more.

## 8. Verification Probes

A bridge, once built, is tested before it is trusted, and the test uses a known record. If you connected to the catalog, search for an article whose reference you know by heart. If the returned record matches what you hold, title, authors, DOI, the bridge stands. If it does not, the problem has been caught early and cheaply. If you connected to your reference manager, list a record you know is in the library.

This known-record probe is the smallest instance of the guide's verification principle. An infrastructure proves itself not at the first real need but in a trial whose outcome is known in advance. A successful probe goes into the record, and the bridge becomes a trusted part of the workflow.

## 9. Disclosure and the Methods Record

The moment MCP joins the research infrastructure, it is part of the method. Hosseini, Rasmussen, and Resnik (2023) tie the duty of disclosure to the use itself, and the principle covers search infrastructure. If a systematic search ran in a given catalog, with a given tool, on a given date, the methods section says so. In an AI-assisted search workflow, the MCP server's name and version belong naturally in that record.

The tool that lightens the record-keeping is, again, the archive itself. A ledger that notes during the session which source came over which bridge, with which query and when, has the disclosure sentence ready at writing time. The source passport, the subject of the next booklet, is exactly that ledger made systematic.

## 10. Bridge, to the Identity of Sources

The archive stands, the rituals are wired, and the session now looks at outside catalogs over controlled bridges. Every source that crosses a bridge brings a question with it. Where did this record come from, which query found it, and which draft used it? The next booklet builds the system for that question. The source passport is each source's identity card across sessions, and the archive-layer guarantee of citation integrity.

## References

Citations are in APA 7 format. DOIs verified against Crossref on 2026-06-12.

Anthropic. (2024). *Model Context Protocol*. https://modelcontextprotocol.io

Anthropic. (2026). *Claude Code documentation*. https://docs.claude.com/en/docs/claude-code

Hosseini, M., Rasmussen, L. M., & Resnik, D. B. (2023). Using AI to write scholarly publications. *Accountability in Research*, 30(7-8), 1-9. https://doi.org/10.1080/08989621.2023.2168535

Tenopir, C., Allard, S., Douglass, K., Aydinoglu, A. U., Wu, L., Read, E., Manoff, M., & Frame, M. (2011). Data sharing by scientists: Practices and perceptions. *PLoS ONE*, 6(6), e21101. https://doi.org/10.1371/journal.pone.0021101

Walters, W. H., & Wilder, E. I. (2023). Fabrication and errors in the bibliographic citations generated by ChatGPT. *Scientific Reports*, 13, Article 14045. https://doi.org/10.1038/s41598-023-41032-5

Wilson, G., Bryan, J., Cranston, K., Kitzes, J., Nederbragt, L., & Teal, T. K. (2017). Good enough practices in scientific computing. *PLoS Computational Biology*, 13(6), e1005510. https://doi.org/10.1371/journal.pcbi.1005510

---

**Booklet ID.** `006-01-0001`
**Version.** `0.1.0`
**Date.** 2026-06-12
**Approximate word count.** 1665 (English body text, measured with wc)
**Verified citations.** 6
**Hallucinated citations.** 0
**Previous booklet.** [`005-02-0001`](../../005-hooks-automation/005-02-0001/en.md). Ritual Hooks: Daily Logging, Session Persistence, Idle Time
**Next booklet.** [`007-01-0001`](../../007-academic-writing/007-01-0001/en.md). IMRAD Scaffolding: A Bilingual Approach
