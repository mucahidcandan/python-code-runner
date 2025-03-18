@echo off
echo Python Kod Calistirici baslatiliyor...
echo.

REM Python'un yuklu olup olmadigini kontrol et
python --version >nul 2>&1
if errorlevel 1 (
    echo HATA: Python yuklu degil!
    echo Python'u https://www.python.org/downloads/ adresinden indirip yukleyin.
    pause
    exit /b
)

echo Gerekli paketler yukleniyor...
pip install -r requirements.txt

echo.
echo Uygulama baslatiliyor...
echo Tarayici otomatik olarak acilacak...
echo.

REM Tarayiciyi ac (5 saniye bekle ki Flask sunucusu baslasin)
start "" cmd /c "timeout /t 5 /nobreak && start http://localhost:5000"

REM Flask uygulamasini baslat
python app.py 