@echo off
title PowerShell Auto-Tab Manager Installer

echo =======================================================
echo     Installer untuk PowerShell Auto-Tab Manager
echo         by Kyugito666
echo =======================================================
echo.
echo Script ini akan menginstal semua package Python yang dibutuhkan.
echo Pastikan Anda memiliki Python dan pip terinstal.
echo.

pause
echo.

echo [+] Memulai instalasi dari requirements.txt...
pip install -r requirements.txt

echo.
echo [+] Instalasi Selesai!
echo Anda sekarang bisa menjalankan program dengan 'python main.py'.
echo.

pause