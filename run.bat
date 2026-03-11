@echo off
echo 启动竞彩足球分析系统...
cd /d "%~dp0"
python main.py %*
pause