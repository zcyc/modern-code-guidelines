---
name: use-modern-spring-boot
description: "Use for Spring Boot code and reviews: injection, transactions, security, and MVC/WebFlux execution."
---

# Spring Boot

Resolve the changed file's target from pom.xml/build.gradle(.kts), dependency management/locks, Boot/Framework, Java/Kotlin toolchain, MVC vs WebFlux, native-image and virtual-thread settings.

Respect the declared target range; if unknown, report it and avoid version-gated APIs. Verify gated APIs in official versioned docs. Installed tools do not establish the target. Keep unrelated migrations/config changes out of local fixes. Preview/experimental features require explicit project opt-in.

Use use-modern-java or use-modern-kotlin for the source language.

Read [references/guidelines.md](references/guidelines.md) before applying rules. Run the project's existing checks for the changed behavior.
