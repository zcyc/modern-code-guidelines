# React version rules

Read the project's declared React and build-tool versions before applying these
rules. React documentation separates the selected major from archived majors;
do not assume an API is available because the editor autocomplete shows it.

## React 19+

- Treat render purity as a correctness requirement; it is also required for
  compiler optimization.
- Prefer React primitives supported by the project's renderer and
  framework. Do not mix server-component conventions into a client-only app.

## React 19.2+

- Use `useEffectEvent` when an effect needs the latest non-reactive value without
  making that value an effect trigger. It does not make an effect safe to omit
  real dependencies.
- Use `Activity` only when the target renderer supports it and preserving the
  hidden subtree's state is useful; do not replace ordinary conditional
  rendering with it by default.

## React 19.3+

- Use `<ViewTransition>` for enter, exit, shared-element, or update animations
  coordinated by React transitions or Suspense. It is currently a DOM-only API;
  let React coordinate the browser view transition instead of calling
  `document.startViewTransition` for the same update.
- Use an explicit `<Fragment ref={...}>` when a group of DOM children needs
  focus, event, observer, measurement, or scrolling behavior without a wrapper.
  Its `FragmentInstance` targets first-level host children, and the shorthand
  `<>...</>` cannot receive the ref.
- For a component that has no meaningful server-rendered output, prefer
  `use(browser(reason))` inside a `<Suspense>` boundary over mounted flags or
  `typeof window` checks. This is a React DOM API; in an RSC app, call it only
  from a Client Component.
- When Trusted Types are enforced, pass `TrustedHTML` through
  `dangerouslySetInnerHTML` without stringifying it, while keeping sanitization
  in the application's security policy. React's support does not make unsafe
  HTML safe.
- In an RSC-capable framework, a Server Component may render a Context imported
  from a `'use client'` module directly. Keep this within the framework's RSC
  contract; it does not change how Context works in client-only apps.

## React 19 actions

- Use `useActionState` and `useOptimistic` when they express an async mutation's
  pending, error, or optimistic state. Keep server actions and client-only form
  flows within the renderer and framework contract that the project actually
  uses.

## React Compiler

- If the project enables the compiler, rely on compiler memoization for new code
  and use `useMemo`, `useCallback`, or `memo` only for a measured need or an
  explicit identity contract.
- Keep existing manual memoization until the compiled output and behavior have
  been tested. Use compiler opt-out directives only for a documented incompatibility.
- The compiler must run before other Babel transforms that change the source it analyzes.

## Authority

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
