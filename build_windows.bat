@echo off
setlocal
cd /d "%~dp0"

set "PY=python"
where py >nul 2>nul && set "PY=py"

%PY% -m pip install --upgrade pip
%PY% -m pip install -r requirements.txt -r requirements-build.txt
%PY% -m PyInstaller --noconfirm contapy.spec
if errorlevel 1 exit /b 1

echo.
echo Built dist\LetoBank\LetoBank.exe
