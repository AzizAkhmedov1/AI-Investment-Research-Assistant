import os
from dotenv import load_dotenv

load_dotenv()

import requests
api_key = os.getenv("ALPHA_VANTAGE_API_KEY")

def get_price(ticker):
    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={ticker}&interval=5min&apikey={api_key}"
    r = requests.get(url)
    data = r.json()
    try:
        price = data["Global Quote"]["05. price"]
        return price
    except KeyError:
        return "Error: Could not retrieve price data. Check ticker or API limit."


