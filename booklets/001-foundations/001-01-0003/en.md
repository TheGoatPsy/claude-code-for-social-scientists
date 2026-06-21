---
title_en: "Installation, First Session, and Sanity Checks"
title_tr: "Kurulum, İlk Oturum ve Sağlamlık Denetimleri"
booklet_id: "001-01-0003"
category: "001-foundations"
language: "en"
version: "0.2.0"
date_published: "2026-05-24"
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
    model_dated: null  # no dated identifier published by Anthropic for Opus 4.7 as of 2026-05-24
    role: "drafting, verification, citation lookup, bilingual re-authoring"
    interaction_mode: "interactive console"
ai_contribution_level: "co-drafting"
human_review: "complete"
human_review_date: "2026-06-21"
verified_citations_count: 6
fabricated_citations_count: 0
disclosure_standard: "COPE 2023 + WAME 2023 + ICMJE 2024 + STM 2025 + EU AI Act 2024/1689 Art. 50 + ENAI"
translation_notes: "Re-authored from the finalized Turkish source (tr.md, v0.2.0) for this revision. The English is a native re-authoring of the Turkish canon, not a literal translation. Same section order, same verified citation set, same arguments. Commands kept minimal and principle-level because CLI syntax drifts between versions."
license:
  - "CC-BY-NC-SA-4.0 (prose)"
status: "release"
---

# Installation, First Session, and Sanity Checks

This booklet is more operational in character than the two that precede it. The first booklet situated Claude Code within a conceptual framework for the social science academic. The second addressed the distinction between a chat window and an agent-based working tool, examined through the lens of continuity and auditability. This third booklet explains which technical and methodological checks a researcher should perform when setting the tool up for the first time and running a first session.

The central claim here is this: installation is not merely a software operation. For the social science academic, installation is the first methodological filter — the one that determines the reliability of every research workflow that follows. When file access, the permission model, the working directory, the command-line environment, and the initial sanity checks are not correctly configured, the tool may appear capable while remaining unsuitable for dependable academic use.

This booklet therefore does not aim to commit specific commands to memory. Command-line tools and their official documentation change over time. What persists is the researcher's understanding of the principles by which a correct installation can be verified. The same discipline that applies to academic source verification applies here as well. Incorporating a tool into a research workflow without understanding how it operates exposes the method to an invisible risk.

The aim of this booklet is to connect the initial installation and first session of Claude Code to a sanity-check protocol that the social science researcher can genuinely control — one that answers not only whether the tool opens, but whether it is running in the correct directory, whether it reads files from disk, whether it performs writes only with explicit permission, and whether it can execute a multi-step task in an auditable manner.

## 1. System Requirements

Claude Code requires a current operating system, a functioning command-line environment, and an appropriate package manager. For macOS and Linux users the path is relatively direct: these systems ship with a Unix shell and command-line tooling already in place, which means the environment Claude Code expects is already close to what these platforms provide.

For Windows users an additional layer is involved. To access the file system and terminal more consistently on Windows, WSL2 is recommended. WSL2 supplies a Linux-based working environment inside Windows, making command-line tools more stable (Microsoft, 2026). This recommendation does not mean that other configurations are impossible; it reduces unnecessary technical complexity for social science researchers setting up for the first time.

The practical checklist for the academic is short. A current operating system, a stable internet connection, a few gigabytes of free disk space, and an environment capable of running basic terminal commands are sufficient for most starting scenarios. Claude Code does not require high local processing power or a graphics card. Model execution happens on Anthropic's infrastructure, not on the local machine. The local computer functions primarily as client, file system, and command-line interface.

This matters in academic environments with varied institutional infrastructure, such as those in Türkiye and Greece. Laptops several years old, or standard university machines, are often sufficient for a first session. What should be verified before the first session is whether the terminal opens and responds, whether commands are recognized, and whether the internet connection is stable.

The central message of this section is this: installation requires not the most powerful available machine, but a correctly configured working environment.

## 2. Account, Subscription, and Billing

Using Claude Code requires an Anthropic account and an access plan suited to the intended usage pattern. Providing specific pricing here would be inappropriate: pricing structures and plan options change over time. The durable recommendation is therefore a budgeting principle rather than a price point.

The right plan for an academic depends on how intensively the tool will be used. The needs of a doctoral student who uses it regularly for weekly literature screening, data organization, and reviewer response preparation are not the same as those of a faculty member who uses it occasionally for course materials or draft editing.

