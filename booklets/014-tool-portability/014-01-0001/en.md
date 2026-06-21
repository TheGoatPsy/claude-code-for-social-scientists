---
title_en: "Beyond Claude Code, Codex and Portable Agentic Discipline"
title_tr: "Claude Code'un Ötesinde, Codex ve Taşınabilir Ajan Disiplini"
booklet_id: "014-01-0001"
category: "014-tool-portability"
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
    model_dated: null
    role: "drafting, verification, citation lookup, bilingual re-authoring"
    interaction_mode: "interactive console"
ai_contribution_level: "co-drafting"
human_review: "complete"
human_review_date: "2026-06-21"
verified_citations_count: 10
fabricated_citations_count: 0
disclosure_standard: "COPE 2023 + WAME 2023 + ICMJE 2024 + STM 2025 + EU AI Act 2024/1689 Art. 50 + ENAI"
translation_notes: "English re-authored from the finalized Turkish source (v0.1.0, 2026-06-21), not a literal translation. Content, structure, section order, claims, and references follow the Turkish canon."
closing_booklet: true
license:
  - "CC-BY-NC-SA-4.0 (prose)"
status: "release"
---

# Beyond Claude Code, Codex and Portable Agentic Discipline

This guide began with Claude Code. The first booklet asked how the tool fits into the social scientist's academic production workflow. The booklets that followed addressed file discipline, citation verification, ethical frameworks, data security, archival reasoning, and troubleshooting protocol. This closing booklet begins with a different question: what happens when the tool changes?

That question is not abstract today. AI-assisted coding and research tools are proliferating rapidly. Codex, GitHub Copilot, Gemini Code Assist, and their equivalents are entering the same workflows. A researcher tried one, moved to another, or found that their institution had chosen a different platform. The tool changed. The problem starts there. Because most researchers change their working discipline along with the tool. They begin again with the new one. Citation accountability, decision logs, disclosure discipline, human oversight — these appear to belong to the previous tool and stay behind with it.

This booklet's argument is that a sound discipline belongs to the researcher, not to any particular tool. The tool changes. The discipline travels. Understanding that distinction is the real test of everything learned throughout this guide.

## 1. What Claude Code Actually Taught

Claude Code served as a laboratory throughout this guide. But what was actually learned was not commands or shortcuts specific to Claude Code. What was learned was which questions working with an agentic tool makes obligatory.

Those questions were these: which files does the tool access? Which decisions does it make on its own, and which does it bring to the researcher for approval? Can a source enter the reference list unverified? Under what conditions can clinical data be passed to the tool? When can agent output be used directly, and when must it be reviewed? These are not technical questions. They are methodological ones. And their answers are not bound to Claude Code.

Wooldridge (2009) identifies the tension between autonomy and accountability in multi-agent systems as a fundamental design problem. In the context of academic research that tension sharpens further, because academic production requires that the process, not only the results, be defensible. However capable a tool may be, that defensibility remains with the researcher. What Claude Code actually taught, then, is this: a tool functions as a methodological partner only to the extent that the researcher can audit it.

That capacity for audit is not tied to a particular interface. When it is well established, it becomes a working habit that travels between tools.

## 2. What Codex Is

Codex is a family of tools developed by OpenAI and positioned in its official documentation as a coding agent (OpenAI, 2026a). According to the official developer documentation, Codex can write code, understand existing codebases, assist with code review and debugging, and automate development workflows. Codex CLI runs from the terminal, and can read, modify, and execute code in a selected directory (OpenAI, 2026b).

For the social scientist that description matters directly. Why directly? Because contemporary social science production is increasingly code-based: data analysis, open-science packages, repository integrity, citation verification scripts, and research automations all depend on it. A researcher who does not write code may find these tools distant at first. But the opposite is closer to the truth. The person who most needs support navigating code-based workflows, and who stands to benefit most from tools that assist with them, is not the experienced programmer — it is the social scientist. That is why understanding Codex is not an exercise reserved for software developers.

