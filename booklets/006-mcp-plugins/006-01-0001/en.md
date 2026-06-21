---
title_en: "MCP for the Researcher. What, Why, When"
title_tr: "Araştırmacı İçin MCP. Ne, Neden, Ne Zaman"
booklet_id: "006-01-0001"
category: "006-mcp-plugins"
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
    model_dated: null
    role: "drafting, verification, citation lookup, bilingual re-authoring"
    interaction_mode: "interactive console"
ai_contribution_level: "substantial-drafting"
human_review: "complete"
human_review_date: "2026-06-21"
verified_citations_count: 6
fabricated_citations_count: 0
disclosure_standard: "COPE 2023 + WAME 2023 + ICMJE 2024 + STM 2025 + EU AI Act 2024/1689 Art. 50 + ENAI"
translation_notes: "English re-authored from the finalized Turkish source (v0.2.0, 2026-06-21), not a literal translation. Structure updated to include an explicit Introduction section, matching the Turkish. Server and search examples are generic and tied to no real participant data or credentials. Citation audit 2026-06-21: all DOIs verified against Crossref. Tenopir et al. (2011) cited for the willing-in-principle, guarded-in-practice finding; Walters and Wilder for the fabrication baseline that grounds the retrieval argument; the two Anthropic references follow the non-DOI citation precedent set in booklet 001-01-0003."
license:
  - "CC-BY-NC-SA-4.0 (prose)"
status: "release"
---

# MCP for the Researcher. What, Why, When

## Introduction

The previous booklet organized the interior of the session with rituals. Opening and closing, and the guard checks in between, were fastened to infrastructure rather than left to the researcher's memory. This booklet moves to what the session has to do with the outside world — because research life does not consist of local files alone. Source catalogs, databases, reference managers, and institutional systems typically reside beyond the boundary of the session.

In its default state, Claude Code operates within a restricted workspace. It can read the researcher's archive, write to permitted files, and generate responses from the knowledge carried by its training. But the researcher's actual needs frequently exceed this. Sometimes what is required is not prompting the model to recall something, but directing it to look at a trustworthy external source. The Model Context Protocol — MCP for short — is one standardized answer to that need.

The central claim of this booklet is the following. MCP is not, for the researcher, a convenience add-on; it is the methodological instrument for connecting in a controlled way to external sources. Every connection simultaneously raises new questions of trust, maintenance, and data flow. MCP must therefore be evaluated not only in terms of what it is, but in terms of when it is warranted and when it is not.

## 1. The Boundary of the Session

Every tool has an access boundary, and that boundary is not merely a technical constraint — it is a security decision. In its default installation, Claude Code confines itself to the files in your working directory and the commands you approve. It does not reach out to an external service on its own initiative. The boundary protects the researcher, and in certain academic tasks it carries a price.

A session conducting a literature search, if it cannot consult the source catalog, has no choice but to work from what the model remembers. This situation is particularly risky from the standpoint of citation integrity. The model remembering something and the model consulting a source are not the same thing. In a research context, reliability often reveals itself in exactly that distinction.

MCP is the standard that opens this boundary in a controlled way (Anthropic, 2024). The protocol subjects how Claude Code communicates with an external service to specific rules. A small server stands on the service side, and the operations that server offers become visible on the tool side. What the researcher constructs is a bridge — and both ends of that bridge must remain defined and inspectable.

## 2. What — The Plain Description

MCP can be explained without technical detail through two concepts: server and tool. A server is a door that opens onto a particular service. A PubMed server opens onto the academic catalog, a Zotero server onto the reference library, a file server onto a designated folder. A tool declares which operations may pass through that door — search, fetch, list, read, or, in limited configurations, write.

When Claude Code connects to an MCP server, the tools that server offers are added to the list of capabilities available to the session (Anthropic, 2026). The model is no longer obliged to rely solely on its own training data; it can consult an external source through a defined interface.

The concrete difference comes down to a single example. In a session without MCP, if you request sources on social anxiety scales, the model assembles a list from what it encountered in training. In a session connected to a PubMed server, the same request becomes a search call, and the list that returns is grounded in the catalog's actual records at that moment. In the first case, the model remembers. In the second, it looks. For research purposes, this distinction is critical.

