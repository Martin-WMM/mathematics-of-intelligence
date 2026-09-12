# Changelog

All notable changes to this project are recorded here.

Updates to this file **count toward the 500-line commit limit**.

## Unreleased

- Allow Dependabot branches into `main`, add weekly update files, and publish a security policy.
- Root README sections: Introduction, Updates / Features, Usage, Contributes.
- Book light and dark editions compile to a title page (title and author only).
- Website production build publishes to `deploy/web` when a pull request that touches `website/` is merged.
- Merged pull requests that change `book/` compile the PDFs and store them on `deploy/book` with Git LFS.
- CI `branch-name` now runs on pull requests and checks the head branch, not the merge ref.
- Book PDF publish resolves absolute paths so Git LFS upload can find the compiled files.
- Repository layout: LaTeX book, Vue website, Manim, PPTX, examples.
- GitHub governance: branch flow, issue and PR templates, labels, push checks.
- Documented how to create `release/<scope>` from `main` with the GitHub API.
