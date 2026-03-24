from scraper import scrape
import asyncio
import requests
import yfinance as yf

async def final_stock(*args: list) -> str:
    await razor(["AAPL", "TSLA", "INTC", "TEAM"])


async def get_score(ticker: str) -> float:
    ...

#disqualifies bad stocks
async def razor (list_of_stocks: list) -> list:
    for stock in list_of_stocks:
        data = yf.Ticker(stock)
        #shows all of the metrics being measured for the razor
        eps = data.financials.loc["Basic EPS"].iloc[0]
        ...

        #conditions for the metrics
        if eps < 0:
            list_of_stocks.remove(stock)
    print(list_of_stocks)


        
  




            


    
if __name__ == "__main__":
    asyncio.run(final_stock())
        

