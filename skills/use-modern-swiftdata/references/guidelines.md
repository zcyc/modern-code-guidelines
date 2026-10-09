# SwiftData

## Availability

- Baseline: iOS/iPadOS 17, macOS 14, tvOS 17, watchOS 10, visionOS 1. Check individual API availability in the selected SDK; macros also need supporting Swift/Xcode.
- Existing Core Data/CloudKit stores have separate schema/backend contracts; preserve them during adoption.

## Models, queries and writes

- @Model declares persisted identity/relationships; use separate transport/presentation values when their shape/lifetime differs.
- Own ModelContainer at app or explicit feature scope and inject it. ModelContext stays on its owning actor; pass IDs/Sendable values, not managed instances/contexts, across actors.
- @ModelActor isolates an owned context through its model executor; it does not guarantee a background thread. @Query is for SwiftUI live reads; FetchDescriptor is for service/actor/command work with explicit predicate/sort/identity.
- Surface save failures and reconcile optimistic UI; transaction/command boundaries own writes. Keep network/migration/unbounded fetches out of repeatedly evaluated UI paths.

## Migration and sync

- VersionedSchema/SchemaMigrationPlan document shipped schema evolution; test lightweight/custom paths on representative existing stores before production migration.
- Verify CloudKit optionality/relationships/identifiers and sync behavior on supported OS versions; not every local model is backend-compatible.

## Sources

- https://developer.apple.com/documentation/swiftdata
- https://developer.apple.com/documentation/swiftdata/modelcontainer
- https://developer.apple.com/documentation/swiftdata/modelcontext
- https://developer.apple.com/documentation/swiftdata/modelactor
- https://developer.apple.com/documentation/swiftdata/modelexecutor
- https://developer.apple.com/documentation/swiftdata/schemamigrationplan
- https://developer.apple.com/documentation/coredata
