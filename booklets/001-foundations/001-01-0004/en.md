---
title_en: "CLAUDE.md and the Discipline of Standing Instructions"
title_tr: "CLAUDE.md ve Kalıcı Talimat Disiplini"
booklet_id: "001-01-0004"
category: "001-foundations"
language: "en"
version: "0.1.0"
date_published: "2026-05-29"
date_last_revised: "2026-06-20"
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
human_review_date: "2026-06-20"
verified_citations_count: 9
fabricated_citations_count: 0
disclosure_standard: "COPE 2023 + WAME 2023 + ICMJE 2024 + STM 2025 + EU AI Act 2024/1689 Art. 50 + ENAI"
translation_notes: "Re-authored from the Turkish version (tr.md) against the same outline and the same verified citation set. The regional and bilingual material is domesticated for an international audience while preserving the Turkish and Western Thrace specificity where relevant."
license:
  - "CC-BY-NC-SA-4.0 (prose)"
status: "release"
---

# CLAUDE.md and the Discipline of Standing Instructions

The preceding booklets of this guide covered what Claude Code is, why it differs from a chat window, and how to install it safely. Once installation is complete, the first lasting decision a researcher faces is methodological. How do you write down what the tool should know at the start of every session? The concrete home of that decision is the `CLAUDE.md` file. This booklet treats `CLAUDE.md` as a methodological instrument, one that shapes, documents, and disciplines academic production.

## Why an Instruction Is a Methodological Instrument

Every chat session starts from zero. The tool does not carry forward which citation style you required in the last manuscript, which ethical limit you set for clinical data, or which Turkish-language output standard you enforced. Each session, these must be re-established or simply forgotten.

A standing context file closes that gap. Claude Code reads `CLAUDE.md` at the beginning of every session and loads its contents as a persistent instruction. Technically, this is project context injected into the conversation, not into the system prompt (Anthropic, 2025). The tool then works within whatever frame that file establishes: who the researcher is, to which standards, and within which limits.

For the social scientist, the consequence is concrete. The instruction file becomes the single, auditable source of style, citation discipline, ethical boundaries, and methodological preferences. Instead of retyping "APA 7, no fabricated citations" at the top of every session, the researcher writes the standard once and fixes it in place. The personal habit has become an institutional standard.

## What CLAUDE.md Is: the Tool's Standing Context

`CLAUDE.md` is a plain markdown file that the agent reads automatically at the start of every session. Its content is open-ended: who the researcher is, the purpose of the project, the expected style, citation rules, file-organization conventions, and impassable ethical boundaries are expressed in ordinary sentences. The file is not code. It is a statement of working standards in language that both the researcher and the tool can read.

The file operates at multiple levels simultaneously. A file at `~/.claude/CLAUDE.md` (the user home directory) carries instructions across every project on the machine. A file at `./CLAUDE.md` or `./.claude/CLAUDE.md` in the project root is shared with the team and scoped to that project. A `CLAUDE.local.md` file holds personal overrides that are not committed to the repository, a separate preferences layer for the individual researcher within a shared team context. Parent and child directory files are pulled in additively as Claude reads files in those subtrees (Anthropic, 2025). More-local files are read last in the loading order, so their instructions appear latest in context.

One technical detail matters for academic reproducibility: after a `/compact` command (which compresses long session history), the project-root `CLAUDE.md` is re-read from disk and re-injected. Nested subdirectory files are not automatically re-injected; they reload only the next time Claude reads a file in that specific subtree. Knowing this prevents the silent loss of context mid-session.

What distinguishes this file from a typed instruction in a chat window is more than a matter of degree. A chat instruction disappears when the window closes. `CLAUDE.md` lives on disk. When the file is committed to a repository, the evolution of the researcher's methodological standards becomes traceable over time. The same file becomes a shared working standard across a research team or a thesis-supervision relationship. These properties transform the instruction from a transient request into durable methodological infrastructure.

## Prompt Sensitivity and the Case for Discipline

There is a precise, empirically grounded reason to write the instruction carefully. Language models are sensitive to small changes in prompt form in ways that are not intuitive. Sclar et al. (2023) demonstrated that minor formatting differences alone, a space inserted or a separator changed, produced large accuracy differences in a few-shot setting across the open-source models they tested. The same content, presented in a different form, can yield meaningfully different output.

For the social scientist, the consequence is direct: reproducibility depends on the stability of the prompt. If the session instruction is given loosely and verbally each time, there is no guarantee that results will remain consistent across sessions. A written, versioned, and tested instruction brings that sensitivity under control.

