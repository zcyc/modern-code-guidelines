---
name: use-modern-angular
description: "Use version-aware Angular component, signals, standalone, template, and change-detection idioms when writing, modifying, fixing, or reviewing Angular code."
---

# Modern Angular

Use for Angular applications and libraries. Use `use-modern-typescript` for
TypeScript decisions and `modern-web-guidance` for browser, CSS, accessibility,
and performance decisions.

## Target resolution

Read `package.json`, lockfile, `angular.json`, the project's TypeScript config,
and the Angular version. Establish whether the changed area uses standalone
components, NgModules, SSR, or zoneless change detection before changing its
style.

## Working rules

- Use standalone components, directives, and pipes for new code when the target
  supports them; do not perform a whole-project NgModule migration unless asked.
- Use signals for local synchronous state and `computed` for derivation. Use
  `effect` for synchronization with external systems, not for ordinary state propagation.
- Keep components focused on view state and user interaction; preserve the
  project's established service and injection boundaries.
- Write components compatible with `OnPush` and zoneless notification rules:
  make state changes observable through signals, inputs, async pipes, or explicit
  change-detection APIs.
- Use the project's supported template control-flow and input/output APIs; do not
  introduce syntax gated to a newer Angular major.
- For new signal-first async state or forms, prefer the supported `resource`,
  `httpResource`, and Signal Forms APIs when they fit; keep mutations explicit
  and do not force existing reactive forms to migrate.
- Preserve existing NgModule or ZoneJS code when the task is local and no
  migration was requested.

Read [references/guidelines.md](references/guidelines.md) for version-gated
standalone, signals, and zoneless rules.
