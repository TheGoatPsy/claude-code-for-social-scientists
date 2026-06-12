# JOSE Submission Package, v3.0.0

Working checklist for submitting the paper in [`paper/paper.md`](../paper/paper.md) to the Journal of Open Source Education (JOSE). The actual submission is a maintainer-gated step and has not been performed. This document records readiness, the remaining open items, and the reasoning behind them.

## Scope fit

JOSE reviews two submission types, open educational resources (learning modules) and open-source software with a documented teaching purpose. This repository is both: twenty-one bilingual booklets organized as standalone teaching units, and an installable skills package (`social-cc-plugin`) with a CLI. The paper presents it as a learning module with companion software, which matches the journal's stated scope.

## Readiness checklist

| Item | Status |
|---|---|
| Public repository with issue tracker | Ready. GitHub, issues enabled, templates in place. |
| Paper in `paper/paper.md` with JOSE metadata block | Ready. Title, tags, author with ORCID, affiliation, date, bibliography. |
| `paper/paper.bib` with resolvable DOIs | Ready. Ten entries, every DOI verified against Crossref before inclusion. |
| Statement of need | Ready. Paper section two, grounded in survey evidence and the bilingual access gap. |
| Software/package installability | Ready. `pip install social-cc-plugin`, Claude Code plugin manifest, `social-cc doctor` environment check, pytest suite in CI on Python 3.9 and 3.12. |
| Archive DOI | Ready. Zenodo concept DOI 10.5281/zenodo.20289687 plus per-version DOIs through v3.0.0. |
| Community guidelines | Ready. CONTRIBUTING in both languages, CODE_OF_CONDUCT, SECURITY. |
| Quality control description | Ready. Paper section seven mirrors the CI reality: validator, markdownlint, pytest, cff-validator, gitleaks. |
| Paper compiles with the Open Journals toolchain | Pending first run. The `draft-pdf.yml` workflow added in v3.0.0 compiles the paper with the official `openjournals-draft-action`; run it from the Actions tab and attach the artifact to the submission. |
| Affiliation confirmation | Open. The affiliation line is taken verbatim from `CITATION.cff` and carries an author-confirmation note in `paper.md`. Confirm or adjust before submitting. |
| License compatibility | Open question, see below. |

## The license question

The repository is dual-licensed: Apache-2.0 for code (the root `LICENSE` file) and CC-BY-NC-SA-4.0 for prose and booklets (`LICENSE.content`). The JOSE reviewer checklist asks whether the repository contains a plain-text LICENSE file with the contents of an OSI-approved license. The literal requirement is satisfied, because the root `LICENSE` is Apache-2.0 and the software components are genuinely under it.

The open question is editorial rather than mechanical. JOSE's spirit for learning modules favors open licenses, and the NonCommercial clause on the prose is more restrictive than CC-BY, which Open Journals itself uses for papers. Three options, in the maintainer's order of preference:

1. Submit as is, with the dual-license structure stated transparently in the submission notes, and let the editor weigh it. The software meets the OSI requirement and the prose remains openly readable, shareable, and adaptable under NC-SA terms.
2. Open a pre-submission inquiry on the Open Journals GitHub before submitting, asking whether CC-BY-NC-SA prose alongside Apache-2.0 code is acceptable for a learning-module submission.
3. Relicense the prose to CC-BY-4.0. This removes the question entirely at the cost of giving up the NonCommercial protection, and it is a decision only the author can make.

No option is exercised in v3.0.0. The choice belongs to the maintainer at submission time.

## Submission mechanics, when gated open

1. Run the `Draft paper PDF` workflow from the Actions tab and review the artifact.
2. Confirm the affiliation line in `paper/paper.md`.
3. Resolve the license question above (option 1, 2, or 3).
4. Submit at the JOSE web form with the repository URL and the v3.0.0 Zenodo DOI.
5. Track the review issue on the openjournals/jose-reviews repository and respond through the established rebuttal discipline of booklet 010-01-0001.
