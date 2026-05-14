import pandas as pd

# Load cleaned dataset
df = pd.read_csv("data/cleaned/cleaned_sales_data.csv")

# Normalize column names
df.columns = df.columns.str.lower()

# KPI Calculations
total_revenue = df['revenue'].sum()

total_quantity = df['quantity'].sum()

average_order_value = df['revenue'].mean()

top_product = df.groupby('product')['revenue'].sum().idxmax()

top_region = df.groupby('region')['revenue'].sum().idxmax()

payment_summary = df.groupby('payment_method')['revenue'].sum()

# Display Results
print("===== KPI ANALYSIS =====")

print("Total Revenue:", total_revenue)

print("Total Quantity Sold:", total_quantity)

print("Average Order Value:", round(average_order_value, 2))

print("Top Product:", top_product)

print("Top Region:", top_region)

print("\nRevenue by Payment Method:")

print(payment_summary)