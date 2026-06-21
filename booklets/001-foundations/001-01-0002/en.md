---
title_en: "The Agentic Shift: From Chat Window to Working Partner"
title_tr: "Aracın Ötesine Geçiş: Sohbet Penceresinden İş Ortağına"
booklet_id: "001-01-0002"
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
    model_dated: null  # no dated identifier published by Anthropic for Opus 4.8 as of 2026-06-21
    role: "drafting, verification, citation lookup, bilingual re-authoring"
    interaction_mode: "interactive console"
ai_contribution_level: "substantial-drafting"
human_review: "complete"
human_review_date: "2026-06-21"
verified_citations_count: 10
fabricated_citations_count: 0
disclosure_standard: "COPE 2023 + WAME 2023 + ICMJE 2024 + STM 2025 + EU AI Act 2024/1689 Art. 50 + ENAI"
translation_notes: "Re-authored in English from the finalized Turkish source (tr.md v0.2.0) as the content canon; not a literal translation. Structure, arguments, section order, and verified citation set are identical to the Turkish. English punctuation and idiom applied throughout. Infrastructure references domesticated for an international audience while preserving Turkish and Greek specificity where it matters."
license:
  - "CC-BY-NC-SA-4.0 (prose)"
status: "release"
---

# The Agentic Shift: From Chat Window to Working Partner

The first booklet of this guide established what Claude Code is for the social scientist and which methodological frame it belongs to. This second booklet takes one step further. It shows why the difference between the chat box in a browser tab and the agent at the command line is an epistemological distinction rather than a preference about where to type. The consequence of that distinction for academic production determines whether the tool is seen as an assistant or as a working partner. The central aim is to show how the distinction transforms the way a researcher actually works.

## 1. Why Chat and Agent Cannot Substitute for Each Other

The first booklet defined Claude Code as a tool that closes the gap between a notebook and a laboratory assistant. The emphasis there was on the identity of the tool and the methodological framework of the user. This booklet asks a different question: how does the interface through which the tool operates shape the production process?

A chat window in a browser and an agent at the command line appear, on the surface, to do the same job. You write a question into each, and each produces a response. The resemblance is deceptive. The first booklet recalled that case formulation is built on the biopsychosocial model (Engel, 1977). The difference between seeing a patient as a symptom list and seeing them as a system operating simultaneously across levels is the difference between diagnosis and formulation. The difference between chat and agent belongs to the same category. Chat is a single passing moment — one interaction that ends when the tab is closed. An agent is a session-narrative: a continuing process bound to a file system, to its own prior decisions, and to external tools.

Academic production, by its nature, requires a session-narrative. A systematic review is not a task that finishes in one sitting. A manuscript revision is not completed in a single response. A literature map is the accumulation of decisions made over weeks. For this reason, the interface through which the tool operates is not cosmetic for the academic; it is methodologically decisive. A choice that looks superficial on the surface reshapes the work pattern underneath. This booklet opens that decisiveness in sequence: the anatomy of chat, the anatomy of the agent, the role of tools and subagents, and the concrete effect on academic production.

## 2. The Anatomy of the Chat Interface

The limits the chat interface places on academic production are interconnected and, taken together, form a structural constraint.

The single-pass problem comes first. The question you write into the chat window is sent to the model, the model produces a response, and the interaction ends. That response is the model's most probable output at that moment. It takes no action on the outside world. It writes no file, runs no command, retrieves no source from a library. For the social scientist the implication is direct: chat can be a thinking partner but not a production partner. Discussing a paragraph is possible; scanning a Zotero library of two hundred articles is not.

The context limit is a separate wall. The chat window knows only the text visible within it. What you wrote in earlier sessions, the files on your computer, the holdings in your institutional library — all of this sits outside the window. In a long research process this limit quickly becomes a bottleneck. When the window fills, the oldest messages fall out of context, and the researcher has to re-explain to the model a decision made three weeks ago.

Transience cuts deepest. When the chat session closes, everything accumulated inside it disappears: the instructions given, the intermediate results reached, the framework constructed. None of it is written anywhere permanent. Academic production requires continuity above all else. Years of field notes, hospital observations, and reviewer responses cannot live in a chat window. The window resets at every close.

