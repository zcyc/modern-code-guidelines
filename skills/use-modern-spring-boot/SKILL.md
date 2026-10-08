---
name: use-modern-spring-boot
description: "Use when writing or reviewing code involving Spring Boot injection, transactions, security, and execution models."
---

# Spring Boot

Resolve the changed file's target from pom.xml/build.gradle(.kts), dependency management/locks, Boot/Framework, Java/Kotlin toolchain, MVC vs WebFlux, native-image and virtual-thread settings.

Use only features supported by the declared target/range; report unknowns and verify gated APIs against official versioned docs. Local tools are not target evidence. Keep migrations and unrelated configuration changes outside a local fix. Preview/experimental features require explicit project opt-in.

Use use-modern-java or use-modern-kotlin for the source language.

Read [references/guidelines.md](references/guidelines.md) before applying rules. Run the project's existing checks for the changed behavior.
