---
title_en: "Qualitative Coding with AI Assistance and Human Oversight"
title_tr: "Yapay Zekâ Yardımı ve İnsan Gözetimiyle Nitel Kodlama"
booklet_id: "008-03-0001"
category: "008-data-analysis"
language: "en"
version: "0.1.0"
date_published: "2026-06-12"
date_last_revised: "2026-06-20"
authors:
  - name: "Onour Impram"
    orcid: "0000-0003-1076-3928"
    role: "author, principal reviewer"
ai_assisted: true
ai_tools:
  - name: "Claude Code"
    vendor: "Anthropic"
    model_alias: "claude-fable-5"
    model_dated: null  # no dated identifier published by Anthropic for Fable 5 as of 2026-06-10
    role: "drafting, verification, citation lookup, bilingual re-authoring"
    interaction_mode: "interactive console"
ai_contribution_level: "substantial-drafting"
human_review: "complete"
human_review_date: "2026-06-20"
verified_citations_count: 6
fabricated_citations_count: 0
disclosure_standard: "COPE 2023 + WAME 2023 + ICMJE 2024 + STM 2025 + EU AI Act 2024/1689 Art. 50 + ENAI"
translation_notes: "English re-authored from the Turkish source, not a literal translation. The codebook example, the disagreement scenarios, and the disclosure sentence are synthetic and drawn from no real study or participant data, in keeping with the vault sanitization protocol. Citation audit 2026-06-10: all DOIs verified live against Crossref before drafting. Morgan (2023) restricted to the descriptive-versus-interpretive finding his case study reports; O'Connor and Joffe (2020) restricted to their subset-and-reporting guidance and their acknowledgment of the reflexive critique; Walters and Wilder cited for citation-level fabrication, with the extension to interview quotes marked in the body as an analogy."
license:
  - "CC-BY-NC-SA-4.0 (prose)"
status: "release"
---

# Qualitative Coding with AI Assistance and Human Oversight

The previous booklet built the consultation discipline on the quantitative side: a protocol in which the model advises on statistical test selection and the decision stays with the author. This booklet carries the same discipline to the qualitative side, and it sets the ground before anything else. Qualitative coding is not a data processing step. It is the act of interpretation itself. Assigning a code to a sentence in an interview transcript is making a decision about what that sentence is saying, and the decision cannot be made apart from the researcher's theoretical position. AI can be a powerful assistant in this process. Under which protocol that assistance becomes safe, how the integrity of quotations is protected, and how the contribution is disclosed are the subject of this booklet.

## 1. What Cannot Be Automated

In a large part of the qualitative tradition, the researcher's subjectivity is not an error source to be eliminated but the engine of the analysis. Braun and Clarke (2019), describing reflexive thematic analysis, put the point directly. Themes do not sit ready-made in the data waiting to be collected. They are produced within the researcher's relationship with the data and with theory. Inside this frame, handing coding entirely to a machine does not remove the method's error. It removes the method.

None of this excludes AI support. What it excludes is support turning into interpretive authority. The difference will be redrawn in every section of this booklet, and it will land in the same place each time. The model processes, the researcher means.

## 2. The Backbone of Thematic Analysis

Before the protocol comes the backbone itself. Braun and Clarke (2006), in the paper that systematized thematic analysis for psychology, describe the process in six phases: familiarization with the data, generating initial codes, searching for themes, reviewing themes, defining and naming themes, and producing the report. The phases are cyclical rather than linear. Reviewing a theme sends you back to the codes, and generating a code sends you back to the data.

The six phases also read as a map of where AI support belongs. In familiarization, support is legitimate and limited, because if the model reads the transcripts instead of the researcher, no familiarization has taken place. In code generation, support is at its most productive. In theme naming and reporting, the interpretive load is at its heaviest and the delegation risk at its highest.

## 3. Codebook Design

The codebook is the constitution of the coding. Four fields are kept for every code: the label, the conceptual definition, the inclusion and exclusion criteria, and an exemplar quotation taken directly from a transcript. The exclusion criterion is the most neglected field and the most valuable one, because the border between two codes is drawn exactly there. If expressions of anxiety and avoidance behavior are separate codes, the exclusion criterion is what says which side a sentence at their intersection falls on.

The codebook is a living document. As coding advances, definitions sharpen, codes merge or split, and every change is recorded with a dated note. The archive structure is the one built in this guide's memory booklets. The codebook lives in a single file, its version history is its log of change, and that log becomes raw material for the disclosure in section nine.

## 4. The Model's Place, a Second Coder Under Protocol

Claude Code can take two distinct roles in this workflow, and both have known limits. The first role is coding assistant. The model scans a transcript against the codebook definitions and proposes candidate code assignments. The second role is second coder under protocol. The model codes a section the researcher has already coded, using the same codebook, without seeing the researcher's assignments. The two codings are laid side by side, and the disagreements fall into a list.

This role has a realistic ceiling. Morgan (2023), in a case study comparing ChatGPT's qualitative analysis with a published human analysis, reported that the model could largely reproduce the descriptive themes and stayed weak on the latent, interpretive ones. The finding explains why the protocol is built the way it is. The model catches the surface pattern reliably, which makes it a good second pair of eyes at the descriptive layer. The interpretation that reaches into deep structure stays on the human side of the disagreement list.

## 5. Reliability Checkpoints

The disagreement list is the most productive material in the coding. O'Connor and Joffe (2020), reviewing the intercoder reliability debate, do two things at once. They show that a reliability check can raise transparency and systematicity, and they offer a practical frame that recommends applying the check to a meaningful subset of the data rather than all of it, with the process openly reported. The same paper records an honest tension. In the reflexive tradition, a high agreement rate is not a virtue in itself, because the richness of interpretation may live precisely in divergent readings.

