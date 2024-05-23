import pandas as pd
import numpy as np

# Simulation settings
np.random.seed(42)
num_stores = 50
num_days_before = 30
num_days_after = 30
num_customers = 1000

# Simulation dates
dates_before = pd.date_range(start='2019-12-01', periods=num_days_before, freq='D')
dates_after = pd.date_range(start='2020-01-01', periods=num_days_after, freq='D')

# Sales simulation before the campaign
sales_before = []
for date in dates_before:
    for store in range(1, num_stores + 1):
        customer_id = np.random.randint(1, num_customers + 1)
        sales = np.random.normal(loc=500, scale=50)  # Average sales before the campaign
        sales_before.append([date, store, customer_id, sales])

# Sales simulation after the campaign
sales_after = []
for date in dates_after:
    for store in range(1, num_stores + 1):
        customer_id = np.random.randint(1, num_customers + 1)
        sales = np.random.normal(loc=550, scale=60)  # Average sales after the campaign (increase due to campaign)
        sales_after.append([date, store, customer_id, sales])

# Convert to DataFrame
df_sales_before = pd.DataFrame(sales_before, columns=['date', 'store_id', 'customer_id', 'sales'])
df_sales_after = pd.DataFrame(sales_after, columns=['date', 'store_id', 'customer_id', 'sales'])

# Store characteristics simulation
store_characteristics = []
for store in range(1, num_stores + 1):
    size = np.random.choice(['small', 'medium', 'large'])
    location = np.random.choice(['urban', 'suburban', 'rural'])
    store_characteristics.append([store, size, location])

# Convert to DataFrame
df_store_characteristics = pd.DataFrame(store_characteristics, columns=['store_id', 'store_size', 'store_location'])

# Customer demographics simulation
customer_demographics = []
for customer in range(1, num_customers + 1):
    age = np.random.randint(18, 70)
    gender = np.random.choice(['M', 'F'])
    income = np.random.normal(loc=30000, scale=10000)
    customer_demographics.append([customer, age, gender, income])

# Convert to DataFrame
df_customer_demographics = pd.DataFrame(customer_demographics, columns=['customer_id', 'age', 'gender', 'income'])

# Save DataFrames to CSV files
df_sales_before.to_csv('data/sales_before.csv', index=False)
df_sales_after.to_csv('data/sales_after.csv', index=False)
df_store_characteristics.to_csv('data/store_characteristics.csv', index=False)
df_customer_demographics.to_csv('data/customer_demographics.csv', index=False)