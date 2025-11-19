@echo off
REM Factor Momentum Visualizer - Quick Start Script for Windows

echo ==========================================
echo Factor Momentum Visualizer
echo ==========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed. Please install Python 3.8+ first.
    pause
    exit /b 1
)

echo Python found!
echo.

REM Check if requirements are installed
echo Checking dependencies...
python -c "import streamlit" >nul 2>&1
if errorlevel 1 (
    echo Dependencies not found. Installing...
    pip install -r requirements.txt
    echo Dependencies installed!
) else (
    echo Dependencies already installed!
)

echo.
echo Starting Factor Momentum Visualizer...
echo.
echo Access the app at: http://localhost:8501
echo.
echo Press Ctrl+C to stop the application
echo.

REM Run Streamlit
streamlit run app.py

pause
