# AGENTS.md — Mathematics of Intelligence

This file is the operating guide for people and coding agents working in this
repository. It reflects the checked-in project documentation, automation, and
Git history. When it disagrees with executable repository configuration, the
executable configuration wins; update this guide in the same change when a
workflow or project convention changes.

## 1. Mission and editorial intent

**Mathematics of Intelligence** is an English, long-form monograph and its
companion learning materials. It is a working map of modern AI theory, not a
claim to original mathematics or a self-contained mathematics treatise.

Every contribution should support both threads:

- **Mathematics:** introduce formal machinery when the argument requires it;
  connect ideas such as calculus, probability, linear algebra, optimisation,
  information, and dynamics rather than collecting isolated definitions.
- **AI:** use models, algorithms, and engineering consequences as the
  laboratory for the mathematics; do not overstate what an argument proves.

The book's canonical narrative is:

```text
Part I    Mathematical Foundations
Part II   Mathematics of AI
Part III  Intelligence and Beyond
References
```

The companion trees use conceptual threads instead of chapter numbering:
`mathematics/`, `ai/`, and `topics/<name>/`. Finance, physics, and future
subjects belong below `topics/`; never create a new top-level subject tree such
as `finance/` or `physics/`.

Write manuscript prose, code comments, UI copy, commit subjects, issue text,
and PR descriptions in English unless a file is specifically a Chinese locale
resource. The public website UI supports `en` and `zh-CN`; the monograph itself
is English.

## 2. Repository map and ownership boundaries

```text
book/                         LaTeX source of the monograph
  book-light.tex              Light-edition entry point
  book-dark.tex               Dark-edition entry point
  preamble/                   Shared packages, macros, themes, blocks, body order
  frontmatter/                Title, preface, notation
  parts/                      One directory and file per canonical part/chapter
  backmatter/                 References inclusion
  bib/references.bib          Bibliography database
  figures/, tikz/             Visual assets and TikZ drawings
  scripts/                    Edition build scripts

website/                      The only JavaScript/pnpm workspace
  apps/web/                   Vue 3 + Vite reader and public site
  packages/ui/                Reusable shadcn-style Vue primitives and design tokens
  packages/i18n/              Locale messages and locale definitions
  packages/shared/            Book TOC and shared types

animations/                   Python >= 3.10 Manim package and scenes
  src/moi_manim/              Reusable visual helpers/themes
  scenes/{mathematics,ai,topics}/

examples/                     Small conceptual Python programs and notebooks
ppts/                         Source PowerPoint decks
scripts/                      Repository-root book render entry points
.github/                      CI, deployment, governance, templates, validation scripts
.githooks/                    Local commit message and commit-size hooks
```

Keep package boundaries intact:

- Do not add Node tooling, a lockfile, or a JavaScript workspace outside
  `website/`.
- Do not place LaTeX, Manim, or example dependencies in the pnpm workspace.
- Treat `website/packages/shared/src/toc.ts` and `book/preamble/body.tex` as
  paired canonical outlines. A change to book parts, chapter titles, or chapter
  order normally requires an intentional matching update to both.
- Book PDFs are build products, not source-branch artifacts. `*.pdf` is tracked
  via Git LFS, but `book/build/` and
  `website/apps/web/public/pdfs/*.pdf` are ignored. CI alone writes
  `deploy/book` and `deploy/web`.

## 3. Before changing anything

1. Inspect `git status --short`, the current branch, and nearby source before
   editing. This workspace can contain unrelated user changes; preserve them.
2. Read the closest README and the source-of-truth files named below. Do not
   infer a convention from a generated PDF, `dist/`, `media/`, or build cache.
3. Keep the task narrowly scoped. Split unrelated refactors, formatting sweeps,
   and dependency upgrades into separate changes/commits.
4. Do not edit protected, bot-owned, generated, or ignored output merely to
   make a local preview look correct.
5. After an edit, run the narrowest relevant validation. For cross-boundary
   changes, validate every affected boundary.

Useful source-of-truth order:

