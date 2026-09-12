# Website

Vue 3 + pnpm workspace for the public introduction site and embedded PDF reader.

The book language is English. The site UI is internationalised (`en`, `zh-CN`).

## Workspace

```text
website/
├── apps/web              # public site
└── packages/
    ├── ui                # shadcn-style components + Tailwind tokens
    ├── i18n              # locale messages
    └── shared            # book TOC and thread types
```

This folder is the only pnpm workspace. LaTeX and Manim stay outside it.

## Stack

- Vue 3, Vue Router, Vite
- Tailwind CSS
- shadcn-vue patterns (`class-variance-authority`, `tailwind-merge`)
- vue-i18n

## Develop

```bash
cd website
pnpm install
pnpm dev
```

The reader looks for `apps/web/public/pdfs/book-light.pdf` and `book-dark.pdf`. Build those from `book/` first (`scripts/build.ps1 all`).

## Deploy

A merged pull request that changes `website/` runs `pnpm build` and publishes `website/apps/web/dist` to `deploy/web`. If `deploy/book` already has Git LFS PDFs, the workflow copies them into `public/pdfs` before the build. Do not push that branch by hand.
