---
title_en: "What is Claude Code? A Social Scientist's Perspective"
title_tr: "Claude Code Nedir? Sosyal Bilimci Bakışıyla"
booklet_id: "001-01-0001"
category: "001-foundations"
language: "en"
version: "0.1.0"
date_published: "2026-05-19"
date_last_revised: "2026-06-20"
authors:
  - name: "Onour Impram"
    orcid: "0000-0003-1076-3928"
    role: "author, principal reviewer"
ai_assisted: true
ai_tools:
  - name: "Claude Code"
    vendor: "Anthropic"
    model_alias: "claude-opus-4-7"
    model_dated: null  # no dated identifier published by Anthropic for Opus 4.7 as of 2026-05-19
    role: "drafting, verification, citation lookup, bilingual re-authoring"
    interaction_mode: "interactive console"
ai_contribution_level: "substantial-drafting"
human_review: "complete"
human_review_date: "2026-06-20"
verified_citations_count: 13
fabricated_citations_count: 0
disclosure_standard: "COPE 2023 + WAME 2023 + ICMJE 2024 + STM 2025 + EU AI Act 2024/1689 Art. 50 + ENAI"
translation_notes: "Re-authored from the Turkish version (tr.md) against the same outline and the same verified citation set. Examples and academic infrastructure references domesticated for an international audience while preserving the Turkish and Greek specificity where relevant."
license:
  - "CC-BY-NC-SA-4.0 (prose)"
status: "release"
---

# What is Claude Code? A Social Scientist's Perspective

This is the first booklet of the guide. It offers a conceptual frame for what Anthropic's Claude Code means for a working researcher, educator, or clinician in the social sciences. The framing is methodological rather than purely technical. The goal is to clarify where Claude Code adds real value to academic production, where it carries enduring risk, and why the answer to that question in 2026 is likely to shape the practice of the next decade.

## 1. A Tool, or a Transformation?

To treat an artificial intelligence assistant as nothing more than a faster search engine is the same category of mistake as treating clinical case formulation as a list of diagnoses. Case formulation, unlike diagnosis, does not ask what the symptom is. It asks why this symptom appears in this patient at this time. To reduce Claude Code to a chat window or a search box is to miss what the social scientist actually needs. The real need is rarely a paragraph written word for word. The real need is the consistent tracing of one research question across ten sources, the documented record of an analysis protocol from beginning to end, the maintenance of a manuscript revision as a traceability matrix against eleven reviewer comments.

Claude Code lives beyond the chat window. It is an agent interface: it can read and write files, run commands in the terminal, remember what it has done within a session, and delegate tasks to other models or tools. This difference matters methodologically. For the social scientist, it means the tool shifts from being a notebook to being a laboratory assistant. What is decisive here is continuity. The years of field notes, hospital observations, interview transcripts, journal readings, course syllabi, peer review responses. All of these can now connect into a single research ecosystem.

That continuity does not produce intellectual quality on its own. Bender et al. (2021) identify, with precision that should make any careful reader uncomfortable, the risk that a language model reproduces statistical patterns without anything that resembles understanding, the stochastic parrot problem. The conclusion this guide draws from that risk is the guide's own: the social scientist must build an explicit methodological framework that governs how the tool is used. Without that framework, the tool remains a statistical mirror. With it, the tool becomes an intellectual partner. How that framework is constructed is the subject of the rest of this guide.

## 2. Technical Identity. Just What the Social Scientist Needs

One sentence captures the technical identity of Claude Code. It is a command-line application, built on Anthropic's large language models, capable of reading and writing files, running code, fetching data over the network, and decomposing higher-level goals into subtasks executed in a modular agent system. All of this happens within the working directory it is launched in and its subfolders, under explicit permission granted at the start of each session.

The methodological implications for the social scientist are worth drawing out.

The most immediate is that this is not a chat box in a browser tab. A browser session with ChatGPT or Claude.ai ends when the tab is closed. Claude Code, launched inside your project folder, operates on the files in that folder: it can read a note written in a previous session, append to it, and link it to another file. That difference is the difference between a notebook and a vault. One additional mechanism makes that continuity persist across sessions: CLAUDE.md, a plain-text file in your project that carries standing instructions to the tool, including your methodological rules, your citation discipline, and your domain preferences. This booklet introduces the concept. Booklet 001-01-0004 covers the full setup.

