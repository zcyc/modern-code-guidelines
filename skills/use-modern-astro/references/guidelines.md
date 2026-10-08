# Astro

## Gates

- Actions: 4.15+; Sessions: 5.7+ with a server-capable adapter/storage. Content collection/content-layer schemas and loaders depend on the installed major.
- Astro 6: Node 22+, Vite 7/Zod 4; content schemas use astro/zod rather than old astro:content imports.
- Astro 7: Vite 8/Rolldown and Rust compiler defaults; test parsing/whitespace changes, custom integrations and non-Node adapters. Route caching needs an explicit freshness/invalidation contract and compatible provider.

## Rendering and boundaries

- Default to static/server-rendered components; client:* islands only for browser interaction. Match output/prerender/server islands to adapter/runtime and verify built output.
- Static routes cannot supply request-time cookies/headers/sessions. Sessions are request-persistent state, not a database; check edge middleware's storage contract.
- Validate content at typed collection/loader boundaries. Use actions for validated server mutations and endpoints for stable HTTP/external-client contracts; authorize both.
- Frontmatter is server/build code, but rendered HTML and island props are public. Keep secrets out of both; locals owns request-scoped middleware data.

## Sources

- https://astro.build/blog/astro-7/
- https://astro.build/blog/astro-6/
- https://docs.astro.build/en/concepts/islands/
- https://docs.astro.build/en/guides/content-collections/
- https://docs.astro.build/en/guides/on-demand-rendering/
- https://docs.astro.build/en/guides/server-islands/
- https://docs.astro.build/en/guides/sessions/
- https://docs.astro.build/en/guides/actions/
- https://docs.astro.build/en/guides/middleware/
- https://docs.astro.build/en/guides/integrations-guide/
