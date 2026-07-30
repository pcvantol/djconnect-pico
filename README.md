# DJConnect Pico

## What this repository is

Experimental Raspberry Pi Pico 2 W firmware and device prototypes for
[DJConnect](https://djconnect.dev). It is an evaluation repository, not a
supported DJConnect product component.

## What it owns

- Pico 2 W-specific prototype firmware, host-side tests, and development docs.
- Constrained-client experiments that consume approved DJConnect contracts.

## What it explicitly does not own

Home Assistant remains the canonical DJConnect runtime and authority. This
repository does not own Session Runtime, Music Backend orchestration, Music
DNA, DJ intelligence, user-profile persistence, pairing contracts, or product
support decisions. Those boundaries are governed by the
[DJConnect platform architecture](https://github.com/pcvantol/djconnect/tree/main/docs/technical).

## Current support status

**Experimental only.** No production support, OTA path, provisioning design, or
release distribution is implied. Product capability and support require a
separate architecture approval.

## Start here

Read [DEVELOPMENT_ENVIRONMENT.md](DEVELOPMENT_ENVIRONMENT.md), then review the
[repository responsibility](docs/architecture/repository-responsibility.md).
The wider project lives in [pcvantol/djconnect](https://github.com/pcvantol/djconnect).

## Initial toolchain

This repository starts with MicroPython for Raspberry Pi Pico 2 W. It gives the
smallest practical loop for constrained-device experiments while preserving the
option to assess the Pico SDK C/C++ route before a product architecture is
approved. The minimal skeleton deliberately contains no device behavior.

## License

MIT. See [LICENSE](LICENSE).
