# -*- mode: python ; coding: utf-8 -*-
"""
PyInstaller Spec File for ZZZ Mod Fixer 
Character Data Separation - Single Executable Build

This spec file packages the modular character data system
into a single executable with all character modules embedded.
"""

block_cipher = None

a = Analysis(
    ['zzz-mod-fixer.py'],
    pathex=['Assets', '.'],
    binaries=[],
    datas=[
        ('Assets/PlayerCharacterPYData/*.py', 'Assets/PlayerCharacterPYData'),
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[
        'tkinter',
        'matplotlib',
        'numpy',
        'pandas',
        'PIL',
        'Pillow',
        'PyQt5',
        'PyQt6',
        'PySide2',
        'PySide6',
        'cryptography',
        'test',
        'unittest',
        'pytest',
        'venv',
        'ensurepip',
        'setuptools',
        'distutils',
        'pip',
        'curses',
        'win32api',
        'win32con',
        'win32gui',
        'idlelib',
    ],
    optimize=2,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='zzz-mod-fixer-v3.0',
    debug=False,
    bootloader_ignore_signals=False,
    strip=True,
    upx=True,
    upx_dir='UPX',
    upx_exclude=[],
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=None,
)
