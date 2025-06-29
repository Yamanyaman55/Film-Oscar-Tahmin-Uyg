# Film-Oscar-Tahmin-Uyg

🎬 IMDb Puan Tahmin Uygulaması
Bu proje, kullanıcı tarafından girilen film özelliklerine (tür, süresi, metascore, oy sayısı, hasılat) göre IMDb puanı tahmini yapan ve tahmine göre Oscar alma potansiyeli değerlendirmesi sunan etkileşimli bir Streamlit uygulamasıdır.



🚀 Özellikler
🎯 IMDb puanı tahmini: Linear Regression, Random Forest ve XGBoost gibi üç farklı model seçeneği

🏆 Oscar potansiyeli analizi: Tahmin sonuçları Oscar kazanmış filmlerle karşılaştırılır

📊 Veri görselleştirme:

Türlere göre ortalama IMDb puanı

Metascore ile IMDb puanı ilişkisi

Hasılat ile IMDb puanı ilişkisi

Oy sayısı dağılımı

🧠 Kullanılan Makine Öğrenimi Modelleri
Linear Regression

Random Forest

XGBoost

Tüm modeller, IMDB-Movie-Data.csv veri seti kullanılarak eğitilmiştir.

🛠️ Kurulum
Python ortamınızda aşağıdaki adımları takip ederek projeyi çalıştırabilirsiniz:

1. Gerekli kütüphaneleri yükleyin:
bash
Kopyala
Düzenle
pip install -r requirements.txt
Veya manuel olarak:

bash
Kopyala
Düzenle
pip install streamlit pandas joblib matplotlib seaborn xgboost scikit-learn
2. Uygulamayı çalıştırın:
bash
Kopyala
Düzenle
streamlit run app.py
📁 Dosya Yapısı
bash
Kopyala
Düzenle
.
├── app.py                  # Streamlit uygulama dosyası
├── IMDB-Movie-Data.csv     # Film verisi
├── model_linear.pkl        # Linear Regression modeli
├── model_rf.pkl            # Random Forest modeli (eklenmeli)
├── model_xgb.pkl           # XGBoost modeli (eklenmeli)
├── columns.pkl             # Özellik sütunları listesi
├── film_foto.jpeg          # Arka plan görseli
🖼️ Ekran Görüntüsü


🔮 Gelecek Geliştirmeler
🎥 Kullanıcıya özel film öneri sistemi

💬 Kullanıcıdan doğal dil girdisi alarak film özelliklerini otomatik çıkartma

🌐 Uygulamanın web üzerinde paylaşılabilir hale getirilmesi (Streamlit Cloud / HuggingFace Spaces)

📌 Notlar
Projede kullanılan modellerin .pkl dosyaları aynı klasörde olmalıdır.

Uygulamada film_foto.jpeg adlı görsel kullanılmaktadır, eksikse hata verebilir.

👨‍💻 Geliştirici
Nurullah Yaman
