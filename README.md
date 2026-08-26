Markdown
# 🏋️‍♂️ 30-Day Fitness & Calorie Command Center

Modern, şık ve kullanımı kolay bir masaüstü fitness, kalori ve antrenman takip uygulaması. **CustomTkinter** arayüzü ve **SQLite** veritabanı altyapısı ile geliştirilmiştir.

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![CustomTkinter](https://img.shields.io/badge/UI-CustomTkinter-blue?style=for-the-badge)
![SQLite](https://img.shields.io/badge/Database-SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)

---

## ✨ Özellikler

* **🏠 Ana Dashboard:** Günlük toplam harcanan kalori, su tüketimi ve son 7 günün kalori yakım grafiği (`Matplotlib` entegrasyonu).
* **🏃 Egzersiz & Yürüyüş Takibi:** Günlük adım, yürüyüş süresi ve egzersiz bazlı set/tekrar/kalori takibi.
* **⚙️ Egzersiz Kütüphanesi Yönetimi:** Özel egzersizler ekleme, mevcut egzersizlerin parametrelerini (Set, Tekrar, kcal) düzenleme ve silme.
* **⚖️ Kilo & VKI (BMI) Takibi:** Günlük kilo kaydı, VKI hesaplama ve kilo değişim trend grafiği.
* **🎯 Kişiselleştirilebilir Hedefler:** Günlük kalori ve su tüketim hedeflerini dinamik olarak ayarlama.
* **📊 Excel İçe / Dışa Aktarma:** Verileri `.xlsx` formatında dışa aktarma ve yedeklenen verileri geri yükleme.

---

## 🛠️ Kurulum

Projeyi yerel makinenizde çalıştırmak için aşağıdaki adımları izleyin.

### 1. Repoyu klonlayın
```bash
git clone [https://github.com/YEMRESTT/fitness-command-center.git](https://github.com/YEMRESTT/fitness-command-center.git)
cd fitness-command-center
2. Gerekli kütüphaneleri yükleyin
Bash
pip install customtkinter matplotlib openpyxl
3. Uygulamayı başlatın
Bash
python main.py
📁 Proje Yapısı
Plaintext
fitness/
├── main.py              # CustomTkinter arayüzü ve ana uygulama mantığı
├── database.py          # SQLite veritabanı bağlantısı ve tablo mantıkları
├── fitness.db           # Yerel veritabanı dosyası (Otomatik oluşturulur)
└── README.md            # Proje dokümantasyonu
```


### Bu proje eğitim ve kişisel kullanım amacıyla geliştirilmiştir. İstediğiniz gibi kullanabilir ve geliştirebilirsiniz.