SET GLOBAL local_infile = 1;

LOAD DATA LOCAL INFILE 'C:/ProgramData/MySQL/MySQL Server 9.7/Uploads/cleaned_sales_data.csv'
INTO TABLE sales_data
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS
(order_id,
 order_date,
 customer_name,
 region,
 salesperson,
 product,
 quantity,
 unit_price,
 total_sales,
 payment_method,
 revenue);
 
 LOAD DATA LOCAL INFILE 'C:/ProgramData/MySQL/MySQL Server 9.7/Uploads/cleaned_sales_data.csv'
INTO TABLE sales_data
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS
(order_id,
 order_date,
 customer_name,
 region,
 salesperson,
 product,
 quantity,
 unit_price,
 total_sales,
 payment_method,
 revenue);
 
 DROP TABLE sales_data;
 
 CREATE TABLE sales_data (
    order_id VARCHAR(20),
    order_date DATE,
    customer_name VARCHAR(100),
    region VARCHAR(50),
    salesperson VARCHAR(100),
    product VARCHAR(100),
    quantity INT,
    unit_price FLOAT,
    total_sales FLOAT,
    payment_method VARCHAR(50),
    revenue FLOAT
);


SELECT COUNT(*) FROM sales_data;
SELECT * FROM sales_data LIMIT 10;

SELECT SUM(revenue) AS total_revenue
FROM sales_data;

SELECT AVG(revenue) AS avg_revenue_per_order
FROM sales_data;



SELECT region,
       SUM(revenue) AS regional_revenue
FROM sales_data
GROUP BY region
ORDER BY regional_revenue DESC;

SELECT salesperson,
       SUM(revenue) AS total_sales
FROM sales_data
GROUP BY salesperson
ORDER BY total_sales DESC;

SELECT payment_method,
       COUNT(*) AS total_orders,
       SUM(revenue) AS total_revenue
FROM sales_data
GROUP BY payment_method;

SELECT MONTH(order_date) AS month,
       SUM(revenue) AS monthly_revenue
FROM sales_data
GROUP BY month
ORDER BY month;

SELECT DAYNAME(order_date) AS weekday,
       SUM(revenue) AS revenue
FROM sales_data
GROUP BY weekday
ORDER BY revenue DESC;