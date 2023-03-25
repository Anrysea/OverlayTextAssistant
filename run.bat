@echo off
cd /d %~dp0
powershell -Command "Start-Process -FilePath 'C:\Python\Python311\python.exe' -ArgumentList 'C:\OverlayTextAssistant\main.py' -Verb RunAs"