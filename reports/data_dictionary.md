


Bluestock Mutual Fund Analytics Project

Enterprise Data Dictionary

Project: Bluestock Mutual Fund Analytics Platform
Version: 1.0
Prepared By: Jaydeep Dhurat
Database: bluestock_mf.db
Prepared Date: June 2026

1) Purpose

This document provides detailed metadata, business definitions, source references, and data quality standards for all datasets used within the Bluestock Mutual Fund Analytics Project.

2) Table Dictionary
Table: 01_fund_master
Business Description

Master reference table containing scheme-level metadata for all mutual funds.

Source

Internal Fund Master Dataset

Grain

One record per AMFI Scheme Code

Primary Key

amfi_code

Data Quality Rules:

1) AMFI code must be unique
2) Scheme name cannot be null
3) Expense ratio must be positive
4) Risk category must be valid

Columns:

Column Name	Data Type	Business Definition
amfi_code	INTEGER	Unique scheme identifier assigned by AMFI
fund_house	TEXT	Asset Management Company name
scheme_name	TEXT	Official scheme name
category	TEXT	Broad category classification
sub_category	TEXT	Detailed category classification
plan	TEXT	Direct or Regular plan
launch_date	DATE	Scheme launch date
benchmark	TEXT	Benchmark index
expense_ratio_pct	DECIMAL	Annual expense ratio percentage
exit_load_pct	DECIMAL	Exit load percentage
min_sip_amount	INTEGER	Minimum SIP amount
min_lumpsum_amount	INTEGER	Minimum lump-sum investment
fund_manager	TEXT	Assigned fund manager
risk_category	TEXT	Risk classification
sebi_category_code	TEXT	SEBI category identifier


Table: 02_nav_history

Business Description

Historical Net Asset Value records for mutual fund schemes.

Source

Historical NAV Dataset

Grain

One record per Scheme per Date

Primary Key

(amfi_code, date)

Data Quality Rules

1) NAV must be greater than zero
2) No duplicate scheme-date combinations
3) Date must be valid

Columns

Column Name	Data Type	Business Definition

amfi_code	INTEGER	AMFI scheme identifier
date	DATE	NAV reporting date
nav	DECIMAL	Net Asset Value per unit

Table: 03_aum_by_fund_house
Business Description

Asset Under Management statistics at fund-house level.

Source

AUM Industry Dataset

Grain

One record per Fund House per Reporting Date

Primary Key

(date, fund_house)

Data Quality Rules

1) AUM values must be positive
2) Fund house name cannot be null

Columns
Column Name	Data Type	Business Definition
date	DATE	Reporting date
fund_house	TEXT	Asset Management Company
aum_lakh_crore	DECIMAL	Total AUM in lakh crore
aum_crore	INTEGER	Total AUM in crore
num_schemes	INTEGER	Number of active schemes

Table: 04_monthly_sip_inflows
Business Description

Monthly SIP industry statistics and growth metrics.

Source

SIP Industry Dataset

Grain

One record per Month

Primary Key

month

Data Quality Rules

1) SIP inflow must be positive
2) Growth percentage should be numeric


Columns

Column Name	Data Type	Business Definition
month	DATE	Reporting month
sip_inflow_crore	DECIMAL	Monthly SIP inflow
active_sip_accounts_crore	DECIMAL	Active SIP accounts
new_sip_accounts_lakh	DECIMAL	Newly registered SIP accounts
sip_aum_lakh_crore	DECIMAL	SIP assets under management
yoy_growth_pct	DECIMAL	Year-over-year growth percentage


Table: 05_category_inflows
Business Description

Net inflow and outflow trends across mutual fund categories.

Source

Category Inflow Dataset

Grain

One record per Category per Month

Primary Key

(month, category)

Data Quality Rules

1) Category name must exist
2) Inflow values must be numeric

Columns

Column Name	Data Type	Business Definition
month	DATE	Reporting month
category	TEXT	Mutual fund category
inflow_crore	DECIMAL	Net category inflow/outflow

Table: 06_industry_folio_count
Business Description

Industry-wide investor folio statistics.

Source

Industry Folio Dataset

Grain

One record per Reporting Date

Primary Key

date

Data Quality Rules

1) Folio counts must be positive
2) Date must be valid

Columns

