#!/usr/bin/env bash
# Publish compiled book PDFs to deploy/book (Git LFS) and copy them onto
# deploy/web/pdfs so GitHub Pages can serve real files, not LFS pointers.
set -euo pipefail

if [ "$#" -lt 3 ]; then
  echo "usage: publish_book_pdfs.sh <light.pdf> <dark.pdf> <github_token>" >&2
  exit 2
fi

LIGHT_PDF="$1"
DARK_PDF="$2"
TOKEN="$3"

if [ -z "${GITHUB_REPOSITORY:-}" ]; then
  echo "GITHUB_REPOSITORY is required" >&2
  exit 2
fi

for path in "$LIGHT_PDF" "$DARK_PDF"; do
  if [ ! -f "$path" ]; then
    echo "missing PDF: $path" >&2
    exit 1
  fi
done

AUTH_URL="https://x-access-token:${TOKEN}@github.com/${GITHUB_REPOSITORY}.git"

git_identity() {
  git config user.name "github-actions[bot]"
  git config user.email "41898282+github-actions[bot]@users.noreply.github.com"
}

remote_has_branch() {
  local branch="$1"
  git ls-remote --heads "$AUTH_URL" "$branch" | grep -q "refs/heads/${branch}$"
}

commit_if_needed() {
  local message="$1"
  if git diff --cached --quiet; then
    echo "No changes to commit."
    return 1
  fi
  git commit -m "$message"
  return 0
}

publish_lfs_book() {
  local work
  work="$(mktemp -d)"
  if remote_has_branch deploy/book; then
    git clone --depth 1 --branch deploy/book "$AUTH_URL" "$work"
  else
    git clone --depth 1 "$AUTH_URL" "$work"
    git -C "$work" checkout --orphan deploy/book
    git -C "$work" rm -rf . >/dev/null 2>&1 || true
  fi

  (
    cd "$work"
    git lfs install
    printf '%s\n' '*.pdf filter=lfs diff=lfs merge=lfs -text' > .gitattributes
    cat > README.md <<'EOF'
# Compiled book PDFs

Light and dark editions produced by `.github/workflows/deploy-book.yml`.
The `.pdf` files are stored with Git LFS. Do not push this branch by hand.
EOF
    cp "$LIGHT_PDF" book-light.pdf
    cp "$DARK_PDF" book-dark.pdf
    git_identity
    git add .gitattributes README.md book-light.pdf book-dark.pdf
    if commit_if_needed "📦[book][build]: publish compiled pdfs to lfs"; then
      git push -u origin deploy/book
    fi
  )
  rm -rf "$work"
}

publish_pages_copies() {
  if ! remote_has_branch deploy/web; then
    echo "deploy/web does not exist yet; skip Pages PDF copy."
    return 0
  fi

  local work
  work="$(mktemp -d)"
  git clone --depth 1 --branch deploy/web "$AUTH_URL" "$work"
  (
    cd "$work"
    mkdir -p pdfs
    cp "$LIGHT_PDF" pdfs/book-light.pdf
    cp "$DARK_PDF" pdfs/book-dark.pdf
    git_identity
    git add pdfs/book-light.pdf pdfs/book-dark.pdf
    if commit_if_needed "📦[book][build]: copy compiled pdfs onto pages"; then
      git push origin deploy/web
    fi
  )
  rm -rf "$work"
}

publish_lfs_book
publish_pages_copies
