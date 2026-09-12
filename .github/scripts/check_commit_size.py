#!/usr/bin/env python3
"""Validate that a git diff does not exceed the 500-line commit limit.

``CHANGELOG.md`` is included. There is no exclusion list.
"""

from __future__ import annotations

import argparse
import subprocess
import sys

MAX_LINES = 500


def count_numstat(args: list[str]) -> int:
    """Return insertions plus deletions for a ``git diff --numstat`` command.

    Args:
        args: Git arguments after ``git``, including ``diff`` and ``--numstat``.

    Returns:
        Total changed lines. A binary file (``-`` in numstat) counts as one line.

    Raises:
        subprocess.CalledProcessError: If git exits non-zero.
        FileNotFoundError: If git is not on ``PATH``.
    """
    result = subprocess.run(
        ["git", *args],
        capture_output=True,
        text=True,
        check=True,
    )
    total = 0
    for line in result.stdout.splitlines():
        if not line.strip():
            continue
        parts = line.split("\t")
        if len(parts) < 2:
            continue
        added, deleted = parts[0], parts[1]
        if added == "-" or deleted == "-":
            total += 1
        else:
            total += int(added) + int(deleted)
    return total


def count_staged_lines() -> int:
    """Count changed lines in the staged index.

    Returns:
        Insertions plus deletions across all staged files, including
        ``CHANGELOG.md``.
    """
    return count_numstat(["diff", "--cached", "--numstat"])


def count_commit_lines(commit: str) -> int:
    """Count changed lines introduced by one commit.

    Args:
        commit: Commit SHA or revision.

    Returns:
        Insertions plus deletions against the commit's first parent, or
        against the empty tree for a root commit.
    """
    parents = subprocess.run(
        ["git", "rev-list", "--parents", "-n", "1", commit],
        capture_output=True,
        text=True,
        check=True,
    ).stdout.split()
    if len(parents) >= 2:
        return count_numstat(["diff", "--numstat", f"{parents[1]}", commit])
    empty = "4b825dc642cb6eb9a060e54bf8d69288fbee4904"
    return count_numstat(["diff", "--numstat", empty, commit])


def main() -> int:
    """Exit 0 if the selected diff is within the limit, else 1.

    Returns:
        Process exit code.
    """
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--commit",
        help="Check this commit instead of the staged index.",
    )
    parsed = parser.parse_args()

    try:
        total = count_commit_lines(parsed.commit) if parsed.commit else count_staged_lines()
    except subprocess.CalledProcessError as exc:
        print(f"ERROR: git diff failed: {exc.stderr.strip()}", file=sys.stderr)
        return 2
    except FileNotFoundError:
        print("ERROR: git is not installed or not on PATH", file=sys.stderr)
        return 2

    label = parsed.commit or "staged"
    if total == 0 and not parsed.commit:
        print("WARN: no staged changes (0 lines)")
        return 0

    if total > MAX_LINES:
        print(
            f"FAIL: {label} changes are {total} lines (limit: {MAX_LINES}). "
            "CHANGELOG.md counts. Split into smaller commits.",
            file=sys.stderr,
        )
        return 1

    print(f"OK: {total}/{MAX_LINES} lines ({label})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
