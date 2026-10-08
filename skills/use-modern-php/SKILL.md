---
name: use-modern-php
description: "Use when writing or reviewing code involving PHP language versions, typing, standard APIs, and database safety."
---

# PHP

Resolve the changed file's target from composer.json require.php/config.platform.php, lockfile, .php-version, php.ini extensions, selected container/CI and framework constraints. Composer platform emulation is not proof of deployed PHP.

Use only features supported by the declared target/range; report unknowns and verify gated APIs against official versioned docs. Local tools are not target evidence. Keep migrations and unrelated configuration changes outside a local fix. Preview/experimental features require explicit project opt-in.

Read [references/guidelines.md](references/guidelines.md) before applying rules. Run the project's existing checks for the changed behavior.
