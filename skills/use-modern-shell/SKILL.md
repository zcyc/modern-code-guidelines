---
name: use-modern-shell
description: "Use for POSIX sh/Bash code and reviews: quoting, processes, errors, and portable utilities."
---

# Shell

Resolve the changed file's target from shebang, invocation, CI/container and documented shell version plus utility implementations. Interactive shell is not the script runtime; unknown target uses POSIX syntax.

Respect the declared target range; if unknown, report it and avoid version-gated APIs. Verify gated APIs in official versioned docs. Installed tools do not establish the target. Keep unrelated migrations/config changes out of local fixes. Preview/experimental features require explicit project opt-in.

Read [references/guidelines.md](references/guidelines.md) before applying rules. Run the project's existing checks for the changed behavior.
