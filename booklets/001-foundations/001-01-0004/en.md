---
title_en: "CLAUDE.md and the Discipline of Standing Instructions"
title_tr: "CLAUDE.md ve Kalıcı Talimat Disiplini"
booklet_id: "001-01-0004"
category: "001-foundations"
language: "en"
version: "0.2.0"
date_published: "2026-05-29"
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
    model_dated: null  # no dated identifier published by Anthropic for Opus 4.8 as of 2026-05-29
    role: "drafting, verification, citation lookup, bilingual authoring"
    interaction_mode: "interactive console"
ai_contribution_level: "full-draft"
human_review: "complete"
human_review_date: "2026-06-21"
verified_citations_count: 9
fabricated_citations_count: 0
disclosure_standard: "COPE 2023 + WAME 2023 + ICMJE 2024 + STM 2025 + EU AI Act 2024/1689 Art. 50 + ENAI"
translation_notes: "The English body was re-authored from the finalized Turkish source (tr.md v0.2.0) for this revision, not translated literally. Content, structure, arguments, and citation set are identical to the Turkish; the prose is native academic English adapted for an international readership."
license:
  - "CC-BY-NC-SA-4.0 (prose)"
status: "release"
---

# CLAUDE.md and the Discipline of Standing Instructions

This booklet examines why standing instructions are not merely a technical convenience when working with Claude Code, but one of the methodological building blocks of AI-assisted academic production. Earlier booklets in this guide covered what Claude Code is, how it differs from a chat window, and how to verify a fresh installation. This booklet turns to the first lasting problem the researcher encounters after setup.

How do you tell the tool what it needs to know at the start of every session?

The practical answer is the `CLAUDE.md` file. But `CLAUDE.md` should not be seen only as a configuration file. For the social scientist, it is a written working standard — the place where style preferences, citation discipline, ethical limits, data-security rules, language conventions, and project-level methodological expectations are made explicit.

The central claim of this booklet is this: `CLAUDE.md` is an instruction infrastructure that maintains behavioral continuity across AI-assisted research, documents the researcher's methodological preferences, and reduces drift between sessions. It is not, however, a mechanism that guarantees correctness. It shapes behavior; it does not replace scientific judgment or human oversight.

## 1. Why an Instruction Is a Methodological Instrument

One of the most persistent problems facing a researcher who works with AI tools is discontinuity. Every session — particularly in ordinary chat interfaces — functions largely as a fresh start. The tool does not reliably carry forward which citation standard was required in the last manuscript, which types of data must never be shared, which linguistic sensitivities must be preserved in Turkish-language text, or which conceptual framework the researcher has adopted.

For academic production, this is a serious problem. Research is not a collection of isolated responses; it requires that the same methodological principles, the same source-verification habits, the same ethical limits, and the same language standards be maintained over time. When those standards must be rebuilt verbally at the beginning of every session, the process becomes fragile. The researcher must re-explain the same frame each time — a cognitive burden that also weakens the consistency of outputs.

`CLAUDE.md` offers a durable answer to this problem. The tool reads this file at the start of each session and loads the project context and the researcher's core instructions. According to Anthropic's documentation, this content is added to the conversation as project context, not as a system prompt (Anthropic, 2025). The distinction matters: the file steers the model's behavior but does not coerce it mechanically.

For the social scientist, the value of this file becomes clear precisely here. Instructions stop being transient requests and become a written, auditable methodological standard. The APA 7 requirement, the prohibition on fabricated citations, the rule against sharing clinical data, the preservation of Turkish diacritics, the principles for bilingual authoring, and the citation-verification requirement can all be fixed in the file rather than repeated at the start of every session.

In this sense, `CLAUDE.md` converts a personal working habit into a methodological document.

## 2. What CLAUDE.md Is

`CLAUDE.md` is a plain markdown file that Claude Code uses to read project context and standing instructions. It is not code. It is an open text that can be read by the researcher, the team, and the tool alike. Its content varies with the researcher's working context: identity, project purpose, expected prose register, citation rules, file organization, ethical limits, and task-completion criteria can all live there.

The file can be positioned at multiple levels. A user-level `CLAUDE.md` carries general instructions that apply to every project on the machine. A project-root `CLAUDE.md` sets working standards specific to a single research project, laboratory, booklet series, or manuscript. Separate files can hold personal settings that are not committed to the repository, allowing the shared project standard and individual working preferences to be kept distinct. Anthropic's documentation specifies that the project-root `CLAUDE.md` may be re-read after certain context-compression events, while nested subdirectory files are only re-loaded into context when Claude is working with files in the relevant subtree (Anthropic, 2025). Researchers should be aware of this to avoid undetected mid-session context loss.

