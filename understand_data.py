from src.data_loader import load_data

df = load_data("data/raw/SampleSuperstore.csv")

print(df.head())

print()

print(df.info())

print()

print(df.describe())

print()

print(df.isnull().sum())