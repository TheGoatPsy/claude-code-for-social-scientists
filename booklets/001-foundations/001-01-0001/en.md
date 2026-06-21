---
title_en: "Claude Code Through a Social Scientist’s Lens"
title_tr: "Sosyal Bilimcinin Gözüyle Claude Code"
booklet_id: "001-01-0001"
category: "001-foundations"
language: "en"
version: "0.2.0"
date_published: "2026-05-19"
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
    role: "drafting, verification, citation lookup, bilingual re-authoring"
    interaction_mode: "interactive console"
ai_contribution_level: "substantial-drafting"
human_review: "complete"
human_review_date: "2026-06-21"
verified_citations_count: 13
fabricated_citations_count: 0
disclosure_standard: "COPE 2023 + WAME 2023 + ICMJE 2024 + STM 2025 + EU AI Act 2024/1689 Art. 50 + ENAI"
translation_notes: "English re-authored natively from the finalized Turkish source (tr.md v0.2.0) for this revision. This is not a literal translation. Content, arguments, section structure, and the verified citation set are preserved; phrasing has been rendered in idiomatic academic English appropriate to the register and audience of the guide."
license:
  - "CC-BY-NC-SA-4.0 (prose)"
status: "release"
---

# Claude Code Through a Social Scientist’s Lens

This booklet situates Anthropic's Claude Code within a conceptual framework for researchers, clinicians, and educators working in the social sciences. The aim is not merely to introduce the tool through its technical features. The more fundamental question is what functions Claude Code can perform within the academic production process of a social scientist, where it encounters its limits as a knowledge system, and under what conditions it may generate methodological risk.

Discussion of artificial intelligence in the social sciences tends to concentrate on speed, productivity, and automation. These are genuine concerns. They are not, however, sufficient. A social scientist's academic production is not reducible to output generation. It requires constructing a research question, verifying sources, using concepts consistently, justifying methodological decisions, maintaining ethical boundaries, and taking final scientific responsibility for the text produced.

Claude Code can provide meaningful support to a researcher at certain stages of that process. It can read files, organize notes, structure a literature search, make a reviewer-response process traceable, and strengthen the continuity of a research archive. These capabilities do not imply that the tool carries academic judgment. The tool generates academic value only within the methodological framework the researcher constructs.

The central claim of this booklet is the following. Claude Code is meaningful for the social scientist as a research assistant. That assistance acquires academic standing only when accompanied by explicit instructions, verifiable outputs, source verification, ethical boundaries, and human oversight. The relevant question, therefore, is not how powerful the tool is. The relevant question is the ethic of work within which it is used.

## 1. A Tool, or a Methodological Transformation?

To treat an AI assistant as merely a faster search engine is to misread the social scientist's actual working needs. A researcher rarely needs a quick answer to a single question. The more fundamental need is to trace one research question consistently across many sources, to document an analysis protocol, to relate a revision process to specific reviewer comments, and to preserve academic context that would otherwise fragment over time.

In this respect, Claude Code is distinct from an ordinary chat interface. It offers an agent-based working environment: it can read and write files, execute operations via the command line, work within a specific project directory, and decompose multi-step tasks into constituent parts. That distinction may appear technical at first. For the social scientist, however, it carries methodological consequences. The tool is no longer merely a text-generation system. When structured within appropriate boundaries, it becomes a research assistant capable of engaging with the file, note, source, and revision layers of a research process.

At the center of that transformation is continuity. Academic work in the social sciences typically unfolds over extended time. Field notes, clinical observations, interview transcripts, course syllabi, reading notes, draft manuscripts, and peer review evaluations are not confined to individual sessions. They are research traces that must be connected, preserved, and retrieved when needed. The potential value of Claude Code lies in its ability to relate those traces to a more durable working archive rather than leaving them in a transient chat history.

Continuity does not, however, produce scientific quality on its own. A tool's ability to access many files does not mean it can exercise correct conceptual judgment over those files. The stochastic parrot argument put forward by Bender et al. (2021) is relevant here. Large language models can reproduce statistical patterns fluently without anything that constitutes genuine understanding. In the social sciences, this risk may manifest as outputs that appear persuasive but are unreliable in terms of sources, concepts, or methods.

