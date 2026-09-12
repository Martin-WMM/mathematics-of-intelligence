#!/usr/bin/env bash
# Apply GitHub rulesets so release/* and main require pull requests.
# Requires: gh auth login, a configured origin.
set -euo pipefail

if ! command -v gh >/dev/null 2>&1; then
  echo "gh is not on PATH" >&2
  exit 1
fi

create_or_update() {
  local name="$1"
  local body="$2"
  local existing
  existing="$(gh api repos/:owner/:repo/rulesets --jq ".[] | select(.name==\"${name}\") | .id" || true)"
  if [ -n "${existing}" ]; then
    echo "Updating ruleset ${name} (${existing})"
    echo "${body}" | gh api --method PUT "repos/:owner/:repo/rulesets/${existing}" --input -
  else
    echo "Creating ruleset ${name}"
    echo "${body}" | gh api --method POST repos/:owner/:repo/rulesets --input -
  fi
}

create_or_update "protect-main" '{
  "name": "protect-main",
  "target": "branch",
  "enforcement": "active",
  "bypass_actors": [],
  "conditions": { "ref_name": { "include": ["refs/heads/main"], "exclude": [] } },
  "rules": [
    { "type": "deletion" },
    { "type": "non_fast_forward" },
    {
      "type": "pull_request",
      "parameters": {
        "required_approving_review_count": 0,
        "dismiss_stale_reviews_on_push": true,
        "require_code_owner_review": false,
        "require_last_push_approval": false,
        "required_review_thread_resolution": false
      }
    },
    {
      "type": "required_status_checks",
      "parameters": {
        "strict_required_status_checks_policy": false,
        "required_status_checks": [
          { "context": "commit-lint" },
          { "context": "pr-target" }
        ]
      }
    }
  ]
}'

create_or_update "protect-release" '{
  "name": "protect-release",
  "target": "branch",
  "enforcement": "active",
  "bypass_actors": [],
  "conditions": { "ref_name": { "include": ["refs/heads/release/**"], "exclude": [] } },
  "rules": [
    { "type": "deletion" },
    { "type": "non_fast_forward" },
    {
      "type": "pull_request",
      "parameters": {
        "required_approving_review_count": 0,
        "dismiss_stale_reviews_on_push": true,
        "require_code_owner_review": false,
        "require_last_push_approval": false,
        "required_review_thread_resolution": false
      }
    },
    {
      "type": "required_status_checks",
      "parameters": {
        "strict_required_status_checks_policy": false,
        "required_status_checks": [
          { "context": "protect-release" },
          { "context": "commit-lint" },
          { "context": "pr-target" }
        ]
      }
    }
  ]
}'

echo "Rulesets applied. deploy/* stays writable for GITHUB_TOKEN."
