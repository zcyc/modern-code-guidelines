# Next.js

## Router and cache gates

- Preserve App vs Pages Router. App layouts/pages default to Server Components; Client Components own interactive state/effects/browser access.
- Next 16+ uses proxy.ts for supported Node request interception; older middleware.ts/edge paths have different contracts. Keep interception lightweight.
- cacheComponents/use cache/cacheLife/cacheTag require matching release/config. Read cookies/headers outside cached scopes and pass relevant values in; never share user-private results through an insufficient cache key.
- Verify freshness/invalidation and static/request-time behavior in a production-like build, not dev mode.

## Server boundaries

- Client props must be serializable and safe to disclose; keep credentials/database clients server-only. A client module can still prerender on the server, so unguarded browser APIs remain unsafe during render.
- Treat every Server Action/route handler as a directly callable entry: validate arguments, authenticate and authorize the specific resource in that call or its server-only data layer. Page/layout/proxy checks alone do not protect actions.
- Return only needed fields; action IDs, hidden UI and encryption are not authorization. Keep server-only modules out of client imports.
- Use loading/error/not-found boundaries where independent streaming/failure is needed; framework navigation/metadata/images preserve router behavior.

## Sources

- [App Router](https://nextjs.org/docs/app)
- [Server and Client Components](https://nextjs.org/docs/app/getting-started/server-and-client-components)
- [`use cache`](https://nextjs.org/docs/app/api-reference/directives/use-cache)
- [Cache Components](https://nextjs.org/docs/app/getting-started/partial-prerendering)
- [Proxy](https://nextjs.org/docs/app/api-reference/file-conventions/proxy)
- [Data security](https://nextjs.org/docs/app/guides/data-security)
