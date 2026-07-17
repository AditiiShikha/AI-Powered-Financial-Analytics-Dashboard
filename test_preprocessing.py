from src.data_loader import load_data
from src.preprocessing import preprocess_data

df = load_data("data/raw/SampleSuperstore.csv")

processed_df = preprocess_data(df)

print(processed_df.head())

print()

print(processed_df.info())