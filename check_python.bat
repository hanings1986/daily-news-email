@echo off
echo 检查Python环境...
python --version
if %errorlevel% neq 0 (
    echo Python未找到或未配置环境变量
    echo 请检查Python安装
)
pause