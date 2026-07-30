"""Declared capability boundary for the experimental Pico repository."""

# This is intentionally a small, static allow-list. New capabilities require an
# approved architecture decision and a dedicated, reviewable increment.
_CAPABILITIES = (
    ("display", False),
    ("input", False),
    ("network", False),
    ("home_assistant", False),
    ("experimental", True),
)


def capability_snapshot():
    """Return the current boundary as a fresh mapping for callers and tests."""
    return dict(_CAPABILITIES)


def supports(capability):
    """Return whether an explicitly declared capability is currently supported."""
    return capability_snapshot().get(capability, False)
