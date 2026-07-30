# Governance and Assurance

This repository follows the active DJConnect source-repository model:

- Pull requests target protected `main`; draft PRs are used for unfinished work.
- Trusted Delivery classifies risk. High-risk work requires explicit Owner
  Authorization evidence before merge.
- Workflows use least privilege and full commit-SHA action pins.
- Post-merge evidence and release workflows are deferred because this repository
  has no supported deployment or release process.
- TDE is intentionally not integrated yet. The bootstrap skeleton has no
  dependency manifest or meaningful coverage/dependency-health evidence. When
  product source exists, use public CLI distribution
  `technical-debt-engine-runtime==1.1.1`, exact-pinned, observe-only and
  non-blocking. Never report unavailable metrics as zero.

## Canonical reference comparison

| Concern | Reference | Decision |
| --- | --- | --- |
| Ownership, security, contributions | `djconnect-esp32` | Adapted for Pico/MicroPython and experimental status. |
| Delivery Guard and Owner Authorization | `djconnect-esp32`, `djconnect` | Adopted as pinned reusable workflows. |
| Software Assurance | `djconnect` | Adopted through the canonical balanced profile. |
| Dependabot and action pins | active device/client repositories | Adopted. |
| TDE Observe | `djconnect-esp32`, TDE 1.1.1 | Deferred truthfully; no qualified evidence yet. |
| Firmware releases/deployment | `djconnect-esp32` | Intentionally not applicable. |
