"""Minimal Pico 2 W smoke skeleton; no product behavior is implemented."""


def startup_message() -> str:
    """Return a non-sensitive marker for a local device smoke check."""
    return "DJConnect Pico experimental skeleton"


if __name__ == "__main__":
    print(startup_message())
