@echo off
echo Candan Python Düzenleyicisi başlatılıyor...

REM Python'un yüklü olup olmadığını kontrol et
python --version >nul 2>&1
if errorlevel 1 (
    echo Python yüklü değil! Lütfen Python'u yükleyin.
    pause
    exit /b 1
)

REM pip kurulumunu kontrol et ve gerekirse yükle
echo Gerekli paketler kontrol ediliyor...
pip install -r requirements.txt

REM Uygulamayı başlat
echo Uygulama başlatılıyor...
python app.py
pause 