# test_import.py
try:
    from etl.extract import fetch_weather
    from etl.transform import clean_weather_data
    from etl.load import save_to_csv
    print("All imports succeeded!")
except Exception as e:
    print("Import error:", e)
