---
name: use-modern-php
description: "Use for PHP code and reviews: language versions, types, standard-library APIs, and database safety."
---

# PHP

Resolve the changed file's target from composer.json require.php/config.platform.php, lockfile, .php-version, php.ini extensions, selected container/CI and framework constraints. Composer platform emulation is not proof of deployed PHP.

Respect the declared target range; if unknown, report it and avoid version-gated APIs. Verify gated APIs in official versioned docs. Installed tools do not establish the target. Keep unrelated migrations/config changes out of local fixes. Preview/experimental features require explicit project opt-in.

Read [references/guidelines.md](references/guidelines.md) before applying rules. Run the project's existing checks for the changed behavior.
