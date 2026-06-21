---
title_en: "When Things Go Wrong, A Working Troubleshooting Protocol"
title_tr: "İşler Ters Gittiğinde, Çalışan Bir Sorun Giderme Protokolü"
booklet_id: "012-01-0001"
category: "012-troubleshooting"
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
    model_dated: null
    role: "drafting, verification, citation lookup, bilingual re-authoring"
    interaction_mode: "interactive console"
ai_contribution_level: "co-drafting"
human_review: "complete"
human_review_date: "2026-06-21"
verified_citations_count: 7
fabricated_citations_count: 0
disclosure_standard: "COPE 2023 + WAME 2023 + ICMJE 2024 + STM 2025 + EU AI Act 2024/1689 Art. 50 + ENAI"
translation_notes: "English re-authored from the finalized Turkish source (v0.2.0), not a literal translation. All worked troubleshooting examples are synthetic, derived from no real incident, in keeping with the archive sanitization protocol."
closing_booklet: true
license:
  - "CC-BY-NC-SA-4.0 (prose)"
status: "release"
---

# When Things Go Wrong, A Working Troubleshooting Protocol

The previous booklet treated the reviewer response letter as one of the highest-stakes text types in academic production. This closing booklet moves to the most fragile moment in that production chain. When a command returns an unexpected result, when a model response stalls at the context limit, when a citation simply will not verify, when a file opens in the wrong version, or when an agent makes an unauthorized decision, what the researcher needs is not a catalog of command-line error codes.

Error messages age. Versions change. The surface of tools keeps shifting. What does not age is the mode of reasoning that narrows a problem to its root. This booklet presents that mode of reasoning as a seven-step protocol for the social science researcher working with Claude Code. The aim is not to multiply memorized commands for moments of panic; it is to show the researcher which layer to examine when things go wrong, which evidence to capture, which variable to isolate, and how to archive the solution.

This booklet is also the closing of the v1.0 series. The guide's first booklet situated Claude Code within the social scientist's academic production workflow. This last booklet concerns the unavoidable truth of that workflow: every system fails at some point. Every tool is misunderstood at some point. Every archive resists at some point. Academic maturity lies not in believing that nothing will break but in being able to move forward methodically when it does.

## 1. The Layers of Troubleshooting

Most problems a researcher encounters while working with Claude Code fall into four layers. The first is the tool layer. The command line returns an error, the model times out, the context window fills, the terminal does not recognize a command. In this case the problem is sought in the tool itself, in the environment it runs in, or in the network connection.

The second is the knowledge layer. A DOI cannot be resolved, a library record cannot be found, a source is inaccessible, a PDF may not return the full text. These problems are largely silent. They produce no error message. That is precisely what makes them dangerous, because an empty result most often does not mean the source does not exist. It may mean no access, out of index scope, a mistyped DOI, or a record held in a different database.

The third is the communication layer. The researcher conveys an intent; the model understands something else. The command is ambiguous, the scope is unspecified, the success criterion is unwritten. The model produces an output that is technically sound but remote from what the researcher wanted. In these problems the tool is not broken. The data is not broken. The transmission of intent is insufficient.

The fourth is the uncertain state. Which layer the problem comes from is not visible at first glance. The model returns an empty response, but whether the cause is a network outage, a blocked source, or a poorly constructed command is unclear. In the uncertain state, the right move is not to guess — it is to eliminate layers in sequence. First the tool layer, then the knowledge layer, then the communication layer. The layer that can be resolved fastest is eliminated first.

Reason (2000) treats human error not as a function of individual deficiency but as a property of the system's structural layers. That framework was not developed for AI-assisted research. Even so, the same structural mode of thinking is valuable here. The problem most often surfaces not in a single person's inattentiveness but at the point of contact between the tool and its environment, between information and its access conditions, or between the researcher's intent and the model's interpretation. The layer model in this guide is a practitioner's framework that adapts Reason's systems approach to the social science researcher's Claude Code workflow.

| Layer | Symptom | First question | First intervention |
|---|---|---|---|
| Tool | Error message, timeout, context limit, permission error | Which assumption did the tool fail to meet? | Capture the error text, reduce the input, inspect the environment |
| Knowledge | DOI not found, source inaccessible, record returns empty | Does the source genuinely not exist, or is access simply unavailable? | Verify via Crossref, publisher page, alternative index, and library record |
| Communication | Model performs the wrong task, enters a loop, exceeds scope | Was the intent communicated clearly enough? | Rewrite the command, add a success criterion, narrow the scope |
| Uncertain | Cause is not visible, symptoms appear mixed | Which layer can be eliminated fastest? | Rule out tool, knowledge, and communication layers in sequence |

