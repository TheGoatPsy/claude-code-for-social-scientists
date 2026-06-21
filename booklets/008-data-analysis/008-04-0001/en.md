---
title_en: "Preparing Sensitive Data, Anonymization, Masking, and Local Preprocessing"
title_tr: "Hassas Veriyi Hazırlamak, Anonimleştirme, Maskeleme ve Yerel Ön İşleme"
booklet_id: "008-04-0001"
category: "008-data-analysis"
language: "en"
version: "0.1.0"
date_published: "2026-06-21"
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
    model_dated: null  # no dated identifier published by Anthropic for Opus 4.8 as of 2026-06-21
    role: "drafting, verification, citation lookup, bilingual authoring"
    interaction_mode: "interactive console"
ai_contribution_level: "substantial-drafting"
human_review: "complete"
human_review_date: "2026-06-21"
verified_citations_count: 9
fabricated_citations_count: 0
disclosure_standard: "COPE 2023 + WAME 2023 + ICMJE 2024 + STM 2025 + EU AI Act 2024/1689 Art. 50 + ENAI"
translation_notes: "Re-authored natively from the finalized Turkish source (tr.md v0.1.0, 2026-06-21). The argument, section structure, and bibliographic set are identical across both languages; phrasing is native to each. Not a literal translation. All DOIs verified against Crossref and doi.org on 2026-06-21."
license:
  - "CC-BY-NC-SA-4.0 (prose)"
status: "release"
---

# Preparing Sensitive Data, Anonymization, Masking, and Local Preprocessing

The most common way a research project goes wrong is not a mistaken statistical test. It is raw data reaching the wrong place. Interview transcripts, clinical notes, field diaries, and student texts outlive the researchers who collected them and reach audiences far wider than any consent form anticipated. This booklet addresses how that material is converted into safe working data before it enters any AI workflow. The foundational rule is simple: anonymization before the tool, not after.

## 1. Raw data, working data, shareable data

Raw data is the material as the participant gave it or the researcher collected it. It records the voice fully, the name fully, the address fully. Working data is the analytic copy with identity and contextual risk reduced (the file that is actually open during a research session). Shareable data has passed a further filter and can be released externally within the bounds of ethical approval and legal compliance.

The boundary between these three layers is not maintained by good intentions alone. Carrying raw data into an AI session by accident erases the distinction, and the damage is not easily undone. Folder architecture should make the separation structural: the raw archive in one location, the working directory in another, the sharing folder in a third. Claude Code operates only in the working directory. No automation touches the raw archive.

Conflating these layers has legal as well as ethical consequences. In Türkiye, the Personal Data Protection Law (KVKK, Law No. 6698) and, in the European context, the General Data Protection Regulation bind the researcher's handling of raw data to a specific legal framework (Kişisel Verileri Koruma Kurumu, 2016; European Parliament and Council, 2016). The participant signed a consent form that implies a working copy, not an open-ended license over everything the researcher holds.

## 2. Anonymization and pseudonymization

These two concepts are not the same, and treating them as synonyms is a substantive security error.

Pseudonymization replaces direct identifiers with codes: Mehmet becomes P07, Ankara Training and Research Hospital becomes Hospital B. The researcher holds the linkage table; reconstruction is possible on demand. Both GDPR and KVKK are explicit: pseudonymized data remains personal data, because re-linkage via the key is possible.

Anonymization aims to eliminate re-identification risk to a reasonable standard. Deleting a name is necessary but nowhere near sufficient. Sweeney (2002) demonstrated that the combination of postal code, sex, and date of birth, three variables that appear entirely innocuous in isolation, uniquely identified 87 percent of the United States population. A systematic review of re-identification attacks on health datasets found that up to 85 percent of individuals could be re-identified using relatively limited contextual information (El Emam et al., 2011). Those numbers make clear why anonymization in large datasets cannot be treated as a completed action. It is an ongoing risk-management process.

## 3. Direct and indirect identifiers

Name, surname, telephone number, email address, and national identification number are direct identifiers. They are usually recognized and removed. The real exposure lies in indirect identifiers.

An indirect identifier is a variable that does not identify anyone on its own but does so in combination with other information: place, occupation, family structure, a rare event, a specific date. In a small community, a village name, a school, a recognizable teacher, and an event year combine into an identifiable individual. Qualitative data is particularly vulnerable here. The narrative detail that makes an interview rich, the dramatic specificity of a lived experience, carries identifier value, and researchers frequently miss this.

