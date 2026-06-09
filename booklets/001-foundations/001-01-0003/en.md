---
title_en: "Installation, First Session, and Sanity Checks"
title_tr: "Kurulum, İlk Oturum, Sağlık Testleri"
booklet_id: "001-01-0003"
category: "001-foundations"
language: "en"
version: "0.1.0"
date_published: "2026-05-24"
date_last_revised: "2026-06-04"
authors:
  - name: "Onour Impram"
    orcid: "0000-0003-1076-3928"
    role: "author, principal reviewer"
ai_assisted: true
ai_tools:
  - name: "Claude Code"
    vendor: "Anthropic"
    model_alias: "claude-opus-4-7"
    model_dated: null  # no dated identifier published by Anthropic for Opus 4.7 as of 2026-05-24
    role: "drafting, verification, citation lookup, bilingual re-authoring"
    interaction_mode: "interactive console"
ai_contribution_level: "co-drafting"
human_review: "complete"
human_review_date: "2026-06-04"
verified_citations_count: 6
fabricated_citations_count: 0
disclosure_standard: "COPE 2023 + WAME 2023 + ICMJE 2024 + STM 2025 + EU AI Act 2024/1689 Art. 50 + ENAI"
translation_notes: "Re-authored from the Turkish version (tr.md) against the same outline and the same verified citation set. Commands kept minimal and principle-level on both sides because CLI syntax drifts between versions. Turkish and Greek payment and connectivity specifics preserved."
license:
  - "CC-BY-NC-SA-4.0 (prose)"
status: "release"
---

# Installation, First Session, and Sanity Checks

This booklet has a different character from the two before it. The first two were conceptual, establishing what the tool is and which interface it works through. This booklet is operational. It describes the installation and first session of Claude Code together with a sanity-check protocol that a social science academic can genuinely control. For the social science academic, installation is a methodological filter rather than a technical barrier. What is configured correctly in the first session determines the return cost over the next twelve weeks. A well-structured installation saves the researcher dozens of hours. A careless one teaches nothing and leaves the tool running loose.

One note is mandatory from the start. Command-line tools are updated often. This booklet targets conceptual control, leaving the memorization of specific commands aside. For exact command syntax, the current official documentation should always be the authoritative reference (Anthropic, 2026a). This is a deliberate choice. For a researcher, the lasting value is in understanding why and how an installation works, the same discipline that governs source verification in a literature review.

## 1. System Requirements

Claude Code runs on macOS, Linux, and Windows. The common requirement across all three is a current command-line environment and a package manager. For macOS and Linux users the path is direct, because those systems ship with a Unix shell already in place. For Windows users there is one additional layer. Full file-system and terminal access by Claude Code on Windows is provided most smoothly through the Windows Subsystem for Linux (WSL2), which opens a complete Ubuntu environment on the Windows machine and supplies the Unix tools the application expects (Microsoft, 2026). This is the guide's recommended path for Windows; alternative configurations are possible but introduce complexity that is not worth absorbing in the first session.

The practical checklist for the social science academic is short: an up-to-date operating system version, a few gigabytes of free disk space (session memory and vault files grow steadily over time), and a stable internet connection (model calls travel over the network). One point is worth emphasizing: the tool does not require a dedicated graphics card or high local processing power. All computation happens in Anthropic's infrastructure; the local machine is only a client. That architecture points to a practical inference: many university machines in Türkiye and Greece, including laptops several years old, are sufficient to run the tool without friction. The one preliminary check that genuinely matters is confirming that the terminal opens and responds to a basic command.

## 2. Account, Subscription, and Billing

An account is required before installation. Anthropic offers several plan tiers calibrated to different usage volumes. The right tier for a given academic depends on how intensively the tool will be used: a doctoral student running continuous literature screenings week after week has different needs from a faculty member who uses the tool occasionally for course design. This booklet gives no specific pricing figures, because plan prices change between versions of this guide. Instead it proposes a principle: begin with the lowest-commitment option, observe your real usage pattern for a full month, and then adjust.

