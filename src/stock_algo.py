from scraper import scrape
import asyncio
import yahooquery as yf
import math
from list_to_str import transform
from dataclasses import dataclass
import time
test_list = [
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

@dataclass
class Ticker_Info:
    earnings: dict
    financials: dict
    
    
        






#runs conditional logic and returns stock if it is good
def razor(list_of_stocks: list):
    new_list = []
    
    data = yf.Ticker(transform(list_of_stocks), asynchronous=True)
    key_stats = data.key_stats
    financial_data = data.financial_data
    earnings = data.earnings
    
   
        #shows all of the metrics being measured for the razor

    for stock in list_of_stocks:
        try:
            eps = key_stats[stock]["trailingEps"]
            
        except (KeyError, TypeError):
            eps = None
        
        try:
            free_cash_flow = financial_data[stock]["freeCashflow"]
        except (KeyError, TypeError):
            free_cash_flow = None
        
        try:
            five_yr_rev = earnings[stock]["financialsChart"]["yearly"]
        except (KeyError, TypeError):
            five_yr_rev = None
        
        if five_yr_rev is not None:
            cagr = get_CAGR(five_yr_rev)
        #stock not counted if conditions are not found 
        if all([eps, free_cash_flow]) and five_yr_rev is not None and cagr is not None and cagr > 3.5 and eps > 0 and free_cash_flow > 0:
            new_list.append(stock)
    return new_list
    





def final_stock(*args: list) -> str:
    print(razor([
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
]))
   


def get_score(ticker: str) -> float:
    ...

#gets the CAGR metric
def get_CAGR(fvyr):
    #t in formula
    t_yrs = 4
    x = True
    for i in fvyr:
        if x:
            x = False
            Initial_V = i["revenue"]
        Final_V = i["revenue"]

    
    #returns the CAGR
    try:
        cagr = (((Final_V/Initial_V)**(1/t_yrs)) - 1)*100
        return cagr
    except ZeroDivisionError:
        return None
    
    
if __name__ == "__main__":
    final_stock()
        

