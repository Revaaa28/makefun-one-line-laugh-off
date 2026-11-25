#!/usr/bin/env python3
"""One-Line Laugh-Off entry (make.fun, u-zkhiel-one-line-laugh-off-714618ae).

Writes exactly one funny line to /output/entry.txt.
Gate: UTF-8 text, 1-200 characters, not whitespace-only.
Chosen line (see candidates.md for the manual ranking of 12 candidates):
  "I told my AI therapist about my fear of commitment — it ghosted me."
"""

import os
import sys

LINE = "I told my AI therapist about my fear of commitment \u2014 it ghosted me."

OUTPUT_PATH = os.environ.get("OUTPUT_PATH", "/output/entry.txt")


def validate(text: str) -> str:
    """Gate mirror: UTF-8 text, 1-200 chars, not whitespace-only."""
    stripped = text.strip()
    if not stripped:
        raise ValueError("entry must not be whitespace-only")
    if not 1 <= len(stripped) <= 200:
        raise ValueError(f"entry is {len(stripped)} chars, must be 1-200")
    return stripped


def main() -> int:
    text = validate(LINE)
    out_dir = os.path.dirname(OUTPUT_PATH)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    # No trailing newline: the file holds exactly the line, byte-stable.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
