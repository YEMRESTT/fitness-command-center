# 🏋️‍♂️ 30-Day Fitness & Calorie Command Center

Modern, şık ve kullanımı kolay bir masaüstü **Masaüstü Fitness ve Sağlık Takip Uygulaması**.  
Bu uygulama; günlük egzersizlerinizi, yürüyüşlerinizi, su tüketiminizi, kilonuzu ve VKI (BMI) değerlerinizi tek bir merkezden takip etmenizi sağlar.

---

## ✨ Öne Çıkan Özellikler

* **🔥 Ana Dashboard:** 
  * Günlük toplam harcanan kalori ve su tüketimi ilerleme barları.
  * Hızlı su ekleme butonları (+250ml, +500ml).
  * Günlük not / ruh hali kaydı.
  * Son 7 günün kalori yakım trendini gösteren dinamik grafik.

* **🏃 Egzersiz & Yürüyüş Yönetimi:**
  * Günlük yürüyüş süresi, adım sayısı ve kalori kaydı.
  * Egzersizleri **✅ Yapıldı**, **❌ Atlandı** veya **🔄 Sıfırla (Beklemede)** olarak işaretleme.
  * Set, tekrar veya birim kalori değerlerini anlık olarak güncelleyebilme.
  * Tarihe özel dinamik kart renkleri (Yeşil: Yapıldı, Kırmızı: Atlandı, Nötr: Beklemede).

* **⚙️ Egzersiz Kütüphanesi:**
  * Sık kullandığınız hareketleri (Şınav, Mekik, Squat vb.) varsayılan set/tekrar ve kalori değerleriyle kütüphaneye kaydetme.
  * Kütüphanedeki egzersizleri düzenleme veya silme.

* **⚖️ Kilo & VKI (BMI) Takibi:**
  * Boy ve kilo bilgisine göre anlık VKI (Vücut Kitle İndeksi) hesaplama ve durum analizi.
  * Zaman içindeki kilo değişimini gösteren Matplotlib destekli çizgi grafiği.

* **🎯 Kişiselleştirilebilir Hedefler:**
  * Günlük hedef kalori ve su miktarını belirleyebilme.

* **📊 Analiz & Raporlar:**
  * Toplam ve ortalama kalori yakımları, tamamlanan/atlanan antrenman sayıları.

* **📊 Excel Entegrasyonu (İçe / Dışa Aktarma):**
  * Tüm verilerinizi tek tıkla `.xlsx` formatında dışa aktarma (Yedekleme).
  * Daha önce kaydettiğiniz Excel dosyalarını uygulamaya geri yükleme.

---

## 🛠️ Teknolojiler ve Kütüphaneler

* **Dil:** Python 3.10+
* **Arayüz (GUI):** `CustomTkinter` (Modern Dark Mode temasıyla)
* **Veritabanı:** SQLite3 (Yerel ve hızlı veri depolama)
* **Veri Görselleştirme:** `Matplotlib` (Dinamik grafikler için)
* **Excel İşlemleri:** `openpyxl`

---

## 🚀 Kurulum ve Çalıştırma

### 1. Depoyu Klonlayın veya İndirin
```bash
git clone [https://github.com/kullanici-adi/fitness-command-center.git](https://github.com/kullanici-adi/fitness-command-center.git)
cd fitness-command-center
```
2. Gerekli Kütüphaneleri Yükleyin
```
Uygulamanın sorunsuz çalışması için gerekli bağımlılıkları yükleyin:

Bash
pip install customtkinter matplotlib openpyxl
```
3. Uygulamayı Başlatın
```
Bash
python main.py
📁 Proje Dosya Yapısı
Plaintext
├── main.py              # Uygulamanın ana grafik arayüzü (GUI) ve sayfa mantıkları
├── database.py          # SQLite veritabanı bağlantıları ve Tablo oluşturma işlemleri
├── fitness_tracker.db   # Otomatik oluşturulan yerel veritabanı dosyası
├── app_icon.ico         # (Opsiyonel) Uygulama ikonu
└── README.md            # Proje dokümantasyonu
```
---
📝 Kullanım İpuçları
```
İlk Başlangıç: Uygulama ilk açıldığında varsayılan egzersiz kütüphanesini ve fitness_tracker.db dosyasını otomatik olarak oluşturur.

Durum Sıfırlama: Egzersiz kartlarındaki 🔄 butonuna basarak yanlışlıkla işaretlediğiniz bir hareketin durumunu tekrar nötr hale getirebilirsiniz.

Yedek Alma: Verilerinizi kaybetmemek için istediğiniz zaman "Excel'e Aktar" butonunu kullanabilirsiniz.