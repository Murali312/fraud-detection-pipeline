import pandas as pd

def load_data(path):
    # Read CSV file
    df = pd.read_csv(path)
    return df
