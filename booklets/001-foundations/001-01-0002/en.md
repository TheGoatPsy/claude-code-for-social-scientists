---
title_en: "The Agentic Shift: From Chat Window to Working Partner"
title_tr: "Aracın Ötesine Geçiş: Sohbet Penceresinden İş Ortağına"
booklet_id: "001-01-0002"
category: "001-foundations"
language: "en"
version: "0.1.0"
date_published: "2026-05-24"
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
    model_dated: null  # no dated identifier published by Anthropic for Opus 4.7 as of 2026-05-24
    role: "drafting, verification, citation lookup, bilingual re-authoring"
    interaction_mode: "interactive console"
ai_contribution_level: "substantial-drafting"
human_review: "complete"
human_review_date: "2026-06-20"
verified_citations_count: 10
fabricated_citations_count: 0
disclosure_standard: "COPE 2023 + WAME 2023 + ICMJE 2024 + STM 2025 + EU AI Act 2024/1689 Art. 50 + ENAI"
translation_notes: "Re-authored from the Turkish version (tr.md) against the same outline and the same verified citation set. Examples and infrastructure references domesticated for an international audience while preserving the Turkish and Greek specificity where relevant."
license:
  - "CC-BY-NC-SA-4.0 (prose)"
status: "release"
---

# The Agentic Shift: From Chat Window to Working Partner

The first booklet of this guide established what Claude Code is for the social scientist and which methodological frame it sits within. This second booklet takes one step further. It shows why the difference between the chat box in a browser tab and the agent at the command line is an epistemological distinction, not merely a design choice about where to type. The consequence of that distinction for academic production determines whether the tool is seen as an assistant or as a working partner. The goal here is not a technical comparison. It is to show how the distinction transforms the way a researcher works.

## 1. Why Chat and Agent Cannot Substitute for Each Other

The first booklet defined Claude Code as a tool that closes the gap between a notebook and a laboratory assistant. The emphasis there was the identity of the tool and the methodological framework of the user. This booklet asks a different question: how does the interface through which the tool works shape the production process?

A chat window in a browser and an agent at the command line appear, on the surface, to do the same job. You type a question into each, and each produces an answer. The resemblance is deceptive. The first booklet recalled that case formulation is built on the biopsychosocial model (Engel, 1977). The difference between seeing a patient as a symptom list and seeing them as a system operating simultaneously is the difference between diagnosis and formulation. The difference between chat and agent belongs to the same category. Chat belongs to a single passing moment, one interaction that ends when the tab is closed. An agent is a session-narrative: a continuing process bound to a file system, to its own earlier decisions, and to external tools.

Academic production, by its nature, requires a session-narrative. A systematic review is not a task that finishes in one sitting. A manuscript revision is not completed in a single response. A literature map is the accumulation of decisions made over weeks. For this reason, the interface through which the tool works is not cosmetic for the academic. It is methodologically decisive. This booklet opens that decisiveness in sequence: the anatomy of chat, the anatomy of the agent, the role of tools and subagents, and the concrete effect on academic production.

## 2. The Anatomy of the Chat Interface

The chat interface imposes interlocking limits on academic production, and together they form a structural constraint.

The single-pass problem comes first. The question you type into the chat window is sent to the model, the model produces an answer, and the interaction ends. The answer is the model's most probable output at that moment. It takes no action on the outside world. It writes no file, runs no command, retrieves no source from a library. For the social scientist this means the chat can be a thinking partner but not a production partner. You can discuss a paragraph, but you cannot scan a Zotero library of two hundred articles.

Context is a separate wall. The chat window knows only the text visible within it. What you wrote in earlier sessions, the files on your computer, the holdings in your institutional library all sit outside the window. In a long research process this limit quickly becomes a bottleneck. When the window fills, the oldest messages fall out of context, and the researcher has to re-explain a decision made three weeks ago.

Transience cuts deepest. When the chat session closes, everything accumulated inside it is lost: the instructions you gave, the intermediate results you reached, the framework you built. None of it is written anywhere permanent. This is the exact opposite of the continuity academic production requires. Years of field notes, hospital observations, and reviewer responses cannot live in a chat window, because the window resets at every close.

