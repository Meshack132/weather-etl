import sys
import os
import sqlite3
from dotenv import load_dotenv
import logging
import yaml
from pathlib import Path

# Add the etl directory to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'etl')))
from extract import fetch_weather
from transform import clean_weather_data

# Database configuration
DB_DIR = "data"
DB_NAME = "weather_data.db"
TABLE_NAME = "weather_observations"

# Create data directory if it doesn't exist
os.makedirs(DB_DIR, exist_ok=True)
DB_PATH = os.path.join(DB_DIR, DB_NAME)

def initialize_environment():
    """Initialize the runtime environment"""
    try:
        # Load environment variables
        if not load_dotenv():
            raise ValueError("Missing .env file")
        
        # Validate API key
        api_key = os.getenv("OPENWEATHER_API_KEY", "").strip()
        if not api_key:
            raise ValueError("OPENWEATHER_API_KEY not set in .env")
        if len(api_key) != 32:
            raise ValueError("API key must be exactly 32 characters")
            
        # Create required directories
        os.makedirs("logs", exist_ok=True)
        
        # Configure logging
        logging.basicConfig(
            filename=os.path.join('logs', 'etl.log'),
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s",
            filemode='w'
        )
        
        # Initialize database
        init_database()
        return True
        
    except Exception as e:
        print(f"Initialization Error: {str(e)}", file=sys.stderr)
        return False

def init_database():
    """Initialize the SQLite database"""
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                city TEXT NOT NULL,
                temperature REAL NOT NULL,
                humidity INTEGER NOT NULL,
                description TEXT NOT NULL,
                observation_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """)
            conn.commit()
    except sqlite3.Error as e:
        logging.error(f"Database initialization failed: {str(e)}")
        raise

def load_configuration():
    """Load and validate configuration file"""
    try:
        config_path = os.path.join("Config", "config.yaml")
        if not os.path.exists(config_path):
            raise FileNotFoundError(f"Missing config file: {config_path}")
            
        with open(config_path) as f:
            config = yaml.safe_load(f)
            
        # Validate required configuration
        required = ["city", "units"]
        for key in required:
            if key not in config:
                raise ValueError(f"Missing required config key: {key}")
        
        return config
        
    except Exception as e:
        logging.error(f"Config Error: {str(e)}")
        raise

def save_to_database(data):
    """Save weather data to SQL database"""
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute(f"""
            INSERT INTO {TABLE_NAME} 
            (city, temperature, humidity, description)
            VALUES (?, ?, ?, ?)
            """, (
                data["city"],
                data["temperature"],
                data["humidity"],
                data["description"]
            ))
            conn.commit()
        return True
    except sqlite3.Error as e:
        logging.error(f"Database Error: {str(e)}")
        return False

def main():
    print("\nWeather Data ETL Pipeline (SQL Version)")
    print("=" * 40)
    
    if not initialize_environment():
        sys.exit(1)
        
    try:
        config = load_configuration()
        print(f"\nProcessing weather data for: {config['city']}")
        
        # Fetch data
        raw_data = fetch_weather(
            city=config["city"],
            units=config["units"],
            api_key=os.getenv("OPENWEATHER_API_KEY").strip()
        )
        if not raw_data:
            raise ValueError("No data received from API")
        
        # Process data
        clean_data = clean_weather_data(raw_data)
        if not clean_data:
            raise ValueError("Data cleaning failed")
        
        # Save to database
        if not save_to_database(clean_data):
            raise ValueError("Failed to save to database")
        
        # Display success message
        print("\nSuccess! Data saved to SQL database")
        print(f"Database: {DB_PATH}")
        print(f"Table: {TABLE_NAME}")
        print("\n" + "=" * 40)
        
    except Exception as e:
        print(f"\nError: {str(e)}", file=sys.stderr)
        print("Details in logs/etl.log", file=sys.stderr)
        print("\n" + "=" * 40)
        sys.exit(1)

if __name__ == "__main__":
    main()