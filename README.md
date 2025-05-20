
```markdown
# Weather ETL Pipeline 🌦️

A Python-based ETL pipeline that extracts weather data from OpenWeatherMap API, transforms it, and loads it into a SQLite database.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![SQLite](https://img.shields.io/badge/SQLite-3.x-green.svg)

## Features ✨

- **Real-time weather data extraction** from OpenWeatherMap API
- **Data cleaning and transformation**
- **SQL database storage** with automatic table creation
- **Query interface** to view collected data
- **Error handling and logging**

## Project Structure 📁

```
weather-etl/
├── data/               # Database storage
│   └── weather_data.db
├── etl/                # ETL components
│   ├── extract.py
│   ├── transform.py
│   └── __init__.py
├── Config/             # Configuration
│   └── config.yaml
├── logs/               # Log files
├── .env                # API keys
├── main.py             # Main pipeline
└── query_data.py       # Data viewer
```

## Installation ⚙️

1. Clone the repository:
```bash
git clone https://github.com/Meshack132/weather-etl.git
cd weather-etl
```

2. Create and activate virtual environment:
```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Configuration ⚙️

1. Create `.env` file:
```ini
OPENWEATHER_API_KEY=your_api_key_here
```

2. Edit `Config/config.yaml`:
```yaml
city: "London"
units: "metric"
```

## Usage 🚀

1. Run the ETL pipeline:
```bash
python main.py
```

2. Query the database:
```bash
python data/query_data.py
```

## Example Output 📊

```
Weather Data ETL Pipeline (SQL Version)
========================================

Processing weather data for: London

Success! Data saved to SQL database
Database: data\weather_data.db
Table: weather_observations

Latest Weather Data (10 most recent):
id | city   | temperature | humidity | description     | time
1  | London |        20.6 |       37 | overcast clouds | 2025-05-20 18:35
```

## Contributing 🤝

Pull requests are welcome! For major changes, please open an issue first.

## License 📄

[MIT](https://choosealicense.com/licenses/mit/)
```


