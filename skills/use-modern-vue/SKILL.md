---
name: use-modern-vue
description: "Use version-aware Vue component, reactivity, Composition API, and TypeScript idioms when writing, modifying, fixing, or reviewing Vue code."
---

# Modern Vue

Use for core Vue and single-file components. For Nuxt-specific server routing
and deployment behavior, follow the project's Nuxt configuration and docs
separately. Use `use-modern-typescript` for TypeScript rules and
`modern-web-guidance` for browser, CSS, accessibility, and performance rules.

## Target resolution

Read the nearest `package.json`, lockfile, Vite/build configuration, and Vue
version. Establish whether the file is a Vue 3 SFC, a legacy Vue 2 module, or
part of a framework wrapper before changing its API style.

## Working rules

- For new Vue 3 application code, prefer Composition API with `<script setup>`;
  preserve Options API in existing code unless migration is requested.
- Use `computed` for derived state and `watch`/`watchEffect` for synchronization
  with external systems. Clean up watchers and async work when their scope ends.
- Preserve reactivity: do not destructure reactive objects casually, mutate
  readonly props, or create duplicate local state that mirrors a prop.
- Declare component props and emitted events explicitly. Keep runtime validation
  and TypeScript contracts aligned at trust boundaries.
- Keep templates and setup code free of unrelated side effects; move reusable
  stateful logic into composables when it has a real second consumer.

Read [references/guidelines.md](references/guidelines.md) before using
version-sensitive macros or reactivity APIs.
