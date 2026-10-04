"""Swiggy project - data cleaning and EDA.
Adjust the COLS mapping to match the column names in your raw file."""
import pandas as pd

RAW = "data/raw/swiggy_raw.csv"
OUT = "data/cleaned/swiggy_cleaned.csv"

# Left: name used below | Right: name in YOUR raw file (edit these)
COLS = {
    "city": "City", "restaurant": "Name", "cuisine": "Cuisine",
    "rating": "Rating", "rating_count": "Rating_Count", "price": "Price",
    "diet": "Veg_or_Non_Veg", "sales": "Sales", "quantity": "Quantity",
    "year": "Year", "age": "Age", "gender": "Gender",
    "marital": "Marital_Status", "occupation": "Occupation",
    "user_id": "User_ID",
}

df = pd.read_csv(RAW)
df = df.rename(columns={v: k for k, v in COLS.items() if v in df.columns})
print("Raw shape:", df.shape)

# 1. Standardise text columns
for c in ["city", "restaurant", "cuisine", "diet", "gender",
          "marital", "occupation"]:
    if c in df.columns:
        df[c] = df[c].astype(str).str.strip().str.title()

# 2. Fix data types
for c in ["rating", "rating_count", "price", "sales", "quantity", "age"]:
    if c in df.columns:
        df[c] = pd.to_numeric(df[c], errors="coerce")

# 3. Missing values and duplicates
print("Missing values:\n", df.isna().sum())
df = df.drop_duplicates()
df = df.dropna(subset=["city", "sales"])
if "rating" in df.columns:
    df["rating"] = df["rating"].fillna(df["rating"].median())

# 4. Remove invalid records
df = df[(df["sales"] >= 0) & (df["price"] >= 0)]
df = df[df["age"].between(10, 90) | df["age"].isna()]

# 5. Outlier check (IQR) on sales - flag, do not delete blindly
q1, q3 = df["sales"].quantile([0.25, 0.75])
iqr = q3 - q1
df["sales_outlier"] = ~df["sales"].between(q1 - 1.5 * iqr, q3 + 1.5 * iqr)
print("Sales outliers flagged:", int(df["sales_outlier"].sum()))

df.to_csv(OUT, index=False)
print("Cleaned shape:", df.shape)

# ---------------- EDA ----------------
print("\nTop 10 cities by sales")
print(df.groupby("city")["sales"].sum().nlargest(10))

print("\nQuantity by year")
qty = df.groupby("year")["quantity"].sum()
print(qty)
print("YoY % change:\n", (qty.pct_change() * 100).round(1))

print("\nAvg price and count by diet type")
print(df.groupby("diet").agg(count=("price", "size"),
                             avg_price=("price", "mean")).round(2))

print("\nUsers by age (top 10)")
print(df.groupby("age")["user_id"].nunique().nlargest(10))

print("\nSales by occupation and gender")
print(df.groupby("occupation")["sales"].sum().sort_values(ascending=False))
print(df.groupby("gender")["sales"].sum())

# Top 10% customers share of sales (Pareto check)
cust = df.groupby("user_id")["sales"].sum().sort_values(ascending=False)
top_n = max(1, int(len(cust) * 0.10))
share = cust.head(top_n).sum() / cust.sum() * 100
print(f"\nTop 10% customers contribute {share:.1f}% of total sales")
