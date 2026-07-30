# DJConnect Security Policy

## Reporting a vulnerability

Report suspected vulnerabilities privately to `security@djconnect.dev`. Do not
open a public issue for vulnerabilities, leaked credentials, private URLs,
exploit details, or sensitive logs.

Include the affected commit or component, impact, safe reproduction steps, and
redacted evidence. Do not include real Wi-Fi credentials, Home Assistant or
DJConnect tokens, private network URLs, personal data, or raw diagnostics.

## Pico-specific secret handling

Wi-Fi credentials, Home Assistant tokens, device secrets, and any backend
credentials must never be committed, logged, placed in test fixtures, copied
into AI prompts, or included in screenshots. Example configuration must use
placeholders. Diagnostics and tests must redact sensitive values.

## Scope and support

This experimental repository currently supports only the current `main` line
for security fixes. Home Assistant, third-party firmware, and other DJConnect
components have their own security boundaries, though cross-repository reports
are welcome at the same private address.