| Concern | Read first |
| --- | --- |
| Repository flow and deployment | `.github/GOVERNANCE.md`, `.github/workflows/` |
| Branch/commit enforcement | `.github/scripts/check_*.py`, `.githooks/` |
| Book outline and build | `book/README.md`, `book/preamble/body.tex`, `book/scripts/` |
| LaTeX appearance and semantics | `book/preamble/*.tex`, adjacent chapter files |
| Website structure and build | `website/README.md`, `website/package.json`, app package manifest |
| Website copy/locales | `website/packages/i18n/src/en.ts`, `zh-CN.ts` |
| Shared chapter metadata | `website/packages/shared/src/toc.ts` |
| Manim or examples | the local README, `pyproject.toml`, `requirements.txt` |

## 4. Book and scholarly-content rules

### 4.1 Canonical structure

Each chapter is a single file in the matching numbered part directory. Add or
rename a chapter only with all of the following considered:

1. the chapter file and its `\chapter{...}` title;
2. the include location in `book/preamble/body.tex`;
3. the parallel entry in `website/packages/shared/src/toc.ts`;
4. surrounding links, citations, examples, animations, slides, and docs;
5. the book build and the website type check/build.

Do not insert chapter content directly into `book-light.tex` or
`book-dark.tex`. The two root files intentionally share one body and differ
only in theme selection. Shared packages, commands, caption behavior, and
statement definitions belong in the corresponding `preamble/` file, not in an
individual chapter unless the behavior is genuinely chapter-local.

### 4.2 Mathematical and citation quality

- Define notation before relying on it; reuse commands from
  `preamble/macros.tex` rather than introducing visually similar ad-hoc macros.
- State hypotheses and the meaning of objects, dimensions, domains, and
  probability measures when material to a claim. Distinguish intuition,
  example, assumption, theorem, and proof.
- Use the existing theorem environments (`definition`, `theorem`, `corollary`,
  `proposition`, `lemma`, `assumption`, `example`, `proof`, `remark`) instead
  of hand-styled boxes. Numbered environments share the chapter counter;
  `proof` and `remark` are unnumbered.
- Cite externally derived claims, formulations, diagrams, and nontrivial
  historical assertions. Add stable BibTeX entries to `book/bib/references.bib`
  and cite keys from prose. Do not invent bibliographic data or citations.
- Preserve the preface's source-disclaimer posture: describe mainstream work
  accurately and do not represent borrowed arguments as original results.
- Keep prose pedagogical and precise. Prefer a small, well-motivated example
  over an unsupported sweep of terminology.

### 4.3 Figures and tables

Every figure and table must be a real `figure` or `table` environment, include
a `\label`, and use:

```tex
\moicaption{Short descriptive title}{Complete explanatory description.}
```

The project numbers figures/tables by chapter. Do not add a bare
`\includegraphics` or a bare `tabular` used as a publication figure/table.
Place reusable LaTeX drawings in `book/tikz/`; use `book/figures/` for figure
assets. Ensure both light and dark themes remain legible.

### 4.4 Book commands and expected outputs

Run from the repository root whenever possible:

```bash
./scripts/render-pdf.sh            # both editions
./scripts/render-pdf.sh light
./scripts/render-pdf.sh dark
```

On Windows use `scripts/render-pdf.cmd` or `scripts/render-pdf.ps1`. The
scripts require `pdflatex` (and use `bibtex` when available), output
`book/build/book-light.pdf` and `book/build/book-dark.pdf`, and attempt to
copy them into the reader's public PDF directory. A failed replacement often
means a PDF viewer has locked the destination; close it and retry. Do not add
the generated outputs to a source commit.

For a change that affects only one edition's wrapper, build that edition. For
any shared body, macro, theme, figure, or bibliography change, build both
editions and resolve LaTeX errors, missing references, and unreadable contrast.

## 5. Website rules

### 5.1 Workspace and commands

Use pnpm 9 from `website/`; retain and respect `pnpm-lock.yaml`.

```bash
cd website
pnpm install --frozen-lockfile
pnpm --filter @moi/web exec vue-tsc --noEmit
pnpm build
pnpm dev
```

