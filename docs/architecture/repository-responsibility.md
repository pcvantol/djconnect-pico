# Repository Responsibility

DJConnect Pico evaluates constrained Raspberry Pi Pico 2 W client or appliance
capabilities. It may consume approved DJConnect contracts through Home
Assistant; it does not establish those contracts.

Home Assistant is the canonical runtime and authority. This repository has no
authority over Session Runtime, backend orchestration, Music DNA, DJ
intelligence, profile persistence, or user data. It is neither a supported
product component nor a production firmware distribution channel.

## Toolchain decision

MicroPython is the initial evaluation stack because it permits a small,
inspectable device loop and host-side syntax validation without committing to a
production firmware architecture. The Pico SDK C/C++ option was assessed as a
strong future candidate for production performance and integration, but is
deferred until hardware capabilities and product scope are approved.

## Deferred decisions

- Device role and supported capabilities.
- Pairing, provisioning, and Home Assistant endpoint changes.
- OTA, release artifacts, and supported hardware configuration.
- Pico SDK C/C++ adoption and any migration plan.

## Current capability boundary

The host-testable `src/capabilities.py` module is a deliberately restrictive
declaration of current scope: display, input, network, and Home Assistant are
all `false`; only `experimental` is `true`. It is not a device-discovery or
runtime contract. Adding a capability requires a separate approved architecture
decision and reviewable increment.
