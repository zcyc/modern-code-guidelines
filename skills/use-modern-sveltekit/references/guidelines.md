# Svelte and SvelteKit

## Core Svelte

- Svelte 5 runes: $state owns state, $derived computes values, $effect synchronizes external systems with cleanup. Preserve legacy component mode unless intentionally migrating; legacy $: cannot be mixed into runes mode.
- Standalone Svelte uses the selected bundler/runtime; SvelteKit file routes, load and $app modules are unavailable there.

## SvelteKit only

- $app/state requires SvelteKit 2.12+ and Svelte 5; reactive reads need runes. Keep legacy $app/stores until that component's migration is intentional.
- load/event.fetch preserve SSR cookies, dependency tracking and invalidation. Private reads belong in +page.server/+layout.server; endpoints in +server and request auth/locals in hooks.server. Universal modules must not import credentials/private clients.
- Form actions are server POST mutations; validate and authorize per operation, and use use:enhance only for progressive enhancement. Client fetch fits non-form interactions.
- Match prerender/SSR/CSR and adapter to deployment; Node APIs need a Node-capable runtime. Avoid module-global request/user state during SSR.

## Sources

- https://svelte.dev/docs/svelte/what-are-runes
- https://svelte.dev/docs/kit/load
- https://svelte.dev/docs/kit/form-actions
- https://svelte.dev/docs/kit/hooks
- https://svelte.dev/docs/kit/$app-state
- https://svelte.dev/docs/kit/adapter-auto
