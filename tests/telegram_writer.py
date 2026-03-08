from dotenv import load_dotenv
import os
import requests
from pathlib import Path

path_to_home_dir = Path(__file__).parent.parent



load_dotenv(path_to_home_dir/'.env')
key = os.getenv("TELEGRAM_BOT_TOKEN")
id = os.getenv("CHAT_ID")
message = "$TSLA is a buy with MACD at ~1.56"

params = {"chat_id": id,
          "text":message}

requests.get(f"https://api.telegram.org/bot{key}/sendMessage", params=params)

