from scraper import scrape
import asyncio
import yfinance as yf
import math

async def final_stock(*args: list) -> str:
    print(await razor(["INTC", "NVDA", "AAPL", "TIPSMUSIC", "TSLA"]))
   


async def get_score(ticker: str) -> float:
    ...

#gets the CAGR metric
async def get_CAGR(stock):
    yfobj = yf.Ticker(stock)
    five_yr_rev = yfobj.financials.loc["Total Revenue"]
    #t in formula
    t_yrs = 0
    for j in (five_yr_rev):
        if math.isnan(j):
            break
         
        elif type(j) == int or float:
            t_yrs += 1
    Final_V = five_yr_rev.iloc[0]
    Initial_V = five_yr_rev.iloc[t_yrs-1]
    
    #returns the CAGR
    try:
        print(stock)
        return ((Final_V/Initial_V)**(1/t_yrs)) + 1
    except:
        pass




#disqualifies bad stocks
async def razor (list_of_stocks: list) -> list:
    updated_list = list_of_stocks.copy()
    for stock in list_of_stocks:
        data = yf.Ticker(stock.upper())
        #shows all of the metrics being measured for the razor
        try:
            eps = int(data.financials.loc["Basic EPS"].iloc[0])
            free_cash_flow = int(data.cash_flow.iloc[0].iloc[0])
        except:
            print(f"{stock} is probably an invalid stock")
            updated_list.remove(stock)
            continue
        
        cagr = await get_CAGR(stock)
        

        #conditions for the metrics
        if eps < 0 or free_cash_flow < 0 or cagr < 4.5:
            updated_list.remove(stock)
            
    return updated_list
   




    
if __name__ == "__main__":
    asyncio.run(final_stock())
        

