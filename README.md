# Mathematics of Intelligence

## Introduction

*Mathematics of Intelligence* is a long-term English manuscript by Martin M. W. It is a working map of AI theory---symbols and arguments, not a claim to be a mathematics treatise---so that new work is easier to place. The book claims no originality: the arguments come from mainstream papers, textbooks, monographs, and public talks. Two threads run through every artifact:

- **Mathematics** — calculus as the start; then the ideas that keep returning (including stochastic processes and convex optimisation)
- **AI** — models and algorithms; missing mathematics is filled in when a chapter needs it, and tied to engineering where that is honest

The narrative spine is **Mathematical Foundations → Mathematics of AI → Intelligence and Beyond**. Physics, finance, and other sciences appear later as *topics*, not as top-level folders.

| Path | What it is |
|------|------------|
| [`book/`](book/) | LaTeX monograph. Light and dark PDFs share one body and switch only the page theme. |
| [`website/`](website/) | Vue 3 + pnpm workspace. Introduction site and embedded PDF reader. UI: English / 中文. |
| [`animations/`](animations/) | Manim library and scenes (`mathematics/`, `ai/`, `topics/`). |
| [`ppts/`](ppts/) | PowerPoint decks, same grouping. |
| [`examples/`](examples/) | Small example programs, same grouping. |

The website is the only JavaScript monorepo. LaTeX and Python stay outside `website/`.

## Updates / Features

Current capabilities of this repository:

- Two book editions from the same source: light (`book-light.tex`) and dark (`book-dark.tex`). Both compile the three-part outline (Mathematical Foundations → Mathematics of AI → Intelligence and Beyond) plus References; later feature branches expand one part at a time.
- A Vue 3 site (`website/`) with English / 中文 UI, light and dark theme, and an embedded PDF reader.
- After a pull request that touches `website/` is **merged**, GitHub Actions runs `pnpm build` and publishes the static files to [`deploy/web`](https://github.com/Martin-WMM/mathematics-of-intelligence/tree/deploy/web).
- After a pull request that touches `book/` is **merged**, GitHub Actions compiles the light and dark PDFs, stores them with Git LFS on [`deploy/book`](https://github.com/Martin-WMM/mathematics-of-intelligence/tree/deploy/book), and copies them into the Pages `pdfs/` folder.
- Branch flow, commit format, issue and PR templates, and push checks. See [`.github/GOVERNANCE.md`](.github/GOVERNANCE.md).
- Security and quality: Dependabot, CodeQL, secret scanning, and private reports via [`SECURITY.md`](SECURITY.md).
- Companion trees for Manim scenes, PowerPoint decks, and small examples, grouped by mathematics / AI / topics.

Recorded changes live in [`CHANGELOG.md`](CHANGELOG.md).

## Usage

### Book

Requires `pdflatex` (MiKTeX or TeX Live). From the repository root (not `book/`):

```powershell
.\scripts\render-pdf.cmd
.\scripts\render-pdf.cmd light
.\scripts\render-pdf.cmd dark
```

```bash
./scripts/render-pdf.sh
./scripts/render-pdf.sh light
./scripts/render-pdf.sh dark
```

Outputs `book/build/book-light.pdf` and `book/build/book-dark.pdf`, and copies them to `website/apps/web/public/pdfs/` for the reader. The same build can still be run from `book/` via `.\scripts\build.ps1`.

### Website

```bash
cd website
pnpm install
pnpm dev
```

Open http://localhost:5173. For a production build:

```bash
cd website
pnpm install
pnpm build
```

The built files are in `website/apps/web/dist`. Open the Read page after the PDFs have been built.

### Animations, slides, examples

See the README in each directory. New topic material goes under `topics/<name>/` inside those three trees—do not add a top-level `finance/` or `physics/` folder.

## Contributes

Do not commit on `main` or `release/*`. Write on a feature or fix branch, then open a pull request.

```text
main
  → release/<scope>          # created from main via the GitHub API
      → feature/<scope>/<keywords>
      → fix/release/<scope>/<keywords>
      → (PR, merge commit) release/<scope>
  → (PR, merge commit) main
  → git tag
```

Hotfix on production: `main` → `fix/main/<keywords>` → PR → `main`.

Start a release line (a laptop cannot push `release/*`):

```bash
git fetch origin
git checkout main
git pull origin main

gh api repos/:owner/:repo/git/refs \
  -f ref="refs/heads/release/<scope>" \
  -f sha="$(git rev-parse origin/main)"

git fetch origin
git checkout -B feature/<scope>/<keywords> origin/release/<scope>
```

Commit messages are English and follow:

```text
<emoji>[book|examples|...][<type>]: <message>
```

Each commit is at most **500** changed lines. `CHANGELOG.md` counts. Full rules: [`.github/GOVERNANCE.md`](.github/GOVERNANCE.md) and the [git-commit skill](.cursor/skills/git-commit/SKILL.md).

If a merged pull request changes `website/`, the deploy workflow publishes `deploy/web`. If it changes `book/`, another workflow compiles the PDFs and writes them to `deploy/book` through Git LFS. Do not push `deploy/*` by hand.
