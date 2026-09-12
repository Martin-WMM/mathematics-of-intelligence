# Mathematics of Intelligence

A long-term project on the mathematics of modern artificial intelligence. The book is written in **English**. Two intellectual threads run through every artifact:

- **Mathematics** — structures introduced when a chapter needs them
- **AI** — models and algorithms as the laboratory

Finance, physics, and other sciences appear later as *topics*, not as top-level folders.

**Representation → Learning → Generation → Intelligence**

## Repository

| Path | What it is |
|------|------------|
| [`book/`](book/) | LaTeX monograph. Light and dark PDFs from the same chapters. |
| [`website/`](website/) | Vue 3 + pnpm workspace. Introduction site and embedded PDF reader. UI: English / 中文. |
| [`animations/`](animations/) | Manim library and scenes (`mathematics/`, `ai/`, `topics/`). |
| [`ppts/`](ppts/) | PowerPoint decks, same grouping. |
| [`examples/`](examples/) | Small example programs, same grouping. |

The website is the only JavaScript monorepo. LaTeX and Python stay outside `website/`.

## Git

Commits: `<emoji>[book|examples|...][<type>]: <message>` (English). At most **500** changed lines per commit; `CHANGELOG.md` counts.

Branches: `main` ← `release/<scope>` ← `feature/<scope>/<keywords>` or `fix/…`. Do not commit on `release/*`. Built sites live on `deploy/web` (from `main`) and `deploy/preview` (from `release/*`).

See [.github/GOVERNANCE.md](.github/GOVERNANCE.md).

## Book

From `book/`, with `pdflatex`, `bibtex`, and `latexmk`:

```powershell
.\scripts\build.ps1 all
```

Outputs `book/build/book-light.pdf` and `book/build/book-dark.pdf`, and copies them to `website/apps/web/public/pdfs/` for the reader.

## Website

```bash
cd website
pnpm install
pnpm dev
```

Open the Read page after the PDFs have been built.

## Animations, slides, examples

See the README in each directory. New topic material goes under `topics/<name>/` inside those three trees—do not add a top-level `finance/` or `physics/` folder.