The value of Claude Code is therefore bounded by the methodological framework the researcher establishes. Without explicit task definitions, source verification, ethical constraints, human oversight, and a document-based working discipline, the tool remains nothing more than a productive text system. When that framework is in place, it can render the research process more traceable, more organized, and more auditable.

## 2. Technical Identity — What the Social Scientist Needs to Know

Claude Code is an agent-based tool built on Anthropic's large language models. It operates via the command line, can read and write files, execute code, and — within the scope of permissions explicitly granted by the user — carry out multi-step tasks within a designated working directory.

Several methodological consequences of that technical identity bear examination.

The first is that Claude Code is not a chat box in a browser tab. Browser-based chat sessions are typically transient: when the session closes, context is largely lost. Claude Code operates inside a project folder. It can read a note written in a previous session, create a new file, propose a bounded change to an existing document, and track relationships among different files. This characteristic moves it closer to a tool that works alongside a research folder than to a temporary conversational space.

The second is that Claude Code's behavior can be configured through persistent instruction files. CLAUDE.md is important in this regard. It is a plain-text structure that allows a researcher to carry methodological preferences, citation conventions, language standards, ethical constraints, and project-level working habits across sessions. The researcher does not need to restate these ground rules at the start of every session. CLAUDE.md is addressed in detail in booklet 001-01-0004.

The third is that Claude Code operates under an agent-based logic. The term agent here denotes more than a system that answers questions. An agent can decompose a high-level goal into subtasks, sequence those subtasks, invoke other tools when required, and integrate intermediate outputs. This architecture is well suited to the social scientist's mode of academic work. Tasks such as literature screening, methodological coding, data organization, preparing reviewer responses, and source verification are not one-shot responses; they are sequences of related operations that must be coordinated.

A functional parallel from clinical psychology is instructive here. The biopsychosocial model (Engel, 1977) does not reduce an individual's experience to a single symptom level. It treats the individual as a system in which biological, psychological, and social processes interact simultaneously. The agent logic of Claude Code can process an academic task not as a single answer but as a sequence of interconnected subtasks. This parallel carries no claim of structural identity; it serves only to illustrate what multi-layered processing looks like at the level of a tool.

One final point must not be overlooked: Claude Code is a general-purpose tool. Knowledge of social science methodology, clinical psychology, Turkish academic literature, COPE publication ethics, IRB procedures, the Personal Data Protection Law, GDPR, DergiPark, or ULAKBIM TR Dizin is not reliably embedded in the tool by default. These domains are brought to the tool through the researcher's guidance, through file structure, and through verification discipline. As Ziems et al. (2024) argue in the context of computational social science, the value of large language models in the social sciences is determined not by the model itself but by how it is directed, which data and tools it is connected to, and within which oversight mechanisms it is used.

For the social scientist, then, Claude Code can be defined as follows. It is a research assistant that operates within a designated project directory under explicit permissions, can execute multi-step tasks, deepens only as far as the researcher's framework goes, and does not spontaneously establish methodological constraints the researcher has not set.

## 3. For Whom It Is Useful, and Where It Falls Short

The conditions under which Claude Code generates value and the conditions under which it reaches its limits must be distinguished. That distinction is a prerequisite for responsible use in academic production.

The tool gains real value in tasks that are high-volume, repetitive, structurable, and verifiable. Doctoral students managing several research projects simultaneously, researchers who must organize large Zotero libraries, qualitative researchers comparing many interview transcripts against a codebook, authors preparing traceable responses to reviewer comments, and faculty members continuously updating course materials are all profiles in this category.

What these tasks share is not only that they require creative thinking. They also require organization, classification, monitoring, comparison, and verification. Claude Code can reduce the researcher's cognitive load at these stages. A randomized controlled trial by Noy and Zhang (2023) on professional writing tasks showed that AI assistance can produce meaningful gains in time and output quality for certain tasks. From this finding, analogous productivity improvements can be expected in academic tasks with similar structural properties. This is a methodological inference that warrants careful testing; it is not direct evidence.

