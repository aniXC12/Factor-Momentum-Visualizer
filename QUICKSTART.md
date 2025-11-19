# ⚡ Quick Start Guide

Get started with Factor Momentum Visualizer in 5 minutes!

---

## 🚀 Installation (2 minutes)

### Option 1: Quick Start Script

**Linux/Mac:**
```bash
./run.sh
```

**Windows:**
```batch
run.bat
```

### Option 2: Manual Installation

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run the app
streamlit run app.py
```

The app will open automatically in your browser at `http://localhost:8501`

---

## 🎯 Your First Analysis (3 minutes)

### Step 1: Configure Settings (1 min)

Open the **sidebar** (left side) and select:

1. **Universe**: Choose "S&P 500 (Top 50)"
2. **Factors**: Select "Momentum" and "Value"
3. **Date Range**: Keep default (last 3 years)

### Step 2: Run Analysis (1 min)

Click the big **"🚀 Run Analysis"** button!

The app will:
- Download stock data (takes ~30 seconds)
- Calculate factor scores
- Construct portfolios
- Run backtests

### Step 3: Explore Results (1 min)

Scroll through to see:

#### Performance Metrics
Quick overview of returns, Sharpe ratio, drawdowns

#### Charts
- **Cumulative Returns**: How strategies performed over time
- **Rolling Sharpe**: Risk-adjusted performance
- **Drawdowns**: Worst periods
- **Correlations**: How factors relate

#### Download
Export your results as CSV files

---

## 💡 Tips for Better Results

### Choose Good Universes

✅ **Good:**
- S&P 500 (Top 50) - Large, liquid stocks
- Custom tickers - Your own selection

❌ **Avoid:**
- Too many tickers (>100) - Slow performance
- Penny stocks - Poor data quality
- Too short date range (<1 year) - Unreliable

### Factor Selection

**Try these combinations:**

🔥 **Classic Long-Short**
```
Factors: Momentum, Value
Period: 3 years
Rebalance: Monthly
```

📊 **Quality Focus**
```
Factors: Quality, Value
Period: 5 years
Rebalance: Quarterly
```

🚀 **Multi-Factor**
```
Factors: Momentum, Value, Size, Quality
Period: 3 years
Rebalance: Monthly
```

---

## 📊 Example Workflow

### Analyze Tech Stocks

1. Select **"Custom Tickers"**
2. Enter:
   ```
   AAPL,MSFT,GOOGL,AMZN,META,NVDA,TSLA,AMD,INTC,ORCL
   ```
3. Select **"Momentum"** factor
4. Choose **last 2 years**
5. Click **"Run Analysis"**

### Upload Your Portfolio

1. Create CSV file `my_stocks.csv`:
   ```csv
   ticker
   AAPL
   MSFT
   GOOGL
   ```
2. Select **"Upload CSV"**
3. Upload your file
4. Select factors
5. Run!

---

## 🐛 Troubleshooting

### "No data fetched"
**Fix:** 
- Check internet connection
- Verify ticker symbols are correct
- Try different date range

### Slow performance
**Fix:**
- Use fewer tickers (20-50 is ideal)
- Shorter date range
- Select fewer factors

### "Module not found"
**Fix:**
```bash
pip install -r requirements.txt
```

---

## 📚 What Next?

### Learn More
- Read the full [README.md](README.md)
- Check [DEPLOYMENT.md](DEPLOYMENT.md) for hosting
- Review factor methodology in docs

### Try Advanced Features
- Upload your own CSV
- Adjust rebalancing frequency
- Compare multiple factors
- Export and analyze results

### Contribute
- Found a bug? Open an issue
- Have an idea? Suggest a feature
- Want to help? Read [CONTRIBUTING.md](CONTRIBUTING.md)

---

## 🎓 Understanding Results

### Key Metrics Explained

**Total Return**
- Total % gain/loss over period
- Higher is better

**Sharpe Ratio**
- Risk-adjusted returns
- \> 1 is good, > 2 is excellent

**Max Drawdown**
- Worst peak-to-trough decline
- Lower (less negative) is better

**Win Rate**
- % of profitable days
- 50-60% is typical for good strategies

---

## 💾 Saving Your Work

### Export Options

1. **Factor Scores CSV**
   - Raw factor calculations
   - Use for further analysis

2. **Performance Metrics CSV**
   - Summary statistics
   - Share with team

3. **Screenshots**
   - Right-click on charts
   - Save as image

---

## 🎯 Common Use Cases

### Portfolio Manager
```
Goal: Compare strategies
Universe: S&P 500 (Top 50)
Factors: All 4
Period: 5 years
```

### Quant Researcher
```
Goal: Test factor predictability
Universe: Custom tickers
Factors: One at a time
Period: Maximum available
```

### Student Learning
```
Goal: Understand factors
Universe: S&P 500 (Top 50)
Factors: Start with Momentum
Period: 3 years
```

---

## 📞 Get Help

- **Documentation**: Check README.md
- **Issues**: Search existing issues on GitHub
- **Questions**: Open a discussion
- **Bugs**: Report with details

---

## ✅ Checklist

Before running your first analysis:

- [ ] App is running (`http://localhost:8501`)
- [ ] Internet connection working
- [ ] Sidebar settings configured
- [ ] Factors selected
- [ ] Date range chosen

Ready? Click **"🚀 Run Analysis"**!

---

**Happy analyzing! 📊🚀**

For more details, see the [full README](README.md).
