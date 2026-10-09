---
name: use-modern-go
description: "Use for Go code and reviews: language versions, standard-library APIs, errors, and concurrency."
---

# Go

Resolve the changed file's target from package go.mod go/toolchain directives, go.work module selection, CI toolchain, build tags and platform. Module/file version gates differ from installed toolchain.

Respect the declared target range; if unknown, report it and avoid version-gated APIs. Verify gated APIs in official versioned docs. Installed tools do not establish the target. Keep unrelated migrations/config changes out of local fixes. Preview/experimental features require explicit project opt-in.

Read [references/guidelines.md](references/guidelines.md) before applying rules. Run the project's existing checks for the changed behavior.