## 3. Why — Looking Rather Than Remembering

The difference between remembering and looking connects directly to the integrity problem that runs throughout this guide. Walters and Wilder (2023) documented how common fabricated and erroneous references are in bibliographies that a model generates from memory. A model can produce records that resemble genuine entries without actually existing. A record returned from a real catalog arrives with the question of existence already resolved. The record is there because the catalog entry is there. The DOI, the title, the authors, and the publication data come from verifiable infrastructure. This does not mean that all verification burden disappears — every record still needs to be read correctly, transcribed faithfully, and evaluated against the context. But MCP changes the failure mode. It substantially reduces the risk of generating sources from nothing and converts the task into more concrete, checkable work. Citation discipline continues. Yet the most dangerous stage of that burden — the creation of phantom references — is largely removed from the circuit.

## 4. When It Is Not Needed

An honest guide must state plainly that MCP is not required in every situation. Every outward connection is a maintenance load, a trust question, and a potential breaking point. Wilson and colleagues (2017) recommend in scientific computing practice not the most impressive tool but the simplest solution that accomplishes the work. The principle applies directly to the MCP decision.

Standing up a server for an operation you run once a week, in one minute through a browser tab, is almost always unnecessary. If consulting a single page suffices, no bridge is needed. MCP earns its place for work that recurs frequently, that accumulates errors when done by hand, and that would benefit from being executed in a structured, reproducible way within the session.

The deciding question is this: does this connection carry work that the researcher performs regularly, that carries genuine error risk, and that will become more auditable with the tool in place? If yes, MCP is a candidate. If no, every server added becomes an unused door and a forgotten permission. A system with few doors is generally both safer and more auditable.

## 5. Trust Triage

If a bridge is to be built, the first question is social rather than technical. Who wrote this server? A server published by an official provider and a server downloaded from a repository of unknown provenance do not occupy the same trust class. The second question concerns scope of access. What can the server touch? A catalog server that only executes searches and a server that can write to the file system operate at different risk levels. The third question is data flow: where do queries go, on which machine are they processed, are they logged, and for how long are they retained? A researcher should not open a bridge without knowing the answers.

Tenopir and colleagues (2011) showed that scientists are open to data sharing in principle but cautious in practice — with concerns about misuse, loss of control, and credit attribution measurably shaping behavior. The same caution is warranted at the tool layer. Declining to open a connection before understanding where the data flows is not paranoia. It is the expression of research ethics at the level of infrastructure.

## 6. Data Flow and Personal Data Protection

The hardest rule in the triage concerns participant data. Raw interview transcripts, tables carrying identifiers, consent forms, clinical materials, and files containing personal data must not pass through any third-party MCP server. Every transfer that the consent form did not foresee is not merely a technical oversight — it is a breach of the promise made to participants. The sequencing principle established in the qualitative coding and ethics booklets applies here as well: anonymization first, then the tool. Even with anonymized data, the question of where the server runs must be asked. A server running locally and a server relaying queries to a remote service are not the same thing.

The same care extends to routine queries. Even a search string sent to a catalog server can leave a data trace concerning the research topic. When the research subject is sensitive, knowing where that trace accumulates becomes a professional obligation. The rule is simple: everything that crosses a bridge has a recipient, and data is not sent to a recipient you have not identified.

## 7. Least-Privilege Setup

The foundational principle for any MCP installation is least privilege. If read-only access is sufficient, write permission is not granted. If the server needs to see one folder, it is opened onto that folder and not the entire disk. If a credential is required, it belongs in an environment variable rather than embedded in a configuration file, and it must never enter the archive repository. The guard hook from the previous booklet performs a second service here: because every commit passes through a secret scan, a key accidentally written into a file is caught at the gate rather than committed to history.

Each of these rules appears small in isolation. Together, they set a ceiling on the damage a bridge can do on a bad day. The basic principle of security engineering holds in a research archive as well: a component is given the authority it needs to do its job, and nothing more.

