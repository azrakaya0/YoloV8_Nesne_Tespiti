# YOLOv8 Tabanlı Nesne Tespiti Projesi (Cat & Apple)

Bu proje, YOLOv8 derin öğrenme modeli kullanılarak kedi (cat) ve elma (apple)
nesnelerinin görüntüler üzerinde otomatik olarak tespit edilmesini amaçlamaktadır.
Çalışma kapsamında özel bir veri seti hazırlanmış, model eğitilmiş ve elde edilen
model PyQt5 tabanlı bir grafik arayüz (GUI) ile test edilmiştir.

---

## Projenin Amacı

Bu projenin temel amacı:
- YOLOv8 mimarisinin nesne tespitindeki kullanımını öğrenmek
- Özel bir veri seti ile model eğitme sürecini deneyimlemek
- Eğitilen modeli gerçek bir uygulama (GUI) üzerinden kullanabilektir

Proje, teorik bilginin pratiğe dökülmesini hedeflemektedir.

---

## Kullanılan Yöntem

Proje üç ana aşamadan oluşmaktadır:

### 1. Veri Seti Hazırlama
- Kedi ve elma nesnelerini içeren görseller kullanılmıştır
- Her görsel için YOLO formatında etiketleme yapılmıştır
- Veri seti train / validation / test olarak ayrılmıştır

### 2. Model Eğitimi
- YOLOv8 (Ultralytics) modeli kullanılmıştır
- Eğitim süreci Jupyter Notebook ortamında gerçekleştirilmiştir
- Eğitim sonunda en iyi model ağırlıkları `best.pt` olarak kaydedilmiştir

### 3. Modelin Test Edilmesi (GUI)
- PyQt5 kullanılarak bir grafik arayüz geliştirilmiştir
- Kullanıcı arayüzden görsel seçebilmektedir
- Seçilen görsel üzerinde nesne tespiti yapılarak sonuçlar gösterilmektedir

---

## Kullanılan Teknolojiler

- Python
- YOLOv8 (Ultralytics)
- PyTorch
- OpenCV
- PyQt5
- Jupyter Notebook

---

## Sınıflar

Model 2 sınıf üzerinden eğitilmiştir:

0 : cat  
1 : apple  

---

## Model Eğitimi

Model eğitimi `yolo_training.ipynb` dosyasında adım adım gerçekleştirilmiştir.
Bu dosyada:
- Veri seti kontrolü
- YOLOv8 eğitim ayarları
- Eğitim çıktıları
- Model kaydetme işlemleri yer almaktadır

---

## GUI Uygulaması

`gui_app.py` dosyası PyQt5 kullanılarak geliştirilmiştir.
GUI uygulaması sayesinde:
- Eğitilen model kolayca test edilebilmektedir
- Kullanıcı teknik detaylara girmeden modeli deneyebilmektedir

---

## Çalıştırma

GUI uygulamasını çalıştırmak için:

python gui_app.py

---


## Sonuç

Bu projede YOLOv8 kullanılarak iki sınıflı bir nesne tespit sistemi geliştirilmiştir.
Elde edilen sonuçlar, modelin kedi ve elma nesnelerini başarılı bir şekilde tespit
edebildiğini göstermektedir.