The word agent, used deliberately here, carries a specific meaning. An agent, in the technical sense used here, is a structure that takes a high-level goal, decomposes it into subtasks, executes those subtasks in sequence, calls on other tools when needed, gathers results, and reports back. The working definition this guide uses draws a useful parallel with the biopsychosocial model of case formulation (Engel, 1977), with the important qualification that this is an analogy, not an identity. A patient in clinical practice is approached as a system operating simultaneously at biological, psychological, and social levels, rather than as a symptom list to be checked off. The agent model treats a complex task in a structurally similar way: as a sequence of interdependent subtasks, each building on the last.

A less visible but equally consequential point is that this is a general-purpose model. The social sciences have no privileged position in its training. Turkish academic literature, clinical psychology methodology, IRB protocols, COPE publication ethics: none of these domains are built in. They depend on your direction. Research on the potential of large language models to transform computational social science has shown that the quality of that direction directly determines the quality of the output (Ziems et al., 2024).

In summary, for the social scientist, Claude Code is a research assistant that operates within your designated project folder under explicit permission, can execute multi-step tasks, deepens as your framework deepens, and provides no framework you did not first provide.

## 3. Who It Is For, Who It Is Not For

The position this booklet takes openly is the following: Claude Code is not for everyone.

The profiles where the tool genuinely adds value share a structure. Consider the doctoral student running several research projects in parallel: a Zotero library approaching three hundred items, overlapping submission deadlines, two ongoing data collections. Or the research assistant who must apply a codebook consistently across a hundred interview transcripts before the team meeting on Thursday. A postdoctoral researcher answering eleven reviewer comments on a manuscript that has already gone through one round of rejection faces the same pressure, as does a faculty member who needs to check twenty student theses for conceptual coherence within a single week. The clinical investigator assembling a fifty-source literature summary before an IRB deadline is no different. The common factor is high-volume, repeated, structured, verifiable work. Noy and Zhang (2023) demonstrate, in a randomized controlled trial on professional writing tasks specifically, that AI assistance produces meaningful gains in both time and output quality for work of this kind. This guide's inference is that those gains extend to other high-volume structured academic tasks such as coding transcripts, preparing IRB applications, and screening systematic reviews. That inference is the guide's own and goes beyond what that single study establishes.

The profiles where the tool loses value should be stated with equal directness. For a researcher conducting a deeply ethnographic study on a single case, Claude Code cannot substitute for observational sensitivity in the field. An AI-assisted tool can help organize field notes, but it cannot stand in for the lived experience of participant observation. The same holds for a therapist working with a clinical case study: the tool cannot replace the concrete moment of the therapeutic encounter. This boundary is epistemological. What the tool cannot grasp is not merely a matter of how it is configured, but concerns what kind of knowing it is structurally capable of: the situated, relational, irreducibly particular knowing that anchors clinical and ethnographic work.

Saying clearly who it is not for makes the case for who it is for more credible. The literature on the ethical limits of AI in scholarly writing emphasizes that the value of the tool depends on the structure of the task (Hosseini et al., 2023).

The next booklet (001-01-0002) describes the practical mechanics of the shift from chat window to working partner. The rest of this booklet covers a first contact scenario, regional specificity, the ethical layer, and a starting protocol.

## 4. A First Contact Scenario

A doctoral student is preparing a systematic review on the relationship between social media use among adolescents and generalized anxiety disorder. The student has assembled a Zotero library of two hundred PDF articles drawn from PubMed, Semantic Scholar, and PsycINFO. The work began three months ago. Now the student faces specific questions. Which articles used the Selvi and Lewinsohn model? Which were longitudinal in design? Which used Turkish or Arabic samples? Which were published before the DSM-5-TR update? Which lacked a control group?

The conventional approach: open the two hundred PDFs one by one, scan title, abstract, and methods, fill in an Excel table, then query the table. For a committed doctoral student, this is two to three weeks of intensive work.

The Claude Code approach, on day one, reads and processes the Zotero library metadata, extracts mentions of specific concepts from the full text of each article, and aggregates those extracts into a queryable structure. All of this happens in a single session. The output is a table. The doctoral student performs manual verification on the table.

Several points in this scenario warrant attention. The tool produces no summary of any article. It queries the full text and reports where a concept appears. The summarizing step belongs to the doctoral student. In the workflow this guide sets up, the tool does not generate citations either: citations are drawn from the original source through Zotero, removing the risk of fabricated references entirely. This is a prescriptive rule of this workflow, not a property of the tool itself, since the tool is capable of producing citations, but this setup instructs it not to. And the tool does not replace manual verification. Evidence that AI-generated abstracts can deceive experienced readers (Else, 2023) does not weaken the requirement for manual verification. It strengthens it.

This scenario holds the basic formula for usefulness in the social sciences: a structured task, a verifiable output, human verification in the last step.

