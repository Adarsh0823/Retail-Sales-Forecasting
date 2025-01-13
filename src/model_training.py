import pandas as pd
from fbprophet import Prophet

def train_model(data_path, model_path):
    # Load processed data
    data = pd.read_csv(data_path)
    data.rename(columns={'date': 'ds', 'sales': 'y'}, inplace=True)

    # Initialize and fit the Prophet model
    model = Prophet()
    model.fit(data)

    # Save the model
    with open(model_path, 'wb') as f:
        import pickle
        pickle.dump(model, f)
    print(f"Model saved to {model_path}")

if __name__ == "__main__":
    train_model("data/processed/sales_data_cleaned.csv", "models/sales_forecast_model.pkl")
