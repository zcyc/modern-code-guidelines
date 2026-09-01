# React version rules

Read the project's declared React and build-tool versions before applying these
rules. React documentation tracks the latest major separately from archived
majors; do not assume an API is available because the editor autocomplete shows it.

## React 19+

- Treat render purity as a correctness requirement; it is also required for
  compiler optimization.
- Prefer the current React primitives supported by the project's renderer and
  framework. Do not mix server-component conventions into a client-only app.

## Actions and effect events

- Use `useActionState` and `useOptimistic` when they express an async mutation's
  pending, error, or optimistic state. Keep server actions and client-only form
  flows within the renderer and framework contract that the project actually
  uses.
- Use `useEffectEvent` when an effect needs the latest non-reactive value without
  making that value an effect trigger. It does not make an effect safe to omit
  real dependencies.
- Use `Activity` only when the target renderer supports it and preserving the
  hidden subtree's state is useful; do not replace ordinary conditional
  rendering with it by default.

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
- [React 19.2](https://react.dev/blog/2025/10/01/react-19-2)