Beginning with a low-commitment, controlled usage level is a reasonable starting strategy. The researcher can observe their real usage pattern over a month: which tasks prompt them to reach for the tool, which tasks genuinely save time, which operations require human verification of the output, and where costs accumulate by task type. Plan selection should follow from that actual usage data.

For the academic budget, the cost of the tool is best understood not as an abstract subscription expense but in comparison with the labor cost of performing the same tasks manually. Screening several hundred articles by hand, for instance, may take days or weeks. That said, caution is warranted. Not every automated operation produces a time saving, and not every time saving corresponds to scientific quality. Cost assessment should therefore be conducted not only on the basis of speed but on the basis of the verifiability and auditability of the output.

Setting a monthly usage cap during the billing configuration is a useful early step. That cap prevents costs from escaping control during experimentation in the first weeks. The healthiest approach for the researcher is to try the tool on small tasks first, then expand usage volume as genuine need becomes clear.

## 3. CLI Installation

Claude Code installation can proceed through several paths depending on the system: a language package manager, a system package manager such as Homebrew on macOS, or a direct download. Whatever path is taken, the expected result at the end of installation is the same: a callable Claude Code command in the terminal.

This booklet does not fix a specific installation command. The reason is that command-line tools and their official installation procedures change over time. The current command and the authoritative instructions should always be verified against Anthropic's own documentation (Anthropic, 2026a, 2026b). For the social science researcher, what matters is not memorizing the command, but being able to determine whether the installation has been completed in a verifiable way.

After installation, the most critical checkpoint is PATH configuration. If the terminal does not recognize the command, the problem in most cases is not that the tool was not installed, but that the installation directory was not added to the system search path. In that case the terminal produces a response meaning "command not found."

For macOS and Linux users the resolution is typically to add the relevant directory to the shell configuration file — the appropriate profile depending on the shell in use, such as `.zshrc`, `.bashrc`, or an equivalent. For Windows users the same logic applies inside the Linux environment within WSL2. Once the terminal has been restarted, a command returning a version number confirms that the installation has succeeded at the basic level.

What the researcher needs to do at this stage is straightforward: verify whether the command is recognized by the system. If it is, the first threshold has been crossed. If it is not, the PATH issue must be resolved before proceeding to research work.

## 4. First Login and Permission Approval

After installation, the first session typically begins with an account verification step. The tool connects to the user's account and from that point is ready to operate within the local working directory. The most important concept from this point forward is the permission model.

Claude Code may request explicit approval from the user before performing operations such as reading a file, writing a file, or running a command in the terminal. This permission layer is not merely a technical security feature for the social science researcher. It is also a methodological instrument for the auditability of the research process. Which file is being accessed, which change is being proposed, which command is being executed, and which output is being produced — all of this must be visible to the researcher.

It is useful to think about this permission model in the context of language model safety. Ouyang et al.'s work on instruction-following through human feedback showed that models can be trained to produce outputs better aligned with user intentions. Bai et al.'s constitutional AI approach aims to embed harm-avoidance principles more directly into model behavior. But the fact that a model has been trained toward safe behavior does not make the researcher's permission oversight unnecessary (Bai et al., 2022; Ouyang et al., 2022).

The permission model is the second safety layer, on the user side. The model may propose a given action; the researcher is responsible for evaluating the context, the risk, and the appropriateness of that action. Automatic approval should not be granted when clinical data, interview transcripts, field notes containing personal identifiers, or materials within the scope of an ethics committee are involved.

The recommended strategy for the first week is clear: each action should be approved individually. This approach may feel slow at the outset, but it is through this process that the researcher learns which files the tool is touching, which commands it is running, which directories it is navigating, and where it is writing output. Trust should be established only after this observation.

## 5. Sanity Check 1: Reading a File

The first sanity check tests whether the tool is genuinely working with the local file system. The researcher should ask Claude Code to read a specific text file — one that carries real content but no sensitive data. A reading note, a dummy literature list, or an anonymized draft file would all be appropriate.

The characteristics of a healthy response are clear. The tool requests the necessary permission before reading the file. It reads the file's content. It reports the structure or a brief summary of that content. It makes no change to the file. The output contains only specific details that could have come from that file.

This test simultaneously checks three things: is file-system access working, is the permission model active, and is the tool maintaining the distinction between reading and writing?

