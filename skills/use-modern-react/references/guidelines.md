# React

## Components and state

- Keep render pure and Hooks order stable; effects synchronize external systems with cleanup, not derivable state. use is a resource-reading API that may appear in conditionals/loops, but not try/catch.
- Use domain keys for reorderable collections. Keep client state, remote data and external-store subscriptions as distinct sources of truth.
- Actions/useActionState/useOptimistic model mutations when the renderer supports them; client forms and server actions have different execution/security contracts.

## Gates

- React 19: Actions APIs; RSC behavior requires an RSC-capable framework, not just the React package.
- 19.2: useEffectEvent reads latest non-reactive values without hiding real dependencies; Activity preserves hidden state only on supporting renderers.
- 19.3 DOM: ViewTransition coordinates transition/Suspense animations; do not start a second browser transition for the same update. Explicit Fragment refs expose first-level host-child focus/events/observers/measurement/scrolling; shorthand fragments cannot receive refs.
- 19.3 DOM: use(browser(reason)) inside Suspense models components without useful SSR output; RSC apps call it in Client Components. Preserve TrustedHTML for dangerouslySetInnerHTML under Trusted Types; application sanitization still owns safety.
- 19.3 RSC: Server Components may render a Context imported from a client module; this does not enable reading client Context in Server Components.

## Compiler

- Run compiler before source-changing Babel transforms. With compiler enabled, new manual memoization needs measured benefit or an identity contract; retain existing memoization until behavior/compiled output is checked.
- Compiler opt-outs require documented incompatibility; ordinary derivation belongs in render, useMemo only when cost/identity justifies it.

## Sources

- [React versions](https://react.dev/versions)
- [Rules of React](https://react.dev/reference/rules)
- [React Compiler introduction](https://react.dev/learn/react-compiler/introduction)
- [React Compiler installation](https://react.dev/learn/react-compiler/installation)
- [React Actions](https://react.dev/reference/react/useActionState)
- [React 19.3](https://react.dev/blog/2026/09/09/react-19-3)
- [`<ViewTransition>`](https://react.dev/reference/react/ViewTransition)
- [`<Fragment>` and Fragment refs](https://react.dev/reference/react/Fragment)
- [`browser`](https://react.dev/reference/react-dom/browser)
- [React DOM common components and Trusted Types](https://react.dev/reference/react-dom/components/common)
