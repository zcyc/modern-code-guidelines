---
name: use-modern-java
description: "Use version-aware Java language and standard-library idioms when writing, modifying, fixing, or reviewing Java code."
---

# Modern Java

Apply the newest stable Java idioms supported by the project's explicit target. Read
`references/guidelines.md` and use only the rules for that target or older stable
releases.

## Target resolution

Read the effective target from the project, including inherited Maven/Gradle
configuration, in this order:

1. A compiler `--release` value from Maven `maven.compiler.release`, compiler-plugin
   `<release>`, Gradle compiler arguments, or checked-in build/CI configuration.
2. Maven `maven.compiler.source` or Gradle toolchain `languageVersion`/source and
   target compatibility for the language level when `--release` is absent.

`source`/`target` and a toolchain language level do not by themselves constrain the
JDK API available at compile time. If no `--release` or equivalent API boundary is
declared, keep the language level and JDK API level separate, report the API target
as unknown, and do not claim that a newer standard-library API is available.

If the project declares more than one target, use the target of the module/file being
changed. If no target is declared, report that the Java target is unknown and avoid
version-gated syntax. Do not infer it from the installed JDK.

Preview features require an explicit `--enable-preview` target and must be labeled as
preview in the response. Do not introduce them into ordinary production code.

## Working rules

- Prefer standard-library APIs over hand-written equivalents when the target supports them.
- Use `var` only when the initializer makes the type immediately clear; keep public API types explicit.
- Prefer records for immutable data carriers, sealed hierarchies for closed domains, and pattern matching for data-oriented branching when the target supports them.
- Use virtual threads for high-concurrency blocking I/O, not as a blanket replacement for CPU-bound executors.
- Preserve existing public behavior and module boundaries while modernizing the smallest relevant diff.
- Do not rewrite a project to a newer JDK unless the user asks for an upgrade.
