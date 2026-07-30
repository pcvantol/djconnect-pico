# Development Environment

## Selected initial stack

The initial, prototype-only stack is MicroPython for **Raspberry Pi Pico 2 W**.
Use a current stable Pico 2 W MicroPython firmware from the official
[MicroPython downloads](https://micropython.org/download/RPI_PICO2_W/). Record
the exact firmware build used for a hardware experiment in its PR; this
repository intentionally does not ship a firmware image.

MicroPython was selected for fast hardware evaluation with the smallest
repository footprint. The Raspberry Pi Pico SDK C/C++ path remains an
architecture decision for a later, approved product increment; do not build a
second implementation during this phase.

## macOS setup

1. Install Python 3.11 or later and create an isolated environment if desired.
2. Install the upload tool: `python3 -m pip install mpremote`.
3. Download the Pico 2 W `.uf2` firmware from the official page above.
4. Hold **BOOTSEL** while connecting the board, copy the `.uf2` to the mounted
   `RPI-RP2` volume, then reconnect normally.

## Local validation

```sh
python3 -m compileall -q src tests
python3 -m unittest discover -s tests -v
```

## Device sync

With a USB-connected, flashed Pico 2 W:

```sh
mpremote connect auto fs cp src/main.py :main.py
mpremote connect auto reset
```

This is only a smoke skeleton. It must not contain credentials, pairing tokens,
or production behavior. Use placeholders in any future examples and redact
sensitive values from diagnostics.

## First hardware smoke test

After syncing `src/main.py`, the Pico 2 W prints two non-sensitive serial
messages and pulses its onboard LED once for 250 ms. This validates only the
MicroPython flash/sync path, serial output, and the board LED; it does not test
Wi-Fi, Home Assistant, provisioning, or a DJConnect protocol.

Capture the board model, MicroPython firmware build, command used, and redacted
serial output in the pull request before treating the experiment as validated.

## Simulator without a board

[`simulator/wokwi/`](simulator/wokwi/) provides a Wokwi browser simulation for
the serial and LED logic. It uses Wokwi's RP2040 Pico model and is deliberately
not represented as Pico 2 W hardware validation. It does not validate Wi-Fi,
Bluetooth, flashing, onboard-LED wiring, or timing on the RP2350-based board.

## Versioning and releases

No release, OTA, or firmware publishing process is authorized yet. When an
approved release process exists, use semantic versions and `vX.Y.Z` tags in
line with the active DJConnect repositories.
