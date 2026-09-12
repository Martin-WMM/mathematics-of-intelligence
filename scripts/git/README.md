# Git checks

Local and CI share these scripts.

| Script | Purpose |
|--------|---------|
| `check_commit_message.py` | `<emoji>[scope][type]: message` |
| `check_commit_size.py` | ≤ 500 changed lines, including `CHANGELOG.md` |
| `check_branch_name.py` | Branch naming rules |
| `check_pr_target.py` | Allowed PR base for each head kind |
| `check_push_range.py` | Lint every non-merge commit in a push or PR |
| `apply_github_rulesets.sh` | Create main/release rulesets via `gh` |

Enable local hooks (optional, do not change git config unless you want this):

```bash
git config core.hooksPath .githooks
```