The real risk arises when this formula is violated. If the doctoral student instead instructs the tool to "summarize the two hundred articles and write a systematic review," the output will be syntactically polished and substantively unreliable. A careful philosophical reading of generative language models has demonstrated that their epistemic character can extend, at the limit, into what one might describe as bullshit production (Hicks et al., 2024), a reading that finds its conceptual scaffolding in Frankfurt's (2005) earlier treatment of bullshit as a philosophical category. The implication is direct: the tool itself is secondary. What determines the outcome is the methodological framework the researcher brings.

## 5. The Turkish and Greek Academic Environment

International academic literature on AI tools tends to overlook the institutional realities of Türkiye, Greece, and the broader Mediterranean. One of the positions this guide maintains throughout is to fill that gap explicitly.

DergiPark is the institutional platform on which hundreds of Turkish academic journals are published. It provides free open access. It is Crossref-integrated, producing DOIs. Claude Code can access an article published on DergiPark through its DOI. Filtering specifically for articles indexed in ULAKBIM TR Dizin requires additional configuration.

ULAKBIM TR Dizin is the list of quality-controlled Turkish journals. It is a critical reference for doctoral evaluation and academic promotion procedures in Türkiye, and an important indicator of a paper's national visibility that international tools do not surface automatically.

In Greece, HEAL-Link provides access to international journals through a joint subscription across Greek university libraries. A researcher at Democritus University in Komotini can access a journal article through HEAL-Link, though EZproxy configurations are not uniform across campuses. A researcher can run a PubMed search through the Claude Code PubMed MCP, but full-text access requires the local library proxy to be configured correctly.

These infrastructure details may look technical at first glance. Their impact on academic production is methodological. A researcher cannot map a literature without knowing which sources are accessible. The AI tool does not solve these obstacles automatically. A coherent configuration guide, however, can dramatically reduce the time the researcher spends on infrastructure. Category 002 of this guide (Academic Access) is dedicated entirely to this topic.

## 6. The Ethical Layer. First-Tier Warnings

In AI-assisted academic production, ethics belongs at the beginning, not at the end of the manuscript. What follows identifies the first-tier warnings that structure the rest of the guide.

Citation integrity comes first. Asking Claude Code to "suggest a source on topic X" always carries the risk of a fabricated citation. The operational rule of this guide is clear: every citation suggested by the tool must be verified against an independent index (Crossref, PubMed, Semantic Scholar, ULAKBIM TR Dizin, DergiPark) before it enters the reference list.

Confidentiality is equally non-negotiable. Clinical data, interview transcripts, and non-anonymized field notes must under no circumstances be shared with the tool. The international consensus on five priorities for AI in research (van Dis et al., 2023) counts data minimization among its priorities. The rule of this guide is that clinical data is not shared with the tool unless anonymized in a way the institutional ethics committee has approved.

Authorship and disclosure raise a separate set of questions. A consensus position has formed among COPE, ICMJE, and WAME: artificial intelligence cannot be an author. The debate over listing AI systems on papers is addressed in those bodies' published guidance, though the precise norms continue to evolve as the field moves. What is settled is that AI assistance must be explicitly disclosed in the methods or acknowledgements (Stokel-Walker, 2023). The rule of this guide is that every booklet carries a disclosure block in its frontmatter.

The social reflection of language models deserves attention as well. The risks of large language models have been mapped taxonomically (Weidinger et al., 2022). For the social scientist, the most relevant risk categories are misinformation generation, disinformation propagation, scale effects, and cultural bias. Bias in Turkish-language content can manifest differently, and in some respects more severely, than bias in English-language content, because multilingual models are trained on corpora that are neither balanced nor equally curated across languages (Xu et al., 2025). For this reason, manual review of Turkish output warrants more care than review of English output.

Structural inequality rounds out the picture. The transformation that large language models bring to higher education has the potential to deepen rather than narrow resource inequalities, a pattern documented in the academic literature (Milano et al., 2023). The work of this guide is not to accept that inequality. It is to act against it explicitly.

## 7. A Practical Starting Protocol

The direction of the first week is set by methodological choices, not technical ones.

Task type should be clarified first. For which kind of academic production will you use the tool? Literature review, systematic review, manuscript revision, course design, IRB application, reviewer response letter: each requires a different configuration. Using the tool as a general-purpose "everything assistant" produces a weak start.

Alongside that, building a vault matters: a persistent folder structure where collected academic notes live. Markdown files, frontmatter, file tree, maps of content. Category 004 of this guide is dedicated entirely to this topic. The vault does not have to be complete in the first week. Three folders are enough: current research, current writing, current reading list.

