import pandas as pd
import pytest
import talib
import numpy as np

def test_sma_calculation():
    """Test SMA calculation for AAPL."""
    df = pd.read_csv("Data/processed/stock_indicators.csv")
    aapl_data = df[df['Stock'] == 'AAPL']
    assert not aapl_data.empty, "No AAPL data in stock_indicators.csv"
    
    sma = talib.SMA(aapl_data['Close'], timeperiod=20)
    assert len(sma) == len(aapl_data), "SMA length does not match data length"
    assert not sma.isna().all(), "SMA contains only NaN values"
    np.testing.assert_allclose(sma, aapl_data['SMA_20'], rtol=1e-5, equal_nan=True, err_msg="SMA calculation mismatch")

def test_rsi_calculation():
    """Test RSI calculation for AAPL."""
    df = pd.read_csv("Data/processed/stock_indicators.csv")
    aapl_data = df[df['Stock'] == 'AAPL']
    assert not aapl_data.empty, "No AAPL data in stock_indicators.csv"
    
    rsi = talib.RSI(aapl_data['Close'], timeperiod=14)
    assert len(rsi) == len(aapl_data), "RSI length does not match data length"
    assert not rsi.isna().all(), "RSI contains only NaN values"
    np.testing.assert_allclose(rsi, aapl_data['RSI'], rtol=1e-5, equal_nan=True, err_msg="RSI calculation mismatch")