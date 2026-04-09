import pandas as pd
import numpy as np

def create_features(df):
    # Sort data by user and time
    df = df.sort_values(by=['user_id', 'time'])

    # 🔹 Feature 1: Transaction count per user
    df['txn_count'] = df.groupby('user_id')['transaction_id'].transform('count')

    # 🔹 Feature 2: Average transaction amount per user
    df['avg_amount'] = df.groupby('user_id')['amount'].transform('mean')

    # 🔹 Feature 3: Time difference between transactions
    df['time_diff'] = df.groupby('user_id')['time'].diff().dt.seconds

    # Fill NaN (first transaction)
    df['time_diff'] = df['time_diff'].fillna(0)

    # 🔹 Feature 4: High amount flag (NumPy usage)
    df['high_amount'] = np.where(df['amount'] > 10000, 1, 0)

    # 🔹 Feature 5: Foreign transaction
    df['foreign_txn'] = np.where(df['location'] != "India", 1, 0)

    return df
