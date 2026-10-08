# Java

## Version gates

- 8: java.time, try-with-resources, computeIfAbsent/merge/getOrDefault and String.join. Optional models absence at return boundaries, not every field/parameter.
- 9: supported module boundaries, List/Set/Map.of and Collectors.filtering/flatMapping; keep collection mutability/null policies explicit.
- 10: local var when the initializer reveals the type.
- 14: switch expressions for value-producing branches.
- 15: text blocks for embedded text.
- 16: records and instanceof patterns.
- 17: sealed hierarchies and Stream.toList (unmodifiable result).
- 21: record/switch patterns, sequenced collections and virtual threads for high-concurrency blocking I/O; bound scarce external resources separately.
- 22: unnamed variables/patterns. String templates were withdrawn in 23; do not recommend them.
- 25: module imports (also in non-modular source), compact source/instance main for scripts, flexible constructor bodies for necessary pre-super work.
- 26: HttpClient HTTP/3 when required, with tested fallback; review final-field reflection restrictions and replace removed Applet APIs.
- Primitive patterns, structured concurrency, lazy constants and Vector API remain preview/incubator at the documented release; verify exact JDK status and explicit build opt-in.

Preserve public behavior/module boundaries; a local edit does not authorize a JDK upgrade. Keep CPU-bound execution separate from virtual-thread I/O; resource ownership remains explicit.

## Sources

- [Oracle Java language updates](https://docs.oracle.com/en/java/javase/26/language/java-language-changes-summary.html)
- [JDK 26 release notes](https://www.oracle.com/java/technologies/javase/26-relnote-issues.html)
- [JEP 511: Module Import Declarations](https://openjdk.org/jeps/511)
- [Java Language Specification](https://docs.oracle.com/javase/specs/jls/se26/html/index.html)
- [Java SE 26 API documentation](https://docs.oracle.com/en/java/javase/26/docs/api/)
- [Oracle JDK migration guide](https://docs.oracle.com/en/java/javase/26/migrate/migrating-jdk-8-later-jdk-releases.html)
