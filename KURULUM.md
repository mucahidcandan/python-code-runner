# Candan Python Düzenleyici Kurulum Kılavuzu

## Geliştirici için Kurulum

1. Gerekli yazılımları yükleyin:
   - Python 3.8 veya üzeri (https://www.python.org/downloads/)
   - Git (https://git-scm.com/)

2. Projeyi klonlayın:
```bash
git clone [proje-url]
cd python-code-runner
```

3. Bağımlılıkları yükleyin:
```bash
pip install -r requirements.txt
```

4. Uygulamayı çalıştırın:
```bash
python app.py
```

## Kullanıcılar için Kurulum

### Windows
1. Python'u yükleyin (eğer yüklü değilse):
   - https://www.python.org/downloads/ adresinden indirin
   - Yükleme sırasında "Add Python to PATH" seçeneğini işaretleyin

2. Uygulamayı başlatın:
   - `run.bat` dosyasını çift tıklayın
   - Gerekli paketler otomatik olarak yüklenecektir
   - Uygulama otomatik olarak tarayıcınızda açılacaktır

## Özellikler
- Çoklu sekme desteği
- Python kod çalıştırma
- Paket yükleme desteği
- Gerçek zamanlı çıktı görüntüleme
- Güvenli kod çalıştırma ortamı
- Syntax highlighting
- Otomatik girinti
- Hata yakalama ve gösterimi

## Gereksinimler
- Windows 10 veya üzeri
- Python 3.8 veya üzeri
- İnternet bağlantısı (paket yüklemek için)

## Güvenlik Notları
- Uygulama, güvenlik nedeniyle bazı Python komutlarını kısıtlar:
  - os modülü
  - sys modülü
  - subprocess modülü
  - eval() fonksiyonu
  - exec() fonksiyonu
- Kod çalıştırma süresi 5 saniye ile sınırlandırılmıştır
- Her kod çalıştırma işlemi izole bir ortamda gerçekleştirilir
- Paket yükleme süresi 30 saniye ile sınırlandırılmıştır

## Sorun Giderme

### Python Yüklü Değil
1. https://www.python.org/downloads/ adresinden Python'u indirin
2. Yükleme sırasında "Add Python to PATH" seçeneğini işaretleyin
3. Bilgisayarınızı yeniden başlatın
4. `run.bat` dosyasını tekrar çalıştırın

### Port Hatası
1. Eğer "5000 portu kullanımda" hatası alırsanız:
   - Uygulama otomatik olarak eski işlemi kapatacaktır
   - 2 saniye bekleyin
   - Tarayıcı otomatik olarak açılacaktır

### Paket Yükleme Hatası
1. İnternet bağlantınızı kontrol edin
2. Paket adının doğru yazıldığından emin olun
3. Konsol kısmına `pip install paket_adi` yazın

## İletişim
Sorularınız için: Dr. Mücahid Candan 