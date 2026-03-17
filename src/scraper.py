from telethon import TelegramClient
import re
import os
from pathlib import Path
from dotenv import load_dotenv
import asyncio

#sets env variables
envdir = Path(__file__).parent.parent
load_dotenv(envdir/".env")
api_id = os.getenv("api_id")
api_hash = os.getenv("apihash")
telegram_bot_token = os.getenv("TELEGRAM_BOT_TOKEN")

#Client Obj

client = TelegramClient("Client2", api_id=api_id, api_hash=api_hash)





#with basically connects and disconencts
async def scrape(channel, lim, Indicator):
   try:
    async with client:
            #gets channel id
            try:
                chatid = (await client.get_entity(channel)).id
            except ValueError as e:
                print(f"Error: {e}")
                return
            
            """
            Gets messages with limit of last 100, then goes through each message object
            and checks for a $, (message.message) where message 2 is an attribute of the message obj
            """
            try:
                messages = await client.get_messages(chatid, limit=lim)
            except:
                ...


            tickers = []
            for message in messages:
                actual_message = message.message
                if actual_message == None:
                    continue
                #checks for $
                if Indicator.lower() in actual_message.lower():
                    #all letters after $, until whitespace
                    x = re.findall(rf"{Indicator}"+r"\D{2,4}\b", actual_message)
                    #appends all tickers, x is the tickers in each message
                    length = len(Indicator)
                    for i in x:
                        if "\n" in i:
                            tickers.append(i[length:-1])
                        else:
                            tickers.append(i[length:])
                        
                    
                    # tickers.append(x[length:])
            return(set(tickers))
   except TypeError as e:
       print(f"Error: Probably Wrong api id or hash, {e}")
            

async def main():
    channel1 = "TopSecretStockAlerts"
    x = await scrape(channel1, lim=200, Indicator="$" )
    print(x)
        
    


if __name__ == "__main__":
    asyncio.run(main())



