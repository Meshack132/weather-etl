

```markdown
# 🌦️ Weather ETL Pipeline

A simple ETL (Extract, Transform, Load) pipeline built with Python to fetch real-time weather data from an external API and store it in a PostgreSQL database.

## 📌 Features

- 🔄 Fetches live weather data via REST API
- 🧹 Cleans and transforms raw JSON into structured data
- 🗃️ Loads the data into a PostgreSQL database
- 🕒 Automatable for scheduled tasks (e.g. using cron)

## 🏗️ Project Structure

```

weather-etl/
├── config.py          # API keys and DB credentials
├── extract.py         # Extracts data from weather API
├── transform.py       # Cleans and processes raw data
├── load.py            # Inserts data into PostgreSQL
├── main.py            # Main entry point for ETL execution
├── requirements.txt   # Dependencies
└── README.md          # Project documentation

````

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Meshack132/weather-etl.git
cd weather-etl
````

### 2. Install dependencies

Create a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

Then install the dependencies:

```bash
pip install -r requirements.txt
```

### 3. Configure API and DB

Update `config.py` with your:

* API key
* PostgreSQL credentials
* City or location of interest

### 4. Run the ETL process

```bash
python main.py
```

## 🛠️ Tech Stack

* Python 3.x
* Requests
* psycopg2 (PostgreSQL connector)
* PostgreSQL

## ✅ Example Output

Weather data is stored in a `weather_data` table with columns like:

* `timestamp`
* `temperature`
* `humidity`
* `pressure`
* `description`
* `location`

## 📅 Automation

This ETL pipeline can be scheduled to run periodically using:

* `cron` (Linux/macOS)
* `Task Scheduler` (Windows)
* Cloud scheduler like AWS Lambda + CloudWatch or Azure Functions

## 🧠 Future Improvements

* Add error logging and retry logic
* Store historical data in S3 or data lake
* Visualize data in a dashboard (e.g., Power BI, Grafana)

## 🤝 Contributing

Pull requests are welcome! If you'd like to contribute:

1. Fork the repo
2. Create a new branch
3. Make changes and commit
4. Push to your fork
5. Create a Pull Request

## 🧾 License

This project is licensed under the MIT License.

---

Built with ❤️ by [Meshack Mthimkhulu](https://github.com/Meshack132)

```

---

```