`pnpm build` already runs the Vue type check for `@moi/web`. Use `pnpm dev` for
manual UI verification. Do not use npm/yarn or introduce an additional
lockfile. Do not manually edit `dist/`, `.vite/`, `node_modules/`, or the PDFs
copied into `apps/web/public/pdfs/`.

### 5.2 Implementation conventions

- The application is Vue 3, TypeScript, Vue Router, Vite, Tailwind CSS, and
  `vue-i18n`. Use `<script setup lang="ts">` and existing import aliases and
  workspace packages.
- Put app-level routes/pages in `website/apps/web/src/`; reusable UI primitives
  and design tokens in `website/packages/ui/`; cross-app data/types in
  `website/packages/shared/`; translations in `website/packages/i18n/`.
- Reuse `Button`, `Card`, `cn`, and the CSS semantic tokens before making a
  one-off component or hard-coded color. Maintain equivalent light and dark
  behavior through the token system.
- New user-visible strings require both `en.ts` and `zh-CN.ts` entries with the
  same key shape. Do not place English copy directly in a component when it
  should be translated.
- Preserve `createWebHistory(import.meta.env.BASE_URL)`: deployment sets a
  repository subpath using `VITE_BASE`.
- The reader expects `book-light.pdf` and `book-dark.pdf`. Handle their absence
  gracefully; source branches deliberately do not commit the generated files.

## 6. Animations, examples, and slides

### Manim

`animations/` is an installable package named `moi-manim` and needs Python
3.10+ and Manim. Set up in an isolated virtual environment:

```bash
cd animations
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -e .
manim -pql scenes/mathematics/example.py ExampleScene
```

Use `moi_manim.LIGHT` or `moi_manim.DARK` so scenes match the book editions.
Place shared helpers in `src/moi_manim/`, a scene in the appropriate conceptual
thread, and never commit `media/` or `.venv/`.

### Examples and decks

Examples are short programs/notebooks that illuminate a concrete conceptual
question, not model-training pipelines. They use `examples/requirements.txt`;
create a virtual environment and run the changed script directly. Name example
files after the mathematical object or question, not a chapter number.

PowerPoint decks are authored source files in `ppts/`, not generated LaTeX
output. Keep deck names in kebab-case (for example, `inner-products.pptx`) and
place them under `mathematics/`, `ai/`, or `topics/<name>/`.

## OpenSpec workflow

This repository uses OpenSpec for spec-driven planning and implementation. The
OpenSpec root is `openspec/`, with active changes under
`openspec/changes/`, durable capability specifications under
`openspec/specs/`, and project-specific configuration in
`openspec/config.yaml`. The current configuration uses the `spec-driven`
schema. OpenSpec artifacts are planning records and specifications; they do
not replace the source code, tests, book files, website files, or the Git/PR
workflow described elsewhere in this document.

### When to use OpenSpec

Use an OpenSpec change for a feature, behavior change, cross-file refactor,
new capability, or other work that benefits from an explicit proposal,
design, requirements, and task list. Small, mechanical, or documentation-only
edits may proceed directly when the change does not need a plan. When OpenSpec
is used, keep the change name lowercase kebab-case and make it describe one
coherent outcome, for example `add-reader-search` or
`explain-conditional-expectation`.

Never create a directory under `openspec/changes/` by hand. Always let the CLI
create the change metadata, including `.openspec.yaml`:

```bash
openspec list --json
openspec new change <change-name>
openspec status --change <change-name> --json
```

If the project has not been initialized, do not let a command create an
OpenSpec root as a side effect. First confirm the situation with
`openspec list --json`; only run `openspec init` after the user explicitly asks
to initialize OpenSpec. In this repository `openspec list --json` should report
the repository root rather than `"root": null`.

### Standard OpenSpec lifecycle

The normal lifecycle is:

```text
explore -> propose -> review/update -> apply -> validate -> archive
                         \-> sync specs (optional, before archive)
```

Use the matching workflow below. Slash commands are shorthand for the same
workflow when the editor integration provides them.

1. **Explore** (`/opsx-explore`): inspect the codebase and existing specs,
   clarify the problem, constraints, and alternatives. Explore is a thinking
   mode: it may read files and run read-only commands, but it must not edit
   implementation code. It may capture explicitly approved planning artifacts;
   do not auto-create a change merely because an idea was discussed.

