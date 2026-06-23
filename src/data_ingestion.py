## Data Ingestion Validation File.





from pathlib import Path       ## Python's built-in library for working with folders and files.  
import pandas as pd 

""" Pandas A Python library used for:

Reading CSV files
Cleaning data
Analyzing data
Transforming data"""



RAW_DATA_DIR = Path("data/raw") ## Creating a variable inside the project
print("=" * 50)                    ## Python repeats the character 50 times, basically used for the seperation line
print("Bluestock Data Ingestion") 
print("=" * 50)


csv_files = list(RAW_DATA_DIR.glob("*.csv"))  ## find all files ending with .csv and then convert results into list.



print(f"\nFound {len(csv_files)} CSV files\n")  ## It is counting the number of csv files

for file in csv_files:                         ## Loop through every csv files
    try:                                       ## If something fails in between then dont crash
        df = pd.read_csv(file)                 ## Reads CSV into dataframe.
        print("-" * 50)
        print(f"Filename:{file.name}")         ## Extracts only the filename.
        print(f"Rows:{df.shape[0]}")           ## It will return rows and columns.
        print(f"Columns:{df.shape[1]}")
        print(f"Size:{round(file.stat().st_size / (1024*1024),2)}MB")  ## file.stat() gets the metadata about the file.
        print("-" * 50)

    except Exception as e:
        print(f"error reading {file.name}:{e}")

