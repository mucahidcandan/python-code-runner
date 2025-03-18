@echo off
echo Python Code Runner Derleme Scripti
echo ================================

REM Python kontrolü
python --version >nul 2>&1
if errorlevel 1 (
    echo HATA: Python yuklu degil!
    echo Python'u https://www.python.org/downloads/ adresinden indirip yukleyin.
    pause
    exit /b
)

REM Node.js kontrolü
node --version >nul 2>&1
if errorlevel 1 (
    echo HATA: Node.js yuklu degil!
    echo Node.js'i https://nodejs.org/ adresinden indirip yukleyin.
    pause
    exit /b
)

echo Gerekli paketler yukleniyor...
pip install -r requirements.txt
npm install

echo.
echo Uygulama derleniyor...
npm run build

echo.
echo Derleme tamamlandi!
echo Uygulama dist/ klasorunde bulunabilir.
pause 