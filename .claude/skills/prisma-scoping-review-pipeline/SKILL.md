---
name: prisma-scoping-review-pipeline
description: Use when a systematic, scoping, or rapid review needs a reproducible pipeline: protocol framing (PICO/SPIDER/PCC), a logged search string, title/abstract and full-text screening with recorded exclusion reasons, and PRISMA flow counts, with the human as the deciding screener.
---

# PRISMA Scoping Review Pipeline

## When to use

Use this skill when a systematic review, scoping review, or rapid review needs a reproducible, auditable pipeline rather than an ad hoc read of the literature: protocol framing, a logged search string, screening with recorded decisions, and PRISMA flow counts. In the wider lifecycle it builds the search layer through social-science-literature-triage and regional-access-workflow, and its per-record decisions feed source-passport-ledger and then apa-doi-verifier. It is not the place for an informal background read, which belongs to social-science-literature-triage, and the AI never owns the final include or exclude decision, which stays with the human screener.

## Inputs

- The research question and the review type, systematic, scoping, or rapid.
- The framing scheme, PICO, SPIDER, or PCC.
- Databases and access routes.
- Inclusion and exclusion criteria, written before any result is seen.
- Search results or screening exports.
- The reviewer arrangement, single or double screening, and the conflict rule.

## Workflow

1. Fix the review type first, because it sets the evidence claim the review is allowed to make.
2. Structure the question with the matching framework, PICO, SPIDER, or PCC.
3. Build the database layer with social-science-literature-triage and regional-access-workflow, and log every search string with its database and date.
4. Write the inclusion and exclusion criteria before looking at the result set.
5. Bind each retrieved record to a source passport so every count stays traceable.
6. Run title and abstract screening with AI support but human decision, recording a reason for every exclusion; any record carrying sensitive or identifying data must first pass through sensitive-data-anonymization-gate before it enters the AI screening step.
7. At full text, write an explicit exclusion reason against each removed record.
8. Assemble the PRISMA flow counts from the screening log, never from an estimate, and draft the AI-use disclosure for the screening step.

## Output

Return:

- A review protocol skeleton carrying the framing scheme.
- The search-string log, with database, string, date, and hits.
- Title/abstract and full-text screening tables with each decision and its reason.
- The PRISMA flow counts: identified, screened, excluded with reasons, included.
- An AI-use disclosure note for the screening stage.
- What to record at session end: the output file paths, the decisions still awaiting a second screener, and the handoff of the included set to apa-doi-verifier.

## Verification

- Every PRISMA number traces to a row in the screening log, never to an estimate.
- The inclusion and exclusion criteria were written before the results were screened.
- Every excluded full-text record carries a stated reason.
- Where double screening is required, a conflict-resolution rule is recorded.
- Before closing: each include or exclude decision is attributable to the human screener, and the search is reproducible from the logged strings alone.

## Safety

AI may pre-screen, but the final include or exclude decision belongs to the human reviewer, because a single excluded source can change the review's conclusion. PRISMA counts are read from the record, not guessed. Sensitive, clinical, or identifying material passes through sensitive-data-anonymization-gate before any AI tool sees it. Document AI involvement at every stage: note the model used, the nature of its contribution, and the human review step that followed.

## Example prompt

"Bu araştırma sorusu için bir kapsam derlemesi hattı kur: çerçeveleme şemasını, arama dizgesi günlüğünü, dahil etme ve dışlama ölçütlerini, tarama tablosunu ve PRISMA sayılarını insan karar noktalarıyla birlikte göster."

Expected smoke output:

- A PCC-framed question and a logged search string for each database.
- Title/abstract and full-text screening tables with an exclusion reason on every removed record.
- PRISMA flow counts assembled from the log, plus the handoff to apa-doi-verifier for the included references.

## Türkçe kullanım notu

Bu beceri sistematik derlemeyi, kapsam derlemesini ya da hızlı derlemeyi gelişigüzel bir okuma olmaktan çıkarıp izlenebilir bir hatta taşır. Soruyu PICO, SPIDER ya da PCC ile çerçeveler, her arama dizgesini veri tabanı ve tarihiyle kaydeder, taramada her dışlamaya gerekçe yazar, PRISMA sayılarını tahminle değil kayıttan toplar. Yapay zekâ ön eleme yapabilir ama dahil etme ve dışlama kararı insan değerlendiricide kalır, çünkü dışlanan tek bir kaynak derlemenin sonucunu değiştirebilir. Arama katmanını social-science-literature-triage ve regional-access-workflow ile kurun, dahil edilen kaynakları apa-doi-verifier'a devredin. Hassas ya da kimlik içeren veri, herhangi bir araca girmeden önce sensitive-data-anonymization-gate'ten geçirilmelidir.
