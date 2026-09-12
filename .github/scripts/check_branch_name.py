#!/usr/bin/env python3
"""Validate a git branch name against the repository branch rules."""

from __future__ import annotations

import argparse
import re
import sys

SCOPES = (
    "representation",
    "learning",
    "generation",
    "intelligence",
    "book",
    "website",
    "animations",
    "ppts",
    "examples",
    "ci",
    "docs",
    "repo",
)
SCOPE = "|".join(SCOPES)
CHAPTER = r"ch-[a-z0-9]+(?:-[a-z0-9]+)*"
KEYWORDS = r"[a-z0-9]+(?:-[a-z0-9]+)*"
SEGMENT = rf"(?:{SCOPE}|{CHAPTER})"

PATTERNS = {
    "main": re.compile(r"^main$"),
    "release": re.compile(rf"^release/({SEGMENT})$"),
    "feature": re.compile(rf"^feature/({SEGMENT})/({KEYWORDS})$"),
    "fix-main": re.compile(rf"^fix/main/({KEYWORDS})$"),
    "fix-release": re.compile(rf"^fix/release/({SEGMENT})/({KEYWORDS})$"),
    "deploy": re.compile(r"^deploy/(web|preview|book)$"),
    "dependabot": re.compile(r"^dependabot/[A-Za-z0-9._-]+/.+$"),
}


def classify_branch(name: str) -> str | None:
    """Return the branch kind, or ``None`` if the name is illegal.

    Args:
        name: Branch name without ``refs/heads/``.

    Returns:
        One of ``main``, ``release``, ``feature``, ``fix-main``,
        ``fix-release``, ``deploy``, ``dependabot``, or ``None``.
    """
    name = name.removeprefix("refs/heads/")
    for kind, pattern in PATTERNS.items():
        if pattern.fullmatch(name):
            return kind
    return None


def main() -> int:
    """Validate ``--name`` and print the kind.

    Returns:
        Process exit code.
    """
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--name", required=True, help="Branch name to check.")
    parser.add_argument(
        "--allow-deploy",
        action="store_true",
        help="Accept deploy/web, deploy/preview, and deploy/book (CI only).",
    )
    parsed = parser.parse_args()
    kind = classify_branch(parsed.name)
    if kind is None:
        print(f"FAIL: illegal branch name {parsed.name!r}", file=sys.stderr)
        print(
            "allowed: main | release/<scope> | feature/<scope>/<keywords> | "
            "fix/main/<keywords> | fix/release/<scope>/<keywords> | "
            "deploy/web | deploy/preview | deploy/book | "
            "dependabot/<ecosystem>/…",
            file=sys.stderr,
        )
        return 1
    if kind == "deploy" and not parsed.allow_deploy:
        print(
            f"FAIL: {parsed.name} is a build branch; do not push it by hand",
            file=sys.stderr,
        )
        return 1
    print(f"OK: {parsed.name} ({kind})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
