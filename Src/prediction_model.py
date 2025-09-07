import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import joblib

def train_model(df):
    df = df.dropna(subset=['sentiment', 'price_usd'])
    X = df[['sentiment']]
    y = df['price_usd']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    print("RMSE:", mean_squared_error(y_test, preds, squared=False))
    joblib.dump(model, 'model.pkl')
    return model

def predict_price(sentiment_score):
    model = joblib.load('model.pkl')
    return model.predict([[sentiment_score]])[0]
