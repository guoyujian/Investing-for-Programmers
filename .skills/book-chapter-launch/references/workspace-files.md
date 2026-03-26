# Workspace Files

## Core Files

- `AGENTS.md`
  - Project-specific study workflow and writing rules.
- `学习进度.md`
  - Canonical source of chapter status and reading granularity.
- `问答笔记.md`
  - Cross-chapter Q&A accumulation.
- `全书总笔记.md`
  - Book-level synthesis and wrap-up.
- `notes/GLOSSARY.md`
  - Terms worth keeping in Chinese and English.

## Chapter File Pattern

- Chapter note:
  - `notes/chXX_<chapter_slug>.md`
- Chapter handout:
  - `notes/chXX_<chapter_slug>_handout.md`

## Note Expectations

- The chapter note is the long-lived document.
- The handout is the first-pass teaching guide.
- Both should link to each other.
- Important figures, tables, examples, formulas, and listings should carry PDF positions when possible.

## Progress Rules

- If the user only asked to initialize a chapter, do not mark the chapter as completed.
- If the user has not chosen reading granularity, mark it as waiting for the user's reading mode.
- If the user explicitly says they only read the handout, record that as first-round `简读 / 速览` rather than full completion.
