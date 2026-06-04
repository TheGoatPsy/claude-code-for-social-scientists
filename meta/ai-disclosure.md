# AI Disclosure, Aggregate Tracking

This file provides an aggregate, machine-friendly view of AI contribution levels and human review states across every booklet with committed AI-assisted drafting (released or draft) in the repository. The authoritative per-file disclosure lives in each booklet's own YAML frontmatter, generated according to the policy in [`AI-AUTHORSHIP.md`](../AI-AUTHORSHIP.md).

This page is updated by the maintainer at each release. Readers who want the latest disclosure for a specific booklet should always check the booklet's own frontmatter, not this aggregate.

## Aggregate table (as of v2.4.0, 2026-06-04)

| Booklet ID | Language | Contribution level | Human review | Verified citations | Fabricated citations | Last reviewed |
|---|---|---|---|---|---|---|
| 001-01-0001 | tr | substantial-drafting | complete | 13 | 0 | 2026-06-04 |
| 001-01-0001 | en | substantial-drafting | complete | 13 | 0 | 2026-06-04 |
| 001-01-0002 | tr | substantial-drafting | complete | 10 | 0 | 2026-06-04 |
| 001-01-0002 | en | substantial-drafting | complete | 10 | 0 | 2026-06-04 |
| 001-01-0003 | tr | co-drafting | complete | 6 | 0 | 2026-06-04 |
| 001-01-0003 | en | co-drafting | complete | 6 | 0 | 2026-06-04 |
| 002-04-0001 | tr | co-drafting | complete | 10 | 0 | 2026-06-04 |
| 002-04-0001 | en | co-drafting | complete | 10 | 0 | 2026-06-04 |
| 003-01-0001 | tr | co-drafting | complete | 9 | 0 | 2026-06-04 |
| 003-01-0001 | en | co-drafting | complete | 9 | 0 | 2026-06-04 |
| 004-01-0001 | tr | substantial-drafting | complete | 9 | 0 | 2026-06-04 |
| 004-01-0001 | en | substantial-drafting | complete | 9 | 0 | 2026-06-04 |
| 007-02-0001 | tr | substantial-drafting | complete | 10 | 0 | 2026-06-04 |
| 007-02-0001 | en | substantial-drafting | complete | 10 | 0 | 2026-06-04 |
| 009-01-0001 | tr | co-drafting | complete | 12 | 0 | 2026-06-04 |
| 009-01-0001 | en | co-drafting | complete | 12 | 0 | 2026-06-04 |
| 010-01-0001 | tr | substantial-drafting | complete | 8 | 0 | 2026-06-04 |
| 010-01-0001 | en | substantial-drafting | complete | 8 | 0 | 2026-06-04 |
| 012-01-0001 | tr | co-drafting | complete | 7 | 0 | 2026-06-04 |
| 012-01-0001 | en | co-drafting | complete | 7 | 0 | 2026-06-04 |
| 001-01-0004 | tr | full-draft | complete | 9 | 0 | 2026-06-04 |
| 001-01-0004 | en | full-draft | complete | 9 | 0 | 2026-06-04 |
| 008-01-0001 | tr | substantial-drafting | complete | 10 | 0 | 2026-06-04 |
| 008-01-0001 | en | substantial-drafting | complete | 10 | 0 | 2026-06-04 |
| 008-02-0001 | tr | substantial-drafting | complete | 11 | 0 | 2026-06-04 |
| 008-02-0001 | en | substantial-drafting | complete | 11 | 0 | 2026-06-04 |

Booklet 001-01-0004 was added in the v2.0.0 cycle as a full AI draft and then human-reviewed by the author, so its human review state is `complete` and it ships at `release` status in v2.0.0. Booklet 008-01-0001 was drafted bilingually in the v2.1.0 cycle at `substantial-drafting` level, human-reviewed by the author, and promoted to `release` status, so its review state is `complete`. Booklet 008-02-0001 was drafted bilingually after the v2.1.0 release at `substantial-drafting` level, human-reviewed by the author, and promoted to `release` status in v2.2.0, so its review state is `complete`. Eighteen booklets in [`CATALOG.md`](../CATALOG.md) remain at `planned` status and have no AI disclosure yet because no booklet-level AI-assisted drafting work has been committed for them.

## Citation discipline summary

| Metric | Value |
|---|---|
| Booklets at `release` status | 13 |
| Booklets at `paired` status | 0 |
| Booklets at `draft` status | 0 |
| Booklets at `planned` status | 18 |
| Total verified citation declarations across all disclosed language files | 248 |
| Unique bilingual citation sets across released booklets | 124 |
| Total fabricated citations across all disclosed language files | 0 |
| Fabrication rate, fabricated divided by verified plus fabricated | 0% |

## Contribution level distribution

