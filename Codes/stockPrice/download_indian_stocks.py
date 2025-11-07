#!/usr/bin/env python3
"""
Download Indian stock market data for the project
Using NSE (National Stock Exchange) data via Yahoo Finance
"""
import yfinance as yf
import pandas as pd
from datetime import datetime

# Indian stocks to download
# RELIANCE.NS - Reliance Industries (like TSMC in Taiwan)
# TCS.NS - Tata Consultancy Services (like Hon Hai)
stocks = {
    'RELIANCE': 'RELIANCE.NS',
    'TCS': 'TCS.NS'
}

def download_stock_data(symbol, ticker, start_date, end_date, filename):
    """Download stock data and save to CSV"""
    print(f"Downloading {symbol} ({ticker}) from {start_date} to {end_date}...")
    
    # Download data
    data = yf.download(ticker, start=start_date, end=end_date, progress=False)
    
    if data.empty:
        print(f"  ERROR: No data received for {symbol}")
        return False
    
    # Rename columns to match the format used in the project
    data_formatted = pd.DataFrame()
    data_formatted['date'] = data.index.strftime('%Y%m%d')
    data_formatted['open'] = data['Open'].values
    data_formatted['close'] = data['Close'].values
    data_formatted['high'] = data['High'].values
    data_formatted['low'] = data['Low'].values
    data_formatted['volumeP'] = data['Volume'].values
    
    # Save to CSV
    data_formatted.to_csv(filename, index=False)
    print(f"  Saved {len(data_formatted)} records to {filename}")
    return True

# Create data directory if it doesn't exist
import os
os.makedirs('data', exist_ok=True)

print("="*60)
print("Downloading Indian Stock Market Data")
print("="*60)
print()

# Download training data (2015-2019)
for symbol, ticker in stocks.items():
    print(f"\n{symbol}:")
    # Training data: 2015-2019
    success = download_stock_data(
        symbol, ticker,
        '2015-01-01', '2019-12-31',
        f'data/{symbol}_2015_2019_ochlv.csv'
    )
    
    if success:
        # Test data: Jan-Mar 2020
        download_stock_data(
            symbol, ticker,
            '2020-01-01', '2020-03-31',
            f'data/{symbol}_202001_03_ochlv.csv'
        )

print()
print("="*60)
print("Download Complete!")
print("="*60)
print()
print("Available stocks:")
print("  - RELIANCE: Reliance Industries Limited (India's largest company)")
print("  - TCS: Tata Consultancy Services (India's largest IT services)")
print()
print("Data files created:")
print("  - RELIANCE_2015_2019_ochlv.csv (training)")
print("  - RELIANCE_202001_03_ochlv.csv (testing)")
print("  - TCS_2015_2019_ochlv.csv (training)")
print("  - TCS_202001_03_ochlv.csv (testing)")
print()
