import plotly.express as px


# Sales by category

def sales_category_chart(sales_data):

    fig = px.bar(
        x=sales_data.index,
        y=sales_data.values,
        labels={
            "x": "Category",
            "y": "Total Sales"
        },
        title="Sales by Category"
    )

    fig.update_layout(
        xaxis_title="Category",
        yaxis_title="Sales"
    )

    return fig


# Profit by category

def profit_category_chart(profit_data):

    fig = px.bar(
        x=profit_data.index,
        y=profit_data.values,
        labels={
            "x": "Category",
            "y": "Total Profit"
        },
        title="Profit by Category"
    )

    fig.update_layout(
        xaxis_title="Category",
        yaxis_title="Profit"
    )

    return fig


# Sales by state

def sales_state_chart(sales_data):

    fig = px.bar(
        x=sales_data.index,
        y=sales_data.values,
        labels={
            "x": "State",
            "y": "Total Sales"
        },
        title="Sales by State"
    )

    fig.update_layout(
        xaxis_title="State",
        yaxis_title="Sales"
    )

    return fig


# Profit by state

def profit_state_chart(profit_data):

    fig = px.bar(
        x=profit_data.index,
        y=profit_data.values,
        labels={
            "x": "State",
            "y": "Total Profit"
        },
        title="Profit by State"
    )

    fig.update_layout(
        xaxis_title="State",
        yaxis_title="Profit"
    )

    return fig


# Monthly sales trend

def monthly_sales_chart(monthly_sales):

    fig = px.line(
        x=monthly_sales.index,
        y=monthly_sales.values,
        markers=True,
        labels={
            "x": "Month",
            "y": "Sales"
        },
        title="Monthly Sales Trend"
    )

    fig.update_layout(
        xaxis_title="Month",
        yaxis_title="Sales"
    )

    return fig


# Monthly profit trend

def monthly_profit_chart(monthly_profit):

    fig = px.line(
        x=monthly_profit.index,
        y=monthly_profit.values,
        markers=True,
        labels={
            "x": "Month",
            "y": "Profit"
        },
        title="Monthly Profit Trend"
    )

    fig.update_layout(
        xaxis_title="Month",
        yaxis_title="Profit"
    )

    return fig


# Top selling products

def top_products_chart(product_data):

    fig = px.bar(
        x=product_data.values,
        y=product_data.index,
        orientation="h",
        labels={
            "x": "Sales",
            "y": "Sub-Category"
        },
        title="Top Selling Products"
    )

    fig.update_layout(
        yaxis=dict(
            categoryorder="total ascending"
        )
    )

    return fig


# Top profitable products

def top_profit_products_chart(product_data):

    fig = px.bar(
        x=product_data.values,
        y=product_data.index,
        orientation="h",
        labels={
            "x": "Profit",
            "y": "Sub-Category"
        },
        title="Top Profitable Products"
    )

    fig.update_layout(
        yaxis=dict(
            categoryorder="total descending"
        )
    )

    return fig