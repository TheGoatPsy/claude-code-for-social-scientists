---
title_en: "Folder Discipline and the Maps of Content (MOC) Pattern"
title_tr: "Klasör Disiplini ve Maps of Content (MOC) Kalıbı"
booklet_id: "004-01-0001"
category: "004-vault-architecture"
language: "en"
version: "0.1.0"
date_published: "2026-05-24"
date_last_revised: "2026-06-20"
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
ai_contribution_level: "substantial-drafting"
human_review: "complete"
human_review_date: "2026-06-20"
verified_citations_count: 9
fabricated_citations_count: 0
disclosure_standard: "COPE 2023 + WAME 2023 + ICMJE 2024 + STM 2025 + EU AI Act 2024/1689 Art. 50 + ENAI"
translation_notes: "English re-authored from the Turkish source, not a literal translation. Folder and MOC examples preserve the Memory as Vault conventions established in the Turkish version. The MOC and frontmatter field keys are intentionally domesticated per language: the Turkish version uses Turkish keys such as tip and etiketler, this English version uses type and tags. A reader consulting both versions sees the same structure with language-appropriate keys, not a single shared schema."
license:
  - "CC-BY-NC-SA-4.0 (prose)"
status: "release"
---

# Folder Discipline and the Maps of Content (MOC) Pattern

The previous booklet established the four steps of the Memory as Vault pattern. This booklet deepens the Store step among those four. Where information belongs looks like a simple question on the surface, but it is an engineering decision, and a consequential one. A wrong folder architecture imposes a hidden productivity tax on a researcher within months. A right architecture shifts finding a file from conceptual recollection to structural navigation. The aim here is to treat folder architecture not as a matter of personal taste but as a design decision, and to adapt the maps of content (MOC) pattern, a practitioner concept introduced by the personal knowledge management community and not an established academic construct, to the social science research context.

## 1. The Cost Calculation of Folder Choice

When a scholar sets up their vault, they most often choose the folder architecture without thinking. The first structure that comes to mind is built, files are dropped in, and work begins. This choice looks cheap. Its real cost emerges over time.

Six months later, the researcher searches for a file and has to remember where they left it. A year later, the same document sits in two different folders under two different names. Two years later, half the vault is inaccessible. The files are still there; the addresses have been forgotten, and the logic behind each folder is no longer legible to anyone. Personal information management research has documented this dynamic directly: scattered storage and inconsistent naming create refinding costs that accumulate silently across a researcher's working life, ultimately constraining what knowledge they can actually act on (Jones, 2007).

This is a hidden tax, because it is not directly visible at the moment of filing. Every misplaced file generates a future search cost; the full overhead only becomes apparent when multiplied across hundreds of documents over years. The basic principle Norman (2013) set out on the design of everyday things applies here: the usability of a system is inversely proportional to how much the user has to think while navigating it. A well-designed vault does not require the researcher to think in order to find a file, because the structure itself shows the way. Folder discipline is an engineering investment that lowers the future cost of access, starting today.

## 2. A Comparison of Common Folder Architectures

Each major folder architecture found in academic vaults has its own logic and its own cost.

The topical architecture organizes folders by research area: clinical notes in one folder, fieldwork in another, literature in a third.

```mermaid
flowchart TD
  V[Vault] --> K1[01-Clinical]
  V --> K2[02-Field]
  V --> K3[03-Literature]
  K1 --> N1[case-formulation.md]
  K2 --> N2[komotini-2025.md]
  K3 --> N3[social-anxiety-review.md]
```

The chronological architecture organizes folders by time: one folder per year, one subfolder per month. This is natural for journaling, but it hides the topical context of any given piece of information.

```mermaid
flowchart TD
  V[Vault] --> Y1[2024]
  V --> Y2[2025]
  V --> Y3[2026]
  Y3 --> M1[2026-05.md]
  Y3 --> M2[2026-06.md]
```

