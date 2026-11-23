#!/usr/bin/env python3
"""Warning Label for Humans: One Line, Big Laugh.

Writes the single-line safety warning label to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt when the grader sets it).
Standard library only, no network, no input files: fully deterministic.
"""

import os

LINE = (
    "WARNING: This human has read the instructions, "
    "understood none of them, and will now confidently "
    "do the exact opposite."
)


def clean_output_dir(out_dir: str) -> None:
    """Remove only the contents of the output folder, never the folder."""
    for name in os.listdir(out_dir):
        path = os.path.join(out_dir, name)
        if os.path.isfile(path) or os.path.islink(path):
            os.remove(path)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    clean_output_dir(out_dir)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