None of this makes the chat interface worthless. For a quick conceptual question, the rephrasing of a draft paragraph, or the explanation of a term, chat is sufficient and efficient. But for structured, multi-step, verifiable academic work the anatomy of chat is not enough. This is precisely where the agent interface enters.

## 3. The Anatomy of the Agent Interface

The word agent has a precise meaning in the multiagent systems literature. An agent is a structure that perceives the environment it is in, decides on the basis of that perception, and acts upon the environment (Wooldridge, 2009). This definition departs fundamentally from the single-pass logic of the chat interface. Chat only produces an answer. An agent perceives, decides, acts, and evaluates the result.

The most influential pattern of this loop in modern language model agents is the structure that interleaves reasoning with action. The model produces a thought step, then takes an action, observes the result of the action, and feeds that observation into the next thought step (Yao et al., 2023). For the social scientist this means the tool works incrementally, breaking a question into substeps, making each move visible, and changing course when the evidence demands it. That behavior is grounded in a growing literature on language agent architecture, which frames the components of a working agent, including memory, action space, and decision process, as analytically distinct and mutually dependent (Sumers et al., 2024).

What concretely separates the agent interface from chat becomes clear through its capabilities. File system access is at the center: the agent can read a folder on your computer, write new files into it, and modify existing ones. Everything that was ephemeral in chat can now persist on disk. Tool calling opens a second dimension, handing off tasks the agent cannot perform alone to an external service, whether that is retrieving a source from an academic index or running a command in the terminal. Within-session continuity ties both together. Over a session, prior turns accumulate in the context window and the agent can reference earlier reasoning and intermediate results as long as the session stays open. A technical clarification belongs here. Continuity in this guide means persistence within a single session. It is not an independent memory module that survives across sessions. When the session closes, that continuity ends. Writing intermediate outputs to files, the vault discipline covered in category 004, is therefore the durable layer.

How these capabilities combine to produce coherent task-oriented behavior has been shown experimentally in work where simulated agents display coordinated action and self-correction over long task horizons (Park et al., 2023). The lesson for the social scientist is methodological. The agent renders a research task as a documentable sequence of subtasks. That sequence can be traced, stopped, and checked at any point, which is what academic auditability requires.

## 4. Tools in Agentic Systems

The power of the agent comes less from what it can do alone than from which tools it can reach. A language model rests on the data it was trained on, and that data ages over time. Tool use lets the model overcome this limit. Approaches that equip the model with external sources, computational tools, and current data systematically extend the capabilities of language models (Mialon et al., 2023). It has also been shown that a model can learn to use tools and decide which tool to call in which situation (Schick et al., 2023).

For the social scientist, the most important category of tool is the academic source connected through the Model Context Protocol (MCP). MCP is an open standard that allows Claude Code to connect to external services (an academic index, a reference manager, a data source) through a structured interface. A critical qualification: MCP connections are not automatic. Each connection requires explicit configuration by the researcher, and what is available depends entirely on which servers have been set up in the local environment. With that configuration in place, the practical effect is substantial. When a researcher runs a PubMed search, the agent does not reconstruct results from training-time knowledge. It connects to PubMed through the configured MCP server, retrieves the real results, and reports them. This explains why the risk of fabricated citations is lower in a properly configured agent workflow: the citation comes from a real index, not from the model's inference about what a plausible citation might look like.

Two core tools are the file system and the terminal. File system access lets the agent read notes in the researcher's vault and write new notes. Terminal access lets the agent run a statistical script, transform a data file, or lint a markdown document. These two tools turn what was a conversation partner into a working environment. That shift carries a responsibility: every tool access is a delegation of authority. The researcher must explicitly approve which tool can perform which operation. That approval discipline is detailed in the next booklet, in the context of installation and the first session.

## 5. Subagent Composition

The most distinctive contribution of the agent model to academic production, at least in principle, is what this guide calls subagent composition: the idea that a research task can be distributed across a coordinated division of labor among several agents rather than handled by one. This is the guide's own working concept for a pattern that Claude Code supports through its subagent invocation mechanism; it is not a standardized term in the multiagent systems literature, and the specific configurations below are illustrative. This pattern resembles the layered thinking of case formulation. Just as a patient's situation calls for simultaneous analysis across biological, psychological, and contextual dimensions, a research task can be divided into distinct specializations that work in parallel.

