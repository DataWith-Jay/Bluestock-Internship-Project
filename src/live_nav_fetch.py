import requests
import pandas as pd
from pathlib import Path

# Scheme codes provided by internship manager
schemes = {
    "119551": "SBI_Bluechip",
    "120503": "ICICI_Bluechip",
    "118632": "Nippon_Large_Cap",
    "119092": "Axis_Bluechip",
    "120841": "Kotak_Bluechip"
}

# Output folder
output_dir = Path("data/raw/live_nav")
output_dir.mkdir(parents=True, exist_ok=True)

print("=" * 60)
print("FETCHING LIVE NAV DATA")
print("=" * 60)

for amfi_code, scheme_name in schemes.items():

    url = f"https://api.mfapi.in/mf/{amfi_code}"

    print(f"\nFetching {scheme_name} ({amfi_code})...")

    response = requests.get(url)

    if response.status_code == 200:

        data = response.json()

        nav_df = pd.DataFrame(data["data"])

        output_file = output_dir / f"{scheme_name}.csv"

        nav_df.to_csv(output_file, index=False)

        print(f"Saved: {output_file}")
        print(f"Rows: {len(nav_df)}")

    else:
        print(f"Failed for {amfi_code}")

print("\nAll NAV files downloaded successfully!")

