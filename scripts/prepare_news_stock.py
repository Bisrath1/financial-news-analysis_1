import pandas as pd
from textblob import TextBlob

# Load news data
try:
    news_df = pd.read_csv("Data/raw/raw_analyst_ratings.csv")
except FileNotFoundError:
    print("Error: 'Data/raw/raw_analyst_ratings.csv' not found.")
    exit(1)

# Load stock price data (try stock_prices.csv or combine individual CSVs)
try:
    stock_df = pd.read_csv("Data/processed/stock_prices.csv")
except FileNotFoundError:
    print("stock_prices.csv not found. Combining individual stock CSVs...")
    stock_files = [
        "Data/raw/AAPL_historical_data.csv",
        "Data/raw/AMZN_historical_data.csv",
        "Data/raw/GOOG_historical_data.csv",
        "Data/raw/META_historical_data.csv",
        "Data/raw/MSFT_historical_data.csv",
        "Data/raw/NVDA_historical_data.csv",
        "Data/raw/TSLA_historical_data.csv"
    ]
    stock_df = pd.concat([pd.read_csv(f) for f in stock_files], ignore_index=True)

# Ensure column names are consistent
news_df.rename(columns={'date': 'Date', 'stock': 'Stock'}, inplace=True)
stock_df.rename(columns={'stock': 'Stock'}, inplace=True)

# Convert Date columns to datetime (handle UTC-4 as per challenge)
news_df['Date'] = pd.to_datetime(news_df['Date'], utc=True).dt.tz_convert('UTC-04:00').dt.date
stock_df['Date'] = pd.to_datetime(stock_df['Date']).dt.date

# Merge on Date and Stock
merged_df = pd.merge(news_df, stock_df, on=['Date', 'Stock'], how='inner')

# Compute sentiment
merged_df['Sentiment'] = merged_df['headline'].apply(lambda x: TextBlob(str(x)).sentiment.polarity)

# Compute daily returns
merged_df['Daily_Return'] = merged_df.groupby('Stock')['Close'].pct_change() * 100

# Ensure all required columns are present
required_cols = ['Date', 'Stock', 'headline', 'Sentiment', 'Daily_Return', 'Open', 'High', 'Low', 'Close']
merged_df = merged_df[required_cols]

# Save to processed folder
merged_df.to_csv("Data/processed/news_stock_merged.csv", index=False)
print("Generated Data/processed/news_stock_merged.csv with required columns")