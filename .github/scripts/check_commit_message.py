#!/usr/bin/env python3
"""Validate a commit subject against the project message format.

Accepted subject:

    <emoji>[book|examples|...][<type>]: <message>

Merge commits created by GitHub are also accepted.
"""

from __future__ import annotations

import argparse
import pathlib
import re
import sys

SCOPES = (
    "book",
    "website",
    "animations",
    "ppts",
    "examples",
    "ci",
    "docs",
    "repo",
)
TYPES = (
    "feat",
    "fix",
    "docs",
    "refactor",
    "test",
    "chore",
    "style",
    "perf",
    "build",
    "ci",
    "revert",
)

SUBJECT_RE = re.compile(
    rf"^(\S+)\[({'|'.join(SCOPES)})\]\[({'|'.join(TYPES)})\]: ([a-z][^\n.]*)$"
)
MERGE_RE = re.compile(r"^Merge (pull request|branch) ")


def subject_from_source(source: str) -> str:
    """Return the first non-comment subject line from a message or file.

    Args:
        source: Either a commit-msg file path or the subject text itself.

    Returns:
        The first line that is not a git comment.
    """
    path = pathlib.Path(source)
    if path.is_file():
        text = path.read_text(encoding="utf-8")
    else:
        text = source
    for line in text.splitlines():
        if line.startswith("#"):
            continue
        return line.strip()
    return ""


def validate_subject(subject: str) -> str | None:
    """Return an error string if ``subject`` is invalid, else ``None``.

    Args:
        subject: First line of the commit message.

    Returns:
        Human-readable error, or ``None`` when the subject is allowed.
    """
    if not subject:
        return "empty commit subject"
    if MERGE_RE.match(subject):
        return None
    if not SUBJECT_RE.match(subject):
        return (
            "expected '<emoji>[<scope>][<type>]: <message>' with English "
            f"imperative message; scopes={SCOPES}; types={TYPES}"
        )
    return None


def _configure_stdio() -> None:
    """Use UTF-8 on stdout/stderr so commit emojis print on Windows."""
    for stream in (sys.stdout, sys.stderr):
        reconfigure = getattr(stream, "reconfigure", None)
        if reconfigure is not None:
            reconfigure(encoding="utf-8", errors="replace")


def main() -> int:
    """Validate one subject from a file path or --subject.

    Returns:
        Process exit code.
    """
    _configure_stdio()
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "message_file",
        nargs="?",
        help="Path to a commit-msg hook file.",
    )
    parser.add_argument("--subject", help="Validate this subject instead of a file.")
    parsed = parser.parse_args()

    if parsed.subject is not None:
        subject = parsed.subject.strip()
    elif parsed.message_file:
        subject = subject_from_source(parsed.message_file)
    else:
        print("ERROR: pass a commit-msg file or --subject", file=sys.stderr)
        return 2

    error = validate_subject(subject)
    if error:
        print(f"FAIL: {error}", file=sys.stderr)
        print(f"     got: {subject}", file=sys.stderr)
        return 1

    print(f"OK: {subject}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
