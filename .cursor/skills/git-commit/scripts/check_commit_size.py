#!/usr/bin/env python3
"""Delegate to the repository commit size check.

``CHANGELOG.md`` is included. There is no exclusion list.
"""

from __future__ import annotations

import pathlib
import subprocess
import sys


def main() -> int:
    """Run ``.github/scripts/check_commit_size.py`` with the same arguments.

    Returns:
        Process exit code from the shared checker.
    """
    repo_root = pathlib.Path(__file__).resolve().parents[4]
    target = repo_root / ".github" / "scripts" / "check_commit_size.py"
    if not target.is_file():
        print(f"ERROR: missing {target}", file=sys.stderr)
        return 2
    return subprocess.call([sys.executable, str(target), *sys.argv[1:]])


if __name__ == "__main__":
    sys.exit(main())
