@echo off
echo Starting Autonomous Coding System...
echo =====================================

:: Set environment variables
set OLLAMA_MODELS=G:\AI_Coding\models
set PYTHONPATH=G:\AI_Coding

:: Activate virtual environment
call G:\AI_Coding\venv\Scripts\activate.bat

:: Start the system
python G:\AI_Coding\autonomous_system.py

pause
