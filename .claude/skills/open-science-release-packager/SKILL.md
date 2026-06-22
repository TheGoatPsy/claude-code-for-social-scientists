---
name: open-science-release-packager
description: Use when a study's materials, data, code, or preprint need an open-science release: license choice, a persistent DOI (Zenodo/OSF), README and metadata, and an access-and-embargo decision that respects ethics constraints.
---

# Open Science Release Packager

## When to use

Use this skill when a completed or near-complete study needs to be released as a reproducible open-science package: data or its shareable derivative, analysis code, supplementary materials, a data dictionary, a license, and a persistent DOI via Zenodo or OSF. It works downstream of authorship-contribution-ledger, which supplies the contributor list and CRediT statement the README needs, and downstream of sensitive-data-anonymization-gate, whose report must accompany any data release. Run repo-release-integrity-check before the final upload, and route any AI-use disclosure questions to ethics-irb-ai-protocol. It is not for releasing data before the anonymization gate has run, for publishing code whose operating environment is undocumented, or for treating a DOI as a guarantee of reproducibility rather than a guarantee of persistence.

## Inputs

- The manuscript or report the release accompanies.
- The data or its shareable anonymized derivative, with the anonymization-gate report attached.
- The analysis code and its execution environment: language version, package versions, operating system.
- Supplementary materials to be included.
- The data dictionary describing every variable.
- License preference for data and for code, which may differ.
- Ethics approval status and any embargo or restricted-access conditions imposed by the board.
- The CRediT contributor list from authorship-contribution-ledger.

## Workflow

1. State explicitly what the package includes and what it withholds, with the ethical or legal reason for each withheld item.
2. Classify each data file by shareability: fully open, embargoed, restricted-access with application, or not releasable; document the classification and its basis.
3. Confirm that sensitive-data-anonymization-gate has run on any participant-level data before it enters the package.
4. List all code, data, and supplementary file paths with their roles in the analysis.
5. Write the reproduction steps in enough detail that a reader with no prior contact with the project can re-execute the analysis from the archived files.
6. Choose licenses separately for the dataset and for the code — common pairings are CC BY 4.0 for data and MIT or Apache 2.0 for code — and state the rationale.
7. Draft the README covering: study summary, package contents with file paths, reproduction instructions, license statements, contributor list with CRediT roles from authorship-contribution-ledger, AI-use disclosure, and the ethics approval reference.
8. Hand off to ai-disclosure-auditor to produce the AI-use disclosure before the upload; the disclosure output must be attached to the package before proceeding to the next step.
9. Run repo-release-integrity-check before the upload; address every flag it raises before proceeding.
10. Note the distinction between the concept DOI (stable across all versions) and the version DOI (specific to this upload), and record both after the Zenodo or OSF deposit.

## Output

Return:

- A README draft with all required sections: study summary, contents, reproduction steps, licenses, CRediT contributors, AI-use disclosure, and ethics reference.
- A data dictionary for every variable included in the released dataset.
- A codebook for any coded or categorical variables.
- A reproduction note detailing software environment, execution order, and expected outputs.
- A supplementary materials index with file names, roles, and formats.
- A license summary stating the chosen license for data and for code, with reasons.
- A Zenodo or OSF release checklist covering required metadata fields, embargo settings, and access-level configuration.
- What to record at session end: which files were included and which withheld with reasons, the concept DOI and version DOI once issued, any flags raised by repo-release-integrity-check and their resolution, and the handoff to authorship-contribution-ledger for contributor confirmation.

## Verification

- Every data file in the package passed through sensitive-data-anonymization-gate; no raw participant data is present.
- The reproduction steps were tested or explicitly marked as untested, with untested steps flagged for the researcher to verify.
- Licenses for data and code are stated separately and are compatible with any third-party dependencies or source datasets.
- The data dictionary covers every variable column in the released dataset.
- The concept DOI and version DOI are recorded and distinct.
- Withheld items are documented with their reason, not silently omitted.
- Before closing: repo-release-integrity-check has been run and all raised flags resolved, and a researcher has confirmed the contributor list and CRediT roles match the authorship-contribution-ledger record.

## Safety

Open science means releasing what can be released responsibly, not releasing everything. Data that cannot be fully anonymized must be withheld and that fact stated clearly in the README; a vague "data available on request" without an access mechanism is not a compliant substitute. Code that cannot be executed in a documented environment should not claim reproducibility. A DOI provides persistence, not correctness; it does not validate the analysis or the findings. AI contribution to this packaging step must be disclosed: name the stage, identify the model, describe what it produced, and confirm what human review verified before inclusion. Do not include any material in the package before sensitive-data-anonymization-gate has cleared it.

## Example prompt

"Bu çalışma için açık bilim paketi hazırla: Zenodo yüklemesi için README, veri sözlüğü, yeniden üretim notu, lisans seçimi, CRediT katkı listesi ve DOI notu. Paylaşılamayan veri varsa nedenini açıkça yaz ve embargo kararını belgele."

Expected smoke output:

- A README draft covering study summary, file paths, reproduction steps, CC BY 4.0 data license and MIT code license, CRediT table from authorship-contribution-ledger, AI-use disclosure, and the ethics approval reference.
- A data dictionary for the released dataset variables.
- A Zenodo release checklist with embargo settings and a note distinguishing concept DOI from version DOI.
- A flag to run repo-release-integrity-check before the upload and a reminder to pass any participant-level data through sensitive-data-anonymization-gate first.

## Türkçe kullanım notu

Açık bilim, paylaşılabilecek olanı düzenli ve sorumlu biçimde açmaktır — her şeyi açmak değil. Bu beceri, bir çalışmanın veri, kod ve ek materyallerini Zenodo ya da OSF üzerinde kalıcı DOI ile yayınlamak için gereken tüm katmanları örgüler: README, veri sözlüğü, yeniden üretim notu, lisans kararı, CRediT katkı tablosu ve erişim düzeyi seçimi. Katılımcı düzeyinde veri ancak sensitive-data-anonymization-gate'ten geçtikten sonra pakete girer — bu adım atlanmaz. Paylaşılamayan veri sessizce dışarıda bırakılmaz, README'de nedeniyle birlikte açıklanır. Veri lisansı ve kod lisansı ayrı düşünülür. İkisini karıştırmak üçüncü taraf kaynaklarla çakışmaya açık kapı bırakır. DOI kalıcılık sağlar, doğruluk değil. Analiz ortamı belgelenmemişse yeniden üretilebilirlik iddiası sınırlandırılır. Paket yüklenmeden önce repo-release-integrity-check çalıştırılır. Katkı listesi authorship-contribution-ledger'dan gelir — iki beceri birbirini tamamlar.
