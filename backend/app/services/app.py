from flask import Flask, render_template, request
import json
from news_data import get_news  # replace with your actual module names
from ai_opinion import analysis

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    ai_opinion = None
    if request.method == 'POST':
        ticker = request.form.get('ticker')
        news_articles = get_news(ticker)
        raw_opinion = analysis(ticker, news_articles)
        try:
            ai_opinion = json.loads(raw_opinion)
        except Exception:
            ai_opinion = {
                "sentiment": "Error",
                "summary": "Could not parse AI response.",
                "suggestion": "Hold"
            }
    return render_template('index.html', ai_opinion=ai_opinion)
if __name__ == "__main__":
    app.run(debug=True)