An academic example clarifies. A doctoral student preparing a literature synthesis on digital media use among adolescents might divide the task into distinct roles. One role finds relevant articles from academic indexes and verifies their full bibliographic details. Another pulls the design, sample, and measurement instruments of those articles into a structured table. A third then draws patterns from the table and prepares summaries keyed to the researcher's questions.

The value of this composition is that each role deepens within its own narrow task while the results remain traceable. Every step, from the sources retrieved to the table built to the final pattern summary, can be audited separately. Work showing that simulated agents can exhibit coordinated behavior provides a technical basis for this kind of division of labor (Park et al., 2023). The critical point for the social scientist is this: subagent composition does not reduce the researcher's control. On the contrary, it increases it by making each stage visible. Instead of a single black box, an auditable workflow is built.

## 6. The Effect on Academic Production: Concrete Scenarios

The advantage of the agent model over the chat model is not an abstract claim; it shows up in practice.

The first scenario is reasoning-chain tracing. A researcher wants to check whether a theoretical argument is built consistently across twelve sources. Chat can discuss each source separately but cannot persistently trace the link between them. The agent reads each source, writes its relation to the argument into a file, and reports where the chain breaks.

The second scenario is the traceability matrix. A manuscript has received eleven reviewer comments. The response to each comment must be traced to the change it produced in the text. The agent keeps this matrix in a file, updates it at each revision, and verifies that no comment is left unanswered. Chat would have to rebuild this matrix in every session, and because it cannot write to the file system, it would lose the matrix the moment the tab closed.

The third scenario is the library map. A source pool of hundreds of articles can be mapped by design, sample, and publication date. The agent writes this map to the file system; when the researcher returns weeks later, the map is still in place.

The fourth scenario is conceptual mapping. In Turkish and English literature the same concept is often named with different terms. The agent can maintain a consistent glossary across sessions, not because it independently remembers across sessions, but because the glossary lives in a file and the agent reads it at the start of each session.

What these scenarios share is that continuity is doing real work in each of them. Treating artificial intelligence as a working partner is a frame defended at the popular level as well (Mollick, 2024). But the emphasis of this booklet is different. Partnership is an interface property. Without a file system, auditable subtasks, and explicit session discipline, it cannot be built.

## 7. Limits and Misunderstandings

The power of the agent model also surfaces persistent misunderstandings. Left unaddressed, they push the researcher toward either overconfidence or underuse.

One is that agency means autonomy. The agent can act, but this does not mean it decides on its own. Every action falls within the framework the researcher builds and the permission the researcher grants. Hicks and colleagues argue directly that language model output can be epistemically indifferent to truth, bullshit in the technical sense (Hicks et al., 2024). Agentic scaffolding does not resolve that. The other misunderstanding is reliability. The agent is still a stochastic system. The risk of reproducing statistical patterns without understanding holds in the agent interface as well (Bender et al., 2021). Writing a file is not the same as writing a correct file.

Three failure modes give this context an operational form. Scope drift is the most visible: the agent may exceed the boundaries of the narrow task it was given and modify files it was never meant to touch. Naming the scope explicitly at the start of every session keeps this in check. The loop trap is quieter. When the agent cannot make progress on a subtask, it tends to repeat the same step; monitoring for non-progressing turns and stopping them early is the reliable counter. Hidden state is the one that goes unnoticed longest. The agent can carry an assumption from a previous step invisibly into the next without flagging it, and the only reliable safeguard is to write intermediate outputs to a file so they can be read and challenged. Naming these patterns is a condition of disciplined use, not an argument against using the tool.

## 8. The Turkish and Greek Specificity

The concrete use of the agent model is not independent of hardware and development-environment realities. University computer environments in Türkiye are predominantly Windows-based. For the agent to have full access to the file system and the terminal, Windows users often have to install a Linux subsystem, an additional step that is not obvious to a first-time user. In Greece, at universities such as Democritus in Komotini and Athens, there are cases where the Linux development environment is set up with the support of the IT department. This infrastructure difference is a practical threshold standing between the researcher and the continuity the agent model offers. This booklet records the existence of the threshold and leaves the technical detail of its solution to the next booklet.

