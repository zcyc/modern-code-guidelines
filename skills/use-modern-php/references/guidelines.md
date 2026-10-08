# PHP

## Gates

- 7.0: scalar/return types and Throwable; DateTimeImmutable predates PHP 7.
- 7.1: nullable parameter/return types; 7.4: typed properties.
- 8.0: named arguments, attributes, promoted constructor properties, unions, nullsafe access and match (strict comparison/exhaustive unless default).
- 8.1: enums, readonly properties and fibers; fibers need a runtime-owned scheduler.
- 8.2: readonly classes with compatible inheritance/property contracts; declare properties instead of relying on deprecated dynamic ones.
- 8.3: typed constants, Override, json_validate and newer Randomizer APIs.
- 8.4: property hooks/asymmetric visibility, lazy objects and PDO driver-specific subclasses; expose lifecycle/driver constraints.
- 8.5: URI APIs, pipe operator, clone() property updates and NoDiscard. URI parsing is not a full application validation policy.

## Boundaries

- declare(strict_types=1) follows repository policy; validate untrusted input regardless of declarations. Use DateTimeImmutable for instants and random_int for security-sensitive randomness.
- Composer owns autoload/platform constraints; run existing PSR/static-analysis rules. Verify required extensions on deployment.
- Bind SQL values, surface operational failures and keep public responses free of internal exceptions; warning suppression is not error handling.

## Sources

- [PHP language manual](https://www.php.net/manual/en/langref.php)
- [PHP 8.0 new features](https://www.php.net/releases/8.0/en.php)
- [PHP 8.5 release](https://www.php.net/releases/8.5/en.php)
- [PHP 8.4 migration guide](https://www.php.net/migration84)
- [PHP 8.5 migration guide](https://www.php.net/migration85)
- [PHP enumerations](https://www.php.net/manual/en/language.enumerations.overview.php)
- [PHP-FIG PSR standards](https://www.php-fig.org/psr/)
- [PHP 7.1](https://www.php.net/manual/en/migration71.new-features.php)
- [PHP 7.4](https://www.php.net/manual/en/migration74.new-features.php)
