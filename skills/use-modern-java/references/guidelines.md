# Java version rules

Use this table after resolving the project's explicit Java target. These rules cover
stable features only unless marked `preview`.

## Java 8+

- Use `java.time` instead of `Date`/`Calendar` for new code.
- Use try-with-resources for every closeable resource.
- Prefer `List.of`/`Map.of` only when the target is 9+; on Java 8 use existing project conventions.
- Use `Optional` at API boundaries where absence is part of the contract, not as a field or method-parameter substitute everywhere.
- Prefer `computeIfAbsent`, `merge`, `getOrDefault`, and `String.join` over equivalent manual boilerplate.

## Java 9+

- Treat JDK internals as unavailable; use supported `java.*` APIs and module boundaries.
- Prefer `List.of`, `Set.of`, `Map.of`, `Collectors.filtering`, and `Collectors.flatMapping` where they make the code clearer.

## Java 10+

- Use local-variable type inference (`var`) when the initializer communicates the exact type without reading distant context.

## Java 14+

- Prefer switch expressions when a branch computes a value.

```java
String label = switch (status) {
    case READY -> "ready";
    case FAILED -> "failed";
};
```

## Java 15+

- Use text blocks for multi-line SQL, JSON, templates, and test fixtures when they improve readability.

## Java 16+

- Use records for transparent immutable data carriers.
- Use pattern matching for `instanceof` when it removes a redundant cast.

## Java 17+

- Use sealed classes/interfaces when a hierarchy is intentionally closed and exhaustive handling matters.
- Prefer the standard immutable collection factories and `Stream.toList()` where their mutability contract is appropriate.

## Java 21+

- Use record patterns and pattern matching for switch for exhaustive domain transformations.
- Use virtual threads for large numbers of mostly-blocking tasks; keep bounded pools for scarce external resources.
- Use sequenced collection APIs when code needs first/last/reversed access across collection types.

## Java 22+

- Use unnamed variables and patterns (`_`) when a matched value is deliberately unused.
- Treat string templates as unavailable: they were Java 21/22 previews and were withdrawn in Java 23; do not recommend them.

## Java 25+

- Use module import declarations when they make imports clearer and the target supports them; they do not require the source file to belong to an explicit module.
- Use compact source files and instance `main` methods for small scripts/examples, not public application APIs.
- Use flexible constructor bodies only when pre-super validation or field preparation materially improves safety.
- Primitive patterns remain `preview`; use them only with an explicit preview build.

## Authority

- [Oracle Java language updates](https://docs.oracle.com/en/java/javase/25/language/java-language-changes-summary.html)
- [JEP 511: Module Import Declarations](https://openjdk.org/jeps/511)
- [Java Language Specification](https://docs.oracle.com/javase/specs/jls/se25/html/index.html)
- [Java SE 25 API documentation](https://docs.oracle.com/en/java/javase/25/docs/api/)
- [Oracle JDK migration guide](https://docs.oracle.com/en/java/javase/25/migrate/migrating-jdk-8-later-jdk-releases.html)
