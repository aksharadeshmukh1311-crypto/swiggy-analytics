-- Swiggy project - analysis queries (MySQL / PostgreSQL compatible).
-- Table: swiggy_data(city, restaurant_name, cuisine, rating, rating_count,
--   price, veg_nonveg, sales, quantity, order_year, user_id, age, gender,
--   marital_status, occupation)   -- rename to match your table

-- 1. Top 10 cities by sales
SELECT city, SUM(sales) AS total_sales, COUNT(*) AS orders
FROM swiggy_data GROUP BY city
ORDER BY total_sales DESC LIMIT 10;

-- 2. Year-over-year sales growth
WITH yearly AS (
  SELECT order_year, SUM(sales) AS total_sales
  FROM swiggy_data GROUP BY order_year)
SELECT order_year, total_sales,
  ROUND(100.0 * (total_sales - LAG(total_sales) OVER (ORDER BY order_year))
        / LAG(total_sales) OVER (ORDER BY order_year), 1) AS yoy_pct
FROM yearly ORDER BY order_year;

-- 3. Veg vs Non-Veg: volume, sales, average price
SELECT veg_nonveg, COUNT(*) AS records, SUM(sales) AS total_sales,
       ROUND(AVG(price), 2) AS avg_price
FROM swiggy_data GROUP BY veg_nonveg;

-- 4. Users by age group
SELECT CASE WHEN age < 18 THEN 'Under 18'
            WHEN age BETWEEN 18 AND 20 THEN '18-20'
            WHEN age BETWEEN 21 AND 25 THEN '21-25'
            WHEN age BETWEEN 26 AND 30 THEN '26-30'
            ELSE '31+' END AS age_group,
       COUNT(DISTINCT user_id) AS users, SUM(sales) AS total_sales
FROM swiggy_data GROUP BY 1 ORDER BY users DESC;

-- 5. Sales by gender and occupation
SELECT gender, occupation, SUM(sales) AS total_sales
FROM swiggy_data GROUP BY gender, occupation
ORDER BY total_sales DESC;

-- 6. Top 10% customers: share of total sales
WITH cust AS (
  SELECT user_id, SUM(sales) AS s,
         NTILE(10) OVER (ORDER BY SUM(sales) DESC) AS decile
  FROM swiggy_data GROUP BY user_id)
SELECT ROUND(100.0 * SUM(CASE WHEN decile = 1 THEN s END) / SUM(s), 1)
       AS top10pct_share
FROM cust;

-- 7. Top 5 cuisines by restaurant count
SELECT cuisine, COUNT(DISTINCT restaurant_name) AS restaurants
FROM swiggy_data GROUP BY cuisine ORDER BY restaurants DESC LIMIT 5;

-- 8. Cities with the highest user and rating counts
SELECT city, COUNT(DISTINCT user_id) AS users, SUM(rating_count) AS ratings
FROM swiggy_data GROUP BY city ORDER BY users DESC LIMIT 10;
