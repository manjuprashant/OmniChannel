import pandas as pd

# Load dataset
df = pd.read_csv("data/raw/sales_dataset.csv")

# Normalize column names
df.columns = df.columns.str.lower()

print("Initial Shape:", df.shape)

# Create revenue column if missing
if 'revenue' not in df.columns:
    df['revenue'] = df['quantity'] * df['unit_price']

# Remove duplicates
df.drop_duplicates(inplace=True)

# Fill numeric columns
numeric_cols = df.select_dtypes(include=['number']).columns
df[numeric_cols] = df[numeric_cols].fillna(0)

# Fill text columns
text_cols = df.select_dtypes(include=['object', 'string']).columns
df[text_cols] = df[text_cols].fillna('Unknown')

# Save cleaned dataset
df.to_csv("data/cleaned/cleaned_sales_data.csv", index=False)

print("Data cleaning completed successfully!")
print("Cleaned Shape:", df.shape)