2. **Propose** (`/opsx-propose <change-name>`): create the change with
   `openspec new change <change-name>`, then follow the artifact graph. For
   each artifact that is `ready`, first run
   `openspec instructions <artifact-id> --change <change-name> --json` and use
   its returned `template`, `instruction`, `dependencies`, `context`, `rules`,
   and `resolvedOutputPath`. Re-run
   `openspec status --change <change-name> --json` after each artifact. Do not
   invent artifact names or paths, and do not create blocked or unrequested
   prerequisites without approval.

3. **Review or update** (`/opsx-update <change-name>`): revise existing
   planning artifacts when requirements, design decisions, or scope change.
   Read all related artifacts first and keep them coherent. This workflow
   edits planning artifacts only; it never edits implementation code and does
   not create missing artifacts. If the intent has materially changed, start a
   new change instead of silently mutating the old one.

4. **Apply** (`/opsx-apply <change-name>`): select the change, inspect
   `openspec status --change <change-name> --json`, then obtain the dynamic
   instructions with
   `openspec instructions apply --change <change-name> --json`. Read every
   path in the returned `contextFiles` before editing code. Implement tasks in
   order, keep the implementation focused, and immediately change each fully
   completed task from `- [ ]` to `- [x]`. Never mark a partial, deferred, or
   unverified task complete. Pause and update the artifacts if a task is
   ambiguous, exposes a design problem, or requires behavior outside the
   approved scope.

5. **Validate**: validate the active change after planning or implementation,
   and validate main specs after a sync:

   ```bash
   openspec validate <change-name> --strict
   openspec validate --specs --strict
   openspec validate --all --strict
   ```

   Use the narrowest applicable command during iteration and `--all` before a
   broad handoff. Treat validation failures as work to fix; do not weaken the
   spec or skip a required artifact to make the command pass.

6. **Sync specs** (`/opsx-sync <change-name>`, optional): merge delta specs
   into the durable specs without archiving the change. First read
   `artifactPaths.specs.existingOutputPaths` from
   `openspec status --change <change-name> --json`; sync only those concrete
   paths, never infer delta files from unrelated artifacts. Preserve existing
   requirements and scenarios, merge ADDED/MODIFIED/REMOVED/RENAMED blocks
   intelligently, and keep main specs in the canonical `## Requirements`
   format. Run `openspec validate --specs` afterward. The change remains
   active until it is separately archived.

7. **Archive** (`/opsx-archive <change-name>`): archive only after the
   implementation and required review are complete. The workflow checks
   artifact status and task checkboxes, compares delta specs with main specs,
   performs the required sync, validates the result, and moves the completed
   change into the archive with a date-prefixed name when needed. If artifacts
   or tasks are incomplete, report them and ask before proceeding; do not claim
   completion merely because the code appears finished.

For a quick status check, use:

```bash
openspec status --change <change-name> --json
openspec show <change-name> --type change --json
openspec list --json
openspec list --specs --json
```

Use the JSON output as the source of truth for `schemaName`, `planningHome`,
`changeRoot`, `artifactPaths`, artifact states, task progress, and
`contextFiles`. A custom schema may use artifact names other than proposal,
design, specs, and tasks; never hard-code those names when the CLI reports
different ones.

### OpenSpec stores and command safety

Most repositories use their nearest local `openspec/` root. A registered
standalone OpenSpec repository is a store. If a task names or lives in a
store, discover it first and pass the selected store ID consistently to every
root-aware command:

```bash
openspec store list --json
openspec list --json --store <store-id>
openspec status --change <change-name> --json --store <store-id>
openspec instructions apply --change <change-name> --json --store <store-id>
```

The `--store` flag applies to root-aware commands such as `new change`,
`status`, `instructions`, `list`, `show`, `validate`, `archive`, `doctor`,
`context`, `schemas`, and `view`. Keep it on all follow-up commands. Do not
mix a store's artifacts with this checkout's local `openspec/` directory.

