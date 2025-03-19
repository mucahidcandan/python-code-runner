# Candan Python Düzenleyicisi

Bu uygulama, Python kodlarını çalıştırmak ve test etmek için geliştirilmiş basit bir web tabanlı editördür.

## Özellikler

- Çoklu sekme desteği
- Python kod çalıştırma
- Paket yükleme desteği
- Kod kaydetme
- Syntax highlighting
- Otomatik girinti
- Hata yakalama ve gösterimi
- Güvenli kod çalıştırma ortamı
- Gerçek zamanlı çıktı görüntüleme

## Gereksinimler

- Windows 10 veya üzeri
- Python 3.8 veya daha yüksek bir sürüm
- İnternet bağlantısı (paket yüklemek için)

## Kurulum ve Çalıştırma

1. Python'u yükleyin (eğer yüklü değilse)
   - https://www.python.org/downloads/ adresinden indirin
   - Yükleme sırasında "Add Python to PATH" seçeneğini işaretleyin

2. `run.bat` dosyasını çift tıklayarak çalıştırın
   - Gerekli paketler otomatik olarak yüklenecektir
   - Uygulama otomatik olarak başlayacaktır
   - Tarayıcınızda otomatik olarak `http://localhost:5000` adresine yönlendirileceksiniz

3. Eğer otomatik yönlendirme olmazsa:
   - Tarayıcınızı açın
   - `http://localhost:5000` adresine gidin

## Kullanım

1. Editörde Python kodunuzu yazın
2. Üst kısımdaki "Kodu Çalıştır" butonuna tıklayın
3. Çıktıyı alt kısımdaki panelde görebilirsiniz
4. Yeni sekme eklemek için "+" butonuna tıklayın
5. Paket yüklemek için konsol kısmına `pip install paket_adi` yazın

## Güvenlik Notları

- Uygulama, güvenlik nedeniyle bazı Python komutlarını kısıtlar (os, sys, subprocess, eval, exec)
- Kod çalıştırma süresi 5 saniye ile sınırlandırılmıştır
- Her kod çalıştırma işlemi izole bir ortamda gerçekleştirilir

## Geliştirici

Dr. Mücahid Candan ve Yapay Zeka 