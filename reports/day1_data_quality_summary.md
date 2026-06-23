### Day 1 Data Quality Summary

## Dataset Overview

A total of 10 CSV datasets were successfully loaded and profiled using Pandas.

Datasets include:

1) Fund Master
2) NAV History
3) AUM by Fund House
4) Monthly SIP Inflows
5) Category Inflows
6) Industry Folio Count
7) Scheme Performance
8) Investor Transactions
9) Portfolio Holdings
10) Benchmark Indices

## Data Profiling Findings

1) All datasets were successfully loaded without errors.
2) Dataset structures, row counts, column counts, and data types were verified.
3) First five records of each dataset were inspected.
4) No missing values were detected in the provided datasets.

## Observed Anomalies

1) Date-related columns such as launch_date, date, transaction_date, and portfolio_date are currently stored as string data types.
2) These columns will be converted to proper datetime format during the ETL process before database loading and analysis.

## Fund Master Exploration

1) Total Fund Houses: 10
2) Total Categories: 2 (Equity, Debt)
3) Total Sub-Categories: 12
4) Total Risk Categories: 5

## AMFI Code Validation

Validation was performed between:

1) 01_fund_master.csv
2) 02_nav_history.csv

Results:

1) Fund Master Codes: 40
2) NAV History Codes: 40
3) All AMFI codes present in fund_master were found in nav_history.

No data integrity issues were identified.

## API Data Collection

Live NAV data was successfully fetched from mfapi.in.

NAV history was collected for:

1) SBI Bluechip
2) ICICI Bluechip
3) Nippon Large Cap
4) Axis Bluechip
5) Kotak Bluechip

Data was saved as CSV files under the raw data directory.

## Conclusion

The datasets passed initial ingestion and validation checks and are ready for the next phase of ETL (Extraction, Transformation & Loading) processing, database modeling, SQL analysis, and dashboard development.
