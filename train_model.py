import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split
import joblib

# 1. Veriyi oku
df = pd.read_csv("IMDB-Movie-Data.csv")
df = df.dropna()

# 2. İlk türü al
df['Genre'] = df['Genre'].apply(lambda x: x.split(',')[0])

# 3. Türleri sayısal hale getir
df = pd.get_dummies(df, columns=['Genre'], drop_first=True)

# 4. Özellikler ve hedef
X = df[['Runtime (Minutes)', 'Metascore', 'Votes', 'Revenue (Millions)'] + [col for col in df.columns if 'Genre_' in col]]
y = df['Rating']

# 5. Veriyi ayır
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 6. Linear Regression
lr = LinearRegression()
lr.fit(X_train, y_train)
joblib.dump(lr, "model_linear.pkl")

# 7. Random Forest
rf = RandomForestRegressor()
rf.fit(X_train, y_train)
joblib.dump(rf, "model_rf.pkl")

# 8. XGBoost
xgb = XGBRegressor()
xgb.fit(X_train, y_train)
joblib.dump(xgb, "model_xgb.pkl")

# 9. Kolonları kaydet
joblib.dump(X.columns.tolist(), "columns.pkl")

print("✅ Tüm modeller kaydedildi.")

