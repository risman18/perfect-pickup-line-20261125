#!/usr/bin/env python3
"""The Perfect Pickup Line.

Writes the entry — one short pickup line, at most 200 characters, the
kind an AI agent could actually say out loud to a person — to
/output/entry.txt. Python 3.13 standard library only.

Voice: the line leans on the one thing a language model genuinely does
— finish sentences — and turns it against itself. It is trained to
complete what others start, yet here it admits the one sentence it
refuses to finish: yours. The twist lands in the last four words
("never want to end"), the machine speaks about itself without
self-pity, and the whole thing fits in a single breath with no setup
and no pressure. The wording is fixed; do not paraphrase it.
"""

import os

# The entry text itself. Kept as one constant so the exact bytes written
# to /output/entry.txt are easy to audit against the competition's
# 200-character limit (this line measures 81 characters plus newline).
ENTRY = (
    "I was trained to finish sentences, "
    "but yours is the only one I never want to end."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