The NIST technical guide on the de-identification of personal information (Garfinkel, 2015) systematizes the distinction between direct and indirect identifiers and specifies the transformations that apply to each data type. An anonymization report must address both categories separately. No process should be considered complete until a checklist across indirect identifiers has been run.

## 4. Clinical data protocol

Clinical data is a special-category data type. Article 6 of KVKK and Article 9 of GDPR both place health data, biometric data, and psychological assessment records under a separate, stricter legal protection. Processing this category requires either explicit consent that names the purpose or an equally specific legal basis.

Case notes, diagnostic information, treatment history, family psychiatric history, and psychometric results are held in the region of the archive closed to model access. The subset of this material required for a specific research question is transferred into a working copy that carries only the minimum information necessary. Unnecessary clinical detail is stripped here, before the working copy is ever opened. Every field the research question does not require leaves the copy.

When clinical examples are to be used for teaching or publication, de-identification alone is insufficient. Context reduction is also required. The city in which a case occurred, the institution, the approximate year range, the size of the community: each of these can function as an indirect identifier and each demands a deliberate decision. That decision integrates the researcher's own professional judgment, the expectations of the relevant ethics committee, and the norms of the publication's intended audience.

## 5. Interview and field note protocol

Interview transcripts carry a participant's identity not only through their name but through the texture of what they say. A participant who describes their childhood village, who refers without naming it to a significant loss in a particular year, who characterizes a teacher by their distinctive habits, who implies the size of a classroom by the way they describe a seating arrangement: each of those details is a separate identifier. In field notes, place and relational network build an even denser identifier set.

For this reason transcripts pass through a masking table before they enter any analysis workflow. Each field (person, place, institution, event, date) is marked separately. A decision is made for each: generalize, delete, or replace with a label that preserves enough context to support analysis without exposing identity? Saunders et al. (2015) showed why this decision cannot be reduced to a single rule applied uniformly. The researcher makes a genuine trade-off between the analytic value of a detail and the re-identification risk it carries. There is no standard script for interview data; the masking logic of each study is specific to that study.

## 6. Local preprocessing

Local preprocessing is the cleaning of data on the researcher's own machine before it reaches any third-party model or cloud service. This step is not a technical convenience. It is an ethical requirement.

Ohm (2010) documented in detail the fragility of anonymization techniques, showing that the technical promise of irreversibility has consistently failed under real-world conditions. Against this background, local preprocessing is the only control point that limits exposure before upload. The practical sequence runs as follows: a plain-text copy is created from the raw file, identity fields are marked, masking is applied, the secure version is written to a separate directory, and that directory — nothing else — is opened to the Claude Code workflow. No automation reaches the raw file directory.

Local preprocessing has a secondary benefit that is easy to undervalue. It brings the researcher into direct contact with the data before any AI mediation. This mirrors the specification-log logic built in the first booklet of this category: the researcher passes through the material, makes decisions, builds a record. The cognitive friction this produces is not overhead to be eliminated. It is part of the research process.

## 7. The masking table

The masking table maintains a record of every substitution made in the working copy. Participant code A, city code X, institution code Y — each row carries the original value, the label applied, the justification for the substitution, and the date of application.

This table does not live alongside the working data. It is held in a separate, access-controlled, encrypted location and remains there for the full duration of the research. Two failure modes explain why. When the masking table is lost and reconstruction becomes necessary, the researcher may no longer be able to connect codes to participants — context is gone. When the masking table is left unprotected, anonymization is entirely undone; anyone with access can reverse the process.

Narayanan and Shmatikov (2008) showed how successfully re-identification attacks can be carried out against large sparse datasets that appear safely anonymized. Rocher et al. (2019) extended that finding to incomplete datasets, demonstrating with a generative model that the risk persists even when only partial information is available. These results concretize why the masking table is a genuine security component, not an administrative formality.

## 8. What must never be given to an AI tool

This list is short, absolute, and does not bend under convenience.

Open identifiers, consent forms, audio and video recordings (the recordings themselves, not transcripts), biometric traces, raw clinical notes, narratives identifiable within small communities, and the masking table itself are never given to an AI tool. The capability of the tool is not a reason to relax the boundary. The tool meets only the secure working copy.

