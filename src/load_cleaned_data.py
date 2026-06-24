import pandas as pd
from pathlib import Path
from sqlalchemy import create_engine

# Database folder inside data/
db_dir = Path("data/db")

db_dir.mkdir(
    parents=True,
    exist_ok=True
)

DB_PATH = db_dir / "bluestock_mf.db"

print(f"Database Path: {DB_PATH}")

engine = create_engine(
    f"sqlite:///{DB_PATH}"
)

processed_dir = Path(
    "data/processed"
)

print("=" * 60)
print("LOADING CLEANED DATA INTO SQLITE")
print("=" * 60)

for file in processed_dir.glob("*.csv"):

    table_name = (
        file.stem
        .replace("_clean", "")
    )

    print(f"\nLoading: {file.name}")

    df = pd.read_csv(file)

    df.to_sql(
        table_name,
        engine,
        if_exists="replace",
        index=False
    )

    print(
        f"Table: {table_name}"
    )

    print(
        f"Rows Loaded: {len(df)}"
    )

print("\nDatabase Load Complete!")


