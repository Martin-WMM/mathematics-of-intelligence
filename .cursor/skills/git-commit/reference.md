# Git Commit Reference

## Format

```text
<emoji>[book|examples|...][<type>]: <message>
```

## Scopes

| Scope | Use when the change is mainly in |
|-------|----------------------------------|
| `book` | LaTeX source, TikZ, bibliography |
| `website` | Vue monorepo under `website/` |
| `animations` | Manim library or scenes |
| `ppts` | PowerPoint decks |
| `examples` | Example programs |
| `ci` | GitHub Actions, hooks, `scripts/git/` |
| `docs` | README, governance, templates that are documentation |
| `repo` | Cross-cutting root files, labels, ignore rules |

Pick the **primary** scope. Do not invent extra scopes.

## Emoji and Type Mapping

| Emoji | Type | Use when |
|-------|------|----------|
| ✨ | `feat` | New chapter, page, scene, or capability |
| 🐛 | `fix` | Bug fix or factual correction |
| 📝 | `docs` | README, governance, comments-only changes |
| ♻️ | `refactor` | Restructure without changing behavior |
| ✅ | `test` | Add or update tests |
| 🔧 | `chore` | Maintenance, config, tooling, `.gitignore` |
| 🎨 | `style` | Formatting, whitespace, no logic change |
| ⚡ | `perf` | Performance improvement |
| 👷 | `ci` | CI/CD pipeline changes |
| 📦 | `build` | Build system, packaging, dependencies |
| ⏪ | `revert` | Revert a previous commit |
| 🏗️ | `chore` | Initial scaffold or structural setup |
| 🔒 | `fix` | Security fix |
| 🗑️ | `chore` | Remove dead code or files |
| 🔀 | `chore` | Merge-related commits (rare; prefer GitHub merge commits) |

When two types fit, prefer the one that best describes **why** the change exists.

## Message Quality

**Good**

```text
✨[book][feat]: add jacobian derivation for backprop
📝[docs][docs]: clarify release branch protection
🐛[website][fix]: point reader at copied dark pdf
```

**Bad**

```text
update files
✨(feat): add chapter
✨[book][feat]: Added new stuff.
fix bug
✨[book][feat]: 添加新章节
```

Rules for bad examples:

- Not English
- Old `emoji(type):` format or missing `[scope][type]`
- Past tense or trailing period
- Too vague to understand intent

## 500-Line Limit Details

Counted via `git diff --cached --numstat`:

- Each text file: `insertions + deletions`
- Binary file: counts as 1 line if listed
- **`CHANGELOG.md` is included**
- There is no exclusion list
- Untracked files are not counted until staged

If exactly at 500 lines, the check passes. At 501+, split the commit.

## Commit Body (Optional)

Use only when the subject alone is insufficient:

```text
✨[book][feat]: add score field figure to diffusion chapter

The figure shows the toy 1D mixture used in examples/.
It is generated from TikZ, not a screenshot.
```

Body rules:

- English only
- Wrap at ~72 characters per line when practical
- Explain **why**, not a raw file manifest
