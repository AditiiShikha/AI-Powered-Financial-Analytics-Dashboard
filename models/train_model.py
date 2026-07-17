import joblib
import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

from src.data_loader import load_data
from src.preprocessing import preprocess_data

# Load data

df = load_data("data/raw/SampleSuperstore.csv")
df = preprocess_data(df)

# Select features and target

X = df[
    [
        "Sales",
        "Quantity",
        "Discount",
        "Order Month",
        "Shipping Time",
        "Discount Amount",
        "Unit Price",
        "Category",
        "Sub-Category",
        "Region",
        "State",
        "Segment"
    ]
]

y = df["Profit"]

# Define feature types

categorical_features = [
    "Category",
    "Sub-Category",
    "Region",
    "State",
    "Segment"
]

# Split dataset

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

# Preprocessing pipeline

preprocessor = ColumnTransformer(
    transformers=[
        (
            "categorical",
            OneHotEncoder(handle_unknown="ignore"),
            categorical_features
        )
    ],
    remainder="passthrough"
)

# Build pipeline

model = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        ("model", LinearRegression())
    ]
)

# Train model

model.fit(X_train, y_train)

# Predictions

predictions = model.predict(X_test)

# Evaluation

mae = mean_absolute_error(
    y_test,
    predictions
)

rmse = mean_squared_error(
    y_test,
    predictions
) ** 0.5

r2 = r2_score(
    y_test,
    predictions
)

print("\nModel Performance\n")

print(f"MAE : {mae:.2f}")
print(f"RMSE: {rmse:.2f}")
print(f"R²  : {r2:.3f}")

# Save model

joblib.dump(
    model,
    "saved_models/linear_regression.pkl"
)

print("\nModel saved successfully.")

# Feature names

feature_names = model.named_steps[
    "preprocessor"
].get_feature_names_out()

coefficients = model.named_steps[
    "model"
].coef_

importance = pd.DataFrame(
    {
        "Feature": feature_names,
        "Coefficient": coefficients
    }
)

importance["Absolute Coefficient"] = (
    importance["Coefficient"].abs()
)

importance = importance.sort_values(
    by="Absolute Coefficient",
    ascending=False
)

print("\nTop Features\n")

print(
    importance[
        [
            "Feature",
            "Coefficient"
        ]
    ].head(15)
)

print("\nFeatures Used\n")

print(X.columns)

print("\nProfit Statistics\n")

print(df["Profit"].describe())