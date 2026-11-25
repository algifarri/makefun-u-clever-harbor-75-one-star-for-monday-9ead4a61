#!/usr/bin/env python3
"""One Star for Monday — a one-star review of Monday as a restaurant.

Writes the review to /output/entry.txt (UTF-8, one line, 23 words,
116 characters). Deterministic, standard library only, no network.

The line: "One star. Monday sat me down at 7am, forgot my order,
served cold coffee, then charged me for a weekend I never got."

Why this line: it reads as a genuine diner's complaint — seated at a
table, an order forgotten, a cold dish, a bill that stings — while the
joke only works for Monday: seated at 7am, the first sitting of the
working week, and billed for the weekend that is already gone. No
other day of the week can be charged for a weekend it never served.
Short enough to retype into the group chat without trimming a word.
"""

import os

REVIEW = (
    "One star. Monday sat me down at 7am, forgot my order, "
    "served cold coffee, then charged me for a weekend I never got."
)
# One line, at most 25 words, 1 to 180 characters per the gate.


def main() -> None:
    words = REVIEW.split()
    assert len(words) <= 25, f"expected at most 25 words, got {len(words)}"
    assert 1 <= len(REVIEW) <= 180, (
        f"expected 1-180 characters, got {len(REVIEW)}"
    )
    assert REVIEW.strip() == REVIEW and REVIEW, (
        "entry must not be only whitespace"
    )
    assert "\n" not in REVIEW, "entry must be a single line"
    # The grader mounts /output; create it defensively for local runs too.
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(REVIEW)


if __name__ == "__main__":
    main()