This moves the prompt into the domain of method. A scattered, oral instruction resembles an uncalibrated instrument. A fixed, written instruction resembles a calibrated one. When the prompt is treated as part of academic method, its form becomes part of the method too, and must be documented accordingly.

## From Prompt Patterns to Durable Configuration

Prompt engineering has matured from a scattered personal knack into a surveyed field with reusable patterns. White et al. (2023) catalogued the patterns that work repeatedly and showed that they transfer across tasks and contexts. Schulhoff et al. (2024) synthesized the techniques of the field into a systematic survey. Together these works establish that a good prompt is not chance but a documentable practice, something that can be written down and refined across uses.

Beyond individual patterns, however, there is a more durable idea. Knuth's (1984) concept of literate programming proposed that code should be written primarily for a human to read, arranged as a text explained to a person rather than merely instructions handed to a machine. `CLAUDE.md` carries the same spirit. It documents the tool's behavior in plain language that the next researcher, and your own future self, can read and understand. A good `CLAUDE.md` is a human-readable statement of a working standard, one that any colleague could inspect, question, and improve.

## CLAUDE.md as Reproducibility Infrastructure

Sandve et al. (2013) articulated ten rules for reproducible computational research. A single imperative runs through all of them: every step of a process should be recorded, and automated where possible, so that someone else, or the same researcher months later, can reproduce the same result from the same starting point.

`CLAUDE.md` is a concrete instrument for carrying this principle into AI-assisted workflows. When the model used, the instruction it followed, and the limits within which it operated are fixed in a single versioned file, the AI component of the work is documented. A year later, the same `CLAUDE.md` is the reproducibility starting point. AI-assisted research fails this standard more often than it should, because the instruction that shaped the output was never written down. The instruction file is the machine-facing side of the methods section: the methods section tells the human reader what was done, and `CLAUDE.md` tells the tool the same thing. Like the methods section, it must be accurate and complete before the work is shared.

One important qualification: Anthropic's own documentation notes that CLAUDE.md content is injected into the conversation as project context, not into the system prompt, meaning Claude attempts to follow it but strict compliance is not guaranteed, especially for vague or conflicting instructions (Anthropic, 2025). The instruction file disciplines behavior. It does not mechanically enforce it. Verification remains the researcher's responsibility.

## What Belongs in CLAUDE.md for a Social Scientist

A useful instruction file is concrete. Identity and expertise come first: the researcher's field, the level of scholarly interlocutor expected, and the disciplinary domain. Style belongs in the same file — sentence structure preferences, a ban on emojis, the tone required in academic prose, any house conventions specific to a journal target or institutional submission.

Citation discipline is the most critical entry. The APA 7 standard, a prohibition on fabricated citations, and the requirement that every DOI be independently verified before it enters the reference list should be stated explicitly. Ethical limits follow from the same logic: unanonymized clinical data must not be shared, KVKK and GDPR obligations are binding, and identifying information must never appear in shared documents. Writing these out explicitly is what converts tacit professional norms into enforceable standing instructions.

The language layer is especially consequential for bilingual researchers. The file can specify precisely in which context Turkish is expected and in which context English, and can add the explicit rule that Turkish diacritics must never be reduced to ASCII. Finally, the verification expectation deserves its own entry: what the tool must demonstrate before treating a task as complete.

## Limits: an Instruction Shapes Behavior, Not Truth

A well-constructed `CLAUDE.md` is a powerful instrument. Two limits need naming before it can be used without misleading the researcher who relies on it uncritically.

The first limit is the probabilistic nature of the model. However carefully the instruction is written, the model remains a statistical system. The instruction lowers the error rate. It does not eliminate it. The risk of reproducing statistical patterns without genuine understanding persists even under the most careful instruction (Bender et al., 2021). Generated text can carry, at the epistemic level, a character indifferent to the distinction between seeming true and being true (Hicks et al., 2024). For this reason, the instruction does not replace the discipline of verification. It complements it.

The second limit is subtler. An instruction offloads cognitive work. Risko and Gilbert (2016) showed that cognitive offloading carries both benefit and cost: when what is offloaded is the burden of recall, the gain is clear, but when what is offloaded is reasoning itself, the loss is hidden. What `CLAUDE.md` should externalize is repetitive procedure: the expected style, the required form, the impassable limit. What it must not externalize is scholarly judgment. A finding's meaning, the weight of an ethical decision: these remain with the researcher. The instruction handles procedure and leaves judgment where it belongs.

## Turkish and Western Thrace Specificity

