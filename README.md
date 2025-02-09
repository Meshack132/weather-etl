# Weather ETL Pipeline

## 🌍 About This Project
This ETL (Extract, Transform, Load) pipeline fetches weather data from **OpenWeatherMap API**, processes it, and stores it in a **MySQL database**.

## 🚀 Features
- Extracts weather data (temperature, humidity, wind speed) for a specified city.
- Transforms and validates the extracted data.
- Loads the data into a MySQL database.
- Handles errors and logs API responses.

## 🛠️ Technologies Used
- **Python** (Requests, MySQL Connector, dotenv)
- **MySQL** (Database Storage)
- **OpenWeatherMap API** (Weather Data Source)
- **Git & GitHub** (Version Control)

## 📌 Prerequisites
Make sure you have the following installed:
- Python 3.x
- MySQL Server
- Pip packages: `requests`, `mysql-connector-python`, `python-dotenv`

## ⚡ Installation & Setup

1. **Clone the repository**
   ```sh
   git clone https://github.com/yourusername/weather-etl.git
   cd weather-etl
   ```

2. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```

3. **Set up the `.env` file**
   Create a `.env` file in the project directory and add:
   ```ini
   RAPIDAPI_KEY=your_api_key_here
   DB_USER=your_db_user
   DB_PASSWORD=your_db_password
   DB_HOST=localhost
   DB_NAME=weather_db
   ```

4. **Run the ETL pipeline**
   ```sh
   python etl_pipeline.py
   ```

## 🔄 Database Schema
The pipeline creates a table `weather_data` with the following structure:
```sql
CREATE TABLE IF NOT EXISTS weather_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    city VARCHAR(255) NOT NULL,
    temperature FLOAT,
    humidity FLOAT,
    wind_speed FLOAT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## ❗ Troubleshooting
- **Error: Table 'weather_data' already exists**
  ```sh
  DROP TABLE weather_data;
  ```
- **API Error: Premium subscription required**
  - Ensure you're using a valid OpenWeatherMap **Free API Key**.

## 📜 License
This project is licensed under the MIT License.

---

### 🎯 Author
[Meshack Mthimkhulu](https://github.com/Meshack132)

