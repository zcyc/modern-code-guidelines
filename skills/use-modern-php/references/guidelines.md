# PHP version rules

Use these rules after resolving the Composer/runtime target. PHP syntax, bundled
extensions, and framework APIs are separate constraints.

## PHP 7+

- Use scalar, return, property, and nullable types when they express the actual
  contract; keep runtime validation at trust boundaries.
- Use `Throwable`-based exception handling and `DateTimeImmutable` for new time
  values.

## PHP 8.0+

- Use named arguments, attributes, constructor property promotion, union types,
  `match`, and the nullsafe operator when their semantics fit.
- Remember that `match` uses strict comparison and is exhaustive unless a default
  arm handles the remaining domain.

## PHP 8.1+

- Use enums for finite domain values and `readonly` properties where immutability
  is part of the invariant.
- Use fibers only through a framework/runtime abstraction that owns scheduling.

## PHP 8.2+

- Do not rely on dynamic properties in new code; declare the property or use an
  explicit data structure.
- Use readonly classes only when every property and inheritance constraint fits.

## PHP 8.3+

- Use typed class constants, `#[\Override]`, `json_validate`, and the improved
  `Random\Randomizer` APIs when they express the contract; do not use reflection
  or ad hoc JSON parsing to emulate them.

## PHP 8.4+

- Use property hooks and asymmetric visibility when they express the property's
  invariant directly; keep ordinary methods when validation has substantial flow.
- Use lazy objects and PDO driver-specific subclasses only when the lifecycle and
  database driver contract are explicit.

## PHP 8.5+

- Use the built-in URI APIs for standards-compliant URI parsing and normalization;
  do not treat `parse_url` as a complete URI validation policy.
- Use the pipe operator and `clone()` with property updates only when the chain or
  immutable-update semantics remain easier to review than named intermediate steps.
- Use `#[\NoDiscard]` on APIs whose ignored result is a likely correctness bug.

## Authority

- [PHP language manual](https://www.php.net/manual/en/langref.php)
- [PHP 8.0 new features](https://www.php.net/releases/8.0/en.php)
- [PHP 8.5 release](https://www.php.net/releases/8.5/en.php)
- [PHP 8.4 migration guide](https://www.php.net/migration84)
- [PHP 8.5 migration guide](https://www.php.net/migration85)
- [PHP enumerations](https://www.php.net/manual/en/language.enumerations.overview.php)
- [PHP-FIG PSR standards](https://www.php-fig.org/psr/)