The project-based architecture organizes folders by active project. It is efficient in the short term, but conflicts with the long-lived nature of academic production: a project ends while the knowledge it produced remains. None of these architectures is sufficient on its own. The topical hides time; the chronological hides topic; the project-based hides permanence. Adding a navigation layer on top is the answer, and that layer is the map of content.

## 3. PARA, Zettelkasten, and Johnny Decimal

Several organization patterns shed light on academic vault design, though none is sufficient as it stands.

The PARA pattern (Projects, Areas, Resources, Archive) is a system proposed by Tiago Forte (2022), a productivity practitioner and author. It organizes information by proximity to action and works well for personal productivity. For academic production it falls short in one specific way: in an academic vault, an article begins as a Project, then becomes a Resource, then ten years later becomes an Archive. PARA captures this life cycle, but across that cycle the file must be moved, and each move creates friction.

The Zettelkasten pattern is the atomic note system popularized by Sönke Ahrens (2017), drawing on the practice of the sociologist Niklas Luhmann. Each note carries a single thought; notes link to one another. The Zettelkasten works well for developing ideas, but on its own it is insufficient for managing large document collections where a researcher needs to navigate by project or deadline, not only by conceptual association.

The Johnny Decimal pattern organizes folders with a numbered decimal system: an area is 10–19, a subarea is 11, a document is 11.01. Navigation becomes numerical and precise. For an academic vault, the value of Johnny Decimal is an ordering and addressing system embedded directly in folder names.

For the social sciences, these three patterns are complementary rather than competing. PARA governs the life cycle, while Zettelkasten builds the conceptual web and Johnny Decimal pins each file to a fixed address. A well-built academic vault layers all three: numbered folder names anchor the address system; atomic notes carry single self-contained thoughts; maps of content draw the whole structure together into something navigable. The basic principle Allen (2015) set out in his productivity practitioner work also applies here: a system reduces mental load only when the researcher genuinely trusts it. That trust depends on the consistency of the structure.

## 4. MOC, the Maps of Content Pattern

The map of content, or MOC, is the navigation spine of a vault. As used in this guide, MOC is a practitioner concept from the personal knowledge management community, not an established academic construct; the term is used here as a working operational definition. A map of content is a gateway opening onto a topic: it gathers related documents in a single place, provides brief context among them, and directs the reader to the right document. The critical distinction is that folders group files physically, while maps of content group them conceptually. A map of content is a readable document: it links to files rather than containing them. A file sits in a single folder, but it can appear in multiple maps of content, and this is exactly what makes the pattern effective.

Why a map of content is necessary follows directly from the limits of the three architectures in the previous section. Folder architecture is one-dimensional: a file is in one folder. But knowledge is multidimensional. A case note can belong simultaneously to the clinical area, to a particular project, and to a particular theoretical framework. The map of content captures that multidimensionality. Bates's (2002) integrated model of information seeking and searching is relevant here: researchers search for information not along a single linear path but from many interconnected entry points, and the map of content makes those entry points concrete and navigable.

How a map of content is built is straightforward. A topic is chosen; the documents related to that topic are listed; a short context sentence is added to each; the map is framed with an introductory paragraph. The goal is density and readability: minimal ornament, maximum signal, a structure that makes the vault's contents immediately legible to the researcher who built it, and equally six months later to a researcher who no longer remembers exactly where everything is.

## 5. The Atomic Note, MOC, Meta-MOC Hierarchy

Maps of content do not remain at a single level. They form a layered hierarchy.

```mermaid
flowchart TD
  MM[Meta-MOC] --> M1[Area MOC]
  MM --> M2[Project MOC]
  M1 --> A1[atomic-note-1.md]
  M1 --> A2[atomic-note-2.md]
  M2 --> A3[atomic-note-3.md]
  M2 --> A1
```

