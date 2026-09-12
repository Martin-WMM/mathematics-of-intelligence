#!/usr/bin/env python3
"""Lint commit messages and sizes for every non-merge commit in a range."""

from __future__ import annotations

import argparse
import pathlib
import subprocess
import sys

_SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
if str(_SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPT_DIR))

from check_commit_message import validate_subject
from check_commit_size import MAX_LINES, count_commit_lines


def commits_in_range(revision_range: str) -> list[str]:
    """List non-merge commit SHAs from oldest to newest.

    Args:
        revision_range: A git revision range such as ``abc..def``.

    Returns:
        Commit SHAs. Empty if the range has no unique non-merge commits.
    """
    result = subprocess.run(
        ["git", "rev-list", "--reverse", "--no-merges", revision_range],
        capture_output=True,
        text=True,
        check=True,
    )
    return [line.strip() for line in result.stdout.splitlines() if line.strip()]


def subject_of(commit: str) -> str:
    """Return the subject line of ``commit``.

    Args:
        commit: Commit SHA.

    Returns:
        First line of the commit message.
    """
    result = subprocess.run(
        ["git", "log", "-1", "--format=%s", commit],
        capture_output=True,
        text=True,
        check=True,
    )
    return result.stdout.strip()


def _configure_stdio() -> None:
    """Use UTF-8 on stdout/stderr so commit emojis print on Windows."""
    for stream in (sys.stdout, sys.stderr):
        reconfigure = getattr(stream, "reconfigure", None)
        if reconfigure is not None:
            reconfigure(encoding="utf-8", errors="replace")


def main() -> int:
    """Validate every non-merge commit in ``--range``.

    Returns:
        Process exit code.
    """
    _configure_stdio()
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--range",
        required=True,
        help="Git revision range, for example origin/main..HEAD",
    )
    parsed = parser.parse_args()

    try:
        shas = commits_in_range(parsed.range)
    except subprocess.CalledProcessError as exc:
        print(f"ERROR: git rev-list failed: {exc.stderr.strip()}", file=sys.stderr)
        return 2

    if not shas:
        print(f"OK: no non-merge commits in {parsed.range}")
        return 0

    failed = False
    for sha in shas:
        subject = subject_of(sha)
        message_error = validate_subject(subject)
        try:
            size = count_commit_lines(sha)
        except subprocess.CalledProcessError as exc:
            print(f"FAIL: {sha[:8]} git diff failed: {exc.stderr.strip()}", file=sys.stderr)
            failed = True
            continue
        if message_error:
            print(f"FAIL: {sha[:8]} message: {message_error} ({subject})", file=sys.stderr)
            failed = True
        if size > MAX_LINES:
            print(
                f"FAIL: {sha[:8]} is {size} lines (limit {MAX_LINES}); "
                "CHANGELOG.md counts",
                file=sys.stderr,
            )
            failed = True
        if not message_error and size <= MAX_LINES:
            print(f"OK: {sha[:8]} {size}/{MAX_LINES} {subject}")

    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
