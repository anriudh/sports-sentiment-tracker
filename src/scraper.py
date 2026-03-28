import requests
import os
from dotenv import load_dotenv
load_dotenv()
import pandas as pd

def fetch_articles():
    api_key = os.getenv("NEWS_API_KEY")
    url = "https://newsapi.org/v2/everything"

    params = {
        "q": "football soccer",
        "language": "en",
        "sortBy": "publishedAt",
        "pageSize": 100,
        "apiKey": api_key
    }

    response = requests.get(url, params = params)
    articles = response.json()["articles"]

    data = [
        {
            "title": article["title"],
            "description": article["description"],
            "published_at": article["publishedAt"],
            "source": article["source"]["name"]
        }
        for article in articles
    ]
    df = pd.DataFrame(data)
    df.to_csv("data/csv/raw_articles.csv", index = False)
    print(f"Saved {len(df)} articles to data/csv/raw_articles.csv")
    return df

if __name__ == "__main__":
    fetch_articles()
