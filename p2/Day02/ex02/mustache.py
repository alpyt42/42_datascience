import psycopg2
import pandas as pd
import matplotlib.pyplot as plt

# Replace these with your actual database connection details
hostname = 'localhost'
database = 'piscineds'
username = 'your_login'  # Replace with your actual username
password = 'mysecretpassword'  # Replace with your actual password
port_id = 5432

# Establish a connection to the database
conn = psycopg2.connect(
    host=hostname,
    dbname=database,
    user=username,
    password=password,
    port=port_id
)

# Execute a query to get the prices of purchased items
query_price = "SELECT price FROM customers WHERE event_type = 'purchase';"
df_price = pd.read_sql_query(query_price, conn)

# Execute another query to get the average basket price per user
query_avg_price = """
SELECT user_id, AVG(price) AS avg_basket_price
FROM customers
WHERE event_type = 'purchase'
GROUP BY user_id;
"""
df_avg_price = pd.read_sql_query(query_avg_price, conn)

# Close the connection
conn.close()

# Print descriptive statistics for individual item prices
print(df_price['price'].describe())

# Calculate and print the quartiles explicitly for item prices
quartiles_price = df_price['price'].quantile([0.25, 0.5, 0.75])
print(f"First quartile (25%): {quartiles_price[0.25]}")
print(f"Median (50%): {quartiles_price[0.5]}")
print(f"Third quartile (75%): {quartiles_price[0.75]}")

# Create a box plot for the individual item prices
plt.figure(figsize=(10, 6))
plt.boxplot(df_price['price'], vert=False)
plt.title('Box Plot of Item Prices')
plt.xlabel('Price (Altairian Dollars)')
plt.show()

# Print descriptive statistics for the average basket price per user
print(df_avg_price['avg_basket_price'].describe())

# Calculate and print the quartiles explicitly for the average basket price
quartiles_avg_price = df_avg_price['avg_basket_price'].quantile([0.25, 0.5, 0.75])
print(f"First quartile (25%): {quartiles_avg_price[0.25]}")
print(f"Median (50%): {quartiles_avg_price[0.5]}")
print(f"Third quartile (75%): {quartiles_avg_price[0.75]}")

# Create a box plot for the average basket price per user
plt.figure(figsize=(10, 6))
plt.boxplot(df_avg_price['avg_basket_price'].dropna(), vert=False)  # Drop NaN values if any
plt.title('Box Plot of Average Basket Price per User')
plt.xlabel('Average Basket Price (Altairian Dollars)')
plt.show()
