# -*- mode: python ; coding: utf-8 -*-

# Import the block_cipher module from PyInstaller
from PyInstaller.utils.hooks import collect_data_files

# Define the block_cipher variable
block_cipher = None

a = Analysis(['app.py'],
             pathex=['.'],
             binaries=[],
             datas=[
    ('.venv\\Lib\\site-packages\\dash_ag_grid', 'dash_ag_grid'),
    # Add other packages if needed
    ],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='app',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    onefile=False # Set this to False to create a directory mode executable
)
