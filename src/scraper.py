from telethon import TelegramClient
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
client = TelegramClient("Client2", api_hash=api_hash, api_id=api_id)

#with basically connects and disconencts
async def scrape(channel, lim):
    async with client:
        #gets channel id
        chatid = (await client.get_entity(channel)).id
        
        """
        Gets messages with limit of last 100, then goes through each message object
        and checks for a $, (message.message) where message 2 is an attribute of the message obj
        """
        messages = await client.get_messages(chatid, limit=lim)
        for message in messages:
            actual_message = message.message
            if actual_message == None:
                continue
            for char in actual_message:
                if char == "$":
                    print(f"{actual_message}")

async def main():
    channel1 = "TopSecretStockAlerts"
    await scrape(channel1, lim=200 )
        
    


if __name__ == "__main__":
    asyncio.run(main())