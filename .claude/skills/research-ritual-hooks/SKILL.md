---
name: research-ritual-hooks
description: Use when automating research session rituals in Claude Code with hooks, such as session-start context injection, daily research logging, session-end persistence, or pre-commit guards that block secrets and unverified citations.
---

# Research Ritual Hooks

## When to use

Use this skill when a recurring research habit should become an automatic part of the Claude Code session lifecycle: loading project context at start, appending to a daily log, persisting state at session end, or guarding commits. It pairs with the memory-vault-architect skill, which designs what the rituals read and write.

## Inputs

- The ritual to automate, described as a habit rather than a script.
- The vault or notes layout the ritual touches.
- Operating system and shell, since hook commands are environment specific.
- The user's tolerance for automation acting without confirmation.

## Workflow

1. Name the ritual before choosing the mechanism. A ritual that cannot be described in one sentence is not ready to automate.
2. Map the ritual to a lifecycle event: context loading to session start, logging and persistence to session end, guarding to the moment before a tool or commit runs.
3. Decide the failure direction deliberately. Context and logging hooks fail open, a broken logger must never block a session. Guard hooks fail closed, a broken secret scan must block the commit it cannot check.
4. Keep each hook script small enough to read in one screen, and let it write one log line saying what it did.
5. Let hooks read the vault freely and write only to designated locations, the daily note and the log, never restructuring content on their own.
6. Test with a dry run in isolation before registering the hook, and measure the session start delay it adds.
7. Version the hook scripts with the project, and document each hook in one line: trigger, input, output, failure direction.

## Output

Return:

- A ritual to hook-event map.
- The hook configuration and the script skeletons.
- The failure direction decision per hook, with the reason.
- A dry run test plan and its results.
- The one-line documentation block for the project README or CLAUDE.md.

## Verification

- Every hook has a recorded dry run result.
- The failure direction of every hook is explicit and matches its role, open for context and logging, closed for guards.
- No hook stores or echoes credentials, and secret material stays in environment stores.
- Measured session start delay is stated, and hooks that slow the start noticeably are trimmed or deferred.
- Each hook writes a log line per run, so silence means it did not run.

## Safety

A hook is automation that runs without asking, so destructive operations do not belong in ritual hooks. No deletion, no outbound network calls carrying vault content, no rewriting of notes. Guards may block actions, and that is the only force a ritual hook should apply.

## Example prompt

"Her oturum başında bugünün günlük notunu ve aktif proje kartını yüklesin, oturum sonunda yapılanları günlüğe eklesin, bunu hook'larla kur."

Expected smoke output:

- A two-ritual map, session start context injection and session end logging.
- Script skeletons with fail-open behavior and one-line logging.
- A dry run plan measuring start delay.

## Türkçe kullanım notu

Bu beceri, tekrarlanan araştırma alışkanlıklarını oturum yaşam döngüsüne bağlar. Ritüel önce tek cümleyle tanımlanır, sonra doğru olaya eşlenir ve her kancanın bozulma yönü bilinçli seçilir. Bağlam yükleyici bozulursa oturumu engellemez, gizlilik bekçisi bozulursa commit'i durdurur. Kancalar tek ekranda okunacak kadar küçük kalır, her çalışmada tek satır iz bırakır ve arşiv içeriğini kendi başına yeniden düzenlemez.
