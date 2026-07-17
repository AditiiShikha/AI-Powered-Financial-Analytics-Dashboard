import pandas as pd


# Calculate dashboard KPIs

def calculate_kpis(df):

    return {
        "Total Sales": df["Sales"].sum(),
        "Total Profit": df["Profit"].sum(),
        "Average Discount": df["Discount"].mean() * 100,
        "Total Orders": len(df),
        "Profit Margin": (
            df["Profit"].sum() / df["Sales"].sum()
        ) * 100
    }


# Sales by category

def sales_by_category(df):

    return (
        df.groupby("Category")["Sales"]
        .sum()
        .sort_values(ascending=False)
    )


# Profit by category

def profit_by_category(df):

    return (
        df.groupby("Category")["Profit"]
        .sum()
        .sort_values(ascending=False)
    )


# Sales by state

def sales_by_state(df):

    return (
        df.groupby("State")["Sales"]
        .sum()
        .sort_values(ascending=False)
    )


# Profit by state

def profit_by_state(df):

    return (
        df.groupby("State")["Profit"]
        .sum()
        .sort_values(ascending=False)
    )


# Sales by region

def sales_by_region(df):

    return (
        df.groupby("Region")["Sales"]
        .sum()
        .sort_values(ascending=False)
    )


# Profit by region

def profit_by_region(df):

    return (
        df.groupby("Region")["Profit"]
        .sum()
        .sort_values(ascending=False)
    )


# Monthly sales

def monthly_sales(df):

    return (
        df.groupby("Order Month")["Sales"]
        .sum()
        .sort_index()
    )


# Monthly profit

def monthly_profit(df):

    return (
        df.groupby("Order Month")["Profit"]
        .sum()
        .sort_index()
    )


# Top selling products

def top_products(df):

    return (
        df.groupby("Sub-Category")["Sales"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )


# Top profitable products

def top_profit_products(df):

    return (
        df.groupby("Sub-Category")["Profit"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )