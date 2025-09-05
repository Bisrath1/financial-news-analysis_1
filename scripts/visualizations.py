import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px
import os

# Ensure output directory exists
os.makedirs("notebooks/plots", exist_ok=True)

# Load data
try:
    news_stock_df = pd.read_csv("Data/processed/news_stock_merged.csv")
    indicators_df = pd.read_csv("Data/processed/stock_indicators.csv")
except FileNotFoundError as e:
    print(f"Error: {e}. Ensure 'Data/processed/news_stock_merged.csv' and 'Data/processed/stock_indicators.csv' exist.")
    exit(1)

# Check required columns
required_news_cols = ['Date', 'stock', 'Open', 'High', 'Low', 'Close', 'sentiment', 'daily_return', 'headline']
required_indicators_cols = ['Date', 'stock', 'SMA_20', 'RSI', 'MACD', 'Signal']
missing_news_cols = [col for col in required_news_cols if col not in news_stock_df.columns]
missing_indicators_cols = [col for col in required_indicators_cols if col not in indicators_df.columns]

if missing_news_cols or missing_indicators_cols:
    print(f"Missing columns in news_stock_merged.csv: {missing_news_cols}")
    print(f"Missing columns in stock_indicators.csv: {missing_indicators_cols}")
    exit(1)

# Convert Date columns to datetime
news_stock_df['Date'] = pd.to_datetime(news_stock_df['Date'])
indicators_df['Date'] = pd.to_datetime(indicators_df['Date'])

# Visualization 1: Candlestick Chart with SMA, RSI, MACD
def plot_stock_indicators(stock_symbol='AAPL'):
    stock_data = news_stock_df[news_stock_df['stock'] == stock_symbol]
    indicator_data = indicators_df[indicators_df['stock'] == stock_symbol]
    
    if stock_data.empty or indicator_data.empty:
        print(f"No data for {stock_symbol}. Skipping plot.")
        return
    
    fig = make_subplots(rows=3, cols=1, shared_xaxes=True, vertical_spacing=0.1,
                        subplot_titles=[f"{stock_symbol} Stock Price", "RSI", "MACD"],
                        row_heights=[0.5, 0.2, 0.3])
    
    # Candlestick
    fig.add_trace(go.Candlestick(
        x=stock_data['Date'], open=stock_data['Open'], high=stock_data['High'],
        low=stock_data['Low'], close=stock_data['Close'], name="OHLC"), row=1, col=1)
    
    # SMA
    fig.add_trace(go.Scatter(
        x=indicator_data['Date'], y=indicator_data['SMA_20'], line=dict(color='blue'), name='SMA 20'), row=1, col=1)
    
    # RSI
    fig.add_trace(go.Scatter(
        x=indicator_data['Date'], y=indicator_data['RSI'], line=dict(color='purple'), name='RSI'), row=2, col=1)
    
    # MACD and Signal
    fig.add_trace(go.Scatter(
        x=indicator_data['Date'], y=indicator_data['MACD'], line=dict(color='green'), name='MACD'), row=3, col=1)
    fig.add_trace(go.Scatter(
        x=indicator_data['Date'], y=indicator_data['Signal'], line=dict(color='orange'), name='Signal'), row=3, col=1)
    
    fig.update_layout(
        title=f"{stock_symbol} Stock Analysis with Technical Indicators",
        yaxis_title="Price (USD)", height=800, showlegend=True, template="plotly_dark"
    )
    fig.write_html(f"notebooks/plots/{stock_symbol}_indicators.html")
    fig.write_png(f"notebooks/plots/{stock_symbol}_indicators.png")
    print(f"Generated plot for {stock_symbol}")

# Visualization 2: Sentiment vs. Stock Returns Scatter
def plot_sentiment_vs_returns():
    fig = px.scatter(
        news_stock_df, x='sentiment', y='daily_return', color='stock',
        hover_data=['Date', 'headline'], size_max=10,
        title="News Sentiment vs. Daily Stock Returns"
    )
    fig.update_layout(template="plotly_dark")
    fig.write_html("notebooks/plots/sentiment_vs_returns.html")
    fig.write_png("notebooks/plots/sentiment_vs_returns.png")
    print("Generated sentiment vs. returns plot")

# Visualization 3: Correlation Heatmap
def plot_correlation_heatmap():
    pivot_df = news_stock_df.pivot_table(
        values=['sentiment', 'daily_return'], index='Date', columns='stock'
    )
    correlation_matrix = pivot_df.corr()
    
    fig = px.imshow(
        correlation_matrix, text_auto=True, aspect="auto",
        title="Correlation Between Sentiment and Stock Returns",
        color_continuous_scale="RdBu"
    )
    fig.update_layout(template="plotly_dark")
    fig.write_html("notebooks/plots/correlation_heatmap.html")
    fig.write_png("notebooks/plots/correlation_heatmap.png")
    print("Generated correlation heatmap")

# Visualization 4: Publication Trends
def plot_publication_trends():
    publication_counts = news_stock_df.groupby(news_stock_df['Date'].dt.date).size().reset_index(name='count')
    fig = px.line(
        publication_counts, x='Date', y='count',
        title="Daily News Publication Frequency",
        labels={'count': 'Number of Articles', 'Date': 'Date'}
    )
    fig.update_layout(template="plotly_dark")
    fig.write_html("notebooks/plots/publication_trends.html")
    fig.write_png("notebooks/plots/publication_trends.png")
    print("Generated publication trends plot")

# Run visualizations
plot_stock_indicators('AAPL')  # Add more stocks if needed (e.g., 'MSFT', 'GOOG')
plot_sentiment_vs_returns()
plot_correlation_heatmap()
plot_publication_trends()