In this booklet Codex functions as a comparative object of thought alongside Claude Code. It is not the new center. It is the second example. The aim is not to recommend one tool over the other. It is to show which questions must remain constant across the transition between them.

## 3. Similarities

Claude Code and Codex raise the same foundational questions for the social scientist. These questions precede the tool's name, because they arise from the shared structure of agentic tools.

The first question is access: which directory, which files does the tool reach? The second is the approval threshold: before running a command, modifying a file, or connecting to an external service, does the tool ask the researcher for explicit consent? The third is transparency: does the tool show its changes as a diff, or does it apply them silently and move on? The fourth is logging: is output archived somewhere, and are the model version and execution date recorded? The fifth is the data boundary: can the tool reach files containing confidential participant data, clinical records, or unlicensed material?

Mialon et al. (2023) systematically examine the integration of language models with external tools and databases. That integration carries both the opportunities it offers the researcher and the privacy and error-management risks the researcher must be aware of. A tool-independent audit matrix is designed precisely to make those risks visible.

These shared questions constitute a stable framework that must be answered regardless of which tool is running. The tool may differ. The matrix does not.

## 4. Differences

Every tool has a distinct permission model, operating environment, balance of cloud versus local processing, skill architecture, and data flow. These differences can look like technical details. In the context of academic research they carry methodological consequences.

The permission model directly determines the researcher's oversight perimeter. A tool that requests approval before every command lets the researcher see every step. A tool that operates autonomously by default places greater monitoring responsibility on the researcher. The cloud-versus-local balance is critical for data security. Knowing whether research data leaves the machine, and which data privacy policy governs its handling, is necessary for the researcher to comply with institutional ethics review conditions.

The most dangerous assumption in any tool transition is this: "it was safe with the previous tool, so it is safe here." That assumption ignores the fact that two separate tools may have different access models, different logging practices, and different data processing terms. A workflow that was safe in Claude Code must have each of those conditions verified independently before it is transferred to Codex.

Yao et al. (2023), in the ReAct framework, show how agent decisions can be made traceable. That traceability is not a property that resists transfer between tools. On the contrary, the questions that demand traceability are independent of the tool's name. Whatever tool a researcher is working in, the question remains the same: how did this decision form, and where was it recorded?

## 5. Five Things That Must Travel

When tools change, five things must remain with the researcher. They are not tied to institutional features or to any particular interface. They belong to the researcher's own working habits.

The first is citation accountability. Whatever tool is in use, every reference must be verified. Even when a model produces a plausible source, the researcher must confirm independently that the source exists, that its content supports the claim attributed to it, and that the bibliographic information is correct. Bender et al. (2021) show how large language models produce errors in contexts where verification is not applied. That observation does not become invalid when the model's name changes.

The second is the data boundary. Whatever tool is in use, clinical data, participant identifiers, unredacted qualitative material, and unlicensed content are not passed to it. This boundary does not arise from the tool's privacy policy; it arises from the researcher's ethical responsibility. When the tool changes, that responsibility does not.

The third is the decision log. Decisions the researcher makes in collaboration with an agent are archived — in whatever tool is running — recording the version, the date, the command, and the output. This record is the only guarantee of reproducibility in an environment where tools keep changing.

The fourth is disclosure discipline. The researcher is obligated to declare the role of AI-assisted tools in academic production clearly and explicitly. That declaration applies not only to Claude Code. If Codex was used, if text was generated through an API call, if an automation script was run — all of these fall within the disclosure perimeter. Regardless of which tool.

The fifth is human oversight. If there is a single principle this guide has defended from beginning to end, it is this. A tool may appear autonomous. Its output may appear persuasive. But methodological judgment belongs to the researcher. When the tool changes, that responsibility cannot be delegated.

## 6. Instructions and Skills