## 8. Verification Probes

A bridge, once built, should be tested before it is trusted, and the test is run against a record whose outcome is already known. If you have connected to the catalog, search for an article whose reference you know precisely. If the returned record matches the title, authors, year, and DOI you hold, the bridge is functioning correctly at a basic level. If it does not, the problem has been caught early and inexpensively — at a stage when it does not interrupt real work. If you have connected to your reference manager, list a record you know is in the library. If you have connected to the file system, retrieve a test file that contains no sensitive data and whose content you can verify.

The purpose is not to obtain an impressive response from the tool. The purpose is to confirm that the infrastructure is genuinely consulting the expected source. This known-record probe is a small-scale application of the guide's verification principle: an infrastructure proves itself not at the moment of its first real need, but in a trial whose result is known in advance.

## 9. Disclosure and the Methods Record

When MCP use becomes part of the research infrastructure, it becomes part of the methodological record. Hosseini, Rasmussen, and Resnik (2023) emphasize that the disclosure obligation for AI use is tied to the nature of the use itself — and the principle extends to search infrastructure. If a systematic search was conducted in a particular catalog, with a particular tool, on a particular date, and with a particular query, the methods section should state this. In an AI-assisted search workflow, the name and version of the MCP server belong naturally in that record, together with an account of what the connection did, which data it accessed, and how the researcher reviewed its outputs.

The structure that lightens this record-keeping burden is, once again, the archive itself. A log that captures during the session which source came over which bridge, with which query and at which point in time, has the disclosure sentence ready when it is needed at the writing stage. The source passport booklet — the next entry in this guide — will establish the systematic form of that log.

## 10. Bridge — Toward the Identity of Sources

When the archive is in place, the rituals are connected, and the session is consulting external catalogs over controlled bridges, a new question arises from each record that crosses. Where did this source come from? Which query found it? On which date was it verified? In which draft was it used?

The next booklet builds the system for answering that question. The source passport is the identity card each source carries across sessions. The archive-layer guarantee of citation integrity begins precisely there.

## References

Citations are in APA 7 format. DOIs verified against Crossref on 2026-06-21.

Anthropic. (2024). *Model Context Protocol*. https://modelcontextprotocol.io

Anthropic. (2026). *Claude Code documentation*. https://code.claude.com/docs

Hosseini, M., Rasmussen, L. M., & Resnik, D. B. (2023). Using AI to write scholarly publications. *Accountability in Research*, *31*(7), 715–723. https://doi.org/10.1080/08989621.2023.2168535

Tenopir, C., Allard, S., Douglass, K., Aydinoglu, A. U., Wu, L., Read, E., Manoff, M., & Frame, M. (2011). Data sharing by scientists: Practices and perceptions. *PLoS ONE*, *6*(6), e21101. https://doi.org/10.1371/journal.pone.0021101

Walters, W. H., & Wilder, E. I. (2023). Fabrication and errors in the bibliographic citations generated by ChatGPT. *Scientific Reports*, *13*, Article 14045. https://doi.org/10.1038/s41598-023-41032-5

Wilson, G., Bryan, J., Cranston, K., Kitzes, J., Nederbragt, L., & Teal, T. K. (2017). Good enough practices in scientific computing. *PLoS Computational Biology*, *13*(6), e1005510. https://doi.org/10.1371/journal.pcbi.1005510

---

**Booklet ID.** `006-01-0001`
**Version.** `0.2.0`
**Date.** 2026-06-21
**License.** This booklet is licensed under CC BY-NC-SA 4.0. https://creativecommons.org/licenses/by-nc-sa/4.0/
**Approximate word count.** 1994 (English body text, measured with wc)
**Verified citations.** 6
**Hallucinated citations.** 0
**Previous booklet.** [`005-02-0001`](../../005-hooks-automation/005-02-0001/en.md). Ritual Hooks. Daily Logging, Session Persistence, and Idle Time
**Next booklet.** [`007-01-0001`](../../007-academic-writing/007-01-0001/en.md). IMRAD Scaffolding. A Bilingual Approach
