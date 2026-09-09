# Angular version rules

Resolve the Angular and TypeScript versions from the workspace before using
version-gated APIs. Angular's standalone, signal, template, and zoneless defaults
changed across majors.

## Version gates

- Standalone components are supported before Angular 19, but the default for
  new components changed in Angular 19. Set the option explicitly when the
  repository supports older majors; do not treat the default as a migration
  requirement.
- Signals are available from Angular 16. Built-in control flow and `@defer`
  require Angular 17 or later.
- Treat `resource`, `httpResource`, and Signal Forms as separately gated APIs.
  `httpResource` and Signal Forms are stable in Angular 22 and later; before
  that, use only the target's documented API and stability level.

## Standalone and templates

- Angular recommends standalone components for new code. Treat `NgModule` as a
  compatibility boundary for existing areas, not a reason to rewrite unrelated files.
- Use the control-flow syntax and input/output APIs supported by the target major;
  check the compiler and migration guides before changing templates.
- Use `@defer` when a real bundle or rendering benefit justifies a deferred view;
  provide explicit placeholder, loading, and error states.

## Signals and change detection

- Use `signal` for writable state and `computed` for pure derivation.
- Keep `effect` for external side effects, logging, persistence, or integration
  boundaries; do not use it to copy one signal into another.
- Zoneless applications require explicit Angular notifications. Signals read by a
  template, `AsyncPipe`, input updates, and `markForCheck` are valid notification paths.
- Test components under the project's actual change-detection mode.

## Signal-first async state and forms

- `resource` and `httpResource` are useful for reactive reads with loading,
  error, and reload state when the target supports them. Keep writes and
  mutations on the project's explicit HttpClient/service boundary.
- Signal Forms are a good fit for new signal-first forms when their validation
  and control model matches the feature. Do not rewrite stable reactive forms
  solely to adopt a newer API.

## Authority

- [Angular overview](https://angular.dev/overview)
- [Component anatomy](https://angular.dev/guide/components)
- [Signals](https://angular.dev/guide/signals)
- [Zoneless](https://angular.dev/guide/zoneless)
- [Standalone migration](https://angular.dev/reference/migrations/standalone)
- [`resource`](https://angular.dev/guide/signals/resource)
- [`httpResource`](https://angular.dev/api/common/http/httpResource)
- [Signal Forms](https://angular.dev/guide/forms/signals/overview)
