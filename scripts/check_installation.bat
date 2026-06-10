@echo off
if "%~1"=="" (
  echo Usage: scripts\check_installation.bat "C:\Users\<your-username>\Projects\your-business-project"
  exit /b 1
)
python "%~dp0check_installation.py" "%~1"
