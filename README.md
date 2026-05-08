# India Energy Demand Forecaster

A machine learning project that forecasts electricity demand across five Indian states and estimates total energy consumption for the next month.

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

```text
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
