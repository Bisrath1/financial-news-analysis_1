import pandas as pd
import pytest

def test_news_stock_data_loading():
    """Test loading of news_stock_merged.csv."""
    df = pd.read_csv("Data/processed/news_stock_merged.csv")
    assert not df.empty, "news_stock_merged.csv is empty"
    assert 'Date' in df.columns, "Missing 'Date' column in news_stock_merged.csv"
    assert 'Stock' in df.columns, "Missing 'Stock' column in news_stock_merged.csv"
    assert 'Sentiment' in df.columns, "Missing 'Sentiment' column in news_stock_merged.csv"
    assert 'Daily_Return' in df.columns, "Missing 'Daily_Return' column in news_stock_merged.csv"
    assert 'headline' in df.columns, "Missing 'headline' column in news_stock_merged.csv"
    assert 'Open' in df.columns, "Missing 'Open' column in news_stock_merged.csv"
    assert 'High' in df.columns, "Missing 'High' column in news_stock_merged.csv"
    assert 'Low' in df.columns, "Missing 'Low' column in news_stock_merged.csv"
    assert 'Close' in df.columns, "Missing 'Close' column in news_stock_merged.csv"

def test_stock_indicators_loading():
    """Test loading of stock_indicators.csv."""
    df = pd.read_csv("Data/processed/stock_indicators.csv")
    assert not df.empty, "stock_indicators.csv is empty"
    assert 'Date' in df.columns, "Missing 'Date' column in stock_indicators.csv"
    assert 'Stock' in df.columns, "Missing 'Stock' column in stock_indicators.csv"
    assert 'SMA_20' in df.columns, "Missing 'SMA_20' column in stock_indicators.csv"
    assert 'RSI' in df.columns, "Missing 'RSI' column in stock_indicators.csv"
    assert 'MACD' in df.columns, "Missing 'MACD' column in stock_indicators.csv"
    assert 'Signal' in df.columns, "Missing 'Signal' column in stock_indicators.csv"