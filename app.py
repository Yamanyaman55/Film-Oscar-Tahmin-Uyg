import streamlit as st
import pandas as pd
import joblib
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import base64

def get_base64(file_path):
    with open(file_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()


# Model ve kolon listesini yükle
model = joblib.load("model.pkl")
columns = joblib.load("columns.pkl")

MODEL_FILES = {
    "Linear Regression": "model_linear.pkl",
    "Random Forest": "model_rf.pkl",
    "XGBoost": "model_xgb.pkl"
}

st.title("🎬 IMDb Puan Tahmin Uygulaması")

model_name = st.selectbox("📌 Tahmin modeli seçin:", list(MODEL_FILES.keys()))

if model_name == "Linear Regression":
    model = joblib.load("model_linear.pkl")
elif model_name == "Random Forest":
    model = joblib.load("model_rf.pkl")
else:
    model = joblib.load("model_xgb.pkl")

st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{get_base64("film_foto.jpeg")}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        position: relative;
    }}

    /* Karanlık overlay filtresi */
    .stApp::before {{
        content: "";
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(0, 0, 0, 0.5); /* %50 siyah karartma */
        z-index: 0;
    }}

    /* Uygulama içeriğini overlay'in üzerine getir */
    .stApp > * {{
        position: relative;
        z-index: 1;
    }}

    /* Yazıların rengini beyaz yap */
    .stApp h1, .stApp h2, .stApp h3, .stApp p, .stApp label, .stApp span {{
        color: white !important;
    }}

        /* Sadece st.button içindeki yazıyı siyah yap */
    .stButton > button {{
        color: black !important;
        background-color: red !important;
        border-radius: 8px;
        font-weight: bold;
        padding: 0.5em 1.5em;
    }}

    

    </style>
    """,
    unsafe_allow_html=True
)



# Kullanıcıdan veri al
runtime = st.number_input("Süre (dakika)", value=100)
metascore = st.slider("Metascore", 0, 100, 70)
votes = st.number_input("Oy Sayısı", value=50000)
revenue = st.number_input("Hasılat (milyon $)", value=100.0)
genre = st.selectbox("Tür", ['Action', 'Adventure', 'Animation', 'Biography', 'Comedy', 'Crime', 'Drama', 'Horror', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'Western'])
# Veri setini yükle 
@st.cache_data
def load_data():
    return pd.read_csv("IMDB-Movie-Data.csv")

df = load_data()

# Tahmin butonu
if st.button("Tahmin Et"):
    input_data = {
        'Runtime (Minutes)': runtime,
        'Metascore': metascore,
        'Votes': votes,
        'Revenue (Millions)': revenue
    }
    

    # Diğer kolonları 0 yap
    for col in columns:
        if col not in input_data:
            input_data[col] = 0

    # Türe göre doğru kolonu 1 yap
    genre_col = f"Genre_{genre}"
    if genre_col in columns:
        input_data[genre_col] = 1

    # DataFrame'e çevir ve tahmin yap
    input_df = pd.DataFrame([input_data])
    prediction = model.predict(input_df)[0]

    st.success(f"Tahmini IMDb Puanı: {prediction:.2f}")
      # IMDb tahmini yapıldıktan hemen sonra referanslarla karşılaştırma
    st.markdown("### 🎯 Film Özellikleri vs Oscar Referansları")

    # Oscar ortalamaları referans alınarak tablo hazırlanır
    comparison_data = {
        "Özellik": ["IMDb Tahmini", "Metascore", "Süre (dk)", "Oy Sayısı", "Hasılat (milyon $)"],
        "Senin Filmin": [round(prediction, 2), metascore, runtime, votes, revenue],
        "Oscar Filmleri Ort.": [8.1, 77, 135, 150000, 120]
    }
    comparison_df = pd.DataFrame(comparison_data)
    st.table(comparison_df)

   # Oscar alma potansiyeli tahmini
    oscar_genres = ["Drama", "Biography", "Mystery","Action","Adventure","Animation","Crime","Comedy"]
    is_oscar_genre = genre in oscar_genres

    if prediction >= 8.0 and metascore >= 75 and revenue >= 100 and votes >= 100000 and is_oscar_genre:
        st.success("🏆 Bu film Oscar alabilir! Tüm güçlü kriterleri karşılıyor! 🎬✨")
    elif prediction >= 7.5 and (metascore >= 70 or revenue >= 80) and is_oscar_genre:
        st.info("🌟 Bu film bazı prestijli ödüller için aday olabilir.")
    else:
        st.warning("🙁 Oscar potansiyeli düşük. Ama belki kült film olur!")



# Grafik 1: Türlere Göre Ortalama IMDb Puanları
st.subheader("🎬 Türlere Göre Ortalama IMDb Puanları")

# Genre sütununda boş olmayan verilerle çalış
genre_ratings = df[df['Genre'].notna()].copy()
genre_ratings['Genre'] = genre_ratings['Genre'].apply(lambda x: x.split(',')[0].strip())  # İlk türü al
genre_rating_means = genre_ratings.groupby('Genre')['Rating'].mean().sort_values(ascending=False)

fig1, ax1 = plt.subplots()
sns.barplot(x=genre_rating_means.values, y=genre_rating_means.index, ax=ax1)
ax1.set_xlabel("Ortalama IMDb Puanı")
ax1.set_ylabel("Tür (Genre)")
st.pyplot(fig1)

# Grafik 2: Metascore ile IMDb Puanı Arasındaki İlişki
st.subheader("🟣 Metascore ile IMDb Puanı Arasındaki İlişki")

fig2, ax2 = plt.subplots()
sns.scatterplot(data=df, x="Metascore", y="Rating", alpha=0.6)
ax2.set_xlabel("Metascore")
ax2.set_ylabel("IMDb Puanı")
st.pyplot(fig2)
# Grafik 3: Hasılat ve IMDb Puanı İlişkisi
st.subheader("💰 Hasılat (Revenue) ile IMDb Puanı Arasındaki İlişki")


fig3, ax3 = plt.subplots()
sns.scatterplot(data=df, x="Revenue (Millions)", y="Rating", alpha=0.6)
ax3.set_xlabel("Hasılat (Milyon $)")
ax3.set_ylabel("IMDb Puanı")
st.pyplot(fig3)
# Grafik 4: Oy Sayısı ve IMDb Puanı Dağılımı
st.subheader("🗳️ Oy Sayısı ile IMDb Puanı Dağılımı")

fig4, ax4 = plt.subplots()
sns.histplot(data=df, x="Rating", bins=20, kde=True, hue=None)
ax4.set_xlabel("IMDb Puanı")
ax4.set_ylabel("Film Sayısı")
st.pyplot(fig4)


