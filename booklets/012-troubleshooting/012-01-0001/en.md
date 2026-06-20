---
title_en: "When Things Go Wrong, A Working Troubleshooting Protocol"
title_tr: "İşler Ters Gittiğinde, Çalışan Bir Sorun Giderme Protokolü"
booklet_id: "012-01-0001"
category: "012-troubleshooting"
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
ai_contribution_level: "co-drafting"
human_review: "complete"
human_review_date: "2026-06-20"
verified_citations_count: 7
fabricated_citations_count: 0
disclosure_standard: "COPE 2023 + WAME 2023 + ICMJE 2024 + STM 2025 + EU AI Act 2024/1689 Art. 50 + ENAI"
translation_notes: "English re-authored from the Turkish source, not a literal translation. All worked troubleshooting examples are synthetic, derived from no real incident, in keeping with the vault sanitization protocol."
closing_booklet: true
license:
  - "CC-BY-NC-SA-4.0 (prose)"
status: "release"
---

# When Things Go Wrong, A Working Troubleshooting Protocol

The previous booklet treated the reviewer response letter as the highest-stakes text type in academic production, and in its final sentence it pointed to the fact that things can go wrong while Claude Code runs and that letter is being drafted. This booklet moves to exactly that moment. When a command returns an unexpected result, when a model response hits the context limit, when a citation simply will not verify, or when an agent makes a decision you did not authorize, the social science researcher does not need a catalog of command-line error codes. Error codes age, versions change, the surface of tools keeps shifting. What does not age is the way of thinking that narrows a problem to its root. This closing booklet presents that way of thinking as a seven-step protocol and draws the guide to a close.

## Placing a Problem Before Solving It

Problems a researcher meets while working with Claude Code tend to fall into recognizable categories, and placing a problem in the right one is already half the solution. The place you look for a tool problem differs from the place you look for a knowledge problem. The question you ask about a communication problem is different from both.

Tool problems: the command line returns an error code, the model times out before producing a response, the context window fills. The root sits in the tool itself, in the environment it runs in, or in the network connection. Knowledge problems: a library cannot be reached, a citation cannot be verified, a DOI cannot be found. These problems lie in the accessibility and accuracy of data. They do not announce themselves with a warning message. They fail quietly. Communication problems: the command given is misunderstood, the agent gets stuck in a loop, or it makes an unexpected decision. These failures live in the language between the researcher and the tool, in the transmission of intent.

Reason (2000), in his influential paper on human error, shows that errors in complex systems arise less from individual incompetence than from the structural layers of the system. His framework applies to clinical and industrial settings. This guide's inference is that the same structural logic extends to AI-assisted research workflows, where failures similarly tend to surface at the boundary between layers: at the seam where a tool meets its environment, or where the researcher's intent meets the model's interpretation differently than expected. That inference is this guide's own extension of his argument. The three categories are this guide's working map of those layers.

There is a fourth condition that does not sit cleanly inside any category: the uncertain one. A problem does not, at first glance, reveal which layer it comes from. The model returns an empty response, and whether the cause is a network outage, an inaccessible source, or a misunderstood command is unclear. In this condition the right move is not to guess a category but to eliminate them in order, from the cheapest test to the most expensive. Test the tool layer first, because an error message is the fastest evidence to read. Then the knowledge layer: is the source actually accessible? Last the communication layer, because rewriting the command demands the most effort. Uncertainty is a condition of its own: the problem's source layer is still obscured, and the narrowing process itself will bring it into view. That narrowing is the work of the fifth step of the protocol.

## Tool Problems: From CLI Error to Context Limit

Tool problems are the most visible category, because they most often come with an explicit error message. The command line returns an error code, a warning falls on the screen, a process is cut off halfway. The first reflex here should be to read the message. Slowly. An academic who is not a developer may perceive the error text as technical noise and look away from it. Yet the message most often names the category and location of the problem directly. The file name, the status code, or something as granular as the line number: noticing what is inside the message is where the solution begins.

