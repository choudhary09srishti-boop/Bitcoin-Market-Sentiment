# Bitcoin Market Sentiment Analysis

## Objective
Explore the relationship between Bitcoin market sentiment (Fear & Greed Index)
and trader performance on Hyperliquid. Uncover hidden patterns and deliver
actionable trading strategy insights.

---

## Datasets
| Dataset | Source | Rows |
|---|---|---|
| Historical Trader Data | Hyperliquid | 211,224 |
| Fear & Greed Index | Alternative.me | 2,644 |

**Date Range Analyzed:** May 2023 → May 2025  
**Trades after cleaning & merge:** 207,327

---

## Project Structure
bitcoin-sentiment-analysis/
├── data/
│   ├── raw/                  # Original CSV files
│   └── processed/            # Cleaned & merged data
├── src/
│   ├── data_loader.py        # Load raw datasets
│   ├── data_cleaning.py      # Clean, merge datasets
│   ├── feature_engineering.py# Create analytical features
│   ├── analysis.py           # EDA & pattern discovery
│   └── visualization.py      # Generate charts
├── outputs/
│   ├── plots/                # 4 generated charts
│   └── report/               # Final insights text
├── requirements.txt
└── .env
---

## Setup & Run

```bash
# 1. Clone the repo
git clone https://github.com/choudhary09srishti-boop/Bitcoin-Market-Sentiment.git
cd Bitcoin-Market-Sentiment

# 2. Create virtual environment
python -m venv venv
venv\Scripts\Activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run pipeline in order
python src/data_loader.py
python src/data_cleaning.py
python src/feature_engineering.py
python src/analysis.py
python src/visualization.py
```

---

## Key Findings

### 1. Performance by Sentiment
| Sentiment | Avg PnL (USD) | Win Rate |
|---|---|---|
| Extreme Greed | $66.11 | 46.24% |
| Fear | $53.50 | 41.98% |
| Greed | $42.43 | 38.81% |
| Neutral | $31.43 | 39.62% |
| Extreme Fear | $31.27 | 36.90% |

**Traders earn 111% more during Extreme Greed vs Extreme Fear.**

### 2. Leverage Behavior
- Traders use **2.2x more leverage** during Greed vs Fear
- Extreme Greed → avg leverage proxy: 953.50
- Extreme Fear → avg leverage proxy: 430.18

### 3. Hidden Pattern
- High leverage during **Fear → $115.25 avg PnL**
- High leverage during **Greed → $105.09 avg PnL**
- Experienced traders selectively use high leverage during Fear
  when assets are undervalued.

### 4. Top Performing Coins
| Coin | Avg PnL |
|---|---|
| @109 | $270.70 |
| AVAX | $239.10 |
| SOL | $153.36 |
| ETH | $172.09 |

### 5. Coin + Sentiment Insight
- **ETH** performs best during Fear ($236.86 avg PnL)
- **@107** crashes during Extreme Fear (-$89.59 avg PnL)
- **SOL** best during Greed ($284.80 avg PnL)

---

## Strategy Recommendations
1. **Best time to trade** → Greed or Extreme Greed phases
2. **Leverage control** → Keep leverage low during Extreme Fear
3. **Opportunistic play** → High leverage selectively during Fear
4. **Avoid** → High frequency trading during Extreme Fear (36.90% win rate)
5. **Coin selection** → Trade ETH during Fear, SOL during Greed

---

## Tech Stack
- Python, Pandas, NumPy
- Matplotlib, Seaborn
- python-dotenv, Jupyter

---

## Author
Srishti Choudhary  
[GitHub](https://github.com/choudhary09srishti-boop/Bitcoin-Market-Sentiment)
