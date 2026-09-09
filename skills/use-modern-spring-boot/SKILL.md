---
name: use-modern-spring-boot
description: "Use version-aware Spring Boot web, data, security, observability, and concurrency idioms when writing, modifying, fixing, or reviewing Spring Boot code."
---

# Modern Spring Boot

Use for Spring Boot applications. Pair with use-modern-java for Java language
rules and use-modern-kotlin for Kotlin rules.

## Target resolution

Read the nearest pom.xml or build.gradle, lockfile/dependency management, Java
toolchain, and Spring Boot version. Establish whether the application uses
Spring MVC, WebFlux, servlet, reactive, native-image, or virtual-thread
execution before changing its model.

## Working rules

- Prefer constructor injection and immutable configuration; use
  ConfigurationProperties for grouped external configuration.
- Keep blocking and reactive execution models separate. Do not call blocking
  I/O from a WebFlux pipeline without an explicit boundary.
- Put transaction boundaries around business operations and remember that
  proxy-based annotations do not apply to self-invocation.
- Treat security, validation, and error responses as boundary behavior; preserve
  the project's established Spring Security configuration rather than weakening it.
- Use Actuator and Micrometer when the application needs operational signals;
  keep metric labels low-cardinality.
- Use virtual threads only when the declared JDK and workload support them and
  measurement shows a benefit. Do not assume they improve every workload.

Read references/guidelines.md before using version-gated Boot, framework, or
JDK integration features.