This category's problems arrive in distinct patterns. The model timeout is the expiry of the time allotted before the model produces a response. The most common cause is too large an input or a temporary network slowdown, and the solution is to reduce the input, split the request, or retry after a pause. The context limit is the total text given to the model exceeding the window: in a long session the accumulated conversation grows silently, and at some point the model begins to lose the oldest parts. The solution is to summarize the session and start fresh, or, better, to write the context to the vault and continue with a clean session. This is the practical counterpart of the memory-as-vault principle described in the third booklet: when context is bound to disk rather than to the window, the limit ceases to be an obstacle and becomes a workflow decision. The third problem is environment configuration: working in the wrong directory, a missing dependency, a faulty path definition. Norman (2013), in *The Design of Everyday Things*, demonstrates that what we label user error is most often a design error: an assumption the tool made that the user did not know to satisfy. A researcher meeting a tool problem should ask not "what did I do wrong?" but "which assumption of the tool was not met?" That question is more productive than blame.

A concrete example clarifies the pattern. A researcher tries to have the model read a hundred-page thesis chapter in a single session, and the model stops halfway with a context error. The first reflex may be to blame the tool, but the error message states the problem directly: the input exceeded the window. The answer lies in changing the workflow, not the tool itself. The chapter is saved to the vault, divided into subsections, and each subsection is processed in a separate session. When context lives on disk, the limit is no longer a wall. It is a signal to structure the work differently.

## Knowledge Problems: The Quiet Failures

Knowledge problems are quieter than tool problems, because they do not come with an error message. When access to a library is blocked, a subscription gate silently engages and the model returns an empty result. When a DOI cannot be found, the citation verification flow stops without producing output. The danger is precisely this invisibility: a tool problem screams, a knowledge problem whispers. The strongest defense against knowledge problems is the citation verification discipline described in the seventh booklet: three-index triangulation, which accepts that a source's absence from a single database does not establish that it does not exist.

When a DOI cannot be found, three possibilities are worth working through in order. First: the DOI genuinely does not exist, because the source is a book or an older article to which no DOI was ever assigned. In this case the source is recorded without a DOI, with an ISBN or a stable URL instead. Second: the DOI exists but there is a transcription error: a digit missing or duplicated. In this case the DOI is entered again, copied directly from the source. Third: the database is temporarily unreachable. In this case an alternative index is tried: OpenAlex if Crossref is not responding, the publisher's own page if that does not respond either.

The critical rule in every case is the same: do not fabricate a source because it cannot be found. If a DOI cannot be verified, that failure is stated honestly, and the source is held until it is verified. A knowledge problem becomes an integrity problem the moment the urge to fill the gap overrides the discipline to wait. A concrete example: a researcher wishes to cite an article, but the DOI in hand does not resolve in Crossref. That empty result does not mean the article does not exist. The DOI is first copied again from the source, because most errors come from a digit entered short or long. If it still does not resolve, the article is searched by title in OpenAlex or on the publisher's page. If it still cannot be found, the most likely explanation is that it is an older source to which no DOI was assigned, and the citation is recorded with a stable URL or a print record. At no stage is an incomplete record invented. The solution here is a discipline, not a tool swap: hold until verified.

## Communication Problems: Where Intent Breaks Down

Communication problems are the subtlest of the three categories: they lie neither in the tool nor in the data but in the language between the researcher and the tool. The most common form is command misunderstanding: the researcher asks for one thing, the model understands another, and produces a result that is technically flawless but far from the intent. The cause is nearly always ambiguity. An academic gives an implicit instruction, as they would to a trusted colleague, and forgets that the model does not share that implicit context. The remedy is to make the command explicit: state what is wanted, in what form, and how success will be measured. That specificity cuts off the misunderstanding before it starts.

A deeper failure is the agent stuck in a loop: the model tries the same step again and again, each time producing a similar failure, and progress halts. This happens when the model cannot notice that one of its underlying assumptions is wrong: it registers that the action is failing but cannot step back far enough to see why. Schoenfeld (1985), in his work on mathematical problem solving, shows that what separates successful problem solvers from unsuccessful ones is metacognition: the capacity to monitor one's own thinking process, recognize that a path is a dead end, and turn back. When an agent loops, the metacognitive intervention the model cannot supply must come from the researcher. Stop the loop. Question the premise. Name the assumption that may be wrong.

Unexpected agent decisions are a distinct form: the model modifies a file that was not mentioned, or drifts toward a default behavior. This is the other face of the agentic shift described in the second booklet. The more autonomy a tool holds, the more opportunity it has to exercise that autonomy in directions you did not intend. The solution is to limit scope: bind critical actions to explicit approval, and begin each session with a clear statement of what is in play and what is not. Communication problems diminish when the researcher treats the tool not as a colleague who shares context by default, but as a capable partner to whom intent must be conveyed precisely and completely.