From an academic standpoint, this layered architecture is valuable. Research is rarely a process that unfolds on a single person's personal computer alone. Team collaboration, supervision relationships, laboratory standards, co-authorship, and open-source documentation can all enter the picture. `CLAUDE.md` provides a written methodological foundation across these different actors.

The contrast with a typed instruction in a chat window is worth making explicit. A chat instruction disappears when the window closes. `CLAUDE.md` lives on the file system. It can be versioned, shared, reviewed, and its evolution over time can be tracked. These properties take the instruction out of personal memory and make it part of the research infrastructure.

## 3. Prompt Sensitivity and the Case for Written Discipline

Language models are sensitive not only at the level of content but at the level of form. How an instruction is phrased, in what order its elements appear, which delimiter is used, and which examples are included can all produce unexpected effects on output. Sclar et al. (2023) demonstrated that minor differences in prompt formatting — a changed separator, a slightly different layout — can cause meaningful shifts in model performance. For the social scientist, this finding has direct methodological implications.

If a researcher provides instructions in a different form each session, scattered and oral, there is no reason to expect consistent outputs across sessions. A written, versioned, and verified instruction file can bring that variability under control.

A useful analogy here is the measurement instrument. Just as an uncalibrated instrument can yield different readings on successive uses, inconsistent and shifting instructions can produce different behavior across sessions. `CLAUDE.md` reduces that variability by anchoring the instructions in a fixed form. It does not eliminate variability entirely — but it gives the researcher the ability to document what standards were conveyed to the tool, when, and in what form.

A well-maintained `CLAUDE.md` is therefore not merely a practical note. It is a methodological record that contributes to reproducibility — enabling the researcher to answer, at a later date, the question: under what instructions was this tool operating?

## 4. From Prompt Patterns to Durable Configuration

Prompt engineering was initially treated largely as an individual trial-and-error skill. In recent years it has been approached more systematically. White et al. (2023) catalogued reusable prompt patterns applicable across different tasks and contexts. Schulhoff et al. (2024) evaluated prompt engineering techniques within a systematic survey. These studies show that effective prompting is not purely a matter of personal intuition: prompts can be documented, classified, and refined over time.

`CLAUDE.md` gives this development a project-level form. Individual prompts may remain transient. But a standing instruction file becomes a structured text that continuously conveys the researcher's working practices to the tool. Prompt engineering thereby ceases to be a moment-to-moment skill and becomes part of the research infrastructure.

Knuth's concept of literate programming offers a meaningful historical parallel here. In Knuth's view, code should be organized not only as a sequence of instructions the machine will execute, but as a text that a human being can read and understand. `CLAUDE.md` carries the same principle into the AI-assisted research environment. It documents the tool's behavior not as a closed configuration accessible only to the machine, but as plain text that the researcher, the team, and future readers can understand.

A good `CLAUDE.md` does not simply tell the tool what to do. It also shows other people which methodological principles governed how you used it. In this respect, the instruction file is simultaneously a working protocol and an accountability document.

## 5. CLAUDE.md as Reproducibility Infrastructure

Reproducibility is one of the foundational principles of computational research. Sandve et al. (2013) argued that every step of a computational process should be recorded, automated where possible, and organized so that results can be reproduced in the future. In AI-assisted research this principle becomes more urgent, because model behavior can shift across sessions, across prompts, and across contexts.

`CLAUDE.md` does not eliminate that variability. It does, however, provide an important starting point for documenting the AI component of the work. The model used, the instructions given, the ethical limits specified, the citation-verification rules required, and the language standards expected can all be stated explicitly in the file.

`CLAUDE.md` can therefore be understood as the machine-facing side of the methods section. A paper's methods section explains to the human reader how the research was conducted. `CLAUDE.md` tells the tool under what limits and standards it is expected to operate. Both must be complete, honest, and auditable.

One important qualification must be stated clearly. Anthropic's documentation notes that `CLAUDE.md` content is processed as project context rather than as a system prompt. The model attempts to follow the instructions, but strict compliance is not guaranteed — particularly for vague, conflicting, or overly broad instructions (Anthropic, 2025). The instruction file disciplines behavior. It does not automatically guarantee correctness, ethical compliance, or source reliability.

