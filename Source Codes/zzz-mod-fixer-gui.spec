# -*- mode: python ; coding: utf-8 -*-
"""
PyInstaller Spec File for ZZZ Mod Fixer GUI
"""

block_cipher = None

a = Analysis(
    ['zzz-mod-fixer-gui.py'],
    pathex=['Assets', '.'],
    binaries=[],
    datas=[
        ('Assets/PlayerCharacterPYData/*.py', 'Assets/PlayerCharacterPYData'),
        ('Assets/Icons/*.png', 'Assets/Icons'),
        ('Assets/Guide/*.md', 'Assets/Guide'),
        ('Config/config.json', 'Config'),
        ('zzz-mod-fixer.py', '.'),
        ('Jane.remapper.py', '.'),
        ('Dialyn.remapper.py', '.'),
    ],
    hiddenimports=['tkinterweb', 'markdown', 'dataclasses'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[
        'matplotlib', 'numpy', 'pandas',
        'PyQt5', 'PyQt6', 'PySide2', 'PySide6',
        'cryptography', 'test', 'unittest', 'pytest',
        'venv', 'ensurepip', 'setuptools', 'distutils', 'pip',
        'curses', 'win32api', 'win32con', 'win32gui', 'idlelib',
        'asyncio', 'ftplib', 'imaplib', 'poplib',
        'smtplib', 'nntplib', 'telnetlib', 'xmlrpc',
        'pickle', 'pickletools', 'shelve',
        'bz2', 'lzma', '_bz2', '_lzma', 'tarfile',
        'audioop', 'sunau', 'wave', 'imghdr', 'sndhdr', 'aifc',
        'pdb', 'profile', 'pstats', 'cProfile', 'timeit',
        'doctest', 'pydoc', 'tabnanny', 'trace', 'tracemalloc',
        'turtle', 'turtledemo', 'tkinter.test', 'tkinter.dnd',
        'msilib', 'nis', 'ossaudiodev', 'pty', 'pwd', 'grp',
        'spwd', 'resource', 'syslog', 'fcntl', 'termios', 'tty',
        'readline', 'rlcompleter', 'dbm', 'gdbm', '_dbm',
        'uuid', 'netrc', 'mailbox', 'mailcap',
        'pipes', 'xdrlib', 'uu',
        'antigravity', 'this', 'lib2to3', 'pyclbr', 'pydoc_data',
        'plistlib', 'graphlib',
        'compileall', 'py_compile', 'modulefinder', 'runpy',
        'cmath', 'secrets',
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
    name='zzz-mod-fixer-v3.1',
    debug=False,
    bootloader_ignore_signals=False,
    strip=True,
    upx=True,
    upx_dir='UPX',
    upx_exclude=[],
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='Assets/Icons/zzzlogo.ico',
)
