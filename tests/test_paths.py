"""Tests for platform-aware config and data locations."""

from __future__ import annotations

import unittest
from pathlib import Path

from contapy.paths import config_dir, data_dir


class PathTests(unittest.TestCase):
    def test_linux_uses_xdg_directories(self) -> None:
        env = {
            "XDG_CONFIG_HOME": "/tmp/letobank-config",
            "XDG_DATA_HOME": "/tmp/letobank-data",
        }
        self.assertEqual(
            config_dir(env, windows=False),
            Path("/tmp/letobank-config/contapy"),
        )
        self.assertEqual(
            data_dir(env, windows=False),
            Path("/tmp/letobank-data/contapy"),
        )

    def test_windows_uses_appdata_directories(self) -> None:
        env = {
            "APPDATA": "C:/Users/me/AppData/Roaming",
            "LOCALAPPDATA": "C:/Users/me/AppData/Local",
        }
        self.assertEqual(
            config_dir(env, windows=True),
            Path("C:/Users/me/AppData/Roaming/contapy"),
        )
        self.assertEqual(
            data_dir(env, windows=True),
            Path("C:/Users/me/AppData/Local/contapy"),
        )

    def test_windows_falls_back_to_home_appdata(self) -> None:
        config = config_dir({}, windows=True)
        data = data_dir({}, windows=True)
        self.assertIn("contapy", config.parts)
        self.assertIn("contapy", data.parts)
        self.assertIn("AppData", config.parts)
        self.assertIn("AppData", data.parts)


if __name__ == "__main__":
    unittest.main()