OpenSpec artifacts should be committed together with the implementation they
describe, subject to the normal branch, commit-size, and review rules. Do not
commit generated PDFs, build output, editor caches, or unrelated files merely
because an OpenSpec task mentions them. Before handoff, check both:

```bash
openspec validate --all --strict
git diff --check
git status --short
```

## 7. Git, branches, commits, and pull requests

The remote is `Martin-WMM/mathematics-of-intelligence`. Recent project history
shows that repository/governance work, book structure, caption/statement
semantics, the preface, and root PDF rendering are deliberately separated into
small commits. Maintain that discipline.

### 7.1 Protected branch flow

```text
main
  -> release/<scope>
       -> feature/<scope>/<keywords>       -> PR -> release/<scope>
       -> fix/release/<scope>/<keywords>   -> PR -> release/<scope>
  -> fix/main/<keywords>                   -> PR -> main
release/<scope>                            -> PR -> main -> annotated tag
```

- Treat `main` as the stable integration branch and `release/*` as the
  stabilization branch for a release. Both are protected branches.
- Before editing, run `git status --short`, `git branch --show-current`, and
  `git log -5 --oneline`. Preserve unrelated modifications, untracked files,
  and work from other contributors; do not reset, clean, stash, or overwrite
  them unless explicitly requested.
- Never commit or push directly to `main` or `release/*`. Do not use force
  push, branch deletion, or history rewriting on shared branches.
- Release branches are created from the current `main` through the GitHub API
  because the ruleset blocks ordinary laptop creation. Feature and fix
  branches must then start from the release branch they will target.
- Normal feature work uses `feature/<scope>/<keywords>` and targets the
  matching `release/<scope>` branch. Release fixes use
  `fix/release/<scope>/<keywords>` and target that release branch. A hotfix
  that must land directly on stable uses `fix/main/<keywords>` and targets
  `main`.
- `<scope>` must be `representation`, `learning`, `generation`,
  `intelligence`, `book`, `website`, `animations`, `ppts`, `examples`, `ci`,
  `docs`, `repo`, or `ch-<kebab-case-slug>`.
- `<keywords>` is lowercase kebab-case. Do not improvise a branch shape.
- Keep a working branch focused on one coherent change. Do not combine
  unrelated refactors, generated output, dependency upgrades, or formatting
  sweeps with the requested work.
- Keep the branch up to date with its target before opening or updating a PR;
  resolve conflicts on the working branch and rerun affected checks. Use merge
  commits for approved PRs; squash and rebase merges are disabled.
- PRs must target only the branch shown in the flow above. Include the scope,
  user-visible impact, validation commands and results, deployment consequence,
  and any follow-up work in the PR description.
- `deploy/web`, `deploy/book`, and `deploy/preview` are CI build branches, not
  human work branches or PR targets. Do not push them by hand.
- `dependabot/*` is bot-only and may target `main`; do not create it manually.

Validate a proposed name/target locally when relevant:

```bash
python .github/scripts/check_branch_name.py --name feature/book/example
python .github/scripts/check_pr_target.py \
  --head feature/book/example --base release/book
```

For routine local work, use this sequence and inspect the result after every
state-changing command:

```bash
git fetch origin --prune
git switch -c feature/book/example origin/release/book
# edit files and run the narrowest relevant checks
git diff --check
git status --short
git diff -- path/to/changed/file
git add path/to/changed/file
python .github/scripts/check_commit_size.py
git commit -m '✨[book][feat]: explain conditional expectation'
git push --set-upstream origin feature/book/example
```

Do not stage unrelated files with `git add -A`. Before committing, review the
staged diff with `git diff --cached`, confirm that no generated files or
secrets are included, and run the directly affected validation. Before pushing
an existing branch, verify its target and commit range; use the repository
checkers below rather than bypassing a failed hook.

### 7.2 Commit contract

Every non-merge, non-Dependabot subject must be exactly:

```text
<emoji>[<scope>][<type>]: <lowercase English imperative message without period>
```

Valid scopes are `book`, `website`, `animations`, `ppts`, `examples`, `ci`,
`docs`, and `repo`. Valid types are `feat`, `fix`, `docs`, `refactor`, `test`,
`chore`, `style`, `perf`, `build`, `ci`, and `revert`.

