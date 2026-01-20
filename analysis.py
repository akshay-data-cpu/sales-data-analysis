import pandas as pd

# Load data
df = pd.read_csv("sales_data.csv")

# Basic analysis
total_sales = df["Sales"].sum()
average_profit = df["Profit"].mean()
total_orders = df["Order_ID"].count()

print("Total Sales:", total_sales)
print("Average Profit:", average_profit)
print("Total Orders:", total_orders)