A worked example shows the loop type. A researcher asks the model to reformat a data file, but the file's actual structure differs from what the model assumed. The model tries the same transformation again and again, each time with the same error: it can see that the transformation fails but cannot see that its premise is wrong. The researcher's metacognitive intervention is needed: stop the loop, change the question. The question shifts from "try again" to "why is this file resisting the transformation?" Most often the answer is that the file is in a different encoding or structure than expected. Once the researcher names that difference explicitly, the loop breaks. More attempts accomplish nothing. The assumption itself needs to be restated.

## A Reasoning Framework

Placing a problem is the diagnostic half; solving it requires a reasoning framework. The protocol laid out below extends Pólya's (1945/2014) classic four-stage framework (understand, plan, carry out, look back) to the social science AI workflow. That extension is this guide's own interpretation of his method. The framework works across the great majority of problems in all three categories, because it is a general discipline of thought, not a guide to any particular command.

| Step | Name | Question | Pólya stage |
|---|---|---|---|
| 1 | Be skeptical | Is the first explanation true, or merely the easiest | Understand |
| 2 | Capture the record | What exactly does the error, log, or screenshot say | Understand |
| 3 | Reproduce | Can the problem be reproduced reliably | Understand |
| 4 | Narrow | Can I reduce the problem to its smallest case | Plan |
| 5 | Isolate | Which single variable opens the problem | Plan |
| 6 | Fix | What is the smallest correct change | Carry out |
| 7 | Document | How is the root cause and fix recorded for my future self | Look back |

The first step is to be skeptical: the first explanation that surfaces is most often the easiest, not the most accurate. Closing a problem with the first story accepted leaves the root cause in shadow. The second step is to capture the record exactly: the full text of the error message, the log output, or the unexpected result, taken from the source, not reconstructed from memory. The third step is to reproduce: if a problem cannot be reproduced reliably, there is no way to verify that it has been solved. These three steps belong to Pólya's stage of understanding.

The fourth step is to narrow: reduce the problem to the smallest case that still opens it, eliminating variables that are not necessary to produce the failure. The fifth step is to isolate: change one variable and observe its effect, so that causation and coincidence are separated. These two steps are the planning stage: the work of finding the right lever before touching anything.

The sixth step is to fix, and the constraint here matters: the solution should be the smallest correct change. A broad intervention that repairs more than the identified root cause breeds new problems in the places it touches unnecessarily. The seventh step is to document: write the root cause and the fix to the vault as a short note, so that when the same problem appears a second time the path to the solution is already laid down. Dörner (1996), in *The Logic of Failure*, shows that human decision-making in complex situations fails most consistently when side effects and delayed consequences are ignored. Documentation is a direct defense against that failure mode. It cannot prevent errors, but it makes the knowledge of how to recover from them persistent.

A single worked example makes the framework concrete. A researcher's citation verification flow quietly produces a faulty record. The researcher is skeptical first: the record looks correct on the surface, but the flow was recently updated, and the surface is not enough. The flow's input and output are captured exactly. When the same source is processed again and the same faulty record appears, the problem is confirmed as non-random. A single source tried in isolation shows the error persists, so the problem is narrowed. Isolating variables one at a time, the researcher empties the year field and the error disappears. The problem is in year parsing. The smallest correct change is made: the year-field parsing rule is fixed, and nothing else in the flow is touched. The root cause and fix are written to the vault. When the same parsing error appears again, the solution is already there. The framework turns an intuition into a method.

## The Turkish and Greek Specificity

Some problems are regional. In Türkiye, particularly in provinces outside the major cities, the internet connection can be intermittent, and access to certain external services may be restricted. In the northern cities of Greece, in Komotini and its surroundings, the variability of fiber infrastructure is a similar condition. In these situations, what looks like a tool problem is actually a network problem, and searching for the solution inside the tool itself comes to nothing.

When a problem appears to be network-sourced, a few practical steps are worth trying: an alternative DNS server, shifting the work to a time of day when the connection is reliably stable, or working over an institutional network when one is available. Detailed network configuration is beyond the scope of this booklet and is left to later versions of the guide. The critical point here is simpler: do not confuse a regional infrastructure condition with a tool defect. A researcher working from a peripheral province or over a variable line should treat the network layer as one of the first things to check in the troubleshooting protocol, not an afterthought.

