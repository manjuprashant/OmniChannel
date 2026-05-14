import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
df = pd.read_csv("data/cleaned/cleaned_sales_data.csv")

# Normalize columns
df.columns = df.columns.str.lower()

# Revenue by product
product_sales = df.groupby('product')['revenue'].sum()

# Plot chart
product_sales.plot(kind='bar')

plt.title("Revenue by Product")

plt.xlabel("Product")

plt.ylabel("Revenue")

plt.xticks(rotation=45)

# Save chart
plt.savefig("data/cleaned/product_revenue_chart.png")

print("Visualization created successfully!")