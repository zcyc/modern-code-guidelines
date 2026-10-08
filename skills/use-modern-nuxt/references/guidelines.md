# Nuxt

## Version and rendering gates

- Nuxt 4 app/shared layout differs from Nuxt 3; inspect directory overrides/compatibility settings before moving files. Resolve Nitro preset and Node/edge capabilities separately.
- useFetch/useAsyncData supply SSR-aware payload/hydration handling; plain $fetch in universal setup may fetch twice. Direct $fetch fits events and server handlers.
- Make route freshness/cache/prerender choices explicit; verify production output for the selected Nuxt/Nitro version.

## Server boundaries

- server/api/server/routes and server utilities own private config/data; public runtime config is shipped to clients.
- Keep server handlers independent of Vue/app-only composables and validate/authorize requests. Universal composables need guarded browser APIs and per-request state rather than mutable module globals.
- Preserve pages/middleware/module conventions of the selected major instead of incidental migrations.

## Sources

- https://nuxt.com/docs/4.x/getting-started/data-fetching
- https://nuxt.com/docs/4.x/directory-structure/server
- https://nuxt.com/docs/4.x/guide/concepts/rendering
- https://nuxt.com/docs/4.x/guide/concepts/server-components
- https://nuxt.com/docs/4.x/getting-started/configuration
- https://nuxt.com/docs/3.x/getting-started/data-fetching
- https://nuxt.com/docs/3.x/directory-structure/server
- https://nuxt.com/docs/3.x/guide/concepts/rendering
