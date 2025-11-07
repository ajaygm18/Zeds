# Indian Stock Market Analysis - LSTM Price Prediction

## Overview

This project has been adapted to work with the **Indian Stock Market** (NSE - National Stock Exchange). It uses LSTM (Long Short-Term Memory) neural networks to predict stock prices for major Indian companies.

## Indian Stocks Included

### 1. Reliance Industries Limited (RELIANCE.NS)
- **Market Cap**: India's largest company by market capitalization
- **Sector**: Conglomerate (Oil & Gas, Retail, Telecom)
- **Similar to**: Taiwan's TSMC (2330) in the original project
- **Data**: 2015-2019 training, Jan-Mar 2020 testing

### 2. Tata Consultancy Services (TCS.NS)
- **Market Cap**: India's largest IT services company
- **Sector**: Information Technology
- **Similar to**: Taiwan's Hon Hai (2317) in the original project
- **Data**: 2015-2019 training, Jan-Mar 2020 testing

## Quick Start

### Step 1: Download Indian Stock Data
```bash
cd Codes/stockPrice
python3 download_indian_stocks.py
```

This will download:
- RELIANCE_2015_2019_ochlv.csv (training data)
- RELIANCE_202001_03_ochlv.csv (test data)
- TCS_2015_2019_ochlv.csv (training data)
- TCS_202001_03_ochlv.csv (test data)

### Step 2: Run Prediction
```bash
python3 prediction.py
```

By default, it predicts **Reliance Industries (RELIANCE)** stock prices.

To predict TCS stock, edit `prediction.py` line 8:
```python
stockID = 'TCS'  # Change from 'RELIANCE' to 'TCS'
```

## Latest Execution Results

### Reliance Industries (RELIANCE)
```
Stock: RELIANCE (Reliance Industries Limited)
Training Period: 2015-2019 (1,228 trading days)
Test Period: Jan-Mar 2020 (62 trading days)

Performance Metrics:
- RMSE (Test Set):     13.65 INR
- RMSE (Training Set): 3.46 INR

Model: 2-layer LSTM (32 units → 16 units → 1 output)
Training: 200 epochs completed
```

### Generated Outputs
1. **RELIANCE.csv** - Predicted stock prices for test period
2. **pic1.png** - Test set predictions vs actual (Indian Market)
3. **pic2.png** - Training set predictions vs actual (Indian Market)

## Model Architecture

```
Model: LSTM Neural Network
├── LSTM Layer 1: 32 units (with return sequences)
├── LSTM Layer 2: 16 units
└── Dense Output: 1 unit (predicted price)

Parameters:
- Optimizer: Adam
- Loss: Mean Squared Error (MSE)
- Input: 20 timesteps × 5 features (OCHLV)
- Output: Next day's closing price
```

## Data Format

CSV files contain the following columns:
```
date,open,close,high,low,volumeP
20150101,189.657,189.999,190.877,189.090,2963643
```

All prices are in **Indian Rupees (INR)**.

## Features

- **Real Indian Stock Data**: Downloaded from Yahoo Finance (NSE)
- **No Synthetic Data**: All data is authentic market data
- **Automated Data Download**: Script to fetch latest data
- **Headless Operation**: Matplotlib configured for server environments
- **Visualization**: Beautiful plots of predictions vs actual prices

## Technical Details

### Dependencies
- Python 3.7+
- TensorFlow 2.16+
- Keras (integrated with TensorFlow)
- pandas
- numpy
- scikit-learn
- matplotlib
- yfinance (for data download)

### Model Training
- **Training Period**: 2015-2019 (5 years)
- **Test Period**: Jan-Mar 2020 (3 months)
- **Timesteps**: 20 days (uses 20 previous days to predict next day)
- **Epochs**: 200
- **Batch Size**: 32
- **Features**: 5 (Open, Close, High, Low, Volume)

### Performance
- Training time: ~5-7 minutes on CPU
- Model size: 8,017 parameters (31 KB)
- Inference time: < 1 second for full test set

## Adding More Indian Stocks

To add more stocks, edit `download_indian_stocks.py`:

```python
stocks = {
    'RELIANCE': 'RELIANCE.NS',
    'TCS': 'TCS.NS',
    'INFY': 'INFY.NS',      # Infosys
    'HDFCBANK': 'HDFCBANK.NS',  # HDFC Bank
    'ITC': 'ITC.NS',        # ITC Limited
}
```

Stock symbols must include `.NS` suffix for NSE (National Stock Exchange) or `.BO` for BSE (Bombay Stock Exchange).

## Comparison: Taiwan vs Indian Market

| Aspect | Original (Taiwan) | Updated (Indian) |
|--------|------------------|------------------|
| Exchange | TWSE | NSE |
| Stock 1 | TSMC (2330) | Reliance (RELIANCE.NS) |
| Stock 2 | Hon Hai (2317) | TCS (TCS.NS) |
| Currency | TWD | INR |
| Data Source | Static CSV | Yahoo Finance API |
| Market Cap | Technology focused | Diverse sectors |

## Known Limitations

- **Market Differences**: Indian market may have different volatility patterns than Taiwan market
- **COVID-19 Impact**: Test period (Q1 2020) includes beginning of pandemic, which affected markets globally
- **Data Quality**: Yahoo Finance data may have occasional gaps or adjustments
- **Model Accuracy**: LSTM models work better for short-term predictions; long-term accuracy decreases

## Future Enhancements

- [ ] Add more Indian stocks (Infosys, HDFC Bank, ITC, etc.)
- [ ] Include sentiment analysis for Indian financial news
- [ ] Add technical indicators (RSI, MACD, Bollinger Bands)
- [ ] Implement ensemble methods for better predictions
- [ ] Real-time data streaming from NSE
- [ ] Web interface for easy access

## License

This project is provided for educational and research purposes.

## Disclaimer

⚠️ **Investment Warning**: This project is for educational purposes only. Stock price predictions should not be used as the sole basis for investment decisions. Always consult with financial advisors and conduct thorough research before investing.

## Contact

For questions or issues, please refer to the main repository README.

---

**Note**: This adaptation uses real Indian stock market data from NSE. All predictions are based on historical patterns and should be used with caution in real trading scenarios.