Disclosure is the habit easiest to start immediately. From the first week onward, any text written with the assistance of the tool must carry a footer that records the level of assistance. This is not merely a formality. The structure of academic production is such that when work eventually reaches a reviewer, an editor, or a student, the disclosure document must already exist.

## 8. Conclusion and Next Step

Claude Code closes the gap between a notebook and a laboratory assistant for the social science researcher. The value of the tool is proportional to the methodological framework brought by the user: one that bans fabricated citations, protects clinical data, sets disclosure at the start, and clarifies task type.

The next booklet describes the practical mechanics of the shift from chat window to working partner: which commands, which permissions, which session structure, which failure modes. Booklet 001-01-0002 (The Agentic Shift) continues from this point.

The remainder of the booklet sequence moves from this frame into increasingly specific territory: memory architecture, citation discipline, regional infrastructure, ethics, and revision practice.

---

## References

Citations are in APA 7 format. Each DOI was independently verified against Crossref on 2026-05-19. The Xu et al. (2025) DOI was verified on 2026-06-04.

Bender, E. M., Gebru, T., McMillan-Major, A., & Shmitchell, S. (2021). On the dangers of stochastic parrots: Can language models be too big? In *Proceedings of the 2021 ACM Conference on Fairness, Accountability, and Transparency (FAccT '21)* (pp. 610-623). Association for Computing Machinery. https://doi.org/10.1145/3442188.3445922

Else, H. (2023). Abstracts written by ChatGPT fool scientists. *Nature*, 613(7944), 423. https://doi.org/10.1038/d41586-023-00056-7

Engel, G. L. (1977). The need for a new medical model: A challenge for biomedicine. *Science*, 196(4286), 129-136. https://doi.org/10.1126/science.847460

Frankfurt, H. G. (2005). *On bullshit*. Princeton University Press. ISBN 978-0-691-12294-6

Hicks, M. T., Humphries, J., & Slater, J. (2024). ChatGPT is bullshit. *Ethics and Information Technology*, 26(2), Article 38. https://doi.org/10.1007/s10676-024-09775-5

Hosseini, M., Rasmussen, L. M., & Resnik, D. B. (2023). Using AI to write scholarly publications. *Accountability in Research*, 31(7), 715–723. https://doi.org/10.1080/08989621.2023.2168535

Milano, S., McGrane, J. A., & Leonelli, S. (2023). Large language models challenge the future of higher education. *Nature Machine Intelligence*, 5(4), 333-334. https://doi.org/10.1038/s42256-023-00644-2

Noy, S., & Zhang, W. (2023). Experimental evidence on the productivity effects of generative artificial intelligence. *Science*, 381(6654), 187-192. https://doi.org/10.1126/science.adh2586

Stokel-Walker, C. (2023). ChatGPT listed as author on research papers: many scientists disapprove. *Nature*, 613(7945), 620-621. https://doi.org/10.1038/d41586-023-00107-z

van Dis, E. A. M., Bollen, J., Zuidema, W., van Rooij, R., & Bockting, C. L. (2023). ChatGPT: Five priorities for research. *Nature*, 614(7947), 224-226. https://doi.org/10.1038/d41586-023-00288-7

Weidinger, L., Uesato, J., Rauh, M., Griffin, C., Huang, P.-S., Mellor, J., Glaese, A., Cheng, M., Balle, B., Kasirzadeh, A., Biles, C., Brown, S., Kenton, Z., Hawkins, W., Stepleton, T., Birhane, A., Hendricks, L. A., Rimell, L., Isaac, W., ... Gabriel, I. (2022). Taxonomy of risks posed by language models. In *2022 ACM Conference on Fairness, Accountability, and Transparency* (pp. 214-229). Association for Computing Machinery. https://doi.org/10.1145/3531146.3533088

Xu, Y., Hu, L., Zhao, J., Qiu, Z., Xu, K., Ye, Y., & Gu, H. (2025). A survey on multilingual large language models: Corpora, alignment, and bias. *Frontiers of Computer Science*, 19(11), Article 1911362. https://doi.org/10.1007/s11704-024-40579-4

Ziems, C., Held, W., Shaikh, O., Chen, J., Zhang, Z., & Yang, D. (2024). Can large language models transform computational social science? *Computational Linguistics*, 50(1), 237-291. https://doi.org/10.1162/coli_a_00502

---

**Booklet identifier.** `001-01-0001`
**Version.** `0.1.0`
**Date.** 2026-06-20
**Approximate word count.** 2509 (English body text, measured with wc)
**Verified citations.** 13
**Fabricated citations.** 0
**Previous booklet.** None (first booklet)
**Next booklet.** [`001-01-0002`](../001-01-0002/en.md). The Agentic Shift: From Chat Window to Working Partner
