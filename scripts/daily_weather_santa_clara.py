import pandas as pd
import requests
import sqlite3
import os

url = "https://api.open-meteo.com/v1/forecast?latitude=37.3541&longitude=-121.9552&hourly=temperature_2m,precipitation_probability,precipitation,relative_humidity_2m,weather_code"

response = requests.get(url)
data = response.json()

df = pd.DataFrame(data["hourly"])

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
db_path = os.path.join(BASE_DIR, "data", "weather_data.db")

print("BASE_DIR:", BASE_DIR)
print("DB PATH:", db_path)
conn = sqlite3.connect(db_path)

df.to_sql("weather", conn, if_exists="replace", index=False)

conn.close()