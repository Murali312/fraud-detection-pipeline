import pandas as pd

def clean_data(df):
    # Convert time column to datetime
    df['time'] = pd.to_datetime(df['time'])

    # Handle missing values
    df['merchant'] = df['merchant'].fillna("Unknown")

    # Remove duplicates
    df = df.drop_duplicates()

    return df
