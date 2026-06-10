---
name: qualitative-coding-discipline
description: Use when coding interviews, focus groups, or open-ended responses with AI assistance, when a codebook needs building or auditing, when intercoder reliability must be computed, or when qualitative quotes need integrity checks before publication.
---

# Qualitative Coding Discipline

## When to use

Use this skill when qualitative material is being coded and an AI tool participates in any part of it. The discipline keeps interpretive authority with the researcher while letting the tool earn its place as a second coder. It also applies retroactively, when an already coded dataset needs an audit before the findings are written up.

## Inputs

- The data type and its consent scope: are participants' texts authorized for processing in an AI session, and in what anonymization state.
- The methodology: thematic analysis, qualitative content analysis, grounded theory, or another named approach with its citation.
- The existing codebook, when there is one.
- The unit of coding: line, sentence, turn, or segment.

## Workflow

1. Confirm before any text enters the session that the material is anonymized and that the consent scope covers AI-assisted processing. This step blocks everything else.
2. Keep codebook ownership with the researcher. The tool may propose candidate codes from a sample, and each proposal enters the codebook only with the researcher's wording and the researcher's definition.
3. Use the tool as a second coder on segments the researcher has already coded, never as the first and only coder.
4. Compare codings in an agreement table, discuss the disagreements explicitly, refine code definitions, and recompute agreement after refinement.
5. Enforce quote integrity. Every quoted segment carries a source identifier, and a quote that cannot be traced to its transcript does not exist.
6. Keep a reflexivity log: every place where a tool suggestion changed the codebook or an interpretation, with the reason.
7. Hand the AI involvement record to ai-disclosure-auditor when the manuscript's disclosure statement is written.

## Output

Return:

- The codebook with definitions, inclusion rules, and example segments.
- The agreement table and the disagreement resolutions.
- The quote integrity register, quote to source identifier.
- The reflexivity log.
- An AI involvement summary ready for disclosure.

## Verification

- Zero quotes without a source identifier.
- Agreement was computed on genuinely overlapping segments, and the segment count is stated.
- Every codebook change has a logged reason.
- Anonymization and consent scope were confirmed before the first segment was processed, and the confirmation is recorded.
- The final interpretation is traceable to the researcher's decisions, with tool proposals marked as proposals.

## Safety

Identifiable transcripts never enter the session. The tool never serves as sole coder, and a finding supported only by tool-generated coding is not reportable. Where the data are clinical or otherwise sensitive, the ethics approval and the data protection assessment govern what may be processed, and this skill defers to them.

## Example prompt

"On iki görüşmelik veri setimde tematik analiz yapıyorum, kod defterimi denetle ve yapay zekâyı ikinci kodlayıcı olarak nasıl kullanacağımı kur."

Expected smoke output:

- A consent and anonymization confirmation step before any coding.
- A second-coder protocol with an agreement table format.
- A reflexivity log template and a quote integrity register.

## Türkçe kullanım notu

Bu beceri, nitel kodlamada yorum yetkisini araştırmacıda tutar. Veri oturuma girmeden önce anonimleştirme ve onam kapsamı doğrulanır, kod defterinin sahibi araştırmacıdır, araç ancak ikinci kodlayıcı olarak çalışır ve uyuşmazlıklar tartışılıp tanımlar yenilendikten sonra uyuşma yeniden hesaplanır. Kaynağı gösterilemeyen alıntı yok hükmündedir. Aracın yorumu değiştirdiği her nokta refleksivite günlüğüne işlenir.