## 2. Tool Problems: From CLI Error to Context Limit

Tool problems are the most visible, because they most often leave a trace on the screen. The terminal returns an error code, the model produces no response, the file system denies access, a command behaves differently than expected. The first reflex in these situations should not be to close the error message but to read it slowly. A researcher need not be a developer. But they must read an error message the way they would read an academic document, because that text most often names the problem's category, the file path, the line number, and the cause directly.

Model timeout typically arises when the input is too large, the network is slow, or a model call takes longer than expected. The solution is most often to reduce the task: rather than processing a hundred pages in a single pass, divide the chapter into subsections, summarize a long conversation and move to a fresh session, or load only the relevant files into context. That is the more reliable path.

The context limit is a more insidious tool problem. In long sessions the model's context window fills. Old messages drop. The researcher may believe the model still remembers earlier decisions, but the context has already overflowed. The solution here is not to push the model harder — it is to move the context to disk. A session summary is written, decisions are archived, and work continues in a clean session. When context is bound to disk rather than to the window, the limit ceases to be a wall and becomes a workflow decision.

Environment configuration is another frequent tool problem. Working in the wrong directory, a missing dependency, a faulty path definition, a PATH error, a permission issue — any of these can create the impression that the tool itself is broken. Norman's (2013) design principle is useful here. What appears to be user error most often originates in an assumption the system never made visible to the user. The question the researcher should ask is: which condition did the tool assume was already met?

A concrete scenario makes this clear. A researcher attempts to have the model read a hundred-page thesis chapter in a single session and the model returns a context error. The first reaction may be that the tool is inadequate. Yet the error message says so directly: the input exceeded the window. The correct solution is to change the workflow. The chapter is saved to the archive, divided into subsections, each subsection processed in a separate session, and the results merged in a central summary file. Troubleshooting does not force the tool. It reorganizes the workflow to match the tool's actual limits.

| Symptom | Likely root cause | Appropriate intervention |
|---|---|---|
| Command not found | PATH or installation path missing | Run the version command, check the PATH setting, restart the terminal |
| Timeout | Input too large, network slow, operation too long | Break the task up, reduce input volume, run a short trial |
| Context limit | Session has grown too large | Extract a summary, write decisions to a file, start a new session |
| Permission error | File or folder access is closed | Check the working directory, grant only the necessary permissions |
| Wrong output file | Working in the wrong directory or ambiguous output path | Specify the output file explicitly, fix the target folder |

## 3. Knowledge Problems: The Quiet Failures

Knowledge problems are more dangerous than tool problems because they most often arrive in silence. A DOI cannot be resolved, but the terminal does not present that dramatically as an error. A library record cannot be found, but the model may interpret that as no source. A subscription gate bars access to the full text, but the output simply returns empty. This silence pushes the researcher toward a fast and wrong conclusion.

In the context of citation verification the fundamental rule does not change. A source is not invented because it cannot be found. If a DOI does not resolve, the first step is to copy the DOI again directly from the source. Then Crossref, the publisher's page, PubMed, OpenAlex, or the library record is tried. If the source is a book, a thesis, a report, or an article predating the DOI system, it is verified with another stable identifier — an ISBN, an institutional URL, or a library record. A source that cannot be verified does not enter the reference list. It is held.

Library access is also a knowledge problem. The inaccessibility of an article does not mean the article does not exist. The institutional subscription may be absent, the proxy may not be functioning, an EZproxy session may have timed out, or a publisher's page may have changed its redirect. Claude Code should not treat the absence of full text as the absence of content. The researcher must maintain the distinction between access and existence.

That distinction is especially important with regional academic sources. DergiPark, ULAKBİM TR Dizin, HEAL Link, and YÖK Tez Merkezi do not behave in the same ways as international commercial databases. When a source cannot be located, the first explanation should not be its non-existence. Database coverage, access path, and record format must be checked first.

### Worked Example: A DOI Will Not Resolve

