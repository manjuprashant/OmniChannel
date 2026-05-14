import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned dataset
df = pd.read_csv("data/cleaned/cleaned_sales_data.csv")

# Total Revenue
total_revenue = df['revenue'].sum()
print("Total Revenue:", total_revenue)

# Top Selling Products
top_products = df.groupby('product')['quantity'].sum().sort_values(ascending=False).head(10)

print(top_products)

# Revenue by City
region_revenue = df.groupby('region')['revenue'].sum().sort_values(ascending=False)

print(region_revenue)

# Convert order_date to datetime
df['order_date'] = pd.to_datetime(df['order_date'])

# Extract month
df['month'] = df['order_date'].dt.month
# Plot Revenue by Month
monthly_sales = df.groupby('month')['revenue'].sum()

plt.figure(figsize=(10, 5))
sns.lineplot(x=monthly_sales.index, y=monthly_sales.values, marker='o')

plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")

plt.savefig("data/cleaned/monthly_sales.png")
print("Chart saved successfully!")