import pandas as pd

df = pd.read_csv(
    "data/raw/07_scheme_performance.csv"
)

print("=" * 60)
print("SCHEME PERFORMANCE CLEANING")
print("=" * 60)

print(f"Original Rows: {len(df)}")

# Return columns
return_cols = [
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

# Validate numeric
for col in return_cols:
    df[col] = pd.to_numeric(
        df[col],
        errors="coerce"
    )

# Check missing after conversion
print("\nMissing Values After Numeric Conversion:")

print(
    df[return_cols]
    .isna()
    .sum()
)

# Expense ratio validation
invalid_expense = (
    (df["expense_ratio_pct"] < 0.1)
    |
    (df["expense_ratio_pct"] > 2.5)
).sum()

print(
    f"\nExpense Ratio Anomalies: "
    f"{invalid_expense}"
)

# Save cleaned data
output_path = (
    "data/processed/"
    "07_scheme_performance_clean.csv"
)

df.to_csv(
    output_path,
    index=False
)

print(f"\nSaved: {output_path}")
print(f"Final Rows: {len(df)}")

