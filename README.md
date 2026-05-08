# India Energy Demand Forecaster

A machine learning project that forecasts electricity demand across five Indian states and estimates total energy consumption for the next month.

---
## Authors

| Name | Roll Number |
|------|-------------|
| *Harshul Goel* | *245UAI049* |
---

## Overview

Electricity demand forecasting helps power planners understand future consumption patterns and improve generation planning.

This project uses historical daily energy consumption data to build **state-wise forecasting models** for:

- Maharashtra
- Gujarat
- Tamil Nadu
- Karnataka
- Uttar Pradesh

The model predicts:

- **next 30 days of daily energy consumption**
- **total next-month energy consumption for each state**

---

## Problem Statement

Energy demand changes due to seasonal patterns, weekday behavior, and recent historical demand.

The objective of this project is to use past consumption trends to estimate upcoming demand at the **state level**.

---

## Features Used

The forecasting model uses:

- **Day of week**
- **Month**
- **Previous day consumption (`lag_1`)**
- **Previous week consumption (`lag_7`)**
- **7-day rolling average**

---

## Project Structure

```
india-energy-forecaster/
│
├── data/
│   └── india_5_state_energy_sample.csv
│
├── src/
│   ├── train.py
│   └── plot_forecast.py
│
├── models/
│   ├── next_month_forecast.csv
│   └── next_month_total_by_state.csv
│
├── outputs/
│   ├── monthly_total_by_state.png
│   └── maharashtra_next_month_forecast.png
│
├── requirements.txt
├── README.md
└── .gitignore

```


---

## Dataset

The dataset contains historical daily electricity consumption records for five Indian states.

### States included

- Maharashtra
- Gujarat
- Tamil Nadu
- Karnataka
- Uttar Pradesh

### Source

The current dataset is a sample dataset created for forecasting experiments.  
The project structure can be extended using official data from:

- **Central Electricity Authority (CEA), India**
- **National Power Portal (NPP), India***Source** | Kaggle — Social Media User Behavior Dataset |


---

## Libraries Used

- **pandas** — data loading, cleaning, feature engineering
- **scikit-learn** — Random Forest model training and evaluation
- **joblib** — saving trained models
- **matplotlib** — generating forecast graphs
- **os** — directory and file handling

Install all dependencies with:

```bash
pip install pandas os matplotlib scikit-learn joblib
```

---

## Models Used

Random Forest Regressor
Evaluation metric:
Mean Absolute Error (MAE)

---

## Results

The project successfully generated:

- **30-day daily energy demand forecasts** for each of the five states
- **total predicted energy consumption for the next month** for each state
- **state-wise visualizations** for easier comparison and interpretation

### Output files

- `models/next_month_forecast.csv`
- `models/next_month_total_by_state.csv`

### Example monthly forecast

| State | Predicted Next Month Consumption |
|---|---:|
| Maharashtra | 548942.27 |
| Gujarat | 425860.33 |
| Tamil Nadu | 381505.94 |
| Karnataka | 359214.81 |
| Uttar Pradesh | 497331.66 |

The model captured short-term consumption trends and produced stable next-month forecasts across all five states.

---

## Key Observations

- Electricity demand shows clear short-term temporal patterns across states.
- Recent historical consumption (`lag_1`, `lag_7`) strongly influences next-day demand.
- Weekly patterns help capture weekday and weekend demand variation.
- The 7-day rolling average reduces short-term fluctuations and improves forecast stability.
- Forecasted next-month consumption differs across states because of different demand scales and historical usage patterns.
- State-wise modeling performs better than combining all states into one model because each state has distinct consumption behavior.
---

## Future Improvements

-weather-based forecasting
-holiday and festival effects
-larger state coverage
-integration with real government datasets
-interactive Streamlit dashboard

---

