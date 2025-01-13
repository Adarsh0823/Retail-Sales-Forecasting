# Data Directory

This directory contains raw and processed data files for the Retail Sales Forecasting project.

## Structure

- **raw/**: Contains raw, unprocessed datasets.  
- **processed/**: Contains cleaned and preprocessed datasets, ready for analysis.  

## Instructions for Data Usage

1. Place the raw sales data file (e.g., `sales_data_raw.csv`) in the `raw/` directory.  
2. Use the `src/data_preprocessing.py` script to clean and preprocess the raw data.  
3. The processed data will be saved to the `processed/` directory as `sales_data_cleaned.csv`.  

## Data Fields Description

### Raw Data (`raw/sales_data_raw.csv`)
- **date**: The date of the sales record.  
- **store_id**: A unique identifier for the store.  
- **product_id**: A unique identifier for the product.  
- **sales**: Number of units sold.  
- **price**: Price of the product.  
- **inventory**: Remaining inventory in the store.  
- **region**: The geographical region of the store.

### Processed Data (`processed/sales_data_cleaned.csv`)
- **date**: The date of the sales record.  
- **sales**: Number of units sold.  
- **store_id**: A unique identifier for the store.  
- **product_id**: A unique identifier for the product.  
- **region**: The geographical region of the store.

## Notes
- Ensure that the raw data files have consistent formatting and column names before running preprocessing scripts.  
- All cleaned data files should be used for analysis and modeling.

