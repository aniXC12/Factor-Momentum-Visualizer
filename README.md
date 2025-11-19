# 📊 Factor Momentum Visualizer

A **production-grade quantitative research platform** for equity factor analysis, portfolio construction, and backtesting. Built with modern Python stack and designed to replicate workflows used at quantitative hedge funds.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.29.0-red.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

---

## 🎯 Overview

Factor Momentum Visualizer is an end-to-end quantitative research tool that demonstrates a real research workflow used in professional quant finance. It enables you to:

- **Analyze multiple equity factors** (Momentum, Value, Size, Quality)
- **Construct long-short portfolios** based on quantile rankings
- **Backtest strategies** with realistic rebalancing
- **Visualize performance** with interactive, research-grade charts
- **Export results** for further analysis

---

## ✨ Key Features

### 📈 **Data Acquisition**
- Download historical OHLCV data via `yfinance`
- Support for S&P 500, Russell 1000, or custom ticker lists
- CSV upload functionality
- Automated data cleaning and alignment

### 🧮 **Factor Engineering**
Compute standard equity factors:
- **Momentum**: 12-month returns minus last month (classic academic definition)
- **Value**: Price-to-Book or Price-to-Earnings ratios
- **Size**: Market capitalization (Small Minus Big)
- **Quality**: Profitability metrics (ROE, ROA, margins)

### 💼 **Portfolio Construction**
- Long-short portfolios based on factor rankings
- Customizable percentiles (default: top 20% long, bottom 20% short)
- Equal-weighted positions
- Monthly or quarterly rebalancing

### 📊 **Backtesting Engine**
Calculate comprehensive metrics:
- Cumulative returns
- Sharpe ratio & Sortino ratio
- Maximum drawdown
- Calmar ratio
- Win rate & profit factor
- Rolling Sharpe ratios

### 📉 **Interactive Visualizations**
- Cumulative performance charts
- Drawdown analysis
- Correlation heatmaps
- Factor scatter plots (predictive power)
- Rolling metrics

### 💾 **Data Export**
- Download factor scores as CSV
- Export performance metrics
- Generate summary reports

---

## 🚀 Quick Start

### **Installation**

1. **Clone or download this repository**
```bash
git clone <repository-url>
cd factor_momentum_visualizer
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the application**
```bash
streamlit run app.py
```

4. **Open your browser**
The app will automatically open at `http://localhost:8501`

---

## 📖 Usage Guide

### **Step 1: Select Universe**
Choose your data source:
- **S&P 500 (Top 50)**: Large-cap US equities
- **Russell 1000 (Top 50)**: Broader market coverage
- **Custom Tickers**: Enter your own comma-separated list
- **Upload CSV**: Upload a file with a 'ticker' column

### **Step 2: Select Factors**
Pick one or more factors to analyze:
- Momentum
- Value
- Size
- Quality

### **Step 3: Configure Settings**
- **Date Range**: Select backtest period
- **Rebalancing Frequency**: Monthly or Quarterly
- **Portfolio Percentiles**: Adjust long/short thresholds
- **Benchmark**: Include SPY comparison (optional)

### **Step 4: Run Analysis**
Click the **"🚀 Run Analysis"** button and explore:
- Performance metrics
- Cumulative return charts
- Drawdown analysis
- Factor correlations
- Predictive power scatter plots

### **Step 5: Download Results**
Export your analysis:
- Factor scores CSV
- Performance metrics CSV

---

## 🏗️ Project Structure

```
factor_momentum_visualizer/
├── app.py                          # Main Streamlit application
├── requirements.txt                # Python dependencies
├── README.md                       # This file
│
├── data/
│   ├── __init__.py
│   └── data_fetcher.py            # Data acquisition module
│
├── factors/
│   ├── __init__.py
│   └── factor_calculator.py       # Factor computation
│
├── backtest/
│   ├── __init__.py
│   └── backtester.py              # Portfolio construction & backtesting
│
├── plots/
│   ├── __init__.py
│   └── visualizations.py          # Interactive Plotly charts
│
└── utils/
    ├── __init__.py
    └── helpers.py                 # Utility functions
```

---

## 📚 Factor Methodology

### **Momentum Factor**
- **Definition**: 12-month cumulative return minus most recent 1-month return
- **Academic Basis**: Jegadeesh & Titman (1993)
- **Signal**: Positive momentum → Buy, Negative momentum → Sell

### **Value Factor**
- **Definition**: Inverse of Price-to-Book (or Price-to-Earnings) ratio
- **Academic Basis**: Fama & French (1992)
- **Signal**: Lower valuation multiples → Higher expected returns

### **Size Factor**
- **Definition**: Inverse of market capitalization (log scale)
- **Academic Basis**: Fama & French (1992), "Small Minus Big"
- **Signal**: Smaller companies → Higher risk-adjusted returns

### **Quality Factor**
- **Definition**: Profitability metrics (ROE, ROA, profit margins)
- **Academic Basis**: Novy-Marx (2013), Asness et al. (2018)
- **Signal**: Higher profitability → More persistent returns