Claude Code's skills architecture is designed to define reusable workflows as persistent instructions. A comparable skills concept exists in the Codex and ChatGPT ecosystem; the OpenAI Help Center describes skills in ChatGPT as reusable capabilities corresponding to specific tasks (OpenAI Help Center, 2026a). These two structures look similar on the surface. For a researcher trying to build a tool-independent working discipline, however, that surface similarity contains a trap.

The trap is this: a skill that works well in one tool has been written for that tool's permission model, its file access behavior, and its external service integrations. When the same skill is transferred to another tool, its behavior may diverge even if its technical form is unchanged. Skill portability, therefore, is not file copying.

The proper meaning of portability is this: the logic underlying a skill — which step requires verification, which condition must be met before the workflow proceeds, where output is archived, and how success is measured — is reconstructed in the new environment with appropriate adaptation. That reconstruction is more careful work than direct copying. But it pays its cost, because an adapted and tested skill delivers genuine portability.

## 7. Health Tests for a First Transition to Codex

When moving to a new tool, the first priority is not to begin producing output. It is to run health tests. These are the minimal verification steps a researcher working in Claude Code must complete before working in a new tool.

The first test is directory verification. Is the tool running in the correct directory? Is it reaching the research file or a system file? Working on a real file without confirming this is risky.

The second test is the approval flow. Does the tool request consent from the researcher before modifying files or running commands? If the default behavior requires approval, that must be confirmed explicitly. If it does not, an additional oversight layer must be constructed accordingly.

The third test is diff visibility. Does the tool present its changes as a diff? Accepting a file change without seeing what changed is unsafe in any tool.

The fourth test is the access boundary. Can the tool reach folders containing confidential data? Have those folders been explicitly excluded from the tool's scope? A small trial run is enough to test this.

The fifth test is the logging flow. Does the tool record the execution date, the model version, and the command history? If so, where? Without this information the reproducibility of the research cannot be guaranteed.

No real research file is worked on in the new tool until these tests are passed. This is not a suggestion. It is a methodological requirement.

## 8. Cross-Agent Oversight

Codex can examine an analysis script produced with Claude Code as a second pair of eyes. Claude Code can review a Codex output. This cross-checking arrangement looks attractive, because two separate tools are unlikely to produce the same error simultaneously.

But the limits of this arrangement must also be seen clearly. First, both tools may have been trained on overlapping base datasets. In that case shared biases survive the second agent's review undetected. Second, a second agent is not a second peer reviewer. Peer review requires human evaluation by someone who understands the field and the method. A tool cannot substitute for that. Third, cross-checking can only improve technical consistency. Detecting methodological errors, ethical gaps, or conceptual mistakes is the researcher's work.

This arrangement produces cross-tool technical verification rather than cross-tool blind trust. Is that adequate? No. But it is better than nothing — provided the researcher does not treat the second agent's approval as a substitute for human scrutiny.

Chang and Bergen (2024) comprehensively examine how language model behavior varies across different contexts. That variation is observable even between versions of the same tool. A cross-checking arrangement between two different tools can reduce — but cannot eliminate — such variation.

## 9. Future Tools

Today's Codex will change. Claude Code will change. New agents, new architectures, and new permission models will arrive. That change is not a threat to academic research. But it requires adaptation.

To understand what adaptation means, a simple question suffices: when a researcher encounters a new tool for the first time, which questions should they ask?

The first question is access: which data does the tool reach? The second is processing: what does it do with that data, where does it process it, how long does it retain it? The third is the approval threshold: when does it request permission from the researcher, and when does it act autonomously? The fourth is logging: where are decisions and outputs archived, and is that archive accessible to the researcher? The fifth is the disclosure requirement: how does using this tool affect ethics review conditions, journal disclosure policies, or institutional data security obligations?

These five questions outlast any particular tool's name. Whatever the tool, they must be answered. A researcher who has internalized them has acquired a tool-independent working discipline. That discipline does not require starting from zero at the next transition. It requires only adapting to the new context.

