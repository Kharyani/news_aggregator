import requests
from config import NEWS_API_KEY, NEWSAPI_URL

def get_news(query):
    url = f"{NEWSAPI_URL}?q={query}&apiKey={NEWS_API_KEY}"
    
    response = requests.get(url)
    data = response.json()
    
    return data.get("articles", [])

if __name__ == "__main__":
    print(get_news("technology"))