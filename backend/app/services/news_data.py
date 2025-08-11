
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("NEWS_API_KEY")

import requests
def get_news(ticker):
    url = ('https://newsapi.org/v2/everything?'
       f'q={ticker}&'
       'from=2025-07-16&'
       'sortBy=popularity&'
       'pageSize=10&'
       f'apiKey={api_key}')
    response = requests.get(url)
    data = response.json()
    try:
        articles = data["articles"][:10]
        simplified = []
        for article in articles:
            simplified.append({
               "title": article.get("title"),
               "url": article.get("url"),
               "source": article.get("source", {}).get("name", "Unknown")
            })
        return simplified

    except KeyError:
      return "Error: Could not retrieve news data. Check ticker or API limit."
