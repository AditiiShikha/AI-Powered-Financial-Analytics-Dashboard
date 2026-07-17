import pandas as pd
import joblib

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

from src.data_loader import load_data
from src.preprocessing import preprocess_data

df = load_data("data/raw/SampleSuperstore.csv")
df = preprocess_data(df)

y = df["Profit"]

X = df[
    [
        "Sales",
        "Quantity",
        "Discount",
        "Category",
        "Sub-Category",
        "Region",
        "State",
        "Segment",
        "Order Month"
    ]
]

categorical_features = [
    "Category",
    "Sub-Category",
    "Region",
    "State",
    "Segment"
]

numeric_features = [
    "Sales",
    "Quantity",
    "Discount",
    "Order Month"
]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
preprocessor = ColumnTransformer(
    transformers=[
        (
            "cat",
            OneHotEncoder(handle_unknown="ignore"),
            categorical_features
        )
    ],
    remainder="passthrough"
)

model = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        ("model", RandomForestRegressor(
            n_estimators=100,
            random_state=42
        ))
    ]
)
model.fit(X_train, y_train)

rf = model.named_steps["model"]

feature_names = model.named_steps["preprocessor"].get_feature_names_out()

import pandas as pd

importance = pd.DataFrame({
    "Feature": feature_names,
    "Importance": rf.feature_importances_
})

print(
    importance.sort_values(
        "Importance",
        ascending=False
    ).head(15)
)


predictions = model.predict(X_test)

mae = mean_absolute_error(y_test, predictions)
rmse = mean_squared_error(y_test, predictions) ** 0.5
r2 = r2_score(y_test, predictions)

print(f"MAE : {mae:.2f}")
print(f"RMSE: {rmse:.2f}")
print(f"R²  : {r2:.3f}")

joblib.dump(
    model,
    "saved_models/random_forest.pkl"
)

print(" Model saved successfully!")

print(X.columns)
print(df["Profit"].describe())
