# Swiggy Sales & Customer Analytics - End-to-End Data Analytics Project

An end-to-end analytics project on Swiggy restaurant, city and customer data:
data collection, cleaning, SQL/Python analysis, a 5-page Power BI dashboard,
business insights and recommendations.

## 1. Business Problem
Swiggy's business team needs to know where sales come from, who the most
valuable customers are, and which cities and cuisines to prioritise.
The project answers:
1. Which cities and restaurants drive the most sales, users and ratings?
2. Who are the core customers (age, gender, occupation, marital status)?
3. How have sales and quantity changed year over year (2017-2020)?
4. How do Veg, Non-Veg and Other categories compare on volume and price?
5. How concentrated is revenue in the top 10% of customers?

## 2. Dataset
- Source: Swiggy restaurant / order / user dataset  (ADD LINK HERE)
- Coverage: about 149K records, 821 cities, years 2017-2020
- Key fields: City, Restaurant Name, Cuisine, Rating, Rating Count, Price,
  Veg/Non-Veg, Sales (Amount), Quantity, Year, User Age, Gender,
  Marital Status, Occupation

## 3. Tools Used
| Stage            | Tool                     |
|------------------|--------------------------|
| Cleaning         | Python (Pandas) / Excel  |
| Analysis         | SQL, Python              |
| Visualisation    | Power BI (DAX measures)  |
| Documentation    | Markdown, PDF, GitHub    |

## 4. Workflow
Raw data -> Cleaning -> EDA -> SQL/Python analysis -> Power BI -> Insights
-> Report -> GitHub.

## 5. Dashboard Pages
1. Overview - orders, users, avg price by Veg/Non-Veg/Others, top 10 cities,
   quantity by year
2. User Performance - age, gender, marital status, occupation, year slicer
3. City Overview - sales, users and ratings by city, city slicer
4. Restaurant Analysis - veg vs non-veg mix, cuisines, top restaurants
5. Insights - written findings and recommendations

## 6. Key Insights
- Tirupati leads sales (43M), followed by Electronic City, Bangalore (29M).
- Customers aged 21-25 (mostly students) are the largest user group.
- Veg options lead on sales; Non-Veg has the higher average price.
- Sales grew sharply in 2018 and declined in 2019 and 2020.
- Revenue is heavily concentrated in the top 10% of customers.

## 7. Recommendations
1. Run targeted campaigns for the 21-25 student segment.
2. Launch a VIP programme for top-spending customers.
3. Offer discounts to attract more female customers.
4. Expand partnerships in high-sales cities (Tirupati, Raipur, Bangalore).
5. Investigate the post-2018 decline before scaling marketing spend.

## 8. Repository Structure
```
swiggy-analytics/
|-- data/
|   |-- raw/                 original dataset
|   |-- cleaned/             cleaned dataset (CSV)
|-- notebooks/               EDA notebook
|-- sql/                     analysis queries
|-- python/                  clean_and_eda.py
|-- powerbi/                 swiggy_project.pbix
|-- screenshots/             dashboard pages (PNG)
|-- reports/                 final PDF report
|-- README.md
```

## 9. How to Run
1. Place the raw file in data/raw/.
2. Run: python python/clean_and_eda.py
3. Load the cleaned CSV into your SQL database and run sql/analysis.sql.
4. Open powerbi/swiggy_project.pbix and refresh the data source.

## 10. Author
Akshara Deshmukh - Data Analyst Intern, Davine Technologies
GitHub: https://github.com/aksharadeshmukh1311-crypto/swiggy-analytics
