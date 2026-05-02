import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

RAW_PATH = os.getenv("DATA_RAW_PATH")

def load_trader_data():
    path = os.path.join(RAW_PATH, "historical_data.csv")
    df = pd.read_csv(path)
    print("✅ Trader Data Loaded")
    print("Shape:", df.shape)
    print("Columns:", df.columns.tolist())
    print(df.head(3))
    return df

def load_sentiment_data():
    path = os.path.join(RAW_PATH, "fear_greed_index.csv")
    df = pd.read_csv(path)
    print("\n✅ Fear & Greed Data Loaded")
    print("Shape:", df.shape)
    print("Columns:", df.columns.tolist())
    print(df.head(3))
    return df

if __name__ == "__main__":
    trader = load_trader_data()
    sentiment = load_sentiment_data()