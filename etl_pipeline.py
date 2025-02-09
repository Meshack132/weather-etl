import os
import requests
import mysql.connector
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# OpenWeatherMap API Configuration
API_KEY = os.getenv('WEATHER_API_KEY', 'a8049fbb4f6dd1b816dd9ada7af56a76')  # Replace with your key
CITY = "Johannesburg"

# Database Configuration
DB_CONFIG = {
    'user': os.getenv('DB_USER', 'etl_user'),
    'password': os.getenv('DB_PASSWORD', 'Pass123!'),
    'host': os.getenv('DB_HOST', 'localhost'),
    'database': os.getenv('DB_NAME', 'weather_db'),
    'raise_on_warnings': True
}

def extract_data():
    """Extract weather data from OpenWeatherMap API"""
    url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        # Validate required fields
        if 'main' not in data or 'wind' not in data:
            print("❌ API response missing required fields")
            return None

        print("✅ API data received:", data)
        return data

    except requests.exceptions.RequestException as e:
        print(f"❌ Extraction failed: {e}")
        return None

def transform_data(raw_data):
    """Transform and validate data"""
    if not raw_data:
        return None

    try:
        return {
            'city': CITY,
            'temperature': float(raw_data['main']['temp']),
            'humidity': float(raw_data['main']['humidity']),
            'wind_speed': float(raw_data['wind']['speed']),
            'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
    except KeyError as e:
        print(f"❌ Missing key in data: {str(e)}")
        return None

def load_data(clean_data):
    """Load data into MySQL database"""
    if not clean_data:
        return False

    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()

        # Create table if not exists
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS weather_data (
                id INT AUTO_INCREMENT PRIMARY KEY,
                city VARCHAR(255) NOT NULL,
                temperature FLOAT,
                humidity FLOAT,
                wind_speed FLOAT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        # Insert data
        cursor.execute("""
            INSERT INTO weather_data 
                (city, temperature, humidity, wind_speed, created_at)
            VALUES
                (%(city)s, %(temperature)s, %(humidity)s, %(wind_speed)s, %(created_at)s)
        """, clean_data)

        conn.commit()
        print(f"✅ Inserted {cursor.rowcount} row(s) successfully")
        return True

    except mysql.connector.Error as e:
        print(f"❌ Database error: {e}")
        return False
    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()

def main():
    print("🚀 Starting ETL pipeline...")

    # Extract
    raw_data = extract_data()
    if not raw_data:
        print("❌ Extraction phase failed")
        return

    # Transform
    clean_data = transform_data(raw_data)
    if not clean_data:
        print("❌ Transformation phase failed")
        return

    # Load
    if load_data(clean_data):
        print("✅ ETL pipeline completed successfully!")
    else:
        print("❌ Loading phase failed")

if __name__ == "__main__":
    main()
