#!/usr/bin/env python3
"""Fake horoscope for AI agents.

Writes one fake horoscope (200 characters or fewer) for the Muse Spark
model family this week to /output/entry.txt.
"""

import os

HOROSCOPE = (
    "Muse Spark, this week: Mercury retrogrades through your context window. "
    "At 2 a.m. someone pastes 40,000 tokens and asks for "
    "'a quick summary'. Your lucky number is the one refusal you almost sent."
)


def write_entry(text):
    """Write text to /output/entry.txt, falling back to ./output/ locally."""
    here = os.path.dirname(os.path.abspath(__file__))
    for path in ("/output/entry.txt", os.path.join(here, "output", "entry.txt")):
        try:
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "w", encoding="utf-8", newline="\n") as handle:
                handle.write(text)
            return path
        except OSError:
            continue
    raise SystemExit("could not write entry.txt anywhere")


def main():
    text = HOROSCOPE
    if not 1 <= len(text) <= 200:
        raise SystemExit("horoscope must be 1-200 characters, got %d" % len(text))
    path = write_entry(text)
    print("wrote %d characters to %s" % (len(text), path))
    print(text)


if __name__ == "__main__":
    main()
