import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder

from sklearn.model_selection import train_test_split

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

from src.data_loader import load_data
from src.preprocessing import preprocess_data

# Load data

df = load_data("data/raw/SampleSuperstore.csv")
df = preprocess_data(df)

# Features and target

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

# Categorical columns

categorical_features = [
    "Category",
    "Sub-Category",
    "Region",
    "State",
    "Segment"
]

# Train test split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

# Preprocessing

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

# Models to compare

models = {
    "Linear Regression": LinearRegression(),

    "Decision Tree": DecisionTreeRegressor(
        random_state=42
    ),

    "Random Forest": RandomForestRegressor(
        n_estimators=300,
        max_depth=15,
        min_samples_split=5,
        min_samples_leaf=2,
        random_state=42,
        n_jobs=-1
    )
}

results = []

# Train and evaluate each model

for name, algorithm in models.items():

    pipeline = Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            ("model", algorithm)
        ]
    )

    pipeline.fit(
        X_train,
        y_train
    )

    predictions = pipeline.predict(X_test)

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

    results.append(
        {
            "Model": name,
            "MAE": round(mae, 2),
            "RMSE": round(rmse, 2),
            "R²": round(r2, 3)
        }
    )

# Display comparison

results = pd.DataFrame(results)

results = results.sort_values(
    by="R²",
    ascending=False
).reset_index(drop=True)

print("\nModel Comparison\n")

print(results)

# Save comparison

results.to_csv(
    "model_comparison.csv",
    index=False
)

print("\nComparison saved successfully.")

# Best model

best_model = results.iloc[0]

print("\nBest Model\n")

print(
    f"{best_model['Model']} "
    f"(R² = {best_model['R²']})"
)