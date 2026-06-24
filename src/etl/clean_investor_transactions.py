import pandas as pd

df = pd.read_csv(
    "data/raw/08_investor_transactions.csv"
)

print("=" * 60)
print("INVESTOR TRANSACTION CLEANING")
print("=" * 60)

print(f"Original Rows: {len(df)}")

# Convert date
df["transaction_date"] = pd.to_datetime(
    df["transaction_date"]
)

df["transaction_type"] = (
    df["transaction_type"]
    .str.strip()
    .replace({
        "SIP": "SIP",
        "Sip": "SIP",
        "sip": "SIP",
        "Lumpsum": "Lumpsum",
        "Redemption": "Redemption"
    })
)

print("\nTransaction Types:")
print(
    df["transaction_type"]
    .value_counts()
)

# Validate amount
invalid_amounts = (
    df["amount_inr"] <= 0
).sum()

print(f"\nInvalid Amount Records: {invalid_amounts}")

# Validate KYC
print("\nKYC Status Values:")
print(
    df["kyc_status"]
    .value_counts()
)

# Save
output_path = (
    "data/processed/"
    "08_investor_transactions_clean.csv"
)

df.to_csv(
    output_path,
    index=False
)

print(f"\nSaved: {output_path}")
print(f"Final Rows: {len(df)}")


