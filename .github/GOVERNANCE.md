# Branch and review rules

## Flow

```text
main
  → release/<scope>
      → feature/<scope>/<keywords>
      → fix/release/<scope>/<keywords>
      → (PR) release/<scope>
  → (PR) main
  → git tag
```

Hotfix on production:

```text
main → fix/main/<keywords> → (PR) main → git tag
```

`release/*` is never edited on the branch itself. Open a `feature/*` or `fix/release/*` pull request.

## Starting a release line

A new `release/<scope>` cannot be pushed from a laptop: the ruleset requires a pull request. Create the ref from `main` with the API, then branch work off it.

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

Write on the feature branch. Open a PR into `release/<scope>`, merge with a **merge commit** (squash and rebase are disabled). Then open `release/<scope>` → `main`, merge the same way, and tag `main`.

## Branch names

| Kind | Pattern | Example |
|------|---------|---------|
| Source of truth | `main` | `main` |
| Release line | `release/<scope>` | `release/representation` |
| Writing / feature | `feature/<scope>/<keywords>` | `feature/representation/signal-to-vector` |
| Fix on a release | `fix/release/<scope>/<keywords>` | `fix/release/representation/tikz-arrow` |
| Fix on main | `fix/main/<keywords>` | `fix/main/reader-iframe` |
| Built website (CI only) | `deploy/web` | `pnpm build` output after a website PR is merged |

`<scope>` is one of: `representation`, `learning`, `generation`, `intelligence`, `book`, `website`, `animations`, `ppts`, `examples`, `ci`, `docs`, `repo`, or a chapter slug `ch-<kebab>`.

`<keywords>` is lowercase kebab-case.

## Pull request targets

| Head | Base |
|------|------|
| `feature/<scope>/…` | `release/<scope>` |
| `fix/release/<scope>/…` | `release/<scope>` |
| `fix/main/…` | `main` |
| `release/<scope>` | `main` |

`deploy/*` is not a PR target and must not be pushed by hand.

## Release protection

Direct commits and force-pushes to `release/*` fail CI (`protect-release`). Enable a GitHub ruleset so GitHub also blocks the push:

- Target: `release/**`
- Require a pull request
- Do not allow force pushes
- Require status checks `commit-lint` and `pr-target` on pull requests
- Do not enforce those checks when the `release/<scope>` ref is first created

`.github/scripts/apply_github_rulesets.sh` reapplies the same rules via `gh` if a ruleset needs to be recreated.

## Workflows

| Workflow | When | What it checks or does |
|----------|------|-------------------------|
| `ci.yml` | Push/PR on `main`, `release/*`, `feature/*`, `fix/*` | Commit format, 500-line size, branch name, website build if `website/` changed |
| `pr-rules.yml` | Every PR | Head name and allowed base |
| `protect-release.yml` | Push to `release/*` | No force-push; after creation, only merge commits |
| `protect-deploy.yml` | Push to `deploy/*` | Only `github-actions[bot]` |
| `deploy-web.yml` | Website PR merged, or `website/` pushed to `main` / `release/*` | `pnpm build` and publish `deploy/web` |
| `sync-labels.yml` | Push of `.github/labels.yml` to `main` | Create/update labels |
| `release-merged.yml` | `release/*` merged to `main` | Comment with a tag command |

Point GitHub Pages at `deploy/web` if you want the production site hosted.

## Tags

After `release/<scope>` merges to `main`, create an annotated tag, for example `v0.1.0` or `book-representation-0.1.0`, and push it.

## Commits

```text
<emoji>[book|examples|...][<type>]: <message>
```

English message. At most 500 changed lines per commit. `CHANGELOG.md` counts.