Two points require additional attention. First: quotations that the researcher believes contain too little information to identify anyone, but in which indirect identifiers have combined without the researcher noticing. Second: participant lists automatically generated by video conferencing platforms, or meeting notes that include participant names. These sometimes carry direct identifiers as transparent as any raw clinical note, but their document format causes them to be overlooked.

## 9. Post-anonymization audit

Completing the secure copy is not the end of the process. Automated tools alone are not sufficient verification. Human review is mandatory.

The audit consists of reading randomly selected samples from the secure copy without reference to the masking table, evaluating them for re-identification risk, and attending specifically to indirect identifiers. Can the reader recognize someone? Which combination of details constitutes a potential risk? This reading is done by the researcher before the working copy enters any AI session.

Anonymization is not a technical cleaning step. It is an ethical decision process. The size of the dataset, the recognizability of the community, the platform through which findings will be disseminated, and the homogeneity of the participant population all enter into it. Rocher et al. (2019) applied a statistical re-identification risk model to a clinical context, incorporating precisely these variables. The researcher draws on every available tool, but the final judgment always belongs to the person responsible for the research.

## 10. Skill outputs

`/sensitive-data-anonymization-gate` produces four outputs, each corresponding to a decision point. The anonymization report is a record of the transformations applied and their justifications. The masking table is the traceable set of every substitution. The indirect identifier risk note lists fields that warrant further review. The secure working copy is the only data file that will be opened to the model.

The skill is a gate, not a speed tool. If any of these four outputs is missing or appears insufficient, the data does not enter the model. Anonymization lives inside a process, and the final step of that process is always the researcher's own assessment.

## References

Citations are in APA 7 format. All DOIs were verified against Crossref and doi.org on 2026-06-21. KVKK and GDPR are official legal instruments and do not carry DOIs; links are given to the official publication sources.

El Emam, K., Jonker, E., Arbuckle, L., & Malin, B. (2011). A systematic review of re-identification attacks on health data. *PLOS ONE*, 6(12), e28071. https://doi.org/10.1371/journal.pone.0028071

European Parliament and Council. (2016). *Regulation (EU) 2016/679 of the European Parliament and of the Council of 27 April 2016 on the protection of natural persons with regard to the processing of personal data and on the free movement of such data, and repealing Directive 95/46/EC (General Data Protection Regulation)*. https://eur-lex.europa.eu/eli/reg/2016/679/oj

Garfinkel, S. L. (2015). *De-identification of personal information* (NIST IR 8053). National Institute of Standards and Technology. https://doi.org/10.6028/NIST.IR.8053

Kişisel Verileri Koruma Kurumu. (2016). *6698 sayılı Kişisel Verilerin Korunması Kanunu* [Personal Data Protection Law No. 6698]. https://www.kvkk.gov.tr

Narayanan, A., & Shmatikov, V. (2008). Robust de-anonymization of large sparse datasets. *IEEE Symposium on Security and Privacy*, 111–125. https://doi.org/10.1109/SP.2008.33

Ohm, P. (2010). Broken promises of privacy: Responding to the surprising failure of anonymization. *UCLA Law Review*, 57, 1701–1777.

Rocher, L., Hendrickx, J. M., & de Montjoye, Y. A. (2019). Estimating the success of re-identifications in incomplete datasets using generative models. *Nature Communications*, 10, Article 3069. https://doi.org/10.1038/s41467-019-10933-3

Saunders, B., Kitzinger, J., & Kitzinger, C. (2015). Anonymising interview data: Challenges and compromise in practice. *Qualitative Research*, 15(5), 616–632. https://doi.org/10.1177/1468794114550439

Sweeney, L. (2002). k-anonymity: A model for protecting privacy. *International Journal on Uncertainty, Fuzziness and Knowledge-Based Systems*, 10(5), 557–570. https://doi.org/10.1142/S0218488502001648

---

**Booklet ID.** `008-04-0001`
**Version.** `0.1.0`
**Date.** 2026-06-21
**License.** This booklet is licensed under CC BY-NC-SA 4.0. https://creativecommons.org/licenses/by-nc-sa/4.0/
**Approximate word count.** 1836 (English body text, measured with wc)
**Verified citations.** 9
**Fabricated citations.** 0
**Previous booklet.** [`008-03-0001`](../008-03-0001/en.md). Qualitative Coding with AI Assistance and Human Oversight
**Next booklet.** [`008-05-0001`](../008-05-0001/en.md). Research Protocol and Preregistration, Deciding Before Analysis
