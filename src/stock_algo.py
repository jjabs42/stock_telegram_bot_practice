from scraper import scrape
import asyncio
import yahooquery as yf
import math


async def get_eps(ticker):
    ...
    
#runs conditional logic and returns stock if it is good
async def get_stock(ticker):
    loop = asyncio.get_running_loop()
    data = yf.Ticker(ticker.upper())
    counter = 0
        #shows all of the metrics being measured for the razor
    try:
        eps = float(data.financials.loc["Basic EPS"].iloc[0])
    except KeyError or ValueError:
        eps = None
        counter += 1
    
    try:
        free_cash_flow = int(data.cash_flow.iloc[0].iloc[0])
    except IndexError:
        free_cash_flow = None
        counter += 1
    
    try:
        five_yr_rev = data.financials.loc["Total Revenue"]
    except KeyError:
        five_yr_rev = None
    
    if five_yr_rev is not None:
        cagr = get_CAGR(five_yr_rev)
    else:
        counter += 1
    #stock not counted if conditions are not found
    if counter > 1:
        return None
    
    elif all([eps, free_cash_flow]) and five_yr_rev is not None and cagr is not None and cagr > 3 and eps > 0 and free_cash_flow > 0:
        print(ticker)
        return ticker
    
    else: 
        return None





async def final_stock(*args: list) -> str:
    print(await razor([
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
   


async def get_score(ticker: str) -> float:
    ...

#gets the CAGR metric
def get_CAGR(fvyr):
    #t in formula
    t_yrs = 0
    for j in (fvyr):
        if math.isnan(j):
            break
         
        elif type(j) == int or float:
            t_yrs += 1
    Final_V = fvyr.iloc[0]
    Initial_V = fvyr.iloc[t_yrs-1]
    
    #returns the CAGR
    try:
        cagr = (((Final_V/Initial_V)**(1/t_yrs)) - 1)*100
        return cagr
    except ZeroDivisionError:
        return None
    




#disqualifies bad stocks
async def razor (list_of_stocks: list) -> list:
    coros = [get_stock(obj) for obj in list_of_stocks]
    await asyncio.gather(*coros)
    
    





    
if __name__ == "__main__":
    asyncio.run(razor(([
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
])))
        

