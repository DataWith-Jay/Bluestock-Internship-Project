import pandas as pd

# Load dataset
df = pd.read_csv("data/raw/02_nav_history.csv")

print("=" * 60)
print("NAV HISTORY CLEANING")
print("=" * 60)

print(f"Original Rows: {len(df)}")

# Convert date
df["date"] = pd.to_datetime(df["date"])

# Sort
df = df.sort_values(
    ["amfi_code", "date"]
)

# Remove duplicates
duplicates = df.duplicated().sum()

print(f"Duplicates Found: {duplicates}")

df = df.drop_duplicates()

# Check missing NAV values before fill
missing_before = df["nav"].isna().sum()

print(f"Missing NAV Before Fill: {missing_before}")

# Forward fill NAV
df["nav"] = (
    df.groupby("amfi_code")["nav"]
    .ffill()
)

# Check missing NAV values after fill
missing_after = df["nav"].isna().sum()

print(f"Missing NAV After Fill: {missing_after}")

# Validate NAV > 0
invalid_nav = (df["nav"] <= 0).sum()

print(f"Invalid NAV Records: {invalid_nav}")

# Save processed file
output_path = "data/processed/02_nav_history_clean.csv"

df.to_csv(
    output_path,
    index=False
)

print(f"Saved: {output_path}")
print(f"Final Rows: {len(df)}")




