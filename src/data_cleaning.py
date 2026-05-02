import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

RAW_PATH = os.getenv("DATA_RAW_PATH")

def audit_data():
    trader = pd.read_csv(os.path.join(RAW_PATH, "historical_data.csv"))
    sentiment = pd.read_csv(os.path.join(RAW_PATH, "fear_greed_index.csv"))

    print("========== TRADER DATA ==========")
    print("\n-- Info --")
    print(trader.info())
    print("\n-- Nulls --")
    print(trader.isnull().sum())
    print("\n-- Describe --")
    print(trader.describe())

    print("\n========== SENTIMENT DATA ==========")
    print("\n-- Info --")
    print(sentiment.info())
    print("\n-- Nulls --")
    print(sentiment.isnull().sum())
    print("\n-- Describe --")
    print(sentiment.describe())

if __name__ == "__main__":
    audit_data()