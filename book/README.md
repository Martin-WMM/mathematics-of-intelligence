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
├── preamble/                 # packages, macros, themes, shared body
├── frontmatter/              # title, preface, notation
├── parts/
│   ├── 01-foundations/                 # Part I  — Mathematical Foundations
│   ├── 02-mathematics-of-ai/           # Part II — Mathematics of AI
│   └── 03-intelligence-and-beyond/     # Part III — Intelligence and Beyond
├── backmatter/               # references
├── figures/
├── tikz/
├── bib/references.bib
├── latexmkrc
└── scripts/
```

## Narrative

```text
Mathematics of Intelligence
│
├── Part I  — Mathematical Foundations
│     1  Spaces, Vectors, and Inner Products
│     2  Linear Maps, Spectra, and Decompositions
│     3  Probability and Expectation
│     4  Information and Compression
│     5  Optimization as Geometry
│     6  Dynamics and Iteration
│     7  Structure Beyond Vectors
│
├── Part II — Mathematics of AI
│     8  Representation
│     9  Learning, Loss, and Risk
│    10  Generalization
│    11  From Classical Learning to Deep Learning
│    12  Modeling Distributions
│    13  Autoregressive Factorization
│    14  Latent Variable Models
│    15  Adversarial and Implicit Generation
│    16  Diffusion, Scores, and Flows
│
├── Part III — Intelligence and Beyond
│    17  Prediction versus Reasoning
│    18  Memory and Retrieval
│    19  Planning and Control
│    20  World Models
│    21  Agents
│    22  Beyond
│
└── References
```

Chapter files are short openings. Expand one part at a time on later feature branches. One file per chapter; `preamble/body.tex` is the single include list.

Statement blocks in `preamble/blocks.tex` share one chapter-wise counter (`Definition 1.1`, `Theorem 1.2`, \ldots). Proof and remark are unnumbered.

Every figure and table must use `figure`/`table` with `\moicaption{Title}{Description}` and a `\label`. Numbers follow the chapter (`Figure 1.1`, `Table 1.1`). The front-matter notation table is `Table N.1`. Do not insert a bare `\includegraphics` or `tabular` without a caption.

| Environment | Role |
|-------------|------|
| `definition` | Named object |
| `theorem` | Main claim |
| `corollary` | Immediate consequence |
| `proof` | Argument (unnumbered) |
| `example` | Laboratory illustration |


## Build

Requires `pdflatex` and `bibtex` (MiKTeX or TeX Live). `latexmk` is optional.

From the repository root (not `book/`):

```powershell
.\scripts\render-pdf.cmd
.\scripts\render-pdf.cmd light
.\scripts\render-pdf.cmd dark
```

```bash
./scripts/render-pdf.sh
```

Or from `book/`:

```powershell
.\scripts\build.ps1 all
.\scripts\build.ps1 light
.\scripts\build.ps1 dark
```

```bash
./scripts/build.sh all
```

A successful build also copies the PDFs into `website/apps/web/public/pdfs/` for the embedded reader.

When a pull request that changes `book/` is merged, GitHub Actions runs the same build and publishes the PDFs with Git LFS on `deploy/book`. GitHub Pages cannot serve LFS pointers, so the workflow also copies the files onto `deploy/web/pdfs/`.