One framing is worth making explicit for the academic budget context. The cost of the tool is best assessed by comparison with the hourly cost of a research assistant performing the same task, rather than as an abstract subscription line item. A single two-hundred-article screening session that saves two weeks of manual work more than justifies a monthly fee. Actual value will vary with task type and usage volume. Usage is typically metered by the volume of text processed, so the cost scales predictably: small exploratory tasks carry nearly no expense, while large screenings carry a proportionate and foreseeable cost. Setting a monthly usage cap in the billing configuration is a sound early step. That cap allows the researcher to experiment freely in the first weeks without anxiety about runaway charges.

## 3. CLI Installation, Step by Step

Installation typically proceeds through a language package manager, a system package manager such as Homebrew on macOS, or a direct download. All converge on the same result: a command callable from the terminal. After installation, the single critical step is confirming that this command is visible on the system search path (PATH). If the terminal does not recognize the command, the problem is almost always in the PATH configuration, rarely in the installation itself.

This booklet does not pin a specific installation command here, because the tool version changes frequently and a fixed command goes stale quickly. The current and correct installation command lives in the official documentation and should be taken from there (Anthropic, 2026a). Recommended starting workflows and good-practice patterns are documented in a separate section of the same official source (Anthropic, 2026b). When installing a technical tool, going to the primary source is safer than trying a command copied from a third-party blog. The same instinct that governs citation verification in a literature review applies here.

The practical symptom of a PATH problem is unmistakable: you call the command and the terminal replies "command not found." The fix usually reduces to two steps: adding the installation directory to the shell configuration file, then restarting the terminal. On macOS and Linux this means editing the shell profile (`.zshrc`, `.bashrc`, or equivalent). On Windows WSL2 the same logic applies inside the Ubuntu environment. This is the most common first-session obstacle; it is also the one that, once resolved, never recurs. The simplest confirmation that installation has succeeded: asking the command for its version number returns a version number.

## 4. First Login and Permission Approval

After installation, the first session opens with authentication: the tool connects to your account. From that point forward, the concept that governs every interaction is the permission model. Claude Code requests explicit permission before performing operations such as reading a file, writing a file, or executing a command in the terminal. This mechanism is the structural foundation of safe use.

Understanding why this permission layer exists is worth a moment's pause. Language models are trained to follow instructions through human feedback. The InstructGPT paradigm establishes that the model learns which outputs humans prefer, and this training shapes how it responds to subsequent instructions (Ouyang et al., 2022). But instruction-following does not make every instruction safe. Anthropic's models are trained with a constitutional alignment approach that encodes a set of harm-avoidance principles directly into model behavior through a self-critique loop (Bai et al., 2022). The permission model is the user-side complement of that alignment layer: the model is trained to behave safely, and the researcher explicitly controls which actions are permitted. Neither side alone is sufficient. Both must hold together.

In practice this means an approval prompt appears before every sensitive operation. The tool states what it intends to do; the researcher approves or declines. The recommended starting strategy for a first session is to approve each action separately. In the first weeks, this one-at-a-time approach is the most reliable way to learn what the tool actually does at each step: which files it touches, how commands actually return, and where directory navigation takes it. As trust builds and familiar patterns repeat, persistent approval can be granted for specific low-risk operations. Access to directories containing clinical data, interview transcripts, or personal identifiers, however, should never be bound to automatic approval. A responsible-use framework requires that such boundaries be drawn explicitly and maintained (Anthropic, 2024), though the RSP speaks to institutional policy rather than the operational permission settings themselves.

## 5. Sanity Check 1: Reading a File

The first sanity check is the simplest and the most informative. Ask the tool to read a text file: a note file from your vault, a reading list, anything with real content. What a healthy response looks like: the tool reads the content of the file, reports a summary or the structure of that content back to you, makes no change, and signals that it requested permission before reading. Concrete details in the output that could only have come from the actual file are the evidence that the connection to the local file system is genuine. This single check covers the essentials: file-system access works, the permission model is active, and the read stays cleanly separated from any write.

