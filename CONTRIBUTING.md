# Contributing to DJConnect Pico

This repository is an experimental DJConnect device surface. Keep changes
small, reviewable, tested, license-compatible, and free of secrets.

## Workflow

All changes go through pull requests to `main`; use draft pull requests for
unfinished work. Do not merge without the evidence required by Delivery Guard.
High-risk changes—including workflows, governance, secrets, security controls,
or cross-repository contracts—require explicit Owner Authorization.

Read [DEVELOPMENT_ENVIRONMENT.md](DEVELOPMENT_ENVIRONMENT.md) before changing
firmware. A change to shared runtime, pairing, profile, or playback contracts
belongs first in the [canonical DJConnect repository](https://github.com/pcvantol/djconnect).

## Before opening a PR

1. Run `python3 -m compileall -q src tests` and `python3 -m unittest discover -s tests -v`.
2. Confirm `git status` only contains intended work.
3. Record validation, architecture impact, risk class, and any required Owner
   Authorization in the PR template.
4. Never commit or log Wi-Fi credentials, Home Assistant tokens, or device secrets.

Contributions are licensed under the [MIT License](LICENSE).
