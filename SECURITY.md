# Security policy

## Reporting a vulnerability

This repository is public. Please do **not** open a public issue for a
security problem.

Use GitHub's private vulnerability reporting on this repository:

https://github.com/Martin-WMM/mathematics-of-intelligence/security/advisories/new

Include what is affected (website, CI, examples, or book build scripts), how
to reproduce it, and the impact. English is preferred.

You should get a first reply within a week. Please wait before discussing the
report in public.

## Supported versions

Only the default branch `main` is supported. Preview and deploy branches are
generated artifacts.

## What this project stores

The monograph source, a static Vue site, Manim helpers, and small examples.
There is no production API or user database. The highest-impact issues are
usually leaked tokens, a compromised GitHub Action, or a vulnerable frontend
dependency.
