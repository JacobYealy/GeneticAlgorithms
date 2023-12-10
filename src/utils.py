import logging
import os
import pandas as pd
from datetime import datetime

# Initialize logging
def setup_logging():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    logger = logging.getLogger()
    return logger

# Function to save DataFrame to Excel
def save_to_excel(df, file_name):
    path = os.path.join('data', file_name)
    df.to_excel(path, index=False)
    print(f"Dataframe is saved to {path}.")

# Function to calculate time taken for a function (decorator)
def timing(f):
    def wrap(*args, **kwargs):
        time1 = datetime.now()
        result = f(*args, **kwargs)
        time2 = datetime.now()
        print(f'Function {f.__name__} took {(time2-time1).total_seconds()} seconds')
        return result
    return wrap

# Function to convert dataframe columns to specific types
def convert_dtypes(df, column_types):
    for column, dtype in column_types.items():
        df[column] = df[column].astype(dtype)
    return df

