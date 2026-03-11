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



#Client Obj
client = TelegramClient("Client1", api_hash=api_hash, api_id=api_id)

#with basically connects and disconencts
async def main():
    async with client:
        await client.send_message("+12489618910", "hello sir")
        
    



asyncio.run(main())