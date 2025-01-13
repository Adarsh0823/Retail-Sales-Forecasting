import pandas as pd

def preprocess_data(input_path, output_path):
    # Load raw data
    data = pd.read_csv(input_path)

    # Fill missing values
    data.fillna(method='ffill', inplace=True)

    # Convert date column to datetime
    data['date'] = pd.to_datetime(data['date'])

    # Sort data by date
    data.sort_values('date', inplace=True)

    # Save processed data
    data.to_csv(output_path, index=False)
    print(f"Processed data saved to {output_path}")

if __name__ == "__main__":
    preprocess_data("data/raw/sales_data.csv", "data/processed/sales_data_cleaned.csv")
