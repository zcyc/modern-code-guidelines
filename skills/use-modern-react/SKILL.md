---
name: use-modern-react
description: "Use version-aware React component, hook, compiler, and state-management idioms when writing, modifying, fixing, or reviewing React code."
---

# Modern React

Use for React primitives and components. Use `use-modern-nextjs` for Next.js
routing, server rendering, and framework data/cache behavior. Use
`modern-web-guidance` for browser APIs, CSS, accessibility, and web performance.

## Target resolution

Read the nearest `package.json`, lockfile, build configuration, and the React
package actually selected for the workspace. Establish the React version and
whether the React Compiler is enabled before using version-sensitive APIs or
compiler directives. Do not infer the target from the globally installed CLI.

## Working rules

- Keep components and hooks pure during render; perform external synchronization
  in effects and clean it up.
- Follow the Rules of Hooks. Do not conditionally call hooks or hide hook order
  behind ordinary control flow.
- Derive values during render or with `useMemo` only when profiling justifies it;
  do not use an effect to mirror derivable state.
- Give collections stable keys from domain identity, not array positions when
  items can be inserted, removed, or reordered.
- Prefer the project's configured React Compiler. Do not add manual memoization
  to new code without evidence; preserve existing memoization until tested.
- Keep client state, server state, and external-store subscriptions distinct;
  do not duplicate one source of truth across effects and local state.
- For async mutations, prefer the renderer-supported Actions primitives such as
  `useActionState`, `useOptimistic`, and form actions over effect-driven mirrors
  of pending, error, or optimistic state.

Read [references/guidelines.md](references/guidelines.md) before applying
version-gated React or compiler features.
