## Data profiling file



from pathlib import Path
import pandas as pd

RAW_DATA_DIR = Path("data/raw")

for file in RAW_DATA_DIR.glob("*.csv"):
    print("\n" + "=" * 80)
    print(file.name)
    print("=" * 80)

    df = pd.read_csv(file)

    print("\nColumns:")
    print(df.columns.to_list())

    print("\nData Types:")
    print(df.dtypes)

    print("\n Missing Values:")
    print(df.isnull().sum())

    print("\nFirst 5 Rows:")
    print(df.head())

