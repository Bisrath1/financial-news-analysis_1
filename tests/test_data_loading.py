import pandas as pd
import pytest

def test_news_stock_data_loading():
    """Test loading of news_stock_merged.csv."""
    df = pd.read_csv("Data/processed/news_stock_merged.csv")
    assert not df.empty, "news_stock_merged.csv is empty"
    assert 'date' in df.columns, "Missing 'date' column in news_stock_merged.csv"
    assert 'stock' in df.columns, "Missing 'stock' column in news_stock_merged.csv"
    assert 'headline' in df.columns, "Missing 'headline' column in news_stock_merged.csv"
    assert 'sentiment' in df.columns, "Missing 'sentiment' column in news_stock_merged.csv"
    assert 'daily_return' in df.columns, "Missing 'daily_return' column in news_stock_merged.csv"

def test_stock_indicators_loading():
    """Test loading of stock_indicators.csv."""
    df = pd.read_csv("Data/processed/stock_indicators.csv")
    assert not df.empty, "stock_indicators.csv is empty"
    assert 'date' in df.columns, "Missing 'date' column in stock_indicators.csv"
    assert 'stock' in df.columns, "Missing 'stock' column in stock_indicators.csv"
    assert 'SMA_20' in df.columns, "Missing 'SMA_20' column in stock_indicators.csv"
    assert 'RSI' in df.columns, "Missing 'RSI' column in stock_indicators.csv"
    assert 'MACD' in df.columns, "Missing 'MACD' column in stock_indicators.csv"