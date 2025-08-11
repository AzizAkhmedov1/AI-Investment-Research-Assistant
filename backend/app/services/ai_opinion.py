import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))  

def analysis(ticker: str, news_articles: list):
    headlines_text = "\n".join([f"- {article['title']}" for article in news_articles])

    prompt = (
        f"You are a financial AI assistant. Analyze the following news headlines about the stock {ticker}.\n"
        "Return the result in this exact JSON format:\n"
        '{\n  "sentiment": "Positive | Neutral | Negative",\n'
        '  "summary": "Short summary here",\n'
        '  "suggestion": "Buy | Hold | Sell"\n}\n'
        f"Headlines:\n{headlines_text}"
    )

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5,
    )

    return response.choices[0].message.content
