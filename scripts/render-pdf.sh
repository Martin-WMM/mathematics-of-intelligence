#!/usr/bin/env bash
# Render the book PDFs from the repository root.
# Usage: ./scripts/render-pdf.sh [all|light|dark]
set -euo pipefail

TARGET="${1:-all}"
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
BUILD="$REPO_ROOT/book/scripts/build.sh"

if [[ ! -f "$BUILD" ]]; then
  echo "Book build script not found: $BUILD" >&2
  exit 1
fi

exec "$BUILD" "$TARGET"
