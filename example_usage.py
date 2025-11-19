"""
Example Usage Script
Demonstrates how to use the Factor Momentum Visualizer components programmatically.
"""

from datetime import datetime, timedelta
import pandas as pd

# Import components
from utils.data_loader import DataLoader
from factors.momentum import MomentumFactor
from factors.value import ValueFactor
from factors.size import SizeFactor
from factors.quality import QualityFactor
from backtest.engine import FactorBacktest
from plots.visualizations import FactorVisualizer


def example_momentum_analysis():
    """
    Example: Run a momentum factor analysis on a custom set of tickers.
    """
    print("=" * 80)
    print("EXAMPLE 1: Momentum Factor Analysis")
    print("=" * 80)
    
    # Define parameters
    tickers = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'META', 'NVDA', 'TSLA', 'JPM', 'V', 'WMT']
    end_date = datetime.now()
    start_date = end_date - timedelta(days=2*365)  # 2 years
    
    print(f"\nAnalyzing {len(tickers)} stocks from {start_date.date()} to {end_date.date()}")
    
    # Load data
    print("\n1. Loading data...")
    loader = DataLoader(start_date.strftime('%Y-%m-%d'), end_date.strftime('%Y-%m-%d'))
    price_data = loader.fetch_price_data(tickers)
    print(f"   Loaded {len(price_data.columns)} stocks with {len(price_data)} days of data")
    
    # Calculate momentum
    print("\n2. Calculating momentum scores...")
    momentum = MomentumFactor(lookback_months=12, skip_months=1)
    momentum_scores = momentum.calculate(price_data)
    print(f"   Calculated momentum for {momentum_scores.shape[1]} stocks")
    
    # Get latest scores
    latest_date = momentum_scores.dropna(how='all').index[-1]
    latest_scores = momentum_scores.loc[latest_date].dropna().sort_values(ascending=False)
    
    print(f"\n3. Latest momentum scores ({latest_date.date()}):")
    print("\n   Top 3 (Strongest Momentum):")
    for ticker, score in latest_scores.head(3).items():
        print(f"   - {ticker}: {score:.4f}")
    
    print("\n   Bottom 3 (Weakest Momentum):")
    for ticker, score in latest_scores.tail(3).items():
        print(f"   - {ticker}: {score:.4f}")
    
    # Run backtest
    print("\n4. Running backtest...")
    backtest = FactorBacktest(rebalance_frequency='M')
    returns = backtest.run_long_short(momentum_scores, price_data, top_pct=0.3, bottom_pct=0.3)
    
    # Calculate metrics
    metrics = backtest.calculate_metrics(returns)
    
    print("\n5. Performance Metrics:")
    print(f"   Total Return:      {metrics['Total Return']:.2%}")
    print(f"   Annualized Return: {metrics['Annualized Return']:.2%}")
    print(f"   Sharpe Ratio:      {metrics['Sharpe Ratio']:.2f}")
    print(f"   Max Drawdown:      {metrics['Max Drawdown']:.2%}")
    print(f"   Win Rate:          {metrics['Win Rate']:.2%}")
    
    print("\n" + "=" * 80)
    return returns, metrics


def example_multi_factor_comparison():
    """
    Example: Compare multiple factors side-by-side.
    """
    print("\n" + "=" * 80)
    print("EXAMPLE 2: Multi-Factor Comparison")
    print("=" * 80)
    
    # Define parameters
    tickers = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'META', 'NVDA', 'JPM', 'BAC', 'WMT', 'KO',
               'PEP', 'NKE', 'DIS', 'NFLX', 'TSLA', 'F', 'GM', 'BA', 'CAT', 'DE']
    end_date = datetime.now()
    start_date = end_date - timedelta(days=3*365)  # 3 years
    
    print(f"\nComparing factors on {len(tickers)} stocks")
    
    # Load data
    print("\n1. Loading data...")
    loader = DataLoader(start_date.strftime('%Y-%m-%d'), end_date.strftime('%Y-%m-%d'))
    price_data = loader.fetch_price_data(tickers)
    fundamental_data = loader.fetch_fundamental_data(price_data.columns.tolist())
    
    # Calculate all factors
    print("\n2. Calculating factors...")
    
    # Momentum
    momentum = MomentumFactor()
    momentum_scores = momentum.calculate(price_data)
    print("   ✓ Momentum")
    
    # Value
    value = ValueFactor()
    try:
        value_scores = value.calculate_from_fundamentals(fundamental_data, price_data)
    except:
        value_scores = value.calculate_synthetic_value(price_data)
    print("   ✓ Value")
    
    # Size
    size = SizeFactor()
    try:
        size_scores = size.calculate_from_fundamentals(fundamental_data, price_data)
    except:
        size_scores = size.calculate_synthetic_size(price_data)
    print("   ✓ Size")
    
    # Quality
    quality = QualityFactor()
    try:
        quality_scores = quality.calculate_from_fundamentals(fundamental_data, price_data)
    except:
        quality_scores = quality.calculate_synthetic_quality(price_data)
    print("   ✓ Quality")
    
    # Run backtests
    print("\n3. Running backtests...")
    results = {}
    
    for factor_name, scores in [('Momentum', momentum_scores), 
                                 ('Value', value_scores),
                                 ('Size', size_scores),
                                 ('Quality', quality_scores)]:
        backtest = FactorBacktest(rebalance_frequency='M')
        returns = backtest.run_long_short(scores, price_data)
        metrics = backtest.calculate_metrics(returns)
        results[factor_name] = {'returns': returns, 'metrics': metrics}
        print(f"   ✓ {factor_name}")
    
    # Display comparison
    print("\n4. Performance Comparison:")
    print("\n   " + "-" * 76)
    print(f"   {'Factor':<12} {'Return':<12} {'Sharpe':<12} {'Max DD':<12} {'Win Rate':<12}")
    print("   " + "-" * 76)
    
    for factor_name, data in results.items():
        m = data['metrics']
        print(f"   {factor_name:<12} {m['Total Return']:<12.2%} {m['Sharpe Ratio']:<12.2f} "
              f"{m['Max Drawdown']:<12.2%} {m['Win Rate']:<12.2%}")
    
    print("   " + "-" * 76)
    
    # Calculate correlations
    print("\n5. Factor Return Correlations:")
    returns_df = pd.DataFrame({name: data['returns'] for name, data in results.items()})
    corr_matrix = returns_df.corr()
    
    print("\n" + str(corr_matrix.round(3)))
    
    print("\n" + "=" * 80)
    return results


