#!/usr/bin/env python3
"""Validate that a pull request uses the allowed base branch for its head."""

from __future__ import annotations

import argparse
import pathlib
import sys

_SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
if str(_SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPT_DIR))

from check_branch_name import classify_branch


def allowed_bases(head_kind: str, head: str, base: str) -> bool:
    """Return whether ``head`` may target ``base``.

    Args:
        head_kind: Kind from :func:`classify_branch`.
        head: Head branch name.
        base: Base branch name.

    Returns:
        ``True`` if the pair matches the repository flow.
    """
    base_kind = classify_branch(base)
    if head_kind == "feature":
        scope = head.split("/")[1]
        return base == f"release/{scope}"
    if head_kind == "fix-main":
        return base == "main"
    if head_kind == "fix-release":
        if base_kind != "release":
            return False
        scope = head.split("/")[2]
        return base == f"release/{scope}"
    if head_kind == "release":
        return base == "main"
    if head_kind == "dependabot":
        return base == "main"
    if head_kind in {"main", "deploy"}:
        return False
    return False


def main() -> int:
    """Exit 0 if the head/base pair is allowed.

    Returns:
        Process exit code.
    """
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--head", required=True)
    parser.add_argument("--base", required=True)
    parsed = parser.parse_args()

    head_kind = classify_branch(parsed.head)
    if head_kind is None:
        print(f"FAIL: illegal head branch {parsed.head!r}", file=sys.stderr)
        return 1
    if classify_branch(parsed.base) is None and parsed.base != "main":
        print(f"FAIL: illegal base branch {parsed.base!r}", file=sys.stderr)
        return 1
    if parsed.base.startswith("deploy/"):
        print("FAIL: deploy branches are not PR targets", file=sys.stderr)
        return 1
    if not allowed_bases(head_kind, parsed.head, parsed.base):
        print(
            f"FAIL: {parsed.head} ({head_kind}) cannot target {parsed.base}",
            file=sys.stderr,
        )
        print(
            "flow: feature/* -> release/* ; "
            "fix/release/<scope>/* -> release/<scope> ; "
            "fix/main/* -> main ; release/* -> main ; "
            "dependabot/* -> main",
            file=sys.stderr,
        )
        return 1
    print(f"OK: {parsed.head} -> {parsed.base}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
