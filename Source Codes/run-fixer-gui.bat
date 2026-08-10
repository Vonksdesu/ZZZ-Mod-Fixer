@echo off
title ZZZ Mod Fixer GUI
cd /d "%~dp0"
call venv\Scripts\activate.bat
python zzz-mod-fixer-gui.py
