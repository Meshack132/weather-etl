# transform.py
def clean_weather_data(data):
    """Clean raw weather data by extracting useful fields."""
    try:
        if not data:
            return {}
        return {
            "city": data.get("name", ""),
            "temperature": data["main"].get("temp", 0),
            "humidity": data["main"].get("humidity", 0),
            "description": data["weather"][0].get("description", ""),
        }
    except KeyError as e:
        logging.error(f"Missing key in raw data: {e}")
        return {}