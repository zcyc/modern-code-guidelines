---
name: use-modern-swiftdata
description: "Use version-aware SwiftData persistence, model-context isolation, schema migration, and Core Data interoperability idioms when writing, modifying, fixing, or reviewing Swift persistence code."
---

# Modern SwiftData

Use for SwiftData persistence and SwiftData/Core Data migration work. Pair with
`use-modern-swift` for Swift language, concurrency, and API-availability rules;
pair with `use-modern-swiftui`, `use-modern-uikit`, or `use-modern-appkit` when
the persistence layer is attached to a UI.

## Target resolution

Read the Swift language mode, Xcode and SDK versions, deployment targets, and
whether the target uses SwiftUI, UIKit, AppKit, CloudKit, or an existing Core
Data store. Establish the supported SwiftData availability before using macros,
query APIs, or migration features.


## Working rules

- Keep `@Model` types focused on persisted identity and relationships. Map
  network or presentation DTOs explicitly when their shape or lifetime differs
  from the stored schema.
- Own the `ModelContainer` at the application or feature boundary; do not create
  a new container from each view or request.
- Keep each `ModelContext` on its owning actor. Pass stable identifiers or
  `Sendable` value data across isolation boundaries instead of passing contexts or
  managed model instances between actors.
- Use `@ModelActor` or an equivalent actor-owned persistence boundary for
  background model access when the target supports it.
- Use `@Query` for UI-owned reads and explicit fetch descriptors for work outside
  a view. Make sorting, filtering, and identity part of the query contract.
- For shipped schema changes, use `VersionedSchema` and
  `SchemaMigrationPlan`; test representative existing stores before shipping a
  migration.
- Treat CloudKit synchronization and Core Data coexistence as explicit storage
  contracts. Do not assume every SwiftData model or relationship is portable to
  the selected backend.

Read `references/guidelines.md` for model ownership, concurrency, migrations,
availability, and Core Data interop rules.
