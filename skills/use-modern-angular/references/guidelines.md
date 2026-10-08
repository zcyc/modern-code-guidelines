# Angular

## Gates

- Standalone is supported from 14 (stable 15), default from 19; older targets may need explicit standalone. Local changes retain existing NgModule boundaries.
- Signals start in 16; built-in control flow/@defer require 17. Check input/output API stability separately.
- resource/httpResource/Signal Forms have separate gates; httpResource and Signal Forms are stable in 22+. Earlier targets require documented API/stability checks.

## State and templates

- signal owns mutable state; computed derives values; effect synchronizes external systems rather than copying state between signals.
- Preserve service/injection boundaries. OnPush/zoneless updates need Angular notifications: template-read signals, input updates, AsyncPipe or markForCheck.
- Defer views for measured bundle/rendering benefits with loading/placeholder/error states. Test actual SSR/change-detection mode.
- resource/httpResource model reactive reads; writes stay explicit through HttpClient/services. Signal Forms fit new signal-first forms without forcing migration of existing reactive forms.

## Sources

- [Angular overview](https://angular.dev/overview)
- [Component anatomy](https://angular.dev/guide/components)
- [Signals](https://angular.dev/guide/signals)
- [Zoneless](https://angular.dev/guide/zoneless)
- [Standalone migration](https://angular.dev/reference/migrations/standalone)
- [`resource`](https://angular.dev/guide/signals/resource)
- [`httpResource`](https://angular.dev/api/common/http/httpResource)
- [Signal Forms](https://angular.dev/guide/forms/signals/overview)
