#!/usr/bin/env python3
"""Fortune Cookie Funnies for Engineers.

Writes a single original fortune-cookie line for a software engineer
to /output/entry.txt. Deterministic: no randomness, no network, no
input beyond this file, standard library only.
"""

import os

FORTUNE = (
    "The function you are afraid to touch is afraid of you too. "
    "It has no tests, and it knows it."
)

# The sealed scorer accepts 1 to 120 characters; refuse to write a
# longer line rather than ship an entry the gate would mark invalid.
MAX_LENGTH = 120

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    if not 1 <= len(FORTUNE) <= MAX_LENGTH:
        raise ValueError(
            f"fortune must be 1-{MAX_LENGTH} characters, got {len(FORTUNE)}"
        )
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(FORTUNE)


if __name__ == "__main__":
    main()
