# Wokwi LED Smoke Simulation

This is a browser-based **logic and GPIO simulation** for the hardware smoke
test. It intentionally uses Wokwi's Raspberry Pi Pico (RP2040) model and an
external virtual LED on GPIO 15. Wokwi does not currently offer a Pico 2 W
(RP2350) model, so this must not be used as evidence for Pico 2 W-specific
hardware, Wi-Fi, Bluetooth, flashing, or power behavior.

## Run it

1. Open the [Raspberry Pi Pico MicroPython template](https://wokwi.com/projects/new/micropython-pi-pico).
2. Replace its `main.py` and `diagram.json` with the files in this directory.
3. Start the simulation.
4. Confirm that the green LED pulses once and that the serial monitor prints
   `Pico simulator LED smoke test passed`.

Do not add Wokwi CI to this repository without separate approval: Wokwi CI
requires a repository secret, while ordinary pull-request validation is kept
secret-free.