---

## 📊 Performance Metrics

The tool calculates the following metrics:

| Metric | Description |
|--------|-------------|
| **Total Return** | Cumulative return over backtest period |
| **Annualized Return** | CAGR (Compound Annual Growth Rate) |
| **Annualized Volatility** | Standard deviation of returns (annualized) |
| **Sharpe Ratio** | Risk-adjusted return (assuming 0% risk-free rate) |
| **Sortino Ratio** | Return relative to downside deviation |
| **Max Drawdown** | Largest peak-to-trough decline |
| **Calmar Ratio** | Return divided by maximum drawdown |
| **Win Rate** | Percentage of positive return days |
| **Profit Factor** | Gross profits / Gross losses |

---

## 🎨 Screenshots

### Main Dashboard
![Dashboard](https://via.placeholder.com/800x400?text=Dashboard+Screenshot)

### Performance Analysis
![Performance](https://via.placeholder.com/800x400?text=Performance+Chart)

### Factor Correlation
![Correlation](https://via.placeholder.com/800x400?text=Correlation+Heatmap)

---

## 🛠️ Advanced Features (Optional Enhancements)

The codebase is designed to be extensible. Consider adding:

- **Multi-factor composite scores**: Combine multiple factors
- **PCA factor decomposition**: Identify principal components
- **Fama-French comparison**: Compare against academic benchmarks
- **Regime detection**: Identify market regimes (bull/bear)
- **Transaction cost modeling**: More realistic backtests
- **Risk parity allocation**: Alternative weighting schemes

---

## 🌐 Deployment

### **Deploy to Streamlit Cloud**

1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your repository
4. Deploy!

### **Deploy to Heroku**

```bash
# Create Procfile
echo "web: streamlit run app.py --server.port $PORT" > Procfile

# Deploy
heroku create your-app-name
git push heroku main
```

### **Deploy to HuggingFace Spaces**

1. Create a new Space at [huggingface.co/spaces](https://huggingface.co/spaces)
2. Select "Streamlit" as the SDK
3. Push your code to the Space repository

---

## 📝 Example Queries

Try these example analyses:

```python
# Compare Momentum vs Value
Factors: ["Momentum", "Value"]
Universe: S&P 500 (Top 50)
Period: 2020-01-01 to 2024-12-31
Rebalance: Monthly

# Quality factor deep dive
Factors: ["Quality"]
Universe: Russell 1000 (Top 50)
Period: 2018-01-01 to 2024-12-31
Rebalance: Quarterly

# Multi-factor analysis
Factors: ["Momentum", "Value", "Size", "Quality"]
Universe: Custom (upload tech_stocks.csv)
Period: 2019-01-01 to 2024-12-31
Rebalance: Monthly
```

---

## 🐛 Troubleshooting

### **Issue: "No data fetched"**
- Check your internet connection
- Verify ticker symbols are valid
- Try a different date range
- Some tickers may not have historical data for the selected period

### **Issue: "Missing fundamental data"**
- yfinance doesn't always have fundamentals for all stocks
- The tool will fall back to synthetic factors based on price data
- Consider using a smaller, higher-quality universe

### **Issue: "Slow performance"**
- Reduce the number of tickers (use Top 50 instead of full universe)
- Shorten the date range
- Select fewer factors

---

## 📚 References

### Academic Papers
- Jegadeesh, N., & Titman, S. (1993). "Returns to Buying Winners and Selling Losers"
- Fama, E., & French, K. (1992). "The Cross-Section of Expected Stock Returns"
- Novy-Marx, R. (2013). "The Other Side of Value: The Gross Profitability Premium"
- Asness, C., Frazzini, A., & Pedersen, L. (2018). "Quality Minus Junk"

### Documentation
- [Streamlit Documentation](https://docs.streamlit.io)
- [yfinance Documentation](https://pypi.org/project/yfinance/)
- [Plotly Documentation](https://plotly.com/python/)

---

## ⚖️ License

MIT License - see LICENSE file for details

---

## ⚠️ Disclaimer

**This tool is for educational and research purposes only.**

- Not financial advice
- Past performance does not guarantee future results
- Trading involves risk of loss
- Always do your own research
- Consult a financial advisor before making investment decisions

---

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest features
- Submit pull requests
- Improve documentation

---

## 📧 Contact

For questions or feedback, please open an issue on GitHub.

---

## 🎓 Learning Resources

Want to learn more about quantitative finance?

- **Books**:
  - "Quantitative Trading" by Ernest Chan
  - "Advances in Financial Machine Learning" by Marcos López de Prado
  - "Active Portfolio Management" by Grinold & Kahn

- **Courses**:
  - [Quantopian Lectures](https://www.quantopian.com/lectures)
  - [Coursera: Investment Management Specialization](https://www.coursera.org/specializations/investment-management)

- **Communities**:
  - r/algotrading
  - QuantConnect Forums
  - Quantopian Community

---

**Built with ❤️ for Quantitative Research**

*Happy Backtesting! 🚀📈*