Reproducibility therefore cannot be delegated to the instruction file alone. The instruction file, the document archive, source verification, output auditing, and human review must all proceed in parallel.

## 6. What Belongs in CLAUDE.md for a Social Scientist

A good `CLAUDE.md` should not consist of abstract and general statements. A useful instruction file for the social scientist defines research context, working standards, and non-negotiable limits in concrete terms.

First, the tool should know who it is working with. The researcher's field, academic level, working context, and the project's purpose should be stated briefly. Clinical psychology, education science, sociology, political science, and AI ethics each entail different conceptual sensitivities and source standards.

Second, prose register and style standards should be defined. Whether the expected output is academic Turkish, international-journal English, bilingual booklet prose, ethics-board submission language, or peer-review response language should be explicit. Where needed, rules about sentence structure, tone, avoidance of overclaiming, prohibition of emojis, and the requirement not to make unverified factual claims should be written out.

Third, citation discipline should be stated in unambiguous terms. APA 7, the obligation to verify every DOI independently, the absolute prohibition on fabricated citations, the rule that only confirmed sources may appear in the reference list, and the requirement to flag uncertainty when a source cannot be verified — these should all be in the file. This section is one of the most critical safety layers in social-science AI use.

Fourth, ethical and data-security limits should be specified. Unanonymized clinical data, raw interview transcripts, field notes containing personal identifiers, and sensitive material within the scope of an ethics board review must not be passed to the tool. Obligations under KVKK and GDPR should be stated explicitly. If the tool must work with sensitive data, the file should specify that this may only occur in anonymized form and in compliance with ethics-board approval.

Fifth, the language layer should be defined. For bilingual researchers, the file should specify when Turkish is expected and when English re-authoring is appropriate, that Turkish diacritics will always be preserved, that machine-translation artifacts are unacceptable, and that conceptual equivalences will be established deliberately rather than arbitrarily.

Sixth, task-completion criteria should be stated. What evidence must the tool produce before it may treat a task as finished? Did it verify its sources? Did it show the file changes? Did it provide a diff? Did it state where the output was written? Did it flag the points that remain uncertain?

These categories transform `CLAUDE.md` from a personal note into a protocol — one that communicates the researcher's working ethics, source discipline, and methodological preferences to the tool.

## 7. Limits: an Instruction Shapes Behavior, Not Truth

A well-constructed `CLAUDE.md` is a strong starting point. But two fundamental limits must be stated explicitly.

The first limit is the probabilistic nature of the model. However detailed the instruction, a large language model still produces output by way of statistical pattern-matching. Bender et al.'s stochastic parrot critique showed that fluent and persuasive text production does not constitute genuine understanding or a guarantee of accuracy. Hicks et al. further argued that generative language models can produce outputs that are, at the epistemic level, indifferent to the distinction between truth and plausibility. For this reason, `CLAUDE.md` can lower the risk of error. It cannot eliminate it.

The second limit concerns cognitive offloading. Risko and Gilbert's work on cognitive offloading is relevant here. When people delegate certain tasks to external tools, their mental load can decrease — and this can be beneficial. But when what is offloaded is not only recall or routine procedure but reasoning itself, risk emerges.

What `CLAUDE.md` should externalize is repetitive procedure: which citation format to use, which data not to share, which language standard to maintain, which file organization to follow.

What it must not externalize is scientific judgment: the meaning of a finding, the weight of an ethical decision, the appropriateness of a method, the contextual force of a concept, the validity of an argument. These remain with the researcher.

`CLAUDE.md` should be used as a methodological instrument that makes the researcher's working standard visible — not as a mechanism that thinks in the researcher's place.

## 8. Turkish, Bilingualism, and the Western Thrace Context

The discipline of standing instructions carries particular weight for researchers who work between Turkish and English. In multilingual academic production, the challenge is not only translation. How concepts are constructed in each language, which term is preferred in which context, and how cultural specificities are preserved are also methodological questions.

`CLAUDE.md` can serve as a shared context file for the bilingual researcher. When to write in Turkish and when to re-author in English, the rule that Turkish characters must always be preserved, the principle that conceptual equivalences will be established deliberately rather than arbitrarily, and the requirement that machine-translation artifacts are not acceptable — all of these can be fixed in the file.

Regional academic infrastructures can also be defined there. DergiPark, ULAKBİM TR Dizin, HEAL-Link, local university names, institutional library access procedures, and regional indexing criteria can be explained to the tool explicitly, eliminating the need for the same corrections to be made in every session.

