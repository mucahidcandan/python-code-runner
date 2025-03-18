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

echo Gerekli paketler yukleniyor...
pip install flask pyinstaller

echo.
echo Eski derleme dosyalari temizleniyor...
rmdir /s /q build 2>nul
rmdir /s /q dist 2>nul
del /f /q *.spec 2>nul

echo.
echo Uygulama derleniyor...
pyinstaller --add-data "templates;templates" --name "CandanPythonDuzenleyici" app.py

echo.
echo Release dosyalari hazirlaniyor...
mkdir release 2>nul
xcopy /E /I /Y "dist\CandanPythonDuzenleyici" "release\CandanPythonDuzenleyici"
copy /Y "README.md" "release\"
copy /Y "LICENSE" "release\"

echo.
echo Release dosyalari release/ klasorunde hazir!
echo.
echo GitHub Release Olusturma Adimlari:
echo 1. GitHub'da yeni bir release olusturun
echo 2. Release/ klasorundeki tum dosyalari zip yapin
echo 3. Zip dosyasini release'e ekleyin
echo 4. Release'i yayinlayin
echo.
echo Not: Uygulamayi baslatmak icin CandanPythonDuzenleyici/CandanPythonDuzenleyici.exe dosyasini calistirin.
pause 