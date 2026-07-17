import pandas as pd
import streamlit as st
import joblib

from src.data_loader import load_data
from src.preprocessing import preprocess_data
from src.utils import format_currency

from src.eda import (
    calculate_kpis,
    sales_by_category,
    profit_by_category,
    sales_by_state,
    profit_by_state,
    top_products
)

from src.charts import (
    sales_category_chart,
    profit_category_chart,
    sales_state_chart,
    profit_state_chart,
    top_products_chart
)

# Page configuration

st.set_page_config(
    page_title="AI-Powered Financial Analytics Dashboard",
    layout="wide"
)

st.title("AI-Powered Financial Analytics Dashboard")
st.caption("Interactive dashboard for sales, profit and business analysis.")

st.markdown("---")

# Load data

df = load_data("data/raw/SampleSuperstore.csv")
df = preprocess_data(df)

# Load trained model

model = joblib.load("saved_models/linear_regression.pkl")

# Sidebar

st.sidebar.title("Filters")

selected_region = st.sidebar.selectbox(
    "Region",
    ["All"] + sorted(df["Region"].unique().tolist())
)

selected_category = st.sidebar.selectbox(
    "Category",
    ["All"] + sorted(df["Category"].unique().tolist())
)

# Apply filters

filtered_df = df.copy()

if selected_region != "All":
    filtered_df = filtered_df[
        filtered_df["Region"] == selected_region
    ]

if selected_category != "All":
    filtered_df = filtered_df[
        filtered_df["Category"] == selected_category
    ]

# Download filtered data

csv = filtered_df.to_csv(index=False).encode("utf-8")

st.sidebar.download_button(
    label="Download Filtered Data",
    data=csv,
    file_name="filtered_data.csv",
    mime="text/csv"
)

# KPI section

kpis = calculate_kpis(filtered_df)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Sales",
        format_currency(kpis["Total Sales"])
    )

with col2:
    st.metric(
        "Total Profit",
        format_currency(kpis["Total Profit"])
    )

with col3:
    st.metric(
        "Average Discount",
        f"{kpis['Average Discount']:.2f}%"
    )

with col4:
    st.metric(
        "Total Orders",
        kpis["Total Orders"]
    )

st.markdown("---")

# Chart data

sales_category = sales_by_category(filtered_df)
profit_category = profit_by_category(filtered_df)

sales_state = sales_by_state(filtered_df)
profit_state = profit_by_state(filtered_df)

products = top_products(filtered_df)

# Charts

col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(
        sales_category_chart(sales_category),
        use_container_width=True
    )

with col2:
    st.plotly_chart(
        profit_category_chart(profit_category),
        use_container_width=True
    )

col3, col4 = st.columns(2)

with col3:
    st.plotly_chart(
        sales_state_chart(sales_state),
        use_container_width=True
    )

with col4:
    st.plotly_chart(
        profit_state_chart(profit_state),
        use_container_width=True
    )

st.plotly_chart(
    top_products_chart(products),
    use_container_width=True
)

# Business insights

st.markdown("---")

st.subheader("Business Insights")

top_category = sales_category.idxmax()
top_state = sales_state.idxmax()
lowest_state = profit_state.idxmin()

st.info(
    f"""
Highest Sales Category: {top_category}

Top Performing State: {top_state}

Lowest Performing State: {lowest_state}

Average Discount: {kpis['Average Discount']:.2f}%

Recommendation:
Increase investment in {top_category} while reviewing operations in {lowest_state}.
"""
)

# Profit prediction

st.markdown("---")

st.subheader("Profit Prediction")

col1, col2 = st.columns(2)

with col1:

    sales = st.number_input(
        "Sales",
        min_value=0.0,
        value=500.0
    )

    quantity = st.number_input(
        "Quantity",
        min_value=1,
        value=2
    )

    discount = st.slider(
        "Discount",
        min_value=0.0,
        max_value=0.8,
        value=0.2,
        step=0.05
    )

    order_month = st.selectbox(
        "Order Month",
        list(range(1, 13))
    )

with col2:

    category = st.selectbox(
        "Category",
        sorted(df["Category"].unique())
    )

    sub_category = st.selectbox(
        "Sub-Category",
        sorted(df["Sub-Category"].unique())
    )

    region = st.selectbox(
        "Region",
        sorted(df["Region"].unique())
    )

    state = st.selectbox(
        "State",
        sorted(df["State"].unique())
    )

    segment = st.selectbox(
        "Segment",
        sorted(df["Segment"].unique())
    )

# Derived features

shipping_time = 4
discount_amount = sales * discount
unit_price = sales / quantity

input_data = pd.DataFrame({
    "Sales": [sales],
    "Quantity": [quantity],
    "Discount": [discount],
    "Order Month": [order_month],
    "Shipping Time": [shipping_time],
    "Discount Amount": [discount_amount],
    "Unit Price": [unit_price],
    "Category": [category],
    "Sub-Category": [sub_category],
    "Region": [region],
    "State": [state],
    "Segment": [segment]
})

if st.button("Predict Profit"):

    prediction = model.predict(input_data)[0]

    st.success(
        f"Estimated Profit: {format_currency(prediction)}"
    )

# Footer

st.markdown("---")

st.caption(
    "Python | Pandas | Scikit-learn | Plotly | Streamlit"
)