A researcher has what appears to be a DOI — a character string believed to be one. Crossref returns nothing. The correct first move is not to try to correct the DOI by hand. The DOI is copied again from the PDF, the publisher's page, or the article's bibliographic record. If it still does not resolve, a title search is tried. If the title is found on the publisher's page but carries no DOI, the source is recorded as DOI-less. If the title cannot be found anywhere, the source is treated as suspect and excluded from the reference list. Every step of this process is written to the source passport. The decision then rests on a record, not on memory.

## 4. Communication Problems: Where Intent Breaks Down

Communication problems surface when both the tool and the data appear to be working. The researcher wanted one thing; the model did something else. The output may be technically correct. It may even appear fluent and persuasive. But it does not serve the goal. In these problems the issue is most often not in the model's capacity but in the command's ambiguity.

The implicit instruction given to an academic colleague is not the same as the instruction given to a model. A colleague can supply domain context, prior conversations, institutional expectations, and the researcher's register from memory. The model sees only what is written. For this reason a good command specifies not only what is to be done but what is not to be done: which files to touch, which to leave out, in what form the output should be delivered, and how success will be measured. A command given without these specifications is well-intentioned but risky shorthand.

The agent loop is one of the most typical forms of communication failure. The model attempts the same step repeatedly, meeting a similar error each time. Retrying solves nothing, because the problem is not in the step being attempted but in the assumption that made that step seem possible. The metacognition Schoenfeld (1985) emphasizes in his work on mathematical problem solving is exactly what is called for here. The researcher must see the process from outside and ask: which assumption does the model believe to be correct?

An unexpected agent decision carries a different risk. The model touches an unrelated file, changes an output path, edits an out-of-scope document, or continues on an unapproved assumption. In this case the problem is that the agent's action space was left too wide. The solution is to narrow the scope, protect critical files, review every change through a diff, and bind high-risk operations to explicit approval.

A concrete example: a researcher tells the model to reformat a data file. The model attempts the same transformation repeatedly and receives an error each time. The problem is that the model has assumed the file is comma-delimited. It is in fact semicolon-delimited. Retrying changes nothing. The right question is: why is this file resisting this transformation? Once the assumption becomes visible, the loop breaks.

| Problem type | Typical symptom | Corrective move |
|---|---|---|
| Ambiguous command | Output is correct but differs from what was wanted | Rewrite the intent, scope, format, and success criterion |
| Agent loop | Model repeats the same step | Stop the loop, name the assumption, reframe the task |
| Scope drift | Unrelated files or extra operations are introduced | Explicitly specify the working directory, files to touch, and off-limits areas |
| Hidden assumption | Model treats something unspoken as correct | Make intermediate decisions visible, list assumptions separately |

## 5. A Seven-Step Reasoning Framework

The three layers help locate a problem. Solving it requires a reasoning framework. The seven-step protocol below is an adaptation of Pólya's classic stages — understand, plan, execute, and look back — to the social science AI workflow (Pólya, 1945/2014). That adaptation is this guide's own practitioner interpretation. It is not bound to any particular command, so the sequence of thinking holds even as tool versions change.

The first step is to be skeptical. The first explanation to surface is most often the easiest story, not the most accurate one. The second step is to capture the record. The error message or unexpected output is taken from the source, not reconstructed from memory. The third step is to reproduce. If a problem cannot be reproduced reliably, neither can its solution be stated with confidence.

The fourth step is to narrow. The problem is reduced to its smallest instance. The fifth step is to isolate. One variable is changed and the result observed. The sixth step is to fix. The fix should not be a broad intervention that extends beyond the identified root cause. The seventh step is to document. Dörner (1996) shows in his work on failure in complex systems that most failures arise from failing to see side effects and delayed consequences. Documentation prevents the same problem from feeling unfamiliar the second time it appears.

The value of these seven steps is that they give the researcher a sequence to follow in a moment of panic. Troubleshooting, through this sequence, ceases to be an emotional reaction and becomes a record-based reasoning process.

| Step | Name | Question | Pólya phase |
|---|---|---|---|
| 1 | Be skeptical | Is the first explanation correct, or merely the easiest one? | Understand |
| 2 | Capture the record | What exactly does the error message, log, screenshot, or output say? | Understand |
| 3 | Reproduce | Can the problem be reproduced reliably? | Understand |
| 4 | Narrow | What is the smallest example that triggers the problem? | Plan |
| 5 | Isolate | Which single variable opens or closes the problem? | Plan |
| 6 | Fix | What is the smallest correct change? | Execute |
| 7 | Document | How will the root cause and solution be recorded for the next researcher? | Look back |

