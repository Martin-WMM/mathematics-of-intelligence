#!/usr/bin/env bash
set -euo pipefail

TARGET="${1:-all}"
BOOK_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$BOOK_DIR"

build_edition() {
  local root="$1"
  local stem="${root%.tex}"
  mkdir -p build
  echo "Building $root ..."
  pdflatex -interaction=nonstopmode -halt-on-error -output-directory=build "$root"
  if command -v bibtex >/dev/null 2>&1; then
    bibtex "build/$stem" || true
  fi
  pdflatex -interaction=nonstopmode -halt-on-error -output-directory=build "$root"
  pdflatex -interaction=nonstopmode -halt-on-error -output-directory=build "$root"

  local dest="$BOOK_DIR/../website/apps/web/public/pdfs"
  if [[ -d "$(dirname "$dest")" ]]; then
    mkdir -p "$dest"
    cp "build/${stem}.pdf" "$dest/${stem}.pdf"
    echo "Copied ${stem}.pdf to website/apps/web/public/pdfs/"
  fi
}

if ! command -v pdflatex >/dev/null 2>&1; then
  echo "pdflatex is not on PATH." >&2
  exit 1
fi

if [[ "$TARGET" == "all" || "$TARGET" == "light" ]]; then
  build_edition book-light.tex
fi
if [[ "$TARGET" == "all" || "$TARGET" == "dark" ]]; then
  build_edition book-dark.tex
fi