The lowest layer is the atomic note: a single thought, a single source, a single observation. Atomic notes are the building blocks of the vault. The middle layer is the map of content: it gathers related atomic notes under a topic. The top layer is the meta map of content, or meta-MOC: it gathers maps of content and serves as the vault's highest-level navigation gateway. When a researcher enters the vault, they open the meta-MOC first, move to the relevant area map, then descend to a particular atomic note.

The power of this hierarchy is that the same atomic note can appear in multiple maps of content. As the diagram shows, atomic-note-1 appears both in the Area MOC and in the Project MOC. This overcomes the one-dimensionality of folder architecture: the file lives physically in a single folder, but conceptually it inhabits multiple maps. The hierarchy transforms the vault from a pile of files into a navigable knowledge space, one that becomes more useful, not less, as the vault grows.

## 6. Markdown Conventions

The consistency of a vault rests on small but disciplined conventions. These ensure that the same rules govern every document in the vault.

| Element | Convention | Example |
|---|---|---|
| File name | English, lowercase, hyphen-separated | `clinical-case-formulation.md` |
| Title | Turkish, in the frontmatter `title` field | `title: "Vaka Formülasyonu"` |
| Internal link | Double square brackets | `[[komotini-field-2025]]` |
| Tag | frontmatter list | `tags: [clinical, formulation]` |
| Date | ISO 8601 format | `2026-05-24` |
| Heading level | A single first-level heading | `# Document Title` |

The most important of these conventions is the distinction between the file name and the title. The file name is kept English and plain; the Turkish title lives within the frontmatter. The reason is the Unicode issue addressed in section 9. Double square bracket links are the concrete application of the hypertext principle described in the previous booklet: when a document references another, that reference becomes a navigable link. Frontmatter tags let the machine query the vault: a researcher can gather all documents bearing a particular tag with a single command.

## 7. An Example Academic Vault, MOC Types in Practice

A concrete example clarifies the pattern. Consider the vault of a clinical psychologist with ten years of practice. This vault contains maps of content differentiated by function.

The project map of content manages an active research project.

```text
---
type: moc-project
tags: [moc, social-anxiety-study]
---
# Social Anxiety Study MOC

This map gathers all documents of the ongoing social anxiety research.

- [[social-anxiety-literature-review]] literature review summary
- [[komotini-field-2025]] field data notes
- [[analysis-plan-v2]] current analysis plan
```

The area map of content tracks a field of expertise over the long term.

```text
---
type: moc-area
tags: [moc, clinical-formulation]
---
# Clinical Formulation Area MOC

All conceptual notes accumulated on case formulation.

- [[biopsychosocial-model]] theoretical framework
- [[formulation-template]] standard template
```

The third type is the archive map of content, which preserves completed projects. When a project ends, the project map is linked to the archive map, and the documents remain in place. Taken together, these maps enrich Forte's (2022) PARA life cycle with a navigation layer. A project opens in the project map; as it accumulates conceptual depth, the area map carries that dimension. When the project closes, the document stays where it is and the archive map simply links to it. Nothing moves. Only the document's visibility across maps changes, and the friction PARA on its own creates disappears.

## 8. Resilience to Tool Changes

The long life of a vault rests on its being tied to no single tool. A researcher may hold their vault today in a note application, but that application may shut down in five years, or change its pricing policy, or be acquired and discontinued. The vault must survive that change. The basis of resilience is the plain-text Markdown principle: maps of content, square-bracket links, and frontmatter are all plain-text conventions. They are tied not to any particular application but to the Markdown standard.

The practical test is simple: when the vault is taken out of a favorite application and opened in a plain-text editor, is it still navigable? In a well-designed vault the answer is yes. Square-bracket links are already visible in the raw text; a map document reads as ordinary prose in any editor; and a tag is nothing more than a character string in the frontmatter. When a tool changes, the only thing lost is the visual conveniences that tool provided, not the vault itself. This resilience makes the vault reliable at the scale of ten years, which is the appropriate planning horizon for a research career.