By contrast, Claude Code cannot substitute for forms of knowledge that are embodied, relational, and contextual. There is no computational equivalent of being present in the field during ethnographic research, of the therapeutic relationship in a clinical case study, of the meaning carried by silence in a counseling session, or of bodily tone in an interview. The tool can organize field notes, assist with classifying anonymized clinical material, and review a conceptual framework. It cannot replace the researcher's observational sensitivity in the field or the clinician's relational judgment.

This limit is not technical; it is epistemological. Certain kinds of knowledge acquire meaning not as structured data but within lived context, relationship, and situational judgment. Delegating such knowledge to an AI tool is not merely incomplete; in some cases it is ethically problematic. The discussion by Hosseini et al. (2023) of AI use in scholarly writing makes clear that the tool's value depends on the type of task and the quality of human oversight.

The right question, then, is not "should Claude Code be used?" The more precise question is: for which task, within which limits, under which oversight, and with what disclosure responsibility?

## 4. A First Contact Scenario

Consider a doctoral student preparing a systematic review of the relationship between social media use among adolescents and generalized anxiety disorder. Approximately two hundred articles collected from PubMed, Semantic Scholar, and PsycINFO are held in a Zotero library. The project began several months ago; the literature has since reached a volume that is increasingly difficult to manage.

The questions the researcher must answer are multiplying. Which studies used a longitudinal design? Which applied a specific theoretical model? Which samples came from Türkiye, Greece, Arabic-speaking countries, or other regional contexts? Which studies were published before the DSM-5-TR update? Which articles lacked a control group? Which measurement instruments recur across studies?

The conventional approach requires the researcher to open each article individually, scan the title, abstract, and methods section, construct a table, and then reclassify on the basis of that table. The process demands rigor, but it is time-consuming and particularly prone to error when dealing with large source pools.

Claude Code can be used here not to interpret the literature on the researcher's behalf but to enable a structured initial screening pass over the literature. It can read Zotero metadata, extract the locations of specific concepts in full texts, and generate a preliminary table for variables such as publication year, sample type, methodological design, and measurement instruments. These outputs are then reviewed manually by the researcher.

The methodological boundary in this scenario must be clear. The tool does not take on the scientific interpretation of articles. It reports where specific information appears in the full text. Summarization, critical evaluation, and inclusion and exclusion decisions remain with the researcher. Citations are not invented by the tool; source information is drawn from Zotero, DOI, PubMed, or other verifiable indices, which substantially reduces the risk of fabricated references.

Evidence reported by Else (2023) shows that AI-generated abstracts can mislead even experienced readers. For this reason, no summary or inference produced by Claude Code should be transferred directly into an academic text. Every output must be checked against the source material, reviewed for methodological soundness, and subjected to human judgment.

This example makes explicit the three conditions Claude Code needs to generate value in the social sciences.

The task must be structured.

The output must be verifiable.

The final decision must remain with the researcher.

When any one of these conditions is absent, risk increases. If the researcher instructs the tool to "summarize the two hundred articles and write the review," the tool may produce text that is formally fluent but unreliable in content. As Hicks et al. (2024) argue, generative language models can produce outputs that are epistemically weak in their relationship to truth while appearing persuasive. The implication is consistent: what is decisive is not the tool's presence but the methodological protocol within which it is used.

## 5. The Turkish and Greek Academic Environment

International guides to AI use in the social sciences typically presuppose an Anglo-American academic infrastructure. Yet the conditions of access, indexing, and institutional visibility that researchers face in Türkiye, Greece, and the broader Mediterranean are different. These differences are not merely technical details. They directly shape the scope of literature searches, source selection, and academic visibility standards.

In Türkiye, DergiPark is the central open-access platform on which a large number of academic journals are published. Through Crossref integration, articles in journals that generate DOIs can be linked to international reference systems. Being published on DergiPark, however, is not the same as being indexed in ULAKBIM TR Dizin. ULAKBIM TR Dizin carries distinct importance for academic promotion, doctoral evaluation, and national visibility in Türkiye. International tools do not surface this distinction automatically.

In Greece, HEAL-Link provides access to international journals through a joint subscription system across university libraries. Full-text access, however, frequently depends on local library configuration, proxy settings, and campus-based access conditions. For a researcher working at Democritus University in Komotini or at an Athens-based institution, these details determine the real boundaries of any literature search.

