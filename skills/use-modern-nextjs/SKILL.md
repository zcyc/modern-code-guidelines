---
name: use-modern-nextjs
description: "Use version-aware Next.js routing, rendering, caching, security, and deployment idioms when writing, modifying, fixing, or reviewing Next.js code."
---

# Modern Next.js

Use for Next.js applications and libraries. Pair with `use-modern-react` for
React component rules, `use-modern-typescript` for type-system decisions, and
`modern-web-guidance` for browser-platform, CSS, accessibility, and performance
decisions.

## Target resolution

Read the nearest `package.json`, lockfile, `next.config.*`, and the router used
by the changed file. Establish the Next.js, React, Node.js, and deployment
targets before using version-sensitive routing, cache, or server APIs. Do not
infer behavior from a different Next.js project or a globally installed CLI.

## Working rules

- In the App Router, keep layouts and pages as Server Components by default;
  add `'use client'` only for interactivity, client hooks, or browser APIs.
- Keep secrets, request-bound data, and privileged access on the server. Treat a
  Client Component boundary as a data-exposure boundary, not just a rendering choice.
- Resolve the project's cache configuration before assuming whether data is
  static, cached, revalidated, or request-time. Make freshness and invalidation
  intent explicit.
- Use route-level `loading`, `error`, and `not-found` boundaries where the user
  can encounter those states; do not replace them with one global spinner.
- Prefer framework primitives for navigation, metadata, images, and route
  handlers when they match the project architecture.
- Do not migrate Pages Router code to App Router, or change rendering/cache
  semantics, unless the request includes that migration.

Read [references/guidelines.md](references/guidelines.md) for version-gated
App Router and cache rules.
