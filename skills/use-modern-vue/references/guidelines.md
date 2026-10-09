# Vue

## Gates

- Vue 3 new application SFCs prefer Composition API/script setup; local changes preserve existing Options API/Vue 2 style.
- 3.4: defineModel; Reactivity Transform removed from core (external macro packages are explicit dependencies).
- 3.5: compiler-managed reactive props destructuring in script setup. Earlier destructuring needs toRef/toRefs or preserved property access.
- Destructured props passed to watch/composables need getters, e.g. watch(() => foo, ...) or useComposable(() => foo); passing foo passes its current value, even in 3.5+.

## Reactivity and contracts

- ref owns focused values, reactive a cohesive identity, computed pure derivation; watch/watchEffect synchronizes external systems and cleans up subscriptions/async work.
- Props are readonly; avoid duplicate mirrored state. Declare props/emits explicitly; defineModel fits simple v-model contracts, explicit props/emits fit complex ones.
- SFC type declarations are not full runtime validation; keep boundary checks explicit and avoid types the installed compiler cannot convert to runtime options.
- Composables extract real reusable stateful logic; setup/templates stay free of unrelated side effects.

## Sources

- [Vue introduction](https://vuejs.org/guide/introduction)
- [Composition API FAQ](https://vuejs.org/guide/extras/composition-api-faq)
- [Vue with TypeScript](https://vuejs.org/guide/typescript/overview)
- [Composables](https://vuejs.org/guide/reusability/composables)
- [Passing destructured props into functions](https://vuejs.org/guide/components/props.html#passing-destructured-props-into-functions)
