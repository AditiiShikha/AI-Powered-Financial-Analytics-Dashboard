import pandas as pd


def preprocess_data(df):
    """
    Clean and preprocess the dataset.
    """

    # Convert date columns
    df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")
    df["Ship Date"] = pd.to_datetime(df["Ship Date"], errors="coerce")
   
    # Extract useful date features
    df["Order Year"] = df["Order Date"].dt.year
    df["Order Month"] = df["Order Date"].dt.month
    df["Order Day"] = df["Order Date"].dt.day

    df["Ship Year"] = df["Ship Date"].dt.year
    df["Ship Month"] = df["Ship Date"].dt.month
    df["Ship Day"] = df["Ship Date"].dt.day

    # Shipping time in days
    df["Shipping Time"] = (
    df["Ship Date"] - df["Order Date"]
).dt.days

# Discount amount
    df["Discount Amount"] = (
    df["Sales"] * df["Discount"]
)

# Average selling price per unit
    df["Unit Price"] = (
    df["Sales"] / df["Quantity"]
)

    

    df = df.drop(
    columns=[
        "Order Date",
        "Ship Date"
    ]
)
    # Drop unnecessary columns
    columns_to_drop = [
        "Row ID",
        "Order ID",
        "Customer ID",
        "Customer Name",
        "Product ID",
        "Product Name",
        "Country"
    ]

    df = df.drop(columns=columns_to_drop)

    return df