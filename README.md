# AI-Powered Financial Analytics Dashboard

## Live Demo

**Application:** https://ai-powered-financial-analytics-dashboard-cbytyep8wavoxxqpksikm.streamlit.app/

**Source Code:** https://github.com/AditiiShikha/AI-Powered-Financial-Analytics-Dashboard


An interactive business intelligence dashboard built with **Python, Pandas, Scikit-learn, Plotly, and Streamlit** for analyzing retail sales data, generating business insights, and predicting profit using machine learning.

---

## Overview

Businesses generate large volumes of transactional data every day, making it difficult to manually identify sales trends, profitable categories, and regional performance.

This project provides an interactive dashboard that allows users to:

- Analyze historical sales and profit data
- Filter results by region and category
- Visualize business performance
- Generate business insights
- Predict profit for new transactions using a trained machine learning model

---

## Features

- Interactive KPI Dashboard
- Sales Analysis
- Profit Analysis
- Region and Category Filters
- Business Insights
- Profit Prediction
- Download Filtered Dataset
- Model Comparison

---

## Dashboard

The dashboard includes:

- Total Sales
- Total Profit
- Average Discount
- Total Orders

Charts include:

- Sales by Category
- Profit by Category
- Sales by State
- Profit by State
- Top Selling Products

Users can also enter transaction details to estimate expected profit using the trained regression model.

---

## Tech Stack

### Programming

- Python

### Data Analysis

- Pandas
- NumPy

### Machine Learning

- Scikit-learn

### Visualization

- Plotly

### Dashboard

- Streamlit

### Model Persistence

- Joblib

---

## Project Structure

```
AI-Powered-Financial-Analytics-Dashboard/

│
├── app.py
├── requirements.txt
├── README.md
│
├── data/
│   └── raw/
│
├── models/
│   ├── compare_models.py
│   └── train_model.py
│
├── saved_models/
│   └── linear_regression.pkl
│
└── src/
    ├── charts.py
    ├── data_loader.py
    ├── eda.py
    ├── preprocessing.py
    └── utils.py
```

---

## Machine Learning Workflow

### Data Preprocessing

The dataset was cleaned and prepared before training.

Preprocessing included:

- Date conversion
- Removal of unnecessary identifiers
- Feature engineering
- Data type correction

Engineered features include:

- Shipping Time
- Discount Amount
- Unit Price
- Order Month

---

## Models Evaluated

Three regression models were compared.

| Model | MAE | RMSE | R² |
|------|------:|------:|------:|
| Linear Regression | 41.82 | 181.74 | **0.319** |
| Random Forest | 25.91 | 206.97 | 0.116 |
| Decision Tree | 33.91 | 290.09 | -0.736 |

Linear Regression achieved the best overall performance on this dataset and was selected for deployment within the dashboard.

---

## Model Evaluation

The model was evaluated using:

- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- R² Score

These metrics provide insight into prediction accuracy and generalization performance.

---

## Business Insights

The dashboard automatically identifies:

- Highest performing product category
- Top performing state
- Lowest performing state
- Average discount
- Business recommendations based on historical data

---

## Profit Prediction

Users can enter:

- Sales
- Quantity
- Discount
- Category
- Sub-Category
- Region
- State
- Segment
- Order Month

The trained model estimates the expected profit for the given transaction.

---

## Dataset

Sample Superstore Dataset

The dataset contains approximately 10,000 retail transactions including:

- Sales
- Profit
- Quantity
- Discount
- Product Category
- Customer Segment
- Region
- State

---

## Model Limitations

Although the deployed model performed best among the evaluated algorithms, predicting profit remains challenging because several important business variables are not included in the dataset.

Examples include:

- Product manufacturing cost
- Supplier cost
- Shipping expenses
- Operational expenses
- Taxes

As a result, the model explains only part of the variation in profit. This project demonstrates an end-to-end machine learning workflow rather than a production forecasting system.

---

## Future Improvements

- Deploy using cloud infrastructure
- Add forecasting using time-series models
- Compare additional regression algorithms (XGBoost, LightGBM)
- Integrate live business datasets
- Add customer segmentation and demand forecasting

---

## Installation

Clone the repository

```bash
git clone <repository-url>
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

## Author

Developed as an end-to-end Machine Learning and Data Analytics project using Python, Scikit-learn, Plotly, and Streamlit.
