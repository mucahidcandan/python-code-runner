# Python Kod Çalıştırıcı

Bu web uygulaması, öğrencilerin Python kodlarını tarayıcı üzerinden yazıp çalıştırabilmelerini sağlar.

## Özellikler

- Syntax highlighting ile kod editörü
- Gerçek zamanlı kod çalıştırma
- Güvenli kod çalıştırma ortamı
- Kullanıcı dostu arayüz

## Kurulum

1. Gerekli paketleri yükleyin:
```bash
pip install -r requirements.txt
```

2. Uygulamayı çalıştırın:
```bash
python app.py
```

3. Tarayıcınızda `http://localhost:5000` adresine gidin.

## Güvenlik Notları

- Uygulama, güvenlik nedeniyle bazı Python komutlarını kısıtlar (os, sys, subprocess, eval, exec)
- Kod çalıştırma süresi 5 saniye ile sınırlandırılmıştır
- Her kod çalıştırma işlemi izole bir ortamda gerçekleştirilir

## Teknolojiler

- Flask
- CodeMirror
- Bootstrap
- Python 