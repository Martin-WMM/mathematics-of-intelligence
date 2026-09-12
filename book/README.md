# Book

LaTeX source for *Mathematics of Intelligence*. The text is English. Two root files share one body and switch only the page theme.

| Edition | Root file | Output |
|---------|-----------|--------|
| Light | `book-light.tex` | `build/book-light.pdf` |
| Dark | `book-dark.tex` | `build/book-dark.pdf` |

## Layout

```text
book/
├── book-light.tex
├── book-dark.tex
├── preamble/          # packages, macros, themes, shared body
├── frontmatter/
├── parts/             # four parts, one file per chapter
├── backmatter/
├── figures/           # raster figures
├── tikz/              # reusable TikZ pictures
├── bib/references.bib
├── latexmkrc
└── scripts/
```

Narrative spine: **Representation → Learning → Generation → Intelligence**. Mathematics is woven into chapters; it is not a separate part.

## Build

Requires `pdflatex` and `bibtex` (MiKTeX or TeX Live). `latexmk` is optional.

```powershell
# from book/
.\scripts\build.ps1 all
.\scripts\build.ps1 light
.\scripts\build.ps1 dark
```

```bash
./scripts/build.sh all
```

A successful build also copies the PDFs into `website/apps/web/public/pdfs/` for the embedded reader.
