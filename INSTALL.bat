@echo off
echo ====================================
echo Autonomous AI Coding Setup
echo ====================================
echo.

:: Check for Python
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python not found. Please install Python 3.10+
    echo Download from: https://www.python.org/downloads/
    pause
    exit /b 1
)

:: Check for NVIDIA GPU
nvidia-smi >nul 2>&1
if errorlevel 1 (
    echo WARNING: NVIDIA GPU not detected or drivers not installed
    echo Continue anyway? (Y/N)
    choice /c YN
    if errorlevel 2 exit /b 1
)

:: Ask for installation drive
echo.
set /p DRIVE="Enter drive letter for installation (default G): "
if "%DRIVE%"=="" set DRIVE=G

:: Create directory and setup
echo.
echo Installing to %DRIVE%:\AI_Coding...
mkdir %DRIVE%:\AI_Coding 2>nul
xcopy /E /I /Y * %DRIVE%:\AI_Coding\

:: Run setup
cd /d %DRIVE%:\AI_Coding
python setup_autonomous_coding.py --drive %DRIVE%

echo.
echo ====================================
echo Installation Complete!
echo Start with: %DRIVE%:\AI_Coding\START_AI_CODING.bat
echo ====================================
pause