def example_custom_portfolio():
    """
    Example: Build a custom multi-factor portfolio.
    """
    print("\n" + "=" * 80)
    print("EXAMPLE 3: Custom Multi-Factor Portfolio")
    print("=" * 80)
    
    # Define parameters
    tickers = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'META', 'TSLA', 'JPM', 'V', 'WMT', 'HD']
    end_date = datetime.now()
    start_date = end_date - timedelta(days=2*365)
    
    print(f"\nBuilding composite factor portfolio")
    
    # Load data
    print("\n1. Loading data...")
    loader = DataLoader(start_date.strftime('%Y-%m-%d'), end_date.strftime('%Y-%m-%d'))
    price_data = loader.fetch_price_data(tickers)
    fundamental_data = loader.fetch_fundamental_data(price_data.columns.tolist())
    
    # Calculate factors
    print("\n2. Calculating factors...")
    momentum = MomentumFactor()
    value = ValueFactor()
    
    momentum_scores = momentum.calculate(price_data)
    value_scores = value.calculate_synthetic_value(price_data)
    
    # Normalize and combine (equal weight)
    print("\n3. Creating composite score (50% Momentum + 50% Value)...")
    
    # Z-score normalization
    momentum_z = (momentum_scores - momentum_scores.mean(axis=1, skipna=True).values.reshape(-1, 1)) / \
                 momentum_scores.std(axis=1, skipna=True).values.reshape(-1, 1)
    value_z = (value_scores - value_scores.mean(axis=1, skipna=True).values.reshape(-1, 1)) / \
              value_scores.std(axis=1, skipna=True).values.reshape(-1, 1)
    
    # Composite score
    composite_scores = 0.5 * momentum_z + 0.5 * value_z
    
    # Run backtest
    print("\n4. Running backtest...")
    backtest = FactorBacktest(rebalance_frequency='M')
    returns = backtest.run_long_short(composite_scores, price_data)
    metrics = backtest.calculate_metrics(returns)
    
    print("\n5. Composite Portfolio Metrics:")
    print(f"   Total Return:      {metrics['Total Return']:.2%}")
    print(f"   Annualized Return: {metrics['Annualized Return']:.2%}")
    print(f"   Sharpe Ratio:      {metrics['Sharpe Ratio']:.2f}")
    print(f"   Sortino Ratio:     {metrics['Sortino Ratio']:.2f}")
    print(f"   Max Drawdown:      {metrics['Max Drawdown']:.2%}")
    
    print("\n" + "=" * 80)
    return returns, metrics


def main():
    """
    Run all examples.
    """
    print("\n" + "=" * 80)
    print("FACTOR MOMENTUM VISUALIZER - EXAMPLE USAGE")
    print("=" * 80)
    print("\nThis script demonstrates how to use the components programmatically.")
    print("Each example can be run independently or together.")
    print("\n")
    
    try:
        # Example 1: Basic momentum analysis
        example_momentum_analysis()
        
        # Example 2: Multi-factor comparison
        example_multi_factor_comparison()
        
        # Example 3: Custom composite portfolio
        example_custom_portfolio()
        
        print("\n" + "=" * 80)
        print("ALL EXAMPLES COMPLETED SUCCESSFULLY!")
        print("=" * 80)
        print("\nNext Steps:")
        print("1. Modify the examples to use your own tickers")
        print("2. Adjust parameters (lookback periods, portfolio sizes, etc.)")
        print("3. Export results to CSV for further analysis")
        print("4. Create visualizations using the FactorVisualizer class")
        print("\nFor the full interactive experience, run: streamlit run app.py")
        print("=" * 80 + "\n")
        
    except Exception as e:
        print(f"\n❌ Error running examples: {e}")
        print("Make sure you have internet connection for downloading data.")
        print("If problems persist, try reducing the number of tickers or date range.")


if __name__ == "__main__":
    main()
