import pandas as pd

# Load dataset
df = pd.read_csv("data/raw/01_fund_master.csv")

print("=" * 60)
print("FUND MASTER ANALYSIS")
print("=" * 60)

# Fund Houses
print("\nNumber of Fund Houses:")
print(df["fund_house"].nunique())

print("\nFund Houses:")
print(sorted(df["fund_house"].unique()))

# Categories
print("\nNumber of Categories:")
print(df["category"].nunique())

print("\nCategories:")
print(sorted(df["category"].unique()))

# Sub Categories
print("\nNumber of Sub-Categories:")
print(df["sub_category"].nunique())

print("\nSub-Categories:")
print(sorted(df["sub_category"].unique()))

# Risk Categories
print("\nNumber of Risk Categories:")
print(df["risk_category"].nunique())

print("\nRisk Categories:")
print(sorted(df["risk_category"].unique()))














