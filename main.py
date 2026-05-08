import os
import joblib
import pandas as pd

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error


CSV_PATH = "data/india_5_state_energy_sample.csv"
MODEL_DIR = "models"
TARGET = "consumption_mu"

FEATURES = [
    "day_of_week",
    "month",
    "lag_1",
    "lag_7",
    "rolling_7"
]


# ---------------------------------
# Load data
# ---------------------------------
df = pd.read_csv(CSV_PATH)

df["date"] = pd.to_datetime(df["date"])
df = df.sort_values(["state", "date"]).reset_index(drop=True)

df["day_of_week"] = df["date"].dt.dayofweek
df["month"] = df["date"].dt.month

df["lag_1"] = df.groupby("state")[TARGET].shift(1)
df["lag_7"] = df.groupby("state")[TARGET].shift(7)

df["rolling_7"] = (
    df.groupby("state")[TARGET]
      .shift(1)
      .rolling(7)
      .mean()
)

df = df.dropna().reset_index(drop=True)

os.makedirs(MODEL_DIR, exist_ok=True)

state_models = {}


# ---------------------------------
# Train one model per state
# ---------------------------------
for state in df["state"].unique():

    sdf = df[df["state"] == state].copy()

    if len(sdf) < 20:
        print(f"Skipping {state}: not enough data")
        continue

    split = int(len(sdf) * 0.8)

    train = sdf.iloc[:split]
    test = sdf.iloc[split:]

    X_train = train[FEATURES]
    y_train = train[TARGET]

    X_test = test[FEATURES]
    y_test = test[TARGET]

    model = RandomForestRegressor(
        n_estimators=100,
        random_state=42
    )

    model.fit(X_train, y_train)

    preds = model.predict(X_test)

    mae = mean_absolute_error(y_test, preds)

    print(f"{state} MAE: {mae:.2f}")

    model_path = (
        f"{MODEL_DIR}/{state.lower().replace(' ', '_')}.pkl"
    )

    joblib.dump(model, model_path)

    state_models[state] = model


# ---------------------------------
# Forecast next 30 days for each state
# ---------------------------------
all_forecasts = []

for state, model in state_models.items():

    sdf = df[df["state"] == state].copy()

    history = sdf[["date", "state", TARGET]].copy()

    for _ in range(30):

        next_date = (
            history["date"].iloc[-1]
            + pd.Timedelta(days=1)
        )

        lag_1 = history[TARGET].iloc[-1]
        lag_7 = history[TARGET].iloc[-7]
        rolling_7 = history[TARGET].iloc[-7:].mean()

        next_row = pd.DataFrame([{
            "day_of_week": next_date.dayofweek,
            "month": next_date.month,
            "lag_1": lag_1,
            "lag_7": lag_7,
            "rolling_7": rolling_7
        }])

        prediction = model.predict(
            next_row[FEATURES]
        )[0]

        forecast_row = {
            "date": next_date,
            "state": state,
            TARGET: prediction
        }

        history = pd.concat(
            [history, pd.DataFrame([forecast_row])],
            ignore_index=True
        )

        all_forecasts.append({
            "date": next_date.strftime("%Y-%m-%d"),
            "state": state,
            "predicted_consumption": round(prediction, 2)
        })


# ---------------------------------
# Save daily forecast
# ---------------------------------
forecast_df = pd.DataFrame(all_forecasts)

forecast_df = forecast_df.sort_values(
    ["state", "date"]
).reset_index(drop=True)

forecast_df.to_csv(
    "models/next_month_forecast.csv",
    index=False
)


# ---------------------------------
# Total next month consumption by state
# ---------------------------------
monthly_total = (
    forecast_df
    .groupby("state")["predicted_consumption"]
    .sum()
    .reset_index()
)

monthly_total["predicted_consumption"] = (
    monthly_total["predicted_consumption"].round(2)
)

monthly_total.to_csv(
    "models/next_month_total_by_state.csv",
    index=False
)


# ---------------------------------
# Output
# ---------------------------------
print("\nForecast rows per state:")
print(forecast_df.groupby("state").size())

print("\nTotal forecasted energy consumption next month:")
print(monthly_total.to_string(index=False))

print("\nSaved files:")
print("models/next_month_forecast.csv")
print("models/next_month_total_by_state.csv")