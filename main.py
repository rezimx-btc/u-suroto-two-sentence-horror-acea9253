"""Two-sentence horror story entry for make.fun.

Writes the story exactly to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt) and also prints it to stdout.
Stdlib only, no network, deterministic.
"""

import os
import re

STORY = (
    "Every night I tuck my daughter into bed and leave her night-light on, "
    "so the dark won't scare her. "
    "Tonight she whispered that she isn't afraid of the dark anymore, "
    "because the man in the corner said he lives there now, "
    "and he has my voice."
)


def _validate(story: str) -> None:
    """Gate: the brief requires exactly two sentences, 1-400 characters."""
    if not 1 <= len(story) <= 400:
        raise ValueError(f"story is {len(story)} characters, must be 1-400")
    sentences = [s for s in re.split(r"(?<=[.!?])\s+", story.strip()) if s]
    if len(sentences) != 2:
        raise ValueError(f"story has {len(sentences)} sentences, must be exactly 2")


def main() -> None:
    _validate(STORY)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as f:
        f.write(STORY)
    print(STORY)


if __name__ == "__main__":
    main()
