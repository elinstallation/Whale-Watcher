import pandas as pd


df = pd.read_csv("stock_prices_daily.csv")

def spot_absorption(company_name):
    df_new = df[df["Ticker"] == company_name][["Volume", "High", "Low", "Close"]].copy()

    df_new["vol_mean"] = df_new["Volume"].rolling(window=30).mean()
    df_new["vol_std"] = df_new["Volume"].rolling(window=30).std()
    df_new["z_score"] = (df_new["Volume"]-df_new["vol_mean"])/df_new["vol_std"]
    df_new.dropna(inplace=True)

    df_new["range_pct"] = (df_new["High"] - df_new["Low"]) / df_new["Close"]
    df_new["avg_range"] = df_new["range_pct"].rolling(window=30).mean()

    df_new["whale"] = (df_new["z_score"] > 2) & (df_new["range_pct"] < df_new["avg_range"])

    return df_new

