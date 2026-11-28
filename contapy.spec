# -*- mode: python ; coding: utf-8 -*-

# Build a one-folder desktop bundle:
#   Windows:  pyinstaller --noconfirm contapy.spec
#   Linux:    pyinstaller --noconfirm contapy.spec
#
# The application data (JetBrains Mono, Font Awesome and SVG assets) is copied
# next to the executable so frozen builds look the same as a source checkout.

a = Analysis(
    ["main.py"],
    pathex=[],
    binaries=[],
    datas=[("contapy/assets", "contapy/assets")],
    hiddenimports=["pypdf", "segno"],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name="LetoBank",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon="contapy/assets/letobank.ico",
)

coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=False,
    upx_exclude=[],
    name="LetoBank",
)
