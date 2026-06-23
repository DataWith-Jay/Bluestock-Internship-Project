from pathlib import Path
import sqlite3
import pandas as pd

# Project paths
RAW_DATA_DIR = Path("data/raw")
DB_PATH = Path("data/db/mutual_fund.db")

# Create database connection
conn = sqlite3.connect(DB_PATH)

print("=" * 60)
print("LOADING CSV FILES INTO SQLITE")
print("=" * 60)

# Loop through all CSV files
for file in RAW_DATA_DIR.glob("*.csv"):

    print(f"\nProcessing: {file.name}")

    # Read CSV
    df = pd.read_csv(file)

    # Create table name from filename
    table_name = file.stem

    # Load into SQLite
    df.to_sql(
        table_name,
        conn,
        if_exists="replace",
        index=False
    )

    print(f"Loaded {len(df)} rows into table: {table_name}")

# Close connection
conn.close()

print("\nDatabase created successfully!")

