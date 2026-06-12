# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

Citations of this work should use the Zenodo concept DOI [10.5281/zenodo.20289687](https://doi.org/10.5281/zenodo.20289687), which always resolves to the latest version. Version-specific DOIs are listed below.

## [3.0.0] - 2026-06-12

Major release. The Journal of Open Source Education paper is refreshed against the finished surface, twenty-one booklets across all twelve categories and twenty skills, and a submission preparation package is added. The major version marks the completion of the arc this line has been building: a fully populated category grid, a doubled skill layer with machine-enforced bilingual parity, and a citable, review-ready reference implementation.

### Added

- A fifth distinctive contribution in the paper: the anti-AI-trace revision method, grounded in the published evidence that detection tools are unreliable and biased against non-native writers, with the disclosure-over-detectability position stated explicitly. `paper/paper.bib` gains the `weberwulff2023` and `liang2023` entries, both DOI-verified.
- `meta/jose-submission.md`, the JOSE readiness checklist, including the open dual-license question that stays with the maintainer.
- A `draft-pdf.yml` workflow that compiles the paper with the official Open Journals action, runnable from the Actions tab and triggered by paper changes on main.

### Changed

- `paper/paper.md` moved from the stale v2.2.0 narrative to the v3.0.0 surface: twenty-one booklets in all twelve categories, twenty skills with the mandatory Turkish usage section, forty-two language files with 354 verified citation declarations and zero fabricated, and a quality-control section that matches the current CI reality.

### Unchanged

- No booklet, citation, or skill content changed. Aggregate metrics stay at 354 verified declarations, 0 fabricated, 21 booklets at release status.

### Archived

- Zenodo version DOI for v3.0.0: [10.5281/zenodo.20665696](https://doi.org/10.5281/zenodo.20665696).

## [2.9.0] - 2026-06-12

Minor release. Four new booklets join the catalog with live-verified citation cores, raising the released total from seventeen to twenty-one. Every one of the twelve categories now carries at least one released booklet, completing the catalog grid that the v3.0 milestone builds on. Aggregate verified citation declarations rise from 306 to 354, with zero fabricated.

### Added

- Booklet 003-03-0001, Material Passport: Tracking Sources Across Sessions. A six-field identity line for every source, FAIR-aligned at the personal archive layer, with the rule that a source without a passport does not enter the bibliography.
- Booklet 005-02-0001, Ritual Hooks: Daily Logging, Session Persistence, Idle Time. Research discipline moved from willpower to infrastructure, with guard hooks for secret scanning and citation protection.
- Booklet 006-01-0001, MCP for the Researcher: What, Why, When. Looking instead of remembering, a trust triage for third-party servers, least-privilege setup, and an honest section on when no bridge is needed.
- Booklet 011-01-0001, Slides, Posters, and Lightning Talks with AI Assistance. Three compressions of one study, visual integrity rules, and disclosure awareness on stage.

### Changed

- Every new citation core was verified live against Crossref before drafting. One candidate with ambiguous registered metadata (Lally et al., 2010) was dropped rather than cited with an uncertain date.
- The Pages workflow opts in to the Node 24 actions runtime (`FORCE_JAVASCRIPT_ACTIONS_TO_NODE24`) ahead of GitHub's 2026-06-16 switch, so the transition is tested under the project's own control.
- The MkDocs navigation gains the 005, 006, and 011 category sections, and the catalog, aggregate AI disclosure, website statistics, and README status lines move to the twenty-one-booklet surface.

### Archived

- Zenodo version DOI for v2.9.0: [10.5281/zenodo.20663876](https://doi.org/10.5281/zenodo.20663876).

## [2.8.0] - 2026-06-12

Minor release. Four new booklets join the catalog with live-verified citation cores, raising the released total from thirteen to seventeen and aggregate verified citation declarations from 248 to 306, with zero fabricated. The academic writing, data analysis, and peer review categories now have every planned slot at release status.

### Added

- Booklet 007-01-0001, IMRAD Scaffolding: A Bilingual Approach. Turkish-first drafting, English re-authoring, and the parity discipline for titles, abstracts, and keywords, grounded in the documented costs of publishing in a second language.
- Booklet 007-03-0001, Journal Fit and Cover Letters. Fit as a researchable question, index layers including ULAKBIM TR Dizin, a predatory journal screening discipline, and the cover letter as a document of fit.
- Booklet 008-03-0001, Qualitative Coding with AI Assistance and Human Oversight. Codebook design, the model as a second coder under protocol, reliability checkpoints, verbatim quote integrity, and anonymization-before-model data protection.
- Booklet 010-02-0001, Anti-AI-Trace Writing for Revisions. The theoretical ground of the `anti-ai-trace-revision` skill: detection tools fail measurably and unevenly, integrity lives in disclosure rather than invisibility, and the two-layer revision method this guide uses on its own prose.

### Changed

- Every new citation core was verified live against Crossref before drafting, and the quantitative claims were checked against publisher or PubMed Central full texts. One candidate reference without a registered DOI, Sollaci and Pereira (2004), was dropped rather than cited unverified.
- The MkDocs navigation, catalog, aggregate AI disclosure, website statistics, and README status lines were updated for the seventeen-booklet surface.

### Archived

- Zenodo version DOI for v2.8.0: [10.5281/zenodo.20662434](https://doi.org/10.5281/zenodo.20662434).

## [2.7.0] - 2026-06-10

Minor release. The project skill set grows from ten to twenty, covering the research lifecycle from literature scoping through bilingual drafting, analysis discipline, citation verification, and AI disclosure to review response and release integrity. Every skill now carries a Turkish usage section alongside its English protocol, extending the guide's bilingual parity principle to the skill layer. No booklet was added or changed. Aggregate citation metrics are unchanged at 248 verified declarations, 0 fabricated, and 13 booklets at release status.

### Added

- Ten new project skills under `.claude/skills/`: `anti-ai-trace-revision`, `bilingual-manuscript-scaffold`, `journal-fit-screening`, `qualitative-coding-discipline`, `statistical-consultation-protocol`, `research-ritual-hooks`, `research-lifecycle-pipeline`, `mcp-research-stack-triage`, `source-passport-ledger`, and `conference-materials-bilingual`.
- A mandatory `## Türkçe kullanım notu` section in every skill, enforced by the repository validator.
- A `social-cc doctor` command that checks the environment the guide's workflows expect: Python version, Claude Code, git, node, and installed skills.
- A `template/skill-template.md` scaffold and a skill proposal issue template, with skill contribution guidance in both CONTRIBUTING files.
- A Python test job in CI on Python 3.9 and 3.12.

### Changed

- The existing ten skills were strengthened: trigger-richer descriptions, cross-skill lifecycle references, falsifiable verification checks, and a Turkish usage section, with the prose taken through the same technical-register de-AI pass as the v2.6.0 booklets.
- The package version is now read from installed metadata with a single source of truth, fixing the drift between `__init__.py` and the release cascade.

### Archived

- Zenodo version DOI for v2.7.0: [10.5281/zenodo.20626097](https://doi.org/10.5281/zenodo.20626097).

## [2.6.0] - 2026-06-09

Minor release. A bilingual language and naturalness pass over the companion website and all thirteen released booklets, in both Turkish and English. The earlier voice work removed lexical calques; this release removes the deeper machine-writing signature, the rhetorical architecture, and the remaining concept-level calques.

### Changed

- The website and all thirteen booklets were re-read end to end in both Turkish and English. Number-announce headings, mechanical rule-of-three lists, and repeated antithesis tails of the "not X but Y" form were removed, and sentence rhythm was varied. The change is prose only.
- Concept-level calques were corrected in Turkish: the Vault metaphor is rendered as arşiv with the "X olarak Y" calque structure broken, parite is replaced with eşlik, and stiff loan-word constructions are replaced with natural Turkish. English keeps Vault as the Obsidian term.
- Booklet 003 title_tr changed from "Kasa Olarak Hafıza, İlkesel Bir Giriş" to "Hafızayı Arşive Dönüştürmek, İlkesel Bir Giriş", with cross-references updated.

### Unchanged

- No booklet was added or removed. No citation, DOI, frontmatter key, or heading count was changed. Bilingual parity is preserved. Aggregate metrics are unchanged: 248 verified declarations, 0 fabricated, 26 human-reviewed language files, 13 booklets at release status.

### Archived

- Zenodo version DOI for v2.6.0: [10.5281/zenodo.20608609](https://doi.org/10.5281/zenodo.20608609).

## [2.5.0] - 2026-06-05

Minor release. A Turkish-language voice revision of all thirteen released booklets, the companion website, and the Turkish README and CONTRIBUTING: the prose was rewritten in the author's academic voice, terminology was locked to correct forms, and AI-disclosure framing was enriched throughout.

### Changed

- The Turkish prose of all thirteen released booklets, the companion website, and README.tr and CONTRIBUTING.tr was rewritten in the author's academic Turkish voice. The change is prose only. Frontmatter, every section heading, every DOI, all inline citations, code blocks, and footer links are unchanged. Bilingual parity is preserved: each booklet keeps an equal section count and an identical DOI set across Turkish and English.
- Terminology locked to the correct Turkish academic forms across all thirteen booklets: ifşa replaced with katkı beyanı (or beyan in context), ajansal replaced with ajan tabanlı, broşür replaced with kitapçık, komponent replaced with bileşen, konsolidasyon replaced with bütünleşme, manüskri replaced with makale.
- AI-disclosure framing enriched: a declaration alone is not enough, the manner and extent of AI use must be explained; the machine-readable structured block is read by AI tools and orients correct work. This framing was applied consistently across all relevant prose passages in the thirteen booklets.
- The revision was verified through three layers: a re-voice pass, an independent voice review, and a Turkish-correctness proofread.

### Unchanged

- No booklet was added or removed. No citation, DOI, or heading was changed. English files were not touched. Aggregate metrics are unchanged: 248 verified declarations, 0 fabricated, 26 human-reviewed language files, 13 booklets at release status.

### Archived

- Zenodo version DOI for v2.5.0: [10.5281/zenodo.20554517](https://doi.org/10.5281/zenodo.20554517).

## [2.4.0] - 2026-06-05

Minor release. A scholarship and voice quality upgrade of all thirteen released booklets, in both Turkish and English, on two dimensions: substantive scholarship and technical accuracy first, then the author's native voice. No booklet was added or removed and no heading structure changed.

### Changed

- All thirteen booklets were revised on two dimensions. First, substantive scholarship and technical accuracy: overclaims were hedged and evidence, inference, and recommendation were distinguished throughout; a factual misstatement of EU AI Act Article 50 scope was corrected in 009-01-0001 (Article 50 transparency duties fall on providers and deployers and concern synthetic media, not an individual researcher flagging all AI-assisted text); the within-session continuity and CLAUDE.md loading descriptions in the foundations booklets were corrected against the official Claude Code documentation. Second, voice: the English was carried into natural-register academic prose and the Turkish into the author's native voice, with the academic register and every citation preserved.
- Misapplied citations were replaced with verified sources that support the exact claim: Squazzoni et al. (2021), a gender-bias study, was replaced with Bordage (2001) in 010-01-0001; Greenhalgh et al. (2016), a co-creation paper, was replaced with Bramer et al. (2017) in 007-02-0001; Tufte (1990), on quantitative graphics, was replaced with Jones (2007) in 004-01-0001. Phantom and dangling references that appeared in a reference list but were never cited in the body were removed: Engel (1977) from 003-01-0001 and Resnik (2018) from 010-01-0001. Citation-metadata errors were corrected, including the Provenzale and Stanley year and volume in 010-01-0001 and APA 7 article-number formatting across several booklets.
- Newly verified citations were added where a load-bearing claim needed support: Xu et al. (2025) on multilingual model bias, Jones (2007) on personal information management, Bramer et al. (2017) on database coverage, Wilson et al. (2017) and Ziems et al. (2024) on reproducible computing and computational social science, Simonsohn et al. (2020) and Munafò et al. (2017) on specification-curve and reproducibility, Bordage (2001) on reviewer decisions, and an Anthropic Claude Code documentation reference. Where no source supported a claim, the claim was hedged rather than propped with a citation. No citation was fabricated.
- Every added or replaced citation was verified live against Crossref and checked to support the exact claim it carries, and an independent adversarial review pass over all thirteen booklets confirmed zero fabricated citations. Bilingual parity is preserved: each booklet keeps an equal section count and an identical DOI set across Turkish and English. Aggregate verified citation declarations rise from 240 to 248, and unique bilingual citation sets from 120 to 124.
- The companion landing page Turkish prose was rewritten to remove sentence fragments, and the README and CONTRIBUTING were brought to the same voice bar.

### Zenodo

- Concept DOI: [10.5281/zenodo.20289687](https://doi.org/10.5281/zenodo.20289687) (resolves to the latest released version).
- Version DOI for v2.4.0: [10.5281/zenodo.20549062](https://doi.org/10.5281/zenodo.20549062).

## [2.3.0] - 2026-05-29

Minor release. A Turkish-language quality revision: the Turkish prose of all thirteen booklets, plus README.tr and CONTRIBUTING.tr, was rewritten in the author's native academic voice, replacing translation-shaped Turkish with natural native Turkish.

### Changed

- The Turkish prose of all thirteen released booklets and both Turkish-language README and CONTRIBUTING files was rewritten in the author's native voice. The change is prose only. Frontmatter, every section heading, every DOI, all inline citations, code blocks, and footer links are unchanged. Bilingual parity is preserved: each booklet keeps an equal section count and an identical DOI set across Turkish and English. No booklet was added or removed, and no citation count changed (240 verified declarations, zero fabricated, twenty-six human-reviewed language files, all unchanged).
- Small meaning-fidelity fixes were made against the English ground truth: a section-4 sentence inversion in booklet 001-01-0001, a pattern-versus-decision terminology drift in 003-01-0001, and a dropped predicate in README.tr.
- The companion website Turkish was corrected as well: ASCII-downgraded diacritics were restored and the copy was rewritten in the author's voice.

### Zenodo

- Concept DOI: [10.5281/zenodo.20289687](https://doi.org/10.5281/zenodo.20289687) (resolves to the latest released version).
- Version DOI for v2.3.0: [10.5281/zenodo.20449820](https://doi.org/10.5281/zenodo.20449820).

## [2.2.0] - 2026-05-29

Minor release. A second Data Analysis booklet, added after human review, on the discipline of statistical test selection when an analysis agent can run any test instantly.

### Added

- Booklet 008-02-0001, "Statistical Test Selection with AI Consultation Discipline," a bilingual Data Analysis booklet at `release` status, human-reviewed by the author. Nine independently verified citations, zero fabricated, full Turkish and English parity. It treats test selection as an inferential commitment that demands consultation discipline. Pre-specify the primary test, report the full specification space through multiverse analysis, verify a test's assumptions against the raw output rather than the agent's narration, and keep the test decision with the human. Three newly verified citations enter the bibliography: Wicherts et al. (2016) on the degrees-of-freedom checklist, Steegen et al. (2016) on multiverse analysis, and Silberzahn et al. (2018) on the many-analysts study. The released catalog grows from twelve to thirteen booklets, the second of the data analysis category.

### Changed

- The catalog, the AI disclosure aggregate, and the roadmap were updated for the new release. Aggregate verified citation declarations across disclosed language files rise from 222 to 240, and human-reviewed language files from 24 to 26.

### Zenodo

- Concept DOI: [10.5281/zenodo.20289687](https://doi.org/10.5281/zenodo.20289687) (resolves to the latest released version).
- Version DOI for v2.2.0: [10.5281/zenodo.20446035](https://doi.org/10.5281/zenodo.20446035).

## [2.1.0] - 2026-05-29

Minor release. The first Data Analysis booklet, added after human review, motivated by survey evidence on how social scientists actually use coding agents.

### Added

- Booklet 008-01-0001, "Reproducible Quantitative Workflows," a bilingual Data Analysis booklet at `release` status, human-reviewed by the author. Nine independently verified citations, zero fabricated, full Turkish and English parity. It treats the discipline of keeping an autonomous analysis agent reproducible and honest, a response to the selective-reporting and quality-erosion concerns recorded in Anthropic's 2026 survey of coding agents in the social sciences. The released catalog grows from eleven to twelve booklets, and the data analysis category is opened.
- A citation to the Anthropic 2026 coding-agents survey (Lyttelton, Massenkoff, and Wilmers) in the Journal of Open Source Education paper and its bibliography.

### Changed

- The Journal of Open Source Education paper draft was refreshed from stale v1.1.1 figures (ten booklets, 188 declarations) to the current release baseline (twelve booklets, 222 declarations), and the README bilingual rationale in both languages now cites the survey.
- The roadmap prioritizes the data analysis category (008) following the survey, and corrects a stale label that had described booklet 001-01-0004 as a draft after it shipped at release in v2.0.0.

### Zenodo

- Concept DOI: [10.5281/zenodo.20289687](https://doi.org/10.5281/zenodo.20289687) (resolves to the latest released version).
- Version DOI for v2.1.0: [10.5281/zenodo.20444934](https://doi.org/10.5281/zenodo.20444934).

## [2.0.0] - 2026-05-29

Major release. An audit-driven correctness and hardening pass, the first content-expansion booklet, version-independent repository tooling, and a companion website and academic paper. The ten v1.0 booklets are unchanged in scholarly content.

### Added

- Booklet 001-01-0004, "CLAUDE.md and the Discipline of Standing Instructions," a bilingual foundations booklet at `release` status, human-reviewed by the author. Eight independently verified citations, full Turkish and English parity. The released catalog grows from ten to eleven booklets, and the long-term catalog total is thirty-one.
- A bilingual MkDocs Material companion website (`mkdocs.yml`) that renders the booklets in place, with a GitHub Pages workflow (`.github/workflows/pages.yml`) that builds on every pull request and deploys on push to main.
- A Journal of Open Source Education companion paper draft (`paper/paper.md`, `paper/paper.bib`), whose bibliography reuses only citations already verified in the repository.
- A bilingual structure and citation parity check in the repository validator. Paired `tr.md` and `en.md` files must carry the same level-2 section count and the same set of bibliographic DOIs.
- A scheduled, non-blocking link and DOI liveness workflow (`.github/workflows/link-check.yml`) and `scripts/check-dois.mjs`, which resolves every cited DOI against the doi.org handle system.

### Changed

- The repository validator derives booklet counts from the filesystem instead of hardcoding version-specific totals, so promoting a booklet no longer requires editing the validator.
- The AI disclosure aggregate now covers all disclosed booklets regardless of status, and its verified and fabricated citation labels were generalized from released to all disclosed language files.
- `.zenodo.json` declares the prose license as CC-BY-NC-SA-4.0 and describes the taxonomy consistently with `CITATION.cff`.

### Fixed

- Corrected the Wooldridge citation in booklet 001-01-0002 to the 2009 second edition with the matching ISBN.
- Added the verified Crossref DOI to the Provenzale and Stanley citation in booklet 010-01-0001.
- Documented the five-level AI contribution scale cross-reference and the per-language MOC field-key domestication note.

### Zenodo

- Concept DOI: [10.5281/zenodo.20289687](https://doi.org/10.5281/zenodo.20289687) (resolves to the latest released version).
- Version DOI for v2.0.0: [10.5281/zenodo.20440754](https://doi.org/10.5281/zenodo.20440754).

## [1.1.1] - 2026-05-24

Patch release for distribution metadata hygiene. The booklets, project skills, and installer behavior are unchanged from v1.1.0.

### Changed

- Removed the maintainer's direct email address from public package metadata, citation metadata, plugin metadata, README contact text, contributor guidance, and conduct reporting text. Public coordination now routes through GitHub issues, discussions, and profile-level contact surfaces.
- Clarified that Zenodo version DOIs are minted after a GitHub release is published. Immutable tag archives can contain the concept DOI and previously known version DOIs, while `main` records newly minted version DOIs after Zenodo creates them.

### Fixed

- Avoided the misleading implication that a GitHub tag archive must already contain the version-specific DOI minted by Zenodo after that tag is released.
- Published a clean patch distribution surface so new PyPI metadata no longer exposes the maintainer's direct email address.

### Zenodo

- Concept DOI: [10.5281/zenodo.20289687](https://doi.org/10.5281/zenodo.20289687) (resolves to the latest released version).
- Version DOI for v1.1.1: [10.5281/zenodo.20364633](https://doi.org/10.5281/zenodo.20364633).

## [1.1.0] - 2026-05-24

Companion project skills and a distribution surface. The ten v1.0 booklets are unchanged in scholarly content. This minor release turns the booklets into repeatable Claude Code workflows and makes them installable.

### Added

- Ten Claude Code project skills under `.claude/skills/<skill-name>/SKILL.md`, each a single repeatable workflow with explicit inputs, verification steps, and safety boundaries, cross-referenced to its companion booklets.
- `social-cc-plugin`, a pip-installable distribution that copies the ten skills into a user's Claude configuration. Published to PyPI through GitHub Actions OpenID Connect trusted publishing, with no stored API token.
- A native Claude Code plugin manifest at `.claude-plugin/plugin.json` so the same skills install through the Claude Code plugin system from a single source.
- Repository validator added at `scripts/validate-repo.mjs` and wired into `npm run validate`.
- GitHub issue templates and a pull request template added for citation corrections, content corrections, bug reports, and review discipline.
- `.gitattributes` to normalize line endings to LF across contributor platforms.

### Changed

- README, README.tr, CATALOG, roadmap, aggregate AI disclosure, contributor notes, and script documentation aligned to the shipped release state.
- The Citation Check workflow now runs on every push and pull request to `main` rather than only when `CITATION.cff` changes, so the required status check cannot hang on unrelated pull requests.
- The repository validator no longer pins the aggregate-disclosure heading to a single hardcoded version and date string. It accepts any version and ISO date, removing a release-time coupling.

### Fixed

- v1.0.0 booklet frontmatter status now uses `release` across all twenty language files.
- Release booklets no longer contain unresolved `10.XXXXX/XXXXX` DOI examples.
- Booklet 009 self-disclosure language now matches completed human review.
- Booklet 012 Turkish wording now uses `şüpheci` rather than `septik`.

### Zenodo

- Concept DOI: [10.5281/zenodo.20289687](https://doi.org/10.5281/zenodo.20289687) (always resolves to the latest version, now v1.1.0).
- Version DOI for v1.1.0: [10.5281/zenodo.20364287](https://doi.org/10.5281/zenodo.20364287).

## [1.0.0] - 2026-05-24

The v1.0 manifesto. Ten core booklets, Turkish and English in full parallel, positioning Claude Code as a methodological partner of academic production for the social scientist. Across three dimensions: foundations (001), the methodological spine (002, 003, 004), and the academic production cycle (007, 009, 010, 012). 94 verified citations, 0 fabrications. Every booklet carries full AI-disclosure frontmatter and human-reviewed approval. Dual license: Apache 2.0 for code, CC-BY-NC-SA 4.0 for prose.

### Added

- Booklet 001-01-0002 (The Agentic Shift: From Chat Window to Working Partner) drafted in Turkish and English. Nine-section map, 10 verified citations (Wooldridge 2020, Park et al. 2023, Sumers et al. 2024, Yao et al. 2023, Mialon et al. 2023, Schick et al. 2023, Engel 1977, Hicks et al. 2024, Bender et al. 2021, Mollick 2024). Status `release`, human review complete.
- Booklet 001-01-0003 (Installation, First Session, and Sanity Checks) drafted in Turkish and English. Ten-section operational map with a failure-modes table, 6 verified citations (Anthropic Claude Code documentation and best practices, Microsoft WSL documentation, Ouyang et al. 2022, Bai et al. 2022, Anthropic Responsible Scaling Policy). Status `release`, human review complete.
- Both new booklets carry the full disclosure frontmatter. `ai_contribution_level` is `substantial-drafting` for 001-01-0002 and `co-drafting` for 001-01-0003. This completes category 001 (Foundations) as a bilingual set for the v1.0 manifesto.
- Booklet 002-04-0001 (DergiPark, ULAKBIM TR Dizin, HEAL-Link, and Regional Indexing) drafted in Turkish and English. The signature regional-access booklet, eleven-section map with a three-language literature-scan workflow and an MCP configuration example, 10 verified citations (van Leeuwen et al. 2001, Mongeon and Paul-Hus 2016, Larivière et al. 2015, Tenopir et al. 2019, Demir 2018, UNESCO 2021, plus the DergiPark, TR Dizin, YÖK Thesis Center, and HEAL-Link institutional sources). `ai_contribution_level` `co-drafting`. Status `release`, human review complete.
- Booklet 003-01-0001 (Memory as Vault: A First-Principles Introduction) drafted in Turkish and English. The original-concept booklet, nine-section map with a Mermaid Input-Store-Retrieve-Present diagram, 10 verified citations (Bush 1945, Nelson 1965, Luhmann 1992, Ahrens 2017, Lewis et al. 2020, Khattab et al. 2023, Valmeekam et al. 2023, Engel 1977, KVKK 2024, EDPB 2024). `original_concept: true`. `ai_contribution_level` `co-drafting`. Status `release`, human review complete.
- Booklet 004-01-0001 (Folder Discipline and the Maps of Content (MOC) Pattern) drafted in Turkish and English. Ten-section map with three Mermaid architecture diagrams, a Markdown conventions table, and three MOC examples (project, area, archive), 8 verified citations (Allen 2015, Forte 2022, Ahrens 2017, Knuth 1984, Brown and Duguid 2017, Tufte 1990, Bates 2002, Norman 2013). `ai_contribution_level` `substantial-drafting`. Status `release`, human review complete. This completes the methodological-spine categories 002, 003, and 004 as bilingual release sets.
- Booklet 007-02-0001 (APA 7 with DOI Discipline) drafted in Turkish and English. Ten-section map with a Crossref API verification workflow, an eight-step bibliography hygiene pipeline, and a language-model citation failure-modes table, 10 verified citations (APA 2020, Walters and Wilder 2023, Greenhalgh et al. 2016, Sallam 2023, Bhattacharyya et al. 2023, Else 2023, Hicks et al. 2024, plus the ICMJE, Crossref, and PubMed sources). `ai_contribution_level` `substantial-drafting`. Status `release`, human review complete.
- Booklet 009-01-0001 (Ethics in AI-Assisted Research: From Principle to Behavior), the spine booklet, drafted in Turkish and English. Eleven-section map with a twelve-item operational ethics checklist and a reflexive disclosure section that points at the booklet's own frontmatter, 12 verified citations (WMA Helsinki 2025, COPE 2023, WAME 2023, ICMJE 2024, STM 2025, EU AI Act 2024/1689, ENAI 2025, KVKK 2016, EDPB 2024, Resnik and Hosseini 2025, Mittelstadt et al. 2016, Jobin et al. 2019). `ai_contribution_level` `co-drafting`. Status `release`, human review complete.
- Booklet 010-01-0001 (Rebuttal Letters with Traceability Matrices) drafted in Turkish and English. Ten-section map with a synthetic eight-row traceability matrix, an ethics boundary table, and a 30/60/90-day plan, 9 verified citations (Provenzale and Stanley 2006, Belcher 2019, Sword 2017, Noble 2017, Williams and Bizup 2016, Hosseini et al. 2023, Else 2023, Resnik 2018, Squazzoni et al. 2021). `ai_contribution_level` `substantial-drafting`. Status `release`, human review complete. This completes the academic-production-cycle categories 007, 009, and 010.
- Booklet 012-01-0001 (When Things Go Wrong, A Working Troubleshooting Protocol), the closing booklet, drafted in Turkish and English. Eight-section map with a three-category problem taxonomy (tool, knowledge, communication), three worked example problems, a seven-step reasoning framework mapped to Polya's four stages, and a GitHub issue template, 7 verified citations (Polya 1945/2014, Schoenfeld 1985, Dörner 1996, Reason 2000, Norman 2013, Vaughan 1996, Perrow 1999). `ai_contribution_level` `co-drafting`. Status `release`, human review complete. This completes the v1.0 manifesto at ten released booklets. The closing section of this booklet closes the whole series.

### Changed

- `CATALOG.md` status of 001-01-0002 and 001-01-0003 moved from `planned` to `release`. Release count 1 to 3, planned count 29 to 27.
- `CATALOG.md` status of 002-04-0001, 003-01-0001, and 004-01-0001 moved from `planned` to `release`. Release count 3 to 6, planned count 27 to 24.
- Claude Code best-practices citation URL updated to the current canonical `https://code.claude.com/docs/en/best-practices` after a 308 permanent redirect from the older `anthropic.com/engineering` path (verified by live fetch on 2026-05-24).
- Citation metadata corrected during Phase 2 verification. The planning-abilities paper (arXiv:2305.15771) is attributed to its correct authors and venue, Valmeekam et al. (NeurIPS 2023), after the work-card draft had carried an incorrect author list and year. DSPy (Khattab et al., arXiv:2310.03714) is cited as an arXiv preprint without a contested conference venue. Bates (2002) is cited without an unresolvable DOI. The Brown and Duguid (2017) ISBN was corrected to 978-1-63369-241-1.
- `CATALOG.md` status of 007-02-0001, 009-01-0001, and 010-01-0001 moved from `planned` to `release`. Release count 6 to 9, planned count 24 to 21. CATALOG titles for 009-01-0001 and 010-01-0001 aligned to the booklet frontmatter.
- Citation metadata corrected during Phase 3 verification. The Declaration of Helsinki citation corrected to its actual JAMA publication, World Medical Association (2025), JAMA, 333(1), 71, after the work-card draft had recorded 2024 with JAMA 332(13), 1066-1069. The three peer-review handbook ISBNs corrected against publisher records: Belcher 2019 to 978-0-226-49991-8, Sword 2017 to 978-0-674-73770-9, Williams and Bizup 2016 to 978-0-13-408041-3. Provenzale and Stanley (2006) is cited without a DOI after 10.2214/AJR.05.0856 failed to resolve in Crossref.
- `CATALOG.md` status of 012-01-0001 moved from `planned` to `release`. Release count 9 to 10, planned count 21 to 20. The CATALOG title for 012-01-0001 aligned to the booklet frontmatter (comma rather than colon). With this, all ten v1.0 announcement-target booklets are released.
- Citation metadata corrected during Phase 4 verification. The Reason (2000) DOI confirmed against Crossref (BMJ 320(7237), 768-770). Two work-card ISBNs corrected: Dörner (1996) to the Metropolitan Books edition 978-0-8050-4160-6 (the card had carried an invalid check digit on a different subtitle), and Vaughan (1996) to 978-0-226-85176-1 (the card check digit was wrong). The Polya citation is given as a republished 1945 classic (2014 Princeton printing) without an unverifiable edition-number claim.
- Booklet 001-01-0001 footer word counts reconciled to measured values. Turkish body corrected from a stated 2900 to the measured 1997, English from a stated 2700 to the measured 2442. The earlier figures predated the Phase 1 reference-list trim and were never re-measured.
- Booklet 003-01-0001 English reference list corrected. The Luhmann (1992) reference, cited in-text in the English body, had been omitted from the English reference list while present in the Turkish. Restored to match the frontmatter count of 10 and the Turkish version. Found during the pre-release cross-booklet consistency audit, which otherwise confirmed that all ten booklets carry matching frontmatter and reference-list citation counts (94 total), a consistent previous-to-next bridge chain, and no forbidden characters across the bilingual set.

### Zenodo

- Concept DOI: [10.5281/zenodo.20289687](https://doi.org/10.5281/zenodo.20289687) (always resolves to the latest version, now v1.0.0).
- Version DOI for v1.0.0: [10.5281/zenodo.20363740](https://doi.org/10.5281/zenodo.20363740).

## [0.2.0] - 2026-05-19

The work since the v0.1.0-alpha tag (commit `4999222`) is grouped below into four phases, each corresponding to a discrete review or remediation cycle. The phase labels also match the vault diary entries for 2026-05-19.

### Phase 0 — Post-tag setup (commits `1272b0d` to `04ceaa3`)

- Zenodo deposit completed. Concept DOI `10.5281/zenodo.20289687` and version DOI `10.5281/zenodo.20289688` minted. Placeholders in `CITATION.cff` replaced with the real DOIs.
- Repository renamed from `sbcc-rehber` to `claude-code-for-social-scientists`. All internal references and the banner SVG updated. The old URL still redirects to the new one through GitHub's automatic mechanism, so Zenodo metadata was not affected.
- markdownlint configuration relaxed (MD033 inline-html allowlist for `p`, `img`, `div`, `a`) so the banner embedding in the README does not fail the lint.

### Phase 1 — Senior peer review remediation, faz 1 (commit `104558f`)

- `disclosure_standard` migrated from the non-existent NISO RP-2025-draft to the consolidating consensus across COPE 2023, WAME 2023, ICMJE 2024, STM 2025, the EU AI Act 2024/1689 Article 50, and ENAI.
- Booklet 001-01-0001 reference list cleaned. Three uncited entries (Bail 2024, Birhane 2022, Sallam 2023) removed to restore APA 7 reference-list discipline. `verified_citations_count` in both `tr.md` and `en.md` frontmatters reduced from 12 to 10 to reflect the corrected count.
- Booklet 001-01-0001 frontmatter `status` changed from `draft` to `paired` to match `CATALOG.md`.
- `AI-AUTHORSHIP.md` Section 3 booklet path schema corrected from `KKK-CC/KKK-CC-SSSS` to the actual `KKK-slug/KKK-AA-SSSS`.
- `meta/ai-disclosure.md` aggregate updated to reflect the corrected 27 planned booklets count (was 24).
- `meta/roadmap.md` mixed-language passages normalized (Turkish words "Hafta" and "Ay" replaced with English equivalents in the English-language file).
- CI hardened. `dieghernan/cff-validator` pinned to SHA `7b3c5e27c65c08af9f0c4a9c5e424aa281834e25`. AI disclosure frontmatter audit expanded from 5 required fields to 10 fields. Frontmatter extraction in CI switched from `head -n 60` to an awk-based YAML block parser.

### Phase 2 — Senior peer review remediation, faz 2 (commit `d6f4ded`)

- Pandoc citeproc keys (`[@author2024]`) in booklet 001-01-0001 converted to inline APA 7 citations so that GitHub renders them as readable text without a build step.
- Frontmatter title schema migrated from `title` plus `title_tr` to `title_en` plus `title_tr`. Both fields are now required by CI. Rationale: the previous schema put an English title in files declared `language: tr`, which was internally inconsistent.
- `ai_tools` entries now carry `model_alias` and `model_dated` fields. The `model` field is deprecated. Rationale: model aliases drift over time; dated identifiers preserve reproducibility.
- Booklet template files added (`template/booklet-template.{tr,en}.md`) with the full frontmatter schema and APA 7 inline citation examples.
- `CHANGELOG.md` (this file) added, following Keep a Changelog 1.1.0.
- `SECURITY.md` added, with responsible disclosure path and vault sanitization principles (SAFE, SANITIZE, BLOCKED, SKIP).

### Phase 3 — Strategic remediation (commit `4251aeb`)

- v1.0 announcement scope reduced from thirty booklets to ten core booklets. The ten v1.0 booklets are marked `[v1.0]` in `CATALOG.md`. The remaining twenty booklets move to the v1.5 and v2.0 backlog. Rationale: quality over breadth for the v1.0 manifesto.
- `meta/roadmap.md` revised end to end (Phase 1 to Phase 3, v1.0, v1.5, v2.0 sections) to reflect the smaller per-month booklet count.
- `README.md` and `README.tr.md` audience descriptions narrowed. The previous text named seven geographies (Türkiye, Greece, Mediterranean, Middle East, Latin America, South and Southeast Asia, Sub-Saharan Africa) which overpromised against the v1.0 scope. Replaced with the bilingual focus statement (every booklet delivered in Turkish and English in full parallel).
- `## Acknowledgements` section removed from both READMEs. The section had named two competitor repositories (Galaxy-Dawn/claude-scholar and Imbad0202/academic-research-skills) as influences. They are competitors, not influences. The guide's structural and methodological choices are original.
- Two citations added to booklet 001-01-0001. Engel (1977) for the biopsychosocial frame in the agent-system analogy in section 2, and Frankfurt (2005) for the philosophical scaffolding behind the bullshit-production reading in section 4. `verified_citations_count` raised from 10 to 12 in both `tr.md` and `en.md`, with corresponding update in `meta/ai-disclosure.md`.

### Phase 4 — Banner and date claim polish (commits `91d9a30`, `fde7ebb`)

- Banner SVG footer line trimmed. The `ECPP Dublin July 2026` segment removed from the footer. The same change applied to ARIA alt text in `README.md` and `README.tr.md`.
- All `ECPP Dublin / July 2026 / Temmuz 2026` date references removed from `README.md` status block, `README.tr.md` durum block, `CATALOG.md` intro, `meta/roadmap.md` v1.0 section, and `CHANGELOG.md`. v1.0 release timing is now set when the ten v1.0 booklets are reviewed and tagged, not by a calendar promise.

### Zenodo

- Concept DOI: [10.5281/zenodo.20289687](https://doi.org/10.5281/zenodo.20289687) (always resolves to the latest version, now v0.2.0).
- Version DOI for v0.2.0: [10.5281/zenodo.20293189](https://doi.org/10.5281/zenodo.20293189).

## [0.1.0-alpha] - 2026-05-19

### Added

- Initial public scaffold of the guide repository.
- Booklet 001-01-0001 paired (Turkish and English drafts). The first inline citation count was 10 at tag time. Frontmatter `verified_citations_count` initially recorded 12 due to an off-by-three counting error against an over-populated reference list. Phase 1 normalized both numbers to 10. Phase 3 added Engel (1977) and Frankfurt (2005), raising both numbers to 12. See the `[Unreleased]` block above for the trajectory.
- Two placeholder booklets (001-01-0002, 001-01-0003) so that CI bilingual coverage and AI disclosure audits exercise non-draft entries.
- 30-booklet catalog across 12 categories targeting the v1.0 launch.
- AI authorship policy aligned with the COPE plus WAME plus ICMJE plus STM 2025 plus EU AI Act 2024/1689 Article 50 plus ENAI consensus.
- Dual license model: Apache 2.0 for code blocks, CC-BY-NC-SA 4.0 for prose.
- Three CI workflows: Markdown lint (markdownlint-cli2), Citation Check (cff-validator SHA-pinned), Secret Scan.
- Bilingual coverage CI gate and AI disclosure frontmatter audit.
- Banner SVG at `assets/banner.svg` embedded in both READMEs.
- Repository renamed from `sbcc-rehber` to `claude-code-for-social-scientists`.

### Zenodo

- Concept DOI: [10.5281/zenodo.20289687](https://doi.org/10.5281/zenodo.20289687) (always points to the latest version).
- Version DOI for v0.1.0-alpha: [10.5281/zenodo.20289688](https://doi.org/10.5281/zenodo.20289688).

## Notes on versioning

The `KKK-AA-SSSS` booklet identifier is immutable. A booklet's content version is tracked in its own `version` frontmatter field. A repository tag (`v0.x.y` or `v1.0.0` and later) bundles a set of booklet versions and corresponds to a Zenodo release.
