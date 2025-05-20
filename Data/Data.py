# Data/query_data.py
import sqlite3
from pathlib import Path
from tabulate import tabulate
import logging

# Configure paths
DB_DIR = Path(__file__).parent
DB_NAME = "weather_data.db"
DB_PATH = DB_DIR / DB_NAME
TABLE_NAME = "weather_observations"

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def verify_database():
    """Ensure database exists and is accessible"""
    try:
        if not DB_PATH.exists():
            raise FileNotFoundError(f"Database file not found at {DB_PATH}")
            
        with sqlite3.connect(str(DB_PATH)) as conn:
            cursor = conn.cursor()
            cursor.execute(f"""
            SELECT name FROM sqlite_master 
            WHERE type='table' AND name='{TABLE_NAME}'
            """)
            if not cursor.fetchone():
                raise ValueError(f"Table {TABLE_NAME} not found in database")
    except Exception as e:
        logging.error(f"Database verification failed: {str(e)}")
        raise

def display_weather_data():
    """Display all weather data"""
    try:
        verify_database()
        
        with sqlite3.connect(str(DB_PATH)) as conn:
            cursor = conn.cursor()
            cursor.execute(f"""
            SELECT id, city, temperature, humidity, description, 
                   strftime('%Y-%m-%d %H:%M', observation_time) as time 
            FROM {TABLE_NAME}
            ORDER BY observation_time DESC
            LIMIT 10
            """)
            
            rows = cursor.fetchall()
            columns = [description[0] for description in cursor.description]
            
            if rows:
                print("\nLatest Weather Data (10 most recent):")
                print(tabulate(rows, headers=columns, tablefmt="psql"))
                print(f"\nDatabase location: {DB_PATH}")
            else:
                print("No weather data available in the database.")
                
    except Exception as e:
        logging.error(f"Error: {str(e)}")
        print("Failed to display data. Check logs for details.")

if __name__ == "__main__":
    display_weather_data()