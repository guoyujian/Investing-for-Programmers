#!/usr/bin/env python3
"""Add lightweight highlights and note comments to selected PDF passages."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import fitz


DEFAULT_COLOR = (1.0, 0.92, 0.45)
SEARCH_FLAGS = (
    fitz.TEXT_DEHYPHENATE
    | fitz.TEXT_PRESERVE_WHITESPACE
    | fitz.TEXT_PRESERVE_LIGATURES
    | fitz.TEXT_MEDIABOX_CLIP
)


def load_spec(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def candidate_snippets(item: dict) -> list[str]:
    variants = [item["snippet"], *item.get("alt_snippets", [])]
    normalized = []
    for text in variants:
        normalized.append(text)
        normalized.append(text.replace("’", "'"))
        normalized.append(text.replace("“", "\"").replace("”", "\""))
        normalized.append(
            text.replace("’", "'").replace("“", "\"").replace("”", "\"")
        )

    deduped = []
    seen = set()
    for text in normalized:
        if text not in seen:
            seen.add(text)
            deduped.append(text)
    return deduped


def add_annotations(pdf_path: Path, spec_path: Path, output_path: Path) -> int:
    spec = load_spec(spec_path)
    doc = fitz.open(pdf_path)
    added = 0

    for item in spec["annotations"]:
        page_number = item["page"]
        snippet = item["snippet"]
        comment = item.get("comment", "")
        page = doc.load_page(page_number - 1)
        rects = []
        for candidate in candidate_snippets(item):
            rects = page.search_for(candidate, flags=SEARCH_FLAGS)
            if rects:
                break

        if not rects:
            raise ValueError(f"Snippet not found on page {page_number}: {snippet}")

        annot = page.add_highlight_annot(rects)
        annot.set_colors(stroke=item.get("color", DEFAULT_COLOR))
        annot.set_info(
            title=item.get("title", "Codex pre-read"),
            content=comment,
            subject=item.get("subject", "Pre-read cue"),
        )
        annot.update()
        added += 1

    output_path.parent.mkdir(parents=True, exist_ok=True)
    doc.save(output_path, garbage=4, deflate=True)
    doc.close()
    return added


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("pdf", help="Source PDF path")
    parser.add_argument("spec", help="JSON file describing annotations")
    parser.add_argument("output", help="Output PDF path")
    args = parser.parse_args()

    count = add_annotations(Path(args.pdf), Path(args.spec), Path(args.output))
    print(f"Added {count} annotations to {args.output}")


if __name__ == "__main__":
    main()
