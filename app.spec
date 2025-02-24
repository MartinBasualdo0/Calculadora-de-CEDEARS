from PyInstaller.utils.hooks import collect_data_files

datas = collect_data_files('dash_ag_grid')  # Asegura incluir todos los archivos necesarios

a = Analysis(
    ['app.py'],
    pathex=['.'],
    binaries=[],
    datas=datas,  # Incluye los archivos extra de dash_ag_grid
    hiddenimports=['dash_ag_grid'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='app',
    debug=False,
    upx=True,
    console=True
)
