from stock_algo import get_stock
import asyncio
import yahooquery as yf
import time


x = [
    "AAPL", "MSFT", "GOOGL", "AMZN", "NVDA", "META", "TSLA", "BRK.B", "UNH", "LLY",
    "JPM", "V", "MA", "AVGO", "HD", "PG", "COST", "ORCL", "ABBV", "ADBE",
    "CVX", "XOM", "BAC", "KO", "PEP", "TMO", "CRM", "WMT", "MCD", "CSCO",
    "ACN", "ABT", "LIN", "AMD", "BAC", "INTC", "INTU", "VZ", "DIS", "PM",
    "TXN", "DHR", "CAT", "PFE", "AMAT", "IBM", "NEE", "MS", "GE", "UNP",
    "RTX", "HON", "LOW", "AXP", "GS", "COP", "BKNG", "AMGN", "T", "SPGI",
    "SYK", "TJX", "PLD", "BLK", "SBUX", "ELV", "GILD", "BA", "LMT", "NOW",
    "MDLZ", "ISRG", "ADI", "C", "BMY", "CB", "MMC", "VRTX", "LRCX", "CI",
    "ADP", "REGN", "ETN", "MDT", "SCHW", "ZTS", "MU", "DE", "MO", "PGR",
    "EOG", "BSX", "VLO", "CVS", "FI", "BDX", "PANW", "SNPS", "KLAC", "TGT"
]

y = True
for i in x:
    if y == True:
        string = i
        y = False
        continue
    string += f" {i}"
        

obj = yf.Ticker(string, asynchronous=True)
print(obj.financial_data["TSLA"])
    