## 6. The Recovery Record and the Incident Log

Troubleshooting is not only solving the problem. It is getting the solution into the archive. Because the same error most often does not happen only once. The context limit recurs. The DOI error recurs. The library access problem recurs. The wrong directory recurs. Rather than reasoning from scratch each time, the first solution should generate a record.

That record need not be long. If it is long, it will not be used. A good incident log is short, dated, and reapplicable. It states what the problem was, which layer it belonged to, how it was reproduced, what the root cause was, which solution worked, and what preventive step was added.

This incident log is the archive's troubleshooting memory. When a tool error is resolved, it is not only today's session that is saved. The future researcher is protected as well. Most often that future researcher is you, returning to the same archive six months later.

## 7. Regional Infrastructure Problems

Some problems originate not in the tool itself but in the geographic and institutional infrastructure from which the researcher works. In Türkiye, some international services may intermittently slow down, payment and access channels may be interrupted, and institutional library proxies may behave differently across universities. In Greece — particularly in institutions around Komotini — off-campus access, HEAL Link, proxy configuration, and connection quality can directly affect the research experience.

In these situations, what looks like a tool problem is actually a network problem. The model times out, but the actual cause is the connection. The catalog returns empty, but the actual cause is that off-campus access has dropped. The full text cannot be downloaded, but the problem is not Claude Code — it is the publisher's access wall.

With regional problems the first step is to test the connection and access layer before blaming the tool. Does the same operation work from a different network? Is the institutional VPN active? Has the EZproxy session timed out? Does the catalog open in a browser? Until these questions are answered, passing judgment on the model's behavior is premature.

## 8. The GitHub Issue Template: Helping Someone Else

Troubleshooting is not only solving your own problem. A well-documented problem also helps the next researcher who encounters the same failure. In the open-source ecosystem a good issue converts an individual breakdown into shared knowledge. Carrying a problem alone, rather than putting it on record, is both slower and less academically sound.

Vaughan (1996), studying the Challenger decision, shows that systemic failures most often arise not from a single large error but from the accumulation of small, visible — yet unshared — deviations. Perrow (1999) analyzes a similar structure in high-risk technologies. The scale of risk in a social scientist's archive with Claude Code bears no comparison to those contexts. But the principle holds. When small deviations are not made visible, the community repeats the same error.

Suggested issue template:

**Problem title.** Short, single line.

**Version.** Claude Code version, operating system, installation path.

**Expected.** What did you expect to happen?

**Actual.** What happened?

**Reproduction steps.**

1. ...

2. ...

3. ...

**Relevant log or error message.**

```
error log here
```

**Previously tried.** Which solutions did not work?

**Problem category.** Tool, knowledge, communication, or uncertain.

**Privacy check.** Confirmed that no personal data, clinical data, or credentials appear in the logs.

The strength of this template is that filling it compels the reporter to think. Writing the gap between expected and actual clarifies the problem. Listing the reproduction steps tests whether the problem is genuinely reproducible. Writing what was previously tried prevents whoever offers help from walking the same dead ends. The privacy check is indispensable in clinical and human-subjects research contexts. No log, no screenshot, no error message should leak personal data.

## 9. Worked Troubleshooting Scenarios

The examples in this section are not drawn from real incidents. They are synthetic scenarios consistent with the archive sanitization protocol. Each one, however, represents a real class of problem the social science researcher may encounter while working with Claude Code.

### Scenario 1. The Rebuttal File Opens in the Wrong Version

Symptom: the author opens the revision file and sees that some changes have disappeared. The first explanation may be that the file is corrupted. The seven-step protocol proceeds more calmly. First, the record is captured: the file name, the date, the folder path, the last-modified timestamp, and any available cloud sync history. Then the problem is reproduced: does the same file appear in the older version on a different device as well? Then it is narrowed: is the problem in the file, in the cloud sync, or in the wrong folder? The root cause is most often that the same file exists in two folders in two different versions. The solution is to identify the single authoritative file, archive the other, and add a versioning naming convention to the revision folder.

### Scenario 2. The Citation Verification Flow Quietly Produces a Faulty Record

