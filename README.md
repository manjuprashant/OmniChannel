# Omnichannel Retail Analytics Dashboard

## Project Overview

The Omnichannel Retail Analytics Dashboard project focuses on analyzing retail sales data using MySQL and Microsoft Power BI to generate actionable business insights. The dashboard provides interactive visualizations for sales trends, product performance, payment analysis, and KPI monitoring.

The project was developed as part of a Data Analytics Internship Program and demonstrates Business Intelligence dashboard development using SQL and Power BI.

---

## Technologies Used

- MySQL Workbench
- Microsoft Power BI Desktop
- Microsoft Excel
- CSV Dataset
- SQL

---

## Dataset Description

The dataset contains retail sales transaction records including:

- Order ID
- Order Date
- Customer Name
- Product
- Quantity
- Unit Price
- Total Sales
- Payment Method
- Sales Channel
- Store Type
- Platform
- Delivery Type

The dataset was cleaned and processed before visualization.

---

## Project Objectives

- Analyze retail sales trends
- Track product performance
- Monitor KPI metrics
- Generate business insights
- Build interactive Power BI dashboards
- Implement filters and slicers for drill-down analysis

---

## Database Setup

### Step 1: Create Database
sql
CREATE DATABASE retail_dashboard;
USE retail_dashboard;


### Step 2: Create table


CREATE TABLE sales_data (
    order_id VARCHAR(50),
    order_date DATE,
    customer_name VARCHAR(100),
    product VARCHAR(100),
    quantity INT,
    unit_price DECIMAL(10,2),
    total_sales DECIMAL(10,2),
    payment_method VARCHAR(50),
    sales_channel VARCHAR(50),
    store_type VARCHAR(50),
    platform VARCHAR(50),
    delivery_type VARCHAR(50)
);


### Step 3: Import CSV file


LOAD DATA LOCAL INFILE 'C:/mysqlfiles/cleaned_sales_data.csv'
INTO TABLE sales_data
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS;


Power BI Dashboard Components
KPI Cards
Total Revenue
Total Orders
Total Quantity Sold
Charts and Visualizations
Line Chart for Sales Trends
Bar Chart for Product Performance
Pie Chart for Payment Method Analysis
Heatmap using Matrix Visual
Interactive Slicers and Filters
Key Business Insights
High-performing products contributed the majority of total revenue.
Digital payment methods generated higher transaction volumes.
Sales trends showed consistent growth across reporting periods.
Heatmap analysis identified strong product-payment combinations.
KPI metrics provided real-time business performance tracking.
Strategic Recommendations
Increase promotions for top-performing products.
Focus marketing campaigns on high-revenue customer segments.
Improve inventory planning using sales trend analysis.
Expand digital payment incentives.
Use dashboard monitoring for strategic decision-making.
Dashboard Screenshots

Add screenshots of:

Main Dashboard
KPI Cards
Heatmap Visualization
Product Performance Analysis
Sales Trend Charts
Repository Structure
OmniChannel/
│
├── dataset/
├── sql/
├── powerbi/
├── screenshots/
├── reports/
└── README.md
How to Run the Project
Install MySQL Workbench
Import the cleaned CSV dataset
Execute SQL table creation scripts
Connect Power BI to MySQL or CSV dataset
Create dashboard visualizations
Apply slicers and filters
Final Deliverables
Interactive Power BI Dashboard
SQL Database Setup
Heatmap Visualization
KPI Analysis
Business Insights Report
GitHub Repository Documentation
Conclusion

This project demonstrates the practical implementation of Business Intelligence and Data Analytics concepts using MySQL and Power BI. The dashboard transforms raw retail data into actionable insights for improved business decision-making.

Author

Manjula Srinivasan

Data Analytics Internship Project



```sql
CREATE DATABASE retail_dashboard;
USE retail_dashboard;
