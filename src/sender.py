from dotenv import load_dotenv
import os
import requests
from pathlib import Path
 


#sets this var to the home dir
path_to_home_dir = Path(__file__).parent.parent

def send_message(message):
    #loads all the necessary env vars
    load_dotenv(path_to_home_dir/'.env')
    key = os.getenv("TELEGRAM_BOT_TOKEN")
    id = os.getenv("CHAT_ID")

    params = {"chat_id": id,
            "text":message}



    #"goes" to api endpoint with the given parameters and sends the message
    requests.get(f"https://api.telegram.org/bot{key}/sendMessage", params=params)


if __name__ == "__main__":
    send_message("Message")
