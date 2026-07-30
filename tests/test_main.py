import pathlib
import subprocess
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "src"))

import main


class StartupMessageTests(unittest.TestCase):
    def test_marker_is_non_sensitive_and_experimental(self):
        self.assertEqual(main.startup_message(), "DJConnect Pico experimental skeleton")


class FakePin:
    OUT = "output"
    created = []

    def __init__(self, name, mode):
        self.name = name
        self.mode = mode
        self.values = []
        self.__class__.created.append(self)

    def value(self, value):
        self.values.append(value)


class HardwareSmokeTests(unittest.TestCase):
    def setUp(self):
        FakePin.created = []

    def test_led_pulses_once_for_the_default_duration(self):
        delays = []

        result = main.run_hardware_smoke(FakePin, delays.append)

        self.assertEqual(result, "Pico 2 W LED smoke test passed")
        self.assertEqual(len(FakePin.created), 1)
        self.assertEqual(FakePin.created[0].name, "LED")
        self.assertEqual(FakePin.created[0].mode, FakePin.OUT)
        self.assertEqual(FakePin.created[0].values, [1, 0])
        self.assertEqual(delays, [250])


class HostEntrypointTests(unittest.TestCase):
    def test_host_execution_skips_hardware_without_failing(self):
        completed = subprocess.run(
            [sys.executable, str(pathlib.Path(main.__file__))],
            check=True,
            capture_output=True,
            text=True,
        )
        self.assertIn("DJConnect Pico experimental skeleton", completed.stdout)
        self.assertIn("Hardware smoke skipped", completed.stdout)
