---
name: multilingual-concept-validity-audit
description: Use when a construct, scale, or key term crosses Turkish and English and conceptual equivalence must be audited: translation and back-translation, construct drift, and culturally bound meaning, before measurement or cross-cultural claims.
---

# Multilingual Concept Validity Audit

## When to use

Use this skill when a construct, scale, or key term must travel between Turkish and English and the question is whether the concept carries the same meaning in both languages, not merely whether the words correspond. It applies before cross-cultural measurement, when back-translation alone has been used and conceptual drift has not been checked, when clinical psychology terms, minority-context vocabulary, or place names must be rendered across languages, and when a bilingual manuscript must claim cross-language equivalence. It is not a substitute for a qualified translator or for professional consultation when the stakes of misclassification are clinical. Handing the output to bilingual-manuscript-scaffold begins the drafting stage; qualitative-coding-discipline takes over when coded data contains the same terms across languages.

## Inputs

- The source text or term list, in Turkish or English.
- The target text or translation, in the other language.
- The language pair or pairs under audit.
- The disciplinary domain and the specific research context.
- The intended audience or journal, which constrains acceptable register.
- Any local context notes, such as minority-community usage, regional legal meanings, or clinical versus everyday distinctions.

## Workflow

1. Extract the key constructs from the source text and rank them by conceptual importance, not word frequency.
2. For each construct, describe its usage context in the source language, including any disciplinary, cultural, or legal connotations it carries.
3. Evaluate the proposed target-language equivalent not only by dictionary match but by how the term functions in the target-language literature.
4. Flag four risk categories explicitly: clinical terms that shift meaning when translated literally, culturally bound terms that have no clean equivalent, minority-context terms that carry legal or historical weight, and place names where language-dependent conventions apply.
5. For each flagged construct, list acceptable alternatives with the conditions under which each is preferable, rather than forcing a single fixed translation.
6. Build the concept passport: a table mapping each source construct to its target equivalent, the risk category, the usage condition, and the researcher's decision status.
7. Run a cross-document consistency check, confirming that the same construct is rendered identically across all sections of a bilingual manuscript.
8. List separately all decisions that require the researcher's judgment, and hand off to bilingual-manuscript-scaffold for drafting, to qualitative-coding-discipline when coded data is involved, to statistical-consultation-protocol when measurement invariance must be tested, and to bilingual-booklet-pairing for paired-document parity.

## Output

Return:

- A conceptual equivalence table mapping each construct across languages with its risk category and usage condition.
- A flagged-term list identifying clinical, cultural, minority-context, and place-name risks.
- A concept passport ready to govern terminology choices across the manuscript.
- A list of decisions reserved for the researcher's judgment, clearly separated from AI-generated suggestions.
- What to record at session end: the concept passport file path, the terms still awaiting researcher confirmation, and the handoff condition for bilingual-manuscript-scaffold or qualitative-coding-discipline.

## Verification

- Every flagged term carries an explicit risk category and at least one stated usage condition.
- No single mandatory translation was imposed where more than one defensible choice exists.
- Clinical terms were evaluated against the target-language clinical literature, not only a dictionary.
- Minority-context and place-name entries were checked for legal or historical connotation, not only semantic content.
- Before closing: the researcher has reviewed and confirmed all decisions marked as requiring human judgment, and the concept passport is consistent with the final manuscript's terminology throughout.

## Safety

Language is the structure of thought, not merely its surface. A term that appears to translate directly can carry clinical, legal, or cultural weight that the target language does not reproduce — and a measurement instrument built on a misaligned translation produces data that cannot support cross-cultural claims. This skill therefore treats conceptual equivalence as a researcher decision that AI can support but never own. Any ambiguity in the equivalence table is flagged rather than silently resolved. When the terms involved come from a minority community with a specific legal or historical context, that context is named explicitly rather than collapsed into a generic translation. Sensitive participant data must pass through sensitive-data-anonymization-gate before it enters any audit workflow.

## Example prompt

"Bu Türkçe ve İngilizce metinlerdeki ana kavramları çıkar. Her kavram için hedef dildeki karşılıkları, bağlam risklerini, klinik veya kültürel kaymaları ve araştırmacı onayı gereken noktaları raporla, terim pasaportu hazırla."

Expected smoke output:

- A conceptual equivalence table listing each construct with its source-language context, target-language equivalent, risk category, and usage condition.
- A flagged-term list identifying at least the clinical, cultural, and minority-context risks present in the texts.
- A concept passport draft with researcher-decision items separated from confirmed equivalences.

## Türkçe kullanım notu

Bu beceri, diller arasında taşınan kavramın aynı anlam alanını koruyup korumadığını denetler. Çeviri doğruluğu değil kavramsal eşdeğerlik soruludur. "Anxiety" her bağlamda "anksiyete" değildir, kimi zaman "kaygı"dır. "minority" sözcüğü tarihsel ve hukuki yük taşıyabilir. Batı Trakya bağlamında bu ağırlık çok daha belirginleşir. Beceri dört risk kategorisini açıkça işaretler: klinik terim kaymaları, kültürel karşılıksızlık, azınlık bağlamı ve yer adı sözleşmeleri. Her kavram için tek zorunlu çeviri dayatmak yerine kabul edilebilir seçenekler ve kullanım koşulları sunulur. Araştırmacı kararını kendisi verir. Kavram pasaportu oluşturulduktan sonra bilingual-manuscript-scaffold taslak aşamasına, qualitative-coding-discipline kodlama verisine, statistical-consultation-protocol ölçüm değişmezliğine ve bilingual-booklet-pairing çift belge uyumuna devir için hazırdır.
