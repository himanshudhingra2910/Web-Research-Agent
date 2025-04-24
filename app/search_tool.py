import requests
from config.settings import SERPAPI_API_KEY

def perform_search(query):
    params = {
        "engine": "google",
        "q": query,
        "api_key": SERPAPI_API_KEY
    }
    res = requests.get("https://serpapi.com/search", params=params)
    data = res.json()
    return [item['link'] for item in data.get('organic_results', [])[:5]]
