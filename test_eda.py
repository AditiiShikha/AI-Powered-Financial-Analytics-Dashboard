from src.data_loader import load_data
from src.preprocessing import preprocess_data
from src.eda import (
    calculate_kpis,
    sales_by_category,
    profit_by_category,
    sales_by_region,
    profit_by_region
)

df = load_data("data/raw/SampleSuperstore.csv")
df = preprocess_data(df)

print(calculate_kpis(df))

print("\nSales by Category")
print(sales_by_category(df))

print("\nProfit by Category")
print(profit_by_category(df))

print("\nSales by Region")
print(sales_by_region(df))

print("\nProfit by Region")
print(profit_by_region(df))