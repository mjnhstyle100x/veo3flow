@echo off
chcp 65001 >nul
title Dong bo code len GitHub va Vercel
echo ===================================================
echo   DANG DONG BO CODE VA ANH LEN GITHUB...
echo ===================================================
echo.

cd /d "%~dp0"
if exist "..\preview" cd ..

git add -A
git commit -m "Update resort villa and real estate prompts"
git push origin main

echo.
echo ===================================================
echo   HOAN TAT! DA DONG BO LEN GITHUB THANH CONG!
echo   Vercel se tu dong cap nhat trong 10-20 giay.
echo ===================================================
echo.
pause
