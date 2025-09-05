import pandas as pd
from textblob import TextBlob

# Load raw news and stock data
news_df = pd.read_csv("Data/raw/raw_analyst_ratings.csv")
stock_df = pd.read_csv("Data/processed/stock_prices.csv")  # or merge individual stock CSVs

# Ensure Date columns are datetime
news_df['date'] = pd.to_datetime(news_df['date'], utc=True).dt.tz_convert('UTC-04:00')
stock_df['Date'] = pd.to_datetime(stock_df['Date'])

# Rename news date column to match stock data
news_df.rename(columns={'date': 'Date'}, inplace=True)

# Merge on Date and stock
merged_df = pd.merge(news_df, stock_df, on=['Date', 'stock'], how='inner')

# Compute sentiment
merged_df['sentiment'] = merged_df['headline'].apply(lambda x: TextBlob(str(x)).sentiment.polarity)

# Compute daily returns
merged_df['daily_return'] = merged_df.groupby('stock')['Close'].pct_change() * 100

# Save to processed folder
merged_df.to_csv("Data/processed/news_stock_merged.csv", index=False)
print("Generated Data/processed/news_stock_merged.csv")