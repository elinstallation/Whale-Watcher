# Whale Watcher

A quantitative tool that detects potential institutional accumulation ("whale" activity) in US equities using Effort vs. Result analysis — inspired by Wyckoff methodology.

## How It Works

It flags days where:
- **Volume Z-score > 2** — unusually high volume relative to the 30-day rolling average
- **Daily price range is tight** — below the 30-day average range

This combination suggests large players are absorbing supply without moving price, a classic institutional footprint.

## Features

- Rolling 30-day volume Z-score calculation
- Price range normalization as a proxy for directional effort
- Interactive scatter plot dashboard built with Matplotlib
- Search any US stock ticker to instantly re-plot

## Setup

**1. Install dependencies**
```bash
pip install pandas matplotlib kagglehub
```

**2. Download the dataset**

Run `kaggle_api.py` to download the [US Stock Market Historical OHLCV dataset](https://www.kaggle.com/datasets/asadullahcreative/us-stock-market-historical-ohlcv-dataset) from Kaggle. You'll need a Kaggle account.

```bash
python kaggle_api.py
```

Place the downloaded CSV in the project root as `stock_prices_daily.csv`.

**3. Run the dashboard**
```bash
python dashboard.py
```

## Usage

The dashboard opens with AAPL loaded by default. Type any ticker symbol into the search box and press Enter to load a new stock.

- **Gray dots** — normal trading days
- **Blue dots** — potential whale accumulation days
- **Red dashed line** — high volume threshold (Z-score = 2)
