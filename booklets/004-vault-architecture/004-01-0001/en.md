---
title_en: "Folder Discipline and the Maps of Content (MOC) Pattern"
title_tr: "Klasör Disiplini ve Maps of Content (MOC) Kalıbı"
booklet_id: "004-01-0001"
category: "004-vault-architecture"
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
ai_contribution_level: "substantial-drafting"
human_review: "complete"
human_review_date: "2026-06-21"
verified_citations_count: 8
fabricated_citations_count: 0
disclosure_standard: "COPE 2023 + WAME 2023 + ICMJE 2024 + STM 2025 + EU AI Act 2024/1689 Art. 50 + ENAI"
translation_notes: "English body re-authored from the finalized Turkish source (v0.2.0, 2026-06-21), not a literal translation. Folder and MOC examples preserve the Memory as Vault conventions established in the Turkish version. MOC and frontmatter field keys are intentionally domesticated per language: the Turkish version uses Turkish keys such as tip and etiketler; this English version uses type and tags. A reader consulting both versions sees the same structure with language-appropriate keys, not a single shared schema."
license:
  - "CC-BY-NC-SA-4.0 (prose)"
status: "release"
---

# Folder Discipline and the Maps of Content (MOC) Pattern

The previous booklet established the four steps of the Memory as Vault pattern. This booklet deepens the Store step among those four. Where information belongs looks like a simple question on the surface. At its core it is an engineering decision, and a consequential one. A wrong folder architecture imposes a hidden productivity tax on a researcher within months. A right architecture shifts finding a file from conceptual recollection to structural navigation. The aim here is to treat folder architecture as a design decision and to adapt the maps of content (MOC) pattern to the social science research context. MOC is a practitioner concept from the personal knowledge management community; it makes no claim to being an established academic construct.

## 1. The Cost Calculation of Folder Choice

When a scholar sets up their vault, they most often choose the folder architecture without thinking. The first structure that comes to mind is built, files are dropped in, and work begins. This choice looks cheap at the outset. Its real cost surfaces over time.

Six months later, the researcher has to remember where they left a file. A year later, the same document sits in two different folders under two different names. Two years later, half the vault is inaccessible—not because anything was deleted, but because addresses have been forgotten and the logic behind each folder is no longer legible to anyone. Personal information management research has documented this dynamic directly: scattered storage and inconsistent naming produce refinding costs that accumulate silently across a researcher's working life, ultimately constraining the knowledge they can actually act on (Jones, 2007). Every misplaced file generates a future search cost; the full overhead only becomes apparent when multiplied across hundreds of documents over years.

This is a hidden tax, invisible at the moment of filing. The basic principle Norman (2013) set out on the design of everyday things applies directly: the usability of a system is inversely proportional to how much the user has to think while navigating it. A well-designed vault does not require the researcher to think in order to find a file, because the structure itself shows the way. Folder discipline is an engineering investment that lowers the future cost of access, starting today.

## 2. A Comparison of Common Folder Architectures

Each major folder architecture found in academic vaults has its own logic and its own cost structure.

The topical architecture organizes folders by research area: clinical notes in one folder, fieldwork in another, literature in a third.

![Tree diagram from an Archive root to Clinical, Field and Literature folders, then to example note files.](../../../assets/figures/004-01-0001/fig-1-domain.png)

