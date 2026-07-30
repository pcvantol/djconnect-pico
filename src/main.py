"""Pico 2 W hardware smoke test; no product behavior is implemented."""


def startup_message() -> str:
    """Return a non-sensitive marker for a local device smoke check."""
    return "DJConnect Pico experimental skeleton"


def run_hardware_smoke(pin_factory, sleep_ms, duration_ms=250) -> str:
    """Pulse the Pico W LED once and return a non-sensitive serial marker.

    Dependencies are injected so host-side tests do not need MicroPython's
    ``machine`` module or a physical board.
    """
    led = pin_factory("LED", pin_factory.OUT)
    led.value(1)
    sleep_ms(duration_ms)
    led.value(0)
    return "Pico 2 W LED smoke test passed"


def run_on_device() -> str:
    """Run the hardware smoke test using the MicroPython Pico 2 W APIs."""
    from machine import Pin
    from time import sleep_ms

    return run_hardware_smoke(Pin, sleep_ms)


if __name__ == "__main__":
    print(startup_message())
    try:
        print(run_on_device())
    except ImportError:
        print("Hardware smoke skipped: run this script on a flashed Pico 2 W.")
