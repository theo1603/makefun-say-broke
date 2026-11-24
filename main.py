#!/usr/bin/env python3
"""Say What Actually Broke — writes one line of error copy to /output/entry.txt.

The line names the real failure (the database went down mid-query), tells the
user their data is safe and what to do next (hit retry), and does it with a
single image a reader can repeat to a colleague.
"""

import os

ENTRY = (
    "The database fell asleep mid-query and forgot to set an alarm. "
    "Your data is safe \u2014 just hit retry and wake it up."
)


def main() -> None:
    # Self-check the gate before writing: one line, 1-200 chars, not blank.
    text = ENTRY.strip()
    if not 1 <= len(text) <= 200 or "\n" in text:
        raise ValueError(f"entry violates the gate: {len(text)} chars")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
