import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from dotenv import load_dotenv
import os

load_dotenv()

PROCESSED_PATH = os.getenv("DATA_PROCESSED_PATH")
PLOTS_PATH = os.path.join(os.getenv("OUTPUTS_PATH"), "plots")

def create_visualizations():
    df = pd.read_csv(os.path.join(PROCESSED_PATH, "featured_data.csv"))
    df['date'] = pd.to_datetime(df['date'])

    sns.set_theme(style="darkgrid")
    order = ['Extreme Fear', 'Fear', 'Neutral', 'Greed', 'Extreme Greed']

    # 1. Avg PnL vs Sentiment
    plt.figure(figsize=(10, 6))
    avg_pnl = df.groupby('classification')['closed_pnl'].mean().reindex(order)
    sns.barplot(x=avg_pnl.index, y=avg_pnl.values, palette="RdYlGn")
    plt.title("Average Closed PnL by Market Sentiment")
    plt.xlabel("Sentiment")
    plt.ylabel("Avg Closed PnL (USD)")
    plt.tight_layout()
    plt.savefig(os.path.join(PLOTS_PATH, "pnl_vs_sentiment.png"))
    plt.close()
    print("✅ Saved pnl_vs_sentiment.png")

    # 2. Win Rate vs Sentiment
    plt.figure(figsize=(10, 6))
    win_rate = df.groupby('classification')['is_win'].mean() * 100
    win_rate = win_rate.reindex(order)
    sns.barplot(x=win_rate.index, y=win_rate.values, palette="RdYlGn")
    plt.title("Win Rate by Market Sentiment")
    plt.xlabel("Sentiment")
    plt.ylabel("Win Rate (%)")
    plt.tight_layout()
    plt.savefig(os.path.join(PLOTS_PATH, "winrate_vs_sentiment.png"))
    plt.close()
    print("✅ Saved winrate_vs_sentiment.png")

    # 3. Leverage vs Sentiment
    plt.figure(figsize=(10, 6))
    avg_lev = df.groupby('classification')['leverage_proxy'].mean().reindex(order)
    sns.barplot(x=avg_lev.index, y=avg_lev.values, palette="coolwarm")
    plt.title("Average Leverage by Market Sentiment")
    plt.xlabel("Sentiment")
    plt.ylabel("Avg Leverage Proxy")
    plt.tight_layout()
    plt.savefig(os.path.join(PLOTS_PATH, "leverage_vs_sentiment.png"))
    plt.close()
    print("✅ Saved leverage_vs_sentiment.png")

    # 4. Time Series PnL + Sentiment Overlay
    plt.figure(figsize=(14, 6))
    daily = df.groupby('date')['closed_pnl'].mean().reset_index()
    plt.plot(daily['date'], daily['closed_pnl'], color='steelblue', linewidth=0.8, label='Avg Daily PnL')
    sentiment_daily = df.groupby('date')['market_condition'].first().reset_index()
    for _, row in sentiment_daily.iterrows():
        color = '#90EE90' if row['market_condition'] == 1 else '#FFB6B6'
        plt.axvspan(row['date'], row['date'] + pd.Timedelta(days=1), alpha=0.3, color=color)
    plt.title("Daily Avg PnL Over Time (Green=Greed, Red=Fear)")
    plt.xlabel("Date")
    plt.ylabel("Avg Closed PnL (USD)")
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(PLOTS_PATH, "timeseries_pnl_sentiment.png"))
    plt.close()
    print("✅ Saved timeseries_pnl_sentiment.png")

if __name__ == "__main__":
    create_visualizations()