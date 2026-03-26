---
name: book-chapter-launch
description: Start a new chapter in the Investing-for-Programmers study workspace. Use when entering a chapter for the first time, preparing a pre-read outline, extracting PDF structure or sample pages, creating the initial chapter note and handout, or updating 学习进度.md with a started or waiting-to-read state.
---

# Book Chapter Launch

Start the chapter with a repeatable workflow, not a one-off summary.

## Workflow

1. Read the local project rules first.
   - Read `AGENTS.md`.
   - Read `学习进度.md` to see the current chapter state.
   - Skim the most recent neighboring chapter note and handout to match naming and tone.

2. Build chapter context from the source PDF.
   - Use the `common` conda environment for PDF parsing.
   - Extract:
     - chapter title and section outline
     - key sample pages
     - important figures, tables, listings, and summary pages when available
   - In the chapter note, record the information source using the project's standard labels:
     - direct PDF parsing
     - chapter outline extraction
     - sample page extraction
     - fallback

3. Create or update the chapter note first.
   - Follow the project's established file naming pattern such as `notes/ch11_algorithmic_trading.md`.
   - Include:
     - chapter overview
     - key concepts
     - questions the learner should be able to answer
     - terms to watch
     - relation to programmer skills
     - section-by-section pre-read notes
   - Add original PDF positions for important figures, tables, examples, formulas, and listings whenever available.

4. Create the chapter handout immediately after the note.
   - The handout is for first-pass reading and should lower the barrier to entry.
   - Preserve the chapter's important example chain instead of reducing everything to abstract concepts.
   - Point the reader back to the original with PDF page numbers and figure or listing ids.

5. Update tracking documents.
   - Update `学习进度.md`.
   - If the user has not chosen a reading mode yet, mark the chapter as:
     - handout generated, waiting for first-pass skim or original deep read
   - If the user explicitly chose a reading mode, record it exactly.
   - Add a placeholder section in `问答笔记.md` only when the chapter does not already have one.

## Output Rules

- Default to Simplified Chinese.
- Keep English terms when translation would reduce precision.
- Use the project's two-track model:
  - chapter note for long-term accumulation
  - handout for first-pass teaching
- Do not claim a chapter is complete unless the user actually finished that pass.
- Do not skip original-position markers for important examples or visual elements.

## References

- Read [workspace-files.md](./references/workspace-files.md) before creating or renaming files.
