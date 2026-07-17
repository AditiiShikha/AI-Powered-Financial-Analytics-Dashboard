import streamlit as st

from src.data_loader import load_data
from src.preprocessing import preprocess_data
from src.utils import format_currency

from src.eda import (
    calculate_kpis,
    revenue_trend,
    profit_trend,
    profit_by_category,
    profit_by_state,
    top_products
)

from src.charts import (
    revenue_trend_chart,
    profit_trend_chart,
    profit_category_chart,
    profit_state_chart,
    top_products_chart
)

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="AI-Powered Financial Analytics Dashboard",
    page_icon=" ",
    layout="wide"
)

st.title(" AI-Powered Financial Analytics Dashboard")
st.caption(
    "Analyze business performance using interactive visualizations and AI-powered insights."
)

st.markdown("---")

# ---------------- LOAD DATA ---------------- #

df = load_data("data/raw/SampleSuperstore.csv")
df = preprocess_data(df)

# ---------------- SIDEBAR ---------------- #

st.sidebar.header("Dashboard Filters")

st.sidebar.caption(
    "Filter the data to analyze different regions and product categories."
)

st.sidebar.markdown(
"""
Filter the dashboard by region and category
to explore different business segments.
"""
)

selected_region = st.sidebar.selectbox(
    "Region",
    ["All"] + sorted(df["Region"].unique())
)

selected_category = st.sidebar.selectbox(
    "Category",
    ["All"] + sorted(df["Category"].unique())
)

filtered_df = df.copy()

if selected_region != "All":
    filtered_df = filtered_df[
        filtered_df["Region"] == selected_region
    ]

if selected_category != "All":
    filtered_df = filtered_df[
        filtered_df["Category"] == selected_category
    ]

st.sidebar.markdown("---")

st.sidebar.caption(
    "Export the currently filtered dataset."
)

st.sidebar.subheader("Export Data")

csv = filtered_df.to_csv(index=False).encode("utf-8")

st.sidebar.download_button(
    label=" Download CSV",
    data=csv,
    file_name="financial_dashboard_data.csv",
    mime="text/csv",
    use_container_width=True
)

#  KPI SECTION

kpis = calculate_kpis(filtered_df)

col1, col2, col3, col4, col5 = st.columns(5)

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
        "Profit Margin",
        f"{kpis['Profit Margin']}%"
    )

with col4:
    st.metric(
        "Average Discount",
        f"{kpis['Average Discount']:.2f}%"
    )

with col5:
    st.metric(
        "Total Orders",
        kpis["Total Orders"]
    )

st.markdown("---")

#  EDA 
revenue = revenue_trend(filtered_df)
profit = profit_trend(filtered_df)

category_profit = profit_by_category(filtered_df)

state_profit = profit_by_state(filtered_df)

products = top_products(filtered_df)

#  TREND CHARTS

col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(
        revenue_trend_chart(revenue),
        use_container_width=True
    )

with col2:
    st.plotly_chart(
        profit_trend_chart(profit),
        use_container_width=True
    )

#  ANALYSIS CHARTS 

col3, col4 = st.columns(2)

with col3:
    st.plotly_chart(
        profit_category_chart(category_profit),
        use_container_width=True
    )

with col4:
    st.plotly_chart(
        profit_state_chart(state_profit),
        use_container_width=True
    )

# - PRODUCTS & TRANSACTIONS
col5, col6 = st.columns(2)

with col5:
    st.plotly_chart(
        top_products_chart(products),
        use_container_width=True
    )

with col6:
    st.subheader("Recent Transactions")

    st.dataframe(
        filtered_df[
            [
                "State",
                "Category",
                "Sub-Category",
                "Sales",
                "Profit",
                "Quantity"
            ]
        ].head(10),
        use_container_width=True
    )

st.markdown("---")

# - BUSINESS INSIGHTS

top_profit_category = category_profit.idxmax()
top_profit_state = state_profit.idxmax()
lowest_profit_state = state_profit.idxmin()

st.subheader("💡 AI Business Insights")

st.info(f"""
Highest Profit Category: **{top_profit_category}**

Top Performing State: **{top_profit_state}**

Lowest Performing State: **{lowest_profit_state}**

Average Discount: **{kpis["Average Discount"]:.2f}%**

### Recommendation

Increase investment in **{top_profit_category}** while reviewing pricing and discount strategies in **{lowest_profit_state}** to improve profitability.
""")

# ---------------- PREDICTION ---------------- #

st.markdown("---")

st.subheader(" AI Profit Prediction")

st.warning(
    "Machine Learning prediction module will be integrated using a Random Forest Regressor."
)

#  FOOTER 

st.markdown("---")

st.caption(
    "Built by Aditi Shikha using Python, Pandas, Scikit-learn, Plotly and Streamlit"
)