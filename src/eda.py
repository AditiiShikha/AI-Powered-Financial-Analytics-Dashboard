import pandas as pd


def calculate_kpis(df):
    """
    Calculate dashboard KPI metrics.
    """

    total_sales = df["Sales"].sum()
    total_profit = df["Profit"].sum()
    average_discount = df["Discount"].mean()
    total_orders = len(df)

    profit_margin = (total_profit / total_sales) * 100

    return {
        "Total Sales": round(total_sales, 2),
        "Total Profit": round(total_profit, 2),
        "Average Discount": round(average_discount * 100, 2),
        "Total Orders": total_orders,
        "Profit Margin": round(profit_margin, 2)
    }


def revenue_trend(df):
    """
    Monthly revenue trend.
    """

    revenue = (
        df.groupby("Order Month")["Sales"]
        .sum()
        .sort_index()
    )

    return revenue


def profit_trend(df):
    """
    Monthly profit trend.
    """

    profit = (
        df.groupby("Order Month")["Profit"]
        .sum()
        .sort_index()
    )

    return profit


def sales_by_category(df):
    """
    Total sales by category.
    """

    return (
        df.groupby("Category")["Sales"]
        .sum()
        .sort_values(ascending=False)
    )


def profit_by_category(df):
    """
    Total profit by category.
    """

    return (
        df.groupby("Category")["Profit"]
        .sum()
        .sort_values(ascending=False)
    )


def sales_by_state(df):
    """
    Top 10 states by sales.
    """

    return (
        df.groupby("State")["Sales"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )


def profit_by_state(df):
    """
    Top 10 states by profit.
    """

    return (
        df.groupby("State")["Profit"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )


def top_products(df):
    """
    Top 5 product sub-categories by profit.
    """

    return (
        df.groupby("Sub-Category")["Profit"]
        .sum()
        .sort_values(ascending=False)
        .head(5)
    )