For a researcher working in the Western Thrace minority context, these matters are not merely formal. Place names, minority context, bilingualism, institutional names, and historical and cultural sensitivities are part of scholarly accuracy. `CLAUDE.md` can convert these sensitivities from personal memory into a written, shareable working standard.

In this respect, `CLAUDE.md` provides not only technical continuity but also linguistic, cultural, and regional consistency.

## 9. The Next Booklet

This booklet has examined `CLAUDE.md` as an instrument of standing instruction discipline in Claude Code use. The core argument is this: in AI-assisted academic production, instructions should not remain as transient, verbal, and session-by-session requests. The researcher's style, citation discipline, ethical limits, data-security rules, language standards, and verification requirements should be maintained in a written, versionable, and auditable file.

That said, `CLAUDE.md` is not memory itself. It tells the tool how to behave at the start of each session. But the intermediate results of research — field notes, source maps, reviewer responses, data dictionaries, and long-term scholarly decisions — must live within a separate archival architecture.

The next booklet turns to that question: where is academic memory kept? How is research context preserved across years? How are notes, sources, decisions, and manuscript drafts organized into a durable archive?

Booklet 003-01-0001, *Memory as Vault: A First-Principles Introduction*, continues from this point.

---

## References

Citations are in APA 7 format. Each DOI and identifier was independently verified against Crossref, arXiv, or Anthropic's official documentation on 2026-06-21.

Anthropic. (2025). *Memory: Claude Code documentation*. https://code.claude.com/docs/en/memory

Bender, E. M., Gebru, T., McMillan-Major, A., & Shmitchell, S. (2021). On the dangers of stochastic parrots: Can language models be too big? In *Proceedings of the 2021 ACM Conference on Fairness, Accountability, and Transparency (FAccT '21)* (pp. 610–623). Association for Computing Machinery. https://doi.org/10.1145/3442188.3445922

Hicks, M. T., Humphries, J., & Slater, J. (2024). ChatGPT is bullshit. *Ethics and Information Technology*, *26*(2), Article 38. https://doi.org/10.1007/s10676-024-09775-5

Knuth, D. E. (1984). Literate programming. *The Computer Journal*, *27*(2), 97–111. https://doi.org/10.1093/comjnl/27.2.97

Risko, E. F., & Gilbert, S. J. (2016). Cognitive offloading. *Trends in Cognitive Sciences*, *20*(9), 676–688. https://doi.org/10.1016/j.tics.2016.07.002

Sandve, G. K., Nekrutenko, A., Taylor, J., & Hovig, E. (2013). Ten simple rules for reproducible computational research. *PLoS Computational Biology*, *9*(10), e1003285. https://doi.org/10.1371/journal.pcbi.1003285

Schulhoff, S., Ilie, M., Balepur, N., Kahadze, K., Liu, A., Si, C., Li, Y., Gupta, A., Han, H., Schulhoff, S., Dulepet, P. S., Vidyadhara, S., Ki, D., Agrawal, S., Pham, C., Kroiz, G., Li, F., Tao, H., Srivastava, A., … Resnik, P. (2024). The prompt report: A systematic survey of prompt engineering techniques. *arXiv*. https://arxiv.org/abs/2406.06608

Sclar, M., Choi, Y., Tsvetkov, Y., & Suhr, A. (2023). Quantifying language models' sensitivity to spurious features in prompt design, or: How I learned to start worrying about prompt formatting. *arXiv*. https://arxiv.org/abs/2310.11324

White, J., Fu, Q., Hays, S., Sandborn, M., Olea, C., Gilbert, H., Elnashar, A., Spencer-Smith, J., & Schmidt, D. C. (2023). A prompt pattern catalog to enhance prompt engineering with ChatGPT. *arXiv*. https://arxiv.org/abs/2302.11382

---

**Booklet identifier.** `001-01-0004`
**Version.** `0.2.0`
**Date.** 2026-06-21
**License.** This booklet is licensed under CC BY-NC-SA 4.0. https://creativecommons.org/licenses/by-nc-sa/4.0/
**Approximate word count.** 2572 (English body text, measured with wc)
**Verified citations.** 9
**Fabricated citations.** 0
**Previous booklet.** [`001-01-0003`](../001-01-0003/en.md). Installation, First Session, and Sanity Checks
**Next booklet.** [`001-02-0001`](../001-02-0001/en.md). Research Lifecycle Map, From Idea to Publication, From Publication to Archive
