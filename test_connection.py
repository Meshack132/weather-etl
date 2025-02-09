import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

def main():
    try:
        conn = mysql.connector.connect(
            host=os.getenv('DB_HOST', 'localhost'),
            user=os.getenv('DB_USER', 'etl_user'),
            password=os.getenv('DB_PASSWORD', 'Pass123!'),
            database=os.getenv('DB_NAME', 'weather_db')
        )
        
        cursor = conn.cursor()
        cursor.execute("SELECT VERSION();")
        result = cursor.fetchone()
        print("Connected to MySQL!\nVersion:", result[0])
        
    except mysql.connector.Error as e:
        print("MySQL Error:", e)
    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()

if __name__ == "__main__":
    main()