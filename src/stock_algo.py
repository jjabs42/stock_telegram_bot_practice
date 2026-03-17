from scraper import scrape
import asyncio


async def main():
    print(await scrape("TGstockstradingroom", 300, "Trading signal for symbol: "))
    

asyncio.run(main())


