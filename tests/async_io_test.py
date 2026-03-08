import asyncio
import requests


channels = [
    "https://www.google.com",
    "https://www.youfasfasdftube.com/",
    "https://www.facebook.com/",
]



async def get_scrape(channel) -> int:
    for i in channel:
        try:
            h = requests.get(i).status_code
        except:
            print(f"Uh oh, probably invalid site {i}")
            continue
        print(h)

async def main():
    await get_scrape(channels)

asyncio.run(main())