The failure modes are instructive. If the tool cannot find the file, the working directory is set incorrectly. Start the session inside the right folder. If it reads without requesting permission, the permission configuration is too permissive and should be tightened before further work. If it produces plausible-sounding content that does not actually match the file, this is a serious warning: the tool has generated text from its own statistical patterns rather than reading the document. This last failure mode is, in the guide's assessment, the most dangerous in an academic context, because fabricated content is syntactically indistinguishable from retrieved content and will not be caught by a casual review. A healthy result from this first check gives the researcher genuine confidence that the tool works with local files. That confidence is the foundation of every workflow that follows.

## 6. Sanity Check 2: Editing a File and Viewing the Diff

The second check moves one step beyond reading. Ask the tool to make a small, bounded change to a file: add a heading to a note, correct a date, append a sentence. A healthy response unfolds in this sequence: the tool first displays the proposed change in a diff view (showing exactly which lines will be added or removed), requests your approval, and only then writes to the file. That sequence is not optional. It is the audit trail.

The diff view is a critical instrument for academic production. You see what will change before the change happens, not after. In a manuscript revision, you can see precisely which sentence the tool altered. In a reviewer response, you can confirm that the edit addresses the comment and only that comment. Working with a diff view from the very first session installs this traceability as a default, not an afterthought. If the tool writes the change directly without showing a diff, the permission configuration needs revision. An unaudited write is professionally unacceptable in academic work, where the integrity of the record is non-negotiable. When this check passes, the tool has graduated from reader to writing partner: capable of making changes, but only under your explicit oversight at each step.

## 7. Sanity Check 3: A Multi-Step Task

The third check tests the agentic character that distinguishes Claude Code from a chat window. Give the tool a chained task: read a literature file, extract the passages where a specific concept appears, and write those extracts to a separate summary file without touching the source. Each step depends on the previous one. Each step touches a different file.

A healthy run looks like this: the tool executes each step in sequence, reports what it has done at each step, and writes the final output to a separate file rather than overwriting the source. The final summary file contains only material that was genuinely present in the source, with no elaborations, interpolations, or content produced from the model's training data. This is what the action loop described in booklet 001-01-0002 looks like when it runs correctly on real files in a real session.

The most common failure mode in this check is that the tool skips an intermediate step or, more seriously, produces content from its own memory rather than the source document. For this reason the verification step is mandatory: compare the final output against the source file, passage by passage. This comparison is academic discipline carried into the technical workflow, the same principle that requires a quotation to be checked against its original source before it enters a manuscript. If this third check passes, the installation is complete and the tool is ready for academic production.

## 8. Failure Modes

Most problems encountered in the first session reduce to a small set of recognizable patterns. Each one has a clear cause and a clear remedy.

| Symbol | Explanation | Solution |
|---|---|---|
| Command not found | The terminal does not recognize the installed command | Check the PATH configuration, restart the shell |
| Permission error | Access was attempted to a file or directory without permission | Grant the permission approval or correct the working directory |
| Network error | The model call could not reach the network | Check the connection, retry if needed |
| Model timeout | The response did not arrive within the expected time | Break the task into smaller steps, check connection quality |
| Context limit | The session exceeded the model's context window | Summarize and restart the session, write persistent information to a file |

None of these modes signals that the installation has failed. All of them are part of the normal learning curve of a first session. What matters is recognizing the pattern quickly and reaching the appropriate remedy without panic. The context-limit mode deserves special attention: it is the failure that most directly reinforces the vault habit. When the session exceeds the model's context window, the work that was not written to a file is gone. The researcher learns firsthand that persistent, file-based documentation is a structural necessity. Encountering it early, before any research workflow depends on session continuity, is the best time to absorb the lesson.

## 9. The Turkish and Greek Specificity

Regional realities appear at two points in the installation process.

