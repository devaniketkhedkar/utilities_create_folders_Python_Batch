@echo off
set /p month="Enter the month (MM): "
set /p year="Enter the year (YYYY): "
python CreateFolders_BASH.py %month% %year%