Claude Code does not resolve these infrastructural barriers on its own. If the researcher correctly specifies available access pathways, however, that configuration can help the tool work more reliably in literature search and source organization processes. For this reason, academic access is treated in this guide not as a secondary matter but as a methodological starting condition. A literature map cannot be constructed without first knowing which sources are accessible.

## 6. The Ethical Layer — First-Order Principles

In AI-assisted academic production, ethics is not an addendum placed at the end of a manuscript. It is the methodological framework that must be established at the outset. That framework takes concrete form in at least four domains: citation integrity, confidentiality, authorship and disclosure, and social bias.

The first imperative is to protect citation integrity. Asking Claude Code to "suggest a source on this topic" always carries the risk of fabricated references. For this reason, no source suggested by the tool should enter the reference list without independent verification in a database. Crossref, PubMed, Semantic Scholar, DergiPark, and ULAKBIM TR Dizin can all be used for this verification. An unverified source must not appear in an academic text.

The second is that confidentiality boundaries are not negotiable. Clinical data, non-anonymized interview transcripts, field notes containing identifying information, or any human participant data not explicitly authorized by an ethics board must not be provided to the tool. The data minimization principle emphasized by van Dis et al. (2023) in their research priorities is a foundational criterion here. The practical implication for the social scientist is clear: personal, clinical, or sensitive data may be processed only within an ethics board approval, an anonymization protocol, and a data security framework.

The third concerns authorship and disclosure, which raise a distinct set of questions. The emerging consensus across COPE, ICMJE, and WAME is that artificial intelligence cannot be an author; it cannot assume accountability, declare conflicts of interest, or respond to post-publication critique in a responsible way. At the same time, AI assistance must not be concealed. At which stages of the text it was used, which model or tool was employed, and how human oversight was conducted must all be stated explicitly.

The fourth is that the social biases of language models must be taken into account. The risk taxonomy developed by Weidinger et al. (2022) maps misinformation generation, disinformation propagation, scale effects, and cultural bias in detail. For the social scientist, the most operationally relevant risks fall in these categories. In non-English languages such as Turkish, these risks can manifest differently; multilingual models are not trained on balanced or equally curated corpora across languages (Xu et al., 2025). Human review of Turkish academic outputs therefore requires particular care with respect to concepts, sources, and cultural context.

Finally, the dimension of structural inequality must not be overlooked. As Milano et al. (2023) argue, large language models hold the potential to deepen resource inequalities in higher education as readily as they might reduce them. The bilingual, open, and verifiable structure of this guide is a limited but concrete academic response to that risk.

## 7. A Practical Starting Protocol

Before beginning work with Claude Code, methodological preparation should precede technical setup. The researcher should first clarify for which academic task the tool will be used. Literature review, systematic review, manuscript revision, course design, ethics board application, and reviewer response letter each require different configurations. Applying the tool in the same way to every task weakens the quality of its output.

The second step is to establish a persistent working archive. This archive does not need to be elaborate at the outset. Three basic folders are sufficient for the start: current research, current writing, and current reading list. Markdown files, frontmatter, content maps, and source passports can be added to this structure progressively. The aim is to avoid leaving academic context in transient chat windows.

The third step is to establish disclosure as a habit from the very beginning. Every text produced or edited with AI assistance should carry a brief record specifying the nature of that assistance. This record may appear minor at first. When the text eventually reaches a reviewer, editor, supervisor, or student, however, it becomes the primary document of academic transparency.

The purpose of the starting protocol is not to constrain the tool but to render it academically usable. Claude Code becomes a reliable working instrument for the researcher only when accompanied by task definition, source verification, data security, and human oversight.

## 8. Conclusion and Next Step

Claude Code can be a capable assistant for the social scientist at specific stages of the research process. That capability, however, carries academic value only within an appropriate methodological framework. The tool can organize sources, connect notes, work across files, and make multi-step tasks traceable. Conceptual judgment, ethical responsibility, source verification, and the final scientific decision remain with the researcher.

This booklet positions Claude Code neither as a marvel nor as an ordinary chat interface. It offers a more measured proposal. Claude Code can become a meaningful research assistant for the social scientist only in conjunction with explicit instructions, verifiable outputs, document-based workflows, human oversight, and disclosure responsibility.

