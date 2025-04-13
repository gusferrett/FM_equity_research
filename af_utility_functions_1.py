# import all packages 
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import fpdf as pdf
import os


def getStockFinancial():
    TICKER = input('Enter a stock ticker (e.g. BHP.AX): ').upper()

    try:
        stock = yf.Ticker(TICKER)
        stock_prices = stock.history(period="10y")
    except Exception as e:
        print(f"Error: {e}")
        return None, None

    return stock_prices, TICKER


