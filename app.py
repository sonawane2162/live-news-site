56230be41a7944abac39a36dc0ce4fd3
from flask import Flask
import requests

app = Flask(__name__)

API_KEY = "56230be41a7944abac39a36dc0ce4fd3"

@app.route("/")
def home():
    url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={API_KEY}"
    response = requests.get(url)
    data = response.json()

    news_html = "<h1>Live India News</h1>"

    for article in data["articles"][:10]:
        news_html += f"<h3>{article['title']}</h3>"
        news_html += f"<p>{article['description']}</p>"
        news_html += "<hr>"

    return news_html

if __name__ == "__main__":
    app.run()
