# Python Code Runner Kurulum Kılavuzu

## Geliştirici için Kurulum

1. Gerekli yazılımları yükleyin:
   - Node.js (https://nodejs.org/)
   - Python (https://www.python.org/downloads/)
   - Git (https://git-scm.com/)

2. Projeyi klonlayın:
```bash
git clone [proje-url]
cd python-code-runner
```

3. Bağımlılıkları yükleyin:
```bash
npm install
pip install -r requirements.txt
```

4. Uygulamayı geliştirme modunda çalıştırın:
```bash
npm start
```

5. Uygulamayı derleyin:
```bash
npm run build
```

## Öğrenciler için Kurulum

### Windows
1. `dist` klasöründeki `Python Code Runner Setup.exe` dosyasını çalıştırın
2. Kurulum sihirbazını takip edin
3. Masaüstündeki "Python Code Runner" kısayoluna çift tıklayarak uygulamayı başlatın

### macOS
1. `dist` klasöründeki `Python Code Runner.dmg` dosyasını çift tıklayın
2. Uygulamayı Applications klasörüne sürükleyin
3. Applications klasöründen "Python Code Runner" uygulamasını başlatın

### Linux
1. `dist` klasöründeki `python-code-runner.AppImage` dosyasını çalıştırılabilir yapın:
```bash
chmod +x python-code-runner.AppImage
```
2. Dosyaya çift tıklayarak uygulamayı başlatın

## Özellikler
- Çoklu sekme desteği
- Python kod çalıştırma
- Paket yükleme desteği
- Gerçek zamanlı çıktı görüntüleme
- Güvenli kod çalıştırma ortamı

## Gereksinimler
- Windows 10 veya üzeri
- macOS 10.13 veya üzeri
- Linux (Ubuntu 18.04 veya üzeri)
- Python 3.8 veya üzeri

## Güvenlik Notları
- Uygulama, güvenlik nedeniyle bazı Python komutlarını kısıtlar
- Kod çalıştırma süresi 5 saniye ile sınırlandırılmıştır
- Her kod çalıştırma işlemi izole bir ortamda gerçekleştirilir

## İletişim
Sorularınız için: Dr. Mücahid Candan 