The discipline of standing instructions carries particular weight in a bilingual and regionally specific context.

A single `CLAUDE.md` can serve as the shared methodological context for a researcher moving between Turkish and English. The file defines once which language is expected in which situation, and adds the explicit rule that Turkish diacritics must not be reduced to ASCII. For an academic working across two languages, this removes the constant cognitive burden of re-explanation session after session.

Regional terms and infrastructures are equally a subject for the instruction. DergiPark, ULAKBIM TR Dizin, HEAL-Link: what each platform is, how to cite from it, and the correct access procedure can be fixed in the file so that the tool uses them accurately without requiring repeated correction. The preferred spelling of place names such as Komotini, and the correct institutional names of regional universities, can be anchored there as well.

For a researcher working in the Western Thrace minority context, the correct and consistent use of terms is not merely formal. It is a matter of identity and of scholarly integrity. `CLAUDE.md` turns this consistency from a personal preference into a documented, shareable standard, one that survives personnel changes, project hand-offs, and the passage of time.

## The Next Booklet

`CLAUDE.md` tells the tool what to do at the start of every session. But the work itself, its intermediate results, its accumulated decisions, the field notes and manuscript drafts and coded interview fragments, has to live somewhere. The instruction shapes behavior. It does not constitute memory.

The next booklet takes up the architecture of persistent memory from first principles. Memory as Vault shows how academic context that spans years can be preserved, organized, and queried without loss. Booklet 003-01-0001 continues from this point.

---

## References

Citations are in APA 7 format. Each DOI and identifier was independently verified against Crossref, arXiv, or the official Anthropic documentation on 2026-06-04.

Anthropic. (2025). *Memory — Claude Code documentation*. https://platform.claude.com/docs/en/claude-code

Bender, E. M., Gebru, T., McMillan-Major, A., & Shmitchell, S. (2021). On the dangers of stochastic parrots: Can language models be too big? In *Proceedings of the 2021 ACM Conference on Fairness, Accountability, and Transparency (FAccT '21)* (pp. 610-623). Association for Computing Machinery. https://doi.org/10.1145/3442188.3445922

Hicks, M. T., Humphries, J., & Slater, J. (2024). ChatGPT is bullshit. *Ethics and Information Technology*, 26(2), Article 38. https://doi.org/10.1007/s10676-024-09775-5

Knuth, D. E. (1984). Literate programming. *The Computer Journal*, 27(2), 97-111. https://doi.org/10.1093/comjnl/27.2.97

Risko, E. F., & Gilbert, S. J. (2016). Cognitive offloading. *Trends in Cognitive Sciences*, 20(9), 676-688. https://doi.org/10.1016/j.tics.2016.07.002

Sandve, G. K., Nekrutenko, A., Taylor, J., & Hovig, E. (2013). Ten simple rules for reproducible computational research. *PLoS Computational Biology*, 9(10), e1003285. https://doi.org/10.1371/journal.pcbi.1003285

Schulhoff, S., Ilie, M., Balepur, N., Kahadze, K., Liu, A., Si, C., Li, Y., Gupta, A., Han, H., Schulhoff, S., Dulepet, P. S., Vidyadhara, S., Ki, D., Agrawal, S., Pham, C., Kroiz, G., Li, F., Tao, H., Srivastava, A., … Resnik, P. (2024). The prompt report: A systematic survey of prompt engineering techniques. *arXiv*. https://arxiv.org/abs/2406.06608

Sclar, M., Choi, Y., Tsvetkov, Y., & Suhr, A. (2023). Quantifying language models' sensitivity to spurious features in prompt design, or: How I learned to start worrying about prompt formatting. *arXiv*. https://arxiv.org/abs/2310.11324

White, J., Fu, Q., Hays, S., Sandborn, M., Olea, C., Gilbert, H., Elnashar, A., Spencer-Smith, J., & Schmidt, D. C. (2023). A prompt pattern catalog to enhance prompt engineering with ChatGPT. *arXiv*. https://arxiv.org/abs/2302.11382

---

**Booklet identifier.** `001-01-0004`
**Version.** `0.1.0`
**Date.** 2026-06-20
**Approximate word count.** 1873 (English body text, measured with wc)
**Verified citations.** 9
**Fabricated citations.** 0
**Previous booklet.** [`001-01-0003`](../001-01-0003/en.md). Installation, First Session, and Sanity Checks
**Next booklet.** [`003-01-0001`](../../003-memory-system/003-01-0001/en.md). Memory as Vault, A First-Principles Introduction
