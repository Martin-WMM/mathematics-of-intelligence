#!/usr/bin/env bash
set -euo pipefail

TARGET="${1:-all}"
BOOK_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$BOOK_DIR"

copy_built_pdf() {
  local from="$1"
  local to="$2"
  if cp -f "$from" "$to"; then
    echo "Wrote $to"
  else
    echo "Could not replace $to. Close the PDF viewer or the website Read tab, then run the script again. Fresh file: $from" >&2
  fi
}

build_edition() {
  local root="$1"
  local stem="${root%.tex}"
  local work="${stem}-wip"
  mkdir -p build
  echo "Building $root ..."
  pdflatex -interaction=nonstopmode -halt-on-error -output-directory=build -jobname="$work" "$root"
  if command -v bibtex >/dev/null 2>&1; then
    bibtex "build/$work" || true
  fi
  pdflatex -interaction=nonstopmode -halt-on-error -output-directory=build -jobname="$work" "$root"
  pdflatex -interaction=nonstopmode -halt-on-error -output-directory=build -jobname="$work" "$root"

  local dest="$BOOK_DIR/../website/apps/web/public/pdfs"
  copy_built_pdf "build/${work}.pdf" "build/${stem}.pdf"
  if [[ -d "$(dirname "$dest")" ]]; then
    mkdir -p "$dest"
    copy_built_pdf "build/${work}.pdf" "$dest/${stem}.pdf"
    echo "App PDF: $dest/${stem}.pdf"
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
