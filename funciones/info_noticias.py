import requests

def get_news():
    url = "https://newsapi.org/v2/top-headlines?country=co&apiKey=6a22b9fffa3b44ed9ba394da947101da"
    response = requests.get(url)
    news_data = response.json()
    articles = news_data["articles"]
    headlines = ""
    for article in articles:
        headlines += article["title"] + ". "
    return headlines