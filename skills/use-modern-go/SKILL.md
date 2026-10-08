---
name: use-modern-go
description: "Use when writing or reviewing code involving Go language versions, standard APIs, errors, and concurrency."
---

# Go

Resolve the changed file's target from package go.mod go/toolchain directives, go.work module selection, CI toolchain, build tags and platform. Module/file version gates differ from installed toolchain.

Use only features supported by the declared target/range; report unknowns and verify gated APIs against official versioned docs. Local tools are not target evidence. Keep migrations and unrelated configuration changes outside a local fix. Preview/experimental features require explicit project opt-in.

Read [references/guidelines.md](references/guidelines.md) before applying rules. Run the project's existing checks for the changed behavior.
