import plotly.express as px


def revenue_trend_chart(revenue_data):
    """
    Revenue trend chart.
    """

    fig = px.line(
        x=revenue_data.index,
        y=revenue_data.values,
        markers=True,
        title="Revenue Trend",
        labels={
            "x": "Month",
            "y": "Revenue"
        }
    )

    fig.update_layout(
        template="plotly_white",
        height=400
    )

    return fig


def profit_trend_chart(profit_data):
    """
    Profit trend chart.
    """

    fig = px.line(
        x=profit_data.index,
        y=profit_data.values,
        markers=True,
        title="Profit Trend",
        labels={
            "x": "Month",
            "y": "Profit"
        }
    )

    fig.update_layout(
        template="plotly_white",
        height=400
    )

    return fig


def sales_category_chart(sales_data):
    """
    Sales by category.
    """

    fig = px.bar(
        x=sales_data.index,
        y=sales_data.values,
        title="Sales by Category",
        labels={
            "x": "Category",
            "y": "Sales"
        },
        color_discrete_sequence=["#2563EB"]
    )

    fig.update_layout(
        template="plotly_white",
        height=400
    )

    return fig


def profit_category_chart(profit_data):
    """
    Profit by category.
    """

    fig = px.bar(
        x=profit_data.index,
        y=profit_data.values,
        title="Profit by Category",
        labels={
            "x": "Category",
            "y": "Profit"
        },
        color_discrete_sequence=["#10B981"]
    )

    fig.update_layout(
        template="plotly_white",
        height=400
    )

    return fig


def sales_state_chart(sales_data):
    """
    Top states by sales.
    """

    fig = px.bar(
        x=sales_data.values,
        y=sales_data.index,
        orientation="h",
        title="Top 10 States by Sales",
        labels={
            "x": "Sales",
            "y": "State"
        },
        color_discrete_sequence=["#2563EB"]
    )

    fig.update_layout(
        template="plotly_white",
        height=400
    )

    return fig


def profit_state_chart(profit_data):
    """
    Top states by profit.
    """

    fig = px.bar(
        x=profit_data.values,
        y=profit_data.index,
        orientation="h",
        title="Top 10 States by Profit",
        labels={
            "x": "Profit",
            "y": "State"
        },
        color_discrete_sequence=["#10B981"]
    )

    fig.update_layout(
        template="plotly_white",
        height=400
    )

    return fig


def top_products_chart(products):
    """
    Top products by profit.
    """

    fig = px.bar(
        x=products.values,
        y=products.index,
        orientation="h",
        title="Top 5 Product Sub-Categories by Profit",
        labels={
            "x": "Profit",
            "y": "Sub-Category"
        },
        color_discrete_sequence=["#F59E0B"]
    )

    fig.update_layout(
        template="plotly_white",
        height=400
    )

    return fig