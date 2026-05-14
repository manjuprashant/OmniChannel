import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

# Load cleaned dataset
df = pd.read_csv("data/cleaned/cleaned_sales_data.csv")

# Normalize columns
df.columns = df.columns.str.lower()

# Convert date column
df['order_date'] = pd.to_datetime(df['order_date'])

# Create month feature
df['month'] = df['order_date'].dt.month

# Features and target
X = df[['quantity', 'unit_price', 'month']]
y = df['revenue']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LinearRegression()

model.fit(X_train, y_train)

# Predictions
predictions = model.predict(X_test)

# Evaluation
mae = mean_absolute_error(y_test, predictions)

print("===== SALES FORECASTING =====")

print("Mean Absolute Error:", round(mae, 2))

# Sample predictions
results = pd.DataFrame({
    'Actual Revenue': y_test.values,
    'Predicted Revenue': predictions
})

print("\nSample Predictions:")

print(results.head())