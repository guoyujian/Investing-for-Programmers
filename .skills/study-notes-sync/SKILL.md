---
name: study-notes-sync
description: Sync stable study outcomes back into the Investing-for-Programmers workspace documents. Use when a question has been answered, a chapter has been wrapped up, a reading state changed, or a concept should be propagated into 问答笔记.md, chapter notes, 学习进度.md, 全书总笔记.md, or notes/GLOSSARY.md.
---

# Study Notes Sync

Sync the answer into the right long-lived documents instead of leaving it only in chat.

## Workflow

1. Decide whether the answer is stable enough to persist.
   - Sync when the answer clarifies:
     - a recurring concept
     - an author's intended meaning
     - an important example
     - a reading-state update
     - a book-level conclusion
   - Skip syncing only for throwaway chatter or unstable drafts.

2. Choose the right destination documents.
   - Use `问答笔记.md` for direct question-answer accumulation.
   - Use the chapter note when the answer deepens chapter understanding.
   - Use `notes/GLOSSARY.md` for reusable terms.
   - Use `学习进度.md` for reading state or pass completion changes.
   - Use `全书总笔记.md` only for stable cross-chapter conclusions.

3. Prefer updating existing sections over creating duplicates.
   - Merge with nearby content.
   - Reorganize repeated points into clearer structure.
   - Keep stable conclusions, not chat chronology.

4. Preserve original meaning carefully.
   - If the answer depends on the author's wording, reconstruct the intent accurately first.
   - Keep short original snippets only when useful and compliant.
   - Do not replace precise meaning with an over-compressed Chinese slogan.

5. Reflect reading granularity honestly.
   - Record `精读`, `简读 / 速览`, or `跳过` as the user actually used them.
   - Do not promote a handout skim to full completion.

## Sync Rules

- Default to updating multiple documents when the answer is clearly reusable.
- Keep `问答笔记.md` and the chapter note aligned on important clarifications.
- If a term explanation is likely to recur, also update `notes/GLOSSARY.md`.
- If the answer changes what the learner has completed, update `学习进度.md` in the same pass.

## References

- Read [sync-targets.md](./references/sync-targets.md) before deciding where an answer belongs.