Examples:

```text
✨[book][feat]: explain conditional expectation
🐛[website][fix]: preserve reader page after theme change
📦[repo][build]: add a root render-pdf entry
```

Each commit may change at most **500 added plus deleted lines**, including
`CHANGELOG.md`; binary files count as one line. Keep independent concerns in
separate commits and update `CHANGELOG.md` for user-visible/repository-notable
changes. The local hooks run the same checks when configured. Check them before
committing or handing off a staged change:

```bash
python .github/scripts/check_commit_size.py
python .github/scripts/check_commit_message.py \
  --subject '✨[book][feat]: explain conditional expectation'
```

For an existing comparison range, run:

```bash
python .github/scripts/check_push_range.py --range origin/main..HEAD
```

Use the actual PR base in the comparison range when working from a release
branch, for example `origin/release/book..HEAD`. A failed branch, message,
size, or push-range check is a correction to make—not a reason to disable the
hook or weaken the repository rule. If a commit is too large, split it into
focused commits while preserving the user's existing changes.

### 7.3 PR and deployment implications

- Use the matching issue/PR templates under `.github/` and state scope,
  validation, and any documentation or deployment consequence.
- The CI workflow checks branch names, commit subjects/sizes, and runs the
  website type check/build only if `website/**` changed.
- A merged PR touching `website/**` publishes a static build to `deploy/web`.
- A merged PR touching `book/**` builds both PDFs, publishes LFS objects to
  `deploy/book`, then the web deployment copies non-LFS PDF files for GitHub
  Pages. Never emulate this by committing build outputs to a source branch.
- Editing workflow or deployment scripts itself can trigger its matching
  deployment; review those changes as production automation.

## 8. Verification matrix

Use the smallest complete set of checks for the change. Report commands not run
and the reason (for example, `pdflatex` or pnpm not installed) rather than
claiming success.

| Changed area | Minimum verification |
| --- | --- |
| Chapter prose, macros, theme, bibliography, TikZ, figures | Build affected edition; build both for shared changes and inspect errors/warnings. |
| Book outline/title/order | Build both editions; run website type check/build after TOC synchronization. |
| Vue app or workspace packages | `pnpm --filter @moi/web exec vue-tsc --noEmit` and `pnpm build` from `website/`. |
| Locale messages | Website type check/build; manually exercise the language switch if UI behavior changed. |
| Manim helper/scene | Render the changed scene at low quality where the runtime is available. |
| Python example | Install declared dependencies if needed; run the changed script. |
| GitHub validation scripts/workflows | Run the directly affected Python checker(s); review YAML paths/triggers and, where possible, validate branch/commit rules. |
| Documentation-only change | Check links, commands, paths, and consistency with actual scripts/configuration. |

Finish with `git diff --check`, review the diff for accidental generated files
or line-ending churn, and confirm only intended paths changed. Do not attempt a
repository-wide line-ending cleanup while doing feature work.

## 9. Safety and handoff

- Preserve user changes and untracked work. Never use `git reset --hard`,
  destructive cleanup, force-push, branch deletion, or deploy-branch writes
  without explicit authorization.
- Do not expose tokens, private reports, or credentials; follow `SECURITY.md`
  for vulnerability reporting.
- Do not weaken the 500-line/commit rule, branch protections, Dependabot,
  CodeQL, secret scanning, or CI checks merely to make a task pass.
- In a final handoff, state what changed, the checks run and their outcomes,
  checks skipped (with reason), and any follow-up required to deploy or review.

## 10. Quick decision guide

```text
New chapter or renamed chapter?
  -> chapter file + preamble/body.tex + shared TOC + both book builds + web build

New site copy?
  -> en.ts + zh-CN.ts + use i18n key + type check/build

New visual explanation?
  -> choose book figure/TikZ, Manim scene, example, or deck by audience;
     keep it under the corresponding conceptual thread

Want to publish PDFs/site?
  -> merge the properly targeted PR; CI owns deploy/book and deploy/web

Want to commit?
  -> valid branch + <=500 changed lines + valid emoji/scope/type subject
```
