# SwiftData version rules

Resolve the Swift language mode, Xcode, SDK, deployment target, and persistence
backend before using SwiftData APIs. SwiftData availability, Swift macro support,
and Core Data store compatibility are separate constraints.

## Availability

- Treat SwiftData as SDK and deployment-target gated. For earlier targets, keep
  Core Data or the project's existing persistence layer explicit instead of hiding
  the difference behind a broad compatibility layer.

## Model and context ownership

- Treat `@Model` as a persistence schema declaration, not as a universal domain
  model. Keep transient transport and presentation types separate when that
  makes boundaries clearer.
- Create one application-owned `ModelContainer` or one explicitly scoped feature
  container. Inject it into views and services rather than constructing it deep in
  a view hierarchy.
- Keep a `ModelContext` on the actor that owns it. UI contexts normally belong to
  the main actor; background work should use an explicitly owned context and pass
  value data or identifiers across actors.
- Prefer `@ModelActor` for a background persistence boundary when the target
  supports it; keep the actor's context and model operations together.
- Keep fetches explicit about sort order and predicates. Never use array position
  as the identity of a persisted entity.

## Queries and writes

- Use `@Query` when a SwiftUI view owns a live query. Use `FetchDescriptor` or an
  explicit repository boundary when a service, actor, or command owns the work.
- Keep writes inside a clear transaction or command boundary and surface save
  errors. Do not hide persistence failures behind an optimistic UI update with no
  reconciliation path.
- Avoid doing network, migration, or unbounded fetch work from `body` or another
  repeatedly evaluated view path.

## Migration and interoperability

- For changes to shipped stores, use `VersionedSchema` and
  `SchemaMigrationPlan`. Exercise lightweight and custom migration paths against
  copies of real legacy stores before changing production data.
- Keep Core Data interop explicit. Preserve the existing store and migration
  contract when adopting SwiftData incrementally; do not replace a mature Core
  Data stack just to remove boilerplate.
- Treat CloudKit as a separate availability and schema contract. Validate
  optionality, relationships, identifiers, and sync behavior on the supported
  OS versions before enabling it for user data.

## Authority

- https://developer.apple.com/documentation/swiftdata
- https://developer.apple.com/documentation/swiftdata/modelcontainer
- https://developer.apple.com/documentation/swiftdata/modelcontext
- https://developer.apple.com/documentation/swiftdata/modelactor
- https://developer.apple.com/documentation/swiftdata/schemamigrationplan
- https://developer.apple.com/documentation/coredata
