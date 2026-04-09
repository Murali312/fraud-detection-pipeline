from ingestion import load_data
from cleaning import clean_data
from feature_engineering import create_features

def run_pipeline(input_path, output_path):
    # Step 1: Load
    df = load_data(input_path)

    # Step 2: Clean
    df = clean_data(df)

    # Step 3: Feature Engineering
    df = create_features(df)

    # Save processed data
    df.to_csv(output_path, index=False)

    print("Pipeline executed successfully!")
