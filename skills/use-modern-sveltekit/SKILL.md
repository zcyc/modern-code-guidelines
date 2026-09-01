---
name: use-modern-sveltekit
description: "Use version-aware Svelte and SvelteKit runes, load, form-action, SSR, routing, and adapter idioms when writing, modifying, fixing, or reviewing SvelteKit code."
---

# Modern SvelteKit

Use for SvelteKit applications. Pair with use-modern-typescript for TypeScript
rules and modern-web-guidance for browser, CSS, accessibility, and performance.

## Target resolution

Read package.json, the lockfile, Svelte and SvelteKit versions, Vite config,
adapter, Node target, and whether the route is prerendered, server-rendered, or
client-only. Establish whether each component uses legacy syntax or Svelte 5
runes before changing its style.

## Working rules

- Use runes in new Svelte 5/runes-mode components. Do not mix `$:` legacy
  reactivity with rune-based state or `$app/state` without an explicit boundary.
- Keep server-only code in `+page.server`, `+layout.server`, `+server`, and
  hooks. Use `load` and `event.fetch` for route data so SSR, cookies, and
  invalidation remain part of the framework contract.
- Prefer form actions for HTML mutations and `use:enhance` for progressive
  enhancement. Validate and authorize on the server; use client fetch only when
  the interaction is not a normal form submission.
- Use `$app/state` with rune-derived values when the target supports it; do not
  copy old store-based page-state examples into rune code.
- Make prerendering, SSR, adapter output, and runtime-only APIs explicit. Never
  assume a Node API exists on an edge or static target.

Read references/guidelines.md before using version-sensitive runes, page state,
form actions, or adapter behavior.
