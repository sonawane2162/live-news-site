
from flask import Flask
import requests
import os

app = Flask(__name__)

API_KEY = os.environ.get("56230be41a7944abac39a36dc0ce4fd3")

@app.route("/")
def home():
    url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={API_KEY}"
    response = requests.get(url)
    data = response.json()

    news_html = "<h1>Live India News</h1>"

    if "articles" in data:
        for article in data["articles"][:10]:
            title = article.get("title", "")
            desc = article.get("description", "")
            news_html += f"<h3>{title}</h3>"
            news_html += f"<p>{desc}</p><hr>"
    else:
        news_html += "<p>Error fetching news.</p>"

    return news_html
