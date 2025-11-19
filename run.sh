#!/bin/bash

# Factor Momentum Visualizer - Quick Start Script

echo "=========================================="
echo "Factor Momentum Visualizer"
echo "=========================================="
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null
then
    echo "❌ Python 3 is not installed. Please install Python 3.8+ first."
    exit 1
fi

echo "✅ Python found: $(python3 --version)"
echo ""

# Check if requirements are installed
echo "📦 Checking dependencies..."
if ! python3 -c "import streamlit" &> /dev/null; then
    echo "⚠️  Dependencies not found. Installing..."
    pip install -r requirements.txt
    echo "✅ Dependencies installed!"
else
    echo "✅ Dependencies already installed!"
fi

echo ""
echo "🚀 Starting Factor Momentum Visualizer..."
echo ""
echo "📝 Access the app at: http://localhost:8501"
echo ""
echo "Press Ctrl+C to stop the application"
echo ""

# Run Streamlit
streamlit run app.py
