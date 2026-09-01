# Vue version rules

Resolve the project's Vue, TypeScript, and build-tool versions first. Vue 3 and
Vue 2 have different defaults and should not be blended in a partial rewrite.

## Vue 3 minor-version gates

- Vue 3.4 and later provide `defineModel`; use explicit props and emits on
  older targets.
- Vue 3.5 and later support reactive props destructuring in compiler-managed
  `<script setup>` code. Do not assume destructured props stay reactive on an
  older target.
- Core Reactivity Transform was removed in Vue 3.4. Use ordinary refs unless a
  separately configured macros package is an explicit project choice.

## Vue 3

- Prefer Composition API and `<script setup>` for new full-application code.
- Prefer `ref`/`computed` for focused reactive values and `reactive` for a
  cohesive object whose identity should remain stable.
- Use `toRef`/`toRefs` when destructuring would otherwise lose reactivity.
- Treat `watch` as an effect boundary, not a general-purpose way to derive state.
- Use typed `defineProps`, `defineEmits`, and other compiler macros only when the
  installed Vue version supports the syntax.
- Do not introduce the removed core Reactivity Transform (`$ref`, `$computed`,
  and related syntax). Use ordinary refs, or a macros package only when the
  repository explicitly chose and configured it.
- Prefer `defineModel` for a simple component `v-model` contract when supported;
  keep explicit props and emits when a reusable component needs a more visible
  or multi-step contract.

## TypeScript

- Keep the runtime declaration and the TypeScript declaration consistent when
  props or emits need runtime validation.
- Do not use complex type constructs that the SFC compiler cannot convert to
  runtime options; simplify the boundary or declare it explicitly.

## Authority

- [Vue introduction](https://vuejs.org/guide/introduction)
- [Composition API FAQ](https://vuejs.org/guide/extras/composition-api-faq)
- [Vue with TypeScript](https://vuejs.org/guide/typescript/overview)
- [Composables](https://vuejs.org/guide/reusability/composables)
