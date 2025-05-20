import os
import requests
import logging
from time import sleep
from dotenv import load_dotenv

load_dotenv()  # Load environment variables

def fetch_weather(city, units, api_key=None, retries=3):
    """Fetch weather data from OpenWeather API"""
    api_key = api_key or os.getenv("OPENWEATHER_API_KEY")  # Fallback to .env
    if not api_key:
        raise ValueError("No API key provided and OPENWEATHER_API_KEY not set in .env")
    
    url = "http://api.openweathermap.org/data/2.5/weather"
    params = {'q': city, 'appid': api_key, 'units': units}

    for attempt in range(retries):
        try:
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            logging.info("Weather data fetched successfully.")
            return response.json()
        except Exception as e:
            logging.warning(f"Attempt {attempt+1}: {e}")
            sleep(2)
    logging.error("Failed to fetch data after retries.")
    return None