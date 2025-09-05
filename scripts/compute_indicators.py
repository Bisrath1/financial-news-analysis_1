import pandas as pd
import talib

# Load stock data
df = pd.read_csv("Data/processed/stock_indicators.csv")

# Ensure data is sorted by Stock and Date
df = df.sort_values(by=['Stock', 'Date'])

# Initialize columns
df['SMA_20'] = pd.NA
df['RSI'] = pd.NA
df['MACD'] = pd.NA
df['Signal'] = pd.NA
df['MACD_Hist'] = pd.NA

# Compute indicators for each stock
for stock in df['Stock'].unique():
    stock_data = df[df['Stock'] == stock].copy()
    df.loc[df['Stock'] == stock, 'SMA_20'] = talib.SMA(stock_data['Close'], timeperiod=20)
    df.loc[df['Stock'] == stock, 'RSI'] = talib.RSI(stock_data['Close'], timeperiod=14)
    macd, signal, hist = talib.MACD(stock_data['Close'], fastperiod=12, slowperiod=26, signalperiod=9)
    df.loc[df['Stock'] == stock, 'MACD'] = macd
    df.loc[df['Stock'] == stock, 'Signal'] = signal
    df.loc[df['Stock'] == stock, 'MACD_Hist'] = hist

# Save updated CSV
df.to_csv("Data/processed/stock_indicators.csv", index=False)
print("Updated Data/processed/stock_indicators.csv with indicators")