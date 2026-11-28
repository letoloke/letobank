"""Locate bundled assets in source checkouts and frozen builds."""

from __future__ import annotations

import sys
from pathlib import Path


def asset_dir() -> Path:
    """The ``contapy/assets`` directory, including inside PyInstaller builds."""
    frozen_root = getattr(sys, "_MEIPASS", None)
    if getattr(sys, "frozen", False) and frozen_root:
        return Path(frozen_root) / "contapy" / "assets"
    return Path(__file__).resolve().parent / "assets"