The failure modes are equally instructive. If the tool cannot find the file, the session was likely started from the wrong working directory. If it reads without requesting permission, the permission configuration may be too permissive. If it produces a plausible-sounding but inaccurate summary without actually reading the file, this is a serious warning: the tool has generated text from its own statistical patterns rather than from the document. This last failure mode is, in the academic context, the most dangerous. Because the output is formally plausible; it simply has no basis in the source. This is why the first file-reading test is indispensable for confirming that Claude Code is genuinely engaging with the research archive.

## 6. Sanity Check 2: Editing a File and Viewing the Diff

The second check moves from reading to writing. The researcher should ask the tool to make a small, bounded change: adding a heading to a draft file, correcting a date, or restructuring a single sentence — a low-risk task.

A healthy workflow should follow this sequence. The tool first displays the proposed change clearly. Where possible, it presents the change in diff view, making visible which line is being added, which is being removed, and which expression is being altered. The tool writes to the file only after the researcher approves.

The diff view is a critical audit instrument for academic production. It allows the researcher to see what will change before the change occurs. In a manuscript draft, which sentence the tool altered is visible. In a reviewer response, which expression was added is visible. In a methods section, which concept was modified is visible.

If the tool writes directly without showing a diff, the researcher should reconsider this behavior. An unaudited write operation is not an acceptable practice in academic work. In documents such as manuscript drafts, data dictionaries, ethics committee texts, and reviewer responses, every change must be traceable.

When this test passes, the tool becomes not only a reader but a working partner capable of contributing to the writing process in a bounded and supervised way. The important point here is that writing authority must never be independent of the researcher's oversight.

## 7. Sanity Check 3: A Multi-Step Task

The third check tests the agentic character of Claude Code. The researcher should give the tool a small task composed of multiple steps: for example, reading a literature note, extracting the occurrences of a specific concept, and transferring those extracts to a separate summary file without touching the source file.

A healthy run is recognized by several criteria. The tool executes each step in sequence. It states clearly which file it is reading, what criterion it is using for selection, and which file it will write the output to. It does not overwrite the source file. The new summary file is based on material genuinely present in the source — containing no additional interpretations, assumptions, or fabricated inferences from the model's training data.

This check is a small-scale test of the agentic working logic discussed in the previous booklet. The tool does not merely produce a single response; it breaks a task into sub-steps, performs intermediate operations, and writes the output to the file system. But that capacity does not eliminate the need for verification.

The researcher should compare the final output against the source file. Are the extracted passages genuinely present in the source? Has a concept been removed from its context? Has the tool conflated interpretation with quotation? Has the summary file remained within the boundaries of the source text?

This comparison is the academic discipline of source verification carried into the technical workflow. Just as a quotation is verified against its original source before it enters a manuscript, Claude Code's intermediate output must be compared with the source file. When the third test passes, the researcher can say: the tool is not merely opening. It is reading files, writing with permission, executing multi-step tasks, and producing output that can be verified against the source.

## 8. Failure Modes

Most problems encountered in the first session reduce to a small number of recognizable patterns. Knowing these patterns allows the researcher to make the correct intervention without panic.

| Symbol | Description | Resolution |
|---|---|---|
| Command not found | The terminal does not recognize the installed command. | Check PATH configuration; restart the shell. |
| Permission error | Access was attempted to a file or directory that is not permitted. | Grant the permission approval, or correct the working directory. |
| Network error | The model call could not reach the network. | Check the connection; retry the operation. |
| Model timeout | A response did not arrive within the expected time. | Break the task into smaller steps; assess connection quality. |
| Context limit | The session has exceeded the model's context window. | Summarize the session and restart; write persistent information to a file. |

None of these patterns mean that the installation has failed entirely. Most are a natural part of the learning curve of a first session. What matters is recognizing the pattern quickly and arriving at the correct remedy.

The context-limit pattern deserves particular attention. Because this problem shows directly why a persistent file-based working habit is necessary. If the session context is exceeded, intermediate decisions and explanations that were not written to a file may be lost. The researcher should therefore not leave important output in the conversation history, but save it to the working archive.

Failure modes are not only technical problems. They also teach the researcher working discipline. A good installation is not a system that runs without error — it is a system that, when an error arises, makes visible where the problem lies.

## 9. Specifics for the Turkish and Greek Context

The installation process does not proceed identically in every country or institution. In the Turkish and Greek contexts, two topics in particular stand out: payment infrastructure and connection quality.

