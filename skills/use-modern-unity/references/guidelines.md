# Unity

## Version-sensitive changes

Reviewed against official Unity 6.0–6.6 upgrade guides on 2026-10-29. These are coding-relevant changes, not an exhaustive release log. For upgrades, read each intervening guide and the exact Editor patch/package release notes; preview releases are not the stable baseline.

- Unity 6.1: custom URP shaders use `_CLUSTER_LIGHT_LOOP` in place of `_FORWARD_PLUS`. `Rigidbody.SetDensity` is deprecated; set mass deliberately rather than assuming per-collider density behavior. See the [6.1 upgrade guide](https://docs.unity.com/en-us/engine/6000.6/manual/upgrade-guides/upgrade-guide-unity61).
- Unity 6.2: URP `AfterRendering` now runs after the final back-buffer blit; use `AfterRenderingPostProcessing` for passes that need the preceding intermediate target. Replace deprecated `SetupRenderPasses` with Render Graph-based passes and `AddRenderPasses`. UI Toolkit transform writes use `style.translate/rotate/scale`, reads use `resolvedStyle`, replacing `VisualElement.transform`. See the [6.2 upgrade guide](https://docs.unity.com/en-us/engine/6000.6/manual/upgrade-guides/upgrade-guide-unity62).
- Unity 6.3: URP Compatibility Mode (the non-Render Graph path, deprecated in 6.0) is removed; `RenderGraphSettings.enableRenderCompatibilityMode` becomes read-only and returns false. Migrate custom passes to Render Graph in 6.0–6.2 before upgrading. The temporary `URP_COMPATIBILITY_MODE` migration define stops working in 6.4; it is not a shipping solution. See the [6.3 rendering upgrade guide](https://docs.unity.com/en-us/engine/6000.3/manual/upgrade-guides/upgrade-guide-unity63).
- Unity 6.4: importers/postprocessors must declare actual source and artifact dependencies with `DependsOnSourceAsset` and `DependsOnArtifact`. An unchanged imported artifact no longer propagates reimports merely because its source was reimported. Test incremental imports, not just a clean Library. See the [6.4 upgrade guide](https://docs.unity.com/en-us/engine/6000.6/manual/upgrade-guides/upgrade-guide-unity64).
- Unity 6.5: replace obsolete instance-ID APIs with their `EntityId` equivalents, carrying the full 64-bit ID through callers and dictionary keys; truncation loses identity. Unity supplies `System.Text.Json`, `System.Collections.Immutable`, `System.Reflection.Metadata` and `System.Runtime.CompilerServices.Unsafe`; audit dependencies against the engine-provided versions. CI should use an explicit `-logFile` or discover `Application.consoleLogPath`, since the default Editor log is project-local. The low-level 2D physics namespace is now `Unity.U2D.Physics`. See the [6.5 upgrade guide](https://docs.unity.com/en-us/engine/6000.5/manual/upgrade-guides/upgrade-guide-unity65).
- Unity 6.6: dictionary fields opt in to native serialization with `[SerializeField]`, including public fields; `[SerializeReference]` is not valid for them. When migrating wrappers, copy and verify asset data before removing the old fields; deleting them first loses data. See [dictionary migration](https://docs.unity.com/en-us/engine/6000.6/manual/scripting/compilation-and-code-reload/script-serialization/dictionaries-migrate).
- Unity 6.6: new projects default to scene-only Play Mode reload. Burst is built in, so a separate Burst package is no longer required. Resolve Unity API Compatibility analyzer warnings against the target's supported APIs. See [6.6 changes](https://docs.unity.com/en-us/engine/6000.6/manual/whats-new/unity66).
- Unity 6.6: diagnostics depend on Managed Code Variant, independently of Development Build. Replace deprecated `DEVELOPMENT_BUILD` usage according to intent with `UNITY_ENABLE_CHECKS` or `UNITY_INCLUDE_INSTRUMENTATION`; check player variants because both are defined in the Editor. Cinemachine becomes a core package and can automatically upgrade v2 projects to v3, changing APIs and data. Dynamic batching is obsolete. Replace removed UXML Factory/Traits controls with `UxmlElement`/`UxmlAttribute`. Replace `UNITY_64` with bitness-independent code or runtime `IntPtr.Size`; use `Debug.isDebugBuild` when the actual development-player status is required. See the [6.6 upgrade guide](https://docs.unity.com/en-us/engine/6000.6/manual/upgrade-guides/upgrade-guide-unity66).

## Engine and package boundaries

- Resolve engine and package availability separately. Keep the project's render pipeline, input system, UI system and GameObject/Entities architecture unless the task calls for migration; package presence alone does not justify adopting it.
- Keep UnityEditor dependencies in Editor-only assemblies or compilation guards. Check assembly references and platform constraints when moving scripts; generated project files are not the source of build configuration.

## Components and play sessions

- Initialize component references in Awake and coordinate dependencies explicitly; callback order between different objects is not a general initialization guarantee. Pair subscriptions and other enabled-only work with OnEnable/OnDisable, and release instance-owned resources at the appropriate teardown boundary.
- UnityEngine.Object has native-object lifetime semantics: use Unity-aware equality or truth checks for destroyed objects. Null-conditional and null-coalescing operators do not perform Unity's destroyed-object check.
- When domain reload is disabled, explicitly reset session-owned static state and static event subscriptions. Verify entering Play Mode twice under the project's actual reload settings.
- Match simulation work to the configured physics update mode, normally FixedUpdate; use the corresponding time step. Keep frame input sampling separate from physics consumption where the input system requires it.

## Serialized assets and Editor changes

- Follow the target Editor's field serialization rules rather than .NET serializer assumptions. Use SerializeReference only when managed reference identity or polymorphism is required; keep ScriptableObject asset configuration separate from mutable session state.
- Preserve serialized data deliberately when renaming fields or changing types: inspect affected scenes, prefabs and assets, migrate when required, and disclose destructive changes. Preserve .meta files and GUIDs when moving assets.
- Editor tools should use SerializedObject/SerializedProperty for serialized edits, or the appropriate Undo and prefab-override recording APIs for direct mutations. Ensure changes persist and remain undoable. Keep OnValidate lightweight; it may run frequently and off the main thread, so schedule work needing main-thread Unity APIs appropriately.

## Async work and resource ownership

- Keep Unity API access on the main thread unless that API explicitly supports worker threads. Tie coroutines and async operations to the intended object, enabled state, scene or application lifetime; destruction and disabling are distinct boundaries.
- Use Unity Awaitable only when supported by the target Editor. Awaitable instances are pooled: await an instance once, and explicitly return to the main thread before accessing Unity objects after background work. Use lifetime cancellation APIs only after checking their availability.
- Give instantiated objects, native containers, runtime-created materials/textures and loaded asset handles explicit owners. Match release to the acquisition API; Addressables handles require Addressables lifetime management when that package is used. Distinguish shared assets from per-instance copies before mutation or destruction.

## Performance and player validation

- Profile a representative player on the target device before changing architecture. Inspect CPU/GPU time, allocations and asset memory; cache stable component references and remove repeated scene searches or avoidable allocations from measured hot paths. Add pooling or Jobs/Burst only for demonstrated needs and supported engine/package versions.
- For Jobs, honor NativeContainer ownership, dependencies and disposal; use Burst-supported code in compiled jobs rather than assuming all managed C# is supported.
- IL2CPP/AOT and managed stripping can break reflection-only or dynamically constructed code paths. Preserve only required members with supported attributes/link.xml and exercise those paths in the target player; Editor tests alone do not validate them.
- Use Edit Mode tests for Editor/asset logic and Play Mode tests for lifecycle, scene transitions and frame-dependent behavior. For affected builds, check platform defines, backend and actual build logs; distinguish an unavailable player/device check from a passing one.

## Sources

Use the matching Editor/package version of these official references; the Unity 6.0 links below cover baseline mechanics, while the version-sensitive section links newer behavior. They do not set a minimum project version.

- [Unity scripting environment and version support](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting-environment.html)
- [Event execution order](https://docs.unity3d.com/6000.0/Documentation/Manual/ExecutionOrder.html)
- [UnityEngine.Object equality](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-operator_eq.html)
- [Domain reload](https://docs.unity3d.com/6000.0/Documentation/Manual/domain-reloading.html)
- [Script serialization](https://docs.unity3d.com/6000.0/Documentation/Manual/script-serialization.html)
- [Editor serialization and Undo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.html)
- [OnValidate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnValidate.html)
- [Unity Awaitable](https://docs.unity3d.com/6000.0/Documentation/Manual/async-await-support.html)
- [Memory and garbage collection](https://docs.unity3d.com/6000.0/Documentation/Manual/performance-garbage-collection-best-practices.html)
- [Managed stripping](https://docs.unity3d.com/6000.0/Documentation/Manual/managed-code-stripping.html)
- [Unity package documentation](https://docs.unity3d.com/Manual/PackagesList.html)

- [Unity 6.0 upgrade guide](https://docs.unity.com/en-us/engine/6000.6/manual/upgrade-guides/upgrade-guide-unity6)
- [Unity 6.3 LTS upgrade guide](https://docs.unity.com/en-us/engine/6000.6/manual/upgrade-guides/upgrade-guide-unity63)
- [Editor patch release notes](https://unity.com/releases/editor/archive)