*Figure 1. Folder discipline by domain. Clinical, Field and Literature branches under an Archive root (labels shown in Turkish, as in the author's working vault).*

The chronological architecture organizes folders by time: one folder per year, one subfolder per month. This is a natural structure for journaling, but it conceals the topical context of any given piece of information.

![Tree diagram from an Archive root to year folders (2024-2026), then to month-based daily note files.](../../../assets/figures/004-01-0001/fig-2-time.png)

*Figure 2. Folder discipline by time. Year and month-based daily logging.*

The project-based architecture organizes folders by active project. It is efficient in the short term, but conflicts with the long-lived nature of academic production: a project ends while the knowledge it produced remains.

None of these architectures is sufficient on its own. The topical hides time; the chronological hides topic; the project-based sacrifices permanence. The way out is to add a navigation layer on top of all three. That layer is the map of content.

## 3. PARA, Zettelkasten, and Johnny Decimal

PARA, Zettelkasten, and Johnny Decimal approach academic vault design from different angles. The opportunities each provides are distinct; so are their limits.

PARA stands for Projects, Areas, Resources, Archive. The system proposed by Tiago Forte (2022) organizes information by proximity to action and is well suited to personal productivity. For academic production it introduces a specific friction: in an academic vault, an article begins as a Project, then becomes a Resource, then ten years later moves to the Archive. PARA captures this life cycle. But across that life cycle the file must be physically moved, and each move carries a cost.

The Zettelkasten is the atomic note system popularized by Sönke Ahrens (2017), drawing on the practice of the sociologist Niklas Luhmann. Each note carries a single thought; notes link to one another to form a network. The Zettelkasten works well for developing ideas. But on its own it is insufficient for managing large document collections where a researcher needs to navigate by project or deadline, not only by conceptual association.

The Johnny Decimal pattern organizes folders with a numbered decimal system: an area is 10–19, a subarea is 11, a document is 11.01. Navigation becomes numerical and precise. For an academic vault, the value of Johnny Decimal is an ordering and addressing system embedded directly in folder names.

For the social sciences, these three patterns are complementary rather than competing. PARA governs the life cycle; Zettelkasten builds the conceptual web; Johnny Decimal pins each file to a fixed address. A well-built academic vault layers all three: numbered folder names anchor the address system; atomic notes carry single self-contained thoughts; maps of content draw the whole structure into something navigable. Allen's (2015) central observation on productivity applies here as well: a system reduces mental load only when the researcher genuinely trusts it. That trust derives from the consistency of the structure.

## 4. MOC, the Maps of Content Pattern

The map of content, or MOC, is the navigation spine of a vault. As used in this guide, MOC is a practitioner concept from the personal knowledge management community, not an established academic construct; the term functions here as a working operational definition, not as a terminological proposal. A map of content is a gateway opening onto a topic: it gathers related documents in one place, provides brief context among them, and directs the reader to the right document. The critical distinction is that folders group files physically, while maps of content group them conceptually. A map of content is a readable document—it links to files rather than containing them. This distinction has a practical consequence: a file lives in a single folder, but it can appear in multiple maps of content. That is precisely what makes the pattern effective.

Why a map of content is necessary follows directly from the limits of the three architectures in the preceding section. Folder architecture is one-dimensional: a file is in one folder. But knowledge is multidimensional. A case note can belong simultaneously to the clinical area, to a particular project, and to a particular theoretical framework. The map of content captures that multidimensionality. Bates's (2002) integrated model of information seeking and searching is relevant here: researchers search for information not along a single path but from many interconnected entry points. The map of content makes those entry points concrete and navigable.

Building a map of content is straightforward in practice. A topic is selected; the documents related to it are listed; a brief context sentence is added to each; an introductory paragraph frames the whole. The goal is a structure stripped of unnecessary ornament, dense with information, and legible to the researcher who built it both at the moment of construction and six months later. The visible skeleton of the vault.

## 5. The Atomic Note, MOC, Meta-MOC Hierarchy

Maps of content do not remain at a single level. They form a layered hierarchy that feeds back into itself.

![Hierarchy from a Meta-MOC to Domain and Project MOCs, then to atomic notes, with cross-links.](../../../assets/figures/004-01-0001/fig-3-moc.png)

*Figure 3. MOC hierarchy. A Meta-MOC links Domain and Project MOCs, which in turn link atomic notes.*

The lowest layer is the atomic note: a single thought, a single source, a single observation. These are the building blocks of the vault. The middle layer is the map of content: it gathers related atomic notes under a topic. The top layer is the meta map of content, or meta-MOC. It gathers maps of content and serves as the vault's highest-level navigation gateway. When a researcher enters the vault, they open the meta-MOC first, move to the relevant area map, then descend to a particular atomic note.

The power of this hierarchy lies in the fact that the same atomic note can appear in multiple maps of content. As the diagram illustrates, atomic-note-1 appears both in the Domain MOC and in the Project MOC. This is how the hierarchy overcomes the one-dimensionality of folder architecture: the file lives physically in a single folder, but conceptually it inhabits multiple maps. The hierarchy transforms the vault from a pile of files into a navigable knowledge space—one that becomes more useful, not less, as the vault grows.

## 6. Markdown Conventions

The consistency of a vault rests on small but disciplined conventions. These ensure the same rules govern every document in the vault.

| Element | Convention | Example |
|---|---|---|
| File name | English, lowercase, hyphen-separated | `clinical-case-formulation.md` |
| Title | Turkish, in the frontmatter `title` field | `title: "Vaka Formülasyonu"` |
| Internal link | Double square brackets | `[[komotini-field-2025]]` |
| Tag | frontmatter list | `tags: [clinical, formulation]` |
| Date | ISO 8601 format | `2026-05-24` |
| Heading level | A single first-level heading | `# Document Title` |

The most critical of these conventions is the distinction between file name and title. The file name is kept English and plain; the Turkish title lives within the frontmatter. The reason is the Unicode issue addressed in section 9. Double square bracket links are the concrete application of the hypertext principle described in the previous booklet: when a document references another, that reference becomes a navigable link. Frontmatter tags open the vault to machine querying: a researcher can gather all documents bearing a particular tag with a single command.

## 7. An Example Academic Vault: MOC Types

A concrete example sharpens the pattern. Consider the vault of a clinical psychologist with ten years of practice. This vault contains maps of content differentiated by function.

The first is the project map of content, which manages an active research project.

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

The second is the area map of content, which tracks a domain of expertise over the long term.

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

The third type is the archive map of content, which preserves completed projects. When a project ends, the project map is linked to the archive map; the documents remain in place. Together, these types enrich Forte's (2022) PARA life cycle with a navigation layer. A project that opens in the project map accumulates conceptual depth in the area map as well. When the project closes, the document stays where it is; the archive map simply links to it. Nothing moves. Only the document's visibility across maps changes; its address does not. The friction PARA creates on its own is eliminated.

## 8. Resilience to Tool Changes

The long life of a vault rests on its not being tied to any single tool. A researcher may hold their vault today in a note application. But that application may shut down in five years, or change its pricing policy, or be acquired and discontinued. This happens on a decadal timescale. The vault must survive such change. The foundation of resilience is the plain-text Markdown principle: maps of content, square-bracket links, and frontmatter are all plain-text conventions. They are bound not to any particular application but to the Markdown standard.

The practical test is this: when the vault is taken out of a favorite application and opened in a plain-text editor, is it still navigable? In a well-designed vault the answer is yes. Square-bracket links are already visible in the raw text. A map document reads as ordinary prose in any editor. A tag is nothing more than a character string in the frontmatter. When a tool changes, what is lost is only the visual conveniences that tool provided, not the vault itself. This resilience makes the vault reliable at the scale of ten years—the appropriate planning horizon for a research career.

## 9. Türkiye and Greece Specificity

Turkish and Greek file names harbor a technical trap. Turkish characters—in particular ğ, ü, ş, ı, ö, ç—can cause problems across operating systems when used in file names. The reason is that Unicode normalization works differently across systems: macOS stores characters in NFD form while Linux expects NFC. When a vault is moved between these two systems through git, file names containing Turkish characters can become corrupted or duplicated—silently, without any visible warning.

The solution is straightforward and is already embedded in the conventions of section 6: file names are kept English and plain, while the Turkish title lives in the `title` field within the frontmatter. A document is stored under the name `social-anxiety-review.md`, but its frontmatter contains `title: "Sosyal Kaygı Derlemesi"`. This rule simultaneously solves the technical problem and eases international collaboration: English file names travel safely across language environments. The same rule applies to Greek: plain Latin-letter file names rather than αβγ characters. This is not a deep technical discussion but a single discipline rule; detailed troubleshooting is reserved for the closing booklet.

## 10. Bridge, to Citation Discipline

Once the folder architecture is established, the bibliographic integrity of every reference entering the vault determines the vault's long-term viability. However well the vault is organized, if the citations within it are inconsistent or unverified, the academic production built on top of them cannot be trusted. The next category addresses APA 7 and DOI discipline, showing how each reference is held in a correct, verified, and consistent form.

Knuth's (1984) philosophy of literate programming captures the underlying principle: write a document so that a human can read it first; the machine's ability to process it is secondary. The same logic applies to the vault: a reference is verified so that a researcher can locate it in their work; bibliographic form is built on top of that verification. Brown and Duguid (2017) demonstrate, examining the social life of knowledge within organizations, that an academic vault is not merely a file repository but an environment in which knowledge lives together with its context. When the context remains alive, the vault remains alive. Citation is the spine of that structure. When it fractures, the structure collapses.

## References

Citations are in APA 7 format. DOIs are verified against Crossref (2026-06-21). Bates (2002) is cited without a DOI; no Crossref record is available for the *New Review of Information Behaviour Research* article. Trade books (Ahrens, Allen, Brown & Duguid, Forte, Norman) are cited with ISBN and framed throughout as practitioner sources.

Ahrens, S. (2017). *How to take smart notes: One simple technique to boost writing, learning and thinking*. ISBN 978-1542866507

Allen, D. (2015). *Getting things done: The art of stress-free productivity* (revised edition). Penguin Books. ISBN 978-0-14-312656-9

Bates, M. J. (2002). Toward an integrated model of information seeking and searching. *New Review of Information Behaviour Research*, 3(1), 1–15.

Brown, J. S., & Duguid, P. (2017). *The social life of information* (updated edition, with a new preface). Harvard Business Review Press. ISBN 978-1-63369-241-1

Forte, T. (2022). *Building a second brain: A proven method to organize your digital life and unlock your creative potential*. Atria Books. ISBN 978-1-9821-6738-7

Jones, W. (2007). Personal information management. *Annual Review of Information Science and Technology*, 41(1), 453–504. https://doi.org/10.1002/aris.2007.1440410117

Knuth, D. E. (1984). Literate programming. *The Computer Journal*, 27(2), 97–111. https://doi.org/10.1093/comjnl/27.2.97

Norman, D. A. (2013). *The design of everyday things* (revised and expanded edition). Basic Books. ISBN 978-0-465-05065-9

---

**Booklet ID.** `004-01-0001`
**Version.** `0.2.0`
**Date.** 2026-06-21
**License.** This booklet is licensed under CC BY-NC-SA 4.0. https://creativecommons.org/licenses/by-nc-sa/4.0/
**Approximate word count.** 2421 (English body text, measured with wc)
**Verified citations.** 8
**Fabricated citations.** 0
**Previous booklet.** [`003-01-0001`](../../003-memory-system/003-01-0001/en.md). Memory as Vault. A First Principles Introduction
**Next booklet.** [`007-02-0001`](../../007-academic-writing/007-02-0001/en.md). APA 7 with DOI Discipline