| Level | Count |
|---|---|
| 1, editing-only | 0 |
| 2, light-assistance | 0 |
| 3, co-drafting | 10 |
| 4, substantial-drafting | 14 |
| 5, full-draft | 2 |

## Human review state distribution

| State | Count |
|---|---|
| complete | 26 |
| partial | 0 |
| pending | 0 |

The CI workflow refuses release booklet frontmatter that declares pending human review, fabricated citations, missing citation counts, stale placeholder DOI examples, broken bilingual pairs, or inconsistent catalog counts. See [`.github/workflows/ci.yml`](../.github/workflows/ci.yml) and [`scripts/validate-repo.mjs`](../scripts/validate-repo.mjs).

## Update history

| Date | Trigger | Change |
|---|---|---|
| 2026-05-19 | v0.1.0-alpha scaffold | Initial aggregate created for 001-01-0001. |
| 2026-05-19 | v0.2.0 remediation | Disclosure schema aligned to `title_en`, `title_tr`, `model_alias`, and `model_dated`. |
| 2026-05-24 | v1.0.0 release | Aggregate expanded to all ten released bilingual booklets. Statuses, citation counts, human review state, and fabricated citation counts aligned to frontmatter. |
| 2026-05-24 | v1.1.0 release | Companion project skills and the `social-cc-plugin` distribution added. Booklet disclosure content unchanged; the aggregate is re-affirmed for the v1.1.0 tag. |
| 2026-05-24 | v1.1.1 release | Metadata hygiene patch. Booklet disclosure content unchanged; the aggregate is re-affirmed for the v1.1.1 tag. |
| 2026-05-29 | v2.0.0 release | Booklet 001-01-0004 (CLAUDE.md and standing-instruction discipline) added at full-draft level, human-reviewed by the author, and promoted to `release` status. The aggregate now covers disclosed booklets at all statuses, and the verified and fabricated citation labels were generalized from released to all disclosed language files. |
| 2026-05-29 | v2.1.0 release | Booklet 008-01-0001 (Reproducible Quantitative Workflows) drafted bilingually at `substantial-drafting` level, human-reviewed by the author, and promoted to `release` status. Nine verified citations per language file, motivated by the Anthropic 2026 coding-agents survey. Aggregate verified declarations rise from 204 to 222, and the released catalog grows from eleven to twelve booklets. |
| 2026-05-29 | v2.2.0 release | Booklet 008-02-0001 (Statistical Test Selection with AI Consultation Discipline) drafted bilingually at `substantial-drafting` level, human-reviewed by the author, and promoted to `release` status. Nine verified citations per language file, zero fabricated. The released catalog grows from twelve to thirteen booklets, the second Data Analysis booklet, motivated by the Anthropic 2026 survey's named fear of selective reporting. Aggregate verified declarations rose from 222 to 240. |
| 2026-05-29 | v2.3.0 release | Turkish-language quality revision. The Turkish prose of all thirteen released booklets and both Turkish-language README and CONTRIBUTING files was rewritten in the author's native voice. No booklet was added or removed. All aggregate metrics are unchanged: 240 verified declarations, 0 fabricated, 26 human-reviewed language files, 13 booklets at `release` status. |
| 2026-06-04 | v2.4.0 quality upgrade | All thirteen released booklets (both tr.md and en.md) underwent a two-dimensional upgrade: substantive scholarship and technical corrections first, then the author's voice (English natural register, Turkish native championship craft). Corpus-wide scholarship work separated evidence from the guide's own inference, hedged unsupported claims rather than fabricating citations, and corrected misstatements (for example, EU AI Act Article 50 scope in 009-01-0001, which governs providers and deployers and synthetic media, not an individual researcher flagging all AI-assisted text). Citations added after Crossref-live and claim-support verification: Xu et al. (2025) in 001-01-0001, an Anthropic Claude Code documentation reference in 001-01-0004, Jones (2007) in 004-01-0001, Bramer et al. (2017) in 007-02-0001, Wilson et al. (2017) and Ziems et al. (2024) in 008-01-0001, Simonsohn et al. (2020) and Munafo et al. (2017) in 008-02-0001, and Bordage (2001) in 010-01-0001. Misapplied or phantom citations removed: Engel (1977) from 003-01-0001, Greenhalgh et al. (2016) from 007-02-0001, Tufte (1990) from 004-01-0001, and Squazzoni et al. (2021) and Resnik (2018) from 010-01-0001. No booklet was added or removed and no heading structure changed. Aggregate verified declarations rise from 240 to 248; unique bilingual citation sets rise from 120 to 124. |

---

**Authoritative source.** Each booklet's own frontmatter, not this aggregate.

**Policy.** [`AI-AUTHORSHIP.md`](../AI-AUTHORSHIP.md).
