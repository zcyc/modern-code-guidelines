# Next.js version rules

Read `package.json`, `next.config.*`, and the router layout before applying these
rules. App Router and Pages Router have different data-fetching and lifecycle
models; preserve the router already used by the file.

## Router and release gates

- On Next.js 16 and later, use the `proxy.ts` convention for the supported
  Node-runtime request interception path. Older targets may require
  `middleware.ts`; resolve the installed major before renaming either file.
- `cacheComponents`, `use cache`, `cacheLife`, and `cacheTag` are target- and
  configuration-gated. Do not infer their behavior from an older App Router
  example or from development mode.

## App Router

- Server Components are the default for layouts and pages. Client Components
  are for state, event handlers, effects, and browser-only APIs.
- Pass serializable props across the server/client boundary. Keep credentials,
  database clients, and authorization checks out of client modules.
- Use `loading.tsx`, `error.tsx`, and `not-found.tsx` boundaries where the route
  needs independent streaming or failure behavior.

## Cache-sensitive releases

- Check the installed Next.js version and `cacheComponents` configuration before
  using `use cache`, `cacheLife`, `cacheTag`, or related APIs.
- When a cached scope needs request data such as cookies or headers, read it
  outside the cached scope and pass the relevant value as an argument.
- Validate cache invalidation and freshness with a production-like build; a
  development request is not evidence of production cache behavior.

## Request interception

- Use the target's request-interception convention for redirects, rewrites, and
  lightweight prechecks. Keep data fetching and long-running authorization work
  outside that boundary.

## Authority

- [App Router](https://nextjs.org/docs/app)
- [Server and Client Components](https://nextjs.org/docs/app/getting-started/server-and-client-components)
- [`use cache`](https://nextjs.org/docs/app/api-reference/directives/use-cache)
- [Cache Components](https://nextjs.org/docs/app/getting-started/partial-prerendering)
- [Proxy](https://nextjs.org/docs/app/api-reference/file-conventions/proxy)