In Türkiye, some international payment systems may create difficulties directly in the subscription process. In that case, virtual cards, foreign bank cards, institutional accounts, or access arranged through a research center may become relevant. Which option will work depends on individual and institutional circumstances. This booklet therefore does not recommend a specific payment route; instead, it encourages the researcher to think through the alternatives in advance.

In Greece, because of the European Union payment infrastructure, standard subscription processes can generally proceed more directly. Here too, however, institutional library access, proxy settings, and computing policy may affect the researcher's experience.

Connection quality is the second significant point. In smaller cities such as Komotini, or in regions closer to rural areas, connection quality may not always be stable. Intermittent connectivity can increase the frequency of model timeout errors. In this case, running large tasks in smaller sequential steps is safer than attempting them in a single pass.

These regional details may appear technical, but they carry methodological significance. Installation is not the identical application of a universal procedure. It is the process of situating a tool within a specific institutional, infrastructural, and geographic context. For the social science researcher, responsible technology use must begin without ignoring this context.

## 10. The Next Category

This booklet treated the installation of Claude Code not as a technical starting step, but as the first methodological filter in the academic workflow. System requirements, account and billing, CLI installation, the permission model, file reading, file editing, multi-step task execution, and failure modes were examined together.

Within this framework, the essential goal for the researcher is not merely to run the tool. It is to see that the tool is running in the correct directory, that it genuinely reads files, that it makes changes only with permission, that it writes intermediate output to separate files, and that the output can be compared against the source.

Once installation is complete, the new question for the social science researcher is academic access. How will reliable access to Turkish- and Greek-language academic sources, regional indices, and institutional library infrastructure be established? The next category is dedicated to that question. Booklet 002-04-0001 — DergiPark, ULAKBIM TR Dizin, HEAL-Link, and Regional Indexing — continues from this point.

---

## References

Citations are in APA 7 format. The two arXiv preprints (Bai et al., 2022; Ouyang et al., 2022) are not registered in Crossref but were verified against arXiv on 2026-05-24. Documentation links were verified by live access on 2026-06-21; the Anthropic 2026a URL resolves to https://code.claude.com/docs and the Microsoft 2026 URL resolves to https://learn.microsoft.com/en-us/windows/wsl/.

Anthropic. (2024). *Announcing our updated responsible scaling policy*. https://www.anthropic.com/news/announcing-our-updated-responsible-scaling-policy

Anthropic. (2026a). *Claude Code documentation*. https://code.claude.com/docs

Anthropic. (2026b). *Claude Code best practices*. https://code.claude.com/docs/en/best-practices

Bai, Y., Kadavath, S., Kundu, S., Askell, A., Kernion, J., Jones, A., Chen, A., Goldie, A., Mirhoseini, A., McKinnon, C., Chen, C., Olsson, C., Olah, C., Hernandez, D., Drain, D., Ganguli, D., Li, D., Tran-Johnson, E., Perez, E., & Kaplan, J. (2022). *Constitutional AI: Harmlessness from AI feedback*. arXiv. https://arxiv.org/abs/2212.08073

Microsoft. (2026). *Windows Subsystem for Linux documentation*. https://learn.microsoft.com/windows/wsl/

Ouyang, L., Wu, J., Jiang, X., Almeida, D., Wainwright, C. L., Mishkin, P., Zhang, C., Agarwal, S., Slama, K., Ray, A., Schulman, J., Hilton, J., Kelton, F., Miller, L., Simens, M., Askell, A., Welinder, P., Christiano, P., Leike, J., & Lowe, R. (2022). Training language models to follow instructions with human feedback. In *Advances in Neural Information Processing Systems 35 (NeurIPS 2022)* (pp. 27730–27744). https://arxiv.org/abs/2203.02155

---

**Booklet identifier.** `001-01-0003`
**Version.** `0.2.0`
**Date.** 2026-06-21
**License.** This booklet is licensed under CC BY-NC-SA 4.0. https://creativecommons.org/licenses/by-nc-sa/4.0/
**Approximate word count.** 3036 (English body text, measured with wc)
**Verified citations.** 6
**Fabricated citations.** 0
**Previous booklet.** [`001-01-0002`](../001-01-0002/en.md). The Agentic Shift: From Chat Window to Working Partner
**Next booklet.** `002-04-0001`. DergiPark, ULAKBIM TR Dizin, HEAL-Link, and Regional Indexing (Phase 2)