Column Name	Data Type	Business Definition
date	DATE	Reporting date
equity_folios_lakh	DECIMAL	Equity fund folios
debt_folios_lakh	DECIMAL	Debt fund folios
hybrid_folios_lakh	DECIMAL	Hybrid fund folios
other_folios_lakh	DECIMAL	Other fund folios
total_folios_lakh	DECIMAL	Total investor folios

Table: 07_scheme_performance
Business Description

Performance and risk metrics at scheme level.

Source

Scheme Performance Dataset

Grain

One record per Scheme

Primary Key

amfi_code

Data Quality Rules

1) Returns must be numeric
2) Expense ratio must be between 0.1% and 2.5%
3) Risk metrics must not be null


Columns
Column Name	Data Type	Business Definition
amfi_code	INTEGER	Scheme identifier
scheme_name	TEXT	Scheme name
fund_house	TEXT	Fund house
category	TEXT	Fund category
plan	TEXT	Plan type
return_1yr_pct	DECIMAL	1-year return
return_3yr_pct	DECIMAL	3-year return
return_5yr_pct	DECIMAL	5-year return
benchmark_3yr_pct	DECIMAL	Benchmark return
alpha	DECIMAL	Alpha measure
beta	DECIMAL	Beta measure
sharpe_ratio	DECIMAL	Sharpe ratio
sortino_ratio	DECIMAL	Sortino ratio
std_dev_ann_pct	DECIMAL	Annualized volatility
max_drawdown_pct	DECIMAL	Maximum drawdown
aum_crore	INTEGER	Assets under management
expense_ratio_pct	DECIMAL	Expense ratio
morningstar_rating	INTEGER	Morningstar rating
risk_grade	TEXT	Risk classification

Table: 08_investor_transactions
Business Description

Investor-level transaction records.

Source

Investor Transaction Dataset

Grain

One record per Transaction

Primary Key

(investor_id, transaction_date, amfi_code)

Data Quality Rules

1) Transaction amount must be positive
2) KYC status must be valid
3) Transaction type must be standardized

Columns
Column Name	Data Type	Business Definition
investor_id	TEXT	Unique investor identifier
transaction_date	DATE	Transaction date
amfi_code	INTEGER	Scheme identifier
transaction_type	TEXT	SIP, Lumpsum, Redemption
amount_inr	INTEGER	Transaction amount
state	TEXT	Investor state
city	TEXT	Investor city
city_tier	TEXT	Tier classification
age_group	TEXT	Investor age segment
gender	TEXT	Investor gender
annual_income_lakh	DECIMAL	Annual income
payment_mode	TEXT	Payment method
kyc_status	TEXT	KYC verification status

Table: 09_portfolio_holdings
Business Description

Scheme-level equity portfolio holdings.

Source

Portfolio Holdings Dataset

Grain

One record per Scheme per Security

Primary Key

(amfi_code, stock_symbol)

Data Quality Rules
Weight percentage must be positive
Security name cannot be null
Columns
Column Name	Data Type	Business Definition
amfi_code	INTEGER	Scheme identifier
stock_symbol	TEXT	Security ticker
stock_name	TEXT	Company name
sector	TEXT	Industry sector
weight_pct	DECIMAL	Portfolio allocation percentage
market_value_cr	DECIMAL	Market value
current_price_inr	DECIMAL	Security market price
portfolio_date	DATE	Portfolio reporting date
Table: 10_benchmark_indices
Business Description

Historical benchmark index performance records.

Source

Benchmark Index Dataset

Grain

One record per Index per Date

Primary Key

(index_name, date)

Data Quality Rules
Index value must be positive
Date must be valid
Columns
Column Name	Data Type	Business Definition
index_name	TEXT	Benchmark index name
date	DATE	Reporting date
index_value	DECIMAL	Index closing value


3) Data Governance & Validation Controls

The following validations were performed during ingestion and processing:

Duplicate record identification and removal
Missing value assessment
Date standardization
Data type validation
AMFI code referential integrity validation
NAV positivity checks
Expense ratio range validation
Transaction amount validation
KYC status validation
SQLite load verification

4) Data Refresh Strategy

Dataset	Refresh Frequency
NAV History	Daily
Live NAV API	Real-Time
Scheme Performance	Monthly
AUM Statistics	Monthly
SIP Statistics	Monthly
Investor Transactions	Daily
Portfolio Holdings	Monthly

5) Document Approval

Prepared For: Bluestock Internship Capstone Project
Prepared By: Jaydeep Dhurat
