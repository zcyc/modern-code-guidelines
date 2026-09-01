# Astro version rules

Resolve Astro, Vite, integrations, adapters, content sources, and deployment
runtime from the repository. Static, server, and hybrid behavior changes which
APIs are available at build time or request time.

## Feature gates

- Astro Actions require Astro 4.15 or later. Use them for typed server
  mutations only when the target exposes the API and the action boundary is
  appropriate.
- Astro Sessions require Astro 5.7 or later and a server-capable adapter or
  deployment. Static output cannot provide request-persistent sessions.
- Content collection and content-layer APIs have changed across Astro majors;
  resolve the installed target before changing schemas or loaders.

## Islands and rendering

- Astro components render on the server or at build time by default. Use a
  framework component with a deliberate `client:*` directive only when the
  browser needs interactivity.
- On-demand pages and endpoints require a compatible adapter. Keep cookies,
  request headers, sessions, and protected data on the server-rendered path.
- Match `output`, per-route `prerender`, server islands, and adapter settings to
  the deployment runtime; test the built output rather than relying on dev mode.
- Use server sessions for data that must persist across requests when the
  adapter/storage target supports them. They are not a replacement for a
  database, and edge middleware may have a different session contract.

## Content and request boundaries

- Prefer typed content collections and the content APIs supported by the target.
  Validate frontmatter or external content at the source boundary.
- Middleware can populate `Astro.locals` for request-specific data. Keep that
  data out of static assumptions and do not expose secrets through component
  props that become browser HTML or JavaScript.
- Astro Actions are a useful typed boundary for validated form or client
  mutations. Keep authorization in the action/server boundary and use an API
  endpoint when callers need a stable HTTP interface.

## Authority

- https://docs.astro.build/en/concepts/islands/
- https://docs.astro.build/en/guides/content-collections/
- https://docs.astro.build/en/guides/on-demand-rendering/
- https://docs.astro.build/en/guides/server-islands/
- https://docs.astro.build/en/guides/sessions/
- https://docs.astro.build/en/guides/actions/
- https://docs.astro.build/en/guides/middleware/
- https://docs.astro.build/en/guides/integrations-guide/