The checkpoint in this workflow is built accordingly. The human-model disagreement list is used to start a conversation, not to produce a rate. Every disagreement is resolved into one of three outcomes. The codebook definition is ambiguous, and it gets sharpened. The model's assignment chased a surface resemblance, and it gets rejected. A pattern escaped the researcher's eye, and it gets accepted. All three outcomes are written into the codebook's log of change.

## 6. The Integrity of Quotations

The evidence of a qualitative report is the quotation, and the only legitimate source of a quotation is the transcript itself. Generative models have a documented tendency to fabricate. When Walters and Wilder (2023) measured that tendency at the level of bibliographies, they showed how easily records are produced that do not exist yet look entirely real. The counterpart of that tendency in interview data is more insidious. A model summarizing a transcript can present, in the guise of a quotation, a sentence no participant ever said but any participant plausibly might have.

The rule therefore allows no exceptions. Every quotation that enters the report is searched for in the transcript, word for word, and found. Claude Code automates this verification, since exact text search is precisely machine work. A quotation that cannot be found is not corrected and not softened. It is deleted, and a real quotation from the transcript takes its place. Changes made for anonymization are marked with square brackets and explained in the methods section.

## 7. The Reflexivity Journal

In the reflexive tradition the researcher is the instrument of the analysis, so the researcher's own position is also kept on record. AI-assisted coding adds a new layer to this journal. The analysis conversations with the model are themselves reflexivity material. What prompt was given, what frame did the model propose, why did the researcher accept or refuse it?

The journal lives in the archive next to the codebook and is fed a few lines after every analysis session. Those lines do two jobs at once. They build the audit trail of the analysis, and they show the researcher how far they have been leaning on the model's frames. A journal page on which every theme proposed by the model was accepted is an early warning that interpretive authority is quietly changing hands.

## 8. Confidentiality and Data Protection

Interview data is the most sensitive material a social scientist handles, and the qualitative coding workflow is built around that sensitivity. The basic rule is a matter of ordering. Anonymization first, model second. No fragment is shown to the model before participant names, institution names, and indirectly identifying details have been removed from the transcript. Data protection obligations, KVKK in Türkiye and the GDPR in the European context, together with the promises made in the consent form, make this ordering a legal matter as well as an ethical one.

On the Claude Code side this means working directory discipline. Raw transcripts stay in the region of the archive closed to model access, coding sessions work only on anonymized copies, and which file lives in which region can be read off the folder structure itself. The scope of consent deserves its reminder here too. If the consent form did not foresee participant data being processed with AI tools, that boundary cannot be stretched for the researcher's convenience.

## 9. Disclosure

AI-assisted coding is disclosed in the methods section, as a description of the process. Hosseini, Rasmussen, and Resnik (2023) tie the duty to disclose to the use itself, and they ask for concreteness. The reader should be able to see where the tool stood. A good disclosure sentence gives the role, the protocol, and the address of authority together. The example below is synthetic.

> In the coding process, Claude Code was used as an assistant producing an independent second coding against the codebook definitions. Disagreements were adjudicated by the first author, and all theme definitions and interpretations were produced by the authors. All quotations in the report were verified word for word against the transcripts.

Those three sentences are this booklet in miniature. The protocol transparent, the authority human, the evidence verified.

## 10. Bridge, to the Ethical Frame

The confidentiality section leaned on the consent form, and the disclosure section leaned on the principle of honesty. Both have their roots in the ethical frame built while the research was still being designed. The next booklet takes up that frame as a whole: how principle becomes daily behavior in AI-assisted research, along the line that runs from consent through data storage to disclosure, gathered in a single workflow document.

## References

Citations are in APA 7 format. DOIs verified against Crossref on 2026-06-10.

Braun, V., & Clarke, V. (2006). Using thematic analysis in psychology. *Qualitative Research in Psychology*, 3(2), 77-101. https://doi.org/10.1191/1478088706qp063oa

Braun, V., & Clarke, V. (2019). Reflecting on reflexive thematic analysis. *Qualitative Research in Sport, Exercise and Health*, 11(4), 589-597. https://doi.org/10.1080/2159676X.2019.1628806

Hosseini, M., Rasmussen, L. M., & Resnik, D. B. (2023). Using AI to write scholarly publications. *Accountability in Research*, 31(7), 715–723. https://doi.org/10.1080/08989621.2023.2168535

Morgan, D. L. (2023). Exploring the use of artificial intelligence for qualitative data analysis: The case of ChatGPT. *International Journal of Qualitative Methods*, 22, Article 16094069231211248. https://doi.org/10.1177/16094069231211248

O'Connor, C., & Joffe, H. (2020). Intercoder reliability in qualitative research: Debates and practical guidelines. *International Journal of Qualitative Methods*, 19, Article 1609406919899220. https://doi.org/10.1177/1609406919899220

Walters, W. H., & Wilder, E. I. (2023). Fabrication and errors in the bibliographic citations generated by ChatGPT. *Scientific Reports*, 13, Article 14045. https://doi.org/10.1038/s41598-023-41032-5

---

**Booklet ID.** `008-03-0001`
**Version.** `0.1.0`
**Date.** 2026-06-20
**Approximate word count.** 1754 (English body text, measured with wc)
**Verified citations.** 6
**Hallucinated citations.** 0
**Previous booklet.** [`008-02-0001`](../008-02-0001/en.md). Statistical Test Selection with AI Consultation Discipline
**Next booklet.** [`009-01-0001`](../../009-ethics-irb/009-01-0001/en.md). Ethics in AI-Assisted Research, From Principle to Behavior
