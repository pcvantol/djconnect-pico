import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "src"))

import capabilities


class CapabilityBoundaryTests(unittest.TestCase):
    def test_only_experimental_status_is_enabled(self):
        self.assertEqual(
            capabilities.capability_snapshot(),
            {
                "display": False,
                "input": False,
                "network": False,
                "home_assistant": False,
                "experimental": True,
            },
        )

    def test_unknown_capabilities_are_not_supported(self):
        self.assertFalse(capabilities.supports("pairing"))

    def test_snapshot_cannot_change_the_declared_boundary(self):
        snapshot = capabilities.capability_snapshot()
        snapshot["network"] = True

        self.assertFalse(capabilities.supports("network"))
