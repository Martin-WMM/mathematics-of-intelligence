---
name: git-commit
description: >-
  Creates git commits in the format <emoji>[book|examples|...][<type>]: <message>,
  enforces a 500-line staged diff limit per commit including CHANGELOG.md, and
  splits oversized changes. Use when the user asks to commit, write commit
  messages, stage changes, or mentions git commits for this project.
---

# Git Commit

## Commit Message Format

All commit messages **must be in English** and follow:

```text
<emoji>[book|examples|...][<type>]: <message>
```

| Part | Rules |
|------|-------|
| `emoji` | Single emoji matching the change type (see [reference.md](reference.md)) |
| `scope` | One of `book`, `website`, `animations`, `ppts`, `examples`, `ci`, `docs`, `repo` |
| `type` | Lowercase conventional type: `feat`, `fix`, `docs`, `refactor`, `test`, `chore`, `style`, `perf`, `build`, `ci`, `revert` |
| `message` | English, imperative mood, lowercase start, no trailing period |

**Subject line only** unless the user explicitly asks for a body. If a body is needed, keep the subject in the format above and add a blank line before the body (also English).

### Examples

```text
✨[book][feat]: add signal-to-vector chapter
🐛[website][fix]: restore dark pdf iframe source
📝[docs][docs]: document release branch rules
♻️[examples][refactor]: extract cosine helper
👷[ci][ci]: add push commit lint
```

## 500-Line Limit

**One commit must not exceed 500 changed lines** (insertions + deletions combined in the staged diff).

`CHANGELOG.md` **counts**. There is no exclusion list.

Before committing:

```bash
python scripts/git/check_commit_size.py
```

If the check fails:

1. Do **not** commit everything at once.
2. Split changes into logical, reviewable commits (each ≤ 500 lines).
3. Re-run the size check after each staging pass.
4. Commit sequentially with separate messages.

Binary files count as 1 changed line each in `--numstat`.

## Commit Workflow

When the user asks to commit:

1. Run in parallel:
   - `git status`
   - `git diff` (unstaged)
   - `git diff --cached` (staged)
   - `git log -5 --oneline` (match recent style)
2. Stage only files relevant to **one logical change**.
3. Run `python scripts/git/check_commit_size.py`.
4. If over 500 lines, unstage and split; repeat from step 2.
5. Draft an English message: `<emoji>[<scope>][<type>]: <message>`.
6. Run `python scripts/git/check_commit_message.py` on that subject (or rely on the commit-msg hook).
7. Commit (never update git config, never skip hooks, never force-push unless explicitly requested).
8. Run `git status` to verify.

### Safety

- Never commit secrets (`.env`, credentials, keys).
- Never `--no-verify` unless the user explicitly requests it.
- Never `git commit --amend` unless user requests it AND HEAD was created this session AND not pushed.
- Do not push unless the user explicitly asks.

## Type Selection

| Change | Type | Emoji |
|--------|------|-------|
| New feature or chapter content | `feat` | ✨ |
| Bug fix | `fix` | 🐛 |
| Documentation only | `docs` | 📝 |
| Code/content restructure, no behavior change | `refactor` | ♻️ |
| Tests | `test` | ✅ |
| Tooling, deps, misc maintenance | `chore` | 🔧 |
| Formatting only | `style` | 🎨 |
| Performance | `perf` | ⚡ |
| CI/CD | `ci` | 👷 |
| Build system | `build` | 📦 |
| Revert | `revert` | ⏪ |

Full mapping and edge cases: [reference.md](reference.md).

## Multi-Commit Splitting

When splitting a large change set:

- Group by purpose (e.g. book text vs website vs CI).
- Order commits so each commit builds on the previous (dependencies first).
- Each commit message describes **why**, not a file list.

Example split for an 800-line init:

1. `🏗️[repo][chore]: initialize top-level workspace layout`
2. `📝[docs][docs]: add repository readme and changelog`
3. `👷[ci][ci]: add push lint and deploy workflows`
