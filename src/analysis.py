import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

PROCESSED_PATH = os.getenv("DATA_PROCESSED_PATH")

def run_eda():
    df = pd.read_csv(os.path.join(PROCESSED_PATH, "featured_data.csv"))
    df['date'] = pd.to_datetime(df['date'])

    print("========== EDA RESULTS ==========")

    # 1. Avg PnL by sentiment
    print("\n1. Avg Closed PnL by Market Condition:")
    print(df.groupby('classification')['closed_pnl'].mean().round(2))

    # 2. Win rate by sentiment
    print("\n2. Win Rate by Market Condition:")
    print(df.groupby('classification')['is_win'].mean().round(4) * 100)

    # 3. Avg leverage by sentiment
    print("\n3. Avg Leverage Proxy by Market Condition:")
    print(df.groupby('classification')['leverage_proxy'].mean().round(2))

    # 4. Trade frequency by sentiment
    print("\n4. Trade Count by Market Condition:")
    print(df.groupby('classification')['closed_pnl'].count())

    # 5. Correlation: leverage vs PnL
    print("\n5. Correlation between Leverage and Closed PnL:")
    print(df[['leverage_proxy', 'closed_pnl']].corr().round(4))

    # 6. High leverage + Greed pattern
    print("\n6. High Leverage + Greed vs Fear (Avg PnL):")
    df['high_leverage'] = df['leverage_proxy'] > df['leverage_proxy'].quantile(0.75)
    print(df[df['high_leverage']].groupby('market_condition')['closed_pnl'].mean().round(2))

def coin_analysis():
    df = pd.read_csv(os.path.join(PROCESSED_PATH, "featured_data.csv"))

    print("========== COIN ANALYSIS ==========")

    # 1. Avg PnL by coin
    print("\n1. Avg PnL by Coin:")
    print(df.groupby('coin')['closed_pnl'].mean().round(2).sort_values(ascending=False).head(10))

    # 2. Win rate by coin
    print("\n2. Win Rate by Coin (%):")
    print((df.groupby('coin')['is_win'].mean() * 100).round(2).sort_values(ascending=False).head(10))

    # 3. Avg PnL by coin + sentiment
    print("\n3. Avg PnL — Top 5 Coins by Sentiment:")
    top5 = df['coin'].value_counts().head(5).index
    print(df[df['coin'].isin(top5)].groupby(['coin', 'classification'])['closed_pnl'].mean().round(2))

if __name__ == "__main__":
    run_eda()
    coin_analysis()