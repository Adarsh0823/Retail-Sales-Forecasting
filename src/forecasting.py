import pandas as pd
from fbprophet import Prophet
import pickle

def generate_forecast(model_path, output_path):
    # Load the trained model
    with open(model_path, 'rb') as f:
        model = pickle.load(f)

    # Create future dates
    future = model.make_future_dataframe(periods=30)  # Forecast for the next 30 days

    # Generate forecast
    forecast = model.predict(future)

    # Save forecast
    forecast.to_csv(output_path, index=False)
    print(f"Forecast saved to {output_path}")

if __name__ == "__main__":
    generate_forecast("models/sales_forecast_model.pkl", "data/processed/sales_forecast.csv")
