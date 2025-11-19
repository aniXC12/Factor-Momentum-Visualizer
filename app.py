"""
Factor Momentum Visualizer - Main Application
A full-stack quant research tool for factor analysis and backtesting
"""

import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import io

# Import custom modules
from data.data_fetcher import DataFetcher
from factors.factor_calculator import FactorCalculator
from backtest.backtester import Backtester
from plots.visualizations import create_performance_chart, create_correlation_heatmap, create_drawdown_chart, create_factor_scatter
from utils.helpers import format_metrics, download_csv

# Page configuration
st.set_page_config(
    page_title="Factor Momentum Visualizer",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main {
        padding: 0rem 1rem;
    }
    .stMetric {
        background-color: #f0f2f6;
        padding: 10px;
        border-radius: 5px;
    }
    h1 {
        color: #1f77b4;
        padding-bottom: 10px;
        border-bottom: 2px solid #1f77b4;
    }
    h2 {
        color: #2ca02c;
        margin-top: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# Title and description
st.title("📊 Factor Momentum Visualizer")
st.markdown("""
**A production-grade quant research platform** for equity factor analysis, portfolio construction, and backtesting.
Analyze momentum, value, size, and quality factors across custom universes.
""")

# Sidebar - Configuration
st.sidebar.header("⚙️ Configuration")

# Universe Selection
st.sidebar.subheader("1️⃣ Select Universe")
universe_type = st.sidebar.radio(
    "Choose data source:",
    ["S&P 500 (Top 50)", "Russell 1000 (Top 50)", "Custom Tickers", "Upload CSV"]
)

custom_tickers = []
if universe_type == "Custom Tickers":
    ticker_input = st.sidebar.text_area(
        "Enter tickers (comma-separated):",
        "AAPL,MSFT,GOOGL,AMZN,META,TSLA,NVDA,JPM,V,WMT"
    )
    custom_tickers = [t.strip().upper() for t in ticker_input.split(",") if t.strip()]
elif universe_type == "Upload CSV":
    uploaded_file = st.sidebar.file_uploader("Upload CSV with 'ticker' column", type=['csv'])
    if uploaded_file is not None:
        df_upload = pd.read_csv(uploaded_file)
        if 'ticker' in df_upload.columns:
            custom_tickers = df_upload['ticker'].tolist()
        else:
            st.sidebar.error("CSV must contain a 'ticker' column")

# Factor Selection
st.sidebar.subheader("2️⃣ Select Factors")
selected_factors = st.sidebar.multiselect(
    "Choose factors to analyze:",
    ["Momentum", "Value", "Size", "Quality"],
    default=["Momentum", "Value"]
)

# Date Range
st.sidebar.subheader("3️⃣ Date Range")
end_date = datetime.now()
start_date = end_date - timedelta(days=3*365)  # 3 years default

date_range = st.sidebar.date_input(
    "Select date range:",
    value=(start_date, end_date),
    max_value=end_date
)

if len(date_range) == 2:
    start_date, end_date = date_range
else:
    start_date = date_range[0]
    end_date = datetime.now()

# Advanced Options
with st.sidebar.expander("⚙️ Advanced Options"):
    rebalance_freq = st.selectbox("Rebalancing Frequency:", ["Monthly", "Quarterly"], index=0)
    top_percentile = st.slider("Long Portfolio Percentile:", 10, 30, 20, 5)
    bottom_percentile = st.slider("Short Portfolio Percentile:", 10, 30, 20, 5)
    include_benchmark = st.checkbox("Include SPY Benchmark", value=True)

# Run Analysis Button
run_analysis = st.sidebar.button("🚀 Run Analysis", type="primary", use_container_width=True)

# Main content area
if run_analysis:
    if not selected_factors:
        st.error("⚠️ Please select at least one factor to analyze.")
    else:
        with st.spinner("🔄 Fetching data and computing factors..."):
            try:
                # Initialize data fetcher
                fetcher = DataFetcher()
                
                # Get tickers based on universe selection
                if universe_type == "S&P 500 (Top 50)":
                    tickers = fetcher.get_sp500_tickers()[:50]
                elif universe_type == "Russell 1000 (Top 50)":
                    tickers = fetcher.get_russell1000_tickers()[:50]
                else:
                    tickers = custom_tickers
                
                if not tickers:
                    st.error("No tickers available. Please check your selection.")
                    st.stop()
                
                st.info(f"📊 Analyzing {len(tickers)} tickers from {start_date.strftime('%Y-%m-%d')} to {end_date.strftime('%Y-%m-%d')}")
                
                # Fetch price data
                price_data = fetcher.fetch_data(tickers, start_date.strftime('%Y-%m-%d'), end_date.strftime('%Y-%m-%d'))
                
                if price_data.empty:
                    st.error("❌ No data fetched. Please check your tickers and date range.")
                    st.stop()
                
                # Fetch fundamental data for Value factor
                fundamental_data = None
                if "Value" in selected_factors:
                    fundamental_data = fetcher.fetch_fundamentals(tickers)
                
                # Calculate factors
                calculator = FactorCalculator(price_data, fundamental_data)
                factor_scores = calculator.calculate_all_factors(selected_factors)
                
                if factor_scores.empty:
                    st.error("❌ Failed to calculate factors. Please try different parameters.")
                    st.stop()
                
                # Fetch benchmark data if needed
                benchmark_data = None
                if include_benchmark:
                    benchmark_data = fetcher.fetch_data(['SPY'], start_date.strftime('%Y-%m-%d'), end_date.strftime('%Y-%m-%d'))
                
                st.success(f"✅ Successfully calculated {len(selected_factors)} factors for {len(tickers)} tickers!")
                
                # Run backtests for each factor
                st.header("📈 Factor Performance Analysis")
                
                results = {}
                for factor in selected_factors:
                    with st.spinner(f"Backtesting {factor} factor..."):
                        backtester = Backtester(
                            factor_scores=factor_scores,
                            price_data=price_data,
                            factor_name=factor.lower(),
                            top_pct=top_percentile,
                            bottom_pct=bottom_percentile,
                            rebalance_freq=rebalance_freq.lower()
                        )
                        
                        portfolio_returns = backtester.run_backtest()
                        metrics = backtester.calculate_metrics()
                        
                        results[factor] = {
                            'returns': portfolio_returns,
                            'metrics': metrics,
                            'backtester': backtester
                        }
                
                # Display metrics
                st.subheader("📊 Performance Metrics")
                
                cols = st.columns(len(selected_factors))
                for idx, factor in enumerate(selected_factors):
                    with cols[idx]:
                        st.markdown(f"**{factor} Factor**")
                        metrics = results[factor]['metrics']
                        
                        st.metric("Total Return", f"{metrics['total_return']:.2%}")
                        st.metric("Sharpe Ratio", f"{metrics['sharpe_ratio']:.2f}")
                        st.metric("Max Drawdown", f"{metrics['max_drawdown']:.2%}")
                        st.metric("Win Rate", f"{metrics['win_rate']:.2%}")
                
                # Performance Chart
                st.subheader("📈 Cumulative Returns")
                returns_dict = {factor: results[factor]['returns'] for factor in selected_factors}
                
                fig_performance = create_performance_chart(
                    returns_dict,
                    benchmark_data['SPY'] if benchmark_data is not None else None
                )
                st.plotly_chart(fig_performance, use_container_width=True)
                
                # Rolling Sharpe Ratio
                st.subheader("📊 Rolling 12-Month Sharpe Ratio")
                
                rolling_sharpe_data = {}
                for factor in selected_factors:
                    backtester = results[factor]['backtester']
                    rolling_sharpe = backtester.calculate_rolling_sharpe(window=252)
                    rolling_sharpe_data[factor] = rolling_sharpe
                
                # Create rolling Sharpe chart
                import plotly.graph_objects as go
                fig_rolling = go.Figure()
                
                for factor, rolling_sharpe in rolling_sharpe_data.items():
                    fig_rolling.add_trace(go.Scatter(
                        x=rolling_sharpe.index,
                        y=rolling_sharpe.values,
                        mode='lines',
                        name=f"{factor} Factor",
                        line=dict(width=2)
                    ))
                
                fig_rolling.add_hline(y=0, line_dash="dash", line_color="gray", annotation_text="Zero Line")
                fig_rolling.update_layout(
                    title="Rolling 12-Month Sharpe Ratio",
                    xaxis_title="Date",
                    yaxis_title="Sharpe Ratio",
                    hovermode='x unified',
                    template='plotly_white',
                    height=400
                )
                st.plotly_chart(fig_rolling, use_container_width=True)
                
                # Drawdown Analysis
                st.subheader("📉 Drawdown Analysis")
                
                drawdown_data = {}
                for factor in selected_factors:
                    backtester = results[factor]['backtester']
                    drawdown_data[factor] = backtester.portfolio_returns
                
                fig_drawdown = create_drawdown_chart(drawdown_data)
                st.plotly_chart(fig_drawdown, use_container_width=True)
                
                # Correlation Analysis
                if len(selected_factors) > 1:
                    st.subheader("🔗 Factor Correlation Analysis")
                    
                    # Create correlation matrix of factor returns
                    returns_df = pd.DataFrame({
                        factor: results[factor]['returns'] 
                        for factor in selected_factors
                    })
                    
                    fig_corr = create_correlation_heatmap(returns_df, title="Factor Returns Correlation")
                    st.plotly_chart(fig_corr, use_container_width=True)
                    
                    # Factor score correlations
                    score_cols = [f"{factor.lower()}_score" for factor in selected_factors]
                    available_cols = [col for col in score_cols if col in factor_scores.columns]
                    
                    if len(available_cols) > 1:
                        st.subheader("📊 Factor Score Correlations")
                        score_corr_data = factor_scores[available_cols].copy()
                        score_corr_data.columns = [col.replace('_score', '').title() for col in available_cols]
                        
                        fig_score_corr = create_correlation_heatmap(score_corr_data, title="Factor Score Correlation")
                        st.plotly_chart(fig_score_corr, use_container_width=True)
                
                # Factor Scatter Plot (Score vs Future Returns)
                st.subheader("🎯 Factor Predictive Power")
                st.markdown("*Relationship between factor scores and subsequent returns*")
                
                scatter_factor = st.selectbox("Select factor for scatter analysis:", selected_factors)
                
                fig_scatter = create_factor_scatter(
                    factor_scores=factor_scores,
                    price_data=price_data,
                    factor_name=scatter_factor.lower()
                )
                st.plotly_chart(fig_scatter, use_container_width=True)
                
                # Detailed Metrics Table
                st.subheader("📋 Detailed Performance Metrics")
                
                metrics_df = pd.DataFrame({
                    factor: results[factor]['metrics']
                    for factor in selected_factors
                }).T
                
                st.dataframe(metrics_df.style.format({
                    'total_return': '{:.2%}',
                    'annualized_return': '{:.2%}',
                    'annualized_volatility': '{:.2%}',
                    'sharpe_ratio': '{:.2f}',
                    'sortino_ratio': '{:.2f}',
                    'max_drawdown': '{:.2%}',
                    'calmar_ratio': '{:.2f}',
                    'win_rate': '{:.2%}'
                }), use_container_width=True)
                
                # Download Results
                st.subheader("💾 Download Results")
                
                col1, col2 = st.columns(2)
                
                with col1:
                    # Download factor scores
                    csv_scores = factor_scores.to_csv(index=True)
                    st.download_button(
                        label="📥 Download Factor Scores",
                        data=csv_scores,
                        file_name=f"factor_scores_{datetime.now().strftime('%Y%m%d')}.csv",
                        mime="text/csv"
                    )
                
                with col2:
                    # Download metrics
                    csv_metrics = metrics_df.to_csv(index=True)
                    st.download_button(
                        label="📥 Download Performance Metrics",
                        data=csv_metrics,
                        file_name=f"performance_metrics_{datetime.now().strftime('%Y%m%d')}.csv",
                        mime="text/csv"
                    )
                
            except Exception as e:
                st.error(f"❌ An error occurred: {str(e)}")
                st.exception(e)

else:
    # Welcome screen
    st.info("👈 Configure your analysis in the sidebar and click **Run Analysis** to begin!")
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🎯 Key Features")
        st.markdown("""
        - **Multi-Factor Analysis**: Momentum, Value, Size, Quality
        - **Custom Universes**: S&P 500, Russell 1000, or your own tickers
        - **Long-Short Portfolios**: Quantile-based construction
        - **Comprehensive Metrics**: Sharpe, Sortino, Calmar, Drawdowns
        - **Interactive Visualizations**: Powered by Plotly
        - **Data Export**: Download all results as CSV
        """)
    
    with col2:
        st.markdown("### 📚 Factor Definitions")
        st.markdown("""
        **Momentum**: 12-month returns minus last month  
        **Value**: Price-to-Book or Price-to-Earnings ratio  
        **Size**: Market capitalization  
        **Quality**: Return on Equity (ROE) or similar metrics  
        """)
    
    st.markdown("---")
    
    st.markdown("### 📖 How to Use")
    st.markdown("""
    1. **Select Universe**: Choose from preset universes or upload custom tickers
    2. **Pick Factors**: Select which equity factors to analyze
    3. **Set Date Range**: Define your backtest period
    4. **Configure Options**: Adjust rebalancing frequency and percentiles
    5. **Run Analysis**: Click the button and explore results!
    """)
    
    st.markdown("---")
    
    st.markdown("### 🏗️ Built With")
    st.markdown("""
    `Python` • `Streamlit` • `yfinance` • `Plotly` • `pandas` • `numpy` • `scikit-learn`
    """)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666;'>
    <p>Factor Momentum Visualizer | Built for Quantitative Research</p>
    <p>Data provided by Yahoo Finance • Not financial advice</p>
</div>
""", unsafe_allow_html=True)