## 9. Türkiye and Greece Specificity

Turkish and Greek file names harbor a technical trap. Turkish characters (in particular ğ, ü, ş, ı, ö, ç) can cause problems between operating systems when used in file names. The reason is that Unicode normalization works differently across systems: macOS stores characters in NFD form, while Linux expects NFC. When a vault is moved between these two systems through git, file names with Turkish characters can become corrupted or duplicated.

The solution is simple and is already embedded in the conventions above: file names are kept English and plain, while the Turkish title lives in the `title` field within the frontmatter. A document is stored under the name `social-anxiety-review.md`, but its frontmatter contains `title: "Sosyal Kaygı Derlemesi"`. This rule solves the technical problem and eases international collaboration simultaneously: English file names travel safely across language environments. The same rule holds for Greek: plain Latin-letter file names rather than αβγ characters. This is not a deep technical debate but a single discipline rule, with detailed troubleshooting left to the closing booklet.

## 10. Bridge, to Citation Discipline

After the folder architecture is established, the bibliographic integrity of every reference that enters it determines the long life of the vault. However well a vault is organized, if the citations within it are inconsistent or unverified, academic production built on top of them cannot be trusted. The next category addresses APA 7 and DOI discipline, showing how every reference is held in a correct, verified, and consistent form. Knuth's (1984) philosophy of literate programming frames the underlying principle: write your document so that a human can read it, and accept the machine's ability to read it as an additional feature, not the primary goal. That principle scales from code to citations. A citation stripped of the argument it anchored, or a note filed where no one can retrieve it, loses most of its value. The vault is the environment that keeps each reference inside its context, and the next booklet shows how to maintain that environment. Brown and Duguid (2017) document the same dependency at the level of organizations: knowledge that loses its surrounding practice also loses its meaning.

## References

Citations are in APA 7 format. DOIs are verified against Crossref. Bates (2002) is cited without a DOI; no Crossref record is available for the *New Review of Information Behaviour Research* article. Trade books (Ahrens, Allen, Brown & Duguid, Forte, Norman) are cited with ISBN and framed throughout as practitioner sources.

Ahrens, S. (2017). *How to take smart notes: One simple technique to boost writing, learning and thinking*. ISBN 978-1542866507

Allen, D. (2015). *Getting things done: The art of stress-free productivity* (revised edition). Penguin Books. ISBN 978-0-14-312656-9

Bates, M. J. (2002). Toward an integrated model of information seeking and searching. *New Review of Information Behaviour Research*, 3(1), 1–15.

Brown, J. S., & Duguid, P. (2017). *The social life of information* (updated edition, with a new preface). Harvard Business Review Press. ISBN 978-1-63369-241-1

Forte, T. (2022). *Building a second brain: A proven method to organize your digital life and unlock your creative potential*. Atria Books. ISBN 978-1-9821-6738-9

Jones, W. (2007). Personal information management. *Annual Review of Information Science and Technology*, 41(1), 453–504. https://doi.org/10.1002/aris.2007.1440410117

Knuth, D. E. (1984). Literate programming. *The Computer Journal*, 27(2), 97–111. https://doi.org/10.1093/comjnl/27.2.97

Norman, D. A. (2013). *The design of everyday things* (revised and expanded edition). Basic Books. ISBN 978-0-465-05065-9

---

**Booklet ID.** `004-01-0001`
**Version.** `0.1.0`
**Date.** 2026-06-20
**Approximate word count.** 2282 (English body text, measured with wc)
**Verified citations.** 9
**Hallucinated citations.** 0
**Previous booklet.** [`003-01-0001`](../../003-memory-system/003-01-0001/en.md). Memory as Vault, A First-Principles Introduction
**Next booklet.** [`007-02-0001`](../../007-academic-writing/007-02-0001/en.md). APA 7 with DOI Discipline
