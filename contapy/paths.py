"""Platform-aware locations for the config file and the database."""

from __future__ import annotations

import os
from pathlib import Path


def is_windows() -> bool:
    return os.name == "nt"


def config_dir(
    environ: dict[str, str] | None = None,
    *,
    windows: bool | None = None,
) -> Path:
    """Per-user configuration directory.

    Linux follows XDG (``~/.config/contapy``); Windows uses
    ``%APPDATA%\\contapy``.
    """
    env = os.environ if environ is None else environ
    use_windows = is_windows() if windows is None else windows
    if use_windows:
        base = env.get("APPDATA") or Path.home() / "AppData" / "Roaming"
        return Path(base) / "contapy"
    base = env.get("XDG_CONFIG_HOME") or Path.home() / ".config"
    return Path(base) / "contapy"


def data_dir(
    environ: dict[str, str] | None = None,
    *,
    windows: bool | None = None,
) -> Path:
    """Per-user data directory for the database and its backups.

    Linux follows XDG (``~/.local/share/contapy``); Windows uses
    ``%LOCALAPPDATA%\\contapy``.
    """
    env = os.environ if environ is None else environ
    use_windows = is_windows() if windows is None else windows
    if use_windows:
        base = (
            env.get("LOCALAPPDATA")
            or env.get("APPDATA")
            or Path.home() / "AppData" / "Local"
        )
        return Path(base) / "contapy"
    base = env.get("XDG_DATA_HOME") or Path.home() / ".local" / "share"
    return Path(base) / "contapy"