The next booklet deepens this framework at the interface level. It examines the difference between a chat window and an agent-based working tool in terms of file system operations, tool calls, subtask execution, and traceability.

Booklet 001-01-0002, The Agentic Shift: From Chat Window to Working Partner, continues from this point.

---

## References

Citations are in APA 7 format. Each DOI was independently verified against Crossref on 2026-06-21.

Bender, E. M., Gebru, T., McMillan-Major, A., & Shmitchell, S. (2021). On the dangers of stochastic parrots: Can language models be too big? In *Proceedings of the 2021 ACM Conference on Fairness, Accountability, and Transparency* (FAccT '21, pp. 610–623). Association for Computing Machinery. https://doi.org/10.1145/3442188.3445922

Else, H. (2023). Abstracts written by ChatGPT fool scientists. *Nature*, *613*(7944), 423. https://doi.org/10.1038/d41586-023-00056-7

Engel, G. L. (1977). The need for a new medical model: A challenge for biomedicine. *Science*, *196*(4286), 129–136. https://doi.org/10.1126/science.847460

Frankfurt, H. G. (2005). *On bullshit*. Princeton University Press. ISBN 978-0-691-12294-6

Hicks, M. T., Humphries, J., & Slater, J. (2024). ChatGPT is bullshit. *Ethics and Information Technology*, *26*(2), Article 38. https://doi.org/10.1007/s10676-024-09775-5

Hosseini, M., Rasmussen, L. M., & Resnik, D. B. (2023). Using AI to write scholarly publications. *Accountability in Research*, *31*(7), 715–723. https://doi.org/10.1080/08989621.2023.2168535

Milano, S., McGrane, J. A., & Leonelli, S. (2023). Large language models challenge the future of higher education. *Nature Machine Intelligence*, *5*(4), 333–334. https://doi.org/10.1038/s42256-023-00644-2

Noy, S., & Zhang, W. (2023). Experimental evidence on the productivity effects of generative artificial intelligence. *Science*, *381*(6654), 187–192. https://doi.org/10.1126/science.adh2586

Stokel-Walker, C. (2023). ChatGPT listed as author on research papers: Many scientists disapprove. *Nature*, *613*(7945), 620–621. https://doi.org/10.1038/d41586-023-00107-z

van Dis, E. A. M., Bollen, J., Zuidema, W., van Rooij, R., & Bockting, C. L. (2023). ChatGPT: Five priorities for research. *Nature*, *614*(7947), 224–226. https://doi.org/10.1038/d41586-023-00288-7

Weidinger, L., Uesato, J., Rauh, M., Griffin, C., Huang, P.-S., Mellor, J., Glaese, A., Cheng, M., Balle, B., Kasirzadeh, A., Biles, C., Brown, S., Kenton, Z., Hawkins, W., Stepleton, T., Birhane, A., Hendricks, L. A., Rimell, L., Isaac, W., & Gabriel, I. (2022). Taxonomy of risks posed by language models. In *2022 ACM Conference on Fairness, Accountability, and Transparency* (pp. 214–229). Association for Computing Machinery. https://doi.org/10.1145/3531146.3533088

Xu, Y., Hu, L., Zhao, J., Qiu, Z., Xu, K., Ye, Y., & Gu, H. (2025). A survey on multilingual large language models: Corpora, alignment, and bias. *Frontiers of Computer Science*, *19*(11), Article 1911362. https://doi.org/10.1007/s11704-024-40579-4

Ziems, C., Held, W., Shaikh, O., Chen, J., Zhang, Z., & Yang, D. (2024). Can large language models transform computational social science? *Computational Linguistics*, *50*(1), 237–291. https://doi.org/10.1162/coli_a_00502

---

**Booklet identifier.** `001-01-0001`
**Version.** `0.2.0`
**Date.** 2026-06-21
**License.** This booklet is licensed under CC BY-NC-SA 4.0. https://creativecommons.org/licenses/by-nc-sa/4.0/
**Approximate word count.** 3188 (English body text, measured with wc)
**Verified citations.** 13
**Fabricated citations.** 0
**Previous booklet.** None (first booklet)
**Next booklet.** [`001-01-0002`](../001-01-0002/en.md). The Agentic Shift: From Chat Window to Working Partner
