import pandas as pd
import psycopg2
from datetime import datetime

# Replace with your local Parquet file path after download
parquet_file = "processed_bitcoin_data.parquet"

# Read parquet file
df = pd.read_parquet(parquet_file)

# PostgreSQL connection
conn = psycopg2.connect(
    dbname="crypto_warehouse",
    user="thetechie_guy",
    password="",
    host="localhost",
    port="5432"
)

cursor = conn.cursor()

for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO bitcoin_prices (
            bitcoin_price_usd,
            year,
            month,
            day
        )
        VALUES (%s, %s, %s, %s)
    """, (
        row["bitcoin_price_usd"],
        row["year"],
        row["month"],
        row["day"]
    ))

conn.commit()
cursor.close()
conn.close()

print("Data loaded successfully into PostgreSQL")