Symptom: the bibliography looks formally correct, but a journal name differs from what was expected. The first explanation may be a minor APA style variant. The protocol does not accept that. The input and output are recorded. The same source is reprocessed, and if the same error appears, the problem is reproducible. A single source is tested in isolation. The journal name field is isolated. The root cause may be that the container-title field returned by the API is incorrect or incomplete. The smallest correct fix is to add a publisher-page cross-check to the record-matching step.

### Scenario 3. The Model Tries the Same Transformation Repeatedly

Symptom: a data file is to be cleaned. The model runs the command, receives an error, and tries the same transformation again. The loop does not advance. The problem is not the model's effort. The assumption is wrong. The file is not in the expected format. The researcher stops the loop and changes the command. Not "try the transformation again" — rather: "do not attempt the transformation yet; first diagnose the file structure: report the delimiter, encoding, and header row." This move breaks the loop. The researcher has asked for observation, not repetition.

### Scenario 4. The Conference Presentation Will Not Open on Stage

Symptom: the presentation file appears corrupted on the projector's computer. This too falls within the troubleshooting protocol. First the record is captured: in which format, in which version, on which device did it not open? Then it is narrowed: does the PDF version open? Does the local copy open? Is the cloud connection down? The solution is most often a triple backup prepared in advance — PPTX, PDF, and a single-page summary slide. A presentation is a live performance. In live performance, troubleshooting is as much about the backup system built beforehand as about technical skill in the moment.

## 10. Closing: The Last Line of the Series

This booklet is the closing booklet of the v1.0 manifesto. Throughout the guide a single thesis was worked. Claude Code gains meaning for the social scientist as a methodological partner in academic production only within a framework, a discipline, and an ethics. The first booklet asked what the tool is. The last booklet asks what to do when the tool fails.

That choice of close is deliberate. Because the real value of a guide is understood not when everything is working but when something goes wrong. When the installation is running, everyone feels competent. When the archive is tidy, everyone is orderly. When sources are being verified, everyone is rigorous. The real test begins when the error message arrives, when the source cannot be found, when the model enters a loop, and when time is running short.

That troubleshooting is a reasoning framework rather than an error list is the final extension of the approach this guide defended from beginning to end. Lists age with the tools that generate them. Frameworks outlast any particular version. When all the booklets in this series are read together, what the social science researcher holds is not a formula that solves every problem. It is something more valuable: an academic working discipline that shows what can be delegated and what cannot, what must be recorded and what need not be, and where to begin when things go wrong.

The rest is the test of practice.

## References

Citations are in APA 7 format. All references verified against Crossref and publisher records on 2026-06-21. All book ISBNs confirmed against publisher records.

Dörner, D. (1996). *The logic of failure: Why things go wrong and what we can do to make them right*. Metropolitan Books. ISBN 978-0-8050-4160-6

Norman, D. A. (2013). *The design of everyday things* (Revised and expanded ed.). Basic Books. ISBN 978-0-465-05065-9

Perrow, C. (1999). *Normal accidents: Living with high-risk technologies* (Updated ed.). Princeton University Press. ISBN 978-0-691-00412-9

Pólya, G. (2014). *How to solve it: A new aspect of mathematical method*. Princeton University Press. (Original work published 1945). ISBN 978-0-691-16407-6

Reason, J. (2000). Human error: Models and management. *BMJ*, *320*(7237), 768–770. https://doi.org/10.1136/bmj.320.7237.768

Schoenfeld, A. H. (1985). *Mathematical problem solving*. Academic Press. ISBN 978-0-12-628870-4

Vaughan, D. (1996). *The Challenger launch decision: Risky technology, culture, and deviance at NASA*. University of Chicago Press. ISBN 978-0-226-85176-1

---

**Booklet ID.** `012-01-0001`
**Version.** `0.2.0`
**Date.** 2026-06-21
**License.** This booklet is licensed under CC BY-NC-SA 4.0. https://creativecommons.org/licenses/by-nc-sa/4.0/
**Word count (approx.).** 3174 (English body text, measured with wc)
**Verified citations.** 7
**Fabricated citations.** 0
**Previous booklet.** [`010-01-0001`](../../010-peer-review/010-01-0001/en.md). Rebuttal Letters with Traceability Matrices
**Next booklet.** None. This is the closing booklet of the v1.0 manifesto. The roadmap extends with category 005 (Hooks), 006 (MCP), and 008 (Data Analysis) in the v1.5 and v2.0 versions.
