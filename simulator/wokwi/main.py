"""Wokwi-only adapter for the Pico hardware smoke test.

Wokwi currently models the RP2040 Pico, not the Pico 2 W RP2350. GPIO 15 is
used for an external virtual LED so the pulse is visible in the diagram.
"""

from machine import Pin
from time import sleep_ms


led = Pin(15, Pin.OUT)
print("DJConnect Pico experimental skeleton")
led.value(1)
sleep_ms(250)
led.value(0)
print("Pico simulator LED smoke test passed")
