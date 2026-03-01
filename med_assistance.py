from dotenv import load_dotenv
import requests
import os

load_dotenv()

SERPAPI_API_KEY = os.getenv("SERPAPI_API_KEY")
SERPAPI_URL = "https://serpapi.com/search"

def search_nearby_hospitals(location):
    params = {
        "engine": "google",
        "q": f"hospitals near {location}",
        "api_key": SERPAPI_API_KEY,
        "num": 5
    }
    response = requests.get(SERPAPI_URL, params=params)
    results = response.json()
    if "organic_results" in results:
        hospitals = []
        for result in results["organic_results"][:5]:
            title = result.get("title", "N/A")
            address = result.get("address", "N/A")
            link = result.get("link", "N/A")
            hospitals.append(f"**{title}**\n\n{address}\n[Visit Website]({link})")
        return hospitals
    return ["No hospital data found."]