None of this makes the chat interface worthless. For a quick conceptual question, the rephrasing of a draft paragraph, or the clarification of a term, chat is sufficient and efficient. But for structured, multi-step, verifiable academic work, the anatomy of chat is insufficient. This is precisely where the agent interface enters.

## 3. The Anatomy of the Agent Interface

The word agent has a precise meaning in the multiagent systems literature. An agent is a structure that perceives the environment it is in, decides on the basis of that perception, and acts upon the environment (Wooldridge, 2009). This definition marks a fundamental departure from the single-pass logic of chat. Chat only produces a response. An agent perceives, decides, acts, and evaluates the outcome.

The most influential pattern of this loop in modern language model agents is the structure that interleaves reasoning with action. The model produces a thought step, takes an action, observes the result, and feeds that observation into the next thought step (Yao et al., 2023). For the social scientist this means the tool does not answer a question in a single pass; it decomposes it into substeps, makes each move visible, and changes direction when the evidence demands it. The cognitive architecture underlying this behavior has a systematic conceptual grounding in the literature on language agents, which frames memory, action space, and decision process as analytically distinct and mutually dependent components (Sumers et al., 2024).

The concrete capabilities that separate the agent interface from chat reinforce one another. At the center stands file system access: the agent can read a folder on the researcher's computer, write new files into it, and modify existing ones. This is the direct counterpart to the transience that characterizes chat. Tool calling opens a second dimension: the agent hands off a task it cannot perform alone to an external service — retrieving a source from an academic index or running a command in the terminal are concrete examples. Within-session continuity ties both together: over the course of a session, prior turns accumulate in the context window and the agent can reference earlier reasoning and intermediate results for as long as the session remains open.

A technical clarification is necessary here. In the working definition of this guide, within-session continuity holds for a single session only. It does not function as an independent memory module that persists across sessions. When the session closes, that continuity ends. This is precisely why writing intermediate outputs to files — the vault discipline addressed in category 004 — becomes the durable layer. It is that layer which marks the real difference from the chat interface.

How these capabilities combine to produce coherent, task-oriented behavior has been demonstrated in experimental work showing that simulated agents can exhibit coordinated action and self-correction over long task horizons (Park et al., 2023). The lesson for the social scientist is methodological. The agent renders a research task as a documentable sequence of subtasks. That sequence is traceable, auditable, and stoppable at any point — which is precisely what academic production demands.

## 4. Tools in Agentic Systems

The power of the agent derives less from what it can do in isolation than from which tools it can access. A language model rests on the data it was trained on, and that data ages over time. Tool use lets the model overcome this limit: approaches that equip language models with external sources, computational tools, and current data have been shown to extend their capabilities systematically (Mialon et al., 2023). It has also been demonstrated that a model can learn to use tools on its own and decide which tool to call in which situation (Schick et al., 2023).

For the social scientist, the most important tool category is the academic source connected through the Model Context Protocol (MCP). MCP is an open standard that allows Claude Code to connect to external services — an academic index, a reference manager, or a data source — through a structured interface. A critical qualification must be stated plainly here: MCP connections are not automatic. Each connection requires explicit configuration by the researcher, and what is accessible depends entirely on which servers have been set up in the local environment. With that configuration in place, the practical effect is substantial. When a researcher runs a PubMed search, the agent does not reconstruct results from training-time knowledge; it connects to PubMed through the configured MCP server, retrieves real results, and reports them. This is why the risk of fabricated citations is lower in a well-configured agent workflow: the citation comes from a real index, not from the model's inference about what a plausible citation might look like.

Two foundational tools are the file system and the terminal. File system access lets the agent read notes in the researcher's archive and write new notes there. Terminal access lets the agent run a statistical script, transform a data file, or lint a Markdown document. Together, these two tools turn a conversation partner into a working environment. A caveat is necessary: every tool access is a delegation of authority. The researcher must explicitly approve which tool may perform which operation. That approval discipline, along with installation and the structure of a first session, is covered in the next booklet.

## 5. Subagent Composition

The most distinctive contribution of the agent model to academic production — at least in principle — is what this guide calls subagent composition: the idea that a research task can be executed through a coordinated division of labor among several agents. A clarification is needed. This is the guide's own working concept for the subagent-invocation pattern that Claude Code supports; it is not a standardized term in the multiagent systems literature, and the specific configurations described below are meant to be illustrative rather than prescriptive. The pattern resembles the layered thinking of case formulation. Just as a patient's situation is held simultaneously across biological, psychological, and contextual dimensions, a research task can be divided into distinct specializations.

