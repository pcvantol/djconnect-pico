import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "src"))

import main


class StartupMessageTests(unittest.TestCase):
    def test_marker_is_non_sensitive_and_experimental(self):
        self.assertEqual(main.startup_message(), "DJConnect Pico experimental skeleton")
