# import all packages 
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import fpdf as pdf
from fpdf import FPDF
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


def addFormattedPDFPage(pdf,logoPath):
    pdf.add_page()
    r, g, b = (81, 36, 122)
    pdf.set_fill_color(r, g, b)

# Header rectangle (top strip)
    header_height = 20
    pdf.rect(x=0, y=0, w=210, h=header_height, style='F')

# Add logo in top right corner (within header)
    if os.path.exists(logoPath):
        logo_width = 20
        x_pos = 10
        pdf.image(logoPath, x=x_pos, y=0, w=logo_width)


# Footer rectangle (bottom strip)
    footer_height = 20
    pdf.rect(x=0, y=297 - footer_height, w=210, h=footer_height, style='F')

    pdf.set_text_color(255, 255, 255)
    pdf.set_font('Arial', 'B', 12)
 
    page_number_text = f'Page {pdf.page_no()}'
    text_width = pdf.get_string_width(page_number_text)
    x_position = 210 - 5 - text_width  # A4 width = 210mm, minus 5mm margin and text width

    pdf.set_auto_page_break(False)
    pdf.set_xy(x_position, 282) 
    pdf.cell(0, 10, page_number_text)
