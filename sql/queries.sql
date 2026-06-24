/*
=========================================================
Bluestock Mutual Fund Analytics Project
Day 2 Deliverable
Analytical SQL Queries

Author : Jaydeep Dhurat
Database : bluestock_mf.db
=========================================================
*/












-- =====================================================
-- Query 1 : Top 5 Fund Houses by AUM
-- =====================================================


SELECT
    fund_house,
    aum_crore
FROM 03_aum_by_fund_house
ORDER BY aum_crore DESC
LIMIT 5;

-- =====================================================
-- Query 2 : Average NAV Per Month
-- =====================================================

SELECT
    strftime('%Y-%m', date) AS month,
    ROUND(AVG(nav), 2) AS avg_nav
FROM "02_nav_history"
GROUP BY month
ORDER BY month;



-- =====================================================
-- Query 3 : SIP Year-over-Year Growth Analysis
-- =====================================================

SELECT
    month,
    sip_inflow_crore,
    ROUND(yoy_growth_pct, 2) AS yoy_growth_pct
FROM "04_monthly_sip_inflows"
WHERE yoy_growth_pct IS NOT NULL
ORDER BY yoy_growth_pct DESC;

-- =====================================================
-- Query 4 : Transactions and Investment Amount by State
-- =====================================================

SELECT
    state,
    COUNT(*) AS total_transactions,
    ROUND(SUM(amount_inr), 2) AS total_investment
FROM "08_investor_transactions"
GROUP BY state
ORDER BY total_investment DESC;


-- =====================================================
-- Query 5 : Funds with Expense Ratio Less Than 1%
-- =====================================================

SELECT
    scheme_name,
    fund_house,
    category,
    expense_ratio_pct
FROM "07_scheme_performance"
WHERE expense_ratio_pct < 1
ORDER BY expense_ratio_pct ASC;



-- =====================================================
-- Query 6 : Top 10 Funds by 5-Year Return
-- =====================================================

SELECT
    scheme_name,
    fund_house,
    category,
    return_5yr_pct
FROM "07_scheme_performance"
ORDER BY return_5yr_pct DESC
LIMIT 10;


-- =====================================================
-- Query 7 : Fund Count by Category
-- =====================================================

SELECT
    category,
    COUNT(*) AS fund_count
FROM "01_fund_master"
GROUP BY category
ORDER BY fund_count DESC;


-- =====================================================
-- Query 8 : Investor Distribution by City Tier
-- =====================================================

SELECT
    city_tier,
    COUNT(DISTINCT investor_id) AS total_investors
FROM "08_investor_transactions"
GROUP BY city_tier
ORDER BY total_investors DESC;


-- =====================================================
-- Query 9 : Average Annual Income by Age Group
-- =====================================================

SELECT
    age_group,
    ROUND(AVG(annual_income_lakh), 2) AS avg_income_lakh
FROM "08_investor_transactions"
GROUP BY age_group
ORDER BY avg_income_lakh DESC;


-- =====================================================
-- Query 10 : Portfolio Allocation by Sector
-- =====================================================

SELECT
    sector,
    ROUND(SUM(weight_pct), 2) AS total_weight_pct
FROM "09_portfolio_holdings"
GROUP BY sector
ORDER BY total_weight_pct DESC;



