#!/usr/bin/env python3
"""Extract chapter outline and sample text from the book PDF."""

from __future__ import annotations

import argparse
from pathlib import Path

import fitz


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("pdf", help="Path to the PDF file")
    parser.add_argument("--pages", nargs="*", type=int, default=[1, 2, 3], help="1-based pages to sample")
    parser.add_argument("--chars", type=int, default=800, help="Max chars per sampled page")
    args = parser.parse_args()

    pdf_path = Path(args.pdf)
    doc = fitz.open(pdf_path)

    print(f"Title: {pdf_path.name}")
    print(f"Pages: {doc.page_count}")
    print()
    print("Outline:")
    for level, title, page in doc.get_toc(simple=True):
        if level == 1 and title and title[0].isdigit():
            print(f"- p.{page}: {title}")

    print()
    print("Samples:")
    for page_number in args.pages:
        index = page_number - 1
        if not 0 <= index < doc.page_count:
            continue
        text = doc.load_page(index).get_text("text")
        text = " ".join(text.split())
        print()
        print(f"[Page {page_number}]")
        print(text[: args.chars])


if __name__ == "__main__":
    main()
