---
name: use-modern-astro
description: "Use version-aware Astro islands, content, routing, SSR, integrations, and deployment idioms when writing, modifying, fixing, or reviewing Astro code."
---

# Modern Astro

Use for Astro sites and applications. Pair with use-modern-typescript for
TypeScript rules and modern-web-guidance for browser, CSS, accessibility, and
performance.

## Target resolution

Read package.json, the lockfile, Astro version, output mode, adapter, framework
integrations, content sources, and deployment runtime. Resolve whether the
changed route is static, prerendered, or rendered on demand.

## Working rules

- Keep the static-by-default model. Add a framework island and a `client:*`
  directive only for behavior that truly needs client JavaScript.
- Use content collections/content-layer APIs supported by the project for typed
  content. Keep content schema and source loaders separate from page rendering.
- Prefer Astro Actions for type-safe, validated server mutations when the project
  supports them; use API endpoints when a real HTTP resource or external client
  contract is required.
- Choose prerendering or on-demand rendering per route and align the adapter
  with the deployment runtime. Do not use request-only APIs on a static route.
- Keep secrets and server-only data in frontmatter, server endpoints, or
  middleware; do not pass private values through island props or shipped code.
- Use middleware `locals` for request-scoped data when appropriate, and keep
  integrations/adapters aligned with the Astro target rather than adding a
  second rendering or routing layer.

Read references/guidelines.md before using version-sensitive content, SSR,
middleware, integration, or island behavior.
