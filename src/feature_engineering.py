import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

PROCESSED_PATH = os.getenv("DATA_PROCESSED_PATH")

def engineer_features():
    df = pd.read_csv(os.path.join(PROCESSED_PATH, "merged_cleaned_data.csv"))

    # Convert date
    df['date'] = pd.to_datetime(df['date'])

    # 1. Win/Loss flag (1 = profit, 0 = loss)
    df['is_win'] = (df['closed_pnl'] > 0).astype(int)

    # 2. Market condition (Fear=0, Greed=1)
    df['market_condition'] = df['classification'].apply(
        lambda x: 0 if 'Fear' in str(x) else 1
    )

    # 3. Daily PnL per trader
    daily_pnl = df.groupby(['date', 'account'])['closed_pnl'].sum().reset_index()
    daily_pnl.columns = ['date', 'account', 'daily_pnl']
    df = pd.merge(df, daily_pnl, on=['date', 'account'], how='left')

    # 4. Average leverage per day (size_usd / execution_price as proxy)
    df['leverage_proxy'] = df['size_usd'] / df['execution_price'].replace(0, 1)

    # 5. Trade volume per day
    daily_volume = df.groupby('date')['size_usd'].sum().reset_index()
    daily_volume.columns = ['date', 'daily_volume']
    df = pd.merge(df, daily_volume, on='date', how='left')

    print("✅ Features Created")
    print("Shape:", df.shape)
    print("New columns:", ['is_win', 'market_condition', 'daily_pnl', 'leverage_proxy', 'daily_volume'])
    print(df[['date', 'closed_pnl', 'is_win', 'market_condition', 'daily_pnl', 'leverage_proxy']].head(5))

    # Save
    df.to_csv(os.path.join(PROCESSED_PATH, "featured_data.csv"), index=False)
    print("\n✅ Saved to data/processed/featured_data.csv")
    return df

if __name__ == "__main__":
    engineer_features()
    