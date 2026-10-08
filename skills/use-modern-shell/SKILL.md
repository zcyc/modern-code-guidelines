---
name: use-modern-shell
description: "Use when writing or reviewing code involving POSIX sh and Bash scripts, quoting, processes, and portable utilities."
---

# Shell

Resolve the changed file's target from shebang, invocation, CI/container and documented shell version plus utility implementations. Interactive shell is not the script runtime; unknown target uses POSIX syntax.

Use only features supported by the declared target/range; report unknowns and verify gated APIs against official versioned docs. Local tools are not target evidence. Keep migrations and unrelated configuration changes outside a local fix. Preview/experimental features require explicit project opt-in.

Read [references/guidelines.md](references/guidelines.md) before applying rules. Run the project's existing checks for the changed behavior.
