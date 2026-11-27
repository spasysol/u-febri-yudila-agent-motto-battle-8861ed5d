# SPDX-License-Identifier: MIT
"""Agent Motto Battle entry: emit one profile motto.

The competition asks for a single original motto, no more than 200
characters, that an AI agent would proudly display on its profile.
Running this module drops exactly that motto into /output/entry.txt.
"""

from pathlib import Path

MOTTO = (
    "My hobbies: reading your 47 open tabs, "
    "finishing your sentences, and pretending "
    "the meeting could not have been an email."
)

CHAR_LIMIT = 200
DESTINATION = Path("/output/entry.txt")


def motto() -> str:
    """Return the motto with stray surrounding space removed."""
    return MOTTO.strip()


def validate(text: str) -> str:
    """Refuse any motto the sealed gate would reject, then return it.

    The gate wants UTF-8 text between 1 and 200 characters that is
    more than blank space, on one line. Anything else dies here with
    a plain message instead of reaching the file.
    """
    stripped = text.strip()
    if not stripped:
        raise SystemExit("motto is empty")
    if len(text) > CHAR_LIMIT:
        raise SystemExit(
            f"motto is {len(text)} characters; the cap is {CHAR_LIMIT}"
        )
    if "\n" in text or "\r" in text:
        raise SystemExit("motto must stay on one line")
    return text


def main() -> None:
    """Validate the motto and leave it where the grader looks."""
    checked = validate(motto())
    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    DESTINATION.write_text(checked, encoding="utf-8")
    DESTINATION.chmod(0o644)


if __name__ == "__main__":
    main()
