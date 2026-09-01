---
name: use-modern-nuxt
description: "Use version-aware Nuxt routing, universal data fetching, rendering, server routes, runtime configuration, and deployment idioms when writing, modifying, fixing, or reviewing Nuxt code."
---

# Modern Nuxt

Use for Nuxt applications and modules. Pair with use-modern-vue for Vue
component rules, use-modern-typescript for TypeScript rules, and
modern-web-guidance for browser, CSS, accessibility, and performance rules.

## Target resolution

Read package.json, the lockfile, nuxt.config.*, the Nuxt major, the Node.js
target, and the Nitro/deployment preset. Establish the pages, server, and
middleware conventions used by the project before changing them.

## Working rules

- Keep server-only code in server routes or utilities and keep app code out of
  that boundary. Never expose private runtime configuration to the client.
- In universal setup code, prefer useFetch or useAsyncData for SSR-aware data
  loading. Use $fetch directly for event-driven browser requests or inside
  server handlers where duplicate hydration fetching is not a concern.
- Make rendering mode and route rules explicit for pages whose freshness,
  caching, or prerendering affects correctness.
- Keep composables SSR-safe: do not assume window, document, or per-request
  mutable state exists on the server.
- Use file-based pages, server/api routes, and route middleware according to the
  project's Nuxt major; do not migrate Nuxt generations incidentally.
- Match the project's Nuxt major when choosing directory conventions and server
  boundaries; do not copy Nuxt 4 `app/` structure into a Nuxt 3 project.

Read references/guidelines.md before using version-sensitive Nuxt, Nitro, or
server-components features.