The first is payment. In Türkiye, certain international payment infrastructures impose restrictions that can prevent direct subscription. Alternative paths in that case include a virtual card issued by a domestic fintech provider, a foreign bank card, or an institutional account configured through a university or research center. This booklet maps these alternatives only; which option works depends on institutional context and individual access conditions, and no financial advice or product recommendation follows from this.

The second is connection quality. In smaller cities (Komotini in the Rhodope region is a concrete example), fiber connectivity is not uniformly reliable. Intermittent connections increase the frequency of the model-timeout failure mode. The practical remedy is the same one that applies everywhere: break tasks into smaller steps, and work during stable connection windows rather than forcing large tasks through an unreliable link. Greece, because it is an EU member state, follows the standard payment flow without the restrictions that apply in Türkiye. These two regional details carry a methodological point that extends beyond the technical: installation is an act of fitting a tool to a specific institutional, infrastructural, and geographic context. The procedure is universal in name; the conditions it meets are always particular.

## 10. The Next Category

This booklet established that installation is a methodological filter, and that the sanity checks give the researcher evidence that the tool genuinely operates on local files. With installation complete, the first substantive question facing the academic is how to access Turkish and Greek academic journals reliably through the tool. The next category is dedicated to academic access infrastructure: DergiPark, ULAKBIM TR Dizin, HEAL-Link, and the EZproxy configurations that connect them to a working research session. That infrastructure is absent from international guides and among the highest-value contributions this guide makes. Booklet 002-04-0001 continues from this point.

---

## References

Citations are in APA 7 format. The two arXiv preprints (Bai et al., 2022; Ouyang et al., 2022) are not registered in Crossref but were verified against arXiv on 2026-05-24. Documentation links were verified by live access on 2026-06-04; the Anthropic 2026a URL resolves to https://platform.claude.com/docs/en/claude-code and the Microsoft 2026 URL resolves to https://learn.microsoft.com/en-us/windows/wsl/.

Anthropic. (2024). *Responsible scaling policy*. https://www.anthropic.com/news/anthropics-responsible-scaling-policy

Anthropic. (2026a). *Claude Code documentation*. https://docs.claude.com/en/docs/claude-code

Anthropic. (2026b). *Claude Code best practices*. https://code.claude.com/docs/en/best-practices

Bai, Y., Kadavath, S., Kundu, S., Askell, A., Kernion, J., Jones, A., Chen, A., Goldie, A., Mirhoseini, A., McKinnon, C., Chen, C., Olsson, C., Olah, C., Hernandez, D., Drain, D., Ganguli, D., Li, D., Tran-Johnson, E., Perez, E., ... Kaplan, J. (2022). *Constitutional AI: Harmlessness from AI feedback*. arXiv. https://arxiv.org/abs/2212.08073

Microsoft. (2026). *Windows Subsystem for Linux documentation*. https://learn.microsoft.com/windows/wsl/

Ouyang, L., Wu, J., Jiang, X., Almeida, D., Wainwright, C. L., Mishkin, P., Zhang, C., Agarwal, S., Slama, K., Ray, A., Schulman, J., Hilton, J., Kelton, F., Miller, L., Simens, M., Askell, A., Welinder, P., Christiano, P., Leike, J., & Lowe, R. (2022). Training language models to follow instructions with human feedback. In *Advances in Neural Information Processing Systems 35 (NeurIPS 2022)* (pp. 27730-27744). https://arxiv.org/abs/2203.02155

---

**Booklet identifier.** `001-01-0003`
**Version.** `0.1.0`
**Date.** 2026-06-04
**Approximate word count.** 2835 (English body text, measured with wc)
**Verified citations.** 6
**Fabricated citations.** 0
**Previous booklet.** [`001-01-0002`](../001-01-0002/en.md). The Agentic Shift: From Chat Window to Working Partner
**Next booklet.** `002-04-0001`. DergiPark, ULAKBIM TR Dizin, HEAL-Link, and Regional Indexing (Phase 2)
