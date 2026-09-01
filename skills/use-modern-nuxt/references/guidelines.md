# Nuxt version rules

Resolve Nuxt, Vue, Nitro, Node.js, and deployment preset versions from the
repository. Nuxt 3 and 4 documentation and directory conventions can differ.

## Major-version gate

- Nuxt 4's `app/` and `shared/` conventions are not a drop-in layout for Nuxt
  3. Resolve the actual directory structure and any compatibility-version
  setting before moving files or copying module examples.

## Data and rendering

- useFetch and useAsyncData are the SSR-aware choices for universal setup code;
  direct $fetch in setup can duplicate a request during hydration.
- Use direct $fetch for event-driven browser requests and server handlers when
  the universal payload de-duplication behavior is not needed.
- Make route rendering and caching decisions explicit with the features
  supported by the installed Nuxt/Nitro version.

## Server boundary

- Files under server/api and server/routes are server code. Do not import Vue
  components, app-only composables, or client state into them.
- Keep private runtime configuration server-only. Public runtime configuration
  is still shipped to the client and must be treated as non-secret.
- Keep composables safe in both environments: avoid unguarded window/document
  access and module-global mutable state that could leak across requests.

## Authority

- https://nuxt.com/docs/4.x/getting-started/data-fetching
- https://nuxt.com/docs/4.x/directory-structure/server
- https://nuxt.com/docs/4.x/guide/concepts/rendering
- https://nuxt.com/docs/4.x/guide/concepts/server-components
- https://nuxt.com/docs/4.x/getting-started/configuration
- https://nuxt.com/docs/3.x/getting-started/data-fetching
- https://nuxt.com/docs/3.x/directory-structure/server
- https://nuxt.com/docs/3.x/guide/concepts/rendering
