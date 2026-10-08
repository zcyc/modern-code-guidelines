# SwiftUI

## Availability

- NavigationStack/NavigationSplitView require iOS/iPadOS 16, macOS 13, tvOS 16 or watchOS 9 (visionOS 1). Check individual overloads separately.
- Observation reference models (@Observable/@Bindable) require iOS/iPadOS 17, macOS 14, tvOS 17 or watchOS 10 (visionOS 1); earlier deployments retain supported model-data APIs.

## State and lifecycle

- body is a pure value description: no network/persistence side effects. Narrow owners hold state; bindings edit parent-owned state, environment/Observation share models.
- Stable domain IDs preserve ForEach/navigation identity; indices or regenerated UUIDs lose state during changes. Restoration/deep-link route values stay lightweight and codable when needed.
- task/task(id:) owns cancellable async work; stable identity prevents duplicate/obsolete loads. Propagate errors/cancellation and update UI on required MainActor isolation.
- Build for Dynamic Type, localization, accessibility and supported layouts. UIKit/AppKit representables forward updates and release owned resources; keep hosting boundaries explicit.

## Sources

- https://developer.apple.com/documentation/SwiftUI
- https://developer.apple.com/documentation/swiftui/model-data
- https://developer.apple.com/documentation/swiftui/navigationstack
- https://developer.apple.com/documentation/swiftui/task
- https://developer.apple.com/documentation/swiftui/foreach
- https://developer.apple.com/design/human-interface-guidelines