## 10. Skill Outputs

This booklet proposes two skill frameworks. These should be understood not as command syntax for existing tools but as templates for what a researcher must produce when moving to a new tool.

The first template is the portability matrix. Before beginning to work with a new tool, the researcher prepares a document that fills four columns for each established workflow: what travels unchanged, in what form it travels, what must be adapted, and what must be re-tested. This matrix prevents the assumption that every workflow functioning in the old tool runs silently and correctly in the new one. It makes the transition visible and auditable.

The second template is the cross-agent second-opinion protocol. When a researcher wants a second tool to review output produced with a first tool, what should they do? First, a privacy check is run on the material to be submitted. Then the minimum expected output from the review is specified: by which criteria will the evaluation proceed, what constitutes a discrepancy and how will it be logged, and how will findings be brought to human review? Without this protocol, cross-checking is not a safeguard — it is simply additional output production.

This is the closing of the booklet. The discipline that began with Claude Code is portable to Codex and to every tool that follows. That portability does not happen on its own. The researcher builds it, tests it, and maintains it. Discipline precedes the tool. When the tool is gone, the discipline remains.

## References

Citations are in APA 7 format. All DOIs verified via Crossref, all institutional URLs verified by direct access on 2026-06-21. Sources that could not be independently verified were not included.

Bender, E. M., Gebru, T., McMillan-Major, A., & Shmitchell, S. (2021). On the dangers of stochastic parrots: Can language models be too big? *Proceedings of the 2021 ACM Conference on Fairness, Accountability, and Transparency*, 610–623. https://doi.org/10.1145/3442188.3445922

Chang, T. A., & Bergen, B. K. (2024). Language model behavior: A comprehensive survey. *Computational Linguistics*, *50*(1), 293–350. https://doi.org/10.1162/coli_a_00492

Mialon, G., Dessì, R., Lomeli, M., Nalmpantis, C., Pasunuru, R., Raileanu, R., Rozière, B., Schick, T., Dwivedi-Yu, J., Celikyilmaz, A., Grave, E., LeCun, Y., & Scialom, T. (2023). Augmented language models: A survey. *Transactions on Machine Learning Research*. https://arxiv.org/abs/2302.07842

OpenAI. (2026a). *Codex*. OpenAI Developers. https://developers.openai.com/codex

OpenAI. (2026b). *Codex CLI*. OpenAI Developers. https://developers.openai.com/codex/cli

OpenAI. (2026c). *Agent skills*. OpenAI Developers. https://developers.openai.com/codex/skills

OpenAI Help Center. (2026a). *Skills in ChatGPT*. https://help.openai.com/en/articles/20001066-skills-in-chatgpt

OpenAI Help Center. (2026b). *Using Codex with your ChatGPT plan*. https://help.openai.com/en/articles/11369540-using-codex-with-your-chatgpt-plan

Wooldridge, M. (2009). *An introduction to multiagent systems* (2nd ed.). Wiley. ISBN 978-0-470-51946-2

Yao, S., Zhao, J., Yu, D., Du, N., Shafran, I., Narasimhan, K., & Cao, Y. (2023). ReAct: Synergizing reasoning and acting in language models. *International Conference on Learning Representations*. https://arxiv.org/abs/2210.03629

---

**Booklet ID.** `014-01-0001`
**Version.** `0.1.0`
**Date.** 2026-06-21
**License.** This booklet is licensed under CC BY-NC-SA 4.0. https://creativecommons.org/licenses/by-nc-sa/4.0/
**Word count (approx.).** 3091 (English body text)
**Verified citations.** 10
**Fabricated citations.** 0
**Previous booklet.** [`013-01-0001`](../../013-teaching-supervision/013-01-0001/en.md). AI in Teaching, Course Design, Supervision, and Student Feedback
**Next booklet.** None. This is the closing booklet of the v3.2.0 expansion.
