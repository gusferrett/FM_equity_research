import requests

# financial_metrics.py

def calculate_pe_ratio(price, earnings_per_share):
    """
    Calculate the Price-to-Earnings (P/E) ratio.
    :param price: Current stock price
    :param earnings_per_share: Earnings per share (EPS)
    :return: P/E ratio
    """
    if earnings_per_share == 0:
        return float('inf')  # Avoid division by zero
    return price / earnings_per_share

def calculate_eps(net_income, shares_outstanding):
    """
    Calculate Earnings Per Share (EPS).
    :param net_income: Net income of the company
    :param shares_outstanding: Total shares outstanding
    :return: EPS
    """
    if shares_outstanding == 0:
        return 0  # Avoid division by zero
    return net_income / shares_outstanding

def calculate_roa(net_income, total_assets):
    """
    Calculate Return on Assets (ROA).
    :param net_income: Net income of the company
    :param total_assets: Total assets of the company
    :return: ROA
    """
    if total_assets == 0:
        return 0  # Avoid division by zero
    return net_income / total_assets

def calculate_dividend_yield(dividend, price):
    """
    Calculate Dividend Yield.
    :param dividend: Annual dividend payment
    :param price: Current stock price
    :return: Dividend yield
    """
    if price == 0:
        return 0  # Avoid division by zero
    return dividend / price

