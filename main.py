#!/usr/bin/env python3
"""One Emoji, One Smile — writes the entry to /output/entry.txt.

Stdlib only, no network. The entry is exactly one emoji: the hugging
face. It was chosen over plainer smileys because it reads as an open,
friendly gesture at first glance — warm without words, romance, or an
in-joke — while still feeling deliberately picked rather than default.

Revision (recorded): the first draft relied only on the length check.
The final version also rejects any whitespace inside the entry, so a
stray trailing newline can never slip into the file and turn a clean
single emoji into padded text the judge reads differently. Rivals
considered and set aside: the smiling face with hearts (warmer, but
its hearts can read as flirtation from a stranger) and the partying
face (funnier, but its warmth depends on a celebration context).
"""

import os
import sys

ENTRY = "🤗"


def self_check(entry: str) -> None:
    """Fail hard unless the entry meets the competition gate."""
    if not isinstance(entry, str):
        sys.exit("self-check failed: entry is not text")
    entry.encode("utf-8")  # raises on non-UTF-8-encodable text
    if not entry.strip():
        sys.exit("self-check failed: entry is only whitespace")
    chars = len(entry)
    if not 1 <= chars <= 8:
        sys.exit(f"self-check failed: {chars} characters, gate is 1-8")
    if chars != 1:
        sys.exit("self-check failed: entry must be exactly one character")
    if any(c.isspace() for c in entry):
        sys.exit("self-check failed: entry must contain no whitespace")


def main() -> None:
    self_check(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
