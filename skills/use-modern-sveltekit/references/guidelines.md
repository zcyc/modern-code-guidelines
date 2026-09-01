# SvelteKit version rules

Resolve Svelte, SvelteKit, Vite, adapter, Node.js, and deployment targets from
the repository. Svelte 5 runes and SvelteKit's newer state APIs are not drop-in
syntax for legacy components.

## Svelte 5 gate

- Runes and `$app/state` require the Svelte 5/SvelteKit target that exposes
  them. Keep legacy store-based code on `$app/stores` unless the change is an
  intentional migration of that component or route.

## Components and page state

- Use `$state`, `$derived`, and `$effect` in rune-mode components. Keep `$effect`
  for synchronization with external systems, not for copying derived values.
- In Svelte 5 applications, `$app/state` exposes reactive page and navigation
  state; derive values with runes. `$app/stores` is the older store-based path.

## Server data and mutations

- Use `load` for route data and `+page.server`/`+layout.server` for server-only
  reads. Use `event.fetch` so cookies, SSR requests, and invalidation behave as
  SvelteKit expects.
- Form actions provide a native POST path that works without JavaScript. Add
  `use:enhance` when client-side progressive enhancement is useful, not as a
  substitute for server validation.
- Keep credentials and private clients out of universal modules and browser
  bundles. Use `hooks.server` for request-level auth and locals.

## Authority

- https://svelte.dev/docs/svelte/what-are-runes
- https://svelte.dev/docs/kit/load
- https://svelte.dev/docs/kit/form-actions
- https://svelte.dev/docs/kit/hooks
- https://svelte.dev/docs/kit/$app-state
- https://svelte.dev/docs/kit/adapter-auto
