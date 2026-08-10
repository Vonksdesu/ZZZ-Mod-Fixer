@echo off
title ZZZ Mod Fixer GUI
cd /d "%~dp0"

if not exist "venv\" (
    echo [ZZZ Mod Fixer] Virtual environment not found. Creating venv...
    python -m venv venv
    if errorlevel 1 (
        echo [ZZZ Mod Fixer] ERROR: Failed to create venv. Make sure Python is installed.
        pause
        exit /b 1
    )
    echo [ZZZ Mod Fixer] Virtual environment created successfully.

    echo [ZZZ Mod Fixer] Installing required dependencies...
    venv\Scripts\python.exe -m pip install --upgrade pip --quiet
    venv\Scripts\python.exe -m pip install tkinterweb markdown --quiet
    if errorlevel 1 (
        echo [ZZZ Mod Fixer] ERROR: Failed to install dependencies.
        pause
        exit /b 1
    )
    echo [ZZZ Mod Fixer] Dependencies installed successfully.
)

call venv\Scripts\activate.bat
python zzz-mod-fixer-gui.py