An academic example makes this concrete. A doctoral student preparing a literature synthesis on digital media use among adolescents could divide the work into distinct roles. The first role locates relevant articles from academic indexes and verifies their full bibliographic details. The second pulls the design, sample, and measurement instruments of those articles into a structured table. With the table in place, the synthesis has a concrete foundation. The third role then draws patterns from the table and prepares summaries keyed to the researcher's questions.

The value of this composition lies in the fact that each role deepens within its own narrow task while the outputs remain traceable. Every step — from the sources retrieved to the table built to the patterns extracted — can be audited separately. Work showing that simulated agents can exhibit coordinated behavior provides the technical basis for this kind of division of labor (Park et al., 2023). The critical point for the social scientist is this: subagent composition does not reduce researcher control. On the contrary, it increases it by making each stage of the process visible. A single black box is replaced by an auditable workflow.

## 6. The Effect on Academic Production: Concrete Scenarios

The advantage of the agent model over the chat model is not an abstract claim; it is understood through concrete scenarios.

The first scenario is reasoning-chain tracing. A researcher wants to verify that a theoretical argument is built consistently across twelve sources. Chat can discuss each source separately but cannot persistently track the connection between them. The agent reads each source, writes its relation to the argument to a file, and reports where the chain breaks.

The second scenario is the traceability matrix. A manuscript draft has received eleven reviewer comments. The response to each comment must be traceable to the specific change it produced in the text. The agent keeps this matrix in a file, updates it at each revision, and verifies that no comment goes unanswered. Chat would have to rebuild this matrix at every session and, because it cannot write to the file system, would lose it the moment the tab closed.

The third scenario is the library map. A source pool of hundreds of articles can be mapped by design, sample, and publication date. The agent writes this map to the file system; when the researcher returns weeks later, the map is still in place.

The fourth scenario is conceptual mapping. In Turkish and English literature the same concept is frequently named with different terms. The agent can maintain a consistent glossary across sessions — not because it independently remembers across sessions, but because the glossary lives in a file and the agent reads that file at the start of each session; cross-session continuity is secured in this way.

What these scenarios share is that continuity is doing real work in each of them. Treating artificial intelligence as a working partner is a frame that has been defended in the wider public discourse as well (Mollick, 2024). The emphasis of this booklet, however, is different. Partnership is an interface property. Without a file system, auditable subtasks, and explicit session discipline, it cannot be built by goodwill alone.

## 7. Limits and Misunderstandings

The power of the agent model brings with it persistent misunderstandings. Left unaddressed, they lead the researcher either to overestimate or to underuse the tool.

The first misunderstanding is that agency implies autonomy. The agent can act, but this does not mean it decides on its own. Every action falls within the framework the researcher builds and the permission the researcher grants. It has been argued on philosophical grounds that the output of a generative language model can be epistemically indifferent to truth at the level of its structure (Hicks et al., 2024). Agentic scaffolding does not resolve this. The second misunderstanding is that the agent is now reliable. The agent is still a stochastic system. The risk of reproducing a statistical pattern without understanding it holds in the agent interface as well (Bender et al., 2021). Writing a file does not guarantee that what is written is correct.

Each of these misunderstandings has a concrete failure mode. Scope drift is the most visible: the agent may exceed the boundaries of the narrow task it was given and modify files it was never meant to touch. Naming the scope explicitly at the start of every session keeps this in check. The loop trap is quieter: when the agent cannot make progress on a subtask, it tends to repeat the same step. Monitoring for steps that are not advancing and stopping them early is the reliable counter. Hidden state is the failure mode that goes unnoticed longest. The agent can carry an assumption from a previous step invisibly into the next without surfacing it; writing intermediate outputs to a file so they can be read and challenged is the only reliable safeguard against this. Naming these failure modes is a precondition of disciplined use, not a case against using the tool.

## 8. The Turkish and Greek Specificity

