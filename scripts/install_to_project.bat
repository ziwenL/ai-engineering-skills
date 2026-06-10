@echo off
if "%~1"=="" (
  echo Usage: scripts\install_to_project.bat "C:\Users\<your-username>\Projects\your-business-project"
  exit /b 1
)
python "%~dp0init_submodule_project.py" "%~1"