## 9. The Next Booklet

This booklet showed that the difference between chat and agent runs deeper than interface design. It is epistemological, and it produces continuity and auditability in academic production, provided the researcher establishes the file discipline and session structure that make continuity durable. If the value of the agent model comes from the interface difference, the first concrete question facing the academic is this: how do you set up this interface in a safe and tested way? The next booklet addresses the steps of installation and the sanity checks a researcher can genuinely run in a first session. Booklet 001-01-0003 (Installation, First Session, and Sanity Checks) continues from this point.

---

## References

Citations are in APA 7 format. Each DOI and identifier was independently verified against Crossref, arXiv, or the publisher page on 2026-05-24; frontmatter and voice revision on 2026-06-04 introduced no citation changes.

Bender, E. M., Gebru, T., McMillan-Major, A., & Shmitchell, S. (2021). On the dangers of stochastic parrots: Can language models be too big? In *Proceedings of the 2021 ACM Conference on Fairness, Accountability, and Transparency (FAccT '21)* (pp. 610-623). Association for Computing Machinery. https://doi.org/10.1145/3442188.3445922

Engel, G. L. (1977). The need for a new medical model: A challenge for biomedicine. *Science*, 196(4286), 129-136. https://doi.org/10.1126/science.847460

Hicks, M. T., Humphries, J., & Slater, J. (2024). ChatGPT is bullshit. *Ethics and Information Technology*, 26(2), Article 38. https://doi.org/10.1007/s10676-024-09775-5

Mialon, G., Dessì, R., Lomeli, M., Nalmpantis, C., Pasunuru, R., Raileanu, R., Rozière, B., Schick, T., Dwivedi-Yu, J., Celikyilmaz, A., Grave, E., LeCun, Y., & Scialom, T. (2023). Augmented language models: A survey. *Transactions on Machine Learning Research*. https://arxiv.org/abs/2302.07842

Mollick, E. (2024). *Co-intelligence: Living and working with AI*. Portfolio. ISBN 978-0-593-71671-3

Park, J. S., O'Brien, J. C., Cai, C. J., Morris, M. R., Liang, P., & Bernstein, M. S. (2023). Generative agents: Interactive simulacra of human behavior. In *Proceedings of the 36th Annual ACM Symposium on User Interface Software and Technology (UIST '23)*. Association for Computing Machinery. https://doi.org/10.1145/3586183.3606763

Schick, T., Dwivedi-Yu, J., Dessì, R., Raileanu, R., Lomeli, M., Zettlemoyer, L., Cancedda, N., & Scialom, T. (2023). Toolformer: Language models can teach themselves to use tools. In *Advances in Neural Information Processing Systems 36 (NeurIPS 2023)*. https://arxiv.org/abs/2302.04761

Sumers, T. R., Yao, S., Narasimhan, K., & Griffiths, T. L. (2024). Cognitive architectures for language agents. *Transactions on Machine Learning Research*. https://arxiv.org/abs/2309.02427

Wooldridge, M. (2009). *An introduction to multiagent systems* (2nd ed.). Wiley. ISBN 978-0-470-51946-2

Yao, S., Zhao, J., Yu, D., Du, N., Shafran, I., Narasimhan, K., & Cao, Y. (2023). ReAct: Synergizing reasoning and acting in language models. In *Proceedings of the 11th International Conference on Learning Representations (ICLR 2023)*. https://arxiv.org/abs/2210.03629

---

**Booklet identifier.** `001-01-0002`
**Version.** `0.1.0`
**Date.** 2026-06-20
**Approximate word count.** 2699 (English body text, measured with wc)
**Verified citations.** 10
**Fabricated citations.** 0
**Previous booklet.** [`001-01-0001`](../001-01-0001/en.md). What is Claude Code? A Social Scientist's Perspective
**Next booklet.** [`001-01-0003`](../001-01-0003/en.md). Installation, First Session, and Sanity Checks
