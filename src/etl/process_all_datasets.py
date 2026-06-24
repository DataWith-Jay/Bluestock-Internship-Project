import pandas as pd
from pathlib import Path

RAW_DIR = Path("data/raw")
PROCESSED_DIR = Path("data/processed")

PROCESSED_DIR.mkdir(
    parents=True,
    exist_ok=True
)

print("=" * 60)
print("PROCESSING ALL DATASETS")
print("=" * 60)

for file in RAW_DIR.glob("*.csv"):

    print(f"\nProcessing: {file.name}")

    df = pd.read_csv(file)

    # -------------------------------------
    # Dataset Specific Cleaning
    # -------------------------------------

    if file.name == "02_nav_history.csv":

        df["date"] = pd.to_datetime(df["date"])

        df = df.sort_values(
            ["amfi_code", "date"]
        )

        df = df.drop_duplicates()

        df["nav"] = (
            df.groupby("amfi_code")["nav"]
            .ffill()
        )

    elif file.name == "08_investor_transactions.csv":

        df["transaction_date"] = pd.to_datetime(
            df["transaction_date"]
        )

        df["transaction_type"] = (
            df["transaction_type"]
            .str.strip()
        )

    elif file.name == "07_scheme_performance.csv":

        numeric_cols = [
            "return_1yr_pct",
            "return_3yr_pct",
            "return_5yr_pct",
            "benchmark_3yr_pct",
            "alpha",
            "beta",
            "sharpe_ratio",
            "sortino_ratio",
            "std_dev_ann_pct",
            "max_drawdown_pct"
        ]

        for col in numeric_cols:

            df[col] = pd.to_numeric(
                df[col],
                errors="coerce"
            )

    # -------------------------------------
    # Save Processed File
    # -------------------------------------

    output_file = (
        PROCESSED_DIR /
        f"{file.stem}_clean.csv"
    )

    df.to_csv(
        output_file,
        index=False
    )

    print(
        f"Saved: {output_file.name}"
    )

print("\nAll datasets processed successfully!")

