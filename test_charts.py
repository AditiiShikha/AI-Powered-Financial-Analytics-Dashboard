from src.data_loader import load_data
from src.preprocessing import preprocess_data
from src.eda import sales_by_category
from src.charts import sales_category_chart

df = load_data("data/raw/SampleSuperstore.csv")
df = preprocess_data(df)

sales = sales_by_category(df)

fig = sales_category_chart(sales)

fig.show()