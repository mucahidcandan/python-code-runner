@echo off
chcp 65001 >nul
echo ====================================
echo Python Kod Calistirici Baslatiliyor
echo ====================================
echo.

REM Python'un yuklu olup olmadigini kontrol et
python --version >nul 2>&1
if errorlevel 1 (
    echo [HATA] Python yuklu degil!
    echo Lutfen https://www.python.org/downloads/ adresinden Python'u indirip yukleyin.
    echo Yukleme sirasinda "Add Python to PATH" secenegini isaretlemeyi unutmayin.
    echo.
    pause
    exit /b 1
)

REM pip kurulumunu kontrol et ve gerekirse yukle
echo [BILGI] Gerekli paketler kontrol ediliyor...
pip install -r requirements.txt >nul 2>&1
if errorlevel 1 (
    echo [HATA] Paketler yuklenirken bir hata olustu!
    echo Lutfen internet baglantinizi kontrol edin ve tekrar deneyin.
    echo.
    pause
    exit /b 1
)

REM Port kontrolu
echo [BILGI] Port kontrolu yapiliyor...
netstat -ano | find ":5000" >nul
if not errorlevel 1 (
    echo [UYARI] 5000 portu kullanimda!
    echo Eski uygulama kapatiliyor...
    for /f "tokens=5" %%a in ('netstat -aon ^| find ":5000"') do taskkill /F /PID %%a >nul 2>&1
    timeout /t 2 >nul
)

REM Uygulamayi baslat
echo [BILGI] Uygulama baslatiliyor...
echo Tarayicinizda otomatik olarak acilacaktir...
echo.

REM Uygulamayi arka planda baslat
start /B python app.py

REM Tarayiciyi acmadan once kisa bir bekleme
timeout /t 2 >nul

REM Tarayiciyi ac
start http://localhost:5000

REM Ana pencereyi acik tut
pause 