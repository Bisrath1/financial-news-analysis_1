import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px
import os

# Ensure output directory exists
os.makedirs("notebooks/plots", exist_ok=True)

# Load data
news_stock_df = pd.read_csv("Data/news_stock_merged.csv")
indicators_df = pd.read_csv("Data/stock_indicators.csv")

# Convert date columns to datetime
news_stock_df['date'] = pd.to_datetime(news_stock_df['date'])
indicators_df['date'] = pd.to_datetime(indicators_df['date'])

# Visualization 1: Candlestick Chart with SMA, RSI, MACD
def plot_stock_indicators(stock_symbol, stock_df, indicators_df):
    stock_data = stock_df[stock_df['stock'] == stock_symbol]
    indicator_data = indicators_df[indicators_df['stock'] == stock_symbol]
    
    fig = make_subplots(rows=3, cols=1, shared_xaxes=True, 
                        vertical_spacing=0.1, 
                        subplot_titles=[f"{stock_symbol} Stock Price", "RSI", "MACD"],
                        row_heights=[0.5, 0.2, 0.3])
    
    # Candlestick
    fig.add_trace(go.Candlestick(
        x=stock_data['date'],
        open=stock_data['Open'],
        high=stock_data['High'],
        low=stock_data['Low'],
        close=stock_data['Close'],
        name="OHLC"
    ), row=1, col=1)
    
    # SMA
    fig.add_trace(go.Scatter(
        x=indicator_data['date'], y=indicator_data['SMA_20'],
        line=dict(color='blue'), name='SMA 20'
    ), row=1, col=1)
    
    # RSI
    fig.add_trace(go.Scatter(
        x=indicator_data['date'], y=indicator_data['RSI'],
        line=dict(color='purple'), name='RSI'
    ), row=2, col=1)
    
    # MACD
    fig.add_trace(go.Scatter(
        x=indicator_data['date'], y=indicator_data['MACD'],
        line=dict(color='green'), name='MACD'
    ), row=3, col=1)
    fig.add_trace(go.Scatter(
        x=indicator_data['date'], y=indicator_data['Signal'],
        line=dict(color='orange'), name='Signal'
    ), row=3, col=1)
    
    fig.update_layout(
        title=f"{stock_symbol} Stock Analysis with Technical Indicators",
        yaxis_title="Price (USD)",
        height=800, showlegend=True,
        template="plotly_dark"
    )
    fig.write_to_html(f"notebooks/plots/{stock_symbol}_indicators.html")
    fig.write_png(f"notebooks/plots/{stock_symbol}_indicators.png")

# Visualization 2: Sentiment vs. Stock Returns Scatter
def plot_sentiment_vs_returns(news_stock_df):
    fig = px.scatter(
        news_stock_df, x='sentiment', y='daily_return', color='stock',
        hover_data=['date', 'headline'], size_max=10,
        title="News Sentiment vs. Daily Stock Returns"
    )
    fig.update_layout(template="plotly_dark")
    fig.write_to_html("notebooks/plots/sentiment_vs_returns.html")
    fig.write_png("notebooks/plots/sentiment_vs_returns.png")

# Visualization 3: Correlation Heatmap
def plot_correlation_heatmap(news_stock_df):
    pivot_df = news_stock_df.pivot_table(
        values=['sentiment', 'daily_return'], index='date', columns='stock'
    )
    correlation_matrix = pivot_df.corr()
    
    fig = px.imshow(
        correlation_matrix, text_auto=True, aspect="auto",
        title="Correlation Between Sentiment and Stock Returns",
        color_continuous_scale="RdBu"
    )
    fig.update_layout(template="plotly_dark")
    fig.write_to_html("notebooks/plots/correlation_heatmap.html")
    fig.write_png("notebooks/plots/correlation_heatmap.png")

# Visualization 4: Publication Trends
def plot_publication_trends(news_stock_df):
    publication_counts = news_stock_df.groupby(news_stock_df['date'].dt.date).size().reset_index(name='count')
    
    fig = px.line(
        publication_counts, x='date', y='count',
        title="Daily News Publication Frequency",
        labels={'count': 'Number of Articles', 'date': 'Date'}
    )
    fig.update_layout(template="plotly_dark")
    fig.write_to_html("notebooks/plots/publication_trends.html")
    fig.write_png("notebooks/plots/publication_trends.png")

# Run visualizations for a sample stock (e.g., AAPL)
plot_stock_indicators('AAPL', news_stock_df, indicators_df)
plot_sentiment_vs_returns(news_stock_df)
plot_correlation_heatmap(news_stock_df)
plot_publication_trends(news_stock_df)