## The GitHub Issue Template: Helping Someone Else

Troubleshooting is not only solving your own problem. A problem well documented also helps the next researcher who meets the same failure, and that act of documentation is the founding gesture of the open-source community. Reporting a problem as a GitHub issue turns it into shareable knowledge. A good issue is the written counterpart of steps two and three in the seven-step framework: capturing the record and reproducing.

The suggested structure is below.

```
**Problem title.** short, single line
**Version.** Claude Code version and operating system
**Expected.** what you hoped would happen
**Actual.** what happened
**Reproduction steps.**
1. ...
2. ...
**Relevant log or error message.**
```

```
error log here
```

```
**Tried before.** which solutions did not work
**Problem category.** tool, knowledge, communication, or uncertain
```

The strength of this template is that filling it forces the reporter to think clearly about the problem. Writing the gap between expected and actual clarifies what the problem actually is. Listing the reproduction steps tests whether the problem is genuinely reproducible. Documenting what was tried before saves the helper from walking the same dead-end paths.

Vaughan (1996), in her study of the NASA Challenger decision, and Perrow (1999), in his analysis of normal accidents in high-risk technologies, each show that systemic failures arise not from a single catastrophic error but from the accumulation of small, seemingly harmless deviations. Those deviations were visible to someone. They were not shared. A well-documented issue makes those deviations visible across the community and adds them to shared memory.

## Closing: The Last Line of the Series

This is the last booklet of the ten-booklet v1.0 manifesto, and this section is the close of the series.

Throughout the guide a single thesis was worked. Claude Code is, for the social scientist, not a command-line tool but a methodological partner in academic production. That partnership is meaningful only when it rests on a framework and is governed by discipline and intellectual ethics. The first booklet defined what Claude Code is at the epistemological level. The methodological-spine booklets established memory, vault architecture, and regional academic access. The production-cycle booklets addressed writing, ethics, and peer review. This last booklet gave the reasoning framework to reach for when things go wrong.

That troubleshooting belongs to a framework of reasoning is the final and consistent extension of the thesis the guide defended from start to finish. Error codes age with the tool that generates them. A reasoning framework outlasts any particular version. When all ten booklets have been read, the social science researcher holds enough of a framework to take the first step in the right direction. The rest will be the test of practice itself.

## References

Citations are in APA 7 format. Reason (2000) DOI verified against Crossref on 2026-06-04. All book ISBNs confirmed against publisher records.

Dörner, D. (1996). *The logic of failure: Why things go wrong and what we can do to make them right*. Metropolitan Books. ISBN 978-0-8050-4160-6

Norman, D. A. (2013). *The design of everyday things* (Revised and expanded ed.). Basic Books. ISBN 978-0-465-05065-9

Perrow, C. (1999). *Normal accidents: Living with high-risk technologies* (Updated ed.). Princeton University Press. ISBN 978-0-691-00412-9

Pólya, G. (2014). *How to solve it: A new aspect of mathematical method*. Princeton University Press. (Original work published 1945). ISBN 978-0-691-16407-6

Reason, J. (2000). Human error: Models and management. *BMJ*, 320(7237), 768–770. https://doi.org/10.1136/bmj.320.7237.768

Schoenfeld, A. H. (1985). *Mathematical problem solving*. Academic Press. ISBN 978-0-12-628870-4

Vaughan, D. (1996). *The Challenger launch decision: Risky technology, culture, and deviance at NASA*. University of Chicago Press. ISBN 978-0-226-85176-1

---

**Booklet ID.** `012-01-0001`
**Version.** `0.1.0`
**Date.** 2026-06-20
**License.** This booklet is licensed under CC BY-NC-SA 4.0. https://creativecommons.org/licenses/by-nc-sa/4.0/
**Word count (approx.).** 3174 (English body text, measured with wc)
**Verified citations.** 7
**Hallucinated citations.** 0
**Previous booklet.** [`010-01-0001`](../../010-peer-review/010-01-0001/en.md). Rebuttal Letters with Traceability Matrices
**Next booklet.** None. This is the closing booklet of the v1.0 manifesto. The roadmap extends with category 005 (Hooks), 006 (MCP), and 008 (Data Analysis) in the v1.5 and v2.0 versions.
