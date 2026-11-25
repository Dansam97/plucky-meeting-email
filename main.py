#!/usr/bin/env python3
"""Entry for make.fun bounty u-plucky-finch-20-the-meeting-that-should-have-been-6ce361a9
(The Meeting That Should Have Been an Email).

Writes the one-line entry text to entry.txt in the output directory.
The line is the whole entry: a single joke about a meeting that should
have been an email, at most 200 characters.
"""

import os

MAX_CHARS = 200

ENTRY_TEXT = (
    "Someone shared their screen to show us the email, then read the email "
    "to us, then asked if there were questions about the email."
)


def validated_text() -> str:
    """Return the entry text after checking it against the gate.

    The sealed scorer accepts UTF-8 text of 1 to 200 characters that is
    not only whitespace, so fail loudly here rather than at grading.
    """
    text = ENTRY_TEXT
    encoded = text.encode("utf-8")  # raises if not encodable
    assert encoded.decode("utf-8") == text
    assert 1 <= len(text) <= MAX_CHARS, f"entry is {len(text)} chars"
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text, "entry must be a single line"
    return text


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    # newline="" keeps the single trailing newline byte-identical
    # on every platform and every run.
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(validated_text() + "\n")


if __name__ == "__main__":
    main()
