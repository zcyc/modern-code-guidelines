---
name: use-modern-php
description: Use version-aware PHP language, type-system, standard-library, and secure database idioms when writing, modifying, fixing, or reviewing PHP code.
---

# Modern PHP

Apply stable PHP features supported by the package's declared runtime. Read
`references/guidelines.md` before using version-gated syntax or functions.

## Target resolution

Read the effective target from:

1. `composer.json` `require.php` and `config.platform.php`.
2. `.php-version`, `php.ini`, container, and CI declarations selected by the
   package.
3. The framework/runtime target when it constrains available APIs.

If the target is unknown, report it and avoid version-gated features. Do not infer
the target from the local PHP binary. Keep the package's autoloading and public API
contract intact.

## Working rules

- Use strict scalar/return/property types and validate untrusted input at the
  boundary; `declare(strict_types=1)` follows the repository's established policy.
- Prefer enums, readonly data, constructor property promotion, `match`, nullsafe
  access, and attributes when the target supports them and they clarify the model.
- Use `DateTimeImmutable`, `random_int`, standard exceptions, and standard library
  functions instead of hand-written equivalents.
- Use Composer autoloading and the project's PSR-12/static-analysis configuration;
  do not introduce a second coding standard for a local edit.
- Use prepared statements/parameter binding for database values. Never construct
  SQL by interpolating untrusted input.
- Keep error handling explicit and never suppress warnings or expose internal
  exceptions through a public response boundary.