The concrete use of the agent model is not independent of hardware and development-environment realities. University computing environments in Türkiye are predominantly Windows-based. For the agent to have full access to the file system and the terminal, Windows users often have to install a Linux subsystem — an additional step that is not self-evident to a first-time user. In Greece, at universities such as Democritus in Komotini and in Athens, there are situations where the Linux development environment is set up with support from the IT department. This infrastructure difference is a practical threshold that stands between the researcher and the continuity the agent model offers. This booklet records the existence of that threshold. The technical details of crossing it are left to the next booklet.

## 9. The Next Booklet

This booklet showed that the difference between chat and agent is deeply epistemological and that this distinction produces continuity and auditability in academic production — provided the researcher establishes the file discipline and session structure that make continuity durable. If the value of the agent model comes from the interface difference, the first concrete question facing the academic is this: how do you set up this interface safely and in a tested way? The next booklet addresses the steps of installation and the sanity checks a researcher can genuinely run in a first session. Booklet 001-01-0003 (Installation, First Session, and Sanity Checks) continues from this point.

---

## References

Citations are in APA 7 format. Each DOI and identifier was independently verified against Crossref, arXiv, or the publisher page on 2026-06-21.

Bender, E. M., Gebru, T., McMillan-Major, A., & Shmitchell, S. (2021). On the dangers of stochastic parrots: Can language models be too big? In *Proceedings of the 2021 ACM Conference on Fairness, Accountability, and Transparency (FAccT '21)* (pp. 610–623). Association for Computing Machinery. https://doi.org/10.1145/3442188.3445922

Engel, G. L. (1977). The need for a new medical model: A challenge for biomedicine. *Science*, *196*(4286), 129–136. https://doi.org/10.1126/science.847460

Hicks, M. T., Humphries, J., & Slater, J. (2024). ChatGPT is bullshit. *Ethics and Information Technology*, *26*(2), Article 38. https://doi.org/10.1007/s10676-024-09775-5

Mialon, G., Dessì, R., Lomeli, M., Nalmpantis, C., Pasunuru, R., Raileanu, R., Rozière, B., Schick, T., Dwivedi-Yu, J., Celikyilmaz, A., Grave, E., LeCun, Y., & Scialom, T. (2023). Augmented language models: A survey. *Transactions on Machine Learning Research*. https://arxiv.org/abs/2302.07842

Mollick, E. (2024). *Co-intelligence: Living and working with AI*. Portfolio. ISBN 978-0-593-71671-7

Park, J. S., O'Brien, J. C., Cai, C. J., Morris, M. R., Liang, P., & Bernstein, M. S. (2023). Generative agents: Interactive simulacra of human behavior. In *Proceedings of the 36th Annual ACM Symposium on User Interface Software and Technology (UIST '23)*. Association for Computing Machinery. https://doi.org/10.1145/3586183.3606763

Schick, T., Dwivedi-Yu, J., Dessì, R., Raileanu, R., Lomeli, M., Zettlemoyer, L., Cancedda, N., & Scialom, T. (2023). Toolformer: Language models can teach themselves to use tools. In *Advances in Neural Information Processing Systems 36 (NeurIPS 2023)*. https://arxiv.org/abs/2302.04761

Sumers, T. R., Yao, S., Narasimhan, K., & Griffiths, T. L. (2024). Cognitive architectures for language agents. *Transactions on Machine Learning Research*. https://arxiv.org/abs/2309.02427

Wooldridge, M. (2009). *An introduction to multiagent systems* (2nd ed.). Wiley. ISBN 978-0-470-51946-2

Yao, S., Zhao, J., Yu, D., Du, N., Shafran, I., Narasimhan, K., & Cao, Y. (2023). ReAct: Synergizing reasoning and acting in language models. In *Proceedings of the 11th International Conference on Learning Representations (ICLR 2023)*. https://arxiv.org/abs/2210.03629

---

**Booklet identifier.** `001-01-0002`
**Version.** `0.2.0`
**Date.** 2026-06-21
**License.** This booklet is licensed under CC BY-NC-SA 4.0. https://creativecommons.org/licenses/by-nc-sa/4.0/
**Approximate word count.** 2745 (English body text, measured with wc)
**Verified citations.** 10
**Fabricated citations.** 0
**Previous booklet.** [`001-01-0001`](../001-01-0001/en.md). Claude Code Through a Social Scientist’s Lens
**Next booklet.** [`001-01-0003`](../001-01-0003/en.md). Installation, First Session, and Sanity Checks
