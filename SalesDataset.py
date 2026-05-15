import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# Load Dataset
# -----------------------------
df = pd.read_csv("SampleSuperstore.csv", encoding="latin1")

# quick look at data
print("First 5 rows:\n", df.head())
print("\nColumns:\n", df.columns)

# -----------------------------
# Data Preprocessing
# -----------------------------
# convert Order Date to datetime
df["Order Date"] = pd.to_datetime(df["Order Date"])

# extract month
df["Month"] = df["Order Date"].dt.month_name()

# -----------------------------
# 1. Monthly Sales Trend
# -----------------------------
monthly_sales = df.groupby("Month")["Sales"].sum()


print("\nMonthly Sales:\n", monthly_sales)

print("\nInsight:")
print("Highest sales month:", monthly_sales.idxmax())
print("Lowest sales month:", monthly_sales.idxmin())
print("\nMonthly Sales:\n", monthly_sales)

plt.figure(figsize=(8,5))
monthly_sales.plot(marker='o')
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.savefig("monthly_sales.png")
plt.grid()
plt.show()

# -----------------------------
# 2. Top 10 Products by Sales
# -----------------------------
top_products = df.groupby("Product Name")["Sales"].sum().sort_values(ascending=False).head(10)

print("\nTop Product:", top_products.idxmax())
print("\nTop 10 Products:\n", top_products)

plt.figure(figsize=(10,5))
top_products.plot(kind="bar")
plt.title("Top 10 Products by Sales")
plt.xlabel("Product Name")
plt.ylabel("Sales")
plt.savefig("top_products.png")
plt.xticks(rotation=45)
plt.show()

# -----------------------------
# 3. Category-wise Sales
# -----------------------------
category_sales = df.groupby("Category")["Sales"].sum()

print("\nCategory-wise Sales:\n", category_sales)
print("\nTop Category:", category_sales.idxmax())
print("\nCategory-wise Sales:\n", category_sales)

plt.figure(figsize=(8,5))
category_sales.plot(kind="bar")
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.savefig("category_sales.png")
plt.show()

# -----------------------------
# 4. Region-wise Sales
# -----------------------------
region_sales = df.groupby("Region")["Sales"].sum()

print("\nRegion-wise Sales:\n", region_sales)

plt.figure(figsize=(8,5))
region_sales.plot(kind="bar")
plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.savefig("region_sales.png")
plt.show()

# -----------------------------
# 5. Profit Analysis
# -----------------------------
profit = df.groupby("Category")["Profit"].sum()

print("\nProfit by Category:\n", profit)

plt.figure(figsize=(8,5))
profit.plot(kind="bar")
plt.title("Profit by Category")
plt.xlabel("Category")
plt.ylabel("Profit")
plt.savefig("profit_analysis.png")
plt.show()