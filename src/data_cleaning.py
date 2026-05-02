import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

RAW_PATH = os.getenv("DATA_RAW_PATH")
PROCESSED_PATH = os.getenv("DATA_PROCESSED_PATH")

def clean_trader_data():
    df = pd.read_csv(os.path.join(RAW_PATH, "historical_data.csv"))

    # Standardize column names
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

    # Convert timestamp to datetime
    df['date'] = pd.to_datetime(df['timestamp_ist'], format='mixed', dayfirst=True).dt.date
    # Remove rows where execution price is zero or near zero
    df = df[df['execution_price'] > 0.01]

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Cap extreme size_tokens outliers (top 1%)
    upper = df['size_tokens'].quantile(0.99)
    df = df[df['size_tokens'] <= upper]

    print("✅ Trader Data Cleaned")
    print("Shape after cleaning:", df.shape)
    print(df.head(3))
    return df

def clean_sentiment_data():
    df = pd.read_csv(os.path.join(RAW_PATH, "fear_greed_index.csv"))

    # Standardize column names
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

    # Convert date to datetime
    df['date'] = pd.to_datetime(df['date']).dt.date

    # Drop timestamp column (not needed)
    df = df.drop(columns=['timestamp'])

    # Remove duplicates
    df = df.drop_duplicates()

    print("\n✅ Sentiment Data Cleaned")
    print("Shape after cleaning:", df.shape)
    print(df.head(3))
    return df

def merge_data(trader, sentiment):
    # Convert date columns to same type
    trader['date'] = pd.to_datetime(trader['date'])
    sentiment['date'] = pd.to_datetime(sentiment['date'])

    # Merge on date
    merged = pd.merge(trader, sentiment, on='date', how='inner')

    print("\n✅ Data Merged")
    print("Shape after merge:", merged.shape)
    print("Date range:", merged['date'].min(), "→", merged['date'].max())
    print(merged.head(3))
    return merged

if __name__ == "__main__":
    trader = clean_trader_data()
    sentiment = clean_sentiment_data()
    merged = merge_data(trader, sentiment)

    # Save to processed folder
    merged.to_csv(os.path.join(PROCESSED_PATH, "merged_cleaned_data.csv"), index=False)
    print("\n✅ Saved to data/processed/merged_cleaned_data.csv")
    