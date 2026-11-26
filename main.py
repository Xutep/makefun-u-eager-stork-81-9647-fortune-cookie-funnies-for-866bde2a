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

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(FORTUNE)


if __name__ == "__main__":
    main()
