from dotenv import load_dotenv
import requests
import os

load_dotenv()

GEOAPIFY_API_KEY = os.getenv("GEOAPIFY_API_KEY")

def get_place_details(location):
    geocode_url = "https://api.geoapify.com/v1/geocode/search"

    params = {
        "text": location,
        "filter": "countrycode:in",
        "limit": 1,
        "api_key": GEOAPIFY_API_KEY
    }

    response = requests.get(geocode_url, params=params)
    data = response.json()

    if data.get("features"):
        properties = data["features"][0]["properties"]
        place_id = properties.get("place_id")
        return place_id
    return None

def search_nearby_hospitals(location):
    place_id = get_place_details(location)
    if not place_id:
        return ["Could not find the location."]

    places_url = "https://api.geoapify.com/v2/places"

    params = {
        "categories": "healthcare.hospital",
        "filter": f"place:{place_id}",
        "limit": 5,
        "api_key": GEOAPIFY_API_KEY
    }

    response = requests.get(places_url, params=params)
    data = response.json()

    hospitals = []

    if data.get("features"):
        for place in data["features"]:
            properties = place.get("properties", {})

            name = properties.get("name", "N/A")
            address = properties.get("formatted", "Address not available")
            phone = properties.get("contact", {}).get("phone", "N/A")

            hospital_info = f"### {name}\n\n{address}"

            if phone:
                hospital_info += f"\n\n({phone})"

            hospitals.append(hospital_info)
        return hospitals
    
    return ["No hospital data found."]