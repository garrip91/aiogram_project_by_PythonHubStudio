@echo off

call %~dp0aiogram_project_by_PythonHubStudio\venv\Scripts\activate

cd %~dp0aiogram_project_by_PythonHubStudio

set TOKEN=809303024:AAGoklo1kZBFI0yfv65P7C9BDMofv8guYCU

